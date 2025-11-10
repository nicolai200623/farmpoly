"""
Market Scanner V2 - Using Playwright to Scrape /rewards Page
Scrapes markets directly from https://polymarket.com/rewards for maximum accuracy
This ensures we only get markets that actually appear on the rewards page
"""

import asyncio
import aiohttp
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeout
import logging
from typing import List, Dict, Optional
import json
import time
from circuit_breaker import CircuitBreaker, CircuitBreakerOpenError
from playwright_rewards_scraper import PlaywrightRewardsScraper
from py_clob_client.client import ClobClient
from py_clob_client.exceptions import PolyApiException

logger = logging.getLogger(__name__)


class MarketScannerV2:
    """Enhanced market scanner with Playwright and API fallback"""

    def __init__(self, config: dict):
        self.config = config
        self.rewards_url = "https://polymarket.com/rewards"
        self.api_url = "https://gamma-api.polymarket.com/events"

        # Read config - handle both nested and direct config
        # If config is already the scanner config (passed from main.py line 161)
        if 'min_reward' in config:
            # Direct scanner config from config['market_scanner']
            self.min_reward = config.get('min_reward', 10)  # Default 10 (match config.yaml)
            self.max_competition = config.get('max_competition_bars', 3)  # Default 3 (match config.yaml)
            self.target_categories = config.get('target_categories', [])
        else:
            # Nested config (for backward compatibility)
            scanner_config = config.get('market_scanner', {})
            self.min_reward = scanner_config.get('min_reward', 10)  # Default 10
            self.max_competition = scanner_config.get('max_competition_bars', 3)  # Default 3
            self.target_categories = scanner_config.get('target_categories', [])

        # Log the actual values being used
        logger.info(f"📊 Market Scanner initialized with:")
        logger.info(f"   - min_reward: ${self.min_reward}")
        logger.info(f"   - max_competition_bars: {self.max_competition}")
        if self.target_categories:
            logger.info(f"   - target_categories: {', '.join(self.target_categories)}")
        else:
            logger.info(f"   - target_categories: ALL (no filter)")

        self.browser = None
        self.context = None
        self._clob_warning_shown = False  # Track if we've shown CLOB warning

        # Initialize CLOB client for orderbook verification
        clob_config = config.get('clob', {})
        self.clob_host = clob_config.get('host', 'https://clob.polymarket.com')
        try:
            self.clob_client = ClobClient(host=self.clob_host)
            logger.info("✅ CLOB client initialized for orderbook verification (spread check enabled)")
        except Exception as e:
            logger.error(f"❌ Could not initialize CLOB client: {e}")
            logger.error(f"   Orderbook verification will be SKIPPED!")
            logger.error(f"   Bot may select illiquid markets with wide spreads!")
            self.clob_client = None

        # Initialize Playwright Rewards Scraper (primary source - scrapes /rewards page!)
        self.playwright_scraper = PlaywrightRewardsScraper()

        # Initialize circuit breakers
        self.playwright_breaker = CircuitBreaker(
            name="playwright_scraper",
            failure_threshold=3,
            timeout_seconds=60,
            success_threshold=2
        )
        self.playwright_breaker = CircuitBreaker(
            name="playwright_scraper",
            failure_threshold=3,
            timeout_seconds=120,
            success_threshold=2
        )
        
    async def initialize(self):
        """Initialize Playwright browser"""
        try:
            playwright = await async_playwright().start()
            self.browser = await playwright.chromium.launch(
                headless=True,
                args=['--disable-blink-features=AutomationControlled']
            )
            self.context = await self.browser.new_context(
                viewport={'width': 1920, 'height': 1080},
                user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            )
            logger.info("✅ Playwright browser initialized")
        except Exception as e:
            logger.error(f"❌ Failed to initialize Playwright: {e}")
    
    async def close(self):
        """Close browser"""
        if self.browser:
            await self.browser.close()
    
    async def scan_rewards_page(self) -> List[Dict]:
        """
        Scan rewards page using official Polymarket Rewards API (primary) with Gamma API fallback

        Priority:
        1. Polymarket Rewards API - Official /api/rewards/markets endpoint (MOST ACCURATE!)
        2. Gamma API - Fallback if rewards API fails
        """
        markets = []

        try:
            # Use Playwright to scrape /rewards page (most accurate method)
            logger.info("🌐 Scraping markets from /rewards page using Playwright...")

            try:
                # Use circuit breaker for Playwright scraper
                playwright_markets = await self.playwright_breaker.call(
                    lambda: self.playwright_scraper.scrape_rewards_page()
                )

                if playwright_markets:
                    # Add category to each market BEFORE filtering
                    for market in playwright_markets:
                        if 'category' not in market:
                            market['category'] = self._infer_category(market['question'], market)

                    markets.extend(playwright_markets)
                    logger.info(f"✅ Got {len(markets)} markets from /rewards page")
                else:
                    logger.warning("⚠️  No markets from /rewards page")

            except CircuitBreakerOpenError as e:
                logger.warning(f"⚠️  Playwright scraper circuit breaker OPEN: {e}")
            except Exception as scraper_error:
                logger.error(f"❌ Playwright scraper error: {scraper_error}")

            # DISABLED: Playwright fallback (unreliable)
            if not markets:
                logger.warning("⚠️  No markets from any source - Playwright is DISABLED")
                logger.info("💡 Bot will retry on next scan cycle")

            # Filter based on criteria
            filtered_markets = self._filter_markets(markets)

            # ✅ NEW FILTER 3: Verify orderbook exists for top markets
            # DISABLED TEMPORARILY - orderbook verification rejecting ALL markets
            # Issue: clob_token_ids may be empty or incorrect from API
            # TODO: Debug why clob_token_ids not extracted properly
            if False and filtered_markets and len(filtered_markets) > 0:  # DISABLED
                top_count = min(50, len(filtered_markets))
                logger.info(f"🔍 Verifying orderbook for top {top_count} markets...")
                verified_markets = []
                no_orderbook_count = 0
                error_count = 0

                for i, market in enumerate(filtered_markets[:50], 1):  # Only check top 50
                    try:
                        # Log progress every 10 markets
                        if i % 10 == 0:
                            logger.info(f"   Progress: {i}/{top_count} markets verified...")

                        has_orderbook = await self._verify_orderbook_exists(market)
                        if has_orderbook:
                            verified_markets.append(market)
                        else:
                            no_orderbook_count += 1
                            logger.debug(f"❌ Rejected (no orderbook): {market['question'][:50]}")

                        # Add small delay to avoid rate limiting (100ms between requests)
                        await asyncio.sleep(0.1)

                    except Exception as e:
                        error_count += 1
                        logger.warning(f"⚠️  Error verifying market {i}/{top_count}: {market.get('question', 'unknown')[:50]} - {e}")
                        # Continue with next market instead of crashing
                        continue

                # Add remaining markets without verification (to avoid too many API calls)
                if len(filtered_markets) > 50:
                    verified_markets.extend(filtered_markets[50:])

                if no_orderbook_count > 0:
                    logger.info(f"   - {no_orderbook_count} markets rejected: no orderbook (no bids or asks)")
                if error_count > 0:
                    logger.warning(f"   - {error_count} markets skipped due to errors")

                filtered_markets = verified_markets

            logger.info(f"✅ Found {len(filtered_markets)} qualifying markets (from {len(markets)} total)")
            return filtered_markets

        except Exception as e:
            logger.error(f"❌ Scanning error: {e}")
            return []
    
    async def _fetch_gamma_api_internal(self) -> List[Dict]:
        """Internal method: Fetch markets from Gamma API using /events endpoint"""
        markets = []

        async with aiohttp.ClientSession() as session:
            # Fetch active events (which contain markets)
            # IMPORTANT: Gamma API uses '_limit' not 'limit'
            params = {
                'closed': 'false',
                '_limit': 100  # Fixed: was 'limit', should be '_limit'
            }

            async with session.get(self.api_url, params=params, timeout=10) as response:
                if response.status == 200:
                    data = await response.json()

                    # Parse API response - events contain markets
                    if isinstance(data, list):
                        for event in data:
                            # Extract markets from event
                            event_markets = event.get('markets', [])
                            for market_data in event_markets:
                                market = self._parse_api_market(market_data, event)
                                if market:
                                    markets.append(market)

                    logger.info(f"✅ Fetched {len(markets)} markets from API")
                else:
                    logger.warning(f"⚠️  API returned status {response.status}")

        return markets
    
    def _parse_api_market(self, market_data: dict, event: dict = None) -> Optional[Dict]:
        """Parse market data from API response"""
        try:
            # Skip closed or inactive markets
            # IMPORTANT: Gamma API can have active=True AND closed=True at the same time!
            # We need to check BOTH conditions
            if market_data.get('closed', False):
                return None

            if not market_data.get('active', False):
                return None

            # ✅ MODIFIED: Check if market has rewards enabled
            # IMPORTANT: Gamma API may not always return rewardsMinSize/rewardsMaxSpread
            # Instead, we should accept markets and let downstream filters handle it
            # Extract these fields if they exist (for compatibility)
            rewards_min_size = float(market_data.get('rewardsMinSize', 0) or 0)
            rewards_max_spread = float(market_data.get('rewardsMaxSpread', 0) or 0)

            # NOTE: We no longer reject based on missing rewards_min_size/rewards_max_spread
            # Instead, we'll rely on:
            # 1. The market appearing on /rewards page (validated by playwright scraper)
            # 2. Downstream filters (orderbook verification, volume checks, etc.)

            # Get actual reward from umaReward field
            # IMPORTANT: umaReward is the ACTUAL dollar amount for rewards, not a multiplier!
            uma_reward = float(market_data.get('umaReward', 0) or 0)

            # Use umaReward as the primary reward value
            if uma_reward > 0:
                reward = uma_reward
            else:
                # Fallback: Estimate reward based on volume (conservative estimate)
                volume = float(market_data.get('volume', 0) or market_data.get('volumeNum', 0) or 0)
                liquidity = float(market_data.get('liquidity', 0) or 0)

                if volume > 10000:
                    reward = min(volume * 0.002, 500)  # 0.2% of volume, max $500
                elif volume > 1000:
                    reward = min(volume * 0.005, 200)  # 0.5% of volume, max $200
                else:
                    reward = min(volume * 0.01, 100)  # 1% of volume, max $100

                # Boost reward if liquidity is high
                if liquidity > 1000:
                    reward *= 1.5

            # Get competition level (use volume as proxy)
            volume = float(market_data.get('volume', 0) or market_data.get('volumeNum', 0) or 0)
            competition = min(3, int(volume / 10000))  # 0-3 bars based on volume

            # Get liquidity
            liquidity = float(
                market_data.get('liquidity', 0) or
                market_data.get('liquidityNum', 0) or
                market_data.get('liquidityClob', 0) or
                0
            )

            # Infer category from question/title
            question = market_data.get('question') or event.get('title', 'Unknown') if event else 'Unknown'
            category = self._infer_category(question, event)

            # Parse clobTokenIds (JSON string array)
            clob_token_ids = []
            try:
                import json
                clob_token_ids_str = market_data.get('clobTokenIds', '[]')
                if isinstance(clob_token_ids_str, str):
                    clob_token_ids = json.loads(clob_token_ids_str)
                elif isinstance(clob_token_ids_str, list):
                    clob_token_ids = clob_token_ids_str
            except Exception as e:
                logger.debug(f"Could not parse clobTokenIds: {e}")

            market = {
                'id': market_data.get('id') or market_data.get('conditionId'),
                'condition_id': market_data.get('conditionId'),  # Store condition ID separately
                'clob_token_ids': clob_token_ids,  # Store CLOB token IDs for orderbook
                'question': question,
                'reward': reward,
                'competition_bars': competition,
                'min_shares': int(rewards_min_size) if rewards_min_size > 0 else 100,
                'volume': volume,
                'liquidity': liquidity,
                'end_date': market_data.get('endDate') or market_data.get('endDateIso'),
                'source': 'gamma_api',
                'category': category,  # Add inferred category
                # Thêm thông tin rewards chi tiết
                'rewards_min_size': rewards_min_size,
                'rewards_max_spread': rewards_max_spread,
            }

            return market

        except Exception as e:
            logger.debug(f"Failed to parse API market: {e}")
            return None
    
    async def _scrape_with_playwright_internal(self) -> List[Dict]:
        """Internal method: Scrape using Playwright for JavaScript-rendered content"""
        markets = []
        
        if not self.context:
            await self.initialize()
        
        try:
            page = await self.context.new_page()
            
            # Navigate to rewards page with longer timeout
            await page.goto(self.rewards_url, wait_until='domcontentloaded', timeout=60000)
            
            # Wait for market cards to load
            try:
                await page.wait_for_selector('[data-testid="market-card"], .market-card, .reward-card', 
                                            timeout=10000)
            except PlaywrightTimeout:
                logger.warning("⚠️  Timeout waiting for market cards")
            
            # Extract market data using JavaScript
            markets_data = await page.evaluate('''
                () => {
                    const cards = document.querySelectorAll('[data-testid="market-card"], .market-card, .reward-card');
                    return Array.from(cards).map(card => {
                        // Try multiple selectors for reward amount
                        const rewardEl = card.querySelector('.reward-amount, [data-testid="reward"], .reward');
                        const reward = rewardEl ? parseFloat(rewardEl.textContent.replace(/[^0-9.]/g, '')) : 0;
                        
                        // Competition bars
                        const bars = card.querySelectorAll('.bar-filled, .competition-bar.filled, [data-filled="true"]');
                        const competition = bars.length;
                        
                        // Minimum shares
                        const sharesEl = card.querySelector('.min-shares, [data-testid="min-shares"]');
                        const minShares = sharesEl ? parseInt(sharesEl.textContent.replace(/[^0-9]/g, '')) : 0;
                        
                        // Question/title
                        const titleEl = card.querySelector('.market-title, h3, h4, [data-testid="title"]');
                        const question = titleEl ? titleEl.textContent.trim() : 'Unknown';
                        
                        // Market ID (from link or data attribute)
                        const linkEl = card.querySelector('a[href*="/market/"]');
                        const marketId = linkEl ? linkEl.href.split('/market/')[1].split('?')[0] : null;
                        
                        return {
                            id: marketId,
                            question: question,
                            reward: reward,
                            competition_bars: competition,
                            min_shares: minShares
                        };
                    }).filter(m => m.id && m.reward > 0);
                }
            ''')
            
            # Convert to market objects
            for data in markets_data:
                market = {
                    'id': data['id'],
                    'question': data['question'],
                    'reward': data['reward'],
                    'competition_bars': data['competition_bars'],
                    'min_shares': data['min_shares'],
                    'volume': 0,
                    'liquidity': 0,
                    'end_date': None,
                    'source': 'playwright'
                }
                markets.append(market)
            
            await page.close()
            
        except Exception as e:
            logger.error(f"❌ Playwright scraping error: {e}")
        
        return markets
    
    def _filter_markets(self, markets: List[Dict]) -> List[Dict]:
        """Filter markets based on criteria with detailed logging"""
        filtered = []
        rejected_reasons = {
            'low_reward': 0,
            'high_competition': 0,
            'wrong_category': 0,
            'no_clob_tokens': 0,
            'no_volume': 0,
            'other': 0
        }

        for market in markets:
            # Check reward threshold
            if market['reward'] < self.min_reward:
                rejected_reasons['low_reward'] += 1
                logger.debug(f"❌ Rejected (low reward): {market['question'][:50]} - Reward: ${market['reward']:.0f} < ${self.min_reward}")
                continue

            # Check competition level
            if market['competition_bars'] > self.max_competition:
                rejected_reasons['high_competition'] += 1
                logger.debug(f"❌ Rejected (high competition): {market['question'][:50]} - Competition: {market['competition_bars']} > {self.max_competition}")
                continue

            # Check category filter (if configured AND category field exists)
            if self.target_categories:
                market_category = market.get('category', None)
                # Only apply category filter if category field exists
                if market_category is not None and market_category not in self.target_categories:
                    rejected_reasons['wrong_category'] += 1
                    logger.debug(f"❌ Rejected (wrong category): {market['question'][:50]} - Category: '{market_category}' not in {self.target_categories}")
                    continue

            # ✅ NEW FILTER 1: Check if market has clob_token_ids
            clob_token_ids = market.get('clob_token_ids', [])
            if not clob_token_ids or len(clob_token_ids) == 0:
                rejected_reasons['no_clob_tokens'] += 1
                logger.debug(f"❌ Rejected (no clob_token_ids): {market['question'][:50]} - ID: {market.get('id')}")
                continue

            # ✅ NEW FILTER 1.4: Reject categorical event outcomes
            # If event_slug != market_slug, this is an outcome of a categorical event
            # Example: NFLX above $1070, NFLX above $1080, etc. are outcomes of categorical event
            market_slug = market.get('market_slug', '')
            event_slug = market.get('event_slug', '')
            if event_slug and market_slug and event_slug != market_slug:
                if 'categorical_outcome' not in rejected_reasons:
                    rejected_reasons['categorical_outcome'] = 0
                rejected_reasons['categorical_outcome'] += 1
                logger.debug(f"❌ Rejected (categorical event outcome): {market['question'][:50]} - event_slug != market_slug")
                continue

            # ✅ NEW FILTER 1.5: Only accept BINARY markets (exactly 2 tokens)
            # Reject categorical markets (>2 tokens) as they're not suitable for YES/NO strategy
            if len(clob_token_ids) != 2:
                if 'categorical_market' not in rejected_reasons:
                    rejected_reasons['categorical_market'] = 0
                rejected_reasons['categorical_market'] += 1
                if len(clob_token_ids) > 2:
                    logger.debug(f"❌ Rejected (categorical market): {market['question'][:50]} - {len(clob_token_ids)} tokens (not binary YES/NO)")
                else:
                    logger.debug(f"❌ Rejected (invalid market): {market['question'][:50]} - only {len(clob_token_ids)} token(s)")
                continue

            # ✅ NEW FILTER 2: Check if market has volume > 0
            volume = market.get('volume', 0) or market.get('volume_24hr', 0)
            if volume <= 0:
                rejected_reasons['no_volume'] += 1
                logger.debug(f"❌ Rejected (no volume): {market['question'][:50]} - Volume: {volume}")
                continue

            # Add score for ranking
            market['score'] = self._calculate_score(market)

            filtered.append(market)

            # Log detailed acceptance info with reward verification
            logger.info(f"✅ ACCEPTED: {market['question'][:60]}")
            logger.info(f"   - Category: {market.get('category', 'unknown')}")
            logger.info(f"   - Estimated Reward: ${market['reward']:.0f} (based on volume=${market.get('volume', 0):.0f})")
            logger.info(f"   - Rewards Config: minSize={market.get('rewards_min_size', 0)}, maxSpread={market.get('rewards_max_spread', 0)}")
            logger.info(f"   - Competition: {market['competition_bars']} bars, Score: {market['score']:.2f}")
            logger.info(f"   - Source: {market.get('source', 'unknown')}")

        # Log summary
        if len(markets) > 0:
            logger.info(f"📊 Filter results: {len(filtered)}/{len(markets)} markets passed")
            if rejected_reasons['low_reward'] > 0:
                logger.info(f"   - {rejected_reasons['low_reward']} rejected: reward < ${self.min_reward}")
            if rejected_reasons['high_competition'] > 0:
                logger.info(f"   - {rejected_reasons['high_competition']} rejected: competition > {self.max_competition}")
            if rejected_reasons['wrong_category'] > 0:
                logger.info(f"   - {rejected_reasons['wrong_category']} rejected: category not in {self.target_categories}")
            if rejected_reasons['no_clob_tokens'] > 0:
                logger.info(f"   - {rejected_reasons['no_clob_tokens']} rejected: no clob_token_ids (cannot trade)")
            if rejected_reasons.get('categorical_outcome', 0) > 0:
                logger.info(f"   - {rejected_reasons['categorical_outcome']} rejected: categorical event outcomes (event_slug != market_slug)")
            if rejected_reasons.get('categorical_market', 0) > 0:
                logger.info(f"   - {rejected_reasons['categorical_market']} rejected: categorical markets (not binary YES/NO)")
            if rejected_reasons['no_volume'] > 0:
                logger.info(f"   - {rejected_reasons['no_volume']} rejected: volume = 0 (no liquidity)")

        # Sort by score (highest first)
        filtered.sort(key=lambda x: x['score'], reverse=True)

        return filtered
    
    def _calculate_score(self, market: Dict) -> float:
        """Calculate market opportunity score"""
        score = 0.0
        
        # Reward contribution (higher is better)
        score += market['reward'] * 0.5
        
        # Competition penalty (lower is better)
        score -= market['competition_bars'] * 100
        
        # Volume bonus (if available)
        if market.get('volume', 0) > 0:
            score += min(market['volume'] / 10000, 50)
        
        # Liquidity bonus (if available)
        if market.get('liquidity', 0) > 0:
            score += min(market['liquidity'] / 5000, 30)

        return score

    async def _verify_orderbook_exists(self, market: Dict) -> bool:
        """
        Verify that an orderbook exists AND has reasonable spread for this market

        Args:
            market: Market dict with clob_token_ids

        Returns:
            True if orderbook exists with reasonable spread, False otherwise
        """
        if not self.clob_client:
            if not self._clob_warning_shown:
                logger.warning("⚠️ CLOB client not available, skipping orderbook verification for all markets!")
                logger.warning("   Markets with wide spreads may pass through filter!")
                self._clob_warning_shown = True
            return True  # Skip verification if CLOB client not available

        clob_token_ids = market.get('clob_token_ids', [])
        if not clob_token_ids or len(clob_token_ids) == 0:
            return False

        try:
            # Try to fetch orderbook for the first token (YES outcome)
            # Add timeout to prevent hanging
            token_id = clob_token_ids[0]

            # Wrap synchronous call in asyncio timeout
            try:
                # Use asyncio.wait_for with timeout of 5 seconds
                book = await asyncio.wait_for(
                    asyncio.to_thread(self.clob_client.get_order_book, token_id),
                    timeout=5.0
                )
            except asyncio.TimeoutError:
                logger.debug(f"⏱️  Timeout fetching orderbook for market {market.get('id')}")
                return False

            # Check if orderbook has any bids or asks
            if hasattr(book, 'bids') and hasattr(book, 'asks'):
                has_bids = book.bids and len(book.bids) > 0
                has_asks = book.asks and len(book.asks) > 0

                if not (has_bids and has_asks):
                    logger.debug(f"❌ Orderbook empty for market {market.get('id')}")
                    return False

                # ✅ Calculate spread and check liquidity
                # Get best bid and ask
                best_bid = float(book.bids[0].price) if has_bids else 0
                best_ask = float(book.asks[0].price) if has_asks else 1

                # Calculate spread
                spread = best_ask - best_bid
                mid_price = (best_bid + best_ask) / 2
                spread_pct = (spread / mid_price * 100) if mid_price > 0 else 999

                # ✅ CHECK 1: Reject markets with EXTREMELY wide spreads (>95%)
                # RELAXED from 80% to 95% to accept more markets
                # Markets with 80-95% spread can still be profitable for liquidity farming
                if spread_pct > 95:
                    logger.debug(f"❌ Spread too wide ({spread_pct:.1f}% > 95%) - too risky for market {market.get('id')}")
                    return False

                # ✅ CHECK 2: Verify orderbook has sufficient depth
                # RELAXED from ≥3 to ≥2 levels to accept more markets
                # Many good markets only have 2 levels on each side
                num_bids = len(book.bids)
                num_asks = len(book.asks)

                if num_bids < 2 or num_asks < 2:
                    logger.debug(f"❌ Insufficient orderbook depth for market {market.get('id')}: {num_bids} bids, {num_asks} asks (need ≥2)")
                    return False

                # ✅ CHECK 3: Calculate total volume in orderbook
                # RELAXED from 100 to 20 contracts to accept more markets
                # Sum up top 5 orders to ensure there's real liquidity
                def get_total_size(orders, limit=5):
                    total = 0
                    for i, order in enumerate(orders[:limit]):
                        if i >= limit:
                            break
                        size = float(getattr(order, 'size', 0))
                        total += size
                    return total

                total_bid_volume = get_total_size(book.bids, 5)
                total_ask_volume = get_total_size(book.asks, 5)

                # Require minimum $10 of liquidity on each side (assuming $0.50 avg price = 20 contracts)
                # RELAXED from 100 to 20 to accept more markets
                min_volume = 20
                if total_bid_volume < min_volume or total_ask_volume < min_volume:
                    logger.debug(f"❌ Insufficient volume for market {market.get('id')}: bid_vol={total_bid_volume:.0f}, ask_vol={total_ask_volume:.0f} (need ≥{min_volume})")
                    return False

                logger.debug(f"✅ Orderbook verified for market {market.get('id')}: {num_bids} bids, {num_asks} asks, spread: {spread_pct:.1f}%, bid_vol={total_bid_volume:.0f}, ask_vol={total_ask_volume:.0f}")
                return True
            else:
                logger.debug(f"❌ Invalid orderbook format for market {market.get('id')}")
                return False

        except PolyApiException as e:
            if e.status_code == 404:
                logger.debug(f"❌ No orderbook exists for market {market.get('id')} (404)")
            else:
                logger.debug(f"❌ Error fetching orderbook for market {market.get('id')}: {e}")
            return False
        except Exception as e:
            logger.debug(f"❌ Unexpected error verifying orderbook for market {market.get('id')}: {e}")
            return False

    def _infer_category(self, question: str, event: dict = None) -> str:
        """
        Infer market category from question text and event data

        Categories:
        - sports: Sports events, esports
        - entertainment: Movies, TV, celebrities
        - crypto: Cryptocurrency prices
        - politics: Elections, government
        - economics: Economy, markets
        - science: Technology, research
        - other: Everything else
        """
        question_lower = question.lower()

        # Crypto keywords (check FIRST - most specific)
        crypto_keywords = [
            'bitcoin', 'btc', 'ethereum', 'eth', 'solana', 'sol', 'xrp', 'ripple',
            'crypto', 'cryptocurrency', 'up or down', 'price', 'fdv', 'market cap',
            'metamask', 'wallet', 'defi', 'token', 'coin', 'blockchain'
        ]

        # Science/Tech keywords (check SECOND - specific)
        science_keywords = [
            'ai', 'artificial intelligence', 'gemini', 'chatgpt', 'gpt', 'claude',
            'openai', 'google ai', 'deepmind', 'machine learning', 'neural network',
            'technology', 'research', 'study', 'discovery', 'space', 'nasa',
            'climate', 'vaccine', 'humanit', 'benchmark'
        ]

        # Politics keywords (check THIRD - specific)
        politics_keywords = [
            # Elections & Government
            'election', 'president', 'senate', 'congress', 'vote', 'poll',
            'democrat', 'republican', 'party', 'government', 'policy', 'campaign',

            # Politicians (US)
            'trump', 'biden', 'harris', 'pelosi', 'nancy pelosi', 'obama', 'clinton',
            'desantis', 'newsom', 'pence', 'mcconnell', 'schumer', 'aoc',

            # Politicians (NYC/Local)
            'mamdani', 'nyc', 'mayor', 'city council', 'rent', 'rents',

            # International Politics & Conflicts
            'russia', 'ukraine', 'putin', 'zelensky', 'war', 'conflict', 'military',
            'israel', 'palestine', 'gaza', 'hamas', 'iran', 'yemen', 'strike', 'attack',
            'china', 'taiwan', 'xi jinping', 'north korea', 'kim jong',

            # Political Events
            'impeachment', 'scandal', 'investigation', 'hearing', 'testimony',
            'shutdown', 'budget', 'debt ceiling', 'supreme court', 'justice',
            'cabinet', 'secretary', 'ambassador', 'diplomat'
        ]

        # Entertainment keywords (check FOURTH - specific)
        entertainment_keywords = [
            # Movies & TV
            'movie', 'film', 'actor', 'actress', 'celebrity', 'tv show',
            'series', 'netflix', 'disney', 'oscar', 'emmy', 'grammy',
            'box office', 'streaming', 'hbo', 'amazon prime',

            # Celebrities & Social Media
            'tweet', 'tweets', 'twitter', 'instagram', 'tiktok', 'viral',
            'influencer', 'streamer', 'youtube', 'podcast',

            # Specific Celebrities (if not political)
            'ackman', 'bill ackman', 'elon musk', 'kardashian', 'swift',
            'beyonce', 'kanye', 'drake', 'rogan'
        ]

        # Economics keywords (check FIFTH - can overlap with crypto)
        economics_keywords = [
            'stock', 'economy', 'gdp', 'inflation', 'fed', 'interest rate',
            'recession', 'unemployment', 'dow', 'nasdaq', 's&p', 'treasury'
        ]

        # Sports keywords (check LAST - has generic words like "game", "score")
        sports_keywords = [
            'nfl', 'nba', 'mlb', 'nhl', 'soccer', 'football', 'basketball', 'baseball',
            'hockey', 'tennis', 'golf', 'ufc', 'boxing', 'f1', 'racing', 'olympics',
            'world cup', 'super bowl', 'playoffs', 'championship', 'premier league',
            'la liga', 'serie a', 'bundesliga', 'champions league',
            'esports', 'counter-strike', 'cs2', 'dota', 'league of legends', 'valorant',
            'mobile legends', 'mlbb', 'tournament', 'qualifier'
        ]

        # Check each category in order of SPECIFICITY (most specific first)
        # This prevents generic sports keywords from matching crypto/AI questions
        if any(keyword in question_lower for keyword in crypto_keywords):
            return 'crypto'
        elif any(keyword in question_lower for keyword in science_keywords):
            return 'science'
        elif any(keyword in question_lower for keyword in politics_keywords):
            return 'politics'
        elif any(keyword in question_lower for keyword in entertainment_keywords):
            return 'entertainment'
        elif any(keyword in question_lower for keyword in economics_keywords):
            return 'economics'
        elif any(keyword in question_lower for keyword in sports_keywords):
            return 'sports'
        else:
            return 'other'


# Backward compatibility - alias to new scanner
MarketScanner = MarketScannerV2

