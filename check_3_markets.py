"""
Check if the 3 markets from Telegram are actually active
"""

import asyncio
import aiohttp
import json


async def check_markets():
    url = 'https://clob.polymarket.com/markets'
    
    search_terms = [
        "Lil Pump",
        "Pittsburgh",
        "Ansem"
    ]
    
    async with aiohttp.ClientSession() as session:
        next_cursor = None
        for page in range(20):
            params = {}
            if next_cursor:
                params['next_cursor'] = next_cursor
            
            async with session.get(url, params=params) as response:
                data = await response.json()
                markets = data.get('data', [])
                next_cursor = data.get('next_cursor')
                
                for market in markets:
                    question = market.get('question', '')
                    for term in search_terms:
                        if term in question:
                            rewards = market.get('rewards', {})
                            print("=" * 80)
                            print(f'Question: {question}')
                            print(f'Rewards: {json.dumps(rewards, indent=2)}')
                            print(f'Active: {market.get("active")}')
                            print(f'Closed: {market.get("closed")}')
                            print(f'End Date: {market.get("end_date_iso")}')
                            print(f'Volume: {market.get("volume", 0)}')
                            print(f'Condition ID: {market.get("condition_id")}')
                            print("=" * 80)
                            search_terms.remove(term)
                            break
                
                if not search_terms:
                    print("\n✅ Found all 3 markets!")
                    return
                
                if not next_cursor or next_cursor == 'LTE=':
                    break
    
    print(f"\n❌ Could not find: {search_terms}")


if __name__ == "__main__":
    asyncio.run(check_markets())

