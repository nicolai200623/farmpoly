#!/usr/bin/env python3
"""
Check positions by querying on-chain balances
This is more accurate than CLOB API
"""

import os
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from web3 import Web3
from dotenv import load_dotenv
from eth_account import Account
import requests

# ERC1155 ABI (minimal - just balanceOf)
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

# Polymarket CTF Exchange contract (holds all outcome tokens)
CTF_EXCHANGE = "0x4bFb41d5B3570DeFd03C39a9A4D8dE6Bd8B8982E"

def get_market_info(market_id):
    """Get market info from Gamma API"""
    try:
        url = f"https://gamma-api.polymarket.com/events/{market_id}"
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.json()
    except:
        pass
    return None

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
    
    # Get RPC URL
    rpc_url = os.getenv('POLYGON_RPC_URL', 'https://polygon-rpc.com')
    
    print("=" * 70)
    print("Polymarket Bot - Check Positions (On-Chain)")
    print("=" * 70)
    print()
    
    try:
        # Connect to Polygon
        w3 = Web3(Web3.HTTPProvider(rpc_url))
        if not w3.is_connected():
            print("❌ Failed to connect to Polygon RPC")
            return
        
        # Get wallet address
        wallet_address = Account.from_key(private_key).address
        print(f"Wallet: {wallet_address}")
        print(f"Network: Polygon (Chain ID: {w3.eth.chain_id})")
        print()
        
        # Get CTF Exchange contract
        ctf_contract = w3.eth.contract(
            address=Web3.to_checksum_address(CTF_EXCHANGE),
            abi=ERC1155_ABI
        )
        
        print("📋 Checking positions...")
        print("⚠️  This requires knowing token IDs from your orders.")
        print()
        
        # Known token IDs from your positions (from Polymarket UI)
        # We need to get these from somewhere - let's try CLOB API first
        from py_clob_client.client import ClobClient
        
        client = ClobClient(
            host="https://clob.polymarket.com",
            key=private_key,
            chain_id=137
        )
        client.set_api_creds(client.create_or_derive_api_creds())
        
        # Get recent orders to find token IDs
        print("🔍 Scanning recent orders for token IDs...")
        orders = client.get_orders()
        
        # Collect unique token IDs
        token_ids = set()
        token_to_market = {}
        
        for order in orders:
            token_id = order.get('asset_id') or order.get('token_id')
            if token_id:
                token_ids.add(token_id)
                market = order.get('market', 'Unknown')
                token_to_market[token_id] = market
        
        print(f"Found {len(token_ids)} unique token IDs from orders")
        print()
        
        if not token_ids:
            print("✅ No token IDs found in recent orders")
            print("   This means you likely have no positions")
            return
        
        # Check balance for each token
        positions = []
        
        for token_id in token_ids:
            try:
                # Query on-chain balance
                balance = ctf_contract.functions.balanceOf(
                    Web3.to_checksum_address(wallet_address),
                    int(token_id)
                ).call()
                
                if balance > 0:
                    market_id = token_to_market.get(token_id, 'Unknown')
                    
                    # Try to get market name from Gamma API
                    market_name = market_id
                    if market_id.startswith('0x'):
                        market_info = get_market_info(market_id)
                        if market_info:
                            market_name = market_info.get('question', market_id)
                    
                    positions.append({
                        'token_id': token_id,
                        'balance': balance,
                        'market_id': market_id,
                        'market_name': market_name
                    })
                    
            except Exception as e:
                print(f"⚠️  Error checking token {token_id}: {e}")
        
        # Display positions
        if not positions:
            print("✅ No positions found")
            print()
            print("This means:")
            print("  • You have no outcome token balances")
            print("  • All your orders are still pending (not filled)")
            return
        
        print(f"Found {len(positions)} position(s)")
        print()
        
        total_shares = 0
        
        for i, pos in enumerate(positions, 1):
            print(f"Position {i}:")
            print(f"  Market: {pos['market_name']}")
            print(f"  Token ID: {pos['token_id']}")
            print(f"  Shares: {pos['balance']}")
            print()
            
            total_shares += pos['balance']
        
        print("=" * 70)
        print(f"TOTAL SHARES: {total_shares}")
        print("=" * 70)
        print()
        
        print("💡 To close positions:")
        print("   1. Go to: https://polymarket.com/profile")
        print("   2. Click on the position you want to close")
        print("   3. Click 'Sell' and choose 'Market' order")
        print("   4. Confirm the transaction")
        print()
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()

