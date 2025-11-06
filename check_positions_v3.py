"""
Script to check positions using py_clob_client
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


async def check_positions_v3():
    """Check positions using py_clob_client"""
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
        
        # Get all open orders first
        logger.info(f"\n📋 Checking open orders...")
        try:
            orders = client.get_orders()
            
            if orders and len(orders) > 0:
                logger.info(f"   Found {len(orders)} open orders")
                
                for order in orders:
                    logger.info(f"\n   Order ID: {order.get('id', 'Unknown')}")
                    logger.info(f"   Token ID: {order.get('asset_id', 'Unknown')}")
                    logger.info(f"   Side: {order.get('side', 'Unknown')}")
                    logger.info(f"   Price: ${float(order.get('price', 0)):.4f}")
                    logger.info(f"   Size: {float(order.get('original_size', 0)):.2f}")
                    logger.info(f"   Status: {order.get('status', 'Unknown')}")
            else:
                logger.info(f"   No open orders")
        except Exception as e:
            logger.error(f"   ❌ Error getting orders: {e}")
        
        # Get balance changes (trades)
        logger.info(f"\n📊 Checking balance changes (trades)...")
        try:
            # Get balance changes from CLOB API
            balance_url = f"{host}/balance-changes"
            params = {"user": wallet_address}
            
            response = requests.get(balance_url, params=params)
            
            if response.status_code == 200:
                balance_changes = response.json()
                
                if len(balance_changes) > 0:
                    logger.info(f"   Found {len(balance_changes)} balance changes")
                    
                    # Group by asset_id to calculate net positions
                    positions = {}
                    
                    for change in balance_changes:
                        asset_id = change.get('asset_id', 'Unknown')
                        amount = float(change.get('amount', 0))
                        
                        if asset_id not in positions:
                            positions[asset_id] = 0
                        
                        positions[asset_id] += amount
                    
                    # Filter out zero positions
                    active_positions = {k: v for k, v in positions.items() if abs(v) > 0.001}
                    
                    if len(active_positions) > 0:
                        logger.info(f"\n{'='*80}")
                        logger.info(f"📋 ACTIVE POSITIONS:")
                        logger.info(f"{'='*80}\n")
                        
                        for i, (token_id, size) in enumerate(active_positions.items(), 1):
                            logger.info(f"{i}. Token ID: {token_id}")
                            logger.info(f"   Size: {size:.2f} shares")
                            
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
                                        
                                        logger.info(f"   Market: {market_name}")
                                        logger.info(f"   Outcome: {outcome}")
                                        
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
                            
                            except Exception as e:
                                logger.error(f"   ❌ Error getting market info: {e}")
                            
                            logger.info("")
                        
                        logger.info(f"{'='*80}\n")
                    else:
                        logger.info(f"   ✅ No active positions (all positions are zero)")
                else:
                    logger.info(f"   No balance changes found")
            else:
                logger.error(f"   ❌ Error: {response.status_code}")
                logger.error(f"   Response: {response.text}")
        
        except Exception as e:
            logger.error(f"❌ Error fetching balance changes: {e}")
            import traceback
            traceback.print_exc()
    
    except Exception as e:
        logger.error(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(check_positions_v3())

