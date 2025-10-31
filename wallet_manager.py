"""
Wallet Manager Module
Manages multiple wallets with rotation and jitter
"""

import logging
import random
import time
from typing import List, Dict, Optional
from eth_account import Account
import asyncio
from web3 import Web3

logger = logging.getLogger(__name__)


class WalletManager:
    """Manages wallet rotation and human-like behavior"""
    
    def __init__(self, config: dict):
        self.config = config
        self.wallets = []
        self.current_wallet_index = 0
        self.wallet_usage = {}
        self.last_wallet_switch = time.time()
        self.w3 = Web3(Web3.HTTPProvider('https://polygon-rpc.com'))
        self._initialize_wallets()
    
    def _initialize_wallets(self):
        """Initialize wallet pool from environment variables"""
        import os
        from dotenv import load_dotenv

        # Load environment variables
        load_dotenv()

        # Try to load real wallets from .env
        use_demo = os.getenv('USE_DEMO_WALLETS', 'false').lower() == 'true'

        if use_demo:
            logger.warning("⚠️  Using DEMO wallets - NOT for real trading!")
            self._load_demo_wallets()
        else:
            logger.info("Loading REAL wallets from .env")
            self._load_real_wallets()

    def _load_real_wallets(self):
        """Load real wallets from environment variables"""
        import os

        loaded_count = 0
        max_wallets = self.config.get('num_wallets', 10)

        for i in range(1, max_wallets + 1):
            priv_key = os.getenv(f'WALLET_{i}_PK')

            if not priv_key:
                continue

            try:
                # Validate and load wallet
                if not priv_key.startswith('0x'):
                    priv_key = '0x' + priv_key

                account = Account.from_key(priv_key)

                wallet = {
                    'index': i - 1,
                    'address': account.address,
                    'private_key': priv_key,
                    'usage_count': 0,
                    'last_used': 0,
                    'total_volume': 0,
                    'created_at': time.time()
                }

                self.wallets.append(wallet)
                self.wallet_usage[account.address] = {
                    'orders': 0,
                    'fills': 0,
                    'volume': 0
                }

                loaded_count += 1
                logger.info(f"✅ Loaded wallet {i}: {account.address[:10]}...{account.address[-8:]}")

            except Exception as e:
                logger.error(f"❌ Failed to load WALLET_{i}_PK: {e}")

        if loaded_count == 0:
            logger.error("❌ NO WALLETS LOADED! Check your .env file")
            logger.error("💡 Add WALLET_1_PK=0x... to .env or set USE_DEMO_WALLETS=true")
            raise ValueError("No wallets configured")

        logger.info(f"✅ Successfully loaded {loaded_count} real wallets")

    def _load_demo_wallets(self):
        """Load demo wallets (for testing only - NO REAL FUNDS)"""
        num_wallets = self.config.get('num_wallets', 5)

        for i in range(num_wallets):
            account = Account.create()
            wallet = {
                'index': i,
                'address': account.address,
                'private_key': account.key.hex(),
                'usage_count': 0,
                'last_used': 0,
                'total_volume': 0,
                'created_at': time.time()
            }
            self.wallets.append(wallet)
            self.wallet_usage[account.address] = {
                'orders': 0,
                'fills': 0,
                'volume': 0
            }

        logger.warning(f"⚠️  Initialized {num_wallets} DEMO wallets (NO REAL TRADING)")
    
    async def get_next_wallet(self) -> Dict:
        """Get next wallet with rotation and jitter"""
        try:
            # Apply jitter to wallet selection
            if random.random() < 0.2:  # 20% chance of random selection
                wallet = random.choice(self.wallets)
            else:
                # Round-robin with checks
                wallet = self._get_least_used_wallet()
            
            # Add human-like delay
            await self._apply_human_delay()
            
            # Update usage
            wallet['usage_count'] += 1
            wallet['last_used'] = time.time()
            
            # Log wallet switch if different
            if wallet['index'] != self.current_wallet_index:
                logger.info(f"Switched to wallet {wallet['index']}")
                self.current_wallet_index = wallet['index']
                self.last_wallet_switch = time.time()
            
            return wallet
            
        except Exception as e:
            logger.error(f"Error getting next wallet: {e}")
            return self.wallets[0]  # Fallback to first wallet
    
    def _get_least_used_wallet(self) -> Dict:
        """Get wallet with least recent usage"""
        # Sort by last used time (oldest first)
        sorted_wallets = sorted(self.wallets, key=lambda w: w['last_used'])
        
        # Check cooldown period (at least 30 seconds between uses)
        current_time = time.time()
        
        for wallet in sorted_wallets:
            if current_time - wallet['last_used'] >= 30:
                return wallet
        
        # If all on cooldown, return least used
        return sorted_wallets[0]
    
    async def _apply_human_delay(self):
        """Apply human-like delay patterns"""
        # Base delay
        base_delay = random.uniform(0.5, 2.0)
        
        # Time of day factor
        hour = time.localtime().tm_hour
        if 2 <= hour <= 6:  # Night time - slower
            base_delay *= random.uniform(1.5, 2.5)
        elif 9 <= hour <= 17:  # Business hours - normal
            base_delay *= random.uniform(0.8, 1.2)
        else:  # Evening - slightly slower
            base_delay *= random.uniform(1.0, 1.5)
        
        # Add micro-delays (typing/clicking simulation)
        micro_delays = random.randint(2, 5)
        for _ in range(micro_delays):
            await asyncio.sleep(random.uniform(0.05, 0.15))
        
        await asyncio.sleep(base_delay)
    
    def add_jitter_to_size(self, base_size: int) -> int:
        """Add human-like jitter to order size"""
        jitter_pct = self.config.get('jitter_percentage', 0.2)
        
        # Random variation
        jitter = random.uniform(-jitter_pct, jitter_pct)
        jittered_size = int(base_size * (1 + jitter))
        
        # Round to "human" numbers sometimes
        if random.random() < 0.3:  # 30% chance
            # Round to nearest 50 or 100
            if jittered_size > 100:
                jittered_size = round(jittered_size / 50) * 50
            else:
                jittered_size = round(jittered_size / 10) * 10
        
        return max(1, jittered_size)  # Ensure positive
    
    def add_jitter_to_price(self, base_price: float) -> float:
        """Add human-like jitter to price"""
        # Small random variation
        jitter = random.uniform(-0.001, 0.001)  # ±0.1 cent
        jittered_price = base_price + jitter
        
        # Sometimes round to cleaner numbers
        if random.random() < 0.4:  # 40% chance
            jittered_price = round(jittered_price, 3)  # Round to 0.1 cent
        
        return max(0.001, min(0.999, jittered_price))  # Keep in valid range
    
    async def check_wallet_balances(self) -> Dict:
        """Check balances for all wallets"""
        balances = {}
        
        for wallet in self.wallets:
            try:
                # Check MATIC balance
                matic_balance = self.w3.eth.get_balance(wallet['address'])
                matic_balance_eth = self.w3.from_wei(matic_balance, 'ether')
                
                # Would also check USDC balance on Polygon
                # For demo, using placeholder
                usdc_balance = 1000  # Placeholder
                
                balances[wallet['address']] = {
                    'matic': float(matic_balance_eth),
                    'usdc': usdc_balance,
                    'index': wallet['index']
                }
                
            except Exception as e:
                logger.error(f"Error checking wallet {wallet['index']}: {e}")
                balances[wallet['address']] = {'matic': 0, 'usdc': 0}
        
        return balances
    
    async def rotate_wallets(self):
        """Force wallet rotation"""
        self.current_wallet_index = (self.current_wallet_index + 1) % len(self.wallets)
        logger.info(f"Rotated to wallet {self.current_wallet_index}")
    
    def update_wallet_stats(self, wallet_address: str, stats: Dict):
        """Update wallet usage statistics"""
        if wallet_address in self.wallet_usage:
            usage = self.wallet_usage[wallet_address]
            usage['orders'] += stats.get('orders', 0)
            usage['fills'] += stats.get('fills', 0)
            usage['volume'] += stats.get('volume', 0)
    
    def get_wallet_distribution(self) -> Dict:
        """Get distribution statistics across wallets"""
        total_orders = sum(u['orders'] for u in self.wallet_usage.values())
        total_volume = sum(u['volume'] for u in self.wallet_usage.values())
        
        distribution = {
            'total_wallets': len(self.wallets),
            'active_wallets': sum(1 for w in self.wallets if w['usage_count'] > 0),
            'total_orders': total_orders,
            'total_volume': total_volume,
            'per_wallet': []
        }
        
        for wallet in self.wallets:
            usage = self.wallet_usage[wallet['address']]
            distribution['per_wallet'].append({
                'index': wallet['index'],
                'orders': usage['orders'],
                'volume': usage['volume'],
                'usage_percentage': (usage['orders'] / total_orders * 100) if total_orders > 0 else 0
            })
        
        return distribution
    
    def should_switch_wallet(self) -> bool:
        """Determine if wallet should be switched"""
        # Time-based switching
        time_since_switch = time.time() - self.last_wallet_switch
        
        # Random switching pattern
        if time_since_switch > 300:  # 5 minutes
            return random.random() < 0.7  # 70% chance
        elif time_since_switch > 180:  # 3 minutes
            return random.random() < 0.3  # 30% chance
        else:
            return random.random() < 0.1  # 10% chance
    
    async def simulate_human_behavior(self):
        """Simulate human-like behavior patterns"""
        # Random breaks
        if random.random() < 0.05:  # 5% chance
            break_duration = random.uniform(30, 180)  # 30s to 3min break
            logger.info(f"Taking a break for {break_duration:.0f} seconds")
            await asyncio.sleep(break_duration)
        
        # Typing speed variation
        if random.random() < 0.1:  # 10% chance of slow typing
            await asyncio.sleep(random.uniform(1, 3))
        
        # Mouse movement simulation (just delays)
        for _ in range(random.randint(1, 3)):
            await asyncio.sleep(random.uniform(0.1, 0.3))
    
    def get_wallet_by_index(self, index: int) -> Optional[Dict]:
        """Get specific wallet by index"""
        if 0 <= index < len(self.wallets):
            return self.wallets[index]
        return None
    
    def get_active_wallet(self) -> Dict:
        """Get currently active wallet"""
        return self.wallets[self.current_wallet_index]
    
    async def fund_wallets(self, funding_amount: float = 100):
        """Fund wallets with USDC (simulation)"""
        logger.info(f"Funding {len(self.wallets)} wallets with ${funding_amount} each")
        
        # In production, this would:
        # 1. Transfer USDC from main wallet
        # 2. Ensure MATIC for gas
        # 3. Use batched transactions
        
        for wallet in self.wallets:
            wallet['funded_amount'] = funding_amount
            logger.info(f"Funded wallet {wallet['index']}: {wallet['address']}")