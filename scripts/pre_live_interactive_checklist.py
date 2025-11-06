#!/usr/bin/env python3
"""
Interactive Pre-Live Checklist
Guides you through all steps needed before going live
"""

import os
import sys
import yaml
from web3 import Web3
from dotenv import load_dotenv

# Colors
class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    END = '\033[0m'

def print_header(text):
    print(f"\n{Colors.BOLD}{Colors.CYAN}{'='*80}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.CYAN}{text}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.CYAN}{'='*80}{Colors.END}\n")

def print_success(text):
    print(f"{Colors.GREEN}✅ {text}{Colors.END}")

def print_warning(text):
    print(f"{Colors.YELLOW}⚠️  {text}{Colors.END}")

def print_error(text):
    print(f"{Colors.RED}❌ {text}{Colors.END}")

def print_info(text):
    print(f"{Colors.BLUE}ℹ️  {text}{Colors.END}")

def ask_yes_no(question):
    """Ask yes/no question"""
    while True:
        response = input(f"{Colors.CYAN}{question} (y/n): {Colors.END}").lower().strip()
        if response in ['y', 'yes']:
            return True
        elif response in ['n', 'no']:
            return False
        else:
            print_warning("Please answer 'y' or 'n'")

def check_hardcoded_values():
    """Check if hardcoded values have been fixed"""
    print_header("STEP 1: CHECK HARDCODED VALUES")
    
    issues = []
    
    # Check order_manager.py
    try:
        with open('order_manager.py', 'r') as f:
            content = f.read()
        
        if 'self.clob_host' in content and 'self.chain_id' in content:
            print_success("order_manager.py: Uses config for CLOB settings")
        else:
            print_error("order_manager.py: Still has hardcoded CLOB settings")
            issues.append("order_manager.py needs fixing")
    except:
        print_error("order_manager.py: Cannot read file")
        issues.append("order_manager.py not found")
    
    # Check wallet_manager.py
    try:
        with open('wallet_manager.py', 'r') as f:
            content = f.read()
        
        if "config.get('rpc_url')" in content or "os.getenv('POLYGON_RPC_URL'" in content:
            print_success("wallet_manager.py: Uses config/env for RPC URL")
        else:
            print_error("wallet_manager.py: Still has hardcoded RPC URL")
            issues.append("wallet_manager.py needs fixing")
    except:
        print_error("wallet_manager.py: Cannot read file")
        issues.append("wallet_manager.py not found")
    
    if issues:
        print()
        print_warning("Found issues with hardcoded values!")
        print_info("Run: python scripts/fix_hardcoded_values.py")
        return False
    
    return True

def check_config_yaml():
    """Check config.yaml settings"""
    print_header("STEP 2: CHECK CONFIG.YAML")
    
    try:
        with open('config.yaml', 'r') as f:
            config = yaml.safe_load(f)
    except Exception as e:
        print_error(f"Cannot load config.yaml: {e}")
        return False
    
    issues = []
    
    # Check test mode
    test_mode = config.get('development', {}).get('test_mode', True)
    paper_trading = config.get('development', {}).get('paper_trading', True)
    
    if test_mode:
        print_error("test_mode is TRUE - Bot will NOT place real orders!")
        issues.append("Set test_mode: false")
    else:
        print_success("test_mode is FALSE - Real trading enabled")
    
    if paper_trading:
        print_error("paper_trading is TRUE - Only simulated trading!")
        issues.append("Set paper_trading: false")
    else:
        print_success("paper_trading is FALSE - Real trading enabled")
    
    # Check CLOB settings
    clob = config.get('clob', {})
    if clob.get('host') == 'https://clob.polymarket.com':
        print_success(f"CLOB host: {clob['host']} (Production)")
    else:
        print_warning(f"CLOB host: {clob.get('host', 'NOT SET')}")
    
    if clob.get('chain_id') == 137:
        print_success(f"Chain ID: {clob['chain_id']} (Polygon Mainnet)")
    else:
        print_error(f"Chain ID: {clob.get('chain_id', 'NOT SET')} (Should be 137)")
        issues.append("Set chain_id: 137")
    
    # Check capital
    capital = config.get('total_capital', 0)
    print_info(f"Total capital: ${capital} USDC")
    if capital < 50:
        print_warning("Capital is very low - consider at least $100")
    
    # Check spread
    spread_min = config.get('order_management', {}).get('spread_min', 0)
    spread_max = config.get('order_management', {}).get('spread_max', 0)
    print_info(f"Spread range: {spread_min:.3f} - {spread_max:.3f}")
    if spread_min < 0.03:
        print_warning("Spread might be too tight - risk of fills!")
    
    if issues:
        print()
        print_warning("Found issues in config.yaml:")
        for issue in issues:
            print(f"  - {issue}")
        return False
    
    return True

def check_wallet_balance():
    """Check wallet balances"""
    print_header("STEP 3: CHECK WALLET BALANCE")
    
    load_dotenv()
    
    # Get wallet
    private_key = os.getenv('WALLET_1_PK') or os.getenv('WALLET_1_PRIVATE_KEY')
    if not private_key:
        print_error("WALLET_1_PK not found in .env")
        return False
    
    # Get RPC
    rpc_url = os.getenv('POLYGON_RPC_URL', 'https://polygon-rpc.com')
    
    try:
        w3 = Web3(Web3.HTTPProvider(rpc_url))
        
        if not w3.is_connected():
            print_error("Cannot connect to Polygon RPC")
            return False
        
        # Get wallet address
        from eth_account import Account
        if private_key.startswith('0x'):
            private_key = private_key[2:]
        wallet_address = Account.from_key(private_key).address
        
        print_info(f"Wallet: {wallet_address}")
        
        # Check MATIC
        matic_balance = w3.eth.get_balance(wallet_address)
        matic_balance_eth = w3.from_wei(matic_balance, 'ether')
        
        if matic_balance_eth >= 0.5:
            print_success(f"MATIC balance: {matic_balance_eth:.4f} MATIC (sufficient for gas)")
        else:
            print_warning(f"MATIC balance: {matic_balance_eth:.4f} MATIC (might need more)")
        
        # Check USDC.e
        USDC_ADDRESS = '0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174'
        USDC_ABI = [{
            "constant": True,
            "inputs": [{"name": "_owner", "type": "address"}],
            "name": "balanceOf",
            "outputs": [{"name": "balance", "type": "uint256"}],
            "type": "function"
        }]
        
        usdc_contract = w3.eth.contract(address=USDC_ADDRESS, abi=USDC_ABI)
        usdc_balance_raw = usdc_contract.functions.balanceOf(wallet_address).call()
        usdc_balance = usdc_balance_raw / 1e6
        
        if usdc_balance >= 100:
            print_success(f"USDC.e balance: ${usdc_balance:,.2f} (sufficient)")
        elif usdc_balance >= 50:
            print_warning(f"USDC.e balance: ${usdc_balance:,.2f} (low but workable)")
        else:
            print_error(f"USDC.e balance: ${usdc_balance:,.2f} (too low!)")
            return False
        
        return True
        
    except Exception as e:
        print_error(f"Error checking balance: {e}")
        return False

def check_usdc_approval():
    """Check USDC approval"""
    print_header("STEP 4: CHECK USDC APPROVAL")
    
    print_info("Checking if USDC is approved for Polymarket Exchange...")
    
    load_dotenv()
    private_key = os.getenv('WALLET_1_PK') or os.getenv('WALLET_1_PRIVATE_KEY')
    rpc_url = os.getenv('POLYGON_RPC_URL', 'https://polygon-rpc.com')
    
    try:
        w3 = Web3(Web3.HTTPProvider(rpc_url))
        
        from eth_account import Account
        if private_key.startswith('0x'):
            private_key = private_key[2:]
        wallet_address = Account.from_key(private_key).address
        
        USDC_ADDRESS = '0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174'
        CLOB_EXCHANGE = '0x4bFb41d5B3570DeFd03C39a9A4D8dE6Bd8B8982E'
        
        USDC_ABI = [{
            "constant": True,
            "inputs": [
                {"name": "_owner", "type": "address"},
                {"name": "_spender", "type": "address"}
            ],
            "name": "allowance",
            "outputs": [{"name": "", "type": "uint256"}],
            "type": "function"
        }]
        
        usdc_contract = w3.eth.contract(address=USDC_ADDRESS, abi=USDC_ABI)
        allowance = usdc_contract.functions.allowance(wallet_address, CLOB_EXCHANGE).call()
        allowance_usdc = allowance / 1e6
        
        if allowance_usdc >= 1000:
            print_success(f"USDC approved: ${allowance_usdc:,.0f} (sufficient)")
            return True
        else:
            print_warning(f"USDC approved: ${allowance_usdc:,.0f} (need to approve)")
            print_info("Run: python scripts/approve_usdc.py")
            return False
        
    except Exception as e:
        print_error(f"Error checking approval: {e}")
        return False

def final_confirmation():
    """Final confirmation before going live"""
    print_header("FINAL CONFIRMATION")
    
    print(f"{Colors.BOLD}⚠️  YOU ARE ABOUT TO GO LIVE WITH REAL MONEY!{Colors.END}")
    print()
    print("Please confirm you understand:")
    print("  1. Bot will place REAL orders on Polymarket")
    print("  2. Orders can be FILLED and you may lose money")
    print("  3. You should monitor the bot closely for the first hour")
    print("  4. You can stop the bot anytime with Ctrl+C")
    print()
    
    if not ask_yes_no("Do you understand and want to proceed?"):
        print_error("Aborted by user")
        return False
    
    print()
    print_success("Confirmed! You're ready to go live!")
    return True

def main():
    print(f"{Colors.BOLD}{Colors.CYAN}")
    print("=" * 80)
    print("🚀 PRE-LIVE INTERACTIVE CHECKLIST")
    print("=" * 80)
    print(f"{Colors.END}")
    
    # Run checks
    checks = [
        ("Hardcoded values", check_hardcoded_values),
        ("Config.yaml", check_config_yaml),
        ("Wallet balance", check_wallet_balance),
        ("USDC approval", check_usdc_approval),
    ]
    
    all_passed = True
    
    for name, check_func in checks:
        try:
            if not check_func():
                all_passed = False
                print()
                print_error(f"{name} check FAILED!")
                print()
                if not ask_yes_no("Continue to next check?"):
                    print_error("Checklist aborted")
                    return 1
        except Exception as e:
            print_error(f"Error in {name} check: {e}")
            all_passed = False
    
    # Summary
    print_header("SUMMARY")
    
    if all_passed:
        print_success("ALL CHECKS PASSED!")
        print()
        
        if final_confirmation():
            print()
            print_header("READY TO GO LIVE!")
            print()
            print_info("To start the bot:")
            print(f"  {Colors.BOLD}python main.py{Colors.END}")
            print()
            print_info("Monitor with:")
            print("  - Telegram notifications")
            print("  - tail -f logs/polymarket_bot.log")
            print()
            return 0
        else:
            return 1
    else:
        print_error("SOME CHECKS FAILED!")
        print()
        print_info("Fix the issues above and run this script again:")
        print(f"  {Colors.BOLD}python scripts/pre_live_interactive_checklist.py{Colors.END}")
        print()
        return 1

if __name__ == '__main__':
    sys.exit(main())

