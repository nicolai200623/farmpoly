"""
Test Official Rewards API directly
"""
import requests

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

print("Testing Official Rewards API...")
print(f"URL: {url}\n")

response = requests.get(url, params=params)

print(f"Status: {response.status_code}")

if response.status_code == 200:
    data = response.json()
    
    print(f"Response type: {type(data)}")
    print(f"Response keys: {list(data.keys())}")
    
    if 'markets' in data:
        markets = data['markets']
        print(f"\nNumber of markets: {len(markets)}")
        
        if markets:
            print(f"\nFirst market:")
            market = markets[0]
            print(f"  Question: {market.get('question', 'N/A')}")
            print(f"  Market ID: {market.get('market_id', 'N/A')}")
            print(f"  Slug: {market.get('slug', 'N/A')}")
            
            # Check rewards_config
            if 'rewards_config' in market:
                print(f"  Rewards config: {market['rewards_config']}")
            
            # Check all keys
            print(f"\n  All keys: {list(market.keys())}")
    
    if 'total_count' in data:
        print(f"\nTotal count: {data['total_count']}")
    
    if 'next_cursor' in data or 'nextCursor' in data:
        cursor = data.get('next_cursor') or data.get('nextCursor')
        print(f"Next cursor: {cursor}")
else:
    print(f"Error: {response.text}")

