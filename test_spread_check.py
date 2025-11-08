"""
Test script to check actual spreads of markets that were filtered
"""

import asyncio
import sys
from py_clob_client.client import ClobClient

async def check_market_spread(token_id: str, question: str):
    """Check spread for a market"""
    try:
        client = ClobClient(host='https://clob.polymarket.com')

        # Get orderbook
        book = await asyncio.to_thread(client.get_order_book, token_id)

        if hasattr(book, 'bids') and hasattr(book, 'asks'):
            has_bids = book.bids and len(book.bids) > 0
            has_asks = book.asks and len(book.asks) > 0

            if not (has_bids and has_asks):
                print(f"❌ No bids or asks")
                return

            best_bid = float(book.bids[0].price)
            best_ask = float(book.asks[0].price)

            spread = best_ask - best_bid
            mid_price = (best_bid + best_ask) / 2
            spread_pct = (spread / mid_price * 100) if mid_price > 0 else 999

            print(f"\n📊 {question[:60]}")
            print(f"   Best Bid: ${best_bid:.4f}")
            print(f"   Best Ask: ${best_ask:.4f}")
            print(f"   Spread: {spread:.4f} ({spread_pct:.1f}%)")
            print(f"   Bid depth: {len(book.bids)} orders")
            print(f"   Ask depth: {len(book.asks)} orders")

            if spread_pct > 50:
                print(f"   ❌ REJECTED (spread > 50%)")
            else:
                print(f"   ✅ PASSED (spread <= 50%)")

    except Exception as e:
        print(f"❌ Error: {e}")


async def main():
    """Test a few markets from the log"""

    # These are example token IDs - replace with actual ones from your log
    # You can get these by adding more logging in market_scanner_v2.py

    print("=" * 80)
    print("TESTING MARKET SPREADS")
    print("=" * 80)
    print("\nNote: Run this with actual token IDs from markets that were rejected")
    print("Add this to market_scanner_v2.py line 602 to see token IDs:")
    print('logger.info(f"Token ID: {clob_token_ids[0]} - {question[:60]}")')
    print("\nThen copy token IDs here and re-run this test")

if __name__ == "__main__":
    asyncio.run(main())
