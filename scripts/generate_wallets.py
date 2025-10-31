#!/usr/bin/env python3
"""
Script to generate new Ethereum wallets for the bot
"""

import secrets
from eth_account import Account
import sys

def generate_wallet():
    """Generate a new Ethereum wallet"""
    # Generate random private key
    priv = secrets.token_hex(32)
    private_key = "0x" + priv
    
    # Create account from private key
    account = Account.from_key(private_key)
    
    return {
        'address': account.address,
        'private_key': private_key
    }

def main():
    """Main function"""
    print("=" * 70)
    print("Polymarket Bot - Wallet Generator")
    print("=" * 70)
    print()
    
    # Ask for number of wallets
    try:
        num_wallets = int(input("How many wallets do you want to generate? (recommended: 5-10): "))
        
        if num_wallets < 1:
            print("❌ Number of wallets must be at least 1")
            sys.exit(1)
        
        if num_wallets > 20:
            confirm = input(f"⚠️  {num_wallets} wallets is a lot. Are you sure? (y/n): ")
            if confirm.lower() != 'y':
                print("Cancelled.")
                sys.exit(0)
    
    except ValueError:
        print("❌ Invalid number")
        sys.exit(1)
    
    print()
    print(f"Generating {num_wallets} wallet(s)...")
    print()
    
    # Generate wallets
    wallets = []
    for i in range(num_wallets):
        wallet = generate_wallet()
        wallets.append(wallet)
        
        print(f"Wallet {i+1}:")
        print(f"  Address:     {wallet['address']}")
        print(f"  Private Key: {wallet['private_key']}")
        print()
    
    # Generate .env format
    print("=" * 70)
    print("ADD TO YOUR .env FILE:")
    print("=" * 70)
    print()
    
    private_keys = ','.join([w['private_key'] for w in wallets])
    print(f"WALLET_PRIVATE_KEYS={private_keys}")
    print()
    
    # Generate addresses list
    print("=" * 70)
    print("WALLET ADDRESSES (for funding):")
    print("=" * 70)
    print()
    
    for i, wallet in enumerate(wallets, 1):
        print(f"{i}. {wallet['address']}")
    
    print()
    
    # Important notes
    print("=" * 70)
    print("⚠️  IMPORTANT SECURITY NOTES:")
    print("=" * 70)
    print()
    print("1. NEVER share your private keys with anyone")
    print("2. NEVER commit .env file to git")
    print("3. Backup these private keys in a secure location")
    print("4. Fund each wallet with USDC and MATIC on Polygon network")
    print("5. Recommended: 10 MATIC + $1000-2000 USDC per wallet")
    print()
    
    # Save to file option
    save = input("Do you want to save this to a file? (y/n): ")
    if save.lower() == 'y':
        filename = input("Enter filename (default: wallets.txt): ").strip()
        if not filename:
            filename = "wallets.txt"
        
        try:
            with open(filename, 'w') as f:
                f.write("=" * 70 + "\n")
                f.write("Polymarket Bot - Generated Wallets\n")
                f.write("=" * 70 + "\n\n")
                
                for i, wallet in enumerate(wallets, 1):
                    f.write(f"Wallet {i}:\n")
                    f.write(f"  Address:     {wallet['address']}\n")
                    f.write(f"  Private Key: {wallet['private_key']}\n\n")
                
                f.write("=" * 70 + "\n")
                f.write(".env FORMAT:\n")
                f.write("=" * 70 + "\n\n")
                f.write(f"WALLET_PRIVATE_KEYS={private_keys}\n\n")
                
                f.write("=" * 70 + "\n")
                f.write("SECURITY WARNING:\n")
                f.write("=" * 70 + "\n\n")
                f.write("This file contains sensitive private keys!\n")
                f.write("- Keep it secure\n")
                f.write("- Never share it\n")
                f.write("- Delete after backing up to secure location\n")
            
            print(f"✅ Saved to {filename}")
            print(f"⚠️  Remember to delete this file after backing up!")
            
        except Exception as e:
            print(f"❌ Error saving file: {e}")
    
    print()
    print("Done! 🎉")
    print()

if __name__ == "__main__":
    main()

