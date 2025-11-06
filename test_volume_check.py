"""
Test Volume Check
Kiem tra volume cua cac markets de hieu tai sao reward thap
"""

import asyncio
import aiohttp

async def test_volume():
    """Test volume of markets"""
    
    api_url = "https://gamma-api.polymarket.com/events"
    params = {
        'closed': 'false',
        '_limit': 100
    }
    
    print("=" * 80)
    print("TESTING VOLUME OF MARKETS WITH REWARDS")
    print("=" * 80)
    
    async with aiohttp.ClientSession() as session:
        async with session.get(api_url, params=params, timeout=10) as response:
            if response.status == 200:
                events = await response.json()
                
                # Collect markets with rewards
                markets_with_rewards = []
                
                for event in events:
                    for market_data in event.get('markets', []):
                        rewards_min_size = float(market_data.get('rewardsMinSize', 0) or 0)
                        rewards_max_spread = float(market_data.get('rewardsMaxSpread', 0) or 0)
                        
                        if rewards_min_size > 0 and rewards_max_spread > 0:
                            volume = float(market_data.get('volume', 0) or 0)
                            liquidity = float(market_data.get('liquidity', 0) or 0)
                            question = market_data.get('question', 'Unknown')
                            
                            # Calculate reward using bot's logic
                            if volume > 10000:
                                reward = min(volume * 0.002, 500)
                            elif volume > 1000:
                                reward = min(volume * 0.005, 200)
                            else:
                                reward = min(volume * 0.01, 100)
                            
                            if liquidity > 1000:
                                reward *= 1.5
                            
                            markets_with_rewards.append({
                                'question': question,
                                'volume': volume,
                                'liquidity': liquidity,
                                'reward': reward,
                                'min_size': rewards_min_size,
                                'max_spread': rewards_max_spread
                            })
                
                # Sort by reward (highest first)
                markets_with_rewards.sort(key=lambda x: x['reward'], reverse=True)
                
                print(f"\nTotal markets with rewards: {len(markets_with_rewards)}")
                print(f"\nTop 10 markets by estimated reward:")
                print("-" * 80)
                
                for i, market in enumerate(markets_with_rewards[:10]):
                    print(f"\n{i+1}. {market['question'][:60]}")
                    print(f"   Volume: ${market['volume']:,.0f}")
                    print(f"   Liquidity: ${market['liquidity']:,.0f}")
                    print(f"   Estimated Reward: ${market['reward']:.2f}")
                    print(f"   Min Size: {market['min_size']}, Max Spread: {market['max_spread']}%")
                
                # Count how many have reward >= $10
                count_above_10 = sum(1 for m in markets_with_rewards if m['reward'] >= 10)
                count_above_20 = sum(1 for m in markets_with_rewards if m['reward'] >= 20)
                
                print(f"\n" + "=" * 80)
                print(f"SUMMARY:")
                print(f"  Markets with reward >= $10: {count_above_10}/{len(markets_with_rewards)}")
                print(f"  Markets with reward >= $20: {count_above_20}/{len(markets_with_rewards)}")
                
                if count_above_10 == 0:
                    print(f"\nPROBLEM IDENTIFIED:")
                    print(f"  ALL markets have estimated reward < $10!")
                    print(f"  This is why bot finds 0 qualifying markets.")
                    print(f"\nSOLUTION:")
                    print(f"  1. Lower min_reward in config (e.g., to $5)")
                    print(f"  2. OR improve reward estimation logic")

if __name__ == "__main__":
    asyncio.run(test_volume())

