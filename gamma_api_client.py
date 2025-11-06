"""
Polymarket Gamma API Client
Fetches markets with rewards from Gamma Markets API
Based on official Polymarket documentation: https://gamma-api.polymarket.com
"""
import aiohttp
import asyncio
import logging
from typing import List, Dict, Optional

logger = logging.getLogger(__name__)


class GammaAPIClient:
    """Client for Polymarket Gamma Markets API"""
    
    def __init__(self):
        self.base_url = "https://gamma-api.polymarket.com/markets"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
    
    async def fetch_all_rewards_markets(self, limit: int = None) -> List[Dict]:
        """
        Fetch ALL markets with rewards using pagination
        
        Args:
            limit: Maximum number of markets to fetch (None = fetch all)
        
        Returns:
            List of market dictionaries with rewards data
        """
        try:
            logger.info(f"🌐 Fetching rewards markets from Gamma API")
            
            all_markets = []
            offset = 0
            page_limit = 100  # API limit per request
            max_pages = 100  # Safety limit
            page = 1
            
            async with aiohttp.ClientSession() as session:
                while page <= max_pages:
                    # Build query parameters according to Gamma API spec
                    params = {
                        'active': 'true',      # Only active markets
                        'closed': 'false',     # Not closed
                        'archived': 'false',   # Not archived
                        'limit': page_limit,
                        'offset': offset
                    }
                    
                    logger.info(f"📄 Fetching page {page} (offset: {offset})...")
                    
                    try:
                        async with session.get(self.base_url, params=params, headers=self.headers, timeout=30) as response:
                            if response.status != 200:
                                logger.error(f"❌ Failed to fetch page: HTTP {response.status}")
                                break
                            
                            markets = await response.json()
                            
                            if not markets:
                                logger.info(f"✅ No more markets on page {page}, stopping")
                                break
                            
                            logger.info(f"✅ Got {len(markets)} markets on page {page}")
                            
                            # Filter and parse markets with rewards
                            markets_with_rewards = self._filter_markets_with_rewards(markets)
                            
                            logger.info(f"   → {len(markets_with_rewards)} markets have rewards")
                            
                            all_markets.extend(markets_with_rewards)
                            
                            # Check if we should stop
                            if limit and len(all_markets) >= limit:
                                logger.info(f"📊 Reached limit of {limit} markets")
                                all_markets = all_markets[:limit]
                                break
                            
                            # If we got less than page_limit, we've reached the end
                            if len(markets) < page_limit:
                                logger.info(f"✅ Reached end of data (got {len(markets)} < {page_limit})")
                                break
                            
                            offset += page_limit
                            page += 1
                            
                    except asyncio.TimeoutError:
                        logger.error(f"❌ Timeout fetching page {page}")
                        break
                    except Exception as e:
                        logger.error(f"❌ Error fetching page {page}: {e}")
                        break
            
            logger.info(f"✅ Fetched {len(all_markets)} total markets with rewards from Gamma API")
            return all_markets
            
        except Exception as e:
            logger.error(f"❌ Error in fetch_all_rewards_markets: {e}")
            return []
    
    def _filter_markets_with_rewards(self, markets: List[Dict]) -> List[Dict]:
        """
        Filter markets that have rewards program

        Args:
            markets: List of markets from Gamma API

        Returns:
            List of markets with rewards
        """
        markets_with_rewards = []

        for market in markets:
            # Gamma API uses camelCase field names
            max_spread = market.get('rewardsMaxSpread', 0)
            min_size = market.get('rewardsMinSize', 0)

            # Only include markets with valid rewards configuration
            if max_spread > 0 or min_size > 0:
                parsed = self._parse_market(market)
                if parsed:
                    markets_with_rewards.append(parsed)

        return markets_with_rewards
    
    def _parse_market(self, market_data: dict) -> Optional[Dict]:
        """
        Parse market data from Gamma API response

        Args:
            market_data: Raw market data from API

        Returns:
            Parsed market dictionary or None if invalid
        """
        try:
            # Gamma API uses camelCase field names
            max_spread = float(market_data.get('rewardsMaxSpread', 0))
            min_size = float(market_data.get('rewardsMinSize', 0))

            # Use umaReward as the reward amount (this is the actual reward in USD)
            uma_reward = float(market_data.get('umaReward', 0))

            # If no umaReward, estimate from volume (fallback)
            if uma_reward == 0:
                # Get total volume (volumeClob is the CLOB volume)
                volume = float(market_data.get('volumeClob', 0))
                # Simple estimation: higher volume = higher potential rewards
                if volume > 100000:
                    uma_reward = 100
                elif volume > 50000:
                    uma_reward = 50
                elif volume > 10000:
                    uma_reward = 20
                elif volume > 1000:
                    uma_reward = 10
                else:
                    uma_reward = 5

            # Calculate competition from 24h volume
            volume_24h = float(market_data.get('volume24hrClob', 0))
            competition = min(3, int(volume_24h / 10000))

            # Build market object
            market = {
                'id': market_data.get('conditionId', ''),
                'market_id': market_data.get('conditionId', ''),
                'condition_id': market_data.get('conditionId', ''),
                'question': market_data.get('question', ''),
                'slug': market_data.get('slug', ''),
                'reward': uma_reward,
                'competition_bars': competition,
                'volume': float(market_data.get('volumeClob', 0)),
                'volume_24hr': volume_24h,
                'liquidity': float(market_data.get('liquidityClob', 0)),
                'spread': max_spread,
                'end_date': market_data.get('endDate'),
                'source': 'gamma_api',
                'active': market_data.get('active', False),
                'closed': market_data.get('closed', False),
                'archived': market_data.get('archived', False),
                'rewards_max_spread': max_spread,
                'rewards_min_size': min_size,
                'clob_token_ids': [],  # Not available in this format
                'url': f"https://polymarket.com/market/{market_data.get('slug', '')}"
            }

            return market

        except Exception as e:
            logger.error(f"❌ Error parsing market: {e}")
            return None
    
    async def get_market_by_id(self, condition_id: str) -> Optional[Dict]:
        """
        Get detailed information for a specific market
        
        Args:
            condition_id: The condition ID of the market
        
        Returns:
            Market dictionary or None if not found
        """
        try:
            url = f"https://gamma-api.polymarket.com/markets/{condition_id}"
            
            async with aiohttp.ClientSession() as session:
                async with session.get(url, headers=self.headers, timeout=10) as response:
                    if response.status == 200:
                        market_data = await response.json()
                        return self._parse_market(market_data)
                    else:
                        logger.error(f"❌ Failed to fetch market {condition_id}: HTTP {response.status}")
                        return None
        except Exception as e:
            logger.error(f"❌ Error fetching market {condition_id}: {e}")
            return None


# For backward compatibility with existing code
class PolymarketRewardsAPI(GammaAPIClient):
    """Alias for backward compatibility"""
    pass

