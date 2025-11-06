#!/usr/bin/env python3
"""
Approve CTF (Conditional Token Framework) for Polymarket trading
This is required to SELL outcome tokens (close positions)

Based on official Polymarket script:
https://gist.github.com/poly-rodr/44313920481de58d5a3f6d1f8226bd5e
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
from eth_account import Account
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
CTF_ADDRESS = '0x4D97DCd97eC945f40cF65F87097ACe5EA0476045'  # Conditional Token Framework
CLOB_EXCHANGE_ADDRESS = '0x4bFb41d5B3570DeFd03C39a9A4D8dE6Bd8B8982E'  # CTF Exchange
NEG_RISK_CTF_EXCHANGE = '0xC5d563A36AE78145C45a50134d48A1215220f80a'  # Neg Risk CTF Exchange
NEG_RISK_ADAPTER = '0xd91E80cF2E7be2e162c6513ceD06f1dD0dA35296'  # Neg Risk Adapter

# CTF ERC1155 ABI (setApprovalForAll function)
CTF_ABI = """[{
    "inputs": [
        { "internalType": "address", "name": "operator", "type": "address" },
        { "internalType": "bool", "name": "approved", "type": "bool" }
    ],
    "name": "setApprovalForAll",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
}, {
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


class CTFApprover:
    """Handles CTF approval for Polymarket trading"""
    
    def __init__(self, config: dict):
        self.config = config
        
        # Get RPC URL from config or env
        rpc_url = config.get('rpc_url') or os.getenv('POLYGON_RPC_URL', 'https://polygon-rpc.com')
        
        # Initialize Web3
        self.w3 = Web3(Web3.HTTPProvider(rpc_url))
        self.w3.middleware_onion.inject(poa_middleware, layer=0)
        
        if not self.w3.is_connected():
            logger.error("❌ Failed to connect to Polygon RPC")
            raise ConnectionError("Cannot connect to Polygon network")
        
        # Initialize CTF contract
        self.ctf_contract = self.w3.eth.contract(
            address=Web3.to_checksum_address(CTF_ADDRESS),
            abi=CTF_ABI
        )
        
        logger.info(f"✅ Connected to Polygon RPC: {rpc_url[:50]}...")
    
    async def check_approval(self, wallet_address: str, operator: str) -> bool:
        """
        Check if operator is approved for all tokens
        
        Args:
            wallet_address: Owner wallet address
            operator: Operator address (exchange contract)
        
        Returns:
            True if approved, False otherwise
        """
        try:
            checksum_owner = Web3.to_checksum_address(wallet_address)
            checksum_operator = Web3.to_checksum_address(operator)
            
            is_approved = self.ctf_contract.functions.isApprovedForAll(
                checksum_owner,
                checksum_operator
            ).call()
            
            return is_approved
            
        except Exception as e:
            logger.error(f"❌ Error checking approval: {e}")
            return False
    
    async def approve_operator(self, wallet: dict, operator: str, operator_name: str) -> bool:
        """
        Approve operator to manage all CTF tokens
        
        Args:
            wallet: Wallet dict with 'private_key' and 'address'
            operator: Operator address to approve
            operator_name: Human-readable name for logging
        
        Returns:
            True if successful, False otherwise
        """
        try:
            # Get account from private key
            private_key = wallet['private_key']
            if not private_key.startswith('0x'):
                private_key = '0x' + private_key
            
            account = Account.from_key(private_key)
            address = Web3.to_checksum_address(account.address)
            
            # Check if already approved
            is_approved = await self.check_approval(address, operator)
            if is_approved:
                logger.info(f"✅ Already approved for {operator_name}")
                return True
            
            # Build approval transaction
            nonce = self.w3.eth.get_transaction_count(address)
            gas_price = self.w3.eth.gas_price
            
            approve_txn = self.ctf_contract.functions.setApprovalForAll(
                Web3.to_checksum_address(operator),
                True
            ).build_transaction({
                'from': address,
                'nonce': nonce,
                'gas': 100000,  # Standard gas limit for setApprovalForAll
                'gasPrice': gas_price,
                'chainId': 137  # Polygon mainnet
            })
            
            # Sign transaction
            signed_txn = self.w3.eth.account.sign_transaction(approve_txn, private_key)
            
            # Send transaction
            tx_hash = self.w3.eth.send_raw_transaction(signed_txn.raw_transaction)
            
            logger.info(f"📤 Approval transaction sent: {tx_hash.hex()}")
            logger.info(f"   Operator: {operator_name}")
            
            # Wait for confirmation
            logger.info("⏳ Waiting for confirmation...")
            receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash, timeout=120)
            
            if receipt['status'] == 1:
                logger.info(f"✅ Approval confirmed! Gas used: {receipt['gasUsed']}")
                return True
            else:
                logger.error(f"❌ Approval transaction failed")
                return False
                
        except Exception as e:
            logger.error(f"❌ Error approving {operator_name}: {e}")
            import traceback
            logger.debug(traceback.format_exc())
            return False
    
    async def approve_all_operators(self, wallet: dict) -> dict:
        """
        Approve all required operators for a wallet
        
        Args:
            wallet: Wallet dict with 'private_key' and 'address'
        
        Returns:
            Dict mapping operator name to approval status
        """
        results = {}
        
        # List of operators to approve
        operators = [
            (CLOB_EXCHANGE_ADDRESS, "CTF Exchange"),
            (NEG_RISK_CTF_EXCHANGE, "Neg Risk CTF Exchange"),
            (NEG_RISK_ADAPTER, "Neg Risk Adapter"),
        ]
        
        for operator_address, operator_name in operators:
            logger.info(f"\n🔄 Approving {operator_name}...")
            success = await self.approve_operator(wallet, operator_address, operator_name)
            results[operator_name] = success
            
            # Small delay between approvals
            if success:
                await asyncio.sleep(2)
        
        return results


async def main():
    """Main approval function"""
    
    print("\n" + "="*70)
    print("🔐 CTF Approval Tool for Polymarket Trading")
    print("="*70)
    print("\n📝 What is CTF approval?")
    print("   CTF (Conditional Token Framework) approval allows Polymarket")
    print("   exchanges to transfer your outcome tokens when you SELL them.")
    print("\n⚠️  This is REQUIRED to:")
    print("   - Close positions (sell outcome tokens)")
    print("   - Take profits")
    print("   - Exit markets")
    print("\n💡 You only need to run this ONCE per wallet.")
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
    
    # Initialize approver
    try:
        approver = CTFApprover(config)
    except Exception as e:
        logger.error(f"❌ Failed to initialize approver: {e}")
        return
    
    # Confirm
    print(f"⚠️  You are about to approve CTF for {len(wallets)} wallets")
    print("   This will approve 3 operators per wallet:")
    print("   - CTF Exchange (for normal markets)")
    print("   - Neg Risk CTF Exchange (for negative risk markets)")
    print("   - Neg Risk Adapter (for negative risk markets)")
    print(f"\n   Total transactions: {len(wallets) * 3}")
    print("   Gas cost: ~0.01 MATIC per transaction (~0.03 MATIC per wallet)")
    
    confirm = input("\nContinue? (yes/no): ").strip().lower()
    
    if confirm not in ['yes', 'y']:
        logger.info("❌ Cancelled by user")
        return
    
    # Approve all wallets
    print("\n" + "="*70)
    print("🚀 Starting CTF approval process...")
    print("="*70 + "\n")
    
    all_results = {}
    
    for i, wallet in enumerate(wallets, 1):
        address = wallet['address']
        
        print(f"\n{'='*70}")
        print(f"Wallet {i}/{len(wallets)}: {address[:10]}...{address[-8:]}")
        print(f"{'='*70}")
        
        results = await approver.approve_all_operators(wallet)
        all_results[address] = results
        
        # Summary for this wallet
        approved = sum(1 for v in results.values() if v)
        total = len(results)
        
        if approved == total:
            logger.info(f"\n✅ Wallet {i} fully approved ({approved}/{total})")
        else:
            logger.warning(f"\n⚠️  Wallet {i} partially approved ({approved}/{total})")
    
    # Final summary
    print("\n" + "="*70)
    print("📊 FINAL RESULTS")
    print("="*70 + "\n")
    
    for address, results in all_results.items():
        approved = sum(1 for v in results.values() if v)
        total = len(results)
        status = "✅ FULL" if approved == total else f"⚠️  PARTIAL ({approved}/{total})"
        print(f"{status} - {address[:10]}...{address[-8:]}")
    
    total_wallets = len(all_results)
    fully_approved = sum(1 for results in all_results.values() if all(results.values()))
    
    print(f"\n{'='*70}")
    print(f"Total: {fully_approved}/{total_wallets} wallets fully approved")
    print(f"{'='*70}\n")
    
    if fully_approved == total_wallets:
        print("✅ All wallets approved! You can now:")
        print("   - Close positions")
        print("   - Take profits")
        print("   - Sell outcome tokens")
        print("\n   Run: python main.py")
    else:
        print("⚠️  Some wallets failed to approve.")
        print("   Check the logs above for errors.")
        print("   Common issues:")
        print("   - Insufficient MATIC for gas fees")
        print("   - Invalid private key")
        print("   - RPC connection issues")


if __name__ == "__main__":
    asyncio.run(main())

