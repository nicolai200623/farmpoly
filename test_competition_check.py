"""
Test Competition Check
Kiem tra competition cua cac markets
"""

import asyncio
import aiohttp

async def test_competition():
    """Test competition of markets"""
    
    api_url = "https://gamma-api.polymarket.com/events"
    params = {
        'closed': 'false',
        '_limit': 100
    }
    
    print("=" * 80)
    print("TESTING COMPETITION OF MARKETS WITH REWARDS")
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
                            question = market_data.get('question', 'Unknown')
                            
                            # Calculate competition using bot's logic
                            competition = min(3, int(volume / 10000))
                            
                            markets_with_rewards.append({
                                'question': question,
                                'volume': volume,
                                'competition': competition
                            })
                
                # Count by competition level
                competition_counts = {}
                for market in markets_with_rewards:
                    comp = market['competition']
                    competition_counts[comp] = competition_counts.get(comp, 0) + 1
                
                print(f"\nTotal markets with rewards: {len(markets_with_rewards)}")
                print(f"\nMARKETS BY COMPETITION LEVEL:")
                for comp in sorted(competition_counts.keys()):
                    count = competition_counts[comp]
                    print(f"  {comp} bars: {count} markets")
                
                # Check how many would pass max_competition = 1
                max_competition = 1
                passed = sum(1 for m in markets_with_rewards if m['competition'] <= max_competition)
                
                print(f"\n" + "=" * 80)
                print(f"FILTER SIMULATION (max_competition_bars = {max_competition}):")
                print(f"  Markets that would pass: {passed}/{len(markets_with_rewards)}")
                
                if passed == 0:
                    print(f"\nPROBLEM IDENTIFIED:")
                    print(f"  ALL markets have competition > {max_competition}!")
                    print(f"  This is why bot finds 0 qualifying markets.")
                    print(f"\nSOLUTION:")
                    print(f"  Increase max_competition_bars in config (e.g., to 3)")
                else:
                    print(f"\nMarkets with competition <= {max_competition}:")
                    for market in [m for m in markets_with_rewards if m['competition'] <= max_competition][:10]:
                        print(f"  - {market['question'][:60]}")
                        print(f"    Volume: ${market['volume']:,.0f}, Competition: {market['competition']} bars")

if __name__ == "__main__":
    asyncio.run(test_competition())

