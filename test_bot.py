#!/usr/bin/env python3
"""
Test Script for Polymarket Trading Bot
Run various tests to ensure bot functionality
"""

import asyncio
import sys
import os
import logging
from datetime import datetime
import json

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import bot modules
from modules.market_scanner import MarketScanner
from modules.market_selector import MarketSelectorAI
from modules.order_manager import OrderManager
from modules.position_monitor import PositionMonitor
from modules.risk_manager import RiskManager
from modules.wallet_manager import WalletManager
from modules.ml_predictor import MLPredictor
from modules.optimizer import DailyOptimizer

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class BotTester:
    """Test suite for Polymarket bot"""
    
    def __init__(self):
        self.test_config = {
            'market_scanner': {
                'interval': 5,
                'min_reward': 300,
                'max_competition_bars': 2,
                'min_shares': 500
            },
            'order_management': {
                'spread_min': 0.008,
                'spread_max': 0.015,
                'size_min': 200,
                'size_max': 500
            },
            'risk_management': {
                'max_capital_per_market': 0.05,
                'enable_hedging': True
            },
            'wallet_management': {
                'num_wallets': 3,
                'jitter_percentage': 0.2
            },
            'ml_prediction': {
                'fill_risk_threshold': 0.8,
                'model_update_interval': 3600
            },
            'monitoring': {
                'websocket_interval': 10,
                'partial_fill_threshold': 0.1,
                'volume_spike_multiplier': 2,
                'price_move_threshold': 0.02
            }
        }
        
        self.test_results = []
    
    async def run_all_tests(self):
        """Run all test suites"""
        print("=" * 60)
        print("POLYMARKET BOT TEST SUITE")
        print("=" * 60)
        
        tests = [
            self.test_market_scanner,
            self.test_market_selector,
            self.test_order_manager,
            self.test_risk_manager,
            self.test_wallet_manager,
            self.test_ml_predictor,
            self.test_position_monitor,
            self.test_optimizer
        ]
        
        for test in tests:
            try:
                await test()
                self.test_results.append({
                    'test': test.__name__,
                    'status': 'PASSED',
                    'timestamp': datetime.now().isoformat()
                })
            except Exception as e:
                self.test_results.append({
                    'test': test.__name__,
                    'status': 'FAILED',
                    'error': str(e),
                    'timestamp': datetime.now().isoformat()
                })
                logger.error(f"Test {test.__name__} failed: {e}")
        
        self.print_results()
    
    async def test_market_scanner(self):
        """Test market scanner module"""
        print("\n📡 Testing Market Scanner...")
        
        scanner = MarketScanner(self.test_config['market_scanner'])
        
        # Test initialization
        assert scanner.config is not None
        assert scanner.base_url == "https://polymarket.com"
        
        # Test market filtering
        test_markets = [
            {'id': '1', 'reward': 500, 'competition_bars': 1, 'min_shares': 100},
            {'id': '2', 'reward': 200, 'competition_bars': 1, 'min_shares': 100},
            {'id': '3', 'reward': 400, 'competition_bars': 4, 'min_shares': 100},
        ]
        
        filtered = scanner._filter_markets(test_markets)
        assert len(filtered) == 1  # Only first market passes all filters
        
        print("✅ Market Scanner tests passed")
    
    async def test_market_selector(self):
        """Test market selector AI"""
        print("\n🤖 Testing Market Selector AI...")
        
        selector = MarketSelectorAI(self.test_config)
        
        # Test scoring
        test_market = {
            'id': 'test-1',
            'title': 'Test Market',
            'reward': 500,
            'competition_bars': 1,
            'volume': 10000,
            'liquidity': 5000,
            'category': 'sports',
            'yes_price': 0.45,
            'no_price': 0.55,
            'end_date': '2024-12-31T00:00:00Z'
        }
        
        score = await selector._calculate_market_score(test_market)
        assert 0 <= score <= 1, f"Score {score} out of range"
        
        print(f"  Market score: {score:.2f}")
        print("✅ Market Selector tests passed")
    
    async def test_order_manager(self):
        """Test order manager"""
        print("\n📝 Testing Order Manager...")
        
        manager = OrderManager(self.test_config['order_management'])
        
        # Test spread calculation
        market_data = {
            'mid_price': 0.5,
            'best_bid': 0.48,
            'best_ask': 0.52,
            'current_spread': 0.04,
            'bid_volume': 1000,
            'ask_volume': 1000
        }
        
        spread = manager._calculate_dynamic_spread(market_data)
        assert self.test_config['order_management']['spread_min'] <= spread <= self.test_config['order_management']['spread_max']
        
        print(f"  Dynamic spread: {spread:.4f}")
        
        # Test size calculation
        yes_size, no_size = manager._calculate_order_sizes()
        assert self.test_config['order_management']['size_min'] <= yes_size <= self.test_config['order_management']['size_max']
        assert self.test_config['order_management']['size_min'] <= no_size <= self.test_config['order_management']['size_max']
        
        print(f"  Order sizes: YES={yes_size}, NO={no_size}")
        print("✅ Order Manager tests passed")
    
    async def test_risk_manager(self):
        """Test risk manager"""
        print("\n🛡️ Testing Risk Manager...")
        
        risk_mgr = RiskManager(self.test_config['risk_management'])
        risk_mgr.set_total_capital(10000)
        
        # Test capital allocation
        test_market = {
            'id': 'test-market',
            'category': 'sports',
            'title': 'Test Market'
        }
        
        can_trade = await risk_mgr.check_market_limit(test_market)
        assert can_trade == True, "Should allow first market"
        
        # Test risk metrics
        risk_metrics = await risk_mgr.calculate_portfolio_risk()
        assert 'needs_hedging' in risk_metrics
        assert 'total_exposure' in risk_metrics
        
        print(f"  Total capital: ${risk_mgr.total_capital}")
        print(f"  Risk metrics: {risk_metrics}")
        print("✅ Risk Manager tests passed")
    
    async def test_wallet_manager(self):
        """Test wallet manager"""
        print("\n👛 Testing Wallet Manager...")
        
        wallet_mgr = WalletManager(self.test_config['wallet_management'])
        
        # Test wallet creation
        assert len(wallet_mgr.wallets) == self.test_config['wallet_management']['num_wallets']
        
        # Test wallet rotation
        wallet1 = await wallet_mgr.get_next_wallet()
        assert wallet1 is not None
        assert 'address' in wallet1
        assert 'private_key' in wallet1
        
        # Test jitter
        base_size = 300
        jittered_size = wallet_mgr.add_jitter_to_size(base_size)
        assert 240 <= jittered_size <= 360  # Within 20% jitter
        
        print(f"  Wallets created: {len(wallet_mgr.wallets)}")
        print(f"  Jittered size: {base_size} -> {jittered_size}")
        print("✅ Wallet Manager tests passed")
    
    async def test_ml_predictor(self):
        """Test ML predictor"""
        print("\n🧠 Testing ML Predictor...")
        
        predictor = MLPredictor(self.test_config['ml_prediction'])
        
        # Test feature extraction
        test_order = {
            'market_id': 'test',
            'spread': 0.01,
            'yes_order': {'price': 0.45, 'size': 300},
            'no_order': {'price': 0.55, 'size': 300},
            'category': 'sports',
            'reward': 500,
            'competition_bars': 2
        }
        
        features = predictor._extract_features(test_order)
        assert len(features) == 20, f"Expected 20 features, got {len(features)}"
        
        # Test prediction
        probability = await predictor.predict_fill(test_order)
        assert 0 <= probability <= 1, f"Probability {probability} out of range"
        
        print(f"  Features extracted: {len(features)}")
        print(f"  Fill probability: {probability:.2%}")
        print("✅ ML Predictor tests passed")
    
    async def test_position_monitor(self):
        """Test position monitor"""
        print("\n👁️ Testing Position Monitor...")
        
        monitor = PositionMonitor(self.test_config['monitoring'])
        
        # Test position tracking
        await monitor.update_position('test-market', {
            'status': 'open',
            'fill_percentage': 0.05
        })
        
        positions = await monitor.get_open_positions()
        assert len(positions) == 1
        
        # Test cancel conditions
        test_position = {
            'market_id': 'test-market',
            'created_at': datetime.now().timestamp() - 400,  # Old order
            'fill_percentage': 0.15  # Partial fill
        }
        
        should_cancel = await monitor.check_cancel_conditions(test_position)
        # Should cancel due to age or partial fill
        
        print(f"  Positions tracked: {len(positions)}")
        print(f"  Cancel decision: {should_cancel}")
        print("✅ Position Monitor tests passed")
    
    async def test_optimizer(self):
        """Test daily optimizer"""
        print("\n📈 Testing Daily Optimizer...")
        
        optimizer = DailyOptimizer(self.test_config)
        
        # Add test performance data
        optimizer.add_performance_record({
            'market_id': 'test-1',
            'category': 'sports',
            'filled': True,
            'pnl': 10,
            'spread': 0.01,
            'size': 300
        })
        
        # Test P&L calculation
        daily_pnl = await optimizer.calculate_daily_pnl()
        assert daily_pnl >= 0
        
        # Test optimization calculation
        performance = optimizer._default_performance()
        optimizations = optimizer._calculate_optimizations(performance)
        assert 'spread_adjustment' in optimizations
        
        print(f"  Daily P&L: ${daily_pnl:.2f}")
        print(f"  Optimizations: {list(optimizations.keys())}")
        print("✅ Daily Optimizer tests passed")
    
    def print_results(self):
        """Print test results summary"""
        print("\n" + "=" * 60)
        print("TEST RESULTS SUMMARY")
        print("=" * 60)
        
        passed = sum(1 for r in self.test_results if r['status'] == 'PASSED')
        failed = sum(1 for r in self.test_results if r['status'] == 'FAILED')
        
        for result in self.test_results:
            emoji = "✅" if result['status'] == 'PASSED' else "❌"
            print(f"{emoji} {result['test']}: {result['status']}")
            if result['status'] == 'FAILED' and 'error' in result:
                print(f"   Error: {result['error']}")
        
        print("\n" + "-" * 60)
        print(f"Total: {len(self.test_results)} | Passed: {passed} | Failed: {failed}")
        
        if failed == 0:
            print("\n🎉 ALL TESTS PASSED! Bot is ready for deployment.")
        else:
            print(f"\n⚠️ {failed} tests failed. Please fix issues before deployment.")
        
        # Save results
        with open('test_results.json', 'w') as f:
            json.dump(self.test_results, f, indent=2)
        print("\nTest results saved to test_results.json")


async def main():
    """Main test runner"""
    tester = BotTester()
    await tester.run_all_tests()


if __name__ == "__main__":
    print("""
    ╔══════════════════════════════════════════════╗
    ║     POLYMARKET BOT TEST SUITE v1.0           ║
    ║     Target: Top 1% Performance               ║
    ╚══════════════════════════════════════════════╝
    """)
    
    asyncio.run(main())