"""
Test different API endpoints to find the correct one for rewards markets
"""
import asyncio
import aiohttp

async def test_endpoint(url, params, description):
    """Test an API endpoint"""
    print(f"\n{'='*80}")
    print(f"Testing: {description}")
    print(f"URL: {url}")
    print(f"{'='*80}")
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            print(f"Status: {response.status}")
            
            if response.status == 200:
                data = await response.json()
                
                # Check structure
                if isinstance(data, dict):
                    print(f"Response type: dict")
                    print(f"Keys: {list(data.keys())[:10]}")
                    
                    if 'data' in data:
                        markets = data['data']
                        print(f"Markets count: {len(markets)}")
                        print(f"Next cursor: {data.get('nextCursor', 'N/A')}")
                        
                        if markets:
                            first = markets[0]
                            print(f"\nFirst market:")
                            print(f"  Question: {first.get('question', 'N/A')[:70]}")
                            print(f"  ID: {first.get('market_id', first.get('id', 'N/A'))}")
                            print(f"  End date: {first.get('end_date', first.get('endDate', 'N/A'))}")
                            
                            # Check rewards
                            if 'rewards_config' in first:
                                print(f"  Rewards config: {first['rewards_config']}")
                            elif 'rewardsConfig' in first:
                                print(f"  Rewards config: {first['rewardsConfig']}")
                            else:
                                print(f"  No rewards config found")
                    
                elif isinstance(data, list):
                    print(f"Response type: list")
                    print(f"Markets count: {len(data)}")
                    
                    if data:
                        first = data[0]
                        print(f"\nFirst market:")
                        print(f"  Question: {first.get('question', 'N/A')[:70]}")
                        print(f"  ID: {first.get('market_id', first.get('id', 'N/A'))}")
            else:
                text = await response.text()
                print(f"Error: {text[:200]}")

async def main():
    # Endpoint 1: Current endpoint (user markets)
    await test_endpoint(
        "https://polymarket.com/api/rewards/markets",
        {
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
        },
        "Current endpoint - /rewards/user/markets"
    )
    
    # Endpoint 2: Try without requestPath
    await test_endpoint(
        "https://polymarket.com/api/rewards/markets",
        {
            'orderBy': 'market',
            'position': 'DESC',
            'query': '',
            'showFavorites': 'false',
            'tagSlug': 'all',
            'nextCursor': 'MA==',
            'onlyMergeable': 'false',
            'noCompetition': 'false',
            'onlyOpenOrders': 'false',
            'onlyPositions': 'false'
        },
        "Without requestPath parameter"
    )
    
    # Endpoint 3: Try /rewards/markets (without user)
    await test_endpoint(
        "https://polymarket.com/api/rewards/markets",
        {
            'orderBy': 'market',
            'position': 'DESC',
            'tagSlug': 'all',
            'nextCursor': 'MA=='
        },
        "Minimal parameters"
    )
    
    # Endpoint 4: Try different requestPath
    await test_endpoint(
        "https://polymarket.com/api/rewards/markets",
        {
            'orderBy': 'market',
            'position': 'DESC',
            'query': '',
            'showFavorites': 'false',
            'tagSlug': 'all',
            'nextCursor': 'MA==',
            'requestPath': '/rewards',
            'onlyMergeable': 'false',
            'noCompetition': 'false',
            'onlyOpenOrders': 'false',
            'onlyPositions': 'false'
        },
        "requestPath = /rewards (not /rewards/user/markets)"
    )
    
    # Endpoint 5: Try orderBy=reward
    await test_endpoint(
        "https://polymarket.com/api/rewards/markets",
        {
            'orderBy': 'reward',
            'position': 'DESC',
            'query': '',
            'showFavorites': 'false',
            'tagSlug': 'all',
            'nextCursor': 'MA==',
            'requestPath': '/rewards',
            'onlyMergeable': 'false',
            'noCompetition': 'false',
            'onlyOpenOrders': 'false',
            'onlyPositions': 'false'
        },
        "orderBy=reward instead of orderBy=market"
    )
    
    # Endpoint 6: Try with limit parameter
    await test_endpoint(
        "https://polymarket.com/api/rewards/markets",
        {
            'orderBy': 'market',
            'position': 'DESC',
            'query': '',
            'showFavorites': 'false',
            'tagSlug': 'all',
            'nextCursor': 'MA==',
            'requestPath': '/rewards',
            'onlyMergeable': 'false',
            'noCompetition': 'false',
            'onlyOpenOrders': 'false',
            'onlyPositions': 'false',
            'limit': '200'
        },
        "With limit=200 parameter"
    )

if __name__ == "__main__":
    asyncio.run(main())

