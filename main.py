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
import os
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
from dotenv import load_dotenv
import random
import time

# Load environment variables FIRST
load_dotenv()

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
from monitoring_system import MonitoringSystem
from telegram_notifier import TelegramNotifier
from profit_taking_manager import ProfitTakingManager


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
        """Load configuration from YAML file and merge with .env"""
        try:
            logger.info(f"📂 Loading config from: {path}")
            with open(path, 'r', encoding='utf-8') as f:
                config = yaml.safe_load(f)

            # Log critical config values for debugging
            scanner_config = config.get('market_scanner', {})
            logger.info(f"✅ Config loaded successfully")
            logger.info(f"   - min_reward: {scanner_config.get('min_reward', 'NOT SET')}")
            logger.info(f"   - max_competition_bars: {scanner_config.get('max_competition_bars', 'NOT SET')}")
            logger.info(f"   - interval: {scanner_config.get('interval', 'NOT SET')}s")

            # Merge Telegram config from .env
            telegram_token = os.getenv('TELEGRAM_BOT_TOKEN', '')
            telegram_chat_id = os.getenv('TELEGRAM_CHAT_ID', '')

            if telegram_token and telegram_chat_id:
                # Ensure alerts section exists
                if 'alerts' not in config:
                    config['alerts'] = {}

                # Override with .env values
                config['alerts']['telegram_bot_token'] = telegram_token
                config['alerts']['telegram_chat_id'] = telegram_chat_id
                config['alerts']['telegram_enabled'] = True

                logger.info(f"✅ Telegram alerts configured (Chat ID: {telegram_chat_id})")
            else:
                logger.warning("⚠️  Telegram not configured in .env")

            # Merge webhook config from .env
            webhook_url = os.getenv('DISCORD_WEBHOOK_URL') or os.getenv('SLACK_WEBHOOK_URL', '')
            if webhook_url:
                if 'alerts' not in config:
                    config['alerts'] = {}
                config['alerts']['webhook_url'] = webhook_url
                config['alerts']['webhook_enabled'] = True
                logger.info("✅ Webhook alerts configured")

            return config
        except Exception as e:
            logger.error(f"❌ Failed to load config from {path}: {e}")
            logger.error(f"   Using default config instead")
            return self._default_config()
    
    def _default_config(self) -> dict:
        """Return default configuration - SHOULD MATCH config.yaml"""
        logger.warning("⚠️  Using DEFAULT config - config.yaml not found or failed to load!")
        return {
            'market_scanner': {
                'interval': 30,  # seconds - match config.yaml
                'min_reward': 100,  # FIXED: was 300, now matches config.yaml
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
            # Initialize Telegram Notifier FIRST
            self.modules['telegram'] = TelegramNotifier(self.config)
            logger.info("✅ Telegram Notifier initialized")

            self.modules['scanner'] = MarketScanner(self.config['market_scanner'])
            self.modules['selector'] = MarketSelectorAI(self.config)

            # Pass telegram notifier to OrderManager
            self.modules['order_mgr'] = OrderManager(
                self.config['order_management'],
                telegram_notifier=self.modules['telegram']
            )

            self.modules['monitor'] = PositionMonitor(self.config['monitoring'])
            self.modules['risk_mgr'] = RiskManager(self.config['risk_management'])
            self.modules['wallet_mgr'] = WalletManager(self.config['wallet_management'])

            # Initialize ML Predictor with alerts config
            ml_config = self.config.get('ml_prediction', {})
            alerts_config = self.config.get('alerts', {})

            # Merge alerts into ml_config for MLPredictor
            ml_config_with_alerts = {
                **ml_config,
                'telegram_bot_token': alerts_config.get('telegram_bot_token', ''),
                'telegram_chat_id': alerts_config.get('telegram_chat_id', ''),
                'alert_webhook': alerts_config.get('webhook_url', ''),
            }

            self.modules['ml_predictor'] = MLPredictor(ml_config_with_alerts)
            self.modules['optimizer'] = DailyOptimizer(self.config)

            # Initialize monitoring system
            self.modules['monitoring'] = MonitoringSystem(
                self.config,
                self.modules['ml_predictor']  # Pass ML predictor for sending alerts
            )
            logger.info("✅ Monitoring System enabled")

            # Initialize reward manager if enabled
            reward_config = self.config.get('reward_management', {})
            if reward_config.get('enabled', True):
                self.modules['reward_mgr'] = RewardManager(self.config)
                logger.info("✅ Reward Manager enabled")
            else:
                logger.info("⏭️  Reward Manager disabled in config")

            # Initialize profit taking manager if enabled
            profit_config = self.config.get('profit_taking', {})
            if profit_config.get('enabled', True):
                self.modules['profit_mgr'] = ProfitTakingManager(
                    self.config,
                    telegram_notifier=self.modules['telegram']
                )
                logger.info("✅ Profit Taking Manager enabled")
            else:
                logger.info("⏭️  Profit Taking Manager disabled in config")

            logger.info("All modules initialized successfully")
        except Exception as e:
            logger.error(f"Module initialization failed: {e}")
            raise
    
    async def start(self):
        """Start the trading bot"""
        self.running = True
        logger.info("🚀 Starting Polymarket Trading Bot...")

        # Send startup alert
        await self._send_startup_alert()

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
            self._daily_optimization_loop(),
            self._monitoring_loop(),  # Add monitoring loop
            self._hourly_report_loop()  # Add hourly report loop
        ]

        # Add reward management loop if enabled
        if 'reward_mgr' in self.modules:
            tasks.append(self._reward_management_loop())

        # Add profit taking loop if enabled
        if 'profit_mgr' in self.modules:
            tasks.append(self._profit_taking_loop())

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
                wallet_address = first_wallet['address']

                # Log which wallet we're checking
                logger.info(f"   Checking wallet: {wallet_address[:10]}...{wallet_address[-8:]}")

                allowance = await approver._get_allowance(wallet_address)

                # Log raw allowance value for debugging
                logger.info(f"   Raw allowance: {allowance} (base units)")
                logger.info(f"   Allowance in USDC: {allowance/1e6:,.2f} USDC")
                logger.info(f"   Required minimum: 100 USDC (test mode)")

                if allowance < 100 * 1e6:  # Less than 100 USDC approved (LOWERED for testing)
                    logger.warning("⚠️  USDC approval needed!")
                    logger.warning(f"   Current: {allowance/1e6:,.2f} USDC")
                    logger.warning(f"   Required: 100 USDC (test mode)")
                    logger.warning("   Run: python scripts/approve_wallets.py")
                    logger.warning("   Or the bot may fail to place orders")
                    logger.warning("")
                    logger.warning("   ⚠️  NOTE: 100 USDC is for TESTING only!")
                    logger.warning("   For production, approve at least 1,000 USDC")
                else:
                    logger.info(f"✅ USDC approval OK ({allowance/1e6:,.0f} USDC)")
                    if allowance < 1000 * 1e6:
                        logger.warning(f"   ⚠️  Running in TEST MODE with {allowance/1e6:,.0f} USDC")
                        logger.warning(f"   For production, approve at least 1,000 USDC")

        except Exception as e:
            logger.warning(f"⚠️  Could not check USDC approval: {e}")
            logger.warning("   Make sure to run: python scripts/approve_wallets.py")
            import traceback
            logger.debug(traceback.format_exc())
    
    async def _market_scanning_loop(self):
        """Continuous market scanning with monitoring"""
        scanner = self.modules['scanner']
        selector = self.modules['selector']
        monitoring = self.modules['monitoring']

        logger.info("🔍 Starting market scanning loop")

        while self.running:
            scan_start = datetime.now()
            try:
                # Scan for opportunities
                markets = await scanner.scan_rewards_page()

                # Record scan metrics
                monitoring.record_market_scan(len(markets))

                # Filter and score markets
                selected_markets = await selector.select_markets(markets)

                # Send notification AFTER filtering (only show qualifying markets)
                telegram = self.modules.get('telegram')
                if telegram and selected_markets:
                    try:
                        await telegram.notify_market_found(selected_markets)
                    except Exception as e:
                        logger.debug(f"Failed to send market found notification: {e}")

                # Process selected markets
                for market in selected_markets:
                    await self._process_market_opportunity(market)

                # Record API response time
                scan_duration = (datetime.now() - scan_start).total_seconds()
                monitoring.record_api_call(scan_duration, True)

                # Add human-like delay with jitter
                await self._jittered_sleep(self.config['market_scanner']['interval'])

            except Exception as e:
                logger.error(f"Market scanning error: {e}")

                # Record error
                monitoring.record_error('market_scan', str(e))
                monitoring.record_api_call((datetime.now() - scan_start).total_seconds(), False)

                # Send error notification
                telegram = self.modules.get('telegram')
                if telegram:
                    try:
                        await telegram.notify_error('Market Scan', str(e), 'Market scanning loop')
                    except Exception as notify_err:
                        logger.debug(f"Failed to send error notification: {notify_err}")

                await asyncio.sleep(10)
    
    async def _order_management_loop(self):
        """Manage order placement and updates"""
        order_mgr = self.modules['order_mgr']
        wallet_mgr = self.modules['wallet_mgr']

        logger.info("📦 Starting order management loop")

        while self.running:
            try:
                # Get active wallet
                wallet = await wallet_mgr.get_next_wallet()

                # Check pending orders
                pending_orders = await order_mgr.get_pending_orders()

                if pending_orders:
                    logger.info(f"📋 Processing {len(pending_orders)} pending orders")

                # Process each pending order
                processed_orders = []
                for order in pending_orders:
                    try:
                        # Apply ML prediction
                        fill_probability = await self.modules['ml_predictor'].predict_fill(order)

                        logger.debug(f"ML prediction for {order['market_id']}: fill_probability={fill_probability:.2%}")

                        if fill_probability < self.config['ml_prediction']['fill_risk_threshold']:
                            # Place order
                            logger.info(f"📤 Placing order for market {order['market_id']}")
                            result = await order_mgr.place_order(order, wallet)

                            if result:
                                logger.info(f"✅ Order placed successfully: {result}")
                                processed_orders.append(order)
                            else:
                                logger.warning(f"⚠️  Failed to place order for {order['market_id']}")
                        else:
                            logger.info(f"⏭️  Skipping high-risk order {order['market_id']} (fill_probability={fill_probability:.2%})")
                            processed_orders.append(order)
                            self.performance_stats['cancelled_orders'] += 1

                    except Exception as e:
                        logger.error(f"❌ Error processing order {order.get('market_id', 'unknown')}: {e}", exc_info=True)

                # Remove processed orders from pending queue
                for order in processed_orders:
                    if order in order_mgr.pending_orders:
                        order_mgr.pending_orders.remove(order)

                # Sleep before next check
                await asyncio.sleep(5)  # Check every 5 seconds

            except Exception as e:
                logger.error(f"❌ Order management loop error: {e}", exc_info=True)
                await asyncio.sleep(10)
    
    async def _position_monitoring_loop(self):
        """Monitor open positions and market conditions"""
        monitor = self.modules['monitor']
        order_mgr = self.modules['order_mgr']

        logger.info("👁️  Starting position monitoring loop")

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

        logger.info("🛡️  Starting risk management loop")

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

        logger.info("🤖 Starting ML training loop")

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

        logger.info("📊 Starting daily optimization loop")

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

    async def _profit_taking_loop(self):
        """Automated profit taking loop - close profitable positions"""
        profit_mgr = self.modules['profit_mgr']

        logger.info("💰 Starting automated profit taking loop")

        while self.running:
            try:
                # Check and close profitable positions
                await profit_mgr.check_and_close_positions()

                # Wait for next check interval
                check_interval = profit_mgr.check_interval
                logger.info(f"⏳ Next profit check in {check_interval}s")
                await asyncio.sleep(check_interval)

            except Exception as e:
                logger.error(f"Profit taking error: {e}")
                await asyncio.sleep(60)  # Wait 1 minute before retry
    
    async def _process_market_opportunity(self, market: dict):
        """Process a selected market opportunity"""
        try:
            # Get market ID (CLOB API uses 'market_id' or 'condition_id', Gamma API uses 'id')
            market_id = market.get('market_id') or market.get('condition_id') or market.get('id', 'unknown')

            # Check risk limits
            if not await self.modules['risk_mgr'].check_market_limit(market):
                logger.info(f"Skipping market {market_id} due to risk limits")
                return

            # Prepare order with dynamic spread
            order = await self.modules['order_mgr'].prepare_market_order(market)

            # Add to pending orders ONLY if order is valid
            if order:
                await self.modules['order_mgr'].add_pending_order(order)
                logger.info(f"✅ Added market {market_id} to pending orders")
            else:
                logger.warning(f"⚠️  Skipped market {market_id} - could not prepare valid order (spread too high or orderbook too thin)")

        except Exception as e:
            market_id = market.get('market_id') or market.get('condition_id') or market.get('id', 'unknown')
            logger.error(f"Error processing market {market_id}: {e}")
    
    async def _monitoring_loop(self):
        """Continuous health monitoring"""
        monitoring = self.modules['monitoring']

        logger.info("🏥 Starting health monitoring loop")

        while self.running:
            try:
                # Check health status
                health = await monitoring.check_health()

                # Log health status
                if not health['healthy']:
                    logger.warning(f"⚠️ Health check failed: {len(health['issues'])} issues")
                    for issue in health['issues']:
                        logger.warning(f"   - {issue['message']}")
                else:
                    logger.debug("✅ Health check passed")

                # Wait 30 seconds before next check
                await asyncio.sleep(30)

            except Exception as e:
                logger.error(f"Monitoring loop error: {e}")
                await asyncio.sleep(60)

    async def _hourly_report_loop(self):
        """Send hourly performance reports"""
        monitoring = self.modules['monitoring']

        logger.info("📈 Starting hourly report loop")

        while self.running:
            try:
                # Calculate time until next hour
                now = datetime.now()
                next_hour = (now + timedelta(hours=1)).replace(
                    minute=0, second=0, microsecond=0
                )
                seconds_until_next_hour = (next_hour - now).total_seconds()

                # Wait until next hour
                await asyncio.sleep(seconds_until_next_hour)

                # Send hourly report via TelegramNotifier
                telegram = self.modules.get('telegram')
                if telegram and self.config.get('alerts', {}).get('notifications', {}).get('hourly_report', True):
                    try:
                        stats = monitoring.get_statistics(time_window_minutes=60)
                        health = await monitoring.check_health()
                        await telegram.notify_hourly_report(stats, health)
                    except Exception as e:
                        logger.error(f"Failed to send hourly report: {e}")
                else:
                    # Fallback to old method
                    await monitoring.send_hourly_report()

            except Exception as e:
                logger.error(f"Hourly report error: {e}")
                await asyncio.sleep(3600)  # Retry in 1 hour

    async def _jittered_sleep(self, base_seconds: float):
        """Sleep with random jitter to appear more human-like"""
        jitter = random.uniform(-0.2, 0.2) * base_seconds
        await asyncio.sleep(base_seconds + jitter)

    async def _send_startup_alert(self):
        """Send startup notification via Telegram"""
        try:
            wallet_mgr = self.modules.get('wallet_mgr')
            num_wallets = len(wallet_mgr.wallets) if wallet_mgr else 0

            # Use new TelegramNotifier
            telegram = self.modules.get('telegram')
            if telegram:
                await telegram.notify_startup(num_wallets)
                logger.info("✅ Startup alert sent via TelegramNotifier")
            else:
                # Fallback to old method
                await self.modules['ml_predictor'].send_alert(f"🚀 Bot Started - {num_wallets} wallets")
                logger.info("✅ Startup alert sent via MLPredictor")

        except Exception as e:
            logger.error(f"Failed to send startup alert: {e}")

    async def _send_performance_report(self):
        """Send daily performance report via alerts"""
        try:
            report = f"""
📊 <b>Daily Performance Report</b>
━━━━━━━━━━━━━━━━━━━━━━
💰 Daily P&L: ${self.performance_stats['daily_pnl']:.2f}
✅ Successful Trades: {self.performance_stats['successful_trades']}
📝 Total Fills: {self.performance_stats['total_fills']}
❌ Cancelled Orders: {self.performance_stats['cancelled_orders']}
━━━━━━━━━━━━━━━━━━━━━━
            """

            # Send via configured alert channels
            await self.modules['ml_predictor'].send_alert(report.strip())

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