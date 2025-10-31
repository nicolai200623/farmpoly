#!/usr/bin/env python3
"""
Script to check wallet balances
"""

import os
import sys
from web3 import Web3
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Connect to Polygon
rpc_url = os.getenv('POLYGON_RPC_URL', 'https://polygon-rpc.com')
w3 = Web3(Web3.HTTPProvider(rpc_url))

# USDC contract on Polygon
USDC_ADDRESS = '0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174'
USDC_ABI = [
    {
        "constant": True,
        "inputs": [{"name": "_owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "balance", "type": "uint256"}],
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "decimals",
        "outputs": [{"name": "", "type": "uint8"}],
        "type": "function"
    }
]

def check_connection():
    """Check if connected to Polygon"""
    try:
        block = w3.eth.block_number
        print(f"✅ Connected to Polygon (Block: {block})")
        return True
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        return False

def get_matic_balance(address):
    """Get MATIC balance"""
    try:
        balance_wei = w3.eth.get_balance(address)
        balance_matic = w3.from_wei(balance_wei, 'ether')
        return float(balance_matic)
    except Exception as e:
        print(f"Error getting MATIC balance: {e}")
        return 0

def get_usdc_balance(address):
    """Get USDC balance"""
    try:
        usdc_contract = w3.eth.contract(address=USDC_ADDRESS, abi=USDC_ABI)
        balance = usdc_contract.functions.balanceOf(address).call()
        decimals = usdc_contract.functions.decimals().call()
        balance_usdc = balance / (10 ** decimals)
        return float(balance_usdc)
    except Exception as e:
        print(f"Error getting USDC balance: {e}")
        return 0

def main():
    """Main function"""
    print("=" * 60)
    print("Polymarket Bot - Wallet Balance Checker")
    print("=" * 60)
    print()
    
    # Check connection
    if not check_connection():
        sys.exit(1)
    
    print()
    
    # Get wallet private keys
    keys_str = os.getenv('WALLET_PRIVATE_KEYS', '')
    if not keys_str:
        print("❌ No wallet private keys found in .env")
        sys.exit(1)
    
    keys = [k.strip() for k in keys_str.split(',') if k.strip()]
    
    if not keys:
        print("❌ No valid wallet private keys")
        sys.exit(1)
    
    print(f"Found {len(keys)} wallet(s)")
    print()
    
    # Check each wallet
    total_matic = 0
    total_usdc = 0
    
    for i, key in enumerate(keys, 1):
        try:
            # Get account from private key
            account = w3.eth.account.from_key(key)
            address = account.address
            
            # Get balances
            matic_balance = get_matic_balance(address)
            usdc_balance = get_usdc_balance(address)
            
            # Update totals
            total_matic += matic_balance
            total_usdc += usdc_balance
            
            # Print wallet info
            print(f"Wallet {i}:")
            print(f"  Address: {address}")
            print(f"  MATIC:   {matic_balance:.4f}")
            print(f"  USDC:    ${usdc_balance:.2f}")
            
            # Warnings
            if matic_balance < 1:
                print(f"  ⚠️  Low MATIC balance! Need at least 1 MATIC for gas")
            if usdc_balance < 100:
                print(f"  ⚠️  Low USDC balance! Consider adding more funds")
            
            print()
            
        except Exception as e:
            print(f"❌ Error checking wallet {i}: {e}")
            print()
    
    # Print totals
    print("=" * 60)
    print("TOTAL BALANCES:")
    print(f"  MATIC:   {total_matic:.4f}")
    print(f"  USDC:    ${total_usdc:.2f}")
    print("=" * 60)
    
    # Recommendations
    print()
    print("RECOMMENDATIONS:")
    
    if total_matic < len(keys) * 5:
        print(f"  ⚠️  Consider adding more MATIC (recommended: {len(keys) * 10} MATIC total)")
    else:
        print(f"  ✅ MATIC balance looks good")
    
    if total_usdc < 1000:
        print(f"  ⚠️  Low total USDC. Recommended minimum: $1000")
    else:
        print(f"  ✅ USDC balance looks good")
    
    print()

if __name__ == "__main__":
    main()

