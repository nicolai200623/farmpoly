"""
Script to check positions using Polymarket Gamma API
This will get the correct token IDs and prices
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


async def check_positions_v2():
    """Check positions using Gamma API"""
    try:
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
        
        # Get wallet address
        from web3 import Web3
        w3 = Web3()
        account = w3.eth.account.from_key(private_key)
        wallet_address = account.address
        
        logger.info(f"🔍 Checking positions for wallet: {wallet_address[:10]}...{wallet_address[-8:]}")
        
        # Get positions from CLOB API
        logger.info(f"\n📊 Fetching positions from Polymarket...")
        
        # Method 1: Get positions via /positions endpoint
        try:
            positions_url = f"https://clob.polymarket.com/positions"
            params = {"user": wallet_address}
            
            response = requests.get(positions_url, params=params)
            
            if response.status_code == 200:
                positions_data = response.json()
                logger.info(f"   Found {len(positions_data)} positions")
                
                if len(positions_data) > 0:
                    logger.info(f"\n{'='*80}")
                    logger.info(f"📋 POSITIONS:")
                    logger.info(f"{'='*80}\n")
                    
                    for i, pos in enumerate(positions_data, 1):
                        token_id = pos.get('asset_id', 'Unknown')
                        size = float(pos.get('size', 0))
                        
                        # Get market info from Gamma API
                        try:
                            gamma_url = f"https://gamma-api.polymarket.com/markets"
                            gamma_params = {"clob_token_ids": token_id}
                            gamma_resp = requests.get(gamma_url, params=gamma_params)
                            
                            if gamma_resp.status_code == 200:
                                markets = gamma_resp.json()
                                
                                if len(markets) > 0:
                                    market = markets[0]
                                    market_name = market.get('question', 'Unknown')
                                    
                                    # Find which outcome this token represents
                                    tokens = market.get('clob_token_ids', [])
                                    outcomes = market.get('outcomes', ['YES', 'NO'])
                                    
                                    outcome = 'Unknown'
                                    if token_id in tokens:
                                        idx = tokens.index(token_id)
                                        outcome = outcomes[idx] if idx < len(outcomes) else 'Unknown'
                                    
                                    logger.info(f"{i}. {market_name}")
                                    logger.info(f"   Outcome: {outcome}")
                                    logger.info(f"   Token ID: {token_id}")
                                    logger.info(f"   Size: {size} shares")
                                    
                                    # Get current price from orderbook
                                    try:
                                        book = client.get_order_book(token_id)
                                        
                                        if hasattr(book, 'bids') and len(book.bids) > 0:
                                            best_bid = float(book.bids[0].price)
                                            logger.info(f"   Best Bid: ${best_bid:.4f}")
                                            logger.info(f"   Est. Value: ${size * best_bid:.2f}")
                                        else:
                                            logger.info(f"   Best Bid: No bids")
                                        
                                        if hasattr(book, 'asks') and len(book.asks) > 0:
                                            best_ask = float(book.asks[0].price)
                                            logger.info(f"   Best Ask: ${best_ask:.4f}")
                                    except Exception as e:
                                        logger.error(f"   ❌ Error getting orderbook: {e}")
                                    
                                    logger.info("")
                                else:
                                    logger.info(f"{i}. Unknown Market")
                                    logger.info(f"   Token ID: {token_id}")
                                    logger.info(f"   Size: {size} shares\n")
                            else:
                                logger.info(f"{i}. Unknown Market")
                                logger.info(f"   Token ID: {token_id}")
                                logger.info(f"   Size: {size} shares\n")
                        
                        except Exception as e:
                            logger.error(f"   ❌ Error getting market info: {e}")
                            logger.info(f"{i}. Unknown Market")
                            logger.info(f"   Token ID: {token_id}")
                            logger.info(f"   Size: {size} shares\n")
                    
                    logger.info(f"{'='*80}\n")
                else:
                    logger.info(f"   ✅ No positions found")
            else:
                logger.error(f"   ❌ Error: {response.status_code}")
                logger.error(f"   Response: {response.text}")
        
        except Exception as e:
            logger.error(f"❌ Error fetching positions: {e}")
            import traceback
            traceback.print_exc()
    
    except Exception as e:
        logger.error(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(check_positions_v2())

