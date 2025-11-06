#!/usr/bin/env python3
"""
Pre-Live Trading Checklist
Kiểm tra toàn bộ bot trước khi chạy live với tiền thật
"""

import os
import sys
from dotenv import load_dotenv
from web3 import Web3
import yaml

# Colors for terminal
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'

def print_header(text):
    print(f"\n{BLUE}{'='*70}{RESET}")
    print(f"{BLUE}{text.center(70)}{RESET}")
    print(f"{BLUE}{'='*70}{RESET}\n")

def print_success(text):
    print(f"{GREEN}✅ {text}{RESET}")

def print_error(text):
    print(f"{RED}❌ {text}{RESET}")

def print_warning(text):
    print(f"{YELLOW}⚠️  {text}{RESET}")

def print_info(text):
    print(f"ℹ️  {text}")


def check_environment():
    """Check environment variables"""
    print_header("1. ENVIRONMENT VARIABLES")
    
    load_dotenv()
    
    # Check USE_DEMO_WALLETS
    use_demo = os.getenv('USE_DEMO_WALLETS', 'false').lower() == 'true'
    if use_demo:
        print_error("USE_DEMO_WALLETS=true - Bot đang dùng demo wallets!")
        print_info("Đổi thành: USE_DEMO_WALLETS=false")
        return False
    else:
        print_success("USE_DEMO_WALLETS=false - Sử dụng real wallets")
    
    # Check RPC URL
    rpc_url = os.getenv('POLYGON_RPC_URL')
    if rpc_url:
        print_success(f"POLYGON_RPC_URL configured")
    else:
        print_warning("No custom RPC URL (using default)")
    
    return True


def check_wallets():
    """Check wallet configuration"""
    print_header("2. WALLET CONFIGURATION")
    
    load_dotenv()
    
    wallet_count = 0
    for i in range(1, 11):
        pk = os.getenv(f'WALLET_{i}_PK')
        if pk:
            wallet_count += 1
            print_success(f"WALLET_{i}_PK configured")
    
    if wallet_count == 0:
        print_error("NO WALLETS CONFIGURED!")
        print_info("Add WALLET_1_PK=0x... to .env")
        return False
    
    print_success(f"Total wallets: {wallet_count}")
    
    if wallet_count < 2:
        print_warning("Recommended: At least 2 wallets for better distribution")
    
    return True


def check_wallet_balances():
    """Check wallet balances"""
    print_header("3. WALLET BALANCES")
    
    load_dotenv()
    
    rpc_url = os.getenv('POLYGON_RPC_URL', 'https://polygon-rpc.com')
    w3 = Web3(Web3.HTTPProvider(rpc_url))
    
    if not w3.is_connected():
        print_error("Cannot connect to Polygon RPC")
        return False
    
    print_success("Connected to Polygon RPC")
    
    # USDC contract
    USDC_ADDRESS = '0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174'
    USDC_ABI = [
        {
            "constant": True,
            "inputs": [{"name": "_owner", "type": "address"}],
            "name": "balanceOf",
            "outputs": [{"name": "balance", "type": "uint256"}],
            "type": "function"
        }
    ]
    
    usdc_contract = w3.eth.contract(address=USDC_ADDRESS, abi=USDC_ABI)
    
    total_usdc = 0
    total_matic = 0
    
    for i in range(1, 11):
        pk = os.getenv(f'WALLET_{i}_PK')
        if not pk:
            continue
        
        try:
            from eth_account import Account
            if not pk.startswith('0x'):
                pk = '0x' + pk
            account = Account.from_key(pk)
            address = account.address
            
            # Check MATIC
            matic_balance = w3.eth.get_balance(address)
            matic_eth = w3.from_wei(matic_balance, 'ether')
            
            # Check USDC
            usdc_balance = usdc_contract.functions.balanceOf(address).call()
            usdc = usdc_balance / 1e6
            
            total_usdc += usdc
            total_matic += float(matic_eth)
            
            print_info(f"Wallet {i}: {usdc:.2f} USDC, {matic_eth:.4f} MATIC")
            
            if usdc < 10:
                print_warning(f"  Low USDC balance (< $10)")
            if matic_eth < 0.1:
                print_warning(f"  Low MATIC balance (< 0.1 for gas)")
        
        except Exception as e:
            print_error(f"Error checking wallet {i}: {e}")
            return False
    
    print_success(f"Total: {total_usdc:.2f} USDC, {total_matic:.4f} MATIC")
    
    if total_usdc < 50:
        print_warning("Total USDC < $50 - Consider adding more capital")
    
    if total_matic < 0.5:
        print_warning("Total MATIC < 0.5 - May not be enough for gas fees")
    
    return True


def check_config():
    """Check configuration file"""
    print_header("4. CONFIGURATION")
    
    try:
        with open('config.yaml', 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
    except Exception as e:
        print_error(f"Cannot load config.yaml: {e}")
        return False
    
    print_success("config.yaml loaded")
    
    # Check test mode
    test_mode = config.get('development', {}).get('test_mode', True)
    if test_mode:
        print_error("test_mode=true - Bot will NOT place real orders!")
        print_info("Set test_mode: false in config.yaml")
        return False
    else:
        print_success("test_mode=false - Real trading enabled")
    
    # Check paper trading
    paper_trading = config.get('development', {}).get('paper_trading', True)
    if paper_trading:
        print_error("paper_trading=true - Bot will NOT place real orders!")
        print_info("Set paper_trading: false in config.yaml")
        return False
    else:
        print_success("paper_trading=false - Real trading enabled")
    
    # Check risk limits
    max_capital = config.get('risk_management', {}).get('max_capital_per_market', 0.05)
    print_info(f"Max capital per market: {max_capital*100}%")
    
    if max_capital > 0.1:
        print_warning("Max capital per market > 10% - High risk!")
    
    return True


def check_dependencies():
    """Check Python dependencies"""
    print_header("5. DEPENDENCIES")
    
    required = [
        'web3',
        'eth_account',
        'aiohttp',
        'playwright',
        'py_clob_client',
        'yaml',
        'dotenv'
    ]
    
    missing = []
    for package in required:
        try:
            __import__(package.replace('-', '_'))
            print_success(f"{package} installed")
        except ImportError:
            print_error(f"{package} NOT installed")
            missing.append(package)
    
    if missing:
        print_error(f"Missing packages: {', '.join(missing)}")
        print_info("Run: pip install -r requirements.txt")
        return False
    
    return True


def main():
    """Run all checks"""
    print_header("🔍 PRE-LIVE TRADING CHECKLIST")
    print_warning("This will check if your bot is ready for LIVE TRADING with REAL MONEY")
    print()
    
    checks = [
        ("Environment Variables", check_environment),
        ("Wallet Configuration", check_wallets),
        ("Wallet Balances", check_wallet_balances),
        ("Configuration File", check_config),
        ("Dependencies", check_dependencies)
    ]
    
    results = []
    for name, check_func in checks:
        try:
            result = check_func()
            results.append((name, result))
        except Exception as e:
            print_error(f"Error in {name}: {e}")
            results.append((name, False))
    
    # Summary
    print_header("📊 SUMMARY")
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for name, result in results:
        if result:
            print_success(f"{name}: PASSED")
        else:
            print_error(f"{name}: FAILED")
    
    print()
    print(f"Results: {passed}/{total} checks passed")
    
    if passed == total:
        print()
        print_success("✅ ALL CHECKS PASSED!")
        print_success("Bot is ready for LIVE TRADING")
        print()
        print_warning("⚠️  FINAL WARNINGS:")
        print_warning("  1. Start with SMALL capital ($50-100)")
        print_warning("  2. Monitor CLOSELY for first few hours")
        print_warning("  3. Check logs frequently")
        print_warning("  4. Have stop-loss ready")
        print_warning("  5. You can lose money - trade at your own risk!")
        print()
        print_info("To start: python main.py")
    else:
        print()
        print_error("❌ SOME CHECKS FAILED!")
        print_error("Fix the issues above before running live")
        print()
        sys.exit(1)


if __name__ == "__main__":
    main()

