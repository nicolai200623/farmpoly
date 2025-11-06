"""
Test Gamma API directly to see response structure
"""
import requests

url = "https://gamma-api.polymarket.com/markets"

params = {
    'active': 'true',
    'closed': 'false',
    'archived': 'false',
    'limit': 10,
    'offset': 0
}

print("Testing Gamma API /markets endpoint...")
print(f"URL: {url}")
print(f"Params: {params}\n")

response = requests.get(url, params=params)

print(f"Status: {response.status_code}")

if response.status_code == 200:
    data = response.json()
    
    print(f"Response type: {type(data)}")
    
    if isinstance(data, list):
        print(f"Number of markets: {len(data)}")
        
        if data:
            print(f"\nFirst market:")
            market = data[0]
            print(f"  Question: {market.get('question', 'N/A')}")
            print(f"  Condition ID: {market.get('condition_id', 'N/A')}")
            print(f"  Active: {market.get('active', 'N/A')}")
            print(f"  Closed: {market.get('closed', 'N/A')}")
            
            # Check rewards
            if 'rewards' in market:
                print(f"  Rewards: {market['rewards']}")
            else:
                print(f"  Rewards: None")
            
            # Check all keys
            print(f"\n  All keys: {list(market.keys())}")
    
    elif isinstance(data, dict):
        print(f"Response keys: {list(data.keys())}")
else:
    print(f"Error: {response.text}")

