#!/usr/bin/env python3
"""
Polymarket Competitive Trading Bot
Main orchestration module for 8 specialized trading components
"""

import asyncio
import logging
import yaml
import signal
import sys
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
import random
import time

# Setup logging FIRST before any imports that use logger
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Core modules
try:
    # Try new V2 scanner first (with Playwright + API)
    from market_scanner_v2 import MarketScannerV2 as MarketScanner
    logger.info("✅ Using MarketScannerV2 (Playwright + Gamma API)")
except ImportError:
    # Fallback to old scanner
    from market_scanner import MarketScanner
    logger.warning("⚠️  Using legacy MarketScanner (Selenium)")

from market_selector import MarketSelectorAI
from order_manager import OrderManager
from position_monitor import PositionMonitor
from risk_manager import RiskManager
from wallet_manager import WalletManager
from ml_predictor import MLPredictor
from optimizer import DailyOptimizer
from usdc_approver import USDCApprover
from reward_manager import RewardManager


class PolymarketBot:
    """Main bot orchestrator for Polymarket trading"""
    
    def __init__(self, config_path: str = 'config.yaml'):
        """Initialize bot with configuration"""
        self.config = self._load_config(config_path)
        self.running = False
        self.modules = {}
        self.performance_stats = {
            'daily_pnl': 0,
            'total_fills': 0,
            'successful_trades': 0,
            'cancelled_orders': 0
        }
        
        # Initialize modules
        self._initialize_modules()
        
    def _load_config(self, path: str) -> dict:
        """Load configuration from YAML file"""
        try:
            with open(path, 'r') as f:
                return yaml.safe_load(f)
        except Exception as e:
            logger.error(f"Failed to load config: {e}")
            return self._default_config()
    
    def _default_config(self) -> dict:
        """Return default configuration"""
        return {
            'market_scanner': {
                'interval': 5,  # seconds
                'min_reward': 300,
                'max_competition_bars': 2,
                'min_shares': 500
            },
            'order_management': {
                'spread_min': 0.008,  # 0.8 cents
                'spread_max': 0.015,  # 1.5 cents
                'size_min': 200,
                'size_max': 500
            },
            'risk_management': {
                'max_capital_per_market': 0.05,  # 5%
                'enable_hedging': True
            },
            'wallet_management': {
                'num_wallets': 5,
                'jitter_percentage': 0.2  # 20%
            },
            'ml_prediction': {
                'fill_risk_threshold': 0.8,
                'model_update_interval': 3600  # seconds
            },
            'monitoring': {
                'websocket_interval': 10,
                'partial_fill_threshold': 0.1,
                'volume_spike_multiplier': 2,
                'price_move_threshold': 0.02
            }
        }
    
    def _initialize_modules(self):
        """Initialize all trading modules"""
        try:
            self.modules['scanner'] = MarketScanner(self.config['market_scanner'])
            self.modules['selector'] = MarketSelectorAI(self.config)
            self.modules['order_mgr'] = OrderManager(self.config['order_management'])
            self.modules['monitor'] = PositionMonitor(self.config['monitoring'])
            self.modules['risk_mgr'] = RiskManager(self.config['risk_management'])
            self.modules['wallet_mgr'] = WalletManager(self.config['wallet_management'])
            self.modules['ml_predictor'] = MLPredictor(self.config['ml_prediction'])
            self.modules['optimizer'] = DailyOptimizer(self.config)

            # Initialize reward manager if enabled
            reward_config = self.config.get('reward_management', {})
            if reward_config.get('enabled', True):
                self.modules['reward_mgr'] = RewardManager(self.config)
                logger.info("✅ Reward Manager enabled")
            else:
                logger.info("⏭️  Reward Manager disabled in config")

            logger.info("All modules initialized successfully")
        except Exception as e:
            logger.error(f"Module initialization failed: {e}")
            raise
    
    async def start(self):
        """Start the trading bot"""
        self.running = True
        logger.info("🚀 Starting Polymarket Trading Bot...")

        # Check USDC approval before starting
        await self._check_usdc_approval()

        # Setup signal handlers
        signal.signal(signal.SIGINT, self._shutdown_handler)
        signal.signal(signal.SIGTERM, self._shutdown_handler)

        # Start all async tasks
        tasks = [
            self._market_scanning_loop(),
            self._order_management_loop(),
            self._position_monitoring_loop(),
            self._risk_management_loop(),
            self._ml_training_loop(),
            self._daily_optimization_loop()
        ]

        # Add reward management loop if enabled
        if 'reward_mgr' in self.modules:
            tasks.append(self._reward_management_loop())

        try:
            await asyncio.gather(*tasks)
        except Exception as e:
            logger.error(f"Bot error: {e}")
            await self.shutdown()

    async def _check_usdc_approval(self):
        """Check if wallets have USDC approval"""
        try:
            logger.info("🔍 Checking USDC approval for wallets...")

            approver = USDCApprover(self.config)
            wallet_mgr = self.modules['wallet_mgr']

            # Check first wallet as sample
            if wallet_mgr.wallets:
                first_wallet = wallet_mgr.wallets[0]
                allowance = await approver._get_allowance(first_wallet['address'])

                if allowance < 1000 * 1e6:  # Less than 1000 USDC approved
                    logger.warning("⚠️  USDC approval needed!")
                    logger.warning("   Run: python scripts/approve_wallets.py")
                    logger.warning("   Or the bot may fail to place orders")
                else:
                    logger.info(f"✅ USDC approval OK ({allowance/1e6:,.0f} USDC)")

        except Exception as e:
            logger.warning(f"⚠️  Could not check USDC approval: {e}")
            logger.warning("   Make sure to run: python scripts/approve_wallets.py")
    
    async def _market_scanning_loop(self):
        """Continuous market scanning"""
        scanner = self.modules['scanner']
        selector = self.modules['selector']
        
        while self.running:
            try:
                # Scan for opportunities
                markets = await scanner.scan_rewards_page()
                
                # Filter and score markets
                selected_markets = await selector.select_markets(markets)
                
                # Process selected markets
                for market in selected_markets:
                    await self._process_market_opportunity(market)
                
                # Add human-like delay with jitter
                await self._jittered_sleep(self.config['market_scanner']['interval'])
                
            except Exception as e:
                logger.error(f"Market scanning error: {e}")
                await asyncio.sleep(10)
    
    async def _order_management_loop(self):
        """Manage order placement and updates"""
        order_mgr = self.modules['order_mgr']
        wallet_mgr = self.modules['wallet_mgr']
        
        while self.running:
            try:
                # Get active wallet
                wallet = await wallet_mgr.get_next_wallet()
                
                # Check pending orders
                pending_orders = await order_mgr.get_pending_orders()
                
                for order in pending_orders:
                    # Apply ML prediction
                    fill_probability = await self.modules['ml_predictor'].predict_fill(order)
                    
                    if fill_probability < self.config['ml_prediction']['fill_risk_threshold']:
                        # Place or update order
                        await order_mgr.place_order(order, wallet)
                    else:
                        # Cancel high-risk order
                        await order_mgr.cancel_order(order['id'])
                        self.performance_stats['cancelled_orders'] += 1
                
                await asyncio.sleep(1)
                
            except Exception as e:
                logger.error(f"Order management error: {e}")
                await asyncio.sleep(5)
    
    async def _position_monitoring_loop(self):
        """Monitor open positions and market conditions"""
        monitor = self.modules['monitor']
        order_mgr = self.modules['order_mgr']
        
        while self.running:
            try:
                # Get all open positions
                positions = await monitor.get_open_positions()
                
                for position in positions:
                    # Check cancellation conditions
                    should_cancel = await monitor.check_cancel_conditions(position)
                    
                    if should_cancel:
                        await order_mgr.cancel_order(position['order_id'])
                        logger.info(f"Cancelled order {position['order_id']} due to market conditions")
                        self.performance_stats['cancelled_orders'] += 1
                
                # WebSocket interval
                await asyncio.sleep(self.config['monitoring']['websocket_interval'])
                
            except Exception as e:
                logger.error(f"Position monitoring error: {e}")
                await asyncio.sleep(10)
    
    async def _risk_management_loop(self):
        """Continuous risk monitoring and hedging"""
        risk_mgr = self.modules['risk_mgr']
        
        while self.running:
            try:
                # Check portfolio risk
                risk_metrics = await risk_mgr.calculate_portfolio_risk()
                
                # Apply hedging if needed
                if risk_metrics['needs_hedging']:
                    await risk_mgr.apply_hedging(risk_metrics['positions'])
                
                # Check capital allocation
                await risk_mgr.rebalance_capital()
                
                await asyncio.sleep(30)  # Check every 30 seconds
                
            except Exception as e:
                logger.error(f"Risk management error: {e}")
                await asyncio.sleep(10)
    
    async def _ml_training_loop(self):
        """Periodic ML model training"""
        ml_predictor = self.modules['ml_predictor']
        
        while self.running:
            try:
                # Train model on recent data
                await ml_predictor.train_model()
                logger.info("ML model updated successfully")
                
                # Wait for next training interval
                await asyncio.sleep(self.config['ml_prediction']['model_update_interval'])
                
            except Exception as e:
                logger.error(f"ML training error: {e}")
                await asyncio.sleep(3600)  # Retry in 1 hour
    
    async def _daily_optimization_loop(self):
        """Daily strategy optimization at UTC 00:00"""
        optimizer = self.modules['optimizer']

        while self.running:
            try:
                # Calculate time until next UTC midnight
                now = datetime.utcnow()
                next_midnight = (now + timedelta(days=1)).replace(
                    hour=0, minute=0, second=0, microsecond=0
                )
                seconds_until_midnight = (next_midnight - now).total_seconds()

                # Wait until midnight
                await asyncio.sleep(seconds_until_midnight)

                # Run daily optimization
                await optimizer.optimize_daily_strategy()

                # Update performance stats
                self.performance_stats['daily_pnl'] = await optimizer.calculate_daily_pnl()

                # Send performance report
                await self._send_performance_report()

            except Exception as e:
                logger.error(f"Daily optimization error: {e}")
                await asyncio.sleep(3600)

    async def _reward_management_loop(self):
        """Automated reward checking and withdrawal loop"""
        reward_mgr = self.modules['reward_mgr']
        wallet_mgr = self.modules['wallet_mgr']

        # Initialize reward manager async resources
        try:
            await reward_mgr.initialize()
        except Exception as e:
            logger.error(f"Failed to initialize reward manager: {e}")
            return

        logger.info("🎁 Starting automated reward management loop")

        while self.running:
            try:
                # Get all wallets
                wallets = wallet_mgr.wallets

                if not wallets:
                    logger.warning("No wallets available for reward checking")
                    await asyncio.sleep(300)  # Wait 5 minutes and retry
                    continue

                # Run the auto-withdraw loop (it handles its own timing)
                await reward_mgr.auto_withdraw_loop(wallets)

            except Exception as e:
                logger.error(f"Reward management error: {e}")
                await asyncio.sleep(300)  # Wait 5 minutes before retry
    
    async def _process_market_opportunity(self, market: dict):
        """Process a selected market opportunity"""
        try:
            # Check risk limits
            if not await self.modules['risk_mgr'].check_market_limit(market):
                logger.info(f"Skipping market {market['id']} due to risk limits")
                return
            
            # Prepare order with dynamic spread
            order = await self.modules['order_mgr'].prepare_market_order(market)
            
            # Add to pending orders
            await self.modules['order_mgr'].add_pending_order(order)
            
            logger.info(f"Added market {market['id']} to pending orders")
            
        except Exception as e:
            logger.error(f"Error processing market {market['id']}: {e}")
    
    async def _jittered_sleep(self, base_seconds: float):
        """Sleep with random jitter to appear more human-like"""
        jitter = random.uniform(-0.2, 0.2) * base_seconds
        await asyncio.sleep(base_seconds + jitter)
    
    async def _send_performance_report(self):
        """Send daily performance report via alerts"""
        try:
            report = f"""
            📊 Daily Performance Report
            ═══════════════════════════
            💰 Daily P&L: ${self.performance_stats['daily_pnl']:.2f}
            ✅ Successful Trades: {self.performance_stats['successful_trades']}
            📝 Total Fills: {self.performance_stats['total_fills']}
            ❌ Cancelled Orders: {self.performance_stats['cancelled_orders']}
            ═══════════════════════════
            """
            
            # Send via configured alert channels
            await self.modules['ml_predictor'].send_alert(report)
            
        except Exception as e:
            logger.error(f"Failed to send performance report: {e}")
    
    def _shutdown_handler(self, signum, frame):
        """Handle shutdown signals"""
        logger.info("Shutdown signal received")
        asyncio.create_task(self.shutdown())
    
    async def shutdown(self):
        """Graceful shutdown"""
        logger.info("Shutting down bot...")
        self.running = False

        # Cancel all open orders
        try:
            await self.modules['order_mgr'].cancel_all_orders()
        except:
            pass

        # Log final reward statistics if reward manager is active
        if 'reward_mgr' in self.modules:
            try:
                stats = self.modules['reward_mgr'].get_statistics()
                logger.info("📊 Final Reward Manager Statistics:")
                logger.info(f"   Total withdrawals: {stats['total_withdrawals']}")
                logger.info(f"   Total withdrawn: ${stats['total_withdrawn_amount']:.2f} USDC")
            except:
                pass

        # Close all connections
        for module in self.modules.values():
            if hasattr(module, 'close'):
                await module.close()

        logger.info("Bot shutdown complete")


async def main():
    """Main entry point"""
    bot = PolymarketBot('config.yaml')
    await bot.start()


if __name__ == "__main__":
    asyncio.run(main())