"""
Test position-based pricing with REAL markets from Polymarket
"""

import asyncio
import logging
import yaml
from market_scanner_v2 import MarketScannerV2
from order_manager import OrderManager

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


async def test_real_market_pricing():
    """Test pricing logic with real markets"""
    
    # Load config
    with open('config.yaml', 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    
    # Create scanner and order manager
    scanner = MarketScannerV2(config['market_scanner'])
    order_mgr = OrderManager(config['order_management'])
    
    print("=" * 80)
    print("TESTING POSITION-BASED PRICING WITH REAL MARKETS")
    print("=" * 80)
    
    # Scan for markets
    print("\nScanning for markets with rewards...")
    markets = await scanner.scan_rewards_page()

    if not markets:
        print("\nNo markets found with rewards!")
        print("\nThis is expected if:")
        print("  1. No markets match your category filter (sports)")
        print("  2. No markets have rewardsMinSize > 0 AND rewardsMaxSpread > 0")
        print("\nTo test with crypto markets, change config.yaml:")
        print("  target_categories:")
        print("    - crypto")
        return

    print(f"\nFound {len(markets)} markets with rewards")
    
    # Test pricing for first 3 markets
    for i, market in enumerate(markets[:3]):
        print(f"\n{'=' * 80}")
        print(f"MARKET {i+1}: {market['question'][:70]}")
        print(f"{'=' * 80}")
        print(f"  Category: {market.get('category', 'unknown')}")
        print(f"  Estimated Reward: ${market['reward']:.0f}")
        print(f"  Max Spread: {market.get('rewards_max_spread', 0)}%")
        print(f"  Min Size: {market.get('rewards_min_size', 0)}")
        
        # Prepare order
        print(f"\nPreparing order...")
        order = await order_mgr.prepare_market_order(market)

        if order:
            print(f"\nOrder prepared successfully!")
            print(f"\n  YES Order:")
            print(f"    - Price: ${order['yes_order']['price']:.4f} ({order['yes_order']['price']*100:.2f}¢)")
            print(f"    - Size: {order['yes_order']['size']} shares")
            print(f"    - Target Position: #{order['position_info'].get('target_position', 3)}")

            print(f"\n  NO Order:")
            print(f"    - Price: ${order['no_order']['price']:.4f} ({order['no_order']['price']*100:.2f}¢)")
            print(f"    - Size: {order['no_order']['size']} shares")
            print(f"    - Target Position: #{order['position_info'].get('target_position', 3)}")

            print(f"\n  Position Info:")
            print(f"    - Position #1 (Best Bid): ${order['position_info']['best_bid']:.4f} ({order['position_info']['best_bid']*100:.2f}¢)")
            print(f"    - Position #2 (Bid): ${order['position_info']['second_bid']:.4f} ({order['position_info']['second_bid']*100:.2f}¢)")
            print(f"    - Position #1 (Best Ask): ${order['position_info']['best_ask']:.4f} ({order['position_info']['best_ask']*100:.2f}¢)")
            print(f"    - Position #2 (Ask): ${order['position_info']['second_ask']:.4f} ({order['position_info']['second_ask']*100:.2f}¢)")
            print(f"    - Offset from position #2: ${order['position_info']['offset']:.4f} ({order['position_info']['offset']*100:.2f}¢)")
            print(f"    - Spread: {order['position_info']['spread']:.2%}")
            print(f"    - Max spread allowed: {order['position_info']['max_spread_allowed']:.2%}")
            print(f"    - Order book depth: {order['position_info']['num_bids']} bids, {order['position_info']['num_asks']} asks")

            # Verify within max spread
            if order['position_info']['spread'] <= order['position_info']['max_spread_allowed']:
                print(f"\n  PASS: Orders are within max spread!")
            else:
                print(f"\n  FAIL: Orders exceed max spread!")
        else:
            print(f"\nFailed to prepare order")
    
    print(f"\n{'=' * 80}")
    print("TEST COMPLETE")
    print(f"{'=' * 80}")


if __name__ == "__main__":
    asyncio.run(test_real_market_pricing())

