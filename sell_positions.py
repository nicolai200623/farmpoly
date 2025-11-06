"""
Script to sell all positions on Polymarket
"""
import asyncio
import os
import sys
from dotenv import load_dotenv
from py_clob_client.client import ClobClient
from py_clob_client.clob_types import OrderArgs, OrderType
from web3 import Web3
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Polygon RPC
POLYGON_RPC = "https://polygon-rpc.com"

# CTF (Conditional Token Framework) contract address
CTF_CONTRACT = "0x4D97DCd97eC945f40cF65F87097ACe5EA0476045"

# ERC1155 ABI (balanceOf only)
ERC1155_ABI = [
    {
        "inputs": [
            {"internalType": "address", "name": "account", "type": "address"},
            {"internalType": "uint256", "name": "id", "type": "uint256"}
        ],
        "name": "balanceOf",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function"
    }
]


async def sell_all_positions():
    """Sell all positions"""
    try:
        # Get wallet private key
        private_key = os.getenv("WALLET_1_PK")
        if not private_key:
            logger.error("❌ WALLET_1_PK not found in .env")
            return
        
        # Initialize Web3
        w3 = Web3(Web3.HTTPProvider(POLYGON_RPC))
        account = w3.eth.account.from_key(private_key)
        wallet_address = account.address
        
        logger.info(f"🔧 Initializing CLOB client...")
        logger.info(f"🔑 Creating API credentials...")
        
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
        
        logger.info(f"🔍 Checking positions via Polymarket API...")
        logger.info(f"   Wallet: {wallet_address[:10]}...{wallet_address[-8:]}")
        
        # Known token IDs from the transaction
        netflix_1050_yes = "109176985745730388398013053205590535560490868817001794547246190093921488790462"
        
        positions = []
        
        # Check balance via Web3
        ctf_contract = w3.eth.contract(address=CTF_CONTRACT, abi=ERC1155_ABI)
        
        logger.info(f"\n💰 Checking token balances...")
        
        balance = ctf_contract.functions.balanceOf(wallet_address, int(netflix_1050_yes)).call()
        
        if balance > 0:
            # Get orderbook to find best bid
            try:
                book = client.get_order_book(netflix_1050_yes)

                # OrderBookSummary has .bids and .asks attributes
                if book and hasattr(book, 'bids') and len(book.bids) > 0:
                    best_bid = float(book.bids[0].price)
                else:
                    best_bid = 0.01  # Default to 1¢ if no bids

                positions.append({
                    'name': 'Netflix $1050 (YES)',
                    'token_id': netflix_1050_yes,
                    'balance': balance,
                    'best_bid': best_bid
                })

                logger.info(f"   ✅ Netflix $1050 (YES): {balance} shares")
                logger.info(f"      Best bid: ${best_bid:.4f}")
                logger.info(f"      Est. value: ${balance * best_bid / 1e6:.2f}")
            except Exception as e:
                logger.error(f"   ❌ Error getting orderbook: {e}")
                import traceback
                traceback.print_exc()
                return
        
        if not positions:
            logger.info(f"\n✅ No positions to sell!")
            return
        
        logger.info(f"\n📊 Summary: Found {len(positions)} positions")
        logger.info(f"\n{'='*60}")
        logger.info(f"💡 Ready to sell positions")
        logger.info(f"{'='*60}\n")
        
        # Ask for confirmation
        print("=" * 60)
        confirm = input("Type 'YES' to sell all positions: ")
        
        if confirm.upper() != 'YES':
            logger.info("❌ Cancelled by user")
            return
        
        # Sell each position
        for pos in positions:
            logger.info(f"\n🔄 Selling {pos['name']}...")
            logger.info(f"   Token ID: {pos['token_id']}")
            logger.info(f"   Balance: {pos['balance']} shares")
            logger.info(f"   Best bid: ${pos['best_bid']:.4f}")
            
            # Calculate sell price (best bid)
            sell_price = pos['best_bid']
            
            # Create sell order
            try:
                order_args = OrderArgs(
                    price=sell_price,
                    size=pos['balance'] / 1e6,  # Convert to decimal
                    side="SELL",
                    token_id=pos['token_id']
                )
                
                logger.info(f"   📝 Creating sell order...")
                logger.info(f"      Price: ${sell_price:.4f}")
                logger.info(f"      Size: {pos['balance'] / 1e6:.2f} shares")
                
                # Post order
                resp = client.post_order(order_args, OrderType.GTC)
                
                if resp and 'orderID' in resp:
                    logger.info(f"   ✅ Order placed successfully!")
                    logger.info(f"      Order ID: {resp['orderID']}")
                else:
                    logger.error(f"   ❌ Failed to place order: {resp}")
            
            except Exception as e:
                logger.error(f"   ❌ Error placing order: {e}")
                continue
        
        logger.info(f"\n{'='*60}")
        logger.info(f"✅ DONE! All sell orders placed")
        logger.info(f"{'='*60}")
        logger.info(f"\n💡 Note: Orders may take time to fill")
        logger.info(f"   Check your positions on Polymarket to see if they're filled")
    
    except Exception as e:
        logger.error(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(sell_all_positions())

