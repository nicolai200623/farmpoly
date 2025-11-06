"""
Script to check and sell positions using Polymarket Data API
Run this on VPS where the bot is running
"""
import os
import sys
import json
import requests
from dotenv import load_dotenv
from py_clob_client.client import ClobClient
from py_clob_client.clob_types import OrderArgs, OrderType

# Load environment variables
load_dotenv()


def check_positions():
    """Check positions using Polymarket Data API"""
    try:
        # Get wallet private key
        private_key = os.getenv("WALLET_1_PK")
        if not private_key:
            print("❌ WALLET_1_PK not found in .env")
            return None
        
        # Get wallet address
        from web3 import Web3
        w3 = Web3()
        account = w3.eth.account.from_key(private_key)
        wallet_address = account.address
        
        print(f"🔍 Checking positions for wallet: {wallet_address[:10]}...{wallet_address[-8:]}")
        
        # Use Polymarket Data API
        data_api_url = "https://data-api.polymarket.com/positions"
        params = {
            "user": wallet_address,
            "sizeThreshold": 0.01,
            "limit": 500
        }
        
        print(f"\n📊 Fetching positions from Polymarket Data API...")
        
        response = requests.get(data_api_url, params=params)
        
        if response.status_code == 200:
            positions = response.json()
            
            if len(positions) > 0:
                print(f"   Found {len(positions)} positions\n")
                print("=" * 100)
                print("📋 ACTIVE POSITIONS:")
                print("=" * 100 + "\n")
                
                total_value = 0
                total_pnl = 0
                
                for i, pos in enumerate(positions, 1):
                    title = pos.get('title', 'Unknown')
                    outcome = pos.get('outcome', 'Unknown')
                    size = float(pos.get('size', 0))
                    avg_price = float(pos.get('avgPrice', 0))
                    cur_price = float(pos.get('curPrice', 0))
                    current_value = float(pos.get('currentValue', 0))
                    initial_value = float(pos.get('initialValue', 0))
                    cash_pnl = float(pos.get('cashPnl', 0))
                    percent_pnl = float(pos.get('percentPnl', 0))
                    
                    total_value += current_value
                    total_pnl += cash_pnl
                    
                    print(f"{i}. {title}")
                    print(f"   Outcome: {outcome}")
                    print(f"   Size: {size:.2f} shares")
                    print(f"   Avg Price: ${avg_price:.4f}")
                    print(f"   Current Price: ${cur_price:.4f}")
                    print(f"   Initial Value: ${initial_value:.2f}")
                    print(f"   Current Value: ${current_value:.2f}")
                    print(f"   Cash P&L: ${cash_pnl:.2f} ({percent_pnl:+.2f}%)")
                    print("")
                
                print("=" * 100)
                print("📊 SUMMARY:")
                print(f"   Total Positions: {len(positions)}")
                print(f"   Total Value: ${total_value:.2f}")
                print(f"   Total P&L: ${total_pnl:.2f}")
                print("=" * 100 + "\n")
                
                return positions
            else:
                print("   ✅ No positions found")
                return []
        else:
            print(f"   ❌ Error: {response.status_code}")
            print(f"   Response: {response.text}")
            return None
    
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return None


def sell_positions(positions):
    """Sell all positions"""
    try:
        if not positions or len(positions) == 0:
            print("✅ No positions to sell!")
            return
        
        # Get wallet private key
        private_key = os.getenv("WALLET_1_PK")
        if not private_key:
            print("❌ WALLET_1_PK not found in .env")
            return
        
        # Initialize CLOB client
        host = "https://clob.polymarket.com"
        chain_id = 137
        
        client = ClobClient(
            host,
            key=private_key,
            chain_id=chain_id,
            signature_type=2,
            funder=None
        )
        
        print(f"🔧 Initialized CLOB client\n")
        
        # Ask for confirmation
        print("=" * 100)
        print("⚠️  WARNING: This will sell ALL positions at current best bid prices!")
        print("=" * 100)
        confirm = input("\nType 'YES' to sell all positions: ")
        
        if confirm.upper() != 'YES':
            print("❌ Cancelled by user")
            return
        
        # Sell each position
        print(f"\n{'=' * 100}")
        print(f"🔄 SELLING POSITIONS...")
        print(f"{'=' * 100}\n")
        
        success_count = 0
        fail_count = 0
        
        for i, pos in enumerate(positions, 1):
            title = pos.get('title', 'Unknown')
            outcome = pos.get('outcome', 'Unknown')
            size = float(pos.get('size', 0))
            cur_price = float(pos.get('curPrice', 0))
            asset_id = pos.get('asset', 'Unknown')
            
            print(f"{i}. Selling {title} ({outcome})")
            print(f"   Size: {size:.2f} shares")
            print(f"   Price: ${cur_price:.4f}")
            
            try:
                # Create sell order at current best bid
                order_args = OrderArgs(
                    price=cur_price,
                    size=size,
                    side="SELL",
                    token_id=asset_id
                )
                
                print(f"   📝 Posting sell order...")
                
                # Post order
                resp = client.post_order(order_args, OrderType.GTC)
                
                if resp and 'orderID' in resp:
                    print(f"   ✅ Order placed successfully!")
                    print(f"      Order ID: {resp['orderID']}")
                    success_count += 1
                else:
                    print(f"   ❌ Failed to place order: {resp}")
                    fail_count += 1
            
            except Exception as e:
                print(f"   ❌ Error placing order: {e}")
                fail_count += 1
            
            print("")
        
        print("=" * 100)
        print("📊 SUMMARY:")
        print(f"   Total Positions: {len(positions)}")
        print(f"   Successfully Placed: {success_count}")
        print(f"   Failed: {fail_count}")
        print("=" * 100 + "\n")
        
        if success_count > 0:
            print("💡 Note: Orders are placed at best bid prices")
            print("   They may take time to fill depending on market liquidity")
            print("   Check your positions on Polymarket to see if they're filled\n")
    
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()


def main():
    """Main function"""
    print("\n" + "=" * 100)
    print("🎯 POLYMARKET POSITION MANAGER")
    print("=" * 100 + "\n")
    
    # Check positions
    positions = check_positions()
    
    if positions is None:
        print("❌ Failed to fetch positions")
        return
    
    if len(positions) == 0:
        print("✅ No positions to manage")
        return
    
    # Ask if user wants to sell
    print("\n💡 Options:")
    print("   1. Exit (do nothing)")
    print("   2. Sell all positions")
    
    choice = input("\nEnter your choice (1 or 2): ")
    
    if choice == "2":
        sell_positions(positions)
    else:
        print("✅ Exiting without selling")


if __name__ == "__main__":
    main()

