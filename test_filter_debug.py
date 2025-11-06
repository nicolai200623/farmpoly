"""
Test Filter Logic - Debug
Kiem tra tai sao filter reject tat ca markets
"""

import asyncio
import sys
import yaml

# Add parent directory to path
sys.path.insert(0, '.')

from market_scanner_v2 import MarketScannerV2

async def test_filter():
    """Test filter logic"""
    
    # Load config
    with open('config.yaml', 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    
    scanner_config = config['market_scanner']
    
    print("=" * 80)
    print("TESTING FILTER LOGIC - DEBUG")
    print("=" * 80)
    
    print(f"\nCONFIG:")
    print(f"  min_reward: {scanner_config['min_reward']}")
    print(f"  max_competition_bars: {scanner_config['max_competition_bars']}")
    print(f"  target_categories: {scanner_config['target_categories']}")
    
    # Initialize scanner
    scanner = MarketScannerV2(scanner_config)
    
    # Fetch markets
    print(f"\nFETCHING MARKETS...")
    markets = await scanner.scan_rewards_page()
    
    print(f"\nRESULTS:")
    print(f"  Total markets fetched: {len(markets)}")
    
    if len(markets) == 0:
        print("\nNO MARKETS FETCHED!")
        print("   This means the API fetch failed or returned 0 markets")
    else:
        print(f"\n{len(markets)} markets passed all filters")
        
        # Show first 3 markets
        for i, market in enumerate(markets[:3]):
            print(f"\nMarket {i+1}:")
            print(f"  Question: {market['question'][:60]}")
            print(f"  Category: {market.get('category', 'unknown')}")
            print(f"  Reward: ${market['reward']:.0f}")
            print(f"  Competition: {market['competition_bars']} bars")
            print(f"  Min Size: {market.get('rewards_min_size', 0)}")
            print(f"  Max Spread: {market.get('rewards_max_spread', 0)}")

if __name__ == "__main__":
    asyncio.run(test_filter())

