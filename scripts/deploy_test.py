#!/usr/bin/env python3
"""
Deployment Test Script
Helps you test the bot step-by-step before going live
"""

import os
import sys
import asyncio
from pathlib import Path
from dotenv import load_dotenv
import yaml

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from wallet_manager import WalletManager
from usdc_approver import USDCApprover
from market_scanner_v2 import MarketScannerV2
from risk_manager import RiskManager


class DeploymentTester:
    """Test deployment step by step"""
    
    def __init__(self):
        self.config = self._load_config()
        self.passed_tests = []
        self.failed_tests = []
    
    def _load_config(self):
        """Load configuration"""
        with open('config.yaml', 'r') as f:
            return yaml.safe_load(f)
    
    def print_header(self, text):
        """Print section header"""
        print("\n" + "="*70)
        print(f"  {text}")
        print("="*70)
    
    def print_success(self, text):
        """Print success message"""
        print(f"✅ {text}")
        self.passed_tests.append(text)
    
    def print_error(self, text):
        """Print error message"""
        print(f"❌ {text}")
        self.failed_tests.append(text)
    
    def print_warning(self, text):
        """Print warning message"""
        print(f"⚠️  {text}")
    
    def print_info(self, text):
        """Print info message"""
        print(f"ℹ️  {text}")
    
    def test_environment(self):
        """Test 1: Check environment setup"""
        self.print_header("TEST 1: Environment Setup")
        
        # Check .env file
        if not os.path.exists('.env'):
            self.print_error(".env file not found")
            self.print_info("Run: cp .env.example .env")
            return False
        
        self.print_success(".env file exists")
        
        # Load environment
        load_dotenv()
        
        # Check demo mode
        use_demo = os.getenv('USE_DEMO_WALLETS', 'false').lower() == 'true'
        if use_demo:
            self.print_warning("Using DEMO wallets (safe for testing)")
        else:
            self.print_info("Using REAL wallets (be careful!)")
        
        # Check RPC URL
        rpc_url = os.getenv('POLYGON_RPC_URL')
        if rpc_url:
            self.print_success(f"RPC URL configured: {rpc_url[:50]}...")
        else:
            self.print_warning("No custom RPC URL (using default)")
        
        return True
    
    def test_dependencies(self):
        """Test 2: Check dependencies"""
        self.print_header("TEST 2: Dependencies")
        
        try:
            import web3
            self.print_success("web3.py installed")
        except ImportError:
            self.print_error("web3.py not installed")
            return False
        
        try:
            import aiohttp
            self.print_success("aiohttp installed")
        except ImportError:
            self.print_error("aiohttp not installed")
            return False
        
        try:
            from playwright.async_api import async_playwright
            self.print_success("playwright installed")
        except ImportError:
            self.print_error("playwright not installed")
            self.print_info("Run: pip install playwright && playwright install chromium")
            return False
        
        try:
            from py_clob_client.client import ClobClient
            self.print_success("py-clob-client installed")
        except ImportError:
            self.print_error("py-clob-client not installed")
            return False
        
        return True
    
    async def test_wallets(self):
        """Test 3: Check wallet setup"""
        self.print_header("TEST 3: Wallet Setup")
        
        try:
            manager = WalletManager(self.config)
            
            if len(manager.wallets) == 0:
                self.print_error("No wallets loaded")
                return False
            
            self.print_success(f"Loaded {len(manager.wallets)} wallets")
            
            # Get first wallet
            wallet = await manager.get_next_wallet()
            self.print_info(f"First wallet: {wallet['address'][:10]}...{wallet['address'][-8:]}")
            
            return True
            
        except Exception as e:
            self.print_error(f"Wallet setup failed: {e}")
            return False
    
    async def test_usdc_approval(self):
        """Test 4: Check USDC approval"""
        self.print_header("TEST 4: USDC Approval")

        load_dotenv()
        use_demo = os.getenv('USE_DEMO_WALLETS', 'false').lower() == 'true'

        if use_demo:
            self.print_warning("Skipping approval check (demo mode)")
            return True

        try:
            # Create config for approver
            approver_config = {
                'rpc_url': os.getenv('POLYGON_RPC_URL', 'https://polygon-rpc.com')
            }
            approver = USDCApprover(approver_config)

            self.print_success("USDC Approver initialized")
            self.print_info("To check balances, run: python scripts/check_wallets.py")
            self.print_info("To approve USDC, run: python scripts/approve_wallets.py")

            return True

        except Exception as e:
            self.print_error(f"Approval check failed: {e}")
            return False
    
    async def test_market_scanner(self):
        """Test 5: Check market scanner"""
        self.print_header("TEST 5: Market Scanner")
        
        try:
            scanner = MarketScannerV2(self.config['market_scanner'])
            
            self.print_info("Fetching markets from Gamma API...")
            markets = await scanner._fetch_gamma_api()
            
            if len(markets) > 0:
                self.print_success(f"Found {len(markets)} markets from API")
            else:
                self.print_warning("No markets found (API may be down)")
            
            return True
            
        except Exception as e:
            self.print_error(f"Market scanner failed: {e}")
            return False
    
    def test_risk_manager(self):
        """Test 6: Check risk manager"""
        self.print_header("TEST 6: Risk Manager")
        
        try:
            manager = RiskManager(self.config)
            
            self.print_success("Risk manager initialized")
            self.print_info(f"Total capital: ${manager.total_capital}")
            
            return True
            
        except Exception as e:
            self.print_error(f"Risk manager failed: {e}")
            return False
    
    def test_config(self):
        """Test 7: Check configuration"""
        self.print_header("TEST 7: Configuration")
        
        # Check capital
        capital = self.config.get('total_capital', 0)
        if capital > 0:
            self.print_success(f"Total capital: ${capital}")
            if capital < 100:
                self.print_warning("Capital is low (< $100)")
        else:
            self.print_error("Total capital not set")
            return False
        
        # Check dry run
        dry_run = self.config.get('dry_run', True)
        if dry_run:
            self.print_warning("DRY RUN mode enabled (no real orders)")
        else:
            self.print_info("LIVE mode enabled (REAL ORDERS!)")
        
        # Check market scanner
        scanner_config = self.config.get('market_scanner', {})
        min_reward = scanner_config.get('min_reward', 0)
        self.print_info(f"Min reward: ${min_reward}")
        
        # Check order management
        order_config = self.config.get('order_management', {})
        size_min = order_config.get('size_min', 0)
        size_max = order_config.get('size_max', 0)
        self.print_info(f"Order size: ${size_min}-${size_max}")
        
        return True
    
    async def run_all_tests(self):
        """Run all tests"""
        print("\n" + "🧪 DEPLOYMENT TEST SUITE".center(70))
        print("Testing bot setup before deployment...\n")
        
        # Run tests
        tests = [
            ("Environment", self.test_environment()),
            ("Dependencies", self.test_dependencies()),
            ("Wallets", await self.test_wallets()),
            ("USDC Approval", await self.test_usdc_approval()),
            ("Market Scanner", await self.test_market_scanner()),
            ("Risk Manager", self.test_risk_manager()),
            ("Configuration", self.test_config()),
        ]
        
        # Print summary
        self.print_header("TEST SUMMARY")
        
        passed = sum(1 for _, result in tests if result)
        total = len(tests)
        
        print(f"\n✅ Passed: {passed}/{total}")
        print(f"❌ Failed: {total - passed}/{total}")
        
        if passed == total:
            print("\n🎉 ALL TESTS PASSED! Bot is ready to deploy!")
            print("\nNext steps:")
            print("  1. Review config.yaml")
            print("  2. Start in demo mode: USE_DEMO_WALLETS=true python main.py")
            print("  3. Monitor logs: tail -f logs/polymarket_bot.log")
            print("  4. If demo works, switch to real mode")
        else:
            print("\n⚠️  SOME TESTS FAILED! Fix issues before deploying.")
            print("\nFailed tests:")
            for name, result in tests:
                if not result:
                    print(f"  - {name}")
        
        return passed == total


async def main():
    """Main function"""
    tester = DeploymentTester()
    success = await tester.run_all_tests()
    
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    asyncio.run(main())

