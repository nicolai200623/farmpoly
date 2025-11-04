#!/usr/bin/env python3
"""
Verify that all fixes have been deployed correctly
Run this on VPS after deployment
"""

import os
import sys
import yaml
from pathlib import Path

# Colors for terminal output
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    END = '\033[0m'
    BOLD = '\033[1m'

def print_header(text):
    print(f"\n{Colors.CYAN}{Colors.BOLD}{'='*70}{Colors.END}")
    print(f"{Colors.CYAN}{Colors.BOLD}{text}{Colors.END}")
    print(f"{Colors.CYAN}{Colors.BOLD}{'='*70}{Colors.END}\n")

def print_success(text):
    print(f"{Colors.GREEN}✅ {text}{Colors.END}")

def print_error(text):
    print(f"{Colors.RED}❌ {text}{Colors.END}")

def print_warning(text):
    print(f"{Colors.YELLOW}⚠️  {text}{Colors.END}")

def print_info(text):
    print(f"{Colors.BLUE}ℹ️  {text}{Colors.END}")

def check_file_exists(filepath):
    """Check if file exists"""
    if not os.path.exists(filepath):
        print_error(f"File not found: {filepath}")
        return False
    print_success(f"File exists: {filepath}")
    return True

def check_code_fix(filepath, search_string, fix_name):
    """Check if a specific fix is present in code"""
    if not os.path.exists(filepath):
        print_error(f"{fix_name}: File not found - {filepath}")
        return False
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if search_string in content:
        print_success(f"{fix_name}: VERIFIED")
        return True
    else:
        print_error(f"{fix_name}: NOT FOUND!")
        print_warning(f"   Expected to find: {search_string}")
        return False

def check_config_value(config, path, expected_value, description):
    """Check if config has expected value"""
    keys = path.split('.')
    value = config
    
    try:
        for key in keys:
            value = value[key]
        
        if value == expected_value:
            print_success(f"{description}: {value} ✅")
            return True
        else:
            print_warning(f"{description}: {value} (expected: {expected_value})")
            return False
    except (KeyError, TypeError):
        print_error(f"{description}: NOT FOUND in config")
        return False

def main():
    print_header("🔍 DEPLOYMENT VERIFICATION")
    
    all_passed = True
    
    # Check 1: Verify Fix #10 (max_concurrent_markets)
    print_header("Fix #10: max_concurrent_markets")
    fix10_passed = check_code_fix(
        'market_selector.py',
        "market_selection_config = self.config.get('market_selection', {})",
        "Fix #10"
    )
    all_passed = all_passed and fix10_passed
    
    # Check 2: Verify Fix #11 (min_reward)
    print_header("Fix #11: min_reward")
    fix11_passed = check_code_fix(
        'market_scanner_v2.py',
        "scanner_config = config.get('market_scanner', {})",
        "Fix #11"
    )
    all_passed = all_passed and fix11_passed
    
    # Check 3: Verify Fix #12 (max_position_age)
    print_header("Fix #12: max_position_age")
    fix12_passed = check_code_fix(
        'position_monitor.py',
        "max_age = self.config.get('max_position_age'",
        "Fix #12"
    )
    all_passed = all_passed and fix12_passed
    
    # Check 4: Verify config.yaml values
    print_header("Fix #13: Config Values")
    
    try:
        with open('config.yaml', 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
        
        print_success("config.yaml loaded")
        print()
        
        # Check spread values
        spread_min = config.get('order_management', {}).get('spread_min', 0)
        spread_max = config.get('order_management', {}).get('spread_max', 0)
        
        if spread_min >= 0.03:
            print_success(f"spread_min: {spread_min} (≥ 0.03) ✅")
        else:
            print_error(f"spread_min: {spread_min} (should be ≥ 0.03)")
            all_passed = False
        
        if spread_max >= 0.08:
            print_success(f"spread_max: {spread_max} (≥ 0.08) ✅")
        else:
            print_error(f"spread_max: {spread_max} (should be ≥ 0.08)")
            all_passed = False
        
        # Check max_position_age
        max_age = config.get('monitoring', {}).get('max_position_age', 0)
        if max_age <= 1800:
            print_success(f"max_position_age: {max_age}s (≤ 30 min) ✅")
        else:
            print_warning(f"max_position_age: {max_age}s (recommended: ≤ 1800)")
        
        # Check partial_fill_threshold
        partial_fill = config.get('monitoring', {}).get('partial_fill_threshold', 0)
        if partial_fill <= 0.05:
            print_success(f"partial_fill_threshold: {partial_fill} (≤ 5%) ✅")
        else:
            print_warning(f"partial_fill_threshold: {partial_fill} (recommended: ≤ 0.05)")
        
        # Check min_reward
        min_reward = config.get('market_scanner', {}).get('min_reward', 0)
        print_info(f"min_reward: ${min_reward}")
        
        # Check max_concurrent_markets
        max_markets = config.get('market_selection', {}).get('max_concurrent_markets', 0)
        print_info(f"max_concurrent_markets: {max_markets}")
        
    except Exception as e:
        print_error(f"Failed to load config.yaml: {e}")
        all_passed = False
    
    # Check 5: Verify log file
    print_header("Log File Check")
    
    log_file = 'logs/polymarket_bot.log'
    if os.path.exists(log_file):
        print_success(f"Log file exists: {log_file}")
        
        # Read last 50 lines
        with open(log_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            last_lines = lines[-50:] if len(lines) > 50 else lines
        
        # Check for min_reward in logs
        min_reward_found = False
        for line in last_lines:
            if 'min_reward' in line.lower() or 'reward <' in line.lower():
                print_info(f"Found in log: {line.strip()}")
                min_reward_found = True
        
        if not min_reward_found:
            print_warning("No min_reward mentions in recent logs (bot may not have scanned yet)")
        
        # Check for "Selected X markets"
        selected_found = False
        for line in last_lines:
            if 'Selected' in line and 'market' in line:
                print_info(f"Found in log: {line.strip()}")
                selected_found = True
        
        if not selected_found:
            print_warning("No 'Selected X markets' in recent logs (bot may not have scanned yet)")
    else:
        print_warning(f"Log file not found: {log_file}")
        print_info("Bot may not have started yet")
    
    # Final summary
    print_header("VERIFICATION SUMMARY")
    
    if all_passed:
        print_success("ALL FIXES VERIFIED! ✅")
        print()
        print_info("Next steps:")
        print_info("  1. Monitor logs: tail -f logs/polymarket_bot.log")
        print_info("  2. Look for 'reward < $100' instead of 'reward < $300'")
        print_info("  3. Look for 'Selected 1 market' instead of 'Selected 3 markets'")
        return 0
    else:
        print_error("SOME FIXES NOT VERIFIED! ❌")
        print()
        print_warning("Action required:")
        print_warning("  1. Make sure you pulled the latest code: git pull origin master")
        print_warning("  2. Restart the bot: sudo systemctl restart farmpoly-bot")
        print_warning("  3. Run this script again to verify")
        return 1

if __name__ == "__main__":
    sys.exit(main())

