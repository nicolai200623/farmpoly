"""
Check what fields the /rewards API returns
"""
import asyncio
import aiohttp

async def check_fields():
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
                print("📋 Fields in first market:")
                print("=" * 80)
                first_market = markets[0]
                for key, value in first_market.items():
                    value_str = str(value)[:100] if value else "None"
                    print(f"   {key}: {value_str}")
                
                print("\n" + "=" * 80)
                print("🔍 Checking for slug field:")
                print("=" * 80)
                print(f"   'slug' in market: {'slug' in first_market}")
                print(f"   'slug' value: {first_market.get('slug', 'NOT FOUND')}")
                print(f"   'market_slug' value: {first_market.get('market_slug', 'NOT FOUND')}")
                print(f"   'question_slug' value: {first_market.get('question_slug', 'NOT FOUND')}")

if __name__ == "__main__":
    asyncio.run(check_fields())

