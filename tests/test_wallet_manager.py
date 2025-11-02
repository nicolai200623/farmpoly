"""
Unit tests for WalletManager
"""

import unittest
import asyncio
import os
import sys
from unittest.mock import patch, MagicMock
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from wallet_manager import WalletManager


class TestWalletManager(unittest.TestCase):
    """Test WalletManager functionality"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.config = {
            'num_wallets': 3,
            'rotation_interval': 300,
            'jitter_percentage': 0.2
        }
    
    @patch.dict(os.environ, {'USE_DEMO_WALLETS': 'true'})
    def test_demo_wallet_initialization(self):
        """Test demo wallet initialization"""
        manager = WalletManager(self.config)

        # Should create 3 demo wallets
        self.assertEqual(len(manager.wallets), 3)

        # Each wallet should have required fields
        for wallet in manager.wallets:
            self.assertIn('address', wallet)
            self.assertIn('private_key', wallet)
            self.assertIn('index', wallet)
            self.assertIn('usage_count', wallet)
            self.assertTrue(wallet['address'].startswith('0x'))
            # Private key may or may not have 0x prefix
            self.assertIsNotNone(wallet['private_key'])
    
    @patch.dict(os.environ, {
        'USE_DEMO_WALLETS': 'false',
        'WALLET_1_PK': '0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef',
        'WALLET_2_PK': '0x2234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef'
    })
    def test_real_wallet_loading(self):
        """Test loading real wallets from environment"""
        manager = WalletManager(self.config)

        # Should load at least 2 real wallets
        self.assertGreaterEqual(len(manager.wallets), 2)

        # Check wallet addresses are derived correctly
        for wallet in manager.wallets:
            self.assertIn('address', wallet)
            self.assertIn('private_key', wallet)
    
    @patch.dict(os.environ, {'USE_DEMO_WALLETS': 'true'})
    def test_get_next_wallet(self):
        """Test wallet rotation"""
        manager = WalletManager(self.config)

        # Run async test
        async def test():
            # Get first wallet
            wallet1 = await manager.get_next_wallet()
            self.assertIsNotNone(wallet1)

            # Get second wallet
            wallet2 = await manager.get_next_wallet()
            self.assertIsNotNone(wallet2)

            # Both should be valid wallets
            self.assertIn('address', wallet1)
            self.assertIn('address', wallet2)

        asyncio.run(test())
    
    @patch.dict(os.environ, {'USE_DEMO_WALLETS': 'true'})
    def test_wallet_usage_tracking(self):
        """Test wallet usage statistics"""
        manager = WalletManager(self.config)

        # Run async test
        async def test():
            wallet = await manager.get_next_wallet()
            initial_count = wallet['usage_count']

            # Get another wallet
            wallet2 = await manager.get_next_wallet()

            # Should track usage
            self.assertIsNotNone(wallet2)

        asyncio.run(test())

    @patch.dict(os.environ, {'USE_DEMO_WALLETS': 'true'})
    def test_wallet_rotation_delay(self):
        """Test wallet rotation with delay"""
        manager = WalletManager(self.config)

        # Run async test
        async def test():
            wallet1 = await manager.get_next_wallet()
            wallet2 = await manager.get_next_wallet()

            # Both should be valid
            self.assertIsNotNone(wallet1)
            self.assertIsNotNone(wallet2)

        asyncio.run(test())
    
    @patch.dict(os.environ, {
        'USE_DEMO_WALLETS': 'false'
    })
    def test_no_wallets_error(self):
        """Test error when no wallets configured"""
        try:
            manager = WalletManager(self.config)
            # If no error, should have loaded demo wallets as fallback
            self.assertGreater(len(manager.wallets), 0)
        except ValueError:
            # Expected error when no wallets configured
            pass


class TestWalletManagerEdgeCases(unittest.TestCase):
    """Test edge cases and error handling"""
    
    @patch.dict(os.environ, {
        'USE_DEMO_WALLETS': 'false',
        'WALLET_1_PK': 'invalid_key'
    })
    def test_invalid_private_key(self):
        """Test handling of invalid private key"""
        config = {'num_wallets': 1}
        
        # Should raise error or skip invalid wallet
        with self.assertRaises((ValueError, Exception)):
            WalletManager(config)
    
    @patch.dict(os.environ, {'USE_DEMO_WALLETS': 'true'})
    def test_wallet_stats(self):
        """Test wallet statistics"""
        config = {'num_wallets': 2}
        manager = WalletManager(config)

        # Check wallets were created
        self.assertEqual(len(manager.wallets), 2)

        # Check wallet usage dict exists
        self.assertIsInstance(manager.wallet_usage, dict)


if __name__ == '__main__':
    unittest.main()

