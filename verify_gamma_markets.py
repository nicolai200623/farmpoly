"""
Verify if Gamma API returns the markets that were reported as NOT on /rewards page
"""
import asyncio
from gamma_api_client import GammaAPIClient

async def main():
    api = GammaAPIClient()
    
    print("Fetching markets from Gamma API...")
    markets = await api.fetch_all_rewards_markets(limit=None)
    
    print(f"\n{'='*80}")
    print(f"GAMMA API RESULTS")
    print(f"{'='*80}")
    print(f"Total markets with rewards: {len(markets)}")
    
    # Markets that were reported as NOT on /rewards page
    search_terms = [
        ("Robinhood say 'Football'", "Will Robinhood say 'Football' during earnings call"),
        ("Los Angeles Clippers win the 2025", "Will the Los Angeles Clippers win the 2025–2026 NBA"),
        ("Atlanta Hawks make the NBA Playoffs", "Will the Atlanta Hawks make the NBA Playoffs"),
        ("Supreme Court rules in favor of Trump's tariffs", "Supreme Court rules in favor of Trump's tariffs"),
        ("Netflix dip to $1050", "Will Netflix dip to $1050 in November")
    ]
    
    print(f"\n{'='*80}")
    print(f"CHECKING MARKETS FROM TELEGRAM (reported as NOT on /rewards page)")
    print(f"{'='*80}\n")
    
    for short_term, full_term in search_terms:
        found = False
        for market in markets:
            question = market['question'].lower()
            if short_term.lower() in question or full_term.lower() in question:
                print(f"❌ FOUND IN GAMMA API (should NOT be here): {market['question'][:70]}")
                print(f"   Reward: ${market['reward']}")
                print(f"   Max Spread: {market['rewards_max_spread']}")
                print(f"   Min Size: {market['rewards_min_size']}")
                print(f"   URL: {market['url']}")
                print()
                found = True
                break
        
        if not found:
            print(f"✅ NOT FOUND in Gamma API (correct!): {short_term}")
    
    # Show top 10 markets from Gamma API
    print(f"\n{'='*80}")
    print(f"TOP 10 MARKETS FROM GAMMA API (by reward)")
    print(f"{'='*80}\n")
    
    sorted_markets = sorted(markets, key=lambda x: x['reward'], reverse=True)
    for i, market in enumerate(sorted_markets[:10], 1):
        print(f"{i}. {market['question'][:70]}")
        print(f"   Reward: ${market['reward']}")
        print(f"   Max Spread: {market['rewards_max_spread']}")
        print(f"   Min Size: {market['rewards_min_size']}")
        print(f"   Volume 24h: ${market['volume_24hr']:.0f}")
        print(f"   URL: {market['url']}")
        print()

if __name__ == "__main__":
    asyncio.run(main())

