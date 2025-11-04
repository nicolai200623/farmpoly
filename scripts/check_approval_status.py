#!/usr/bin/env python3
"""
Check USDC approval status for all wallets
Debug tool to verify approval is working correctly
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
    level=logging.DEBUG,  # Use DEBUG to see all details
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


async def main():
    """Check approval status for all wallets"""
    
    print("\n" + "="*80)
    print("🔍 USDC Approval Status Checker")
    print("="*80 + "\n")
    
    # Load config
    try:
        with open('config.yaml', 'r', encoding='utf-8') as f:
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
        import traceback
        traceback.print_exc()
        return
    
    # Initialize approver
    try:
        approver = USDCApprover(config)
        logger.info("✅ USDC Approver initialized\n")
    except Exception as e:
        logger.error(f"❌ Failed to initialize approver: {e}")
        import traceback
        traceback.print_exc()
        return
    
    # Check each wallet
    print("="*80)
    print("📊 CHECKING APPROVAL STATUS")
    print("="*80 + "\n")
    
    results = []
    
    for i, wallet in enumerate(wallets, 1):
        address = wallet['address']
        
        print(f"\n{'='*80}")
        print(f"Wallet {i}/{len(wallets)}: {address[:10]}...{address[-8:]}")
        print(f"{'='*80}")
        
        try:
            # Check USDC balance
            usdc_balance = await approver.check_usdc_balance(address)
            print(f"💰 USDC Balance: {usdc_balance:,.2f} USDC")
            
            # Check MATIC balance
            matic_balance = await approver.check_matic_balance(address)
            print(f"⛽ MATIC Balance: {matic_balance:.4f} MATIC")
            
            # Check allowance
            print(f"\n🔍 Checking USDC allowance...")
            allowance = await approver._get_allowance(address)
            allowance_usdc = allowance / 1e6
            
            print(f"   Raw allowance: {allowance} base units")
            print(f"   Allowance: {allowance_usdc:,.2f} USDC")
            
            # Determine status
            if allowance >= 1000 * 1e6:
                status = "✅ APPROVED"
                status_emoji = "✅"
            elif allowance > 0:
                status = "⚠️  PARTIALLY APPROVED"
                status_emoji = "⚠️"
            else:
                status = "❌ NOT APPROVED"
                status_emoji = "❌"
            
            print(f"\n{status_emoji} Status: {status}")

            # Check against test mode threshold (100 USDC)
            if allowance < 100 * 1e6:
                print(f"   ⚠️  Need to approve at least 100 USDC (test mode)")
                print(f"   Current: {allowance_usdc:,.2f} USDC")
                print(f"   Missing: {100 - allowance_usdc:,.2f} USDC")
            elif allowance < 1000 * 1e6:
                print(f"   ⚠️  Running in TEST MODE")
                print(f"   Current: {allowance_usdc:,.2f} USDC")
                print(f"   Recommended for production: 1,000 USDC")

            results.append({
                'address': address,
                'usdc_balance': usdc_balance,
                'matic_balance': matic_balance,
                'allowance': allowance_usdc,
                'status': status,
                'approved': allowance >= 100 * 1e6  # LOWERED to 100 USDC for testing
            })
            
        except Exception as e:
            logger.error(f"❌ Error checking wallet: {e}")
            import traceback
            traceback.print_exc()
            
            results.append({
                'address': address,
                'error': str(e),
                'approved': False
            })
    
    # Summary
    print("\n" + "="*80)
    print("📊 SUMMARY")
    print("="*80 + "\n")
    
    approved_count = sum(1 for r in results if r.get('approved', False))
    total_count = len(results)
    
    print(f"Total wallets: {total_count}")
    print(f"Approved: {approved_count}")
    print(f"Not approved: {total_count - approved_count}")
    
    print("\n" + "-"*80)
    print("Wallet Details:")
    print("-"*80)
    
    for i, result in enumerate(results, 1):
        if 'error' in result:
            print(f"{i}. {result['address'][:10]}... - ❌ ERROR: {result['error']}")
        else:
            status_emoji = "✅" if result['approved'] else "❌"
            print(f"{i}. {result['address'][:10]}... - {status_emoji} {result['allowance']:,.2f} USDC approved")
    
    print("\n" + "="*80)
    
    if approved_count == total_count:
        print("✅ ALL WALLETS APPROVED!")
        print("   Bot should work correctly.")
    elif approved_count > 0:
        print("⚠️  SOME WALLETS NOT APPROVED!")
        print(f"   {total_count - approved_count} wallet(s) need approval.")
        print("   Run: python scripts/approve_wallets.py")
    else:
        print("❌ NO WALLETS APPROVED!")
        print("   You MUST run: python scripts/approve_wallets.py")
        print("   Before starting the bot.")
    
    print("="*80 + "\n")
    
    # Recommendations
    print("💡 RECOMMENDATIONS:")
    print("-"*80)
    
    for result in results:
        if 'error' not in result:
            address_short = f"{result['address'][:10]}...{result['address'][-8:]}"
            
            issues = []
            
            if result['usdc_balance'] < 100:
                issues.append(f"⚠️  Low USDC balance ({result['usdc_balance']:.2f} USDC)")
            
            if result['matic_balance'] < 0.1:
                issues.append(f"⚠️  Low MATIC balance ({result['matic_balance']:.4f} MATIC)")
            
            if not result['approved']:
                issues.append(f"❌ Not approved (only {result['allowance']:.2f} USDC)")
            
            if issues:
                print(f"\n{address_short}:")
                for issue in issues:
                    print(f"  {issue}")
    
    print("\n" + "="*80)
    print("✅ Check complete!")
    print("="*80 + "\n")


if __name__ == "__main__":
    asyncio.run(main())

