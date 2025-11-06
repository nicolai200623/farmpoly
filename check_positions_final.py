"""
Script to check positions using Polymarket Data API
"""
import asyncio
import os
import sys
from dotenv import load_dotenv
from py_clob_client.client import ClobClient
import requests
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()


async def check_positions_final():
    """Check positions using Polymarket Data API"""
    try:
        # Get wallet private key
        private_key = os.getenv("WALLET_1_PK")
        if not private_key:
            logger.error("❌ WALLET_1_PK not found in .env")
            return
        
        # Get wallet address
        from web3 import Web3
        w3 = Web3()
        account = w3.eth.account.from_key(private_key)
        wallet_address = account.address
        
        logger.info(f"🔍 Checking positions for wallet: {wallet_address[:10]}...{wallet_address[-8:]}")
        
        # Use Polymarket Data API
        data_api_url = "https://data-api.polymarket.com/positions"
        params = {
            "user": wallet_address,
            "sizeThreshold": 0.01,  # Include all positions > 0.01
            "limit": 500
        }
        
        logger.info(f"\n📊 Fetching positions from Polymarket Data API...")
        
        response = requests.get(data_api_url, params=params)
        
        if response.status_code == 200:
            positions = response.json()
            
            if len(positions) > 0:
                logger.info(f"   Found {len(positions)} positions\n")
                logger.info(f"{'='*100}")
                logger.info(f"📋 ACTIVE POSITIONS:")
                logger.info(f"{'='*100}\n")
                
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
                    asset_id = pos.get('asset', 'Unknown')
                    redeemable = pos.get('redeemable', False)
                    
                    total_value += current_value
                    total_pnl += cash_pnl
                    
                    logger.info(f"{i}. {title}")
                    logger.info(f"   Outcome: {outcome}")
                    logger.info(f"   Size: {size:.2f} shares")
                    logger.info(f"   Avg Price: ${avg_price:.4f}")
                    logger.info(f"   Current Price: ${cur_price:.4f}")
                    logger.info(f"   Initial Value: ${initial_value:.2f}")
                    logger.info(f"   Current Value: ${current_value:.2f}")
                    logger.info(f"   Cash P&L: ${cash_pnl:.2f} ({percent_pnl:+.2f}%)")
                    logger.info(f"   Redeemable: {redeemable}")
                    logger.info(f"   Token ID: {asset_id}")
                    logger.info("")
                
                logger.info(f"{'='*100}")
                logger.info(f"📊 SUMMARY:")
                logger.info(f"   Total Positions: {len(positions)}")
                logger.info(f"   Total Value: ${total_value:.2f}")
                logger.info(f"   Total P&L: ${total_pnl:.2f}")
                logger.info(f"{'='*100}\n")
                
                # Ask if user wants to sell
                logger.info(f"💡 Do you want to sell these positions?")
                logger.info(f"   Note: You can sell on Polymarket UI or use the sell script")
                logger.info(f"   Current prices shown above are the best bid prices\n")
                
                # Save positions to file for sell script
                import json
                with open('positions_data.json', 'w') as f:
                    json.dump(positions, f, indent=2)
                
                logger.info(f"✅ Positions data saved to positions_data.json")
            else:
                logger.info(f"   ✅ No positions found")
        else:
            logger.error(f"   ❌ Error: {response.status_code}")
            logger.error(f"   Response: {response.text}")
    
    except Exception as e:
        logger.error(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(check_positions_final())

