"""
Find the API endpoint that /rewards page uses to fetch markets
"""

import asyncio
import aiohttp
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def test_api():
    """
    Test Polymarket API endpoints for rewards markets
    Based on typical Next.js data fetching patterns
    """
    
    # Possible API endpoints
    endpoints = [
        "https://gamma-api.polymarket.com/markets?_limit=100&active=true&closed=false&rewards=true",
        "https://gamma-api.polymarket.com/markets?limit=100&rewards=true",
        "https://clob.polymarket.com/rewards",
        "https://strapi-matic.poly.market/markets?rewards=true",
    ]
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Accept': 'application/json',
    }
    
    async with aiohttp.ClientSession() as session:
        for endpoint in endpoints:
            logger.info(f"\nTesting: {endpoint}")
            try:
                async with session.get(endpoint, headers=headers, timeout=10) as response:
                    if response.status == 200:
                        data = await response.json()
                        
                        # Check if it's a list or dict
                        if isinstance(data, list):
                            logger.info(f"✅ SUCCESS: Got {len(data)} markets (list)")
                            
                            # Show first market
                            if len(data) > 0:
                                first = data[0]
                                logger.info(f"First market: {first.get('question', 'N/A')[:60]}")
                                logger.info(f"Has rewards: {first.get('rewardsMinSize', 0) > 0}")
                        
                        elif isinstance(data, dict):
                            # Check for common pagination fields
                            if 'data' in data:
                                markets = data['data']
                                logger.info(f"✅ SUCCESS: Got {len(markets)} markets (dict.data)")
                                logger.info(f"Total count: {data.get('total_count', 'N/A')}")
                                logger.info(f"Next cursor: {data.get('next_cursor', 'N/A')}")
                                
                                if len(markets) > 0:
                                    first = markets[0]
                                    logger.info(f"First market: {first.get('question', 'N/A')[:60]}")
                            else:
                                logger.info(f"✅ Got dict with keys: {list(data.keys())[:10]}")
                    else:
                        logger.warning(f"❌ HTTP {response.status}")
                        
            except asyncio.TimeoutError:
                logger.warning(f"❌ Timeout")
            except Exception as e:
                logger.warning(f"❌ Error: {e}")


if __name__ == "__main__":
    asyncio.run(test_api())

