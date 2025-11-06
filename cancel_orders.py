#!/usr/bin/env python3
"""Cancel all open orders"""

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

async def cancel_all_orders():
    """Cancel all open orders"""
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
        
        # Get wallet address
        from eth_account import Account
        account = Account.from_key(priv_key)
        wallet_address = account.address
        
        logger.info(f"   Wallet: {wallet_address[:10]}...{wallet_address[-8:]}")
        
        # Get open orders
        logger.info("\n📋 Fetching open orders...")
        
        open_orders = client.get_orders()
        
        if not open_orders:
            logger.info("✅ No open orders to cancel")
            return
        
        logger.info(f"   Found {len(open_orders)} open orders\n")
        
        for i, order in enumerate(open_orders, 1):
            order_id = order.get('id', 'Unknown')
            token_id = order.get('asset_id', 'Unknown')
            size = order.get('original_size', 0)
            price = order.get('price', 0)
            
            logger.info(f"{i}. Order ID: {order_id}")
            logger.info(f"   Token: {token_id}")
            logger.info(f"   Size: {size} shares")
            logger.info(f"   Price: ${price}")
            logger.info("")
        
        # Ask for confirmation
        print("="*60)
        confirm = input("Type 'YES' to cancel ALL orders: ").strip()
        print("="*60)
        
        if confirm != 'YES':
            logger.info("\n❌ Cancelled by user")
            return
        
        # Cancel all orders
        logger.info("\n🔥 Cancelling orders...")
        
        for order in open_orders:
            order_id = order.get('id')
            
            try:
                logger.info(f"   Cancelling order {order_id}...")
                
                # Cancel order
                client.cancel(order_id)
                
                logger.info(f"   ✅ Order cancelled successfully!")
                
                # Wait a bit between cancellations
                await asyncio.sleep(1)
                
            except Exception as e:
                logger.error(f"   ❌ Error cancelling order {order_id}: {e}")
        
        logger.info("\n✅ Finished cancelling orders!")
        
    except Exception as e:
        logger.error(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(cancel_all_orders())

