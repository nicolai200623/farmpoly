"""
Check total_count and next_cursor from API response
"""
import asyncio
import aiohttp
import json

async def main():
    url = "https://polymarket.com/api/rewards/markets"
    
    params = {
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
    }
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            if response.status == 200:
                data = await response.json()
                
                print(f"{'='*80}")
                print(f"API RESPONSE METADATA")
                print(f"{'='*80}")
                print(f"limit: {data.get('limit')}")
                print(f"count: {data.get('count')}")
                print(f"total_count: {data.get('total_count')}")
                print(f"next_cursor: {data.get('next_cursor')}")
                print(f"next_cursor type: {type(data.get('next_cursor'))}")
                print(f"next_cursor is None: {data.get('next_cursor') is None}")
                
                print(f"\n{'='*80}")
                print(f"FULL RESPONSE KEYS")
                print(f"{'='*80}")
                for key, value in data.items():
                    if key != 'data':
                        print(f"{key}: {value}")
                
                # Try to fetch page 2 with different cursor values
                print(f"\n{'='*80}")
                print(f"TESTING DIFFERENT CURSOR VALUES")
                print(f"{'='*80}\n")
                
                # Test 1: Use the next_cursor from response (even if None)
                next_cursor = data.get('next_cursor')
                if next_cursor:
                    print(f"Test 1: Using next_cursor from response: {next_cursor}")
                    params['nextCursor'] = next_cursor
                    
                    async with session.get(url, params=params) as response2:
                        if response2.status == 200:
                            data2 = await response2.json()
                            print(f"  ✅ Success! Got {len(data2.get('data', []))} markets")
                            print(f"  Next cursor: {data2.get('next_cursor')}")
                        else:
                            print(f"  ❌ Failed: {response2.status}")
                else:
                    print(f"Test 1: ❌ No next_cursor in response")
                
                # Test 2: Try cursor = "100" (offset-based)
                print(f"\nTest 2: Using cursor = '100' (offset-based)")
                params['nextCursor'] = '100'
                
                async with session.get(url, params=params) as response2:
                    if response2.status == 200:
                        data2 = await response2.json()
                        markets2 = data2.get('data', [])
                        print(f"  ✅ Success! Got {len(markets2)} markets")
                        if markets2:
                            print(f"  First market: {markets2[0].get('question', 'N/A')[:70]}")
                    else:
                        print(f"  ❌ Failed: {response2.status}")
                
                # Test 3: Try cursor = base64 encoded "100"
                import base64
                cursor_100 = base64.b64encode(b"100").decode()
                print(f"\nTest 3: Using cursor = base64('100') = '{cursor_100}'")
                params['nextCursor'] = cursor_100
                
                async with session.get(url, params=params) as response2:
                    if response2.status == 200:
                        data2 = await response2.json()
                        markets2 = data2.get('data', [])
                        print(f"  ✅ Success! Got {len(markets2)} markets")
                        if markets2:
                            print(f"  First market: {markets2[0].get('question', 'N/A')[:70]}")
                    else:
                        print(f"  ❌ Failed: {response2.status}")
                
                # Test 4: Try without nextCursor parameter
                print(f"\nTest 4: Without nextCursor parameter")
                params_no_cursor = params.copy()
                del params_no_cursor['nextCursor']
                
                async with session.get(url, params=params_no_cursor) as response2:
                    if response2.status == 200:
                        data2 = await response2.json()
                        markets2 = data2.get('data', [])
                        print(f"  ✅ Success! Got {len(markets2)} markets")
                        print(f"  Next cursor: {data2.get('next_cursor')}")
                    else:
                        print(f"  ❌ Failed: {response2.status}")
                
                # Test 5: Try with offset parameter
                print(f"\nTest 5: Using offset=100 parameter")
                params_offset = params.copy()
                params_offset['offset'] = '100'
                
                async with session.get(url, params=params_offset) as response2:
                    if response2.status == 200:
                        data2 = await response2.json()
                        markets2 = data2.get('data', [])
                        print(f"  ✅ Success! Got {len(markets2)} markets")
                        if markets2:
                            print(f"  First market: {markets2[0].get('question', 'N/A')[:70]}")
                    else:
                        print(f"  ❌ Failed: {response2.status}")

if __name__ == "__main__":
    asyncio.run(main())

