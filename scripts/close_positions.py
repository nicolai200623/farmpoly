#!/usr/bin/env python3
"""
Close positions on Polymarket
Sell shares to realize profits/losses
"""

import os
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from py_clob_client.client import ClobClient
from py_clob_client.clob_types import OrderArgs
from py_clob_client.order_builder.constants import BUY, SELL
from dotenv import load_dotenv
from eth_account import Account

def main():
    # Load environment variables
    load_dotenv()
    
    # Get wallet info
    private_key = os.getenv('WALLET_1_PRIVATE_KEY') or os.getenv('WALLET_1_PK')
    if not private_key:
        print("❌ Error: WALLET_1_PRIVATE_KEY or WALLET_1_PK not found in .env")
        return
    
    # Remove '0x' prefix if present
    if private_key.startswith('0x'):
        private_key = private_key[2:]
    
    print("=" * 70)
    print("Polymarket Bot - Close Positions")
    print("=" * 70)
    print()
    
    try:
        # Initialize CLOB client
        client = ClobClient(
            host="https://clob.polymarket.com",
            key=private_key,
            chain_id=137
        )
        
        # Set API credentials
        client.set_api_creds(client.create_or_derive_api_creds())
        
        # Get wallet address
        wallet_address = Account.from_key(private_key).address
        print(f"Wallet: {wallet_address}")
        print()
        
        # Get positions (filled orders)
        print("📋 Fetching positions...")
        
        # Get all orders (including filled)
        orders = client.get_orders()
        
        # Filter for filled orders (these are positions)
        positions = {}
        for order in orders:
            if order.get('status') == 'FILLED' or order.get('original_size', 0) > order.get('size', 0):
                market = order.get('market', 'Unknown')
                token_id = order.get('asset_id', order.get('token_id', 'Unknown'))
                
                if market not in positions:
                    positions[market] = {}
                
                if token_id not in positions[market]:
                    positions[market][token_id] = {
                        'shares': 0,
                        'avg_price': 0,
                        'total_cost': 0,
                        'orders': []
                    }
                
                filled_size = order.get('original_size', 0) - order.get('size', 0)
                fill_price = float(order.get('price', 0))
                
                pos = positions[market][token_id]
                pos['shares'] += filled_size
                pos['total_cost'] += filled_size * fill_price
                pos['orders'].append(order)
        
        # Calculate average prices
        for market in positions:
            for token_id in positions[market]:
                pos = positions[market][token_id]
                if pos['shares'] > 0:
                    pos['avg_price'] = pos['total_cost'] / pos['shares']
        
        if not positions:
            print("✅ No positions found")
            print()
            print("This means:")
            print("  • All your orders are still pending (not filled)")
            print("  • Or you have already closed all positions")
            return
        
        # Display positions
        print(f"Found {len(positions)} position(s)")
        print()
        
        position_list = []
        for i, (market, tokens) in enumerate(positions.items(), 1):
            for token_id, pos in tokens.items():
                if pos['shares'] > 0:
                    # Get current price from orderbook
                    try:
                        orderbook = client.get_order_book(token_id)
                        
                        # Get best bid (price we can sell at)
                        best_bid = 0
                        if hasattr(orderbook, 'bids') and len(orderbook.bids) > 0:
                            best_bid = float(orderbook.bids[0].price)
                        
                        current_value = pos['shares'] * best_bid
                        pnl = current_value - pos['total_cost']
                        pnl_pct = (pnl / pos['total_cost'] * 100) if pos['total_cost'] > 0 else 0
                        
                        print(f"Position {len(position_list) + 1}:")
                        print(f"  Market: {market}")
                        print(f"  Token ID: {token_id}")
                        print(f"  Shares: {pos['shares']:.2f}")
                        print(f"  Avg Buy Price: ${pos['avg_price']:.4f}")
                        print(f"  Current Price: ${best_bid:.4f}")
                        print(f"  Cost: ${pos['total_cost']:.2f}")
                        print(f"  Current Value: ${current_value:.2f}")
                        
                        if pnl >= 0:
                            print(f"  P&L: +${pnl:.2f} (+{pnl_pct:.2f}%) ✅")
                        else:
                            print(f"  P&L: -${abs(pnl):.2f} ({pnl_pct:.2f}%) ❌")
                        
                        print()
                        
                        position_list.append({
                            'market': market,
                            'token_id': token_id,
                            'shares': pos['shares'],
                            'avg_price': pos['avg_price'],
                            'current_price': best_bid,
                            'pnl': pnl,
                            'pnl_pct': pnl_pct
                        })
                        
                    except Exception as e:
                        print(f"  ⚠️  Could not get current price: {e}")
                        print()
        
        if not position_list:
            print("✅ No active positions to close")
            return
        
        # Ask user which position to close
        print("=" * 70)
        print("Which position do you want to close?")
        print()
        for i, pos in enumerate(position_list, 1):
            pnl_str = f"+${pos['pnl']:.2f}" if pos['pnl'] >= 0 else f"-${abs(pos['pnl']):.2f}"
            print(f"  {i}. Market {pos['market'][:30]}... ({pnl_str})")
        print(f"  0. Cancel")
        print()
        
        choice = input("Enter number (0 to cancel): ").strip()
        
        if choice == '0':
            print("Cancelled.")
            return
        
        try:
            choice_idx = int(choice) - 1
            if choice_idx < 0 or choice_idx >= len(position_list):
                print("❌ Invalid choice")
                return
        except ValueError:
            print("❌ Invalid input")
            return
        
        selected_pos = position_list[choice_idx]
        
        # Confirm
        print()
        print("=" * 70)
        print("You are about to SELL:")
        print(f"  Shares: {selected_pos['shares']:.2f}")
        print(f"  Current Price: ${selected_pos['current_price']:.4f}")
        print(f"  You will receive: ~${selected_pos['shares'] * selected_pos['current_price']:.2f} USDC")
        print(f"  P&L: ${selected_pos['pnl']:.2f} ({selected_pos['pnl_pct']:.2f}%)")
        print()
        
        confirm = input("Confirm? (yes/no): ").strip().lower()
        
        if confirm not in ['yes', 'y']:
            print("Cancelled.")
            return
        
        # Place SELL order
        print()
        print("📤 Placing SELL order...")
        
        # Create sell order slightly below best bid to ensure fill
        sell_price = selected_pos['current_price'] * 0.99  # 1% below best bid
        
        order_args = OrderArgs(
            token_id=selected_pos['token_id'],
            price=sell_price,
            size=selected_pos['shares'],
            side=SELL
        )
        
        # Sign and submit
        signed_order = client.create_order(order_args)
        response = client.post_order(signed_order)
        
        if response and 'orderID' in response:
            print(f"✅ SELL order placed successfully!")
            print(f"   Order ID: {response['orderID']}")
            print()
            print("💡 Your order is now on the orderbook.")
            print("   It should fill within a few seconds/minutes.")
            print()
            print("   Check status:")
            print(f"   • Polymarket UI: https://polymarket.com/profile")
            print(f"   • Or run: python scripts/check_orders.py")
        else:
            print(f"❌ Failed to place order: {response}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()

