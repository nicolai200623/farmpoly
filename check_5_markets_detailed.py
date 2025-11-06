"""
Check if the 5 markets from Telegram are on the official /rewards page
"""

import asyncio
import aiohttp
import json


async def check_gamma_api():
    """Check Gamma API for the 5 markets"""
    url = 'https://gamma-api.polymarket.com/events'
    
    search_terms = [
        "Bitcoin reach $120,000",
        "Ethereum hit $4,000",
        "Ethereum dip to $1,500",
        "SpaceX have less than 100 launches",
        "SpaceX have between 180-199 launches"
    ]
    
    params = {
        '_limit': 100,
        'closed': 'false',
        'archived': 'false'
    }
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            data = await response.json()
            
            print(f"Total events from Gamma API: {len(data)}")
            print("=" * 80)
            
            for term in search_terms:
                found = False
                for event in data:
                    markets = event.get('markets', [])
                    for market in markets:
                        question = market.get('question', '')
                        if term.lower() in question.lower():
                            print(f"\n✅ Found: {question}")
                            print(f"   rewardsMinSize: {market.get('rewardsMinSize')}")
                            print(f"   rewardsMaxSpread: {market.get('rewardsMaxSpread')}")
                            print(f"   active: {market.get('active')}")
                            print(f"   closed: {market.get('closed')}")
                            print(f"   volume: {market.get('volume')}")
                            print(f"   id: {market.get('id')}")
                            found = True
                            break
                    if found:
                        break
                
                if not found:
                    print(f"\n❌ NOT FOUND: {term}")


async def check_official_rewards_page():
    """Check official /rewards page using web scraping"""
    print("\n" + "=" * 80)
    print("CHECKING OFFICIAL /REWARDS PAGE")
    print("=" * 80)
    
    url = 'https://polymarket.com/rewards'
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            html = await response.text()
            
            search_terms = [
                "Bitcoin reach $120,000",
                "Ethereum hit $4,000",
                "Ethereum dip to $1,500",
                "SpaceX have less than 100 launches",
                "SpaceX have between 180-199 launches"
            ]
            
            for term in search_terms:
                if term.lower() in html.lower():
                    print(f"✅ Found on /rewards page: {term}")
                else:
                    print(f"❌ NOT on /rewards page: {term}")


if __name__ == "__main__":
    asyncio.run(check_gamma_api())
    asyncio.run(check_official_rewards_page())

