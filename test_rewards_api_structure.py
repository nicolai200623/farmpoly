"""
Test script to analyze the structure of /api/rewards/markets
and understand how to differentiate liquidity rewards from other reward types
"""

import asyncio
import aiohttp
import json

async def fetch_rewards_data():
    """Fetch data from /api/rewards/markets and analyze structure"""

    url = "https://polymarket.com/api/rewards/markets"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Accept': 'application/json',
        'Referer': 'https://polymarket.com/rewards',
        'Origin': 'https://polymarket.com'
    }

    params = {
        'orderBy': 'market',
        'position': 'DESC',
        'query': '',
        'showFavorites': 'false',
        'tagSlug': 'all',
        'nextCursor': 'MA==',
        'requestPath': '/rewards/user/markets',
        'onlyMergeable': 'false',
        'noCompetition': 'false',
        'onlyOpenOrders': 'false',
        'onlyPositions': 'false'
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, headers=headers, timeout=30) as response:
            if response.status != 200:
                print(f"❌ Failed: HTTP {response.status}")
                return

            data = await response.json()

            # Handle different response formats
            if isinstance(data, list):
                markets = data
            elif isinstance(data, dict) and 'data' in data:
                markets = data['data']
            else:
                markets = []

            print(f"✅ Fetched {len(markets)} markets")
            print(f"\n{'='*100}")
            print(f"ANALYZING FIRST 5 MARKETS")
            print(f"{'='*100}\n")

            for i, market in enumerate(markets[:5], 1):
                print(f"\n{i}. {market.get('question', 'Unknown')}")
                print(f"   Market ID: {market.get('market_id')}")

                # Analyze rewards_config structure
                rewards_config = market.get('rewards_config', [])
                print(f"   Rewards Config: {len(rewards_config)} entries")

                total_reward = 0
                for j, config in enumerate(rewards_config):
                    reward_type = config.get('reward_type', 'unknown')
                    rate_per_day = config.get('rate_per_day', 0)
                    total_reward += rate_per_day

                    print(f"      [{j+1}] Type: {reward_type}, Rate/Day: ${rate_per_day}")

                    # Print all keys in config to understand structure
                    if j == 0:
                        print(f"          Available fields: {list(config.keys())}")

                print(f"   Total Reward: ${total_reward}/day")
                print(f"   Competition: {market.get('market_competitiveness', 0)} bars")
                print(f"   Volume 24h: ${market.get('volume_24hr', 0):.0f}")

            # Analyze reward types across all markets
            print(f"\n{'='*100}")
            print(f"REWARD TYPE ANALYSIS (ALL MARKETS)")
            print(f"{'='*100}\n")

            reward_types = {}
            markets_by_reward_type = {}

            for market in markets:
                rewards_config = market.get('rewards_config', [])
                for config in rewards_config:
                    reward_type = config.get('reward_type', 'unknown')
                    rate = config.get('rate_per_day', 0)

                    if reward_type not in reward_types:
                        reward_types[reward_type] = {
                            'count': 0,
                            'total_rate': 0,
                            'markets': []
                        }

                    reward_types[reward_type]['count'] += 1
                    reward_types[reward_type]['total_rate'] += rate
                    reward_types[reward_type]['markets'].append(market.get('question', 'Unknown')[:60])

            for reward_type, stats in reward_types.items():
                print(f"📊 {reward_type.upper()}:")
                print(f"   Count: {stats['count']}")
                print(f"   Total Rate: ${stats['total_rate']:.2f}/day")
                print(f"   Avg Rate: ${stats['total_rate']/stats['count']:.2f}/day")
                print(f"   Example markets:")
                for example in stats['markets'][:3]:
                    print(f"      - {example}")
                print()

if __name__ == "__main__":
    asyncio.run(fetch_rewards_data())
