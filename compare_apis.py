"""
Compare Gamma API vs Official Rewards API
"""
import asyncio
import aiohttp

async def fetch_gamma_api():
    """Fetch from Gamma API"""
    url = "https://gamma-api.polymarket.com/markets"
    params = {
        'active': 'true',
        'closed': 'false',
        'archived': 'false',
        'limit': 100,
        'offset': 0
    }
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            if response.status == 200:
                markets = await response.json()
                # Filter markets with rewards
                markets_with_rewards = [
                    m for m in markets 
                    if m.get('rewardsMaxSpread', 0) > 0 or m.get('rewardsMinSize', 0) > 0
                ]
                return markets_with_rewards
            return []

async def fetch_official_rewards_api():
    """Fetch from Official Rewards API"""
    url = "https://polymarket.com/api/rewards/markets"
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
        async with session.get(url, params=params) as response:
            if response.status == 200:
                data = await response.json()
                return data.get('markets', [])
            return []

async def main():
    print("Fetching from both APIs...\n")
    
    gamma_markets, official_markets = await asyncio.gather(
        fetch_gamma_api(),
        fetch_official_rewards_api()
    )
    
    print(f"{'='*80}")
    print(f"COMPARISON RESULTS")
    print(f"{'='*80}\n")
    
    print(f"Gamma API: {len(gamma_markets)} markets with rewards")
    print(f"Official Rewards API: {len(official_markets)} markets")
    
    # Get market IDs
    gamma_ids = set(m.get('conditionId', '') for m in gamma_markets)
    official_ids = set(m.get('market_id', '') or m.get('condition_id', '') for m in official_markets)
    
    # Find markets only in Gamma API
    only_in_gamma = gamma_ids - official_ids
    only_in_official = official_ids - gamma_ids
    in_both = gamma_ids & official_ids
    
    print(f"\nOverlap:")
    print(f"  In both APIs: {len(in_both)} markets")
    print(f"  Only in Gamma API: {len(only_in_gamma)} markets")
    print(f"  Only in Official API: {len(only_in_official)} markets")
    
    # Show examples of markets only in Gamma API
    if only_in_gamma:
        print(f"\n{'='*80}")
        print(f"MARKETS ONLY IN GAMMA API (first 10)")
        print(f"{'='*80}\n")
        
        count = 0
        for market in gamma_markets:
            if market.get('conditionId', '') in only_in_gamma:
                print(f"{count+1}. {market.get('question', '')[:70]}")
                print(f"   Condition ID: {market.get('conditionId', '')}")
                print(f"   Rewards Max Spread: {market.get('rewardsMaxSpread', 0)}")
                print(f"   Rewards Min Size: {market.get('rewardsMinSize', 0)}")
                print(f"   URL: https://polymarket.com/market/{market.get('slug', '')}")
                print()
                count += 1
                if count >= 10:
                    break
    
    # Show examples of markets only in Official API
    if only_in_official:
        print(f"\n{'='*80}")
        print(f"MARKETS ONLY IN OFFICIAL REWARDS API (first 10)")
        print(f"{'='*80}\n")
        
        count = 0
        for market in official_markets:
            market_id = market.get('market_id', '') or market.get('condition_id', '')
            if market_id in only_in_official:
                print(f"{count+1}. {market.get('question', '')[:70]}")
                print(f"   Market ID: {market_id}")
                print(f"   URL: https://polymarket.com/market/{market.get('slug', '')}")
                print()
                count += 1
                if count >= 10:
                    break

if __name__ == "__main__":
    asyncio.run(main())

