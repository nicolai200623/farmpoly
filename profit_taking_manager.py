"""
Profit Taking Manager
Automatically close profitable positions to lock in gains
"""

import asyncio
import logging
import time
import requests
from typing import Dict, List, Optional
from datetime import datetime
from py_clob_client.client import ClobClient
from py_clob_client.clob_types import OrderArgs, OrderType
from py_clob_client.constants import POLYGON
from py_clob_client.order_builder.constants import BUY, SELL
import os
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)


class ProfitTakingManager:
    """Monitor filled positions and automatically close profitable ones"""
    
    def __init__(self, config: dict, telegram_notifier=None):
        self.config = config.get('profit_taking', {})
        self.telegram = telegram_notifier
        
        # Configuration
        self.enabled = self.config.get('enabled', True)
        self.check_interval = self.config.get('check_interval', 300)  # 5 minutes
        self.min_profit_pct = self.config.get('min_profit_percentage', 50)
        self.target_profit_pct = self.config.get('target_profit_percentage', 80)
        self.max_profit_pct = self.config.get('max_profit_percentage', 150)
        self.never_close_losing = self.config.get('never_close_losing_positions', True)
        self.min_hold_time = self.config.get('min_hold_time', 300)  # 5 minutes
        self.alert_on_close = self.config.get('alert_on_profit_close', True)
        
        # Initialize CLOB client
        self.client = self._initialize_client()
        
        # Tracking
        self.closed_positions = {}
        self.last_check_time = 0
        
        logger.info("✅ Profit Taking Manager initialized")
        logger.info(f"   - Min profit: {self.min_profit_pct}%")
        logger.info(f"   - Target profit: {self.target_profit_pct}%")
        logger.info(f"   - Max profit: {self.max_profit_pct}%")
        logger.info(f"   - Check interval: {self.check_interval}s")
    
    def _initialize_client(self) -> ClobClient:
        """Initialize CLOB client for placing sell orders"""
        try:
            # Try WALLET_1_PK first, then fall back to PRIVATE_KEY
            private_key = os.getenv('WALLET_1_PK') or os.getenv('PRIVATE_KEY')
            if not private_key:
                raise ValueError("WALLET_1_PK or PRIVATE_KEY not found in .env")

            # Remove 0x prefix if present
            if private_key.startswith('0x'):
                private_key = private_key[2:]
            
            host = "https://clob.polymarket.com"
            chain_id = POLYGON
            
            client = ClobClient(
                host,
                key=private_key,
                chain_id=chain_id,
                signature_type=2,
                funder=None
            )
            
            # Create API credentials
            try:
                client.create_or_derive_api_creds()
                logger.info("✅ CLOB client initialized with API credentials")
            except Exception as e:
                logger.warning(f"⚠️  API credentials may already exist: {e}")
            
            return client
            
        except Exception as e:
            logger.error(f"❌ Failed to initialize CLOB client: {e}")
            return None
    
    async def check_and_close_positions(self):
        """Main loop: Check positions and close profitable ones"""
        if not self.enabled:
            logger.info("Profit taking disabled in config")
            return
        
        if not self.client:
            logger.error("CLOB client not initialized, cannot close positions")
            return
        
        try:
            # Get wallet address
            wallet_address = os.getenv('WALLET_ADDRESS')
            if not wallet_address:
                logger.error("WALLET_ADDRESS not found in .env")
                return
            
            logger.info(f"🔍 Checking positions for wallet: {wallet_address[:10]}...{wallet_address[-8:]}")
            
            # Fetch positions from Polymarket Data API
            positions = await self._fetch_positions(wallet_address)
            
            if not positions:
                logger.info("✅ No active positions to check")
                return
            
            logger.info(f"📊 Found {len(positions)} active positions")
            
            # Check each position
            for position in positions:
                await self._process_position(position)
            
            self.last_check_time = time.time()
            
        except Exception as e:
            logger.error(f"❌ Error checking positions: {e}")
    
    async def _fetch_positions(self, wallet_address: str) -> List[Dict]:
        """Fetch positions from Polymarket Data API"""
        try:
            data_api_url = "https://data-api.polymarket.com/positions"
            params = {
                "user": wallet_address,
                "sizeThreshold": 0.01,
                "limit": 500
            }
            
            response = requests.get(data_api_url, params=params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            # Filter out positions we've already closed
            active_positions = []
            for pos in data:
                token_id = pos.get('asset_id')
                if token_id not in self.closed_positions:
                    active_positions.append(pos)
            
            return active_positions
            
        except Exception as e:
            logger.error(f"❌ Failed to fetch positions: {e}")
            return []
    
    async def _process_position(self, position: Dict):
        """Process a single position and decide if it should be closed"""
        try:
            # Debug: Log raw position data
            logger.debug(f"Raw position data: {position}")

            market = position.get('title', 'Unknown')  # Changed from 'market' to 'title'
            token_id = position.get('asset')  # Changed from 'asset_id' to 'asset'
            shares = float(position.get('size', 0))
            avg_price = float(position.get('avgPrice', 0))  # Changed from 'average_entry_price' to 'avgPrice'
            current_price = float(position.get('curPrice', 0))  # Changed from 'current_price' to 'curPrice'

            # Debug: Log extracted values
            logger.debug(f"Extracted - shares: {shares}, avg_price: {avg_price}, current_price: {current_price}")

            if shares <= 0 or avg_price <= 0 or current_price <= 0:
                logger.warning(f"⚠️  Skipping position {market[:30]} - invalid data (shares={shares}, avg={avg_price}, current={current_price})")
                return
            
            # Calculate P&L
            total_cost = shares * avg_price
            current_value = shares * current_price
            pnl = current_value - total_cost
            pnl_pct = (pnl / total_cost * 100) if total_cost > 0 else 0
            
            logger.info(f"\n📈 Position: {market[:50]}")
            logger.info(f"   Shares: {shares:.2f} @ ${avg_price:.4f}")
            logger.info(f"   Current: ${current_price:.4f}")
            logger.info(f"   P&L: ${pnl:.2f} ({pnl_pct:+.2f}%)")
            
            # Check if losing position
            if pnl_pct < 0:
                if self.never_close_losing:
                    logger.info(f"   ⏸️  Losing position - NOT closing (manual decision required)")
                    return
            
            # Check profit thresholds
            should_close = False
            close_reason = ""
            
            if pnl_pct >= self.max_profit_pct:
                should_close = True
                close_reason = f"max_profit_reached ({pnl_pct:.2f}% >= {self.max_profit_pct}%)"
            elif pnl_pct >= self.target_profit_pct:
                should_close = True
                close_reason = f"target_profit_reached ({pnl_pct:.2f}% >= {self.target_profit_pct}%)"
            elif pnl_pct >= self.min_profit_pct:
                logger.info(f"   💰 Profitable ({pnl_pct:.2f}%), waiting for target ({self.target_profit_pct}%)")
                return
            else:
                logger.info(f"   ⏳ Not profitable enough ({pnl_pct:.2f}% < {self.min_profit_pct}%)")
                return
            
            # Close the position
            if should_close:
                logger.info(f"   🎯 CLOSING: {close_reason}")
                await self._close_position(position, close_reason, pnl, pnl_pct)
            
        except Exception as e:
            logger.error(f"❌ Error processing position: {e}")
    
    async def _close_position(self, position: Dict, reason: str, pnl: float, pnl_pct: float):
        """Close a position by placing a sell order"""
        try:
            market = position.get('title', 'Unknown')  # Changed from 'market' to 'title'
            token_id = position.get('asset')  # Changed from 'asset_id' to 'asset'
            shares = float(position.get('size', 0))
            current_price = float(position.get('curPrice', 0))  # Changed from 'current_price' to 'curPrice'
            
            logger.info(f"\n🔄 Placing SELL order for {market[:50]}")
            logger.info(f"   Token ID: {token_id}")
            logger.info(f"   Shares: {shares:.2f}")
            logger.info(f"   Price: ${current_price:.4f}")

            # Place sell order slightly below current price to ensure fill
            sell_price = current_price * 0.99  # 1% below to ensure quick fill

            # Create a NEW signing client for this order (same approach as order_manager.py)
            # This ensures fresh API credentials and proper signature
            try:
                # Get private key
                private_key = os.getenv('WALLET_1_PK') or os.getenv('PRIVATE_KEY')
                if not private_key:
                    raise ValueError("WALLET_1_PK or PRIVATE_KEY not found in .env")

                # Remove 0x prefix if present
                if private_key.startswith('0x'):
                    private_key = private_key[2:]

                # Create fresh signing client
                logger.debug("Creating fresh signing client for SELL order...")
                signing_client = ClobClient(
                    host="https://clob.polymarket.com",
                    key=private_key,
                    chain_id=POLYGON,
                    signature_type=2,
                    funder=None
                )

                # Set API credentials (required for L2 auth)
                logger.debug("Setting API credentials...")
                signing_client.set_api_creds(signing_client.create_or_derive_api_creds())
                logger.debug("✅ API credentials set successfully for SELL order")

            except Exception as e:
                logger.error(f"❌ Failed to create signing client: {e}")
                raise

            order_args = OrderArgs(
                token_id=token_id,
                price=sell_price,
                size=shares,
                side=SELL
            )

            # Create, sign, and post order using the fresh signing client
            logger.debug("Creating and signing SELL order...")
            signed_order = signing_client.create_order(order_args)
            logger.debug("Posting SELL order to CLOB...")
            resp = signing_client.post_order(signed_order, OrderType.GTC)
            
            if resp and resp.get('success'):
                order_id = resp.get('orderID', 'unknown')
                logger.info(f"✅ SELL order placed successfully!")
                logger.info(f"   Order ID: {order_id}")
                logger.info(f"   Expected proceeds: ${shares * sell_price:.2f}")
                logger.info(f"   Profit: ${pnl:.2f} ({pnl_pct:+.2f}%)")
                
                # Track closed position
                self.closed_positions[token_id] = {
                    'market': market,
                    'closed_at': time.time(),
                    'reason': reason,
                    'pnl': pnl,
                    'pnl_pct': pnl_pct,
                    'order_id': order_id
                }
                
                # Send alert
                if self.alert_on_close and self.telegram:
                    await self._send_close_alert(market, shares, pnl, pnl_pct, reason)
            else:
                error_msg = resp.get('error', 'Unknown error') if resp else 'No response'
                logger.error(f"❌ Failed to place SELL order: {error_msg}")
            
        except Exception as e:
            logger.error(f"❌ Error closing position: {e}")
    
    async def _send_close_alert(self, market: str, shares: float, pnl: float, pnl_pct: float, reason: str):
        """Send Telegram alert for closed position"""
        try:
            message = f"""
🎯 **POSITION CLOSED - PROFIT TAKEN**

📊 Market: {market[:50]}
💰 Shares: {shares:.2f}
📈 Profit: ${pnl:.2f} ({pnl_pct:+.2f}%)
🎯 Reason: {reason}

✅ Position successfully closed!
"""
            await self.telegram.send_message(message)
            
        except Exception as e:
            logger.error(f"Failed to send close alert: {e}")
    
    def get_stats(self) -> Dict:
        """Get profit taking statistics"""
        total_closed = len(self.closed_positions)
        total_profit = sum(p['pnl'] for p in self.closed_positions.values())
        
        return {
            'enabled': self.enabled,
            'total_closed': total_closed,
            'total_profit': total_profit,
            'last_check': datetime.fromtimestamp(self.last_check_time).isoformat() if self.last_check_time > 0 else 'Never',
            'min_profit_pct': self.min_profit_pct,
            'target_profit_pct': self.target_profit_pct,
            'max_profit_pct': self.max_profit_pct
        }

