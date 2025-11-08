"""
Polymarket Rewards API Scraper
Uses the official Polymarket rewards API endpoint discovered via Playwright
This is the MOST ACCURATE method as it uses the same API the website uses
"""

import asyncio
import aiohttp
import logging
from typing import List, Dict, Optional
import urllib.parse

logger = logging.getLogger(__name__)


class PolymarketRewardsAPI:
    """Fetch rewards markets using official Polymarket API"""
    
    def __init__(self):
        self.base_url = "https://polymarket.com/api/rewards/markets"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'application/json',
            'Accept-Language': 'en-US,en;q=0.9',
            'Referer': 'https://polymarket.com/rewards',
            'Origin': 'https://polymarket.com'
        }
    
    async def fetch_all_rewards_markets(self, limit: int = None) -> List[Dict]:
        """
        Fetch ALL markets with rewards using cursor pagination
        
        Args:
            limit: Maximum number of markets to fetch (None = fetch all)
        
        Returns:
            List of market dictionaries with complete rewards data
        """
        try:
            logger.info(f"🌐 Fetching rewards markets from official Polymarket API")
            
            all_markets = []
            next_cursor = "MA=="  # Initial cursor (base64 encoded "0")
            page = 1
            max_pages = 100  # Safety limit
            
            async with aiohttp.ClientSession() as session:
                while page <= max_pages:
                    # Build query parameters
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
                    
                    logger.info(f"📄 Fetching page {page} (cursor: {next_cursor[:20]}...)...")
                    
                    try:
                        async with session.get(self.base_url, params=params, headers=self.headers, timeout=30) as response:
                            if response.status != 200:
                                logger.error(f"❌ Failed to fetch page: HTTP {response.status}")
                                break
                            
                            data = await response.json()
                            
                            # Extract markets from response
                            if isinstance(data, list):
                                markets = data
                            elif isinstance(data, dict) and 'markets' in data:
                                markets = data['markets']
                            elif isinstance(data, dict) and 'data' in data:
                                markets = data['data']
                            else:
                                logger.error(f"❌ Unexpected response structure: {list(data.keys()) if isinstance(data, dict) else type(data)}")
                                break
                            
                            if not markets:
                                logger.info(f"✅ No more markets on page {page}, stopping")
                                break
                            
                            logger.info(f"✅ Got {len(markets)} markets on page {page}")
                            
                            # Parse and add markets
                            for market_data in markets:
                                parsed = self.parse_market(market_data)
                                if parsed:
                                    all_markets.append(parsed)
                            
                            # Check if we should stop
                            if limit and len(all_markets) >= limit:
                                logger.info(f"📊 Reached limit of {limit} markets")
                                all_markets = all_markets[:limit]
                                break
                            
                            # Get next cursor
                            prev_cursor = next_cursor
                            if isinstance(data, dict) and 'next_cursor' in data:
                                next_cursor = data['next_cursor']
                            elif isinstance(data, dict) and 'nextCursor' in data:
                                next_cursor = data['nextCursor']
                            else:
                                # No more pages
                                logger.info(f"✅ No next cursor, reached end of data")
                                break

                            # Check if cursor indicates end
                            if not next_cursor or next_cursor == prev_cursor:
                                logger.info(f"✅ Reached end of pagination")
                                break
                            
                            page += 1
                            
                    except asyncio.TimeoutError:
                        logger.error(f"❌ Timeout fetching page {page}")
                        break
                    except Exception as e:
                        logger.error(f"❌ Error fetching page {page}: {e}")
                        break
            
            logger.info(f"✅ Fetched {len(all_markets)} total markets with rewards")
            return all_markets
            
        except Exception as e:
            logger.error(f"❌ Error fetching rewards markets: {e}")
            import traceback
            traceback.print_exc()
            return []
    
    def parse_market(self, market_data: dict) -> Optional[Dict]:
        """
        Parse market data from API response

        Args:
            market_data: Raw market data from API

        Returns:
            Parsed market dictionary or None if invalid (including non-liquidity rewards)
        """
        try:
            # ✅ FILTER 1: Check if this is a LIQUIDITY REWARDS market
            # Liquidity rewards MUST have both rewards_min_size AND rewards_max_spread > 0
            # Other reward types (trading rewards, event rewards) don't have these requirements
            rewards_min_size = float(market_data.get('rewards_min_size', 0) or 0)
            rewards_max_spread = float(market_data.get('rewards_max_spread', 0) or 0)

            # Skip markets without LIQUIDITY REWARDS indicators
            # Only accept if BOTH conditions are true:
            # 1. rewards_min_size > 0 (requires minimum order size)
            # 2. rewards_max_spread > 0 (requires spread limit)
            if rewards_min_size == 0 or rewards_max_spread == 0:
                logger.debug(f"⏭️  Skipped (not liquidity rewards): {market_data.get('question', 'Unknown')[:60]} - minSize={rewards_min_size}, maxSpread={rewards_max_spread}")
                return None  # Skip this market

            # Extract reward from rewards_config
            reward = 0
            if 'rewards_config' in market_data and market_data['rewards_config']:
                for config in market_data['rewards_config']:
                    reward += float(config.get('rate_per_day', 0))

            # Extract competition from market_competitiveness
            competition = market_data.get('market_competitiveness', 0)

            # Extract other fields
            market = {
                'id': market_data.get('market_id', ''),
                'market_id': market_data.get('market_id', ''),
                'question': market_data.get('question', ''),
                'reward': reward,
                'competition_bars': competition,
                'volume': market_data.get('volume_24hr', 0),
                'volume_24hr': market_data.get('volume_24hr', 0),
                'liquidity': market_data.get('liquidity', 0),
                'spread': market_data.get('spread', 0),
                'end_date': market_data.get('end_date'),
                'source': 'polymarket_rewards_api',
                'rewardsMinSize': rewards_min_size,
                'rewardsMaxSpread': rewards_max_spread,
                'earning_percentage': market_data.get('earning_percentage', 0),
                'active': True,
                'closed': False,
                # Store raw rewards_config for reference
                'rewards_config': market_data.get('rewards_config', [])
            }

            return market

        except Exception as e:
            logger.debug(f"Failed to parse market: {e}")
            return None


async def test_api():
    """Test the Polymarket Rewards API"""
    api = PolymarketRewardsAPI()
    
    # Fetch first 200 markets
    markets = await api.fetch_all_rewards_markets(limit=200)
    
    print(f"\n{'='*80}")
    print(f"📊 FETCHED {len(markets)} MARKETS FROM POLYMARKET REWARDS API")
    print(f"{'='*80}\n")
    
    if markets:
        # Show first 10 markets
        for i, market in enumerate(markets[:10], 1):
            print(f"{i}. {market['question'][:70]}")
            print(f"   💰 Reward: ${market['reward']}")
            print(f"   📊 Competition: {market['competition_bars']} bars")
            print(f"   📈 Volume 24h: ${market['volume_24hr']:.0f}")
            print(f"   🆔 ID: {market['market_id']}")
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
        
        # Show competition distribution
        print(f"\n{'='*80}")
        print(f"📊 COMPETITION DISTRIBUTION")
        print(f"{'='*80}\n")
        
        comp_ranges = {
            '0 bars': 0,
            '1-2 bars': 0,
            '3-4 bars': 0,
            '5+ bars': 0
        }
        
        for market in markets:
            comp = market['competition_bars']
            if comp == 0:
                comp_ranges['0 bars'] += 1
            elif comp < 3:
                comp_ranges['1-2 bars'] += 1
            elif comp < 5:
                comp_ranges['3-4 bars'] += 1
            else:
                comp_ranges['5+ bars'] += 1
        
        for range_name, count in comp_ranges.items():
            print(f"{range_name}: {count} markets")
    else:
        print("❌ No markets found")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(test_api())

