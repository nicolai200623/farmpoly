"""
Check CLOB API for markets with high rewards
"""

import asyncio
import aiohttp


async def check_clob_rewards():
    """Check CLOB API for markets with rewards"""
    url = 'https://clob.polymarket.com/markets'
    
    all_markets = []
    next_cursor = None
    page = 1
    max_pages = 10  # Check first 10 pages
    
    async with aiohttp.ClientSession() as session:
        while page <= max_pages:
            params = {}
            if next_cursor:
                params['next_cursor'] = next_cursor
            
            print(f"📄 Fetching page {page}...")
            
            async with session.get(url, params=params, timeout=10) as response:
                if response.status == 200:
                    data = await response.json()
                    
                    markets = data.get('data', [])
                    next_cursor = data.get('next_cursor')
                    
                    # Filter for markets with rewards
                    for market in markets:
                        # Skip closed or inactive
                        if market.get('closed', False):
                            continue
                        if not market.get('active', False):
                            continue
                        
                        rewards = market.get('rewards', {})
                        if rewards:
                            min_size = float(rewards.get('min_size', 0) or 0)
                            max_spread = float(rewards.get('max_spread', 0) or 0)
                            
                            if min_size > 0 and max_spread > 0:
                                # Get reward info
                                question = market.get('question', 'Unknown')
                                
                                # CLOB API might have different reward fields
                                uma_reward = market.get('umaReward', 0)
                                rewards_daily_rate = market.get('rewardsDailyRate', 0)
                                
                                all_markets.append({
                                    'question': question,
                                    'umaReward': uma_reward,
                                    'rewardsDailyRate': rewards_daily_rate,
                                    'min_size': min_size,
                                    'max_spread': max_spread,
                                    'rewards_obj': rewards
                                })
                    
                    print(f"   Found {len(markets)} markets, {len([m for m in markets if m.get('rewards')])} with rewards")
                    
                    # Check if done
                    if not next_cursor or next_cursor == 'LTE=':
                        print("✅ Reached end of pagination")
                        break
                    
                    page += 1
                else:
                    print(f"❌ Error: {response.status}")
                    break
    
    print(f"\n📊 Total markets with rewards: {len(all_markets)}\n")
    print("=" * 80)
    
    if len(all_markets) > 0:
        # Show first 20
        print("\n🏆 FIRST 20 MARKETS WITH REWARDS:\n")
        for i, market in enumerate(all_markets[:20], 1):
            print(f"{i}. {market['question'][:60]}")
            print(f"   💰 umaReward: {market['umaReward']}")
            print(f"   📈 rewardsDailyRate: {market['rewardsDailyRate']}")
            print(f"   📏 MinSize: {market['min_size']}, MaxSpread: {market['max_spread']}")
            print(f"   🔧 Rewards object: {market['rewards_obj']}")
            print()
    else:
        print("❌ No markets with rewards found in CLOB API")


if __name__ == "__main__":
    asyncio.run(check_clob_rewards())

