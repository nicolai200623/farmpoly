"""
USDC Approver Module
Handles USDC token approval for Polymarket CLOB trading
"""

import asyncio
import logging
from web3 import Web3
from eth_account import Account
from typing import Dict, Optional
import os

logger = logging.getLogger(__name__)

# Polygon Mainnet Addresses
# ⚠️ IMPORTANT: Polymarket uses USDC.e (bridged USDC), NOT USDC native!
USDC_ADDRESS = '0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174'  # USDC.e (bridged) - Polymarket uses this
CLOB_EXCHANGE_ADDRESS = '0x4bFb41d5B3570DeFd03C39a9A4D8dE6Bd8B8982E'  # Polymarket Exchange

# USDC ERC20 ABI (minimal - just approve function)
USDC_ABI = [
    {
        "constant": False,
        "inputs": [
            {"name": "_spender", "type": "address"},
            {"name": "_value", "type": "uint256"}
        ],
        "name": "approve",
        "outputs": [{"name": "", "type": "bool"}],
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [
            {"name": "_owner", "type": "address"},
            {"name": "_spender", "type": "address"}
        ],
        "name": "allowance",
        "outputs": [{"name": "", "type": "uint256"}],
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [{"name": "_owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "balance", "type": "uint256"}],
        "type": "function"
    }
]


class USDCApprover:
    """Handles USDC approval for trading"""
    
    def __init__(self, config: dict):
        self.config = config
        
        # Get RPC URL from config or env
        rpc_url = config.get('rpc_url') or os.getenv('POLYGON_RPC_URL', 'https://polygon-rpc.com')
        
        # Initialize Web3
        self.w3 = Web3(Web3.HTTPProvider(rpc_url))
        
        if not self.w3.is_connected():
            logger.error("❌ Failed to connect to Polygon RPC")
            raise ConnectionError("Cannot connect to Polygon network")
        
        # Initialize USDC contract
        self.usdc_contract = self.w3.eth.contract(
            address=Web3.to_checksum_address(USDC_ADDRESS),
            abi=USDC_ABI
        )
        
        logger.info(f"✅ Connected to Polygon RPC: {rpc_url[:50]}...")
    
    async def check_and_approve_wallet(self, wallet: Dict, amount_usdc: float = 10000) -> bool:
        """
        Check if wallet has USDC approval and approve if needed
        
        Args:
            wallet: Wallet dict with 'address' and 'private_key'
            amount_usdc: Amount to approve (default 10,000 USDC)
        
        Returns:
            True if approved or already has approval, False on error
        """
        try:
            address = Web3.to_checksum_address(wallet['address'])
            
            # Check current allowance
            current_allowance = await self._get_allowance(address)
            required_amount = int(amount_usdc * 1e6)  # USDC has 6 decimals
            
            if current_allowance >= required_amount:
                logger.info(f"✅ Wallet {address[:10]}... already has sufficient USDC approval")
                return True
            
            # Need to approve
            logger.info(f"🔄 Approving {amount_usdc:,.0f} USDC for wallet {address[:10]}...")
            
            success = await self._approve_usdc(wallet, required_amount)
            
            if success:
                logger.info(f"✅ Successfully approved {amount_usdc:,.0f} USDC")
                return True
            else:
                logger.error(f"❌ Failed to approve USDC")
                return False
                
        except Exception as e:
            logger.error(f"❌ Error checking/approving wallet: {e}")
            return False
    
    async def _get_allowance(self, address: str) -> int:
        """Get current USDC allowance for CLOB exchange"""
        try:
            checksum_address = Web3.to_checksum_address(address)
            checksum_exchange = Web3.to_checksum_address(CLOB_EXCHANGE_ADDRESS)

            logger.debug(f"Checking allowance for {checksum_address[:10]}...")
            logger.debug(f"Exchange address: {checksum_exchange}")

            allowance = self.usdc_contract.functions.allowance(
                checksum_address,
                checksum_exchange
            ).call()

            logger.debug(f"Allowance retrieved: {allowance} base units ({allowance/1e6:.2f} USDC)")

            return allowance

        except Exception as e:
            logger.error(f"❌ Error getting allowance for {address[:10]}...: {e}")
            logger.error(f"   This usually means RPC connection issue or invalid address")
            import traceback
            logger.debug(traceback.format_exc())
            return 0
    
    async def _approve_usdc(self, wallet: Dict, amount: int) -> bool:
        """
        Approve USDC spending for CLOB exchange
        
        Args:
            wallet: Wallet dict with 'private_key'
            amount: Amount in USDC base units (1e6 = 1 USDC)
        
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
            
            # Build approve transaction
            nonce = self.w3.eth.get_transaction_count(address)
            
            # Get current gas price
            gas_price = self.w3.eth.gas_price
            
            # Build transaction
            approve_txn = self.usdc_contract.functions.approve(
                Web3.to_checksum_address(CLOB_EXCHANGE_ADDRESS),
                amount
            ).build_transaction({
                'from': address,
                'nonce': nonce,
                'gas': 100000,  # Standard gas limit for approve
                'gasPrice': gas_price,
                'chainId': 137  # Polygon mainnet
            })
            
            # Sign transaction
            signed_txn = self.w3.eth.account.sign_transaction(approve_txn, private_key)
            
            # Send transaction
            tx_hash = self.w3.eth.send_raw_transaction(signed_txn.raw_transaction)
            
            logger.info(f"📤 Approval transaction sent: {tx_hash.hex()}")
            
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
            logger.error(f"❌ Error approving USDC: {e}")
            return False
    
    async def check_usdc_balance(self, address: str) -> float:
        """
        Check USDC balance for an address
        
        Args:
            address: Wallet address
        
        Returns:
            USDC balance as float
        """
        try:
            balance = self.usdc_contract.functions.balanceOf(
                Web3.to_checksum_address(address)
            ).call()
            
            # Convert from base units (6 decimals) to USDC
            return balance / 1e6
            
        except Exception as e:
            logger.error(f"Error checking USDC balance: {e}")
            return 0.0
    
    async def check_matic_balance(self, address: str) -> float:
        """
        Check MATIC balance for gas fees
        
        Args:
            address: Wallet address
        
        Returns:
            MATIC balance as float
        """
        try:
            balance = self.w3.eth.get_balance(Web3.to_checksum_address(address))
            
            # Convert from wei to MATIC
            return balance / 1e18
            
        except Exception as e:
            logger.error(f"Error checking MATIC balance: {e}")
            return 0.0
    
    async def approve_all_wallets(self, wallets: list, amount_usdc: float = 10000) -> Dict[str, bool]:
        """
        Approve USDC for all wallets
        
        Args:
            wallets: List of wallet dicts
            amount_usdc: Amount to approve per wallet
        
        Returns:
            Dict mapping wallet address to approval status
        """
        results = {}
        
        for wallet in wallets:
            address = wallet['address']
            
            # Check balances first
            usdc_balance = await self.check_usdc_balance(address)
            matic_balance = await self.check_matic_balance(address)
            
            logger.info(f"\n💰 Wallet {address[:10]}...")
            logger.info(f"   USDC: {usdc_balance:,.2f}")
            logger.info(f"   MATIC: {matic_balance:.4f}")
            
            # Check if wallet has enough USDC
            if usdc_balance < 10:
                logger.warning(f"⚠️  Low USDC balance! Need at least 100 USDC for trading")
            
            # Check if wallet has enough MATIC for gas
            if matic_balance < 0.1:
                logger.warning(f"⚠️  Low MATIC balance! Need at least 0.5 MATIC for gas fees")
                results[address] = False
                continue
            
            # Approve USDC
            success = await self.check_and_approve_wallet(wallet, amount_usdc)
            results[address] = success
            
            # Small delay between approvals
            await asyncio.sleep(2)
        
        # Summary
        approved = sum(1 for v in results.values() if v)
        total = len(results)
        
        logger.info(f"\n📊 Approval Summary: {approved}/{total} wallets approved")
        
        return results


# Convenience function for quick approval
async def approve_wallets_for_trading(wallets: list, config: dict) -> bool:
    """
    Quick function to approve all wallets for trading
    
    Args:
        wallets: List of wallet dicts
        config: Bot configuration
    
    Returns:
        True if all wallets approved successfully
    """
    approver = USDCApprover(config)
    results = await approver.approve_all_wallets(wallets)
    
    # Return True only if all wallets approved
    return all(results.values())

