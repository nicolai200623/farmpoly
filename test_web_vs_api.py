"""
Test Web vs API
So sanh markets tu trang /rewards voi Gamma API
"""

import asyncio
import aiohttp
import json
import re

async def test_web_vs_api():
    """Compare web page data with API data"""
    
    print("=" * 80)
    print("COMPARING WEB PAGE vs GAMMA API")
    print("=" * 80)
    
    # Fetch from web page
    print("\n1. FETCHING FROM WEB PAGE...")
    async with aiohttp.ClientSession() as session:
        async with session.get("https://polymarket.com/rewards", timeout=10) as response:
            html = await response.text()
            
            # Extract JSON data from __NEXT_DATA__ script tag
            match = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.+?)</script>', html, re.DOTALL)
            if match:
                data = json.loads(match.group(1))
                
                # Navigate to markets data
                markets_data = data['props']['pageProps']['dehydratedState']['queries'][0]['state']['data']['data']
                
                print(f"   Found {len(markets_data)} markets on web page")
                
                # Extract market questions
                web_markets = {}
                for market in markets_data:
                    question = market['question']
                    web_markets[question] = {
                        'market_id': market['market_id'],
                        'rewards_min_size': market.get('rewards_min_size', 0),
                        'rewards_max_spread': market.get('rewards_max_spread', 0),
                        'volume_24hr': market.get('volume_24hr', 0)
                    }
                
                print(f"   Parsed {len(web_markets)} markets")
            else:
                print("   ERROR: Could not find __NEXT_DATA__ in HTML")
                return
    
    # Fetch from Gamma API
    print("\n2. FETCHING FROM GAMMA API...")
    api_url = "https://gamma-api.polymarket.com/events"
    params = {
        'closed': 'false',
        '_limit': 100
    }
    
    async with aiohttp.ClientSession() as session:
        async with session.get(api_url, params=params, timeout=10) as response:
            events = await response.json()
            
            # Extract markets
            api_markets = {}
            for event in events:
                for market_data in event.get('markets', []):
                    question = market_data.get('question', 'Unknown')
                    rewards_min_size = float(market_data.get('rewardsMinSize', 0) or 0)
                    rewards_max_spread = float(market_data.get('rewardsMaxSpread', 0) or 0)
                    
                    if rewards_min_size > 0 and rewards_max_spread > 0:
                        api_markets[question] = {
                            'market_id': market_data.get('id'),
                            'rewards_min_size': rewards_min_size,
                            'rewards_max_spread': rewards_max_spread,
                            'volume': float(market_data.get('volume', 0) or 0)
                        }
            
            print(f"   Found {len(api_markets)} markets with rewards from API")
    
    # Compare
    print("\n3. COMPARING...")
    
    # Check SpaceX markets
    spacex_questions = [
        "Will SpaceX have less than 100 launches in 2025?",
        "Will SpaceX have between 120-139 launches in 2025?",
        "Will SpaceX have between 180-199 launches in 2025?"
    ]
    
    print("\n   SPACEX MARKETS:")
    for question in spacex_questions:
        in_web = question in web_markets
        in_api = question in api_markets
        
        print(f"\n   - {question[:60]}")
        print(f"     On web page: {in_web}")
        print(f"     In API: {in_api}")
        
        if in_web:
            print(f"     Web data: {web_markets[question]}")
        if in_api:
            print(f"     API data: {api_markets[question]}")
    
    # Find markets only on web
    only_web = set(web_markets.keys()) - set(api_markets.keys())
    only_api = set(api_markets.keys()) - set(web_markets.keys())
    
    print(f"\n" + "=" * 80)
    print(f"SUMMARY:")
    print(f"  Markets on web page: {len(web_markets)}")
    print(f"  Markets in API: {len(api_markets)}")
    print(f"  Markets ONLY on web: {len(only_web)}")
    print(f"  Markets ONLY in API: {len(only_api)}")
    
    if len(only_web) > 0:
        print(f"\n  First 5 markets ONLY on web page:")
        for question in list(only_web)[:5]:
            print(f"    - {question[:60]}")
    
    if len(only_api) > 0:
        print(f"\n  First 5 markets ONLY in API:")
        for question in list(only_api)[:5]:
            print(f"    - {question[:60]}")

if __name__ == "__main__":
    asyncio.run(test_web_vs_api())

