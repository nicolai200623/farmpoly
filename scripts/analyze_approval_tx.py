#!/usr/bin/env python3
"""
Analyze USDC approval transaction on Polygon
"""

import sys
import os
import asyncio
import yaml
from pathlib import Path
from web3 import Web3

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Transaction hash to analyze
TX_HASH = "0xe1b9caf14831ccd8588a20b48d563c2abc7e66e45327a18ea61547965d9ddf88"

# Polygon addresses
USDC_ADDRESS = '0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174'  # USDC.e
CLOB_EXCHANGE_ADDRESS = '0x4bFb41d5B3570DeFd03C39a9A4D8dE6Bd8B8982E'  # Polymarket Exchange

# USDC ABI (minimal - just for allowance check)
USDC_ABI = [
    {
        "constant": True,
        "inputs": [
            {"name": "owner", "type": "address"},
            {"name": "spender", "type": "address"}
        ],
        "name": "allowance",
        "outputs": [{"name": "", "type": "uint256"}],
        "type": "function"
    }
]


async def main():
    """Analyze the approval transaction"""
    
    print("\n" + "="*80)
    print("🔍 USDC Approval Transaction Analysis")
    print("="*80 + "\n")
    
    # Load config to get RPC URL
    try:
        with open('config.yaml', 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
    except Exception as e:
        logger.error(f"❌ Failed to load config.yaml: {e}")
        return
    
    # Get RPC URL (try multiple locations)
    rpc_url = (
        config.get('rpc_url') or
        config.get('blockchain', {}).get('rpc_url') or
        config.get('blockchain', {}).get('polygon_rpc_url')
    )

    if not rpc_url:
        logger.error("❌ No Polygon RPC URL in config!")
        return

    logger.info(f"Using RPC: {rpc_url[:50]}...")
    
    # Connect to Polygon
    try:
        w3 = Web3(Web3.HTTPProvider(rpc_url))
        
        if not w3.is_connected():
            logger.error("❌ Failed to connect to Polygon RPC")
            return
        
        logger.info(f"✅ Connected to Polygon RPC")
        logger.info(f"   Chain ID: {w3.eth.chain_id}")
        logger.info(f"   Latest block: {w3.eth.block_number:,}")
        
    except Exception as e:
        logger.error(f"❌ RPC connection error: {e}")
        return
    
    # Get transaction details
    print(f"\n{'='*80}")
    print(f"📊 TRANSACTION DETAILS")
    print(f"{'='*80}\n")
    
    try:
        tx = w3.eth.get_transaction(TX_HASH)
        
        print(f"Transaction Hash: {TX_HASH}")
        print(f"From: {tx['from']}")
        print(f"To: {tx['to']}")
        print(f"Value: {w3.from_wei(tx['value'], 'ether')} MATIC")
        print(f"Gas Price: {w3.from_wei(tx['gasPrice'], 'gwei')} Gwei")
        print(f"Gas Limit: {tx['gas']:,}")
        print(f"Nonce: {tx['nonce']}")
        print(f"Block Number: {tx['blockNumber']:,}")
        
        # Check if it's to USDC contract
        if tx['to'].lower() == USDC_ADDRESS.lower():
            print(f"\n✅ Transaction is to USDC contract")
        else:
            print(f"\n⚠️  Transaction is NOT to USDC contract!")
            print(f"   Expected: {USDC_ADDRESS}")
            print(f"   Got: {tx['to']}")
        
    except Exception as e:
        logger.error(f"❌ Error getting transaction: {e}")
        return
    
    # Get transaction receipt
    print(f"\n{'='*80}")
    print(f"📋 TRANSACTION RECEIPT")
    print(f"{'='*80}\n")
    
    try:
        receipt = w3.eth.get_transaction_receipt(TX_HASH)
        
        print(f"Status: {'✅ SUCCESS' if receipt['status'] == 1 else '❌ FAILED'}")
        print(f"Gas Used: {receipt['gasUsed']:,}")
        print(f"Cumulative Gas Used: {receipt['cumulativeGasUsed']:,}")
        print(f"Logs: {len(receipt['logs'])} events")
        
        if receipt['status'] != 1:
            print(f"\n❌ TRANSACTION FAILED!")
            print(f"   The approval did not succeed on-chain")
            return
        
    except Exception as e:
        logger.error(f"❌ Error getting receipt: {e}")
        return
    
    # Decode input data to get approval amount
    print(f"\n{'='*80}")
    print(f"🔍 APPROVAL DETAILS")
    print(f"{'='*80}\n")
    
    try:
        input_data = tx['input']
        
        # Check if it's approve function (0x095ea7b3)
        if input_data[:10] == '0x095ea7b3':
            print(f"✅ Function: approve(address spender, uint256 amount)")
            
            # Decode parameters
            spender = '0x' + input_data[34:74]
            amount_hex = input_data[74:138]
            amount = int(amount_hex, 16)
            amount_usdc = amount / 1e6
            
            print(f"\nSpender: {spender}")
            
            if spender.lower() == CLOB_EXCHANGE_ADDRESS.lower():
                print(f"✅ Spender is Polymarket CLOB Exchange")
            else:
                print(f"⚠️  Spender is NOT Polymarket CLOB Exchange!")
                print(f"   Expected: {CLOB_EXCHANGE_ADDRESS}")
            
            print(f"\nApproval Amount:")
            print(f"   Raw: {amount:,} base units")
            print(f"   USDC: {amount_usdc:,.2f} USDC")
            
            if amount_usdc >= 1000:
                print(f"   ✅ Amount is sufficient (>= 1,000 USDC)")
            else:
                print(f"   ⚠️  Amount is LESS than 1,000 USDC!")
                print(f"   Bot requires at least 1,000 USDC approval")
        else:
            print(f"⚠️  Not an approve() function call")
            print(f"   Function signature: {input_data[:10]}")
        
    except Exception as e:
        logger.error(f"❌ Error decoding input: {e}")
    
    # Check current allowance
    print(f"\n{'='*80}")
    print(f"🔍 CURRENT ALLOWANCE CHECK")
    print(f"{'='*80}\n")
    
    try:
        usdc_contract = w3.eth.contract(
            address=Web3.to_checksum_address(USDC_ADDRESS),
            abi=USDC_ABI
        )
        
        from_address = tx['from']
        
        current_allowance = usdc_contract.functions.allowance(
            Web3.to_checksum_address(from_address),
            Web3.to_checksum_address(CLOB_EXCHANGE_ADDRESS)
        ).call()
        
        current_allowance_usdc = current_allowance / 1e6
        
        print(f"Wallet: {from_address}")
        print(f"Spender: {CLOB_EXCHANGE_ADDRESS}")
        print(f"\nCurrent Allowance:")
        print(f"   Raw: {current_allowance:,} base units")
        print(f"   USDC: {current_allowance_usdc:,.2f} USDC")
        
        if current_allowance >= 1000 * 1e6:
            print(f"\n✅ CURRENT ALLOWANCE IS SUFFICIENT!")
            print(f"   Bot should work correctly")
        elif current_allowance > 0:
            print(f"\n⚠️  CURRENT ALLOWANCE IS PARTIAL!")
            print(f"   Current: {current_allowance_usdc:,.2f} USDC")
            print(f"   Required: 1,000 USDC")
            print(f"   Missing: {1000 - current_allowance_usdc:,.2f} USDC")
        else:
            print(f"\n❌ NO ALLOWANCE!")
            print(f"   The approval transaction succeeded but allowance is 0")
            print(f"   This is very unusual - possible issues:")
            print(f"   - Wrong wallet address")
            print(f"   - Wrong spender address")
            print(f"   - Approval was revoked later")
        
    except Exception as e:
        logger.error(f"❌ Error checking allowance: {e}")
        import traceback
        traceback.print_exc()
    
    # Summary
    print(f"\n{'='*80}")
    print(f"📊 SUMMARY")
    print(f"{'='*80}\n")
    
    print(f"Transaction: {TX_HASH}")
    print(f"Status: {'✅ SUCCESS' if receipt['status'] == 1 else '❌ FAILED'}")
    print(f"From: {from_address}")
    print(f"Approved Amount: {amount_usdc:,.2f} USDC")
    print(f"Current Allowance: {current_allowance_usdc:,.2f} USDC")
    
    if current_allowance >= 1000 * 1e6:
        print(f"\n✅ CONCLUSION: Approval is working correctly!")
        print(f"   If bot still shows 'approval needed', it's a code bug")
    else:
        print(f"\n❌ CONCLUSION: Approval is NOT sufficient!")
        print(f"   Need to approve at least 1,000 USDC")
    
    print(f"\n{'='*80}\n")


if __name__ == "__main__":
    asyncio.run(main())

