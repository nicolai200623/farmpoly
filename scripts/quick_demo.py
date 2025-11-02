#!/usr/bin/env python3
"""
Quick Demo Script
Run bot in demo mode for testing
"""

import os
import sys
import asyncio
from pathlib import Path
from dotenv import load_dotenv, set_key

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))


def setup_demo_env():
    """Setup demo environment"""
    env_file = Path('.env')
    
    # Create .env if not exists
    if not env_file.exists():
        print("📝 Creating .env file...")
        env_file.write_text("""# Demo Mode Configuration
USE_DEMO_WALLETS=true

# RPC URL (public)
POLYGON_RPC_URL=https://polygon-rpc.com

# Optional: Telegram alerts
TELEGRAM_BOT_TOKEN=
TELEGRAM_CHAT_ID=
""")
        print("✅ Created .env file")
    else:
        # Update existing .env
        print("📝 Updating .env for demo mode...")
        set_key('.env', 'USE_DEMO_WALLETS', 'true')
        print("✅ Updated .env file")
    
    load_dotenv()


def print_banner():
    """Print demo banner"""
    print("\n" + "="*70)
    print("🧪 POLYMARKET BOT - DEMO MODE".center(70))
    print("="*70)
    print("\n⚠️  DEMO MODE - No real trading!")
    print("   - Using virtual wallets")
    print("   - No real orders placed")
    print("   - Safe for testing\n")


async def run_demo():
    """Run demo"""
    print_banner()
    
    # Setup environment
    setup_demo_env()
    
    # Import main after env setup
    from main import main as bot_main
    
    print("🚀 Starting bot in demo mode...\n")
    
    try:
        await bot_main()
    except KeyboardInterrupt:
        print("\n\n⏹️  Demo stopped by user")
    except Exception as e:
        print(f"\n\n❌ Demo error: {e}")
        import traceback
        traceback.print_exc()


def main():
    """Main function"""
    print("\n🎯 Quick Demo Launcher")
    print("\nThis will:")
    print("  1. Setup demo environment")
    print("  2. Run bot with virtual wallets")
    print("  3. Show you how the bot works")
    print("\n⚠️  No real money involved!")
    
    response = input("\nContinue? (y/n): ").lower()
    
    if response != 'y':
        print("❌ Cancelled")
        return
    
    # Run demo
    asyncio.run(run_demo())


if __name__ == '__main__':
    main()

