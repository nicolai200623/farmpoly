#!/usr/bin/env python3
"""Test the fix by running one iteration of market scanning"""

import asyncio
import sys
import os
from pathlib import Path
from dotenv import load_dotenv

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

import yaml
import logging

# Set logging to DEBUG to see all details
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

async def test_fix():
    """Test the fix"""
    try:
        # Load environment variables
        load_dotenv()
        
        # Load config
        with open('config.yaml', 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
        
        # Import modules
        from market_scanner_v2 import MarketScannerV2
        from order_manager import OrderManager
        
        # Initialize scanner
        logger.info("🔍 Initializing market scanner...")
        scanner = MarketScannerV2(config['market_scanner'])
        
        # Initialize order manager
        logger.info("📋 Initializing order manager...")
        order_mgr = OrderManager(config['order_management'])
        
        # Scan markets
        logger.info("\n" + "="*60)
        logger.info("🔍 SCANNING MARKETS...")
        logger.info("="*60 + "\n")
        
        markets = await scanner.scan_rewards_page()
        
        logger.info(f"\n✅ Found {len(markets)} qualifying markets")
        
        if not markets:
            logger.info("No markets to test")
            return
        
        # Test order preparation for first market
        logger.info("\n" + "="*60)
        logger.info("📋 TESTING ORDER PREPARATION...")
        logger.info("="*60 + "\n")
        
        test_market = markets[0]
        logger.info(f"Testing market: {test_market.get('question', 'Unknown')}")
        logger.info(f"Reward: ${test_market.get('reward', 0)}")
        logger.info(f"Competition: {test_market.get('competition_bars', 0)} bars")
        logger.info("")
        
        order = await order_mgr.prepare_market_order(test_market)
        
        if order:
            logger.info("\n✅ Order prepared successfully!")
            logger.info(f"   YES: ${order['yes_order']['price']:.4f}")
            logger.info(f"   NO: ${order['no_order']['price']:.4f}")
        else:
            logger.info("\n❌ Order preparation failed (market rejected)")
        
        logger.info("\n" + "="*60)
        logger.info("✅ TEST COMPLETE")
        logger.info("="*60)
        
    except Exception as e:
        logger.error(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_fix())

