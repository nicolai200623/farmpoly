"""
Test Web Extract
Tim cach extract JSON tu trang /rewards
"""

import asyncio
import aiohttp
import json
import re

async def test_extract():
    """Extract JSON from web page"""
    
    print("=" * 80)
    print("EXTRACTING JSON FROM WEB PAGE")
    print("=" * 80)
    
    async with aiohttp.ClientSession() as session:
        async with session.get("https://polymarket.com/rewards", timeout=10) as response:
            html = await response.text()
            
            # Try different patterns
            patterns = [
                r'<script id="__NEXT_DATA__" type="application/json">(.+?)</script>',
                r'<script id="__NEXT_DATA__">(.+?)</script>',
                r'"data":\{"data":\[(.+?)\]',
                r'window\.__NEXT_DATA__\s*=\s*(.+?)</script>',
            ]
            
            for i, pattern in enumerate(patterns):
                print(f"\nTrying pattern {i+1}...")
                match = re.search(pattern, html, re.DOTALL)
                if match:
                    print(f"  FOUND! Length: {len(match.group(1))}")
                    
                    # Try to parse as JSON
                    try:
                        data = json.loads(match.group(1))
                        print(f"  Successfully parsed JSON")
                        print(f"  Keys: {list(data.keys())[:10]}")
                        
                        # Try to find markets
                        if 'props' in data:
                            print(f"  Found 'props' key")
                            if 'pageProps' in data['props']:
                                print(f"  Found 'pageProps' key")
                                if 'dehydratedState' in data['props']['pageProps']:
                                    print(f"  Found 'dehydratedState' key")
                                    queries = data['props']['pageProps']['dehydratedState'].get('queries', [])
                                    print(f"  Found {len(queries)} queries")
                                    
                                    if len(queries) > 0:
                                        first_query = queries[0]
                                        print(f"  First query keys: {list(first_query.keys())}")
                                        
                                        if 'state' in first_query:
                                            state = first_query['state']
                                            print(f"  State keys: {list(state.keys())}")
                                            
                                            if 'data' in state:
                                                state_data = state['data']
                                                print(f"  Data keys: {list(state_data.keys())}")
                                                
                                                if 'data' in state_data:
                                                    markets = state_data['data']
                                                    print(f"  FOUND {len(markets)} MARKETS!")
                                                    
                                                    # Show first market
                                                    if len(markets) > 0:
                                                        first_market = markets[0]
                                                        print(f"\n  First market:")
                                                        print(f"    Question: {first_market.get('question', 'N/A')}")
                                                        print(f"    Market ID: {first_market.get('market_id', 'N/A')}")
                                                        print(f"    Rewards Min Size: {first_market.get('rewards_min_size', 'N/A')}")
                                                        print(f"    Rewards Max Spread: {first_market.get('rewards_max_spread', 'N/A')}")
                                    
                                    return
                        
                    except json.JSONDecodeError as e:
                        print(f"  Failed to parse JSON: {e}")
                else:
                    print(f"  Not found")
            
            # If all patterns fail, search for "SpaceX" in HTML
            print(f"\n\nSearching for 'SpaceX' in HTML...")
            if 'SpaceX' in html:
                print(f"  FOUND 'SpaceX' in HTML!")
                
                # Find context around SpaceX
                spacex_index = html.find('SpaceX')
                context_start = max(0, spacex_index - 200)
                context_end = min(len(html), spacex_index + 200)
                context = html[context_start:context_end]
                
                print(f"\n  Context around 'SpaceX':")
                print(f"  {context[:400]}")
            else:
                print(f"  'SpaceX' NOT FOUND in HTML!")
                print(f"\n  This means SpaceX markets are NOT on the /rewards page")

if __name__ == "__main__":
    asyncio.run(test_extract())

