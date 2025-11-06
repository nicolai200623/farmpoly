"""
Test fetching ALL markets (2891 markets)
"""
import asyncio
import sys
sys.path.insert(0, '.')

from polymarket_rewards_api import PolymarketRewardsAPI

async def main():
    api = PolymarketRewardsAPI()
    
    print("Fetching ALL markets with rewards...")
    print("This should fetch ~2,891 markets (may take 1-2 minutes)")
    print()
    
    markets = await api.fetch_all_rewards_markets(limit=None)
    
    print(f"\n{'='*80}")
    print(f"RESULTS")
    print(f"{'='*80}")
    print(f"Total markets fetched: {len(markets)}")
    
    if markets:
        print(f"\nFirst market:")
        print(f"  {markets[0]['question'][:70]}")
        print(f"  Reward: ${markets[0]['reward']}")
        
        print(f"\nLast market:")
        print(f"  {markets[-1]['question'][:70]}")
        print(f"  Reward: ${markets[-1]['reward']}")
        
        # Check for duplicates
        market_ids = [m['market_id'] for m in markets]
        unique_ids = set(market_ids)
        
        print(f"\nDuplicate check:")
        print(f"  Total markets: {len(markets)}")
        print(f"  Unique IDs: {len(unique_ids)}")
        print(f"  Duplicates: {len(markets) - len(unique_ids)}")
        
        # Show reward distribution
        rewards = [m['reward'] for m in markets]
        print(f"\nReward distribution:")
        print(f"  Min: ${min(rewards)}")
        print(f"  Max: ${max(rewards)}")
        print(f"  Average: ${sum(rewards)/len(rewards):.2f}")
        
        # Count by reward ranges
        reward_ranges = {
            '$0-10': 0,
            '$10-50': 0,
            '$50-100': 0,
            '$100-200': 0
        }
        
        for r in rewards:
            if r < 10:
                reward_ranges['$0-10'] += 1
            elif r < 50:
                reward_ranges['$10-50'] += 1
            elif r < 100:
                reward_ranges['$50-100'] += 1
            else:
                reward_ranges['$100-200'] += 1
        
        print(f"\nReward ranges:")
        for range_name, count in reward_ranges.items():
            print(f"  {range_name}: {count} markets ({count/len(markets)*100:.1f}%)")
        
        # Check if Frankenstein market exists
        print(f"\n{'='*80}")
        print(f"CHECKING SPECIFIC MARKETS")
        print(f"{'='*80}\n")
        
        search_terms = [
            "Frankenstein",
            "The Bad Guys: Breaking In",
            "Nobody Wants This",
            "EdgeX FDV above $2B",
            "Nikkei 225 (NIK) Up or Down"
        ]
        
        for term in search_terms:
            found = False
            for market in markets:
                if term.lower() in market['question'].lower():
                    print(f"✅ FOUND: {market['question'][:70]}")
                    print(f"   Reward: ${market['reward']}")
                    print(f"   ID: {market['market_id']}")
                    found = True
                    break
            
            if not found:
                print(f"❌ NOT FOUND: {term}")

if __name__ == "__main__":
    asyncio.run(main())

