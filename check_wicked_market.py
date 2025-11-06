"""
Check the Wicked market to see actual reward
"""

import asyncio
import aiohttp


async def check_wicked():
    """Check Wicked market from Gamma API"""
    url = 'https://gamma-api.polymarket.com/events'
    
    params = {
        'closed': 'false',
        '_limit': 100
    }
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            data = await response.json()
            
            print(f"Total events: {len(data)}")
            print("=" * 80)
            
            for event in data:
                markets = event.get('markets', [])
                for market in markets:
                    question = market.get('question', '')
                    if 'Wicked' in question and 'For Good' in question:
                        print(f"\n✅ Found: {question}")
                        print(f"   rewardsMinSize: {market.get('rewardsMinSize')}")
                        print(f"   rewardsMaxSpread: {market.get('rewardsMaxSpread')}")
                        print(f"   volume: {market.get('volume')}")
                        print(f"   active: {market.get('active')}")
                        print(f"   closed: {market.get('closed')}")
                        
                        # Check if event has rewards config
                        if event.get('rewards'):
                            print(f"\n   Event rewards config:")
                            print(f"   {event['rewards']}")
                        
                        # Check market rewards
                        print(f"\n   Market data:")
                        print(f"   umaReward: {market.get('umaReward')}")
                        print(f"   rewardsDailyRate: {market.get('rewardsDailyRate')}")
                        
                        return


if __name__ == "__main__":
    asyncio.run(check_wicked())

