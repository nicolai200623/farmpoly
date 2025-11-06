#!/usr/bin/env python3
"""
Check CTF approval status for all wallets
"""

import sys
import os
import asyncio
import yaml
from pathlib import Path
from web3 import Web3
try:
    # Web3.py v7+
    from web3.middleware import ExtraDataToPOAMiddleware
    poa_middleware = ExtraDataToPOAMiddleware
except ImportError:
    # Web3.py v6 and earlier
    from web3.middleware import geth_poa_middleware
    poa_middleware = geth_poa_middleware
import logging

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from wallet_manager import WalletManager

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Polygon Mainnet Addresses
CTF_ADDRESS = '0x4D97DCd97eC945f40cF65F87097ACe5EA0476045'
CLOB_EXCHANGE_ADDRESS = '0x4bFb41d5B3570DeFd03C39a9A4D8dE6Bd8B8982E'
NEG_RISK_CTF_EXCHANGE = '0xC5d563A36AE78145C45a50134d48A1215220f80a'
NEG_RISK_ADAPTER = '0xd91E80cF2E7be2e162c6513ceD06f1dD0dA35296'

# CTF ABI
CTF_ABI = """[{
    "inputs": [
        { "internalType": "address", "name": "owner", "type": "address" },
        { "internalType": "address", "name": "operator", "type": "address" }
    ],
    "name": "isApprovedForAll",
    "outputs": [
        { "internalType": "bool", "name": "", "type": "bool" }
    ],
    "stateMutability": "view",
    "type": "function"
}]"""


async def check_wallet_approvals(w3, ctf_contract, wallet_address: str):
    """Check all CTF approvals for a wallet"""
    
    operators = [
        (CLOB_EXCHANGE_ADDRESS, "CTF Exchange"),
        (NEG_RISK_CTF_EXCHANGE, "Neg Risk CTF Exchange"),
        (NEG_RISK_ADAPTER, "Neg Risk Adapter"),
    ]
    
    results = {}
    
    for operator_address, operator_name in operators:
        try:
            checksum_owner = Web3.to_checksum_address(wallet_address)
            checksum_operator = Web3.to_checksum_address(operator_address)
            
            is_approved = ctf_contract.functions.isApprovedForAll(
                checksum_owner,
                checksum_operator
            ).call()
            
            results[operator_name] = is_approved
            
        except Exception as e:
            logger.error(f"❌ Error checking {operator_name}: {e}")
            results[operator_name] = False
    
    return results


async def main():
    """Main check function"""
    
    print("\n" + "="*70)
    print("🔍 CTF Approval Status Checker")
    print("="*70 + "\n")
    
    # Load config
    try:
        with open('config.yaml', 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
    except Exception as e:
        logger.error(f"❌ Failed to load config.yaml: {e}")
        return
    
    # Initialize wallet manager
    try:
        wallet_manager = WalletManager(config)
        wallets = wallet_manager.wallets
        
        if not wallets:
            logger.error("❌ No wallets loaded! Check your .env file")
            return
        
        logger.info(f"✅ Loaded {len(wallets)} wallets\n")
        
    except Exception as e:
        logger.error(f"❌ Failed to load wallets: {e}")
        return
    
    # Initialize Web3
    try:
        rpc_url = config.get('rpc_url') or os.getenv('POLYGON_RPC_URL', 'https://polygon-rpc.com')
        w3 = Web3(Web3.HTTPProvider(rpc_url))
        w3.middleware_onion.inject(poa_middleware, layer=0)
        
        if not w3.is_connected():
            logger.error("❌ Failed to connect to Polygon RPC")
            return
        
        ctf_contract = w3.eth.contract(
            address=Web3.to_checksum_address(CTF_ADDRESS),
            abi=CTF_ABI
        )
        
        logger.info(f"✅ Connected to Polygon RPC\n")
        
    except Exception as e:
        logger.error(f"❌ Failed to initialize Web3: {e}")
        return
    
    # Check all wallets
    print("="*70)
    print("📊 APPROVAL STATUS")
    print("="*70 + "\n")
    
    all_results = {}
    
    for i, wallet in enumerate(wallets, 1):
        address = wallet['address']
        
        print(f"Wallet {i}/{len(wallets)}: {address[:10]}...{address[-8:]}")
        
        results = await check_wallet_approvals(w3, ctf_contract, address)
        all_results[address] = results
        
        for operator_name, is_approved in results.items():
            status = "✅ APPROVED" if is_approved else "❌ NOT APPROVED"
            print(f"  {status} - {operator_name}")
        
        # Summary for this wallet
        approved = sum(1 for v in results.values() if v)
        total = len(results)
        
        if approved == total:
            print(f"  ✅ Fully approved ({approved}/{total})\n")
        elif approved > 0:
            print(f"  ⚠️  Partially approved ({approved}/{total})\n")
        else:
            print(f"  ❌ Not approved ({approved}/{total})\n")
    
    # Final summary
    print("="*70)
    print("📈 SUMMARY")
    print("="*70 + "\n")
    
    total_wallets = len(all_results)
    fully_approved = sum(1 for results in all_results.values() if all(results.values()))
    partially_approved = sum(1 for results in all_results.values() if any(results.values()) and not all(results.values()))
    not_approved = sum(1 for results in all_results.values() if not any(results.values()))
    
    print(f"✅ Fully approved: {fully_approved}/{total_wallets}")
    print(f"⚠️  Partially approved: {partially_approved}/{total_wallets}")
    print(f"❌ Not approved: {not_approved}/{total_wallets}")
    
    print(f"\n{'='*70}\n")
    
    if fully_approved == total_wallets:
        print("✅ All wallets are fully approved!")
        print("   You can close positions and take profits.")
    elif fully_approved > 0:
        print("⚠️  Some wallets are not fully approved.")
        print("   Run: python scripts/approve_ctf.py")
    else:
        print("❌ No wallets are approved!")
        print("   You MUST run: python scripts/approve_ctf.py")
        print("   Otherwise you cannot close positions or take profits.")


if __name__ == "__main__":
    asyncio.run(main())

