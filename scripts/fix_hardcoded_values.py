#!/usr/bin/env python3
"""
Script to fix hardcoded values in order_manager.py and wallet_manager.py
Converts hardcoded URLs and chain IDs to use config.yaml values
"""

import os
import sys
from pathlib import Path

# Colors for output
class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    END = '\033[0m'

def print_success(text):
    print(f"{Colors.GREEN}✅ {text}{Colors.END}")

def print_warning(text):
    print(f"{Colors.YELLOW}⚠️  {text}{Colors.END}")

def print_error(text):
    print(f"{Colors.RED}❌ {text}{Colors.END}")

def print_info(text):
    print(f"{Colors.BLUE}ℹ️  {text}{Colors.END}")

def backup_file(filepath):
    """Create backup of file before modifying"""
    backup_path = f"{filepath}.backup"
    
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        with open(backup_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print_success(f"Created backup: {backup_path}")
        return True
    else:
        print_error(f"File not found: {filepath}")
        return False

def fix_order_manager():
    """Fix hardcoded values in order_manager.py"""
    filepath = 'order_manager.py'
    
    print_info(f"Fixing {filepath}...")
    
    if not backup_file(filepath):
        return False
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Track changes
        changes = []
        
        # Fix 1: Add config reading in __init__
        if 'self.clob_host = ' not in content:
            # Add after self.telegram = telegram_notifier
            old_init = '        self.telegram = telegram_notifier  # Telegram notifier\n        self._initialize_clob()'
            new_init = '''        self.telegram = telegram_notifier  # Telegram notifier
        
        # Read CLOB settings from config
        clob_config = self.config.get('clob', {})
        self.clob_host = clob_config.get('host', 'https://clob.polymarket.com')
        self.chain_id = clob_config.get('chain_id', 137)
        
        self._initialize_clob()'''
            
            if old_init in content:
                content = content.replace(old_init, new_init)
                changes.append("Added CLOB config reading in __init__")
        
        # Fix 2: Use self.clob_host in _initialize_clob
        old_clob_init = '''            self.clob_client = ClobClient(
                host="https://clob.polymarket.com"
            )'''
        new_clob_init = '''            self.clob_client = ClobClient(
                host=self.clob_host
            )'''
        
        if old_clob_init in content:
            content = content.replace(old_clob_init, new_clob_init)
            changes.append("Fixed CLOB host in _initialize_clob()")
        
        # Fix 3: Use self.clob_host in get_order_book
        old_url = '                url = f"https://clob.polymarket.com/book?token_id={lookup_id}"'
        new_url = '                url = f"{self.clob_host}/book?token_id={lookup_id}"'
        
        if old_url in content:
            content = content.replace(old_url, new_url)
            changes.append("Fixed CLOB URL in get_order_book()")
        
        # Fix 4: Use self.clob_host and self.chain_id in place_order
        old_signing = '''            signing_client = ClobClient(
                host="https://clob.polymarket.com",
                key=wallet['private_key'],  # Add private key for signing
                chain_id=137  # Polygon mainnet chain ID
            )'''
        new_signing = '''            signing_client = ClobClient(
                host=self.clob_host,
                key=wallet['private_key'],  # Add private key for signing
                chain_id=self.chain_id  # From config
            )'''
        
        if old_signing in content:
            content = content.replace(old_signing, new_signing)
            changes.append("Fixed signing client in place_order()")
        
        # Write changes
        if changes:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print_success(f"Fixed {filepath}:")
            for change in changes:
                print(f"  - {change}")
            return True
        else:
            print_warning(f"No changes needed in {filepath}")
            return True
            
    except Exception as e:
        print_error(f"Error fixing {filepath}: {e}")
        return False

def fix_wallet_manager():
    """Fix hardcoded RPC URL in wallet_manager.py"""
    filepath = 'wallet_manager.py'
    
    print_info(f"Fixing {filepath}...")
    
    if not backup_file(filepath):
        return False
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Track changes
        changes = []
        
        # Fix: Use config for RPC URL
        old_w3_init = "        self.w3 = Web3(Web3.HTTPProvider('https://polygon-rpc.com'))"
        new_w3_init = """        # Get RPC URL from config or env
        rpc_url = self.config.get('rpc_url') or os.getenv('POLYGON_RPC_URL', 'https://polygon-rpc.com')
        self.w3 = Web3(Web3.HTTPProvider(rpc_url))"""
        
        if old_w3_init in content:
            content = content.replace(old_w3_init, new_w3_init)
            changes.append("Fixed RPC URL to use config/env")
            
            # Make sure os is imported
            if 'import os' not in content:
                # Add after other imports
                import_section = 'from web3 import Web3'
                content = content.replace(import_section, f'{import_section}\nimport os')
                changes.append("Added 'import os'")
        
        # Write changes
        if changes:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print_success(f"Fixed {filepath}:")
            for change in changes:
                print(f"  - {change}")
            return True
        else:
            print_warning(f"No changes needed in {filepath}")
            return True
            
    except Exception as e:
        print_error(f"Error fixing {filepath}: {e}")
        return False

def verify_config_yaml():
    """Verify config.yaml has required settings"""
    print_info("Verifying config.yaml...")
    
    try:
        import yaml
        
        with open('config.yaml', 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
        
        # Check CLOB settings
        clob = config.get('clob', {})
        if not clob.get('host'):
            print_error("config.yaml missing: clob.host")
            return False
        if not clob.get('chain_id'):
            print_error("config.yaml missing: clob.chain_id")
            return False
        
        print_success("config.yaml has required CLOB settings:")
        print(f"  - host: {clob['host']}")
        print(f"  - chain_id: {clob['chain_id']}")
        
        # Check RPC URL
        rpc_url = config.get('rpc_url')
        if rpc_url:
            print_success(f"config.yaml has RPC URL: {rpc_url[:50]}...")
        else:
            print_warning("config.yaml missing top-level rpc_url (will use env or default)")
        
        return True
        
    except Exception as e:
        print_error(f"Error reading config.yaml: {e}")
        return False

def main():
    print("=" * 80)
    print("🔧 FIX HARDCODED VALUES")
    print("=" * 80)
    print()
    
    # Verify we're in the right directory
    if not os.path.exists('config.yaml'):
        print_error("config.yaml not found! Run this script from the project root.")
        return 1
    
    # Verify config.yaml
    if not verify_config_yaml():
        print_error("config.yaml verification failed!")
        return 1
    
    print()
    
    # Fix files
    success = True
    
    if not fix_order_manager():
        success = False
    
    print()
    
    if not fix_wallet_manager():
        success = False
    
    print()
    print("=" * 80)
    
    if success:
        print_success("ALL FIXES APPLIED SUCCESSFULLY!")
        print()
        print_info("Backup files created:")
        print("  - order_manager.py.backup")
        print("  - wallet_manager.py.backup")
        print()
        print_info("Next steps:")
        print("  1. Review the changes in order_manager.py and wallet_manager.py")
        print("  2. Run: python pre_live_check.py")
        print("  3. If all checks pass, you're ready to go live!")
        return 0
    else:
        print_error("SOME FIXES FAILED!")
        print()
        print_info("Check the error messages above and fix manually if needed.")
        return 1

if __name__ == '__main__':
    sys.exit(main())

