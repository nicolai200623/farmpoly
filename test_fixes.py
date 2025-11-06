"""
Test script để kiểm tra các bug fixes
Chạy script này để verify các sửa đổi hoạt động đúng
"""

import asyncio
import logging
import sys
from dotenv import load_dotenv

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

load_dotenv()


async def test_profit_taking_api_creds():
    """Test 1: Kiểm tra API credentials được set đúng trong ProfitTakingManager"""
    logger.info("\n" + "="*70)
    logger.info("TEST 1: Profit Taking API Credentials")
    logger.info("="*70)
    
    try:
        from profit_taking_manager import ProfitTakingManager
        import yaml
        
        # Load config
        with open('config.yaml', 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
        
        # Initialize manager
        profit_mgr = ProfitTakingManager(config)
        
        # Check if client is initialized
        if profit_mgr.client is None:
            logger.error("❌ CLOB client not initialized!")
            return False
        
        logger.info("✅ CLOB client initialized successfully")
        
        # Check if client has set_api_creds method
        if not hasattr(profit_mgr.client, 'set_api_creds'):
            logger.error("❌ Client missing set_api_creds method!")
            return False
        
        logger.info("✅ Client has set_api_creds method")
        
        # Try to create and set API credentials
        try:
            api_creds = profit_mgr.client.create_or_derive_api_creds()
            profit_mgr.client.set_api_creds(api_creds)
            logger.info("✅ API credentials can be created and set successfully")
        except Exception as e:
            logger.error(f"❌ Failed to set API credentials: {e}")
            return False
        
        logger.info("\n✅ TEST 1 PASSED: Profit Taking API credentials working correctly")
        return True
        
    except Exception as e:
        logger.error(f"❌ TEST 1 FAILED: {e}", exc_info=True)
        return False


async def test_order_management_loop_logging():
    """Test 2: Kiểm tra logging trong order management loop"""
    logger.info("\n" + "="*70)
    logger.info("TEST 2: Order Management Loop Logging")
    logger.info("="*70)
    
    try:
        # Read main.py and check for logging statements
        with open('main.py', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for startup logs in all loops
        required_logs = [
            ('🔍 Starting market scanning loop', '_market_scanning_loop'),
            ('📦 Starting order management loop', '_order_management_loop'),
            ('👁️  Starting position monitoring loop', '_position_monitoring_loop'),
            ('🛡️  Starting risk management loop', '_risk_management_loop'),
            ('🤖 Starting ML training loop', '_ml_training_loop'),
            ('📊 Starting daily optimization loop', '_daily_optimization_loop'),
            ('🏥 Starting health monitoring loop', '_monitoring_loop'),
            ('📈 Starting hourly report loop', '_hourly_report_loop'),
        ]
        
        all_found = True
        for log_msg, loop_name in required_logs:
            if log_msg in content:
                logger.info(f"✅ Found log in {loop_name}: '{log_msg}'")
            else:
                logger.error(f"❌ Missing log in {loop_name}: '{log_msg}'")
                all_found = False
        
        # Check for detailed logging in order management loop
        order_mgr_logs = [
            'Processing',
            'pending orders',
            'Placing order for market',
            'Order placed successfully',
            'exc_info=True'  # Stack trace logging
        ]
        
        for log_check in order_mgr_logs:
            if log_check in content:
                logger.info(f"✅ Found detailed logging: '{log_check}'")
            else:
                logger.warning(f"⚠️  Missing detailed logging: '{log_check}'")
        
        if all_found:
            logger.info("\n✅ TEST 2 PASSED: All required logging statements found")
            return True
        else:
            logger.error("\n❌ TEST 2 FAILED: Some logging statements missing")
            return False
        
    except Exception as e:
        logger.error(f"❌ TEST 2 FAILED: {e}", exc_info=True)
        return False


async def test_order_queue_processing():
    """Test 3: Kiểm tra logic xử lý pending orders"""
    logger.info("\n" + "="*70)
    logger.info("TEST 3: Order Queue Processing Logic")
    logger.info("="*70)
    
    try:
        # Read main.py and check for order processing logic
        with open('main.py', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for key logic elements
        logic_checks = [
            ('pending_orders = await order_mgr.get_pending_orders()', 'Get pending orders'),
            ('if pending_orders:', 'Check if orders exist'),
            ('for order in pending_orders:', 'Iterate through orders'),
            ('fill_probability = await', 'ML prediction'),
            ('await order_mgr.place_order(order, wallet)', 'Place order'),
            ('processed_orders.append(order)', 'Track processed orders'),
            ('order_mgr.pending_orders.remove(order)', 'Remove from queue'),
        ]
        
        all_found = True
        for code_snippet, description in logic_checks:
            if code_snippet in content:
                logger.info(f"✅ Found logic: {description}")
            else:
                logger.error(f"❌ Missing logic: {description}")
                all_found = False
        
        if all_found:
            logger.info("\n✅ TEST 3 PASSED: Order processing logic looks correct")
            return True
        else:
            logger.error("\n❌ TEST 3 FAILED: Some logic elements missing")
            return False
        
    except Exception as e:
        logger.error(f"❌ TEST 3 FAILED: {e}", exc_info=True)
        return False


async def test_profit_taking_code_fix():
    """Test 4: Kiểm tra code fix trong profit_taking_manager.py"""
    logger.info("\n" + "="*70)
    logger.info("TEST 4: Profit Taking Code Fix")
    logger.info("="*70)
    
    try:
        # Read profit_taking_manager.py
        with open('profit_taking_manager.py', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for the fix
        if 'self.client.set_api_creds(' in content:
            logger.info("✅ Found set_api_creds() call")
        else:
            logger.error("❌ Missing set_api_creds() call")
            return False
        
        # Check for proper error handling
        if 'raise' in content and 'Failed to set API credentials' in content:
            logger.info("✅ Found proper error handling")
        else:
            logger.warning("⚠️  Error handling might be incomplete")
        
        # Check for logging
        if 'API credentials set successfully' in content:
            logger.info("✅ Found success logging")
        else:
            logger.warning("⚠️  Success logging might be missing")
        
        logger.info("\n✅ TEST 4 PASSED: Profit taking code fix verified")
        return True
        
    except Exception as e:
        logger.error(f"❌ TEST 4 FAILED: {e}", exc_info=True)
        return False


async def main():
    """Run all tests"""
    logger.info("\n" + "="*70)
    logger.info("🧪 RUNNING BUG FIX VERIFICATION TESTS")
    logger.info("="*70)
    
    results = []
    
    # Run all tests
    results.append(await test_profit_taking_api_creds())
    results.append(await test_order_management_loop_logging())
    results.append(await test_order_queue_processing())
    results.append(await test_profit_taking_code_fix())
    
    # Summary
    logger.info("\n" + "="*70)
    logger.info("📊 TEST SUMMARY")
    logger.info("="*70)
    
    passed = sum(results)
    total = len(results)
    
    logger.info(f"Tests Passed: {passed}/{total}")
    
    if passed == total:
        logger.info("\n✅ ALL TESTS PASSED! Bug fixes verified successfully.")
        logger.info("\n🚀 You can now restart the bot with confidence!")
        return 0
    else:
        logger.error(f"\n❌ {total - passed} TEST(S) FAILED! Please review the errors above.")
        return 1


if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)

