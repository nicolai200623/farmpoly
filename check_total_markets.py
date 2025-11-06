"""
Check total number of markets on /rewards page
"""

import asyncio
import aiohttp
import json
import re
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def check_total():
    url = "https://polymarket.com/rewards"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
    }
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            html = await response.text()
            
            # Find __NEXT_DATA__ script
            pattern = r'<script id="__NEXT_DATA__" type="application/json">(.+?)</script>'
            match = re.search(pattern, html, re.DOTALL)
            
            if not match:
                logger.error("Could not find __NEXT_DATA__")
                return
            
            json_str = match.group(1)
            data = json.loads(json_str)
            
            # Navigate to markets data
            try:
                queries = data['props']['pageProps']['dehydratedState']['queries']
                
                # Find the query with markets data
                for query in queries:
                    query_data = query.get('state', {}).get('data', {})
                    
                    # Check if this has markets
                    if isinstance(query_data, dict) and 'data' in query_data:
                        markets = query_data['data']
                        count = query_data.get('count', 0)
                        total_count = query_data.get('total_count', 0)
                        
                        if isinstance(markets, list) and len(markets) > 0:
                            print("=" * 80)
                            print("FOUND MARKETS DATA")
                            print("=" * 80)
                            print(f"Markets in current response: {len(markets)}")
                            print(f"Count field: {count}")
                            print(f"Total count field: {total_count}")
                            print()
                            
                            # Check if there's pagination info
                            if 'next_cursor' in query_data:
                                print(f"Next cursor: {query_data['next_cursor']}")
                            
                            # Show first few markets
                            print("\nFirst 5 markets:")
                            for i, market in enumerate(markets[:5], 1):
                                question = market.get('question', 'N/A')
                                print(f"{i}. {question[:70]}")
                            
                            print("\n" + "=" * 80)
                            print("CONCLUSION")
                            print("=" * 80)
                            if total_count > len(markets):
                                print(f"WARNING: Only fetched {len(markets)} markets out of {total_count} total!")
                                print(f"Missing: {total_count - len(markets)} markets")
                                print("\nNeed to implement pagination to fetch all markets!")
                            else:
                                print(f"OK: Fetched all {len(markets)} markets")
                            
                            return
                
                logger.error("Could not find markets data in queries")
                
            except Exception as e:
                logger.error(f"Error parsing data: {e}")


if __name__ == "__main__":
    asyncio.run(check_total())

