#!/usr/bin/env python3
"""Check market IDs from log"""

import requests

# Market IDs to search
market_ids = ['657210', '657207', '666752', '666754']

for mid in market_ids:
    try:
        # Try Gamma API
        url = f'https://gamma-api.polymarket.com/markets/{mid}'
        resp = requests.get(url, timeout=5)
        if resp.status_code == 200:
            data = resp.json()
            print(f"Market {mid}: {data.get('question', 'Unknown')}")
            print(f"  - Slug: {data.get('slug', 'Unknown')}")
            print(f"  - Active: {data.get('active', 'Unknown')}")
            print(f"  - Closed: {data.get('closed', 'Unknown')}")
            print()
        else:
            print(f"Market {mid}: API returned {resp.status_code}")
            print()
    except Exception as e:
        print(f"Market {mid}: Error - {e}")
        print()

