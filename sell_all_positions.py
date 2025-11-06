"""
Script to sell all positions using Polymarket CLOB API
"""
import asyncio
import os
import sys
import json
from dotenv import load_dotenv
from py_clob_client.client import ClobClient
from py_clob_client.clob_types import OrderArgs, OrderType
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()


async def sell_all_positions():
    """Sell all positions"""
    try:
        # Load positions data
        if not os.path.exists('positions_data.json'):
            logger.error("❌ positions_data.json not found! Run check_positions_final.py first")
            return
        
        with open('positions_data.json', 'r') as f:
            positions = json.load(f)
        
        if len(positions) == 0:
            logger.info("✅ No positions to sell!")
            return
        
        # Get wallet private key
        private_key = os.getenv("WALLET_1_PK")
        if not private_key:
            logger.error("❌ WALLET_1_PK not found in .env")
            return
        
        # Initialize CLOB client
        host = "https://clob.polymarket.com"
        chain_id = 137  # Polygon mainnet
        
        client = ClobClient(
            host,
            key=private_key,
            chain_id=chain_id,
            signature_type=2,
            funder=None
        )
        
        logger.info(f"🔧 Initialized CLOB client")
        logger.info(f"\n{'='*100}")
        logger.info(f"📋 POSITIONS TO SELL:")
        logger.info(f"{'='*100}\n")
        
        for i, pos in enumerate(positions, 1):
            title = pos.get('title', 'Unknown')
            outcome = pos.get('outcome', 'Unknown')
            size = float(pos.get('size', 0))
            cur_price = float(pos.get('curPrice', 0))
            current_value = float(pos.get('currentValue', 0))
            cash_pnl = float(pos.get('cashPnl', 0))
            
            logger.info(f"{i}. {title}")
            logger.info(f"   Outcome: {outcome}")
            logger.info(f"   Size: {size:.2f} shares")
            logger.info(f"   Current Price: ${cur_price:.4f}")
            logger.info(f"   Est. Value: ${current_value:.2f}")
            logger.info(f"   P&L: ${cash_pnl:.2f}")
            logger.info("")
        
        logger.info(f"{'='*100}\n")
        
        # Ask for confirmation
        print("=" * 100)
        print("⚠️  WARNING: This will sell ALL positions at current best bid prices!")
        print("=" * 100)
        confirm = input("\nType 'YES' to sell all positions: ")
        
        if confirm.upper() != 'YES':
            logger.info("❌ Cancelled by user")
            return
        
        # Sell each position
        logger.info(f"\n{'='*100}")
        logger.info(f"🔄 SELLING POSITIONS...")
        logger.info(f"{'='*100}\n")
        
        success_count = 0
        fail_count = 0
        
        for i, pos in enumerate(positions, 1):
            title = pos.get('title', 'Unknown')
            outcome = pos.get('outcome', 'Unknown')
            size = float(pos.get('size', 0))
            cur_price = float(pos.get('curPrice', 0))
            asset_id = pos.get('asset', 'Unknown')
            
            logger.info(f"{i}. Selling {title} ({outcome})")
            logger.info(f"   Size: {size:.2f} shares")
            logger.info(f"   Price: ${cur_price:.4f}")
            
            try:
                # Create sell order at current best bid
                order_args = OrderArgs(
                    price=cur_price,
                    size=size,
                    side="SELL",
                    token_id=asset_id
                )
                
                logger.info(f"   📝 Posting sell order...")
                
                # Post order
                resp = client.post_order(order_args, OrderType.GTC)
                
                if resp and 'orderID' in resp:
                    logger.info(f"   ✅ Order placed successfully!")
                    logger.info(f"      Order ID: {resp['orderID']}")
                    success_count += 1
                else:
                    logger.error(f"   ❌ Failed to place order: {resp}")
                    fail_count += 1
            
            except Exception as e:
                logger.error(f"   ❌ Error placing order: {e}")
                fail_count += 1
            
            logger.info("")
        
        logger.info(f"{'='*100}")
        logger.info(f"📊 SUMMARY:")
        logger.info(f"   Total Positions: {len(positions)}")
        logger.info(f"   Successfully Placed: {success_count}")
        logger.info(f"   Failed: {fail_count}")
        logger.info(f"{'='*100}\n")
        
        if success_count > 0:
            logger.info(f"💡 Note: Orders are placed at best bid prices")
            logger.info(f"   They may take time to fill depending on market liquidity")
            logger.info(f"   Check your positions on Polymarket to see if they're filled\n")
    
    except Exception as e:
        logger.error(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(sell_all_positions())

