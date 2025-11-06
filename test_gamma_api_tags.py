"""
Test Gamma API with tag filtering
"""

import asyncio
import aiohttp
import json


async def test_gamma_api():
    """Test Gamma API with different tag filters"""
    
    base_url = "https://gamma-api.polymarket.com/events"
    
    # Test different tags
    tags = ["sports", "crypto", "politics", "science", "entertainment"]
    
    async with aiohttp.ClientSession() as session:
        for tag in tags:
            print(f"\n{'='*80}")
            print(f"Testing tag: {tag}")
            print('='*80)
            
            params = {
                '_limit': 100,
                'tag': tag,
                'closed': 'false',  # Only active markets
                'archived': 'false'
            }
            
            try:
                async with session.get(base_url, params=params, timeout=10) as response:
                    if response.status == 200:
                        data = await response.json()
                        
                        # Count markets with rewards
                        markets_with_rewards = 0
                        total_markets = len(data)
                        
                        for event in data:
                            markets = event.get('markets', [])
                            for market in markets:
                                if market.get('rewardsMinSize', 0) > 0 and market.get('rewardsMaxSpread', 0) > 0:
                                    markets_with_rewards += 1
                        
                        print(f"✅ Total events: {total_markets}")
                        print(f"✅ Markets with rewards: {markets_with_rewards}")
                        
                        # Show first 3 markets with rewards
                        count = 0
                        for event in data:
                            markets = event.get('markets', [])
                            for market in markets:
                                if market.get('rewardsMinSize', 0) > 0 and market.get('rewardsMaxSpread', 0) > 0:
                                    print(f"\n   {count+1}. {market.get('question', 'Unknown')[:60]}")
                                    print(f"      Reward: minSize={market.get('rewardsMinSize')}, maxSpread={market.get('rewardsMaxSpread')}")
                                    count += 1
                                    if count >= 3:
                                        break
                            if count >= 3:
                                break
                    else:
                        print(f"❌ HTTP {response.status}")
            except Exception as e:
                print(f"❌ Error: {e}")


if __name__ == "__main__":
    asyncio.run(test_gamma_api())

