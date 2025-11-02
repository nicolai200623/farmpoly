"""
Unit tests for USDCApprover
"""

import unittest
import asyncio
import sys
from unittest.mock import patch, MagicMock, AsyncMock
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from usdc_approver import USDCApprover, USDC_ADDRESS, CLOB_EXCHANGE_ADDRESS


class TestUSDCApprover(unittest.TestCase):
    """Test USDCApprover functionality"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.config = {
            'rpc_url': 'https://polygon-rpc.com'
        }
        
        self.test_wallet = {
            'address': '0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb',
            'private_key': '0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef'
        }
    
    @patch('usdc_approver.Web3')
    def test_initialization(self, mock_web3):
        """Test USDCApprover initialization"""
        # Mock Web3 connection
        mock_w3 = MagicMock()
        mock_w3.is_connected.return_value = True
        mock_web3.return_value = mock_w3
        
        approver = USDCApprover(self.config)
        
        # Should initialize Web3
        self.assertIsNotNone(approver.w3)
        self.assertIsNotNone(approver.usdc_contract)
    
    @patch('usdc_approver.Web3')
    def test_connection_failure(self, mock_web3):
        """Test handling of RPC connection failure"""
        # Mock failed connection
        mock_w3 = MagicMock()
        mock_w3.is_connected.return_value = False
        mock_web3.return_value = mock_w3
        
        with self.assertRaises(ConnectionError):
            USDCApprover(self.config)
    
    @patch('usdc_approver.Web3')
    def test_check_usdc_balance(self, mock_web3):
        """Test USDC balance checking"""
        # Mock Web3 and contract
        mock_w3 = MagicMock()
        mock_w3.is_connected.return_value = True
        mock_contract = MagicMock()
        mock_contract.functions.balanceOf.return_value.call.return_value = 100_000_000  # 100 USDC
        mock_w3.eth.contract.return_value = mock_contract
        mock_web3.return_value = mock_w3
        
        approver = USDCApprover(self.config)
        
        # Run async test
        async def test():
            balance = await approver.check_usdc_balance(self.test_wallet['address'])
            self.assertEqual(balance, 100.0)  # 100 USDC
        
        asyncio.run(test())
    
    @patch('usdc_approver.Web3')
    def test_check_matic_balance(self, mock_web3):
        """Test MATIC balance checking"""
        # Mock Web3
        mock_w3 = MagicMock()
        mock_w3.is_connected.return_value = True
        mock_w3.eth.get_balance.return_value = 500_000_000_000_000_000  # 0.5 MATIC
        mock_web3.return_value = mock_w3
        
        approver = USDCApprover(self.config)
        
        # Run async test
        async def test():
            balance = await approver.check_matic_balance(self.test_wallet['address'])
            self.assertEqual(balance, 0.5)  # 0.5 MATIC
        
        asyncio.run(test())
    
    @patch('usdc_approver.Web3')
    def test_get_allowance(self, mock_web3):
        """Test getting current USDC allowance"""
        # Mock Web3 and contract
        mock_w3 = MagicMock()
        mock_w3.is_connected.return_value = True
        mock_contract = MagicMock()
        mock_contract.functions.allowance.return_value.call.return_value = 10_000_000_000  # 10,000 USDC
        mock_w3.eth.contract.return_value = mock_contract
        mock_web3.return_value = mock_w3
        
        approver = USDCApprover(self.config)
        
        # Run async test
        async def test():
            allowance = await approver._get_allowance(self.test_wallet['address'])
            self.assertEqual(allowance, 10_000_000_000)
        
        asyncio.run(test())
    
    def test_usdc_address_constant(self):
        """Test USDC address constant"""
        self.assertEqual(USDC_ADDRESS, '0x3c499c542cEF5E3811e1192ce70d8cC03d5c3359')
    
    def test_clob_address_constant(self):
        """Test CLOB exchange address constant"""
        self.assertEqual(CLOB_EXCHANGE_ADDRESS, '0x4bFb41d5B3570DeFd03C39a9A4D8dE6Bd8B8982E')


class TestUSDCApproverIntegration(unittest.TestCase):
    """Integration tests for USDC approval flow"""
    
    @patch('usdc_approver.Web3')
    def test_check_and_approve_wallet_already_approved(self, mock_web3):
        """Test wallet that already has sufficient approval"""
        # Mock Web3 and contract
        mock_w3 = MagicMock()
        mock_w3.is_connected.return_value = True
        mock_contract = MagicMock()
        mock_contract.functions.allowance.return_value.call.return_value = 20_000_000_000  # 20,000 USDC
        mock_w3.eth.contract.return_value = mock_contract
        mock_web3.return_value = mock_w3
        
        approver = USDCApprover({'rpc_url': 'https://polygon-rpc.com'})
        
        wallet = {
            'address': '0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb',
            'private_key': '0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef'
        }
        
        # Run async test
        async def test():
            result = await approver.check_and_approve_wallet(wallet, 10000)
            self.assertTrue(result)  # Should return True (already approved)
        
        asyncio.run(test())


if __name__ == '__main__':
    unittest.main()

