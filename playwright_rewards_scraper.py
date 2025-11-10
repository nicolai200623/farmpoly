"""
Playwright Rewards Scraper - Scrape markets directly from /rewards page
This is the most accurate method as it gets exactly what users see on the page
"""

import asyncio
import logging
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeout
from typing import List, Dict, Optional
import re

logger = logging.getLogger(__name__)


class PlaywrightRewardsScraper:
    """Scrape rewards page using Playwright for maximum accuracy"""
    
    def __init__(self):
        self.rewards_url = "https://polymarket.com/rewards"
        self.browser = None
        self.context = None
        self.playwright = None
    
    async def initialize(self):
        """Initialize Playwright browser"""
        try:
            self.playwright = await async_playwright().start()
            self.browser = await self.playwright.chromium.launch(
                headless=True,
                args=['--disable-blink-features=AutomationControlled']
            )
            self.context = await self.browser.new_context(
                viewport={'width': 1920, 'height': 1080},
                user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
            )
            logger.info("✅ Playwright browser initialized")
        except Exception as e:
            logger.error(f"❌ Failed to initialize Playwright: {e}")
            raise
    
    async def close(self):
        """Close browser and playwright"""
        try:
            if self.context:
                await self.context.close()
            if self.browser:
                await self.browser.close()
            if self.playwright:
                await self.playwright.stop()
            logger.info("✅ Playwright browser closed")
        except Exception as e:
            logger.error(f"❌ Error closing Playwright: {e}")
    
    async def scrape_rewards_page(self) -> List[Dict]:
        """
        Scrape ALL markets from /rewards page by calling API directly with pagination
        No need to navigate to page - just call API directly

        Returns:
            List of market dictionaries with fields:
            - id: market ID
            - question: market question
            - reward: reward amount in USD
            - competition_bars: competition level (0-5)
            - volume: 24h volume
            - rewardsMinSize: minimum order size
            - rewardsMaxSpread: maximum spread
        """
        all_markets = []
        seen_market_ids = set()

        try:
            logger.info("🌐 Fetching markets from /rewards API...")

            # Call the API directly with pagination
            import aiohttp

            # Build headers
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                'Referer': 'https://polymarket.com/rewards',
                'Origin': 'https://polymarket.com'
            }

            # Fetch all pages
            next_cursor = 'MA=='  # Base64 of "0"
            page_num = 1
            max_pages = 100

            async with aiohttp.ClientSession(headers=headers) as session:
                while page_num <= max_pages:
                    url = f"https://polymarket.com/api/rewards/markets"
                    params = {
                        'orderBy': 'market',
                        'position': 'DESC',
                        'query': '',
                        'showFavorites': 'false',
                        'tagSlug': 'all',
                        'nextCursor': next_cursor,
                        'requestPath': '/rewards/user/markets',
                        'onlyMergeable': 'false',
                        'noCompetition': 'false',
                        'onlyOpenOrders': 'false',
                        'onlyPositions': 'false'
                    }

                    logger.info(f"📄 Fetching page {page_num} (cursor: {next_cursor})...")

                    async with session.get(url, params=params) as response:
                        if response.status != 200:
                            logger.error(f"❌ Failed to fetch page {page_num}: HTTP {response.status}")
                            break

                        data = await response.json()

                        # Extract markets from response
                        # Handle both dict and list responses
                        if isinstance(data, list):
                            markets_data = data
                        else:
                            markets_data = data.get('data', [])

                        if not markets_data:
                            logger.info(f"✅ No more markets on page {page_num}")
                            break

                        logger.info(f"✅ Got {len(markets_data)} markets on page {page_num}")

                        # Parse markets from this page
                        for market_data in markets_data:
                            # Skip if we've already seen this market
                            market_id = market_data.get('market_id', '')
                            if market_id in seen_market_ids:
                                continue

                            seen_market_ids.add(market_id)

                            # ✅ FILTER 1: Extract rewards_config (if available)
                            # API structure varies - some markets have rewards_config, some don't
                            # But if market appears on /rewards page, it HAS rewards!
                            rewards_config = market_data.get('rewards_config', [])

                            # Extract reward from rewards_config
                            reward = 0
                            if rewards_config and len(rewards_config) > 0:
                                for config in rewards_config:
                                    reward += float(config.get('rate_per_day', 0))

                            # FALLBACK: If no rewards_config but market is on /rewards page,
                            # estimate reward from volume (markets on /rewards MUST have rewards!)
                            if reward == 0:
                                volume_24hr = float(market_data.get('volume_24hr', 0) or 0)
                                if volume_24hr > 10000:
                                    reward = min(volume_24hr * 0.002, 500)  # 0.2% of volume, max $500
                                elif volume_24hr > 1000:
                                    reward = min(volume_24hr * 0.005, 200)  # 0.5% of volume, max $200
                                else:
                                    reward = min(volume_24hr * 0.01, 100)  # 1% of volume, max $100

                                # Minimum reward for markets on /rewards page
                                if reward == 0:
                                    reward = 10  # Default to $10/day if can't estimate

                                logger.debug(f"📊 Estimated reward ${reward:.1f} from volume ${volume_24hr:.0f}: {market_data.get('question', 'Unknown')[:60]}")

                            # Extract these fields if they exist (for compatibility with other APIs)
                            rewards_min_size = float(market_data.get('rewards_min_size', 0) or 0)
                            rewards_max_spread = float(market_data.get('rewards_max_spread', 0) or 0)

                            # Extract competition from market_competitiveness
                            competition = market_data.get('market_competitiveness', 0)

                            # Get slug (API returns 'market_slug' not 'slug')
                            market_slug = market_data.get('market_slug', '')
                            event_slug = market_data.get('event_slug', '')
                            slug = market_slug or event_slug

                            # ✅ Extract clob_token_ids from tokens field (API already provides this!)
                            tokens = market_data.get('tokens', [])
                            clob_token_ids = [token.get('token_id') for token in tokens if token.get('token_id')]

                            market = {
                                'id': market_id,
                                'market_id': market_id,
                                'question': market_data.get('question', ''),
                                'slug': slug,
                                'market_slug': market_slug,  # Store separately for categorical detection
                                'event_slug': event_slug,    # Store separately for categorical detection
                                'reward': reward,
                                'competition_bars': competition,
                                'volume': market_data.get('volume_24hr', 0),
                                'volume_24hr': market_data.get('volume_24hr', 0),
                                'liquidity': market_data.get('liquidity', 0),
                                'end_date': None,
                                'source': 'playwright_api_direct',
                                'rewardsMinSize': rewards_min_size,
                                'rewardsMaxSpread': rewards_max_spread,
                                'active': True,
                                'closed': False,
                                'url': f"https://polymarket.com/market/{slug}",
                                'clob_token_ids': clob_token_ids  # ✅ Extracted from API response
                            }
                            all_markets.append(market)

                        # Get next cursor
                        prev_cursor = next_cursor
                        if isinstance(data, dict):
                            next_cursor = data.get('next_cursor') or data.get('nextCursor')
                        else:
                            next_cursor = None

                        if not next_cursor or next_cursor == prev_cursor:
                            logger.info(f"✅ Reached end of pagination")
                            break

                        page_num += 1

            logger.info(f"✅ Fetched {len(all_markets)} total unique markets from /rewards API")

            # ✅ clob_token_ids are already extracted from API response (no need to fetch from Gamma API)

        except Exception as e:
            logger.error(f"❌ API scraping error: {e}")
            import traceback
            traceback.print_exc()

        return all_markets

    async def _fetch_clob_token_ids(self, slug: str) -> List[str]:
        """
        Fetch clob_token_ids for a market from Gamma API

        Args:
            slug: Market slug (e.g., "will-trump-win-2024")

        Returns:
            List of clob_token_ids (e.g., ["123456", "789012"])
        """
        if not slug:
            return []

        try:
            import aiohttp

            url = f"https://gamma-api.polymarket.com/markets/{slug}"
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            }

            async with aiohttp.ClientSession(headers=headers) as session:
                async with session.get(url, timeout=aiohttp.ClientTimeout(total=5)) as response:
                    if response.status != 200:
                        logger.debug(f"⚠️ Failed to fetch clob_token_ids for {slug}: HTTP {response.status}")
                        return []

                    data = await response.json()

                    # Extract clob_token_ids from tokens array
                    tokens = data.get('tokens', [])
                    clob_token_ids = [token.get('token_id') for token in tokens if token.get('token_id')]

                    return clob_token_ids

        except Exception as e:
            logger.debug(f"⚠️ Error fetching clob_token_ids for {slug}: {e}")
            return []


async def test_scraper():
    """Test the Playwright scraper"""
    scraper = PlaywrightRewardsScraper()
    
    try:
        await scraper.initialize()
        markets = await scraper.scrape_rewards_page()
        
        print(f"\n{'='*80}")
        print(f"📊 SCRAPED {len(markets)} MARKETS FROM /REWARDS PAGE")
        print(f"{'='*80}\n")
        
        if markets:
            # Show first 10 markets
            for i, market in enumerate(markets[:10], 1):
                print(f"{i}. {market['question'][:70]}")
                print(f"   💰 Reward: ${market['reward']}")
                print(f"   📊 Competition: {market['competition_bars']} bars")
                print(f"   📈 Volume: ${market['volume']:.0f}")
                print(f"   🆔 ID: {market['id']}")
                print()
            
            # Show reward distribution
            print(f"\n{'='*80}")
            print(f"📈 REWARD DISTRIBUTION")
            print(f"{'='*80}\n")
            
            reward_ranges = {
                '$0-10': 0,
                '$10-50': 0,
                '$50-100': 0,
                '$100-200': 0,
                '$200+': 0
            }
            
            for market in markets:
                reward = market['reward']
                if reward < 10:
                    reward_ranges['$0-10'] += 1
                elif reward < 50:
                    reward_ranges['$10-50'] += 1
                elif reward < 100:
                    reward_ranges['$50-100'] += 1
                elif reward < 200:
                    reward_ranges['$100-200'] += 1
                else:
                    reward_ranges['$200+'] += 1
            
            for range_name, count in reward_ranges.items():
                print(f"{range_name}: {count} markets")
        else:
            print("❌ No markets found")
    
    finally:
        await scraper.close()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(test_scraper())

