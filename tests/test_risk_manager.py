"""
Unit tests for RiskManager
"""

import unittest
import asyncio
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from risk_manager import RiskManager


class TestRiskManager(unittest.TestCase):
    """Test RiskManager functionality"""

    def setUp(self):
        """Set up test fixtures"""
        self.config = {
            'max_capital_per_market': 0.05,  # 5%
            'max_total_exposure': 0.3,  # 30%
            'enable_hedging': True,
            'hedge_threshold': 0.7,
            'stop_loss_percentage': 0.15
        }

        self.total_capital = 1000  # $1000 USDC

    def test_initialization(self):
        """Test RiskManager initialization"""
        manager = RiskManager(self.config)

        # Check basic initialization
        self.assertIsNotNone(manager.config)
        self.assertIsInstance(manager.allocated_capital, dict)
        self.assertIsInstance(manager.market_exposures, dict)
        self.assertIsInstance(manager.hedging_positions, dict)
    
    def test_calculate_required_capital(self):
        """Test capital requirement calculation"""
        manager = RiskManager(self.config)

        market = {'id': 'test-market-1', 'category': 'sports'}
        required = manager._calculate_required_capital(market)

        # Should return positive capital requirement
        self.assertGreater(required, 0)

    def test_check_market_limit(self):
        """Test market limit checking"""
        manager = RiskManager(self.config)
        manager.total_capital = self.total_capital

        market = {
            'id': 'test-market-1',
            'category': 'sports',
            'reward': 100
        }

        # Run async test
        async def test():
            can_trade = await manager.check_market_limit(market)
            # Should be able to trade (within limits)
            self.assertIsInstance(can_trade, bool)

        asyncio.run(test())
    
    def test_check_hedging_needed(self):
        """Test hedging detection"""
        manager = RiskManager(self.config)
        manager.total_capital = self.total_capital

        # Check if hedging is needed
        needs_hedging = manager._check_hedging_needed()

        # Should return boolean
        self.assertIsInstance(needs_hedging, bool)

    def test_calculate_hedge_params(self):
        """Test hedge parameter calculation"""
        manager = RiskManager(self.config)

        position = {
            'yes_exposure': 500,
            'no_exposure': 200,
            'market_id': 'test-market-1'
        }

        hedge_params = manager._calculate_hedge_params(position)

        # Should return hedge parameters or None
        if hedge_params:
            self.assertIn('side', hedge_params)
            self.assertIn('size', hedge_params)

    def test_portfolio_risk_calculation(self):
        """Test portfolio risk metrics"""
        manager = RiskManager(self.config)

        # Run async test
        async def test():
            risk_metrics = await manager.calculate_portfolio_risk()

            # Should return dict with metrics
            self.assertIsInstance(risk_metrics, dict)
            self.assertIn('needs_hedging', risk_metrics)

        asyncio.run(test())

    def test_capital_allocation(self):
        """Test capital allocation tracking"""
        manager = RiskManager(self.config)

        # Add allocation
        manager.allocated_capital['market-1'] = 100
        manager.allocated_capital['market-2'] = 150

        # Check total
        total = sum(manager.allocated_capital.values())
        self.assertEqual(total, 250)

    def test_market_exposures(self):
        """Test market exposure tracking"""
        manager = RiskManager(self.config)

        # Add exposure
        manager.market_exposures['market-1'] = {
            'yes_exposure': 100,
            'no_exposure': 50,
            'net_exposure': 50
        }

        # Check exposure exists
        self.assertIn('market-1', manager.market_exposures)
        self.assertEqual(manager.market_exposures['market-1']['net_exposure'], 50)


class TestRiskManagerEdgeCases(unittest.TestCase):
    """Test edge cases and error handling"""

    def test_zero_capital(self):
        """Test handling of zero capital"""
        config = {'max_capital_per_market': 0.05}
        manager = RiskManager(config)
        manager.total_capital = 0

        market = {'id': 'test', 'category': 'sports'}
        required = manager._calculate_required_capital(market)

        # Should still calculate requirement
        self.assertGreater(required, 0)

    def test_empty_allocations(self):
        """Test with no allocations"""
        config = {'max_capital_per_market': 0.05}
        manager = RiskManager(config)

        # Should have empty dicts
        self.assertEqual(len(manager.allocated_capital), 0)
        self.assertEqual(len(manager.market_exposures), 0)

    def test_correlation_check(self):
        """Test correlation limit checking"""
        config = {'max_capital_per_market': 0.05}
        manager = RiskManager(config)

        market = {
            'id': 'test-market-1',
            'category': 'sports',
            'question': 'Will team A win?'
        }

        # Check correlation
        result = manager._check_correlation_limits(market)

        # Should return boolean
        self.assertIsInstance(result, bool)


if __name__ == '__main__':
    unittest.main()

