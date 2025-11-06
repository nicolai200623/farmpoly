"""
Web Rewards Scraper
Scrapes markets directly from https://polymarket.com/rewards
This is the OFFICIAL source of truth for which markets have rewards.
"""

import asyncio
import aiohttp
import json
import re
import logging
from typing import List, Dict, Optional

logger = logging.getLogger(__name__)


class WebRewardsScraper:
    """Scrapes rewards markets from Polymarket web page"""
    
    def __init__(self):
        self.url = "https://polymarket.com/rewards"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Cache-Control': 'max-age=0'
        }
    
    async def fetch_rewards_markets(self, limit: int = None) -> List[Dict]:
        """
        Fetch ALL markets with rewards from Polymarket CLOB API using cursor pagination

        Args:
            limit: Maximum number of markets to fetch (None = fetch all, recommended: 500-1000)

        Returns:
            List of market dictionaries with rewards data
        """
        try:
            logger.info(f"🌐 Fetching rewards markets from Polymarket CLOB API")

            all_markets = []
            next_cursor = None
            page = 1
            max_pages = 20  # Safety limit (20 pages * 1000 markets = 20,000 markets max)
            pages_without_rewards = 0  # Early stopping: stop if 5 consecutive pages have no rewards

            async with aiohttp.ClientSession() as session:
                while True:
                    # Use CLOB API with cursor-based pagination
                    api_url = "https://clob.polymarket.com/markets"
                    params = {}
                    if next_cursor:
                        params['next_cursor'] = next_cursor

                    logger.info(f"📄 Fetching page {page}...")

                    try:
                        async with session.get(api_url, params=params, headers=self.headers, timeout=20) as response:
                            if response.status != 200:
                                logger.error(f"❌ Failed to fetch page: HTTP {response.status}")
                                break

                            data = await response.json()

                            # CLOB API returns dict with 'data', 'count', 'next_cursor'
                            if not isinstance(data, dict):
                                logger.error(f"❌ Unexpected response type: {type(data)}")
                                break

                            markets = data.get('data', [])
                            count = data.get('count', 0)
                            next_cursor = data.get('next_cursor')

                            if not markets or len(markets) == 0:
                                logger.info("✅ Reached end of results")
                                break

                            # Filter for markets with rewards
                            # IMPORTANT: Don't filter by closed/active here - some closed markets still have rewards!
                            # We'll filter by rewards first, then check if they're tradeable
                            page_markets = []
                            for market in markets:
                                # CLOB API uses 'rewards' object
                                rewards = market.get('rewards', {})
                                if rewards:
                                    min_size = float(rewards.get('min_size', 0) or 0)
                                    max_spread = float(rewards.get('max_spread', 0) or 0)

                                    # Only accept markets with ACTIVE rewards (min_size > 0, max_spread > 0)
                                    if min_size > 0 and max_spread > 0:
                                        # Extract rewards_daily_rate from rates array
                                        rates = rewards.get('rates', [])
                                        rewards_daily_rate = 0
                                        if rates and len(rates) > 0:
                                            rewards_daily_rate = float(rates[0].get('rewards_daily_rate', 0) or 0)

                                        # Convert CLOB format to our format
                                        market['rewardsMinSize'] = min_size
                                        market['rewardsMaxSpread'] = max_spread
                                        market['rewardsDailyRate'] = rewards_daily_rate

                                        # Use rewards_daily_rate as umaReward if available
                                        if rewards_daily_rate > 0:
                                            market['umaReward'] = rewards_daily_rate

                                        page_markets.append(market)

                            logger.info(f"✅ Got {len(markets)} markets, {len(page_markets)} with rewards (total: {len(all_markets) + len(page_markets)})")
                            all_markets.extend(page_markets)

                            # Early stopping: track pages without rewards
                            if len(page_markets) == 0:
                                pages_without_rewards += 1
                                if pages_without_rewards >= 5:
                                    logger.info(f"⏹️  Stopping early: {pages_without_rewards} consecutive pages without rewards")
                                    break
                            else:
                                pages_without_rewards = 0  # Reset counter

                            # Check if we should stop
                            if limit and len(all_markets) >= limit:
                                logger.info(f"📊 Reached limit of {limit} markets")
                                all_markets = all_markets[:limit]
                                break

                            # Check if done (next_cursor is 'LTE=' or None)
                            if not next_cursor or next_cursor == 'LTE=':
                                logger.info("✅ Reached end of pagination")
                                break

                            page += 1

                            # Safety limit
                            if page > max_pages:
                                logger.warning(f"⚠️  Reached safety limit of {max_pages} pages")
                                break

                    except asyncio.TimeoutError:
                        logger.error("❌ Timeout fetching page")
                        break
                    except Exception as e:
                        logger.error(f"❌ Error fetching page: {e}")
                        break

            logger.info(f"✅ Total: {len(all_markets)} markets with rewards")
            return all_markets

        except Exception as e:
            logger.error(f"❌ Error fetching rewards markets: {e}")
            return []
    
    def _extract_complete_json(self, text: str) -> Optional[str]:
        """
        Extract complete JSON object by matching braces

        Args:
            text: Text starting with '{'

        Returns:
            Complete JSON string or None
        """
        if not text.startswith('{'):
            return None

        depth = 0
        in_string = False
        escape = False

        for i, char in enumerate(text):
            if escape:
                escape = False
                continue

            if char == '\\':
                escape = True
                continue

            if char == '"':
                in_string = not in_string
                continue

            if in_string:
                continue

            if char == '{':
                depth += 1
            elif char == '}':
                depth -= 1
                if depth == 0:
                    return text[:i+1]

        return None

    def _extract_markets_from_html(self, html: str) -> List[Dict]:
        """
        Extract markets from HTML by parsing __NEXT_DATA__ JSON

        Args:
            html: HTML content from /rewards page

        Returns:
            List of market dictionaries
        """
        try:
            # Search for the specific pattern we found in test_web_extract.py
            # The JSON is embedded in the HTML, look for the props structure
            pattern = r'{"props":{"pageProps":{"dehydratedState":.+?"data":\[.+?\]'
            match = re.search(pattern, html, re.DOTALL)

            if not match:
                logger.warning("⚠️  Could not find market data in HTML")
                # Save HTML for debugging
                with open('debug_rewards_page.html', 'w', encoding='utf-8') as f:
                    f.write(html)
                logger.info("💾 Saved HTML to debug_rewards_page.html for inspection")
                return []

            # Extract the full JSON object by finding matching braces
            json_start = match.start()
            json_str = self._extract_complete_json(html[json_start:])

            if not json_str:
                logger.error("❌ Could not extract complete JSON")
                return []

            data = json.loads(json_str)
            
            # Navigate to markets data
            # Structure: props -> pageProps -> dehydratedState -> queries[0] -> state -> data -> data
            try:
                queries = data['props']['pageProps']['dehydratedState']['queries']

                # Find the query with market data
                for query in queries:
                    if 'state' in query and 'data' in query['state']:
                        state_data = query['state']['data']
                        if 'data' in state_data and isinstance(state_data['data'], list):
                            markets = state_data['data']
                            count = state_data.get('count', len(markets))
                            total_count = state_data.get('total_count', len(markets))

                            logger.info(f"✅ Extracted {len(markets)} markets from JSON")
                            logger.info(f"📊 Count: {count}, Total: {total_count}")

                            # Check if there are more markets
                            if total_count > len(markets):
                                logger.warning(f"⚠️  Only fetched {len(markets)}/{total_count} markets!")
                                logger.warning(f"⚠️  Missing {total_count - len(markets)} markets - pagination needed!")

                            return markets

                logger.warning("⚠️  Could not find markets in expected JSON structure")
                return []

            except (KeyError, TypeError, IndexError) as e:
                logger.error(f"❌ Error navigating JSON structure: {e}")
                return []
                
        except json.JSONDecodeError as e:
            logger.error(f"❌ Failed to parse JSON: {e}")
            return []
        except Exception as e:
            logger.error(f"❌ Error extracting markets: {e}")
            return []
    
    def _infer_category_from_tags(self, question: str, tags: List[str]) -> str:
        """
        Infer market category from question and tags

        Args:
            question: Market question text
            tags: List of tags from CLOB API (can be None)

        Returns:
            Category string: crypto, sports, politics, science, entertainment, economics, other
        """
        question_lower = question.lower()
        tags_lower = [tag.lower() for tag in (tags or [])]  # Handle None tags

        # Check tags first (more reliable)
        if any(tag in tags_lower for tag in ['politics', 'elections', 'usa election', 'potus']):
            return 'politics'
        if any(tag in tags_lower for tag in ['sports', 'football', 'basketball', 'baseball', 'soccer', 'nfl', 'nba', 'mlb', 'premier league']):
            return 'sports'
        if any(tag in tags_lower for tag in ['crypto', 'cryptocurrency', 'bitcoin', 'ethereum']):
            return 'crypto'
        if any(tag in tags_lower for tag in ['science', 'technology', 'ai', 'space']):
            return 'science'
        if any(tag in tags_lower for tag in ['entertainment', 'movies', 'tv', 'celebrities']):
            return 'entertainment'
        if any(tag in tags_lower for tag in ['economics', 'economy', 'markets', 'finance']):
            return 'economics'

        # Fallback to question keywords
        crypto_keywords = ['bitcoin', 'btc', 'ethereum', 'eth', 'solana', 'sol', 'crypto', 'price']
        science_keywords = ['ai', 'artificial intelligence', 'chatgpt', 'openai', 'technology', 'space', 'nasa']
        politics_keywords = ['election', 'president', 'senate', 'congress', 'vote', 'democrat', 'republican']
        entertainment_keywords = ['movie', 'film', 'actor', 'actress', 'celebrity', 'tv show', 'netflix']
        economics_keywords = ['gdp', 'inflation', 'recession', 'stock market', 'dow jones', 's&p 500']
        sports_keywords = ['nfl', 'nba', 'mlb', 'nhl', 'soccer', 'football', 'basketball', 'super bowl']

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

    def parse_market(self, market_data: Dict) -> Optional[Dict]:
        """
        Parse a market from CLOB API data into standardized format

        Args:
            market_data: Raw market data from CLOB API

        Returns:
            Parsed market dict or None if invalid
        """
        try:
            # Extract basic info (CLOB API format)
            # CLOB uses condition_id as the unique identifier
            market_id = market_data.get('condition_id', '')
            question = market_data.get('question', '')

            if not market_id or not question:
                logger.debug(f"⏭️  Skipped (missing id/question): {question[:60] if question else 'N/A'}")
                return None

            # Extract rewards config (already converted in fetch_rewards_markets)
            rewards_min_size = float(market_data.get('rewardsMinSize', 0) or 0)
            rewards_max_spread = float(market_data.get('rewardsMaxSpread', 0) or 0)
            
            # Skip if no rewards
            if rewards_min_size == 0 or rewards_max_spread == 0:
                logger.debug(f"⏭️  Skipped (no rewards): {question[:60]}")
                return None

            # CLOB API doesn't have volume24hr, so we estimate based on rewards config
            # Higher min_size and tighter max_spread = higher rewards

            # Get tokens
            tokens = market_data.get('tokens', [])

            # Estimate reward based on rewardsMinSize and rewardsMaxSpread
            # Formula: Higher min_size = higher rewards, tighter spread = higher rewards
            base_reward = rewards_min_size * 0.5  # Base: 50% of min_size

            # Adjust for spread (tighter spread = higher rewards)
            if rewards_max_spread <= 2.0:
                spread_multiplier = 2.0  # Very tight spread
            elif rewards_max_spread <= 3.5:
                spread_multiplier = 1.5  # Tight spread
            elif rewards_max_spread <= 5.0:
                spread_multiplier = 1.2  # Medium spread
            else:
                spread_multiplier = 1.0  # Wide spread

            reward = base_reward * spread_multiplier

            # Cap at reasonable values
            reward = min(reward, 750)
            reward = max(reward, 10)  # Minimum $10

            # Estimate volume from reward (for compatibility)
            volume_24hr = reward * 100  # Rough estimate
            liquidity = volume_24hr * 0.1
            
            # Calculate competition (0-3 bars based on volume)
            competition = min(3, int(volume_24hr / 10000))

            # Get market competitiveness (CLOB doesn't have this, default to 0)
            market_competitiveness = 0

            # Infer category from question and tags
            category = self._infer_category_from_tags(question, market_data.get('tags', []))

            # Build standardized market dict (CLOB API format)
            parsed = {
                'market_id': market_id,
                'condition_id': market_id,  # CLOB uses condition_id as primary key
                'question': question,
                'market_slug': market_data.get('market_slug', ''),
                'event_id': '',  # CLOB doesn't have event_id
                'event_slug': '',  # CLOB doesn't have event_slug
                'image': market_data.get('image', ''),
                'volume': volume_24hr,
                'volume_24hr': volume_24hr,
                'liquidity': liquidity,
                'reward': reward,
                'competition_bars': competition,
                'market_competitiveness': market_competitiveness,
                'rewardsMinSize': rewards_min_size,
                'rewardsMaxSpread': rewards_max_spread,
                'tokens': tokens,
                'spread': 0,  # CLOB doesn't have spread field
                'tags': market_data.get('tags', []),  # CLOB has tags for category classification
                'category': category,  # Add inferred category for filtering
                'source': 'clob_api'  # Mark source for debugging
            }
            
            return parsed
            
        except Exception as e:
            logger.error(f"❌ Error parsing market: {e}")
            return None


async def test_scraper():
    """Test the web scraper"""
    scraper = WebRewardsScraper()
    
    print("=" * 80)
    print("TESTING WEB REWARDS SCRAPER")
    print("=" * 80)
    
    # Fetch markets
    markets = await scraper.fetch_rewards_markets(limit=10)
    
    print(f"\n✅ Fetched {len(markets)} markets\n")
    
    # Parse and display first 5
    for i, market_data in enumerate(markets[:5], 1):
        parsed = scraper.parse_market(market_data)
        if parsed:
            print(f"{i}. {parsed['question'][:70]}")
            print(f"   Market ID: {parsed['market_id']}")
            print(f"   Volume 24h: ${parsed['volume_24hr']:.2f}")
            print(f"   Rewards: Min Size={parsed['rewardsMinSize']}, Max Spread={parsed['rewardsMaxSpread']}%")
            print(f"   Estimated Reward: ${parsed['reward']:.2f}")
            print(f"   Competition: {parsed['competition_bars']} bars")
            print()


if __name__ == "__main__":
    asyncio.run(test_scraper())

