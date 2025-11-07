#!/usr/bin/env python3
"""
Check Pending Markets
=====================
Kiểm tra các market mà bot đang cố gắng đặt lệnh

Phân tích log để tìm:
1. Market IDs mà bot đang cố đặt lệnh
2. Lý do thất bại (balance, allowance, etc.)
3. Thông tin chi tiết về các markets này

Usage:
    python scripts/check_pending_markets.py
"""

import re
import requests
from collections import Counter
from datetime import datetime

# Colors
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

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

def get_market_info(market_id):
    """Get market information from Gamma API"""
    try:
        # Try Gamma API first
        url = f"https://gamma-api.polymarket.com/markets/{market_id}"
        response = requests.get(url, timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            return {
                'question': data.get('question', 'Unknown'),
                'end_date': data.get('end_date_iso', 'Unknown'),
                'volume': data.get('volume', 0),
                'liquidity': data.get('liquidity', 0),
                'active': data.get('active', False)
            }
    except:
        pass
    
    # Try CLOB API
    try:
        url = f"https://clob.polymarket.com/markets/{market_id}"
        response = requests.get(url, timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            return {
                'question': data.get('question', 'Unknown'),
                'end_date': data.get('end_date', 'Unknown'),
                'volume': data.get('volume', 0),
                'liquidity': 0,
                'active': data.get('active', False)
            }
    except:
        pass
    
    return None

def analyze_log():
    """Analyze log file for pending markets"""
    print_header("ANALYZING LOG FILE")
    
    log_file = "log.md"
    
    try:
        with open(log_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        print_success(f"Loaded {log_file}")
        print()
        
        # Find all "Placing order for market" entries
        pattern = r'Placing order for market (\d+)'
        matches = re.findall(pattern, content)
        
        if not matches:
            print_warning("No pending orders found in log")
            return
        
        # Count occurrences
        market_counts = Counter(matches)
        
        print_info(f"Found {len(matches)} order placement attempts")
        print_info(f"Unique markets: {len(market_counts)}")
        print()
        
        # Find balance errors
        balance_errors = content.count("not enough balance / allowance")
        print_error(f"Balance/Allowance errors: {balance_errors}")
        print()
        
        # Show most attempted markets
        print_header("TOP MARKETS (Most Attempted)")
        
        for market_id, count in market_counts.most_common(10):
            print(f"\n{Colors.BOLD}Market ID: {market_id}{Colors.ENDC}")
            print(f"   Attempts: {count}")
            
            # Get market info
            info = get_market_info(market_id)
            if info:
                print(f"   Question: {info['question'][:60]}")
                print(f"   End Date: {info['end_date']}")
                volume = float(info['volume']) if info['volume'] else 0
                print(f"   Volume: ${volume:,.2f}")
                print(f"   Active: {info['active']}")
                
                if not info['active']:
                    print_warning("   Market is CLOSED!")
            else:
                print_warning("   Could not fetch market info")
        
        # Check for successful orders
        print_header("ORDER SUCCESS RATE")
        
        success_pattern = r'Order placed successfully: (0x[a-fA-F0-9]+)'
        successes = re.findall(success_pattern, content)
        
        print(f"   Total Attempts: {len(matches)}")
        print(f"   Successful: {len(successes)}")
        print(f"   Failed: {len(matches) - len(successes)}")
        
        if len(matches) > 0:
            success_rate = (len(successes) / len(matches)) * 100
            print(f"   Success Rate: {success_rate:.1f}%")
            
            if success_rate < 10:
                print_error("Very low success rate! Check balance and allowance")
            elif success_rate < 50:
                print_warning("Low success rate. May need more USDC or allowance")
            else:
                print_success("Good success rate")
        
        print()
        
        # Show recent successful orders
        if successes:
            print_header("RECENT SUCCESSFUL ORDERS")
            print_info(f"Last {min(5, len(successes))} successful order IDs:")
            for order_id in successes[-5:]:
                print(f"   {order_id}")
            print()
        
        # Recommendations
        print_header("RECOMMENDATIONS")
        
        if balance_errors > 100:
            print_error("Many balance/allowance errors detected!")
            print_info("Solutions:")
            print_info("   1. Check USDC balance: python scripts/check_wallets.py")
            print_info("   2. Increase allowance: python scripts/approve_ctf.py")
            print_info("   3. Add more USDC to wallet")
        
        if len(successes) == 0 and len(matches) > 10:
            print_error("No successful orders despite many attempts!")
            print_info("This indicates a critical issue:")
            print_info("   - Insufficient USDC balance")
            print_info("   - Insufficient USDC allowance")
            print_info("   - Wallet configuration issue")
            print_info("Run: python scripts/check_bot_status_comprehensive.py")
        
        # Check for specific markets
        if market_counts:
            most_common_market = market_counts.most_common(1)[0]
            if most_common_market[1] > 50:
                print_warning(f"Bot is stuck trying to place order for market {most_common_market[0]}")
                print_info("This market may have issues. Consider:")
                print_info("   1. Checking if market is still active")
                print_info("   2. Restarting the bot")
                print_info("   3. Checking market details manually")
        
    except FileNotFoundError:
        print_error(f"Log file not found: {log_file}")
    except Exception as e:
        print_error(f"Error analyzing log: {e}")

def check_market_details():
    """Interactive check for specific market"""
    print_header("CHECK SPECIFIC MARKET")
    
    try:
        market_id = input("Enter market ID to check (or press Enter to skip): ").strip()
        
        if not market_id:
            return
        
        print()
        print_info(f"Fetching details for market {market_id}...")
        
        info = get_market_info(market_id)
        
        if info:
            print()
            print(f"{Colors.BOLD}Market Details:{Colors.ENDC}")
            print(f"   Question: {info['question']}")
            print(f"   End Date: {info['end_date']}")
            print(f"   Volume: ${info['volume']:,.2f}")
            print(f"   Liquidity: ${info['liquidity']:,.2f}")
            print(f"   Active: {info['active']}")
            print()
            
            if not info['active']:
                print_error("This market is CLOSED!")
            else:
                print_success("Market is active")
            
            # Check if it's on rewards page
            print_info("Checking if market is on rewards page...")
            try:
                rewards_url = "https://polymarket.com/api/rewards/markets"
                params = {
                    'orderBy': 'market',
                    'position': 'DESC',
                    'nextCursor': 'MA==',
                    'requestPath': '/rewards/user/markets',
                }
                response = requests.get(rewards_url, params=params, timeout=10)
                if response.status_code == 200:
                    data = response.json()
                    markets = data.get('data', [])
                    found = any(m.get('id') == market_id for m in markets)
                    if found:
                        print_success("Market is on rewards page")
                    else:
                        print_warning("Market NOT found on rewards page")
            except:
                print_warning("Could not check rewards page")
        else:
            print_error("Could not fetch market information")
            print_info("Market may not exist or API is unavailable")
        
    except KeyboardInterrupt:
        print("\nSkipped")
    except Exception as e:
        print_error(f"Error: {e}")

def main():
    """Main function"""
    print_header("PENDING MARKETS CHECKER")
    print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    analyze_log()
    check_market_details()
    
    print()
    print_success("Analysis complete!")

if __name__ == "__main__":
    main()

