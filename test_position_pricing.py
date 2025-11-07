"""
Test script to verify position-based pricing logic
"""

import asyncio
import logging
from order_manager import OrderManager

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


async def test_position_pricing():
    """Test the position-based pricing logic"""
    
    # Mock config
    config = {
        'spread_min': 0.05,
        'spread_max': 0.12,
        'size_min': 100,
        'size_max': 500,
        'clob': {
            'host': 'https://clob.polymarket.com',
            'chain_id': 137
        }
    }
    
    # Create OrderManager
    order_mgr = OrderManager(config)
    
    # Test Case 1: Normal order book with enough depth
    mock_order_book_normal = {
        'bids': [
            {'price': 0.52, 'size': 100},  # Position 1 (best bid)
            {'price': 0.51, 'size': 150},  # Position 2
            {'price': 0.50, 'size': 200},  # Position 3
            {'price': 0.49, 'size': 100},  # Position 4
        ],
        'asks': [
            {'price': 0.55, 'size': 100},  # Position 1 (best ask)
            {'price': 0.56, 'size': 150},  # Position 2
            {'price': 0.57, 'size': 200},  # Position 3
            {'price': 0.58, 'size': 100},  # Position 4
        ]
    }

    # Test Case 2: Thin order book (only 1 order on each side)
    mock_order_book_thin = {
        'bids': [
            {'price': 0.52, 'size': 100},  # Only 1 bid
        ],
        'asks': [
            {'price': 0.55, 'size': 100},  # Only 1 ask
        ]
    }

    # Test Case 3: Asymmetric order book (2 bids, 1 ask)
    mock_order_book_asymmetric = {
        'bids': [
            {'price': 0.52, 'size': 100},
            {'price': 0.51, 'size': 150},
        ],
        'asks': [
            {'price': 0.55, 'size': 100},  # Only 1 ask
        ]
    }
    
    # Test scenarios
    test_scenarios = [
        {
            'name': 'NORMAL ORDER BOOK (4 bids, 4 asks)',
            'order_book': mock_order_book_normal,
            'should_pass': True
        },
        {
            'name': 'THIN ORDER BOOK (1 bid, 1 ask) - SHOULD REJECT',
            'order_book': mock_order_book_thin,
            'should_pass': False
        },
        {
            'name': 'ASYMMETRIC ORDER BOOK (2 bids, 1 ask) - SHOULD REJECT',
            'order_book': mock_order_book_asymmetric,
            'should_pass': False
        }
    ]

    print("=" * 80)
    print("TESTING POSITION-BASED PRICING WITH ORDER BOOK DEPTH CHECK")
    print("=" * 80)

    for scenario in test_scenarios:
        order_book = scenario['order_book']
        name = scenario['name']
        should_pass = scenario['should_pass']

        # Create market data for this scenario
        bids = order_book['bids']
        asks = order_book['asks']

        if bids and asks:
            mid_price = (bids[0]['price'] + asks[0]['price']) / 2
        else:
            mid_price = 0.535

        mock_market_data = {
            'mid_price': mid_price,
            'best_bid': bids[0]['price'] if bids else 0,
            'best_ask': asks[0]['price'] if asks else 0,
            'current_spread': (asks[0]['price'] - bids[0]['price']) if (bids and asks) else 0,
            'bid_volume': sum(b['size'] for b in bids),
            'ask_volume': sum(a['size'] for a in asks),
            'order_book': order_book
        }

        print(f"\n{'=' * 80}")
        print(f"TEST: {name}")
        print(f"{'=' * 80}")
        print(f"  Order Book Depth: {len(bids)} bids, {len(asks)} asks")
        print(f"  Expected Result: {'ACCEPT' if should_pass else 'REJECT'}")

        # Test with 3.5% max spread
        max_spread = 0.035
        yes_price, no_price, position_info = order_mgr._calculate_position_based_prices(
            mock_market_data,
            max_spread
        )

        if yes_price is None or no_price is None:
            print(f"\n  Result: REJECTED (no prices calculated)")
            if not should_pass:
                print(f"  ✅ PASS: Correctly rejected thin order book")
            else:
                print(f"  ❌ FAIL: Should have accepted this order book!")
        else:
            print(f"\n  Result: ACCEPTED")
            print(f"    Position #2 Bid: ${position_info.get('second_bid', 0):.4f} ({position_info.get('second_bid', 0)*100:.2f}¢)")
            print(f"    Position #2 Ask: ${position_info.get('second_ask', 0):.4f} ({position_info.get('second_ask', 0)*100:.2f}¢)")
            print(f"    Our YES bid (Position #3): ${yes_price:.4f} ({yes_price*100:.2f}¢)")
            print(f"    Our NO bid (Position #3): ${no_price:.4f} ({no_price*100:.2f}¢)")
            print(f"    Spread: {position_info.get('spread', 0):.2%}")
            print(f"    Offset from position #2: ${position_info.get('offset', 0):.4f} ({position_info.get('offset', 0)*100:.2f}¢)")

            if should_pass:
                print(f"  ✅ PASS: Correctly accepted normal order book")
            else:
                print(f"  ❌ FAIL: Should have rejected this order book!")
    
    print(f"\n{'=' * 80}")
    print("TEST COMPLETE")
    print(f"{'=' * 80}")


if __name__ == "__main__":
    asyncio.run(test_position_pricing())

