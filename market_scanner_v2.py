"""
Market Scanner V2 - Upgraded with Playwright + Gamma API
Replaces fragile Selenium scraper with robust multi-source approach
"""

import asyncio
import aiohttp
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeout
import logging
from typing import List, Dict, Optional
import json
import time
from circuit_breaker import CircuitBreaker, CircuitBreakerOpenError

logger = logging.getLogger(__name__)


class MarketScannerV2:
    """Enhanced market scanner with Playwright and API fallback"""

    def __init__(self, config: dict):
        self.config = config
        self.rewards_url = "https://polymarket.com/rewards"
        self.api_url = "https://gamma-api.polymarket.com/events"
        self.min_reward = config.get('min_reward', 300)
        self.max_competition = config.get('max_competition_bars', 2)
        self.browser = None
        self.context = None

        # Initialize circuit breakers
        self.api_breaker = CircuitBreaker(
            name="gamma_api",
            failure_threshold=5,
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
        """Scan rewards page using multiple sources with circuit breaker protection"""
        markets = []

        try:
            # Method 1: Try Gamma API first (fastest and most reliable)
            logger.info("🔍 Fetching from Gamma API...")

            try:
                # Use circuit breaker for API calls
                api_markets = await self.api_breaker.call(self._fetch_gamma_api_internal)

                if api_markets:
                    markets.extend(api_markets)
                    logger.info(f"✅ Got {len(api_markets)} markets from API")
                else:
                    logger.warning("⚠️  No markets from API")

            except CircuitBreakerOpenError as e:
                logger.warning(f"⚠️  API circuit breaker OPEN: {e}")
            except Exception as api_error:
                logger.error(f"❌ API error: {api_error}")

            # Method 2: Fallback to Playwright scraping if API didn't return markets
            if not markets:
                logger.warning("⚠️  Trying Playwright scraping...")
                try:
                    scraped_markets = await self.playwright_breaker.call(self._scrape_with_playwright_internal)
                    markets.extend(scraped_markets)
                except CircuitBreakerOpenError as e:
                    logger.warning(f"⚠️  Playwright circuit breaker OPEN: {e}")
                except Exception as scrape_error:
                    logger.error(f"❌ Playwright scraping failed: {scrape_error}")

            # Filter based on criteria
            filtered_markets = self._filter_markets(markets)

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
            params = {
                'closed': 'false',
                'order': 'id',
                'ascending': 'false',
                'limit': 100
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
            # Check if market has rewards enabled
            rewards_min_size = float(market_data.get('rewardsMinSize', 0) or 0)
            rewards_max_spread = float(market_data.get('rewardsMaxSpread', 0) or 0)
            uma_reward = float(market_data.get('umaReward', 0) or 0)

            # Skip markets without ANY rewards indicators
            # Accept if ANY of these conditions is true:
            # 1. rewardsMinSize > 0 (có yêu cầu minimum size)
            # 2. rewardsMaxSpread > 0 (có giới hạn spread)
            # 3. umaReward > 0 (có UMA reward)
            if rewards_min_size == 0 and rewards_max_spread == 0 and uma_reward == 0:
                return None

            # Calculate estimated reward (improved calculation)
            # Sử dụng rewardsMinSize hoặc volume để ước tính
            if rewards_min_size > 0:
                reward = rewards_min_size * 10  # Rough estimate based on min size
            elif uma_reward > 0:
                reward = uma_reward * 100  # UMA rewards are typically smaller
            else:
                # Fallback: estimate from volume
                volume = float(market_data.get('volume', 0) or market_data.get('volumeNum', 0) or 0)
                reward = min(volume * 0.001, 1000)  # 0.1% of volume, max $1000

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
                'uma_reward': uma_reward,
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

            # Add score for ranking
            market['score'] = self._calculate_score(market)

            filtered.append(market)
            logger.debug(f"✅ Accepted: {market['question'][:50]} - Reward: ${market['reward']:.0f}, Competition: {market['competition_bars']}, Score: {market['score']:.1f}")

        # Log summary
        if len(markets) > 0:
            logger.info(f"📊 Filter results: {len(filtered)}/{len(markets)} markets passed")
            if rejected_reasons['low_reward'] > 0:
                logger.info(f"   - {rejected_reasons['low_reward']} rejected: reward < ${self.min_reward}")
            if rejected_reasons['high_competition'] > 0:
                logger.info(f"   - {rejected_reasons['high_competition']} rejected: competition > {self.max_competition}")

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

        # Sports keywords
        sports_keywords = [
            'nfl', 'nba', 'mlb', 'nhl', 'soccer', 'football', 'basketball', 'baseball',
            'hockey', 'tennis', 'golf', 'ufc', 'boxing', 'f1', 'racing', 'olympics',
            'world cup', 'super bowl', 'playoffs', 'championship', 'league',
            'esports', 'counter-strike', 'cs2', 'dota', 'league of legends', 'valorant',
            'mobile legends', 'mlbb', 'team', 'match', 'game', 'vs', 'win', 'score'
        ]

        # Crypto keywords
        crypto_keywords = [
            'bitcoin', 'btc', 'ethereum', 'eth', 'solana', 'sol', 'xrp', 'ripple',
            'crypto', 'cryptocurrency', 'up or down', 'price', 'trading'
        ]

        # Politics keywords
        politics_keywords = [
            'election', 'president', 'senate', 'congress', 'vote', 'poll',
            'democrat', 'republican', 'party', 'government', 'policy'
        ]

        # Entertainment keywords
        entertainment_keywords = [
            'movie', 'film', 'actor', 'actress', 'celebrity', 'tv show',
            'series', 'netflix', 'disney', 'oscar', 'emmy', 'grammy'
        ]

        # Economics keywords
        economics_keywords = [
            'stock', 'market', 'economy', 'gdp', 'inflation', 'fed', 'interest rate',
            'recession', 'unemployment', 'dow', 'nasdaq', 's&p'
        ]

        # Science keywords
        science_keywords = [
            'technology', 'ai', 'artificial intelligence', 'research', 'study',
            'discovery', 'space', 'nasa', 'climate', 'vaccine'
        ]

        # Check each category
        if any(keyword in question_lower for keyword in sports_keywords):
            return 'sports'
        elif any(keyword in question_lower for keyword in crypto_keywords):
            return 'crypto'
        elif any(keyword in question_lower for keyword in politics_keywords):
            return 'politics'
        elif any(keyword in question_lower for keyword in entertainment_keywords):
            return 'entertainment'
        elif any(keyword in question_lower for keyword in economics_keywords):
            return 'economics'
        elif any(keyword in question_lower for keyword in science_keywords):
            return 'science'
        else:
            return 'other'


# Backward compatibility - alias to new scanner
MarketScanner = MarketScannerV2

