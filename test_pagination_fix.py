"""
Test if pagination works after fixing the bug
"""
import asyncio
import sys
sys.path.insert(0, '.')

from polymarket_rewards_api import PolymarketRewardsAPI

async def main():
    api = PolymarketRewardsAPI()
    
    print("Testing pagination with fixed code...")
    print("Fetching first 500 markets (should take ~5 pages)")
    print()
    
    markets = await api.fetch_all_rewards_markets(limit=500)
    
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

if __name__ == "__main__":
    asyncio.run(main())

