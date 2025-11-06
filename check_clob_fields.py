"""
Check what fields CLOB API returns
"""

import asyncio
import aiohttp
import json


async def check_clob_fields():
    """Check CLOB API fields"""
    url = 'https://clob.polymarket.com/markets'

    all_markets_with_rewards = []
    all_markets_with_orderbook = []

    async with aiohttp.ClientSession() as session:
        # Check first 5 pages to get more samples
        next_cursor = None
        for page in range(1, 6):
            params = {}
            if next_cursor:
                params['next_cursor'] = next_cursor

            print(f"\n📄 Checking page {page}...")

            async with session.get(url, params=params, timeout=10) as response:
                if response.status == 200:
                    data = await response.json()

                    markets = data.get('data', [])
                    next_cursor = data.get('next_cursor')

                    # Find markets with ACTIVE rewards and check enable_order_book
                    markets_with_rewards = []
                    markets_with_rewards_and_orderbook = []

                    for market in markets:
                        rewards = market.get('rewards', {})
                        if rewards:
                            min_size = rewards.get('min_size', 0)
                            max_spread = rewards.get('max_spread', 0)

                            if min_size > 0 and max_spread > 0:
                                enable_order_book = market.get('enable_order_book', False)
                                markets_with_rewards.append({
                                    'question': market.get('question', 'Unknown')[:60],
                                    'enable_order_book': enable_order_book,
                                    'closed': market.get('closed', False),
                                    'active': market.get('active', False),
                                    'accepting_orders': market.get('accepting_orders', False)
                                })

                                if enable_order_book:
                                    markets_with_rewards_and_orderbook.append(market)

                    all_markets_with_rewards.extend(markets_with_rewards)
                    all_markets_with_orderbook.extend(markets_with_rewards_and_orderbook)

                    if not next_cursor or next_cursor == 'LTE=':
                        break

        # Print summary
        print(f"\n📊 SUMMARY FROM {page} PAGES:")
        print(f"   - Total markets with rewards: {len(all_markets_with_rewards)}")
        print(f"   - Markets with enable_order_book=True: {len(all_markets_with_orderbook)}")
        print(f"   - Markets with enable_order_book=False: {len(all_markets_with_rewards) - len(all_markets_with_orderbook)}")

        if all_markets_with_rewards:
            print("\n🔍 SAMPLE MARKETS WITH REWARDS:")
            for i, m in enumerate(all_markets_with_rewards[:10], 1):
                print(f"\n{i}. {m['question']}")
                print(f"   enable_order_book: {m['enable_order_book']}")
                print(f"   closed: {m['closed']}")
                print(f"   active: {m['active']}")
                print(f"   accepting_orders: {m['accepting_orders']}")

            if all_markets_with_orderbook:
                print("\n" + "=" * 80)
                print("✅ EXAMPLE MARKET WITH enable_order_book=True:")
                print("=" * 80)
                print(json.dumps(all_markets_with_orderbook[0], indent=2)[:2000])
        else:
            print("\n❌ No markets with active rewards found")


if __name__ == "__main__":
    asyncio.run(check_clob_fields())

