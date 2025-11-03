"""
Test script để verify tất cả optimizations
Kiểm tra monitoring, circuit breaker, và market scanner
"""

import asyncio
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from market_scanner_v2 import MarketScannerV2
from circuit_breaker import CircuitBreaker, CircuitBreakerOpenError
from monitoring_system import MonitoringSystem
from ml_predictor import MLPredictor
import yaml
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


async def test_circuit_breaker():
    """Test circuit breaker functionality"""
    print("\n" + "="*80)
    print("🔧 TEST 1: CIRCUIT BREAKER")
    print("="*80)
    
    # Create a test circuit breaker
    breaker = CircuitBreaker(
        name="test_api",
        failure_threshold=3,
        timeout_seconds=5,
        success_threshold=2
    )
    
    # Simulate failing API
    async def failing_api():
        raise Exception("API Error")
    
    # Simulate successful API
    async def successful_api():
        return "Success"
    
    print("\n📝 Test 1.1: Trigger circuit breaker with failures")
    for i in range(5):
        try:
            await breaker.call(failing_api)
        except CircuitBreakerOpenError as e:
            print(f"   ✅ Call {i+1}: Circuit OPEN - {e}")
        except Exception as e:
            print(f"   ⚠️  Call {i+1}: Failed - {e}")
    
    # Check stats
    stats = breaker.get_stats()
    print(f"\n📊 Stats after failures:")
    print(f"   - State: {stats['state']}")
    print(f"   - Total calls: {stats['total_calls']}")
    print(f"   - Total failures: {stats['total_failures']}")
    print(f"   - Total rejected: {stats['total_rejected']}")
    
    assert stats['state'] == 'open', "Circuit should be OPEN"
    print("   ✅ Circuit breaker correctly OPENED after failures")
    
    print(f"\n📝 Test 1.2: Wait for timeout and recovery")
    print(f"   Waiting {breaker.timeout_seconds}s for timeout...")
    await asyncio.sleep(breaker.timeout_seconds + 1)
    
    # Try successful calls
    for i in range(3):
        try:
            result = await breaker.call(successful_api)
            print(f"   ✅ Call {i+1}: {result}")
        except Exception as e:
            print(f"   ❌ Call {i+1}: {e}")
    
    # Check final stats
    stats = breaker.get_stats()
    print(f"\n📊 Final stats:")
    print(f"   - State: {stats['state']}")
    print(f"   - Success rate: {stats['success_rate']:.1%}")
    
    assert stats['state'] == 'closed', "Circuit should be CLOSED after recovery"
    print("   ✅ Circuit breaker correctly CLOSED after recovery")
    
    print("\n✅ Circuit Breaker Test PASSED!")


async def test_monitoring_system():
    """Test monitoring system"""
    print("\n" + "="*80)
    print("📊 TEST 2: MONITORING SYSTEM")
    print("="*80)
    
    # Create mock ML predictor for alerts
    class MockMLPredictor:
        async def send_alert(self, message):
            print(f"   📨 Alert: {message[:50]}...")
    
    # Create monitoring system
    config = {'market_scanner': {'interval': 5}}
    monitoring = MonitoringSystem(config, MockMLPredictor())
    
    print("\n📝 Test 2.1: Record metrics")
    
    # Record some scans
    for i in range(5):
        monitoring.record_market_scan(markets_found=10 + i)
        print(f"   ✅ Recorded scan {i+1}: {10+i} markets")
    
    # Record some orders
    for i in range(3):
        monitoring.record_order_placed(f"order_{i}")
        print(f"   ✅ Recorded order {i+1}")
    
    # Record some fills
    for i in range(2):
        monitoring.record_order_filled(f"order_{i}", profit=5.0 + i)
        print(f"   ✅ Recorded fill {i+1}: ${5.0+i:.2f}")
    
    # Record API calls
    monitoring.record_api_call(response_time=1.5, success=True)
    monitoring.record_api_call(response_time=2.0, success=True)
    print(f"   ✅ Recorded API calls")
    
    print("\n📝 Test 2.2: Get statistics")
    stats = monitoring.get_statistics(time_window_minutes=60)
    
    print(f"\n📊 Statistics (last 60 min):")
    print(f"   - Total scans: {stats['total_scans']}")
    print(f"   - Total markets found: {stats['total_markets_found']}")
    print(f"   - Avg markets/scan: {stats['avg_markets_per_scan']:.1f}")
    print(f"   - Total orders placed: {stats['total_orders_placed']}")
    print(f"   - Total orders filled: {stats['total_orders_filled']}")
    print(f"   - Fill rate: {stats['fill_rate']:.1%}")
    print(f"   - Total profit: ${stats['total_profit']:.2f}")
    
    assert stats['total_scans'] == 5, "Should have 5 scans"
    assert stats['total_orders_placed'] == 3, "Should have 3 orders"
    assert stats['total_orders_filled'] == 2, "Should have 2 fills"
    print("   ✅ Statistics correct")
    
    print("\n📝 Test 2.3: Health check")
    health = await monitoring.check_health()
    
    print(f"\n🏥 Health Status:")
    print(f"   - Healthy: {health['healthy']}")
    print(f"   - Issues: {len(health['issues'])}")
    
    if health['issues']:
        for issue in health['issues']:
            print(f"      • {issue['message']}")
    
    print("\n✅ Monitoring System Test PASSED!")


async def test_market_scanner():
    """Test market scanner with optimizations"""
    print("\n" + "="*80)
    print("🔍 TEST 3: MARKET SCANNER WITH OPTIMIZATIONS")
    print("="*80)
    
    # Load config
    try:
        with open('config.yaml', 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
        scanner_config = config.get('market_scanner', {})
    except Exception as e:
        print(f"   ⚠️  Using default config: {e}")
        scanner_config = {
            'min_reward': 10,
            'max_competition_bars': 5,
            'min_shares': 500
        }
    
    print(f"\n📋 Scanner config:")
    print(f"   - Min reward: ${scanner_config.get('min_reward', 10)}")
    print(f"   - Max competition: {scanner_config.get('max_competition_bars', 5)} bars")
    
    # Create scanner
    scanner = MarketScannerV2(scanner_config)
    
    # Initialize
    print(f"\n🌐 Initializing browser...")
    await scanner.initialize()
    
    # Test circuit breaker stats
    print(f"\n📊 Circuit Breaker Stats (before scan):")
    api_stats = scanner.api_breaker.get_stats()
    print(f"   - API breaker state: {api_stats['state']}")
    
    # Scan markets
    print(f"\n🔍 Scanning markets...")
    markets = await scanner.scan_rewards_page()
    
    # Display results
    print(f"\n📊 Scan Results:")
    print(f"   - Markets found: {len(markets)}")
    
    if len(markets) > 0:
        print(f"\n📋 Top 5 markets:")
        for i, market in enumerate(markets[:5], 1):
            print(f"   {i}. {market['question'][:60]}")
            print(f"      💰 Reward: ${market['reward']:.0f}")
            print(f"      📊 Competition: {market['competition_bars']} bars")
            print(f"      ⭐ Score: {market.get('score', 0):.1f}")
    
    # Test circuit breaker stats after scan
    print(f"\n📊 Circuit Breaker Stats (after scan):")
    api_stats = scanner.api_breaker.get_stats()
    print(f"   - API breaker state: {api_stats['state']}")
    print(f"   - Total calls: {api_stats['total_calls']}")
    print(f"   - Success rate: {api_stats['success_rate']:.1%}")
    
    # Close scanner
    await scanner.close()
    
    assert len(markets) > 0, "Should find at least some markets"
    print("\n✅ Market Scanner Test PASSED!")


async def main():
    """Run all tests"""
    print("="*80)
    print("🧪 TESTING ALL OPTIMIZATIONS")
    print("="*80)
    
    try:
        # Test 1: Circuit Breaker
        await test_circuit_breaker()
        
        # Test 2: Monitoring System
        await test_monitoring_system()
        
        # Test 3: Market Scanner
        await test_market_scanner()
        
        # Summary
        print("\n" + "="*80)
        print("🎉 ALL TESTS PASSED!")
        print("="*80)
        print("\n✅ Optimizations verified:")
        print("   1. ✅ Circuit Breaker working correctly")
        print("   2. ✅ Monitoring System tracking metrics")
        print("   3. ✅ Market Scanner finding markets")
        print("\n🚀 Bot is ready to run!")
        
    except AssertionError as e:
        print(f"\n❌ TEST FAILED: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())

