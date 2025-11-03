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

# USDC contracts on Polygon
USDC_BRIDGED = '0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174'  # USDC.e (Polymarket uses this)
USDC_NATIVE = '0x3c499c542cEF5E3811e1192ce70d8cC03d5c3359'   # USDC (native)

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

def get_usdc_balance(address, contract_address):
    """Get USDC balance for a specific contract"""
    try:
        usdc_contract = w3.eth.contract(address=contract_address, abi=USDC_ABI)
        balance = usdc_contract.functions.balanceOf(address).call()
        decimals = usdc_contract.functions.decimals().call()
        balance_usdc = balance / (10 ** decimals)
        return float(balance_usdc)
    except Exception as e:
        print(f"Error getting USDC balance: {e}")
        return 0

def get_wallet_keys():
    """Get wallet private keys from .env (supports both new and legacy format)"""
    keys = []

    # Try new format first (WALLET_1_PK, WALLET_2_PK, etc.)
    for i in range(1, 11):
        key = os.getenv(f'WALLET_{i}_PK')
        if key:
            keys.append(key.strip())

    # If no keys found, try legacy format
    if not keys:
        keys_str = os.getenv('WALLET_PRIVATE_KEYS', '')
        if keys_str:
            keys = [k.strip() for k in keys_str.split(',') if k.strip()]

    return keys

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
    keys = get_wallet_keys()

    if not keys:
        print("❌ No wallet private keys found in .env")
        print()
        print("Please add wallet private keys in one of these formats:")
        print("  New format: WALLET_1_PK=0x...")
        print("  Legacy format: WALLET_PRIVATE_KEYS=0x...,0x...")
        sys.exit(1)

    print(f"Found {len(keys)} wallet(s)")
    print()
    
    # Check each wallet
    total_matic = 0
    total_usdc_bridged = 0
    total_usdc_native = 0

    for i, key in enumerate(keys, 1):
        try:
            # Get account from private key
            account = w3.eth.account.from_key(key)
            address = account.address

            # Get balances
            matic_balance = get_matic_balance(address)
            usdc_bridged = get_usdc_balance(address, USDC_BRIDGED)
            usdc_native = get_usdc_balance(address, USDC_NATIVE)

            # Update totals
            total_matic += matic_balance
            total_usdc_bridged += usdc_bridged
            total_usdc_native += usdc_native

            # Print wallet info
            print(f"Wallet {i}:")
            print(f"  Address:      {address}")
            print(f"  MATIC:        {matic_balance:.4f}")
            print(f"  USDC.e:       ${usdc_bridged:.2f} (Polymarket uses this)")
            print(f"  USDC native:  ${usdc_native:.2f}")

            # Warnings
            if matic_balance < 0.5:
                print(f"  ⚠️  Low MATIC balance! Need at least 0.5 MATIC for gas")
            if usdc_bridged < 50:
                print(f"  ⚠️  Low USDC.e balance! This is what Polymarket uses")
            if usdc_native > 0 and usdc_bridged == 0:
                print(f"  ⚠️  You have USDC native but need USDC.e for Polymarket!")
                print(f"      Swap at: https://app.uniswap.org/")

            print()

        except Exception as e:
            print(f"❌ Error checking wallet {i}: {e}")
            print()
    
    # Print totals
    print("=" * 70)
    print("TOTAL BALANCES:")
    print(f"  MATIC:        {total_matic:.4f}")
    print(f"  USDC.e:       ${total_usdc_bridged:.2f} (Polymarket uses this)")
    print(f"  USDC native:  ${total_usdc_native:.2f}")
    print("=" * 70)

    # Recommendations
    print()
    print("RECOMMENDATIONS:")

    if total_matic < len(keys) * 0.5:
        print(f"  ⚠️  Consider adding more MATIC (recommended: {len(keys) * 1} MATIC total)")
    else:
        print(f"  ✅ MATIC balance looks good")

    if total_usdc_bridged < 50:
        print(f"  ⚠️  Low USDC.e balance. Recommended minimum: $50-100")
        if total_usdc_native > 0:
            print(f"  💡 You have ${total_usdc_native:.2f} USDC native - swap to USDC.e!")
            print(f"     Swap at: https://app.uniswap.org/")
    else:
        print(f"  ✅ USDC.e balance looks good for trading")

    print()
    print("NOTE: Polymarket uses USDC.e (bridged USDC)")
    print(f"Contract: {USDC_BRIDGED}")
    print()

if __name__ == "__main__":
    main()

