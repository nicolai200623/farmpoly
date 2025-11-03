"""
Reward Manager Module
Automated reward checking and withdrawal system for Polymarket trading bot
"""

import asyncio
import logging
import time
from typing import Dict, List, Optional, Tuple
from datetime import datetime
from web3 import Web3
from eth_account import Account
import aiohttp
import os
from dotenv import load_dotenv

logger = logging.getLogger(__name__)


class RewardManager:
    """Manages automated reward checking and withdrawal"""
    
    def __init__(self, config: dict):
        """
        Initialize reward manager
        
        Args:
            config: Configuration dictionary with reward settings
        """
        self.config = config
        self.reward_config = config.get('reward_management', {})
        
        # Load environment variables
        load_dotenv()
        
        # Web3 setup
        rpc_url = os.getenv('POLYGON_RPC_URL', config.get('rpc_url', 'https://polygon-rpc.com'))
        self.w3 = Web3(Web3.HTTPProvider(rpc_url))
        
        # Withdrawal configuration
        self.withdrawal_wallet = os.getenv('REWARD_WITHDRAWAL_WALLET', '')
        self.min_withdrawal_threshold = float(os.getenv('MIN_REWARD_THRESHOLD', 
                                                        self.reward_config.get('min_withdrawal_threshold', 10)))
        self.check_interval = int(os.getenv('REWARD_CHECK_INTERVAL', 
                                            self.reward_config.get('check_interval', 3600)))
        
        # USDC contract on Polygon
        self.usdc_address = Web3.to_checksum_address('0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174')
        self.usdc_abi = [
            {
                "constant": True,
                "inputs": [{"name": "_owner", "type": "address"}],
                "name": "balanceOf",
                "outputs": [{"name": "balance", "type": "uint256"}],
                "type": "function"
            },
            {
                "constant": False,
                "inputs": [
                    {"name": "_to", "type": "address"},
                    {"name": "_value", "type": "uint256"}
                ],
                "name": "transfer",
                "outputs": [{"name": "", "type": "bool"}],
                "type": "function"
            }
        ]
        
        # Polymarket reward contract (if available)
        self.reward_contract_address = os.getenv('POLYMARKET_REWARD_CONTRACT', '')
        
        # Statistics
        self.stats = {
            'total_rewards_checked': 0,
            'total_withdrawals': 0,
            'total_withdrawn_amount': 0.0,
            'last_check_time': 0,
            'last_withdrawal_time': 0,
            'failed_withdrawals': 0,
            'check_errors': 0
        }
        
        # Session for API calls
        self.session = None
        
        logger.info("✅ Reward Manager initialized")
        logger.info(f"   Check interval: {self.check_interval}s ({self.check_interval/3600:.1f}h)")
        logger.info(f"   Min withdrawal threshold: ${self.min_withdrawal_threshold:.2f}")
        if self.withdrawal_wallet:
            logger.info(f"   Withdrawal wallet: {self.withdrawal_wallet[:10]}...{self.withdrawal_wallet[-8:]}")
        else:
            logger.warning("⚠️  No withdrawal wallet configured!")
    
    async def initialize(self):
        """Initialize async resources"""
        if not self.session:
            self.session = aiohttp.ClientSession()
        
        # Verify Web3 connection
        if not self.w3.is_connected():
            logger.error("❌ Failed to connect to Polygon RPC")
            raise ConnectionError("Cannot connect to Polygon network")
        
        logger.info("✅ Reward Manager async resources initialized")
    
    async def close(self):
        """Close async resources"""
        if self.session:
            await self.session.close()
            self.session = None
    
    async def check_rewards(self, wallets: List[Dict]) -> Dict[str, float]:
        """
        Check available rewards for all wallets from Polymarket Rewards API

        ⚠️ IMPORTANT: This checks ACTUAL REWARDS from Polymarket, NOT wallet USDC balance!

        Args:
            wallets: List of wallet dictionaries with 'address' and 'private_key'

        Returns:
            Dictionary mapping wallet address to reward amount in USDC
        """
        try:
            self.stats['total_rewards_checked'] += 1
            self.stats['last_check_time'] = time.time()

            rewards = {}

            for wallet in wallets:
                address = wallet['address']
                try:
                    # Convert to checksum address if needed
                    if not Web3.is_checksum_address(address):
                        address = Web3.to_checksum_address(address)

                    # ✅ Check ACTUAL rewards from Polymarket API
                    api_rewards = await self.check_polymarket_rewards_api(address)

                    if api_rewards is not None:
                        # Got rewards from API
                        rewards[address] = api_rewards
                        logger.debug(f"Wallet {address[:10]}... has ${api_rewards:.2f} rewards from API")
                    else:
                        # API not available - set to 0 (DO NOT use wallet balance!)
                        rewards[address] = 0.0
                        logger.debug(f"Wallet {address[:10]}... - API unavailable, assuming $0 rewards")

                except Exception as e:
                    logger.error(f"Error checking rewards for {wallet['address']}: {e}")
                    rewards[wallet['address']] = 0.0

            total_rewards = sum(rewards.values())
            logger.info(f"💰 Total ACTUAL rewards across {len(wallets)} wallets: ${total_rewards:.2f} USDC")

            return rewards

        except Exception as e:
            logger.error(f"Error checking rewards: {e}")
            self.stats['check_errors'] += 1
            return {}
    
    async def check_polymarket_rewards_api(self, wallet_address: str) -> Optional[float]:
        """
        Check ACTUAL rewards via Polymarket Rewards API

        ⚠️ IMPORTANT: This checks REAL rewards from Polymarket's reward program,
        NOT the wallet's USDC balance!

        Args:
            wallet_address: Wallet address to check

        Returns:
            Reward amount or None if unavailable
        """
        try:
            if not self.session:
                await self.initialize()

            # Convert to checksum address
            if not Web3.is_checksum_address(wallet_address):
                wallet_address = Web3.to_checksum_address(wallet_address)

            # Try multiple Polymarket rewards API endpoints
            endpoints = [
                f"https://gamma-api.polymarket.com/rewards?address={wallet_address}",
                f"https://polymarket.com/api/rewards/{wallet_address}",
                f"https://clob.polymarket.com/rewards/{wallet_address}",
            ]

            for api_url in endpoints:
                try:
                    async with self.session.get(api_url, timeout=10) as response:
                        if response.status == 200:
                            data = await response.json()

                            # Parse reward data (structure may vary)
                            # Try different possible field names
                            unclaimed = (
                                data.get('unclaimed_rewards') or
                                data.get('unclaimedRewards') or
                                data.get('unclaimed') or
                                data.get('pending_rewards') or
                                data.get('pendingRewards') or
                                data.get('available') or
                                0
                            )

                            if unclaimed > 0:
                                logger.info(f"✅ API rewards for {wallet_address[:10]}...: ${unclaimed:.2f}")
                                return float(unclaimed)
                            else:
                                logger.debug(f"No unclaimed rewards for {wallet_address[:10]}...")
                                return 0.0
                        else:
                            logger.debug(f"Rewards API {api_url} returned status {response.status}")

                except Exception as e:
                    logger.debug(f"Could not fetch from {api_url}: {e}")
                    continue

            # All endpoints failed
            logger.warning(f"⚠️  Could not fetch rewards from any API endpoint for {wallet_address[:10]}...")
            logger.warning(f"   This is normal if Polymarket doesn't have a public rewards API")
            logger.warning(f"   Rewards will be set to $0 (will NOT withdraw wallet balance)")
            return 0.0

        except Exception as e:
            logger.debug(f"Could not fetch rewards from API: {e}")
            return 0.0
    
    async def withdraw_rewards(self, wallet: Dict, amount: float = None) -> Tuple[bool, str]:
        """
        Withdraw rewards from a wallet to the configured withdrawal address
        
        Args:
            wallet: Wallet dictionary with 'address' and 'private_key'
            amount: Amount to withdraw (None = withdraw all available)
        
        Returns:
            Tuple of (success: bool, transaction_hash or error_message: str)
        """
        try:
            if not self.withdrawal_wallet:
                error_msg = "No withdrawal wallet configured"
                logger.error(f"❌ {error_msg}")
                return False, error_msg
            
            # Validate withdrawal wallet
            try:
                if not Web3.is_address(self.withdrawal_wallet):
                    error_msg = f"Invalid withdrawal wallet address: {self.withdrawal_wallet}"
                    logger.error(f"❌ {error_msg}")
                    return False, error_msg

                source_address = wallet['address']
                if not Web3.is_checksum_address(source_address):
                    source_address = Web3.to_checksum_address(source_address)

                target_address = self.withdrawal_wallet
                if not Web3.is_checksum_address(target_address):
                    target_address = Web3.to_checksum_address(target_address)
            except Exception as e:
                error_msg = f"Address validation error: {str(e)}"
                logger.error(f"❌ {error_msg}")
                return False, error_msg
            
            # Get current balance
            usdc_contract = self.w3.eth.contract(address=self.usdc_address, abi=self.usdc_abi)
            balance_raw = usdc_contract.functions.balanceOf(source_address).call()
            balance_usdc = balance_raw / 1e6
            
            # Determine withdrawal amount
            if amount is None:
                # Withdraw all available (minus a small buffer for gas)
                withdrawal_amount = balance_usdc
            else:
                withdrawal_amount = min(amount, balance_usdc)
            
            # Check minimum threshold
            if withdrawal_amount < self.min_withdrawal_threshold:
                msg = f"Amount ${withdrawal_amount:.2f} below threshold ${self.min_withdrawal_threshold:.2f}"
                logger.info(f"⏭️  {msg}")
                return False, msg
            
            logger.info(f"💸 Withdrawing ${withdrawal_amount:.2f} USDC from {source_address[:10]}... to {target_address[:10]}...")
            
            # Prepare transaction
            withdrawal_amount_raw = int(withdrawal_amount * 1e6)  # Convert to USDC decimals
            
            # Get account from private key
            account = Account.from_key(wallet['private_key'])
            
            # Build transaction
            nonce = self.w3.eth.get_transaction_count(source_address)
            
            # Estimate gas
            gas_estimate = usdc_contract.functions.transfer(
                target_address,
                withdrawal_amount_raw
            ).estimate_gas({'from': source_address})
            
            # Get gas price
            gas_price = self.w3.eth.gas_price
            max_gas_price = int(os.getenv('MAX_GAS_PRICE', 500)) * 1e9  # Convert Gwei to Wei
            
            if gas_price > max_gas_price:
                logger.warning(f"⚠️  Gas price {gas_price/1e9:.2f} Gwei exceeds max {max_gas_price/1e9:.2f} Gwei")
                gas_price = max_gas_price
            
            # Build transaction
            transaction = usdc_contract.functions.transfer(
                target_address,
                withdrawal_amount_raw
            ).build_transaction({
                'from': source_address,
                'gas': int(gas_estimate * 1.2),  # Add 20% buffer
                'gasPrice': gas_price,
                'nonce': nonce,
                'chainId': 137  # Polygon mainnet
            })
            
            # Sign transaction
            signed_txn = account.sign_transaction(transaction)

            # Send transaction (handle both old and new Web3.py versions)
            try:
                # Try new version first (raw_transaction)
                raw_tx = signed_txn.raw_transaction
            except AttributeError:
                # Fallback to old version (rawTransaction)
                raw_tx = signed_txn.rawTransaction

            tx_hash = self.w3.eth.send_raw_transaction(raw_tx)
            tx_hash_hex = tx_hash.hex()
            
            logger.info(f"📤 Transaction sent: {tx_hash_hex}")
            
            # Wait for confirmation
            logger.info("⏳ Waiting for confirmation...")
            receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash, timeout=120)
            
            if receipt['status'] == 1:
                logger.info(f"✅ Withdrawal successful! TX: {tx_hash_hex}")
                logger.info(f"   Amount: ${withdrawal_amount:.2f} USDC")
                logger.info(f"   Gas used: {receipt['gasUsed']}")
                
                # Update statistics
                self.stats['total_withdrawals'] += 1
                self.stats['total_withdrawn_amount'] += withdrawal_amount
                self.stats['last_withdrawal_time'] = time.time()
                
                return True, tx_hash_hex
            else:
                error_msg = f"Transaction failed: {tx_hash_hex}"
                logger.error(f"❌ {error_msg}")
                self.stats['failed_withdrawals'] += 1
                return False, error_msg
                
        except Exception as e:
            error_msg = f"Withdrawal error: {str(e)}"
            logger.error(f"❌ {error_msg}")
            self.stats['failed_withdrawals'] += 1
            return False, error_msg
    
    async def auto_withdraw_loop(self, wallets: List[Dict]):
        """
        Main loop for automatic reward checking and withdrawal
        
        Args:
            wallets: List of wallet dictionaries
        """
        logger.info("🔄 Starting automatic reward withdrawal loop")
        
        while True:
            try:
                logger.info("🔍 Checking rewards...")
                
                # Check rewards for all wallets
                rewards = await self.check_rewards(wallets)
                
                # Process each wallet
                for wallet in wallets:
                    address = wallet['address']
                    reward_amount = rewards.get(address, 0.0)
                    
                    # Check if withdrawal threshold is met
                    if reward_amount >= self.min_withdrawal_threshold:
                        logger.info(f"💰 Wallet {address[:10]}... has ${reward_amount:.2f} - initiating withdrawal")
                        
                        success, result = await self.withdraw_rewards(wallet, reward_amount)
                        
                        if success:
                            logger.info(f"✅ Successfully withdrew ${reward_amount:.2f} from {address[:10]}...")
                        else:
                            logger.warning(f"⚠️  Withdrawal failed for {address[:10]}...: {result}")
                        
                        # Add delay between withdrawals to avoid rate limiting
                        await asyncio.sleep(5)
                    else:
                        logger.debug(f"Wallet {address[:10]}... has ${reward_amount:.2f} (below threshold)")
                
                # Log statistics
                self._log_statistics()
                
                # Wait for next check interval
                logger.info(f"⏰ Next reward check in {self.check_interval}s ({self.check_interval/3600:.1f}h)")
                await asyncio.sleep(self.check_interval)
                
            except Exception as e:
                logger.error(f"Error in auto-withdraw loop: {e}")
                self.stats['check_errors'] += 1
                # Wait a bit before retrying
                await asyncio.sleep(60)
    
    def _log_statistics(self):
        """Log reward manager statistics"""
        logger.info("📊 Reward Manager Statistics:")
        logger.info(f"   Total checks: {self.stats['total_rewards_checked']}")
        logger.info(f"   Total withdrawals: {self.stats['total_withdrawals']}")
        logger.info(f"   Total withdrawn: ${self.stats['total_withdrawn_amount']:.2f} USDC")
        logger.info(f"   Failed withdrawals: {self.stats['failed_withdrawals']}")
        logger.info(f"   Check errors: {self.stats['check_errors']}")
        
        if self.stats['last_withdrawal_time'] > 0:
            last_withdrawal = datetime.fromtimestamp(self.stats['last_withdrawal_time'])
            logger.info(f"   Last withdrawal: {last_withdrawal.strftime('%Y-%m-%d %H:%M:%S')}")
    
    def get_statistics(self) -> Dict:
        """
        Get reward manager statistics
        
        Returns:
            Dictionary with statistics
        """
        return self.stats.copy()

