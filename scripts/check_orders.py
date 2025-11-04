#!/usr/bin/env python3
"""
Check active orders on Polymarket CLOB
Shows all pending orders and locked USDC
"""

import os
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from py_clob_client.client import ClobClient
from dotenv import load_dotenv

def main():
    # Load environment variables
    load_dotenv()
    
    # Get wallet info
    private_key = os.getenv('WALLET_1_PRIVATE_KEY')
    if not private_key:
        print("❌ Error: WALLET_1_PRIVATE_KEY not found in .env")
        return
    
    # Remove '0x' prefix if present
    if private_key.startswith('0x'):
        private_key = private_key[2:]
    
    print("=" * 70)
    print("Polymarket Bot - Active Orders Checker")
    print("=" * 70)
    print()
    
    try:
        # Initialize CLOB client with private key
        client = ClobClient(
            host="https://clob.polymarket.com",
            key=private_key,
            chain_id=137  # Polygon mainnet
        )
        
        # Set API credentials
        client.set_api_creds(client.create_or_derive_api_creds())
        
        # Get wallet address
        from eth_account import Account
        wallet_address = Account.from_key(private_key).address
        
        print(f"Wallet: {wallet_address}")
        print()
        
        # Get open orders
        print("📋 Fetching open orders...")
        orders = client.get_orders()
        
        if not orders:
            print("✅ No active orders found")
            print()
            print("This means all your USDC.e is available (not locked)")
            return
        
        print(f"Found {len(orders)} active order(s)")
        print()
        
        # Calculate total locked USDC
        total_locked = 0.0
        
        # Group orders by market
        from collections import defaultdict
        orders_by_market = defaultdict(list)
        
        for order in orders:
            market_id = order.get('market', 'Unknown')
            orders_by_market[market_id].append(order)
        
        # Display orders
        for i, (market_id, market_orders) in enumerate(orders_by_market.items(), 1):
            print(f"Market {i}: {market_id}")
            
            for order in market_orders:
                order_id = order.get('id', 'N/A')
                side = order.get('side', 'N/A').upper()
                price = float(order.get('price', 0))
                size = float(order.get('size', 0))
                original_size = float(order.get('original_size', size))
                
                # Calculate locked amount
                locked = price * original_size
                total_locked += locked
                
                # Get status
                status = order.get('status', 'UNKNOWN')
                
                print(f"  ├─ Order: {order_id[:16]}...")
                print(f"  │  Side: {side}")
                print(f"  │  Price: ${price:.4f}")
                print(f"  │  Size: {size:.2f} (original: {original_size:.2f})")
                print(f"  │  Locked: ${locked:.2f}")
                print(f"  │  Status: {status}")
                print()
            
        print("=" * 70)
        print(f"TOTAL LOCKED USDC: ${total_locked:.2f}")
        print("=" * 70)
        print()
        
        # Recommendations
        print("💡 WHAT THIS MEANS:")
        print()
        print(f"  • ${total_locked:.2f} is LOCKED in pending orders")
        print("  • This USDC is NOT lost - it's just reserved")
        print("  • When orders fill → USDC converts to shares")
        print("  • When orders cancel → USDC returns to balance")
        print()
        print("🎯 TO FREE UP USDC:")
        print()
        print("  Option 1: Wait for orders to fill (automatic)")
        print("  Option 2: Cancel orders manually on Polymarket UI")
        print("  Option 3: Stop bot to prevent new orders")
        print()
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()

