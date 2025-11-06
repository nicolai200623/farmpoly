"""
Check tokens field in /rewards API response
"""
import asyncio
import aiohttp
import json

async def check_tokens():
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
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Referer': 'https://polymarket.com/rewards',
        'Origin': 'https://polymarket.com'
    }
    
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url, params=params) as response:
            data = await response.json()
            
            if isinstance(data, list):
                markets = data
            else:
                markets = data.get('data', [])
            
            if markets:
                print("=" * 80)
                print("📋 Checking 'tokens' field in first 5 markets:")
                print("=" * 80)
                
                for i, market in enumerate(markets[:5]):
                    print(f"\n{i+1}. {market.get('question', 'NO QUESTION')[:60]}...")
                    
                    tokens = market.get('tokens', [])
                    print(f"   Tokens count: {len(tokens)}")
                    
                    if tokens:
                        print(f"   Tokens:")
                        for token in tokens:
                            token_id = token.get('token_id', 'NO ID')
                            outcome = token.get('outcome', 'NO OUTCOME')
                            print(f"      - {outcome}: {token_id}")
                    else:
                        print(f"   ❌ NO TOKENS!")
                
                # Check if all markets have tokens
                markets_with_tokens = [m for m in markets if m.get('tokens') and len(m['tokens']) > 0]
                print(f"\n" + "=" * 80)
                print(f"📊 Summary:")
                print(f"   Total markets: {len(markets)}")
                print(f"   Markets with tokens: {len(markets_with_tokens)}")
                print(f"   Markets without tokens: {len(markets) - len(markets_with_tokens)}")

if __name__ == "__main__":
    asyncio.run(check_tokens())

