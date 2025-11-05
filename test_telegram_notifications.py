#!/usr/bin/env python3
"""
Test script for enhanced Telegram notifications
Tests all notification types
"""

import asyncio
import yaml
import logging
from datetime import datetime
from dotenv import load_dotenv
import os

# Load environment
load_dotenv()

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Import TelegramNotifier
from telegram_notifier import TelegramNotifier


async def test_all_notifications():
    """Test all notification types"""
    
    print("=" * 80)
    print("TESTING TELEGRAM NOTIFICATIONS")
    print("=" * 80)
    
    # Load config
    with open('config.yaml', 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    
    # Override with .env
    config['alerts']['telegram_bot_token'] = os.getenv('TELEGRAM_BOT_TOKEN', '')
    config['alerts']['telegram_chat_id'] = os.getenv('TELEGRAM_CHAT_ID', '')
    
    # Initialize notifier
    telegram = TelegramNotifier(config)
    
    if not telegram.enabled:
        print("\n❌ Telegram not enabled!")
        print("   Please set TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID in .env")
        return
    
    print(f"\n✅ Telegram enabled")
    print(f"   Bot Token: {telegram.bot_token[:20]}...")
    print(f"   Chat ID: {telegram.chat_id}")
    
    # Test 1: Startup notification
    print("\n" + "=" * 80)
    print("TEST 1: Startup Notification")
    print("=" * 80)
    
    await telegram.notify_startup(num_wallets=3)
    print("✅ Startup notification sent")
    await asyncio.sleep(2)
    
    # Test 2: Order placed notification
    print("\n" + "=" * 80)
    print("TEST 2: Order Placed Notification")
    print("=" * 80)
    
    test_order = {
        'market_id': 'test-market-123',
        'market_title': 'Will Bitcoin hit $100k by end of 2024?',
        'yes_order': {
            'price': 0.485,
            'size': 100
        },
        'no_order': {
            'price': 0.515,
            'size': 100
        },
        'spread': 0.03
    }
    
    test_market = {
        'question': 'Will Bitcoin hit $100k by end of 2024?',
        'id': 'test-market-123'
    }
    
    await telegram.notify_order_placed(test_order, test_market)
    print("✅ Order placed notification sent")
    await asyncio.sleep(2)
    
    # Test 3: Order filled notification (IMPORTANT!)
    print("\n" + "=" * 80)
    print("TEST 3: Order Filled Notification (CRITICAL!)")
    print("=" * 80)
    
    test_fill = {
        'market_id': 'test-market-123',
        'side': 'yes',
        'order_id': 'order-abc-123',
        'fill_price': 0.485,
        'fill_size': 50
    }
    
    await telegram.notify_order_filled(test_fill, test_market, pnl=-5.50)
    print("✅ Order filled notification sent")
    await asyncio.sleep(2)
    
    # Test 4: Order cancelled notification
    print("\n" + "=" * 80)
    print("TEST 4: Order Cancelled Notification")
    print("=" * 80)
    
    await telegram.notify_order_cancelled(
        'order-xyz-456',
        'Will Bitcoin hit $100k by end of 2024?',
        'Partial fill threshold exceeded'
    )
    print("✅ Order cancelled notification sent")
    await asyncio.sleep(2)
    
    # Test 5: Markets found notification
    print("\n" + "=" * 80)
    print("TEST 5: Markets Found Notification")
    print("=" * 80)
    
    test_markets = [
        {
            'question': 'Will Bitcoin hit $100k by end of 2024?',
            'reward': 250,
            'competition_bars': 1
        },
        {
            'question': 'Will Trump win 2024 election?',
            'reward': 180,
            'competition_bars': 2
        },
        {
            'question': 'Will Ethereum reach $5000 in 2024?',
            'reward': 150,
            'competition_bars': 0
        }
    ]
    
    await telegram.notify_market_found(test_markets)
    print("✅ Markets found notification sent")
    await asyncio.sleep(2)
    
    # Test 6: Error notification
    print("\n" + "=" * 80)
    print("TEST 6: Error Notification")
    print("=" * 80)
    
    await telegram.notify_error(
        'API Error',
        'Failed to connect to Gamma API: Connection timeout',
        'Market scanning loop'
    )
    print("✅ Error notification sent")
    await asyncio.sleep(2)
    
    # Test 7: Circuit breaker notification
    print("\n" + "=" * 80)
    print("TEST 7: Circuit Breaker Notification")
    print("=" * 80)
    
    await telegram.notify_circuit_breaker('gamma_api', 'OPEN')
    print("✅ Circuit breaker OPEN notification sent")
    await asyncio.sleep(2)
    
    await telegram.notify_circuit_breaker('gamma_api', 'CLOSED')
    print("✅ Circuit breaker CLOSED notification sent")
    await asyncio.sleep(2)
    
    # Test 8: Risk alert notification
    print("\n" + "=" * 80)
    print("TEST 8: Risk Alert Notification")
    print("=" * 80)
    
    await telegram.notify_risk_alert(
        'High Exposure',
        {
            'total_exposure': 850.00,
            'max_allowed': 800.00,
            'exposure_ratio': 0.85,
            'action': 'Reduce positions'
        }
    )
    print("✅ Risk alert notification sent")
    await asyncio.sleep(2)
    
    # Test 9: Hourly report
    print("\n" + "=" * 80)
    print("TEST 9: Hourly Report")
    print("=" * 80)
    
    test_stats = {
        'total_scans': 120,
        'total_markets_found': 15,
        'total_orders_placed': 8,
        'total_orders_filled': 2,
        'total_profit': 12.50
    }
    
    test_health = {
        'healthy': True,
        'metrics': {
            'system_cpu_percent': 45.2,
            'system_memory_percent': 62.8
        },
        'issues': []
    }
    
    await telegram.notify_hourly_report(test_stats, test_health)
    print("✅ Hourly report sent")
    await asyncio.sleep(2)
    
    # Test 10: Daily report
    print("\n" + "=" * 80)
    print("TEST 10: Daily Report")
    print("=" * 80)
    
    test_daily_stats = {
        'total_pnl': 45.80,
        'orders_placed': 156,
        'orders_filled': 12,
        'fill_rate': 0.077,
        'markets_traded': 8,
        'estimated_rewards': 120.00,
        'fill_pnl': -74.20,
        'win_rate': 0.583,
        'avg_profit': 3.82,
        'best_trade': 15.50,
        'worst_trade': -12.30
    }
    
    await telegram.notify_daily_report(test_daily_stats)
    print("✅ Daily report sent")
    await asyncio.sleep(2)
    
    # Test 11: Shutdown notification
    print("\n" + "=" * 80)
    print("TEST 11: Shutdown Notification")
    print("=" * 80)
    
    await telegram.notify_shutdown("Test completed")
    print("✅ Shutdown notification sent")
    
    # Summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print("✅ All 11 notification types tested successfully!")
    print("\nCheck your Telegram app to verify all messages were received.")
    print("\nNotification types tested:")
    print("   1. ✅ Startup")
    print("   2. ✅ Order Placed")
    print("   3. ✅ Order Filled (CRITICAL)")
    print("   4. ✅ Order Cancelled")
    print("   5. ✅ Markets Found")
    print("   6. ✅ Error")
    print("   7. ✅ Circuit Breaker (OPEN/CLOSED)")
    print("   8. ✅ Risk Alert")
    print("   9. ✅ Hourly Report")
    print("  10. ✅ Daily Report")
    print("  11. ✅ Shutdown")
    print("\n" + "=" * 80)


if __name__ == '__main__':
    asyncio.run(test_all_notifications())

