"""
Unit tests for MarketScannerV2
"""

import unittest
import asyncio
import sys
from unittest.mock import patch, MagicMock, AsyncMock
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from market_scanner_v2 import MarketScannerV2


class TestMarketScannerV2(unittest.TestCase):
    """Test MarketScannerV2 functionality"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.config = {
            'min_reward': 50,
            'max_competition_bars': 2,
            'min_shares': 500
        }
        
        self.sample_api_market = {
            'id': 'test-market-1',
            'question': 'Will Bitcoin reach $100k?',
            'rewards': {'amount': 500},
            'competition_bars': 1,
            'min_shares': 300,
            'volume': 50000,
            'liquidity': 25000,
            'end_date': '2025-12-31'
        }
    
    def test_initialization(self):
        """Test scanner initialization"""
        scanner = MarketScannerV2(self.config)
        
        self.assertEqual(scanner.min_reward, 50)
        self.assertEqual(scanner.max_competition, 2)
        self.assertIsNone(scanner.browser)
    
    def test_parse_api_market_valid(self):
        """Test parsing valid API market data"""
        scanner = MarketScannerV2(self.config)
        
        market = scanner._parse_api_market(self.sample_api_market)
        
        self.assertIsNotNone(market)
        self.assertEqual(market['id'], 'test-market-1')
        self.assertEqual(market['reward'], 500)
        self.assertEqual(market['competition_bars'], 1)
        self.assertEqual(market['source'], 'gamma_api')
    
    def test_parse_api_market_no_reward(self):
        """Test parsing market with no reward"""
        scanner = MarketScannerV2(self.config)
        
        market_data = {
            'id': 'test-market-2',
            'question': 'Test question'
            # No rewards field
        }
        
        market = scanner._parse_api_market(market_data)
        
        self.assertIsNone(market)  # Should return None for markets without rewards
    
    def test_filter_markets_by_reward(self):
        """Test filtering markets by reward threshold"""
        scanner = MarketScannerV2(self.config)
        
        markets = [
            {'id': '1', 'reward': 100, 'competition_bars': 1, 'volume': 0, 'liquidity': 0},
            {'id': '2', 'reward': 30, 'competition_bars': 1, 'volume': 0, 'liquidity': 0},  # Below threshold
            {'id': '3', 'reward': 200, 'competition_bars': 1, 'volume': 0, 'liquidity': 0}
        ]
        
        filtered = scanner._filter_markets(markets)
        
        # Should filter out market with reward < 50
        self.assertEqual(len(filtered), 2)
        self.assertNotIn('2', [m['id'] for m in filtered])
    
    def test_filter_markets_by_competition(self):
        """Test filtering markets by competition level"""
        scanner = MarketScannerV2(self.config)
        
        markets = [
            {'id': '1', 'reward': 100, 'competition_bars': 1, 'volume': 0, 'liquidity': 0},
            {'id': '2', 'reward': 100, 'competition_bars': 3, 'volume': 0, 'liquidity': 0},  # Too competitive
            {'id': '3', 'reward': 100, 'competition_bars': 2, 'volume': 0, 'liquidity': 0}
        ]
        
        filtered = scanner._filter_markets(markets)
        
        # Should filter out market with competition > 2
        self.assertEqual(len(filtered), 2)
        self.assertNotIn('2', [m['id'] for m in filtered])
    
    def test_calculate_score(self):
        """Test market scoring algorithm"""
        scanner = MarketScannerV2(self.config)
        
        market = {
            'reward': 500,
            'competition_bars': 1,
            'volume': 50000,
            'liquidity': 25000
        }
        
        score = scanner._calculate_score(market)
        
        # Score should be positive
        self.assertGreater(score, 0)
        
        # Higher reward should give higher score
        market2 = market.copy()
        market2['reward'] = 1000
        score2 = scanner._calculate_score(market2)
        self.assertGreater(score2, score)
    
    def test_calculate_score_competition_penalty(self):
        """Test that competition reduces score"""
        scanner = MarketScannerV2(self.config)
        
        market1 = {'reward': 500, 'competition_bars': 0, 'volume': 0, 'liquidity': 0}
        market2 = {'reward': 500, 'competition_bars': 2, 'volume': 0, 'liquidity': 0}
        
        score1 = scanner._calculate_score(market1)
        score2 = scanner._calculate_score(market2)
        
        # More competition should reduce score
        self.assertGreater(score1, score2)
    
    @patch('market_scanner_v2.aiohttp.ClientSession')
    def test_fetch_gamma_api_success(self, mock_session_class):
        """Test successful API fetch"""
        scanner = MarketScannerV2(self.config)

        # Create proper async context manager mock
        mock_response = MagicMock()
        mock_response.status = 200
        mock_response.json = AsyncMock(return_value=[self.sample_api_market])

        # Mock the get() context manager
        mock_get_cm = MagicMock()
        mock_get_cm.__aenter__ = AsyncMock(return_value=mock_response)
        mock_get_cm.__aexit__ = AsyncMock(return_value=None)

        # Mock the session context manager
        mock_session = MagicMock()
        mock_session.get = MagicMock(return_value=mock_get_cm)

        mock_session_cm = MagicMock()
        mock_session_cm.__aenter__ = AsyncMock(return_value=mock_session)
        mock_session_cm.__aexit__ = AsyncMock(return_value=None)

        mock_session_class.return_value = mock_session_cm

        # Run async test
        async def test():
            markets = await scanner._fetch_gamma_api()
            self.assertIsInstance(markets, list)
            self.assertGreater(len(markets), 0)

        asyncio.run(test())
    
    @patch('market_scanner_v2.aiohttp.ClientSession')
    def test_fetch_gamma_api_failure(self, mock_session):
        """Test API fetch failure handling"""
        scanner = MarketScannerV2(self.config)
        
        # Mock failed API response
        mock_response = AsyncMock()
        mock_response.status = 500
        
        mock_session_instance = AsyncMock()
        mock_session_instance.get.return_value.__aenter__.return_value = mock_response
        mock_session.return_value.__aenter__.return_value = mock_session_instance
        
        # Run async test
        async def test():
            markets = await scanner._fetch_gamma_api()
            self.assertEqual(len(markets), 0)  # Should return empty list on failure
        
        asyncio.run(test())


class TestMarketScannerV2Sorting(unittest.TestCase):
    """Test market sorting and ranking"""
    
    def test_markets_sorted_by_score(self):
        """Test that filtered markets are sorted by score"""
        config = {'min_reward': 50, 'max_competition_bars': 3}
        scanner = MarketScannerV2(config)
        
        markets = [
            {'id': '1', 'reward': 100, 'competition_bars': 2, 'volume': 0, 'liquidity': 0},
            {'id': '2', 'reward': 500, 'competition_bars': 1, 'volume': 0, 'liquidity': 0},  # Best
            {'id': '3', 'reward': 200, 'competition_bars': 1, 'volume': 0, 'liquidity': 0}
        ]
        
        filtered = scanner._filter_markets(markets)
        
        # Should be sorted by score (highest first)
        self.assertEqual(filtered[0]['id'], '2')  # Highest reward, low competition


if __name__ == '__main__':
    unittest.main()

