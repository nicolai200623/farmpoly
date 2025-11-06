"""
Check ALL markets from Gamma API and their actual rewards
"""

import asyncio
import aiohttp


async def check_all_rewards():
    """Check all markets and their umaReward values"""
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
            
            # Collect all markets with rewards
            markets_with_rewards = []
            
            for event in data:
                markets = event.get('markets', [])
                for market in markets:
                    # Check if market has rewards
                    rewards_min_size = market.get('rewardsMinSize', 0)
                    rewards_max_spread = market.get('rewardsMaxSpread', 0)
                    
                    if rewards_min_size > 0 and rewards_max_spread > 0:
                        uma_reward = market.get('umaReward', 0)
                        active = market.get('active', False)
                        closed = market.get('closed', False)
                        question = market.get('question', 'Unknown')
                        
                        markets_with_rewards.append({
                            'question': question,
                            'umaReward': uma_reward,
                            'active': active,
                            'closed': closed,
                            'rewardsMinSize': rewards_min_size,
                            'rewardsMaxSpread': rewards_max_spread
                        })
            
            # Sort by umaReward (highest first)
            markets_with_rewards.sort(key=lambda x: x['umaReward'], reverse=True)
            
            print(f"\n📊 Found {len(markets_with_rewards)} markets with rewards\n")
            print("=" * 80)
            
            # Show top 20 markets by reward
            print("\n🏆 TOP 20 MARKETS BY REWARD:\n")
            for i, market in enumerate(markets_with_rewards[:20], 1):
                status = "✅ ACTIVE" if market['active'] and not market['closed'] else "❌ CLOSED/INACTIVE"
                print(f"{i}. {market['question'][:60]}")
                print(f"   💰 umaReward: ${market['umaReward']}")
                print(f"   📊 Status: {status}")
                print(f"   📏 MinSize: {market['rewardsMinSize']}, MaxSpread: {market['rewardsMaxSpread']}")
                print()
            
            # Show distribution
            print("\n📈 REWARD DISTRIBUTION:\n")
            reward_ranges = {
                '0-5': 0,
                '5-10': 0,
                '10-20': 0,
                '20-50': 0,
                '50+': 0
            }
            
            for market in markets_with_rewards:
                reward = market['umaReward']
                if reward < 5:
                    reward_ranges['0-5'] += 1
                elif reward < 10:
                    reward_ranges['5-10'] += 1
                elif reward < 20:
                    reward_ranges['10-20'] += 1
                elif reward < 50:
                    reward_ranges['20-50'] += 1
                else:
                    reward_ranges['50+'] += 1
            
            for range_name, count in reward_ranges.items():
                print(f"${range_name}: {count} markets")


if __name__ == "__main__":
    asyncio.run(check_all_rewards())

