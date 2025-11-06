import requests
import json
import re

def fetch_rewards_page():
    """Fetch and parse rewards from polymarket.com/rewards"""
    url = "https://polymarket.com/rewards"
    
    response = requests.get(url)
    html = response.text
    
    # Find the JSON data embedded in the page
    # Look for the pattern: {"props":{"pageProps":...
    # Try multiple patterns
    match = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.+?)</script>', html, re.DOTALL)

    if not match:
        # Try without id attribute
        match = re.search(r'<script type="application/json">(.+?)</script>', html, re.DOTALL)

    if not match:
        # Try to find any JSON with "markets" key
        match = re.search(r'"markets":\s*\[', html)
        if match:
            # Find the start of the JSON object containing this
            start = html.rfind('{', 0, match.start())
            # Find the matching closing brace (simplified - may not work for all cases)
            print("Found 'markets' in HTML, trying to extract JSON...")
            # Save a sample to debug
            with open('rewards_page_sample.html', 'w', encoding='utf-8') as f:
                f.write(html[:5000])
            print("Saved first 5000 chars to rewards_page_sample.html for debugging")
    
    if not match:
        print("❌ Could not find JSON data in page")
        return
    
    data = json.loads(match.group(1))
    
    # Navigate to the markets data
    try:
        markets_data = data['props']['pageProps']['dehydratedState']['queries']
        
        # Find the rewards query
        rewards_query = None
        for query in markets_data:
            if 'queryKey' in query and '/api/rewards' in str(query['queryKey']):
                rewards_query = query
                break
        
        if not rewards_query:
            print("❌ Could not find rewards query")
            return
        
        markets = rewards_query['state']['data']['markets']
        
        print("=" * 80)
        print(f"FOUND {len(markets)} MARKETS WITH REWARDS ON POLYMARKET.COM/REWARDS")
        print("=" * 80)
        
        # Show first 10 markets
        for i, market in enumerate(markets[:10]):
            print(f"\n{i+1}. {market['question'][:70]}")
            print(f"   Market ID: {market['market_id']}")
            print(f"   Volume 24h: ${market['volume_24hr']:.2f}")
            print(f"   Spread: {market['spread']:.2f}")
            
            # REWARDS INFO
            print(f"\n   REWARDS CONFIG:")
            if 'rewards_config' in market and market['rewards_config']:
                for config in market['rewards_config']:
                    print(f"     - Asset: {config['asset_address']}")
                    print(f"     - Rate per day: ${config['rate_per_day']}")
                    print(f"     - Start: {config['start_date']}")
                    print(f"     - End: {config['end_date']}")
            
            print(f"   rewards_max_spread: {market.get('rewards_max_spread', 'N/A')}")
            print(f"   rewards_min_size: {market.get('rewards_min_size', 'N/A')}")
            print(f"   earning_percentage: {market.get('earning_percentage', 'N/A')}")
            print(f"   market_competitiveness: {market.get('market_competitiveness', 'N/A')}")
        
        # Check if any Counter-Strike markets
        cs_markets = [m for m in markets if 'counter-strike' in m['question'].lower() or 'cs2' in m['question'].lower()]
        print(f"\n{'='*80}")
        print(f"COUNTER-STRIKE MARKETS: {len(cs_markets)}")
        print(f"{'='*80}")
        
        if cs_markets:
            for i, m in enumerate(cs_markets[:5]):
                print(f"\n{i+1}. {m['question'][:70]}")
                print(f"   Market ID: {m['market_id']}")
                print(f"   rewards_max_spread: {m.get('rewards_max_spread', 'N/A')}")
                print(f"   rewards_min_size: {m.get('rewards_min_size', 'N/A')}")
        else:
            print("\n⚠️  NO COUNTER-STRIKE MARKETS FOUND ON REWARDS PAGE!")
            
    except Exception as e:
        print(f"❌ Error parsing data: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    fetch_rewards_page()

