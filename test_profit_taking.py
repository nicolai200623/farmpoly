#!/usr/bin/env python3
"""
Test Profit Taking Manager
Test automatic profit taking with current positions
"""

import asyncio
import logging
import yaml
from profit_taking_manager import ProfitTakingManager
from telegram_notifier import TelegramNotifier

# Setup logging
logging.basicConfig(
    level=logging.DEBUG,  # Changed to DEBUG for detailed logging
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


async def main():
    """Test profit taking manager"""
    try:
        # Load config
        logger.info("📂 Loading config...")
        with open('config.yaml', 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
        
        # Initialize Telegram notifier
        logger.info("📱 Initializing Telegram notifier...")
        telegram = TelegramNotifier(config)
        
        # Initialize Profit Taking Manager
        logger.info("💰 Initializing Profit Taking Manager...")
        profit_mgr = ProfitTakingManager(config, telegram_notifier=telegram)
        
        # Display configuration
        logger.info("\n" + "="*70)
        logger.info("📊 PROFIT TAKING CONFIGURATION:")
        logger.info("="*70)
        logger.info(f"Enabled: {profit_mgr.enabled}")
        logger.info(f"Check Interval: {profit_mgr.check_interval}s")
        logger.info(f"Min Profit: {profit_mgr.min_profit_pct}%")
        logger.info(f"Target Profit: {profit_mgr.target_profit_pct}%")
        logger.info(f"Max Profit: {profit_mgr.max_profit_pct}%")
        logger.info(f"Never Close Losing: {profit_mgr.never_close_losing}")
        logger.info(f"Alert on Close: {profit_mgr.alert_on_close}")
        logger.info("="*70 + "\n")
        
        # Check and close positions
        logger.info("🔍 Checking positions for profit taking opportunities...")
        logger.info("="*70 + "\n")
        
        await profit_mgr.check_and_close_positions()
        
        # Display stats
        logger.info("\n" + "="*70)
        logger.info("📈 PROFIT TAKING STATS:")
        logger.info("="*70)
        stats = profit_mgr.get_stats()
        for key, value in stats.items():
            logger.info(f"{key}: {value}")
        logger.info("="*70)
        
        logger.info("\n✅ Test completed successfully!")
        
    except Exception as e:
        logger.error(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(main())

