"""
Debug script to check what markets are returned by Polymarket Rewards API
and verify if they exist on the /rewards page
"""
import asyncio
import aiohttp
from datetime import datetime

async def fetch_rewards_page():
    """Fetch first page from Polymarket Rewards API"""
    url = "https://polymarket.com/api/rewards/markets"
    
    params = {
        'orderBy': 'market',
        'position': 'DESC',
        'query': '',
        'showFavorites': 'false',
        'tagSlug': 'all',
        'nextCursor': 'MA==',  # Initial cursor
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
                return data
            else:
                print(f"Error: {response.status}")
                return None

async def main():
    print("Fetching markets from Polymarket Rewards API...")
    data = await fetch_rewards_page()
    
    if not data:
        print("Failed to fetch data")
        return
    
    markets = data.get('data', [])
    next_cursor = data.get('nextCursor')
    
    print(f"\n{'='*80}")
    print(f"API RESPONSE SUMMARY")
    print(f"{'='*80}")
    print(f"Total markets returned: {len(markets)}")
    print(f"Next cursor: {next_cursor}")
    print(f"Has more pages: {next_cursor is not None}")
    
    # Show first 10 markets
    print(f"\n{'='*80}")
    print(f"FIRST 10 MARKETS")
    print(f"{'='*80}\n")
    
    for i, market in enumerate(markets[:10], 1):
        question = market.get('question', 'N/A')
        market_id = market.get('market_id', 'N/A')
        
        # Extract reward
        reward = 0
        if 'rewards_config' in market and market['rewards_config']:
            for config in market['rewards_config']:
                reward += float(config.get('rate_per_day', 0))
        
        # Extract competition
        competition = market.get('market_competitiveness', 0)
        
        # Extract volume
        volume = market.get('volume_24hr', 0)
        
        # Extract end date
        end_date = market.get('end_date', 'N/A')
        if end_date != 'N/A':
            try:
                dt = datetime.fromisoformat(end_date.replace('Z', '+00:00'))
                end_date = dt.strftime('%Y-%m-%d %H:%M')
            except:
                pass
        
        print(f"{i}. {question[:70]}")
        print(f"   ID: {market_id}")
        print(f"   Reward: ${reward}")
        print(f"   Competition: {competition}")
        print(f"   Volume 24h: ${volume:.0f}")
        print(f"   End date: {end_date}")
        print()
    
    # Check if these are the same markets as in Telegram
    print(f"\n{'='*80}")
    print(f"CHECKING SPECIFIC MARKETS FROM TELEGRAM")
    print(f"{'='*80}\n")
    
    telegram_markets = [
        "Frankenstein",
        "The Bad Guys: Breaking In",
        "Nobody Wants This",
        "EdgeX FDV above $2B",
        "Nikkei 225 (NIK) Up or Down"
    ]
    
    for search_term in telegram_markets:
        found = False
        for market in markets:
            if search_term.lower() in market.get('question', '').lower():
                print(f"✅ FOUND: {market['question'][:70]}")
                print(f"   ID: {market.get('market_id')}")
                print(f"   End date: {market.get('end_date', 'N/A')}")
                found = True
                break
        
        if not found:
            print(f"❌ NOT FOUND: {search_term}")
    
    # Check pagination - try to fetch page 2
    print(f"\n{'='*80}")
    print(f"TESTING PAGINATION")
    print(f"{'='*80}\n")
    
    if next_cursor:
        print(f"Next cursor exists: {next_cursor}")
        print(f"Fetching page 2...")
        
        params = {
            'orderBy': 'market',
            'position': 'DESC',
            'query': '',
            'showFavorites': 'false',
            'tagSlug': 'all',
            'nextCursor': next_cursor,
            'requestPath': '/rewards/user/markets',
            'onlyMergeable': 'false',
            'noCompetition': 'false',
            'onlyOpenOrders': 'false',
            'onlyPositions': 'false'
        }
        
        async with aiohttp.ClientSession() as session:
            async with session.get("https://polymarket.com/api/rewards/markets", params=params) as response:
                if response.status == 200:
                    data2 = await response.json()
                    markets2 = data2.get('data', [])
                    next_cursor2 = data2.get('nextCursor')
                    
                    print(f"✅ Page 2 fetched successfully")
                    print(f"   Markets on page 2: {len(markets2)}")
                    print(f"   Next cursor: {next_cursor2}")
                    print(f"   Has more pages: {next_cursor2 is not None}")
                    
                    if markets2:
                        print(f"\n   First market on page 2:")
                        print(f"   {markets2[0].get('question', 'N/A')[:70]}")
                else:
                    print(f"❌ Failed to fetch page 2: {response.status}")
    else:
        print("❌ No next cursor - API says there are no more pages")

if __name__ == "__main__":
    asyncio.run(main())

