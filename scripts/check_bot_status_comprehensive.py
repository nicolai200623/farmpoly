#!/usr/bin/env python3
"""
Comprehensive Bot Status Checker
=================================
Kiểm tra toàn diện trạng thái hoạt động của Polymarket Trading Bot

Chức năng:
1. Kiểm tra số dư ví (USDC, MATIC)
2. Kiểm tra USDC allowance cho CTF Exchange
3. Kiểm tra các lệnh đang hoạt động (pending/active orders)
4. Kiểm tra positions hiện tại
5. Kiểm tra rewards (nếu có)
6. Phân tích log để tìm vấn đề

Usage:
    python scripts/check_bot_status_comprehensive.py
"""

import os
import sys
import asyncio
import requests
from web3 import Web3
from eth_account import Account
from py_clob_client.client import ClobClient
from dotenv import load_dotenv
from datetime import datetime
import json

# Load environment variables
load_dotenv()

# Colors for terminal output
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_header(text):
    print(f"\n{Colors.HEADER}{Colors.BOLD}{'='*70}{Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}{text.center(70)}{Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}{'='*70}{Colors.ENDC}\n")

def print_success(text):
    print(f"{Colors.OKGREEN}✅ {text}{Colors.ENDC}")

def print_warning(text):
    print(f"{Colors.WARNING}⚠️  {text}{Colors.ENDC}")

def print_error(text):
    print(f"{Colors.FAIL}❌ {text}{Colors.ENDC}")

def print_info(text):
    print(f"{Colors.OKCYAN}ℹ️  {text}{Colors.ENDC}")

# Contract addresses on Polygon
USDC_ADDRESS = '0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174'  # USDC.e (Bridged)
CTF_EXCHANGE = '0x4bFb41d5B3570DeFd03C39a9A4D8dE6Bd8B8982E'  # Polymarket CTF Exchange

# ABIs
USDC_ABI = [
    {
        "constant": True,
        "inputs": [{"name": "_owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "balance", "type": "uint256"}],
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [
            {"name": "_owner", "type": "address"},
            {"name": "_spender", "type": "address"}
        ],
        "name": "allowance",
        "outputs": [{"name": "remaining", "type": "uint256"}],
        "type": "function"
    }
]

def get_wallet_info():
    """Get wallet private key and address from .env"""
    private_key = os.getenv('WALLET_1_PK')
    if not private_key:
        print_error("WALLET_1_PK not found in .env file")
        sys.exit(1)
    
    if not private_key.startswith('0x'):
        private_key = '0x' + private_key
    
    account = Account.from_key(private_key)
    return private_key, account.address

def check_wallet_balances(w3, wallet_address):
    """Check MATIC and USDC balances"""
    print_header("1. WALLET BALANCES")
    
    print_info(f"Wallet Address: {wallet_address}")
    print()
    
    # Check MATIC balance
    try:
        matic_balance = w3.eth.get_balance(wallet_address)
        matic_eth = w3.from_wei(matic_balance, 'ether')
        print(f"   MATIC Balance: {matic_eth:.4f} MATIC")
        
        if matic_eth < 0.1:
            print_warning(f"   Low MATIC balance! Recommended: at least 0.5 MATIC for gas")
        else:
            print_success(f"   MATIC balance is sufficient")
    except Exception as e:
        print_error(f"Failed to check MATIC balance: {e}")
        matic_eth = 0
    
    # Check USDC balance
    try:
        usdc_contract = w3.eth.contract(address=USDC_ADDRESS, abi=USDC_ABI)
        usdc_balance_raw = usdc_contract.functions.balanceOf(wallet_address).call()
        usdc_balance = usdc_balance_raw / 1e6  # USDC has 6 decimals
        
        print(f"   USDC.e Balance: ${usdc_balance:.2f}")
        
        if usdc_balance < 10:
            print_warning(f"   Low USDC balance! Recommended: at least $50-100 for trading")
        else:
            print_success(f"   USDC balance is sufficient for trading")
    except Exception as e:
        print_error(f"Failed to check USDC balance: {e}")
        usdc_balance = 0
    
    return matic_eth, usdc_balance

def check_usdc_allowance(w3, wallet_address):
    """Check USDC allowance for CTF Exchange"""
    print_header("2. USDC ALLOWANCE")
    
    try:
        usdc_contract = w3.eth.contract(address=USDC_ADDRESS, abi=USDC_ABI)
        allowance_raw = usdc_contract.functions.allowance(wallet_address, CTF_EXCHANGE).call()
        allowance = allowance_raw / 1e6  # USDC has 6 decimals
        
        print(f"   CTF Exchange: {CTF_EXCHANGE}")
        print(f"   Current Allowance: ${allowance:.2f} USDC")
        print()
        
        if allowance < 100:
            print_warning(f"   Low allowance! Bot may fail to place orders")
            print_info(f"   Run: python scripts/approve_ctf.py to increase allowance")
            print_info(f"   Recommended: Approve at least $1,000 USDC")
        elif allowance < 1000:
            print_warning(f"   Allowance is OK but low for production")
            print_info(f"   Recommended: Approve at least $1,000 USDC for production")
        else:
            print_success(f"   Allowance is sufficient")
        
        return allowance
    except Exception as e:
        print_error(f"Failed to check allowance: {e}")
        return 0

def check_active_orders(private_key, wallet_address):
    """Check active orders via CLOB API"""
    print_header("3. ACTIVE ORDERS")
    
    try:
        # Initialize CLOB client
        client = ClobClient(
            host="https://clob.polymarket.com",
            key=private_key,
            chain_id=137
        )
        
        # Set API credentials
        client.set_api_creds(client.create_or_derive_api_creds())
        
        # Get open orders
        print_info("Fetching open orders from CLOB...")
        orders = client.get_orders()
        
        if not orders:
            print_success("No active orders found")
            print_info("All USDC.e is available (not locked in orders)")
            return []
        
        print(f"\n   Found {len(orders)} active order(s):\n")
        
        total_locked = 0
        for i, order in enumerate(orders, 1):
            market_id = order.get('market', 'Unknown')
            side = order.get('side', 'Unknown')
            price = float(order.get('price', 0))
            size = float(order.get('original_size', 0))
            filled = float(order.get('size_matched', 0))
            remaining = size - filled
            
            locked_value = remaining * price
            total_locked += locked_value
            
            print(f"   Order #{i}:")
            print(f"      Market ID: {market_id}")
            print(f"      Side: {side.upper()}")
            print(f"      Price: ${price:.4f}")
            print(f"      Size: {remaining:.2f} shares (filled: {filled:.2f})")
            print(f"      Locked Value: ${locked_value:.2f}")
            print()
        
        print(f"   Total USDC Locked in Orders: ${total_locked:.2f}")
        print()
        
        if total_locked > 0:
            print_warning(f"You have ${total_locked:.2f} USDC locked in active orders")
            print_info(f"To cancel all orders, run: python scripts/close_positions.py")
        
        return orders
        
    except Exception as e:
        print_error(f"Failed to check orders: {e}")
        return []

def check_positions(wallet_address):
    """Check current positions via Data API"""
    print_header("4. CURRENT POSITIONS")
    
    try:
        # Use Polymarket Data API
        data_api_url = "https://data-api.polymarket.com/positions"
        params = {
            "user": wallet_address,
            "sizeThreshold": 0.01,
            "limit": 500
        }
        
        print_info("Fetching positions from Data API...")
        response = requests.get(data_api_url, params=params, timeout=10)
        response.raise_for_status()
        
        positions = response.json()
        
        if not positions:
            print_success("No active positions found")
            return []
        
        print(f"\n   Found {len(positions)} position(s):\n")
        
        total_value = 0
        total_pnl = 0
        
        for i, pos in enumerate(positions, 1):
            market = pos.get('market', {})
            title = market.get('question', 'Unknown Market')
            outcome = pos.get('outcome', 'Unknown')
            size = float(pos.get('size', 0))
            avg_price = float(pos.get('price', 0))
            current_price = float(pos.get('current_price', avg_price))
            
            position_value = size * avg_price
            current_value = size * current_price
            pnl = current_value - position_value
            pnl_pct = (pnl / position_value * 100) if position_value > 0 else 0
            
            total_value += position_value
            total_pnl += pnl
            
            print(f"   Position #{i}:")
            print(f"      Market: {title[:60]}")
            print(f"      Outcome: {outcome}")
            print(f"      Size: {size:.2f} shares @ ${avg_price:.4f}")
            print(f"      Current Price: ${current_price:.4f}")
            print(f"      P&L: ${pnl:.2f} ({pnl_pct:+.2f}%)")
            
            if pnl_pct > 0:
                print_success(f"      Status: PROFITABLE")
            elif pnl_pct < -10:
                print_error(f"      Status: LOSING")
            else:
                print_warning(f"      Status: NEUTRAL")
            print()
        
        print(f"   Total Position Value: ${total_value:.2f}")
        print(f"   Total P&L: ${total_pnl:.2f} ({(total_pnl/total_value*100) if total_value > 0 else 0:+.2f}%)")
        print()
        
        if total_pnl < -20:
            print_warning(f"You have significant losses. Consider reviewing your strategy.")
        elif total_pnl > 20:
            print_success(f"You have good profits! Consider taking some profits.")
        
        return positions
        
    except Exception as e:
        print_error(f"Failed to check positions: {e}")
        return []

def check_rewards(wallet_address):
    """Check Polymarket rewards (if available)"""
    print_header("5. POLYMARKET REWARDS")
    
    print_info("Checking rewards from Polymarket API...")
    print_warning("Note: Polymarket rewards API may not be publicly available")
    print()
    
    # Try multiple possible endpoints
    endpoints = [
        f"https://gamma-api.polymarket.com/rewards?address={wallet_address}",
        f"https://polymarket.com/api/rewards/{wallet_address}",
        f"https://clob.polymarket.com/rewards/{wallet_address}",
    ]
    
    for endpoint in endpoints:
        try:
            response = requests.get(endpoint, timeout=5)
            if response.status_code == 200:
                data = response.json()
                print_success(f"Found rewards data from: {endpoint}")
                print(json.dumps(data, indent=2))
                return data
        except:
            continue
    
    print_warning("Could not fetch rewards from any API endpoint")
    print_info("This is normal - Polymarket may not have a public rewards API")
    print_info("Check your rewards manually at: https://polymarket.com/rewards")
    
    return None

def analyze_log_file():
    """Analyze log file for recent errors"""
    print_header("6. LOG ANALYSIS")
    
    log_file = "log.md"
    if not os.path.exists(log_file):
        print_warning(f"Log file not found: {log_file}")
        return
    
    print_info(f"Analyzing {log_file}...")
    print()
    
    try:
        with open(log_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # Get last 100 lines
        recent_lines = lines[-100:]
        
        # Count errors
        errors = [line for line in recent_lines if 'ERROR' in line]
        warnings = [line for line in recent_lines if 'WARNING' in line]
        balance_errors = [line for line in recent_lines if 'not enough balance' in line]
        
        print(f"   Last 100 log lines:")
        print(f"      Errors: {len(errors)}")
        print(f"      Warnings: {len(warnings)}")
        print(f"      Balance Errors: {len(balance_errors)}")
        print()
        
        if balance_errors:
            print_error(f"Found {len(balance_errors)} 'not enough balance' errors!")
            print_info("This means bot is trying to place orders but doesn't have enough USDC")
            print_info("Solutions:")
            print_info("   1. Add more USDC to your wallet")
            print_info("   2. Increase USDC allowance: python scripts/approve_ctf.py")
            print()
        
        if errors:
            print_warning(f"Recent errors found. Last 3 errors:")
            for error in errors[-3:]:
                print(f"      {error.strip()[:100]}")
            print()
        
        if not errors and not warnings:
            print_success("No recent errors or warnings found!")
        
    except Exception as e:
        print_error(f"Failed to analyze log: {e}")

def main():
    """Main function"""
    print_header("POLYMARKET BOT STATUS CHECKER")
    print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Get wallet info
    private_key, wallet_address = get_wallet_info()
    
    # Initialize Web3
    rpc_url = os.getenv('POLYGON_RPC_URL', 'https://polygon-rpc.com')
    w3 = Web3(Web3.HTTPProvider(rpc_url))
    
    if not w3.is_connected():
        print_error("Failed to connect to Polygon RPC")
        sys.exit(1)
    
    # Run all checks
    matic_balance, usdc_balance = check_wallet_balances(w3, wallet_address)
    allowance = check_usdc_allowance(w3, wallet_address)
    orders = check_active_orders(private_key, wallet_address)
    positions = check_positions(wallet_address)
    rewards = check_rewards(wallet_address)
    analyze_log_file()
    
    # Summary
    print_header("SUMMARY")
    print(f"   Wallet: {wallet_address}")
    print(f"   MATIC: {matic_balance:.4f}")
    print(f"   USDC: ${usdc_balance:.2f}")
    print(f"   Allowance: ${allowance:.2f}")
    print(f"   Active Orders: {len(orders)}")
    print(f"   Positions: {len(positions)}")
    print()
    
    # Recommendations
    print_header("RECOMMENDATIONS")
    
    if usdc_balance < 10:
        print_error("Add more USDC to your wallet (minimum $50-100)")
    
    if allowance < 100:
        print_error("Increase USDC allowance: python scripts/approve_ctf.py")
    
    if matic_balance < 0.1:
        print_warning("Add more MATIC for gas fees (minimum 0.5 MATIC)")
    
    if not orders and not positions:
        print_info("Bot is not currently trading. Check if bot is running.")
    
    print()
    print_success("Status check complete!")

if __name__ == "__main__":
    main()

