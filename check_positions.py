#!/usr/bin/env python3
"""Check current positions and prepare sell orders"""

import asyncio
import sys
import os
from pathlib import Path
from dotenv import load_dotenv

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from py_clob_client.client import ClobClient
import yaml
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def check_positions():
    """Check current positions"""
    try:
        # Load environment variables
        load_dotenv()

        # Load config
        with open('config.yaml', 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)

        # Get wallet private key from .env
        priv_key = os.getenv('WALLET_1_PK')
        if not priv_key:
            logger.error("❌ WALLET_1_PK not found in .env")
            return

        if not priv_key.startswith('0x'):
            priv_key = '0x' + priv_key

        # Initialize CLOB client
        host = "https://clob.polymarket.com"
        chain_id = 137  # Polygon mainnet

        logger.info("🔧 Initializing CLOB client...")
        client = ClobClient(host, key=priv_key, chain_id=chain_id)

        # Create API credentials
        logger.info("🔑 Creating API credentials...")
        client.set_api_creds(client.create_or_derive_api_creds())
        
        logger.info("🔍 Checking positions via Polymarket API...")

        # Get wallet address
        from eth_account import Account
        account = Account.from_key(priv_key)
        wallet_address = account.address

        logger.info(f"   Wallet: {wallet_address[:10]}...{wallet_address[-8:]}")

        # Get positions from Polymarket API
        import requests

        # Try CLOB API for open orders first
        logger.info("\n📋 Checking open orders...")
        try:
            # Get open orders using py_clob_client
            open_orders = client.get_orders()

            if open_orders:
                logger.info(f"   Found {len(open_orders)} open orders")
                for order in open_orders:
                    logger.info(f"   - Order ID: {order.get('id', 'Unknown')}")
                    logger.info(f"     Token: {order.get('asset_id', 'Unknown')}")
                    logger.info(f"     Size: {order.get('original_size', 0)}")
                    logger.info(f"     Price: ${order.get('price', 0)}")
                    logger.info("")
            else:
                logger.info("   No open orders")
        except Exception as e:
            logger.warning(f"   Could not fetch open orders: {e}")

        # Try to get balances using CLOB client
        logger.info("\n💰 Checking token balances...")

        # Known token IDs from the transaction
        # From transaction: 109176985745730388398013053205590535560490868817001794547246190093921488790462
        netflix_1050_yes = "109176985745730388398013053205590535560490868817001794547246190093921488790462"  # Will Netflix dip to $1050 (YES)

        # Other markets from screenshot
        charlotte_49ers = "Unknown"  # Charlotte 49ers vs. East Carolina
        google_gemini = "Unknown"  # Will Google Gemini 3 score at least 70%
        syracuse_miami = "Unknown"  # Syracuse vs. Miami

        token_ids = [netflix_1050_yes]
        token_names = [
            "Netflix $1050 (YES) - From TX"
        ]

        positions_found = []

        for token_id, token_name in zip(token_ids, token_names):
            try:
                # Check balance using Web3
                from web3 import Web3
                rpc_url = config.get('rpc_url', 'https://polygon-rpc.com')
                w3 = Web3(Web3.HTTPProvider(rpc_url))

                # CTF Exchange contract address (Polymarket's conditional token framework)
                ctf_address = "0x4D97DCd97eC945f40cF65F87097ACe5EA0476045"

                # ERC1155 balanceOf ABI
                abi = [{
                    "constant": True,
                    "inputs": [
                        {"name": "account", "type": "address"},
                        {"name": "id", "type": "uint256"}
                    ],
                    "name": "balanceOf",
                    "outputs": [{"name": "", "type": "uint256"}],
                    "type": "function"
                }]

                contract = w3.eth.contract(address=ctf_address, abi=abi)
                balance = contract.functions.balanceOf(wallet_address, int(token_id)).call()

                if balance > 0:
                    logger.info(f"   ✅ {token_name}: {balance} shares")
                    positions_found.append({
                        'token_id': token_id,
                        'token_name': token_name,
                        'balance': balance
                    })

                    # Get current best bid
                    try:
                        orderbook = client.get_order_book(token_id)
                        if orderbook and hasattr(orderbook, 'bids') and orderbook.bids:
                            best_bid = float(orderbook.bids[0].price)
                            logger.info(f"      Best bid: ${best_bid:.4f}")
                            logger.info(f"      Est. value: ${best_bid * balance:.2f}")
                    except:
                        pass

            except Exception as e:
                logger.debug(f"   Error checking {token_name}: {e}")

        if not positions_found:
            logger.info("   ✅ No positions found")
            return None

        data = positions_found

        logger.info(f"\n📊 Summary: Found {len(data)} positions")

        # Ask user if they want to sell
        logger.info("\n" + "="*60)
        logger.info("💡 Do you want to sell these positions?")
        logger.info("="*60)

        return data, client, wallet_address
        
    except Exception as e:
        logger.error(f"Error checking positions: {e}")
        import traceback
        traceback.print_exc()

async def sell_positions(positions, client, wallet_address):
    """Sell all positions"""
    try:
        from py_clob_client.order_builder.constants import SELL
        from py_clob_client.clob_types import OrderArgs

        logger.info("\n🔥 Starting to sell positions...")

        for pos in positions:
            token_id = pos['token_id']
            token_name = pos['token_name']
            balance = pos['balance']

            logger.info(f"\n📍 Selling {token_name}: {balance} shares")

            try:
                # Get current orderbook
                orderbook = client.get_order_book(token_id)

                if not orderbook or not hasattr(orderbook, 'bids') or not orderbook.bids:
                    logger.error(f"   ❌ No bids available - cannot sell!")
                    continue

                # Get best bid price
                best_bid = float(orderbook.bids[0].price)
                logger.info(f"   Best bid: ${best_bid:.4f}")

                # Sell at best bid (market order)
                # We'll place a limit order at best bid price to ensure fill
                sell_price = best_bid

                logger.info(f"   Placing sell order: {balance} shares @ ${sell_price:.4f}")

                # Create order args
                order_args = OrderArgs(
                    price=sell_price,
                    size=balance,
                    side=SELL,
                    token_id=token_id
                )

                # Create and sign order
                signed_order = client.create_and_sign_order(order_args)

                # Post order
                response = client.post_order(signed_order)

                logger.info(f"   ✅ Sell order placed successfully!")
                logger.info(f"   Order ID: {response.get('orderID', 'Unknown')}")

                # Wait a bit between orders
                await asyncio.sleep(2)

            except Exception as e:
                logger.error(f"   ❌ Error selling {token_name}: {e}")
                import traceback
                traceback.print_exc()

        logger.info("\n✅ Finished selling positions!")

    except Exception as e:
        logger.error(f"Error in sell_positions: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    result = asyncio.run(check_positions())

    if result:
        positions, client, wallet_address = result

        # Ask for confirmation
        print("\n" + "="*60)
        confirm = input("Type 'YES' to sell all positions: ").strip()
        print("="*60)

        if confirm == 'YES':
            asyncio.run(sell_positions(positions, client, wallet_address))
        else:
            print("\n❌ Cancelled by user")

