#!/usr/bin/env python3
"""
Test Telegram Bot Configuration
Sends a test message to verify Telegram alerts are working
"""

import asyncio
import aiohttp
import os
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', '')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID', '')


async def send_telegram_message(message: str):
    """Send a test message via Telegram"""
    try:
        if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
            print("❌ Telegram not configured!")
            print("   Please set TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID in .env")
            return False
        
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        
        data = {
            'chat_id': TELEGRAM_CHAT_ID,
            'text': message,
            'parse_mode': 'HTML'
        }
        
        print(f"📤 Sending test message to Telegram...")
        print(f"   Bot Token: {TELEGRAM_BOT_TOKEN[:20]}...")
        print(f"   Chat ID: {TELEGRAM_CHAT_ID}")
        
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=data) as response:
                if response.status == 200:
                    result = await response.json()
                    print(f"✅ Message sent successfully!")
                    print(f"   Message ID: {result.get('result', {}).get('message_id')}")
                    return True
                else:
                    error_text = await response.text()
                    print(f"❌ Failed to send message!")
                    print(f"   Status: {response.status}")
                    print(f"   Error: {error_text}")
                    return False
                    
    except Exception as e:
        print(f"❌ Error sending Telegram message: {e}")
        return False


async def get_bot_info():
    """Get information about the Telegram bot"""
    try:
        if not TELEGRAM_BOT_TOKEN:
            return None
        
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/getMe"
        
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    result = await response.json()
                    return result.get('result', {})
                else:
                    return None
                    
    except Exception as e:
        print(f"❌ Error getting bot info: {e}")
        return None


async def main():
    """Main test function"""
    print("=" * 60)
    print("TELEGRAM BOT CONFIGURATION TEST")
    print("=" * 60)
    print()
    
    # Check configuration
    print("1. CHECKING CONFIGURATION:")
    print("-" * 60)
    
    if not TELEGRAM_BOT_TOKEN:
        print("❌ TELEGRAM_BOT_TOKEN not set in .env")
        print()
        print("To fix:")
        print("1. Create a bot with @BotFather on Telegram")
        print("2. Copy the bot token")
        print("3. Add to .env: TELEGRAM_BOT_TOKEN=your_token_here")
        return
    else:
        print(f"✅ TELEGRAM_BOT_TOKEN: {TELEGRAM_BOT_TOKEN[:20]}...")
    
    if not TELEGRAM_CHAT_ID:
        print("❌ TELEGRAM_CHAT_ID not set in .env")
        print()
        print("To fix:")
        print("1. Send a message to your bot on Telegram")
        print("2. Visit: https://api.telegram.org/bot{TOKEN}/getUpdates")
        print("3. Find 'chat':{'id': YOUR_CHAT_ID}")
        print("4. Add to .env: TELEGRAM_CHAT_ID=your_chat_id")
        return
    else:
        print(f"✅ TELEGRAM_CHAT_ID: {TELEGRAM_CHAT_ID}")
    
    print()
    
    # Get bot info
    print("2. CHECKING BOT INFO:")
    print("-" * 60)
    
    bot_info = await get_bot_info()
    if bot_info:
        print(f"✅ Bot connected successfully!")
        print(f"   Bot Name: {bot_info.get('first_name', 'N/A')}")
        print(f"   Bot Username: @{bot_info.get('username', 'N/A')}")
        print(f"   Bot ID: {bot_info.get('id', 'N/A')}")
    else:
        print("❌ Could not connect to bot")
        print("   Check if TELEGRAM_BOT_TOKEN is correct")
        return
    
    print()
    
    # Send test message
    print("3. SENDING TEST MESSAGE:")
    print("-" * 60)
    
    test_message = f"""
🧪 <b>Telegram Test Message</b>
━━━━━━━━━━━━━━━━━━━━━━
⏰ Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
✅ Status: Telegram alerts are working!
━━━━━━━━━━━━━━━━━━━━━━

If you see this message, your Telegram bot is configured correctly! 🎉

The Polymarket bot will send alerts to this chat when:
• Bot starts/stops
• Orders are placed
• Errors occur
• Daily performance reports
    """
    
    success = await send_telegram_message(test_message.strip())
    
    print()
    
    # Summary
    print("=" * 60)
    print("SUMMARY:")
    print("=" * 60)
    
    if success:
        print("✅ Telegram alerts are working correctly!")
        print()
        print("Next steps:")
        print("1. Check your Telegram app for the test message")
        print("2. Run the bot: python main.py")
        print("3. You should receive a startup notification")
    else:
        print("❌ Telegram alerts are NOT working")
        print()
        print("Troubleshooting:")
        print("1. Check TELEGRAM_BOT_TOKEN is correct")
        print("2. Check TELEGRAM_CHAT_ID is correct")
        print("3. Make sure you've sent /start to the bot")
        print("4. Check bot has permission to send messages")
    
    print()


if __name__ == "__main__":
    asyncio.run(main())

