#!/usr/bin/env python3
"""
Approve USDC for all wallets
Run this before starting the bot for the first time
"""

import sys
import os
import asyncio
import yaml
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from usdc_approver import USDCApprover
from wallet_manager import WalletManager
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


async def main():
    """Main approval function"""
    
    print("\n" + "="*60)
    print("🔐 USDC Approval Tool for Polymarket Trading")
    print("="*60 + "\n")
    
    # Load config
    try:
        with open('config.yaml', 'r') as f:
            config = yaml.safe_load(f)
    except Exception as e:
        logger.error(f"❌ Failed to load config.yaml: {e}")
        return
    
    # Initialize wallet manager
    try:
        wallet_manager = WalletManager(config)
        wallets = wallet_manager.wallets
        
        if not wallets:
            logger.error("❌ No wallets loaded! Check your .env file")
            return
        
        logger.info(f"✅ Loaded {len(wallets)} wallets\n")
        
    except Exception as e:
        logger.error(f"❌ Failed to load wallets: {e}")
        return
    
    # Initialize approver
    try:
        approver = USDCApprover(config)
    except Exception as e:
        logger.error(f"❌ Failed to initialize approver: {e}")
        return
    
    # Ask for approval amount
    print("\n💰 How much USDC should each wallet be approved for?")
    print("   Recommended: 10,000 USDC (allows trading without re-approval)")
    print("   Minimum: 1,000 USDC")
    
    try:
        amount_input = input("\nEnter amount (default 10000): ").strip()
        amount = float(amount_input) if amount_input else 10000
        
        if amount < 100:
            logger.error("❌ Amount too low! Minimum is 100 USDC")
            return
        
    except ValueError:
        logger.error("❌ Invalid amount")
        return
    
    # Confirm
    print(f"\n⚠️  You are about to approve {amount:,.0f} USDC for {len(wallets)} wallets")
    print("   This will cost gas fees (approximately 0.01 MATIC per wallet)")
    
    confirm = input("\nContinue? (yes/no): ").strip().lower()
    
    if confirm not in ['yes', 'y']:
        logger.info("❌ Cancelled by user")
        return
    
    # Approve all wallets
    print("\n" + "="*60)
    print("🚀 Starting approval process...")
    print("="*60 + "\n")
    
    results = await approver.approve_all_wallets(wallets, amount)
    
    # Print results
    print("\n" + "="*60)
    print("📊 APPROVAL RESULTS")
    print("="*60 + "\n")
    
    for wallet in wallets:
        address = wallet['address']
        status = "✅ APPROVED" if results.get(address) else "❌ FAILED"
        print(f"{status} - {address[:10]}...{address[-8:]}")
    
    approved = sum(1 for v in results.values() if v)
    total = len(results)
    
    print(f"\n{'='*60}")
    print(f"Total: {approved}/{total} wallets approved successfully")
    print(f"{'='*60}\n")
    
    if approved == total:
        print("✅ All wallets approved! You can now start trading.")
        print("   Run: python main.py")
    else:
        print("⚠️  Some wallets failed to approve.")
        print("   Check the logs above for errors.")
        print("   Common issues:")
        print("   - Insufficient MATIC for gas fees")
        print("   - Invalid private key")
        print("   - RPC connection issues")


if __name__ == "__main__":
    asyncio.run(main())

