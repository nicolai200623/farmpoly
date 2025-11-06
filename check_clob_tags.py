"""
Check if CLOB API has tags field
"""

import asyncio
import aiohttp
import json


async def check_tags():
    url = "https://clob.polymarket.com/markets"
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            markets = data.get('data', [])
            
            # Check first market with rewards
            for market in markets:
                rewards = market.get('rewards')
                if rewards and rewards.get('min_size', 0) > 0:
                    print("=" * 80)
                    print("FIRST MARKET WITH REWARDS")
                    print("=" * 80)
                    print(f"Question: {market.get('question')}")
                    print(f"Tags: {market.get('tags')}")
                    print(f"Description: {market.get('description', '')[:200]}")
                    break


if __name__ == "__main__":
    asyncio.run(check_tags())

