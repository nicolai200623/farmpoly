"""
Find markets that are actually tradeable (enable_order_book: True)
"""

import asyncio
import aiohttp


async def find_tradeable_markets():
    """Find markets with enable_order_book: True"""
    url = 'https://clob.polymarket.com/markets'
    
    tradeable_count = 0
    total_count = 0
    next_cursor = None
    page = 1
    max_pages = 20
    
    async with aiohttp.ClientSession() as session:
        while page <= max_pages:
            params = {}
            if next_cursor:
                params['next_cursor'] = next_cursor
            
            print(f"📄 Checking page {page}...")
            
            async with session.get(url, params=params, timeout=10) as response:
                if response.status == 200:
                    data = await response.json()
                    
                    markets = data.get('data', [])
                    next_cursor = data.get('next_cursor')
                    
                    for market in markets:
                        total_count += 1
                        
                        if market.get('enable_order_book', False):
                            tradeable_count += 1
                            
                            # Show first 5 tradeable markets
                            if tradeable_count <= 5:
                                print(f"\n✅ TRADEABLE MARKET #{tradeable_count}:")
                                print(f"   Question: {market.get('question', 'Unknown')[:60]}")
                                print(f"   enable_order_book: {market.get('enable_order_book')}")
                                print(f"   closed: {market.get('closed')}")
                                print(f"   active: {market.get('active')}")
                                print(f"   accepting_orders: {market.get('accepting_orders')}")
                                
                                # Check if it has rewards
                                rewards = market.get('rewards', {})
                                if rewards:
                                    min_size = rewards.get('min_size', 0)
                                    max_spread = rewards.get('max_spread', 0)
                                    print(f"   rewards.min_size: {min_size}")
                                    print(f"   rewards.max_spread: {max_spread}")
                    
                    print(f"   Page {page}: {len(markets)} markets, {tradeable_count} tradeable so far (total: {total_count})")
                    
                    if not next_cursor or next_cursor == 'LTE=':
                        print("✅ Reached end of pagination")
                        break
                    
                    page += 1
                else:
                    print(f"❌ Error: {response.status}")
                    break
    
    print(f"\n📊 FINAL SUMMARY:")
    print(f"   Total markets checked: {total_count}")
    print(f"   Tradeable markets (enable_order_book=True): {tradeable_count}")
    print(f"   Percentage: {tradeable_count / total_count * 100:.2f}%")


if __name__ == "__main__":
    asyncio.run(find_tradeable_markets())

