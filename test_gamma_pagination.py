"""
Test Gamma API pagination to fetch ALL markets with rewards
"""

import asyncio
import aiohttp
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def fetch_all_rewards_markets():
    """
    Fetch ALL markets with rewards using pagination
    """
    
    base_url = "https://gamma-api.polymarket.com/markets"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Accept': 'application/json',
    }
    
    all_markets = []
    offset = 0
    limit = 100
    
    async with aiohttp.ClientSession() as session:
        while True:
            # Build URL with pagination
            params = {
                '_limit': limit,
                '_offset': offset,
                'active': 'true',
                'closed': 'false',
            }
            
            logger.info(f"\nFetching offset={offset}, limit={limit}...")
            
            try:
                async with session.get(base_url, params=params, headers=headers, timeout=10) as response:
                    if response.status != 200:
                        logger.error(f"HTTP {response.status}")
                        break
                    
                    markets = await response.json()
                    
                    if not markets or len(markets) == 0:
                        logger.info("No more markets")
                        break
                    
                    # Filter for markets with rewards
                    rewards_markets = [
                        m for m in markets 
                        if m.get('rewardsMinSize', 0) > 0 and m.get('rewardsMaxSpread', 0) > 0
                    ]
                    
                    logger.info(f"Got {len(markets)} markets, {len(rewards_markets)} with rewards")
                    all_markets.extend(rewards_markets)
                    
                    # Check if we got less than limit (last page)
                    if len(markets) < limit:
                        logger.info("Reached last page")
                        break
                    
                    offset += limit
                    
                    # Safety limit
                    if offset >= 1000:
                        logger.warning("Reached safety limit of 1000 markets")
                        break
                    
            except Exception as e:
                logger.error(f"Error: {e}")
                break
    
    logger.info(f"\n{'='*80}")
    logger.info(f"TOTAL: {len(all_markets)} markets with rewards")
    logger.info(f"{'='*80}")
    
    # Show first 10
    logger.info("\nFirst 10 markets with rewards:")
    for i, market in enumerate(all_markets[:10], 1):
        logger.info(f"{i}. {market['question'][:60]}")
        logger.info(f"   Reward min: ${market['rewardsMinSize']}, max spread: {market['rewardsMaxSpread']}")
    
    return all_markets


if __name__ == "__main__":
    asyncio.run(fetch_all_rewards_markets())

