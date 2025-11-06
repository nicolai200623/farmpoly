"""
Check if Man City market has rewards
"""

import asyncio
import aiohttp
import json


async def check_market():
    # Check if 'Will Man City win the Premier League?' has rewards
    url = 'https://clob.polymarket.com/markets'
    
    async with aiohttp.ClientSession() as session:
        # Fetch first few pages
        next_cursor = None
        for page in range(10):
            params = {}
            if next_cursor:
                params['next_cursor'] = next_cursor
            
            async with session.get(url, params=params) as response:
                data = await response.json()
                markets = data.get('data', [])
                next_cursor = data.get('next_cursor')
                
                print(f"Page {page+1}: {len(markets)} markets")
                
                for market in markets:
                    question = market.get('question', '')
                    if 'Man City' in question and 'Premier League' in question:
                        rewards = market.get('rewards', {})
                        print("=" * 80)
                        print(f'✅ Found: {question}')
                        print(f'Rewards: {json.dumps(rewards, indent=2)}')
                        print(f'Active: {market.get("active")}')
                        print(f'Closed: {market.get("closed")}')
                        print(f'End Date: {market.get("end_date_iso")}')
                        print(f'Condition ID: {market.get("condition_id")}')
                        print("=" * 80)
                        return
                
                if not next_cursor or next_cursor == 'LTE=':
                    break
    
    print('❌ Market not found in first 10 pages')


if __name__ == "__main__":
    asyncio.run(check_market())

