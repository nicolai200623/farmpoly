"""
Unit tests for Reward Manager
Tests automated reward checking and withdrawal functionality
"""

import unittest
import asyncio
from unittest.mock import Mock, patch, MagicMock, AsyncMock
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from reward_manager import RewardManager


class TestRewardManager(unittest.TestCase):
    """Test cases for RewardManager"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.config = {
            'rpc_url': 'https://polygon-rpc.com',
            'reward_management': {
                'enabled': True,
                'check_interval': 60,  # 1 minute for testing
                'min_withdrawal_threshold': 10.0,
                'max_gas_price': 500
            }
        }
        
        # Mock environment variables (using valid checksummed addresses)
        self.env_patcher = patch.dict('os.environ', {
            'POLYGON_RPC_URL': 'https://polygon-rpc.com',
            'REWARD_WITHDRAWAL_WALLET': '0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb0',
            'MIN_REWARD_THRESHOLD': '10.0',
            'REWARD_CHECK_INTERVAL': '60'
        })
        self.env_patcher.start()
    
    def tearDown(self):
        """Clean up after tests"""
        self.env_patcher.stop()
    
    def test_initialization(self):
        """Test reward manager initialization"""
        manager = RewardManager(self.config)
        
        # Check basic attributes
        self.assertIsNotNone(manager.w3)
        self.assertEqual(manager.min_withdrawal_threshold, 10.0)
        self.assertEqual(manager.check_interval, 60)
        self.assertIsNotNone(manager.withdrawal_wallet)
        
        # Check statistics initialized
        self.assertEqual(manager.stats['total_rewards_checked'], 0)
        self.assertEqual(manager.stats['total_withdrawals'], 0)
        self.assertEqual(manager.stats['total_withdrawn_amount'], 0.0)
    
    def test_initialization_without_withdrawal_wallet(self):
        """Test initialization without withdrawal wallet configured"""
        with patch.dict('os.environ', {'REWARD_WITHDRAWAL_WALLET': ''}):
            manager = RewardManager(self.config)
            self.assertEqual(manager.withdrawal_wallet, '')
    
    @patch('reward_manager.Web3')
    def test_web3_connection(self, mock_web3):
        """Test Web3 connection setup"""
        mock_web3_instance = MagicMock()
        mock_web3.return_value = mock_web3_instance
        mock_web3.HTTPProvider.return_value = MagicMock()
        
        manager = RewardManager(self.config)
        
        # Verify Web3 was initialized with correct RPC
        mock_web3.HTTPProvider.assert_called()
    
    def test_check_rewards_async(self):
        """Test async reward checking"""
        manager = RewardManager(self.config)

        # Mock wallets (using valid checksummed address)
        wallets = [
            {
                'address': '0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb0',
                'private_key': '0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef'
            }
        ]

        # Mock Web3 contract
        with patch.object(manager.w3.eth, 'contract') as mock_contract:
            mock_contract_instance = MagicMock()
            mock_balance_func = MagicMock()
            mock_balance_func.call.return_value = 50000000  # 50 USDC (6 decimals)
            mock_contract_instance.functions.balanceOf.return_value = mock_balance_func
            mock_contract.return_value = mock_contract_instance

            # Run async test
            async def test():
                rewards = await manager.check_rewards(wallets)
                # Check if address is in rewards (may be checksummed)
                self.assertTrue(len(rewards) > 0)
                # Get the actual balance value
                balance = list(rewards.values())[0]
                self.assertEqual(balance, 50.0)
                self.assertEqual(manager.stats['total_rewards_checked'], 1)

            asyncio.run(test())
    
    def test_withdrawal_threshold_check(self):
        """Test withdrawal threshold validation"""
        manager = RewardManager(self.config)

        wallet = {
            'address': '0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb0',
            'private_key': '0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef'
        }

        # Mock Web3 to return balance below threshold
        with patch.object(manager.w3.eth, 'contract') as mock_contract:
            mock_contract_instance = MagicMock()
            mock_balance_func = MagicMock()
            mock_balance_func.call.return_value = 5000000  # 5 USDC (below 10 threshold)
            mock_contract_instance.functions.balanceOf.return_value = mock_balance_func
            mock_contract.return_value = mock_contract_instance

            async def test():
                success, message = await manager.withdraw_rewards(wallet)
                self.assertFalse(success)
                self.assertIn('below threshold', message)

            asyncio.run(test())
    
    def test_no_withdrawal_wallet_configured(self):
        """Test withdrawal fails when no withdrawal wallet is configured"""
        with patch.dict('os.environ', {'REWARD_WITHDRAWAL_WALLET': ''}):
            manager = RewardManager(self.config)

            wallet = {
                'address': '0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb0',
                'private_key': '0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef'
            }

            async def test():
                success, message = await manager.withdraw_rewards(wallet)
                self.assertFalse(success)
                self.assertIn('No withdrawal wallet', message)

            asyncio.run(test())
    
    def test_statistics_tracking(self):
        """Test statistics are properly tracked"""
        manager = RewardManager(self.config)
        
        # Manually update stats
        manager.stats['total_withdrawals'] = 5
        manager.stats['total_withdrawn_amount'] = 125.50
        manager.stats['failed_withdrawals'] = 1
        
        stats = manager.get_statistics()
        
        self.assertEqual(stats['total_withdrawals'], 5)
        self.assertEqual(stats['total_withdrawn_amount'], 125.50)
        self.assertEqual(stats['failed_withdrawals'], 1)
    
    def test_usdc_contract_setup(self):
        """Test USDC contract is properly configured"""
        manager = RewardManager(self.config)
        
        # Check USDC address is set correctly (Polygon USDC)
        self.assertEqual(
            manager.usdc_address.lower(),
            '0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174'.lower()
        )
        
        # Check ABI has required functions
        abi_function_names = [item['name'] for item in manager.usdc_abi if 'name' in item]
        self.assertIn('balanceOf', abi_function_names)
        self.assertIn('transfer', abi_function_names)
    
    def test_async_initialize(self):
        """Test async initialization"""
        manager = RewardManager(self.config)
        
        with patch.object(manager.w3, 'is_connected', return_value=True):
            async def test():
                await manager.initialize()
                self.assertIsNotNone(manager.session)
            
            asyncio.run(test())
    
    def test_async_close(self):
        """Test async resource cleanup"""
        manager = RewardManager(self.config)
        
        async def test():
            # Initialize first
            await manager.initialize()
            self.assertIsNotNone(manager.session)
            
            # Then close
            await manager.close()
            self.assertIsNone(manager.session)
        
        asyncio.run(test())
    
    def test_invalid_withdrawal_wallet_address(self):
        """Test withdrawal fails with invalid wallet address"""
        with patch.dict('os.environ', {'REWARD_WITHDRAWAL_WALLET': 'invalid_address'}):
            manager = RewardManager(self.config)
            
            wallet = {
                'address': '0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb',
                'private_key': '0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef'
            }
            
            async def test():
                success, message = await manager.withdraw_rewards(wallet)
                self.assertFalse(success)
                self.assertIn('Invalid withdrawal wallet', message)
            
            asyncio.run(test())
    
    def test_check_interval_configuration(self):
        """Test check interval can be configured"""
        # Test with config
        manager1 = RewardManager(self.config)
        self.assertEqual(manager1.check_interval, 60)
        
        # Test with environment variable override
        with patch.dict('os.environ', {'REWARD_CHECK_INTERVAL': '7200'}):
            manager2 = RewardManager(self.config)
            self.assertEqual(manager2.check_interval, 7200)
    
    def test_min_threshold_configuration(self):
        """Test minimum threshold can be configured"""
        # Test with config
        manager1 = RewardManager(self.config)
        self.assertEqual(manager1.min_withdrawal_threshold, 10.0)
        
        # Test with environment variable override
        with patch.dict('os.environ', {'MIN_REWARD_THRESHOLD': '25.0'}):
            manager2 = RewardManager(self.config)
            self.assertEqual(manager2.min_withdrawal_threshold, 25.0)


class TestRewardManagerIntegration(unittest.TestCase):
    """Integration tests for RewardManager"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.config = {
            'rpc_url': 'https://polygon-rpc.com',
            'reward_management': {
                'enabled': True,
                'check_interval': 60,
                'min_withdrawal_threshold': 10.0
            }
        }
        
        self.env_patcher = patch.dict('os.environ', {
            'POLYGON_RPC_URL': 'https://polygon-rpc.com',
            'REWARD_WITHDRAWAL_WALLET': '0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb',
            'MIN_REWARD_THRESHOLD': '10.0'
        })
        self.env_patcher.start()
    
    def tearDown(self):
        """Clean up after tests"""
        self.env_patcher.stop()
    
    def test_full_reward_check_cycle(self):
        """Test complete reward checking cycle"""
        manager = RewardManager(self.config)

        wallets = [
            {
                'address': '0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb0',
                'private_key': '0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef'
            },
            {
                'address': '0x853d955aCEf822Db058eb8505911ED77F175b99e0',
                'private_key': '0xabcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890'
            }
        ]

        with patch.object(manager.w3.eth, 'contract') as mock_contract:
            mock_contract_instance = MagicMock()
            mock_balance_func = MagicMock()
            # Return different balances for different wallets
            mock_balance_func.call.side_effect = [25000000, 15000000]  # 25 and 15 USDC
            mock_contract_instance.functions.balanceOf.return_value = mock_balance_func
            mock_contract.return_value = mock_contract_instance

            async def test():
                rewards = await manager.check_rewards(wallets)

                # Verify both wallets were checked
                self.assertEqual(len(rewards), 2)
                self.assertGreater(sum(rewards.values()), 0)

            asyncio.run(test())


if __name__ == '__main__':
    unittest.main()

