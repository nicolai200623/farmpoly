"""
Test CLOB API for rewards markets with pagination
"""

import asyncio
import aiohttp
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def test_clob_api():
    """
    Test CLOB API /markets endpoint with pagination
    """
    
    base_url = "https://clob.polymarket.com/markets"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Accept': 'application/json',
    }
    
    all_markets = []
    next_cursor = None
    page = 1
    
    async with aiohttp.ClientSession() as session:
        while True:
            # Build params
            params = {}
            if next_cursor:
                params['next_cursor'] = next_cursor
            
            logger.info(f"\nFetching page {page}...")
            if next_cursor:
                logger.info(f"Cursor: {next_cursor[:50]}...")
            
            try:
                async with session.get(base_url, params=params, headers=headers, timeout=10) as response:
                    if response.status != 200:
                        logger.error(f"HTTP {response.status}")
                        break
                    
                    data = await response.json()
                    
                    # Check response structure
                    if isinstance(data, dict):
                        markets = data.get('data', [])
                        count = data.get('count', 0)
                        next_cursor = data.get('next_cursor')
                        
                        logger.info(f"Got {len(markets)} markets, count={count}")
                        logger.info(f"Next cursor: {next_cursor[:50] if next_cursor else 'None'}...")
                        
                        # Filter for rewards
                        rewards_markets = [
                            m for m in markets
                            if m.get('rewards', {}).get('min_size', 0) > 0
                        ]
                        
                        logger.info(f"Markets with rewards: {len(rewards_markets)}")
                        all_markets.extend(rewards_markets)
                        
                        # Check if done
                        if not next_cursor or next_cursor == 'LTE=':
                            logger.info("Reached end")
                            break
                        
                        page += 1
                        
                        # Safety limit
                        if page > 50:
                            logger.warning("Reached safety limit of 50 pages")
                            break
                    else:
                        logger.error(f"Unexpected response type: {type(data)}")
                        break
                    
            except Exception as e:
                logger.error(f"Error: {e}")
                break
    
    logger.info(f"\n{'='*80}")
    logger.info(f"TOTAL: {len(all_markets)} markets with rewards")
    logger.info(f"{'='*80}")
    
    # Show first 10
    if all_markets:
        logger.info("\nFirst 10 markets with rewards:")
        for i, market in enumerate(all_markets[:10], 1):
            question = market.get('question', 'N/A')
            rewards = market.get('rewards', {})
            logger.info(f"{i}. {question[:60]}")
            logger.info(f"   Min size: {rewards.get('min_size')}, Max spread: {rewards.get('max_spread')}")


if __name__ == "__main__":
    asyncio.run(test_clob_api())

