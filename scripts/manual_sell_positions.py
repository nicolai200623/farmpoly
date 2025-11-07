#!/usr/bin/env python3
"""
Manual Sell Positions Script
Allows manual selling of filled positions
"""

import asyncio
import os
import sys
import logging
import requests
from dotenv import load_dotenv
from typing import List, Dict

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from py_clob_client.client import ClobClient
from py_clob_client.clob_types import OrderArgs, OrderType
from py_clob_client.constants import POLYGON
from py_clob_client.order_builder.constants import SELL

# Load environment
load_dotenv()

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


async def get_positions(wallet_address: str) -> List[Dict]:
    """Get all open positions from Polymarket Data API"""
    try:
        data_api_url = "https://data-api.polymarket.com/positions"
        params = {
            "user": wallet_address,
            "sizeThreshold": 0.01,
            "limit": 500
        }

        logger.info(f"Fetching positions for wallet: {wallet_address[:10]}...{wallet_address[-8:]}")
        response = requests.get(data_api_url, params=params, timeout=10)
        response.raise_for_status()

        positions = response.json()

        if not positions:
            logger.info("No positions found")
            return []

        logger.info(f"Found {len(positions)} position(s)")
        return positions

    except Exception as e:
        logger.error(f"Failed to get positions: {e}")
        import traceback
        traceback.print_exc()
        return []


async def display_positions(positions: list):
    """Display positions in a readable format"""
    if not positions:
        print("\n❌ No positions found\n")
        return

    print("\n" + "="*100)
    print("📊 YOUR OPEN POSITIONS")
    print("="*100)

    for i, pos in enumerate(positions, 1):
        # Data API field names (different from what I expected)
        market = pos.get('title', pos.get('market', 'Unknown'))[:60]
        token_id = pos.get('asset_id', pos.get('asset', 'unknown'))
        shares = float(pos.get('size', 0))
        avg_entry = float(pos.get('average_price', pos.get('avgPrice', 0)))
        current_price = float(pos.get('current_price', pos.get('curPrice', 0)))

        # Calculate P&L
        entry_cost = shares * avg_entry
        current_value = shares * current_price
        pnl = current_value - entry_cost
        pnl_pct = (pnl / entry_cost * 100) if entry_cost > 0 else 0

        # Color code P&L
        pnl_color = "🟢" if pnl >= 0 else "🔴"

        print(f"\n{i}. {market}")
        print(f"   Token ID: {token_id}")
        print(f"   Shares: {shares:.2f}")
        print(f"   Entry Price: ${avg_entry:.4f}")
        print(f"   Current Price: ${current_price:.4f}")
        print(f"   {pnl_color} P&L: ${pnl:.2f} ({pnl_pct:+.2f}%)")
        print(f"   Value: ${current_value:.2f}")

    print("\n" + "="*100 + "\n")


async def sell_position(position: dict, sell_percentage: float = 100.0):
    """Sell a position (default: 100% = sell all)"""
    try:
        market = position.get('title', position.get('market', 'Unknown'))
        token_id = position.get('asset_id', position.get('asset'))
        total_shares = float(position.get('size', 0))
        current_price = float(position.get('current_price', position.get('curPrice', 0)))

        # Calculate shares to sell
        shares_to_sell = total_shares * (sell_percentage / 100.0)

        if shares_to_sell <= 0:
            logger.error("Invalid sell amount")
            return False

        logger.info(f"\n🔄 Preparing to SELL {sell_percentage}% of position...")
        logger.info(f"   Market: {market[:60]}")
        logger.info(f"   Token ID: {token_id}")
        logger.info(f"   Shares to sell: {shares_to_sell:.2f} / {total_shares:.2f}")
        logger.info(f"   Current Price: ${current_price:.4f}")

        # Ask for price (or use market price)
        print("\nSell options:")
        print(f"1. Market sell (price: ${current_price * 0.99:.4f} - 1% below to ensure fill)")
        print(f"2. Limit sell (enter custom price)")
        print("3. Cancel")

        choice = input("\nChoose option (1/2/3): ").strip()

        if choice == "1":
            # Market sell: 1% below current price
            sell_price = current_price * 0.99
            logger.info(f"✅ Using market sell price: ${sell_price:.4f}")
        elif choice == "2":
            # Custom limit price
            try:
                custom_price = float(input(f"Enter sell price (current: ${current_price:.4f}): ").strip())
                if custom_price <= 0 or custom_price > 1.0:
                    logger.error("Invalid price (must be between 0 and 1)")
                    return False
                sell_price = custom_price
                logger.info(f"✅ Using custom sell price: ${sell_price:.4f}")
            except ValueError:
                logger.error("Invalid price format")
                return False
        else:
            logger.info("❌ Sell cancelled")
            return False

        # Confirm
        expected_proceeds = shares_to_sell * sell_price
        print(f"\n⚠️  CONFIRM SELL:")
        print(f"   Shares: {shares_to_sell:.2f}")
        print(f"   Price: ${sell_price:.4f}")
        print(f"   Expected proceeds: ${expected_proceeds:.2f}")

        confirm = input("\nConfirm sell? (yes/no): ").strip().lower()
        if confirm != "yes":
            logger.info("❌ Sell cancelled")
            return False

        # Create fresh signing client
        logger.info("\n🔧 Creating signing client...")
        private_key = os.getenv('WALLET_1_PK') or os.getenv('PRIVATE_KEY')
        if not private_key:
            raise ValueError("WALLET_1_PK or PRIVATE_KEY not found in .env")

        if private_key.startswith('0x'):
            private_key = private_key[2:]

        signing_client = ClobClient(
            host="https://clob.polymarket.com",
            key=private_key,
            chain_id=POLYGON
        )

        # Set API credentials
        logger.info("🔑 Setting API credentials...")
        signing_client.set_api_creds(signing_client.create_or_derive_api_creds())
        logger.info("✅ API credentials set")

        # Create order
        order_args = OrderArgs(
            token_id=token_id,
            price=sell_price,
            size=shares_to_sell,
            side=SELL
        )

        logger.info("📝 Creating and signing SELL order...")
        signed_order = signing_client.create_order(order_args)

        logger.info("📤 Posting SELL order to CLOB...")
        resp = signing_client.post_order(signed_order, OrderType.GTC)

        if resp and resp.get('success'):
            order_id = resp.get('orderID', 'unknown')
            logger.info(f"\n✅ SELL ORDER PLACED SUCCESSFULLY!")
            logger.info(f"   Order ID: {order_id}")
            logger.info(f"   Shares: {shares_to_sell:.2f}")
            logger.info(f"   Price: ${sell_price:.4f}")
            logger.info(f"   Expected proceeds: ${expected_proceeds:.2f}")
            logger.info(f"\n   Track order: https://polymarket.com/")
            return True
        else:
            error_msg = resp.get('error', 'Unknown error') if resp else 'No response'
            logger.error(f"\n❌ Failed to place SELL order: {error_msg}")
            return False

    except Exception as e:
        logger.error(f"❌ Error selling position: {e}")
        import traceback
        traceback.print_exc()
        return False


async def main():
    """Main function"""
    try:
        print("\n" + "="*100)
        print("💰 MANUAL POSITION SELLER")
        print("="*100)

        # Get wallet address from .env
        wallet_address = os.getenv('WALLET_1_ADDRESS')
        if not wallet_address:
            logger.error("❌ WALLET_1_ADDRESS not found in .env")
            logger.error("   Please add WALLET_1_ADDRESS=0x... to your .env file")
            return

        logger.info(f"Using wallet: {wallet_address[:10]}...{wallet_address[-8:]}")

        # Get positions
        logger.info("📊 Fetching positions...")
        positions = await get_positions(wallet_address)

        # Display positions
        await display_positions(positions)

        if not positions:
            return

        # Sell menu
        while True:
            print("\nOptions:")
            print("1. Sell a position")
            print("2. Refresh positions")
            print("3. Exit")

            choice = input("\nChoose option (1/2/3): ").strip()

            if choice == "1":
                # Select position
                try:
                    pos_num = int(input(f"\nEnter position number (1-{len(positions)}): ").strip())
                    if pos_num < 1 or pos_num > len(positions):
                        print("❌ Invalid position number")
                        continue

                    selected_pos = positions[pos_num - 1]

                    # Ask for percentage
                    print("\nSell amount:")
                    print("1. Sell all (100%)")
                    print("2. Sell partial (enter %)")

                    sell_choice = input("\nChoose (1/2): ").strip()

                    if sell_choice == "1":
                        sell_pct = 100.0
                    elif sell_choice == "2":
                        try:
                            sell_pct = float(input("Enter percentage to sell (1-100): ").strip())
                            if sell_pct <= 0 or sell_pct > 100:
                                print("❌ Invalid percentage")
                                continue
                        except ValueError:
                            print("❌ Invalid percentage format")
                            continue
                    else:
                        continue

                    # Sell
                    success = await sell_position(selected_pos, sell_pct)

                    if success:
                        print("\n✅ Position sold successfully!")
                        print("Refreshing positions...")
                        positions = await get_positions(wallet_address)
                        await display_positions(positions)

                except ValueError:
                    print("❌ Invalid input")

            elif choice == "2":
                logger.info("📊 Refreshing positions...")
                positions = await get_positions(wallet_address)
                await display_positions(positions)

            elif choice == "3":
                logger.info("👋 Exiting...")
                break
            else:
                print("❌ Invalid choice")

    except KeyboardInterrupt:
        logger.info("\n\n👋 Interrupted by user")
    except Exception as e:
        logger.error(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(main())
