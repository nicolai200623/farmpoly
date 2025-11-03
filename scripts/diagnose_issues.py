"""
Script chẩn đoán các vấn đề của bot
Kiểm tra:
1. Gamma API có hoạt động không
2. Webhook có chấp nhận POST requests không
3. Playwright timeout issues
4. Market filtering criteria
"""

import asyncio
import aiohttp
import sys
import os
from datetime import datetime

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv
load_dotenv()


class BotDiagnostics:
    """Chẩn đoán các vấn đề của bot"""
    
    def __init__(self):
        self.gamma_api_url = "https://gamma-api.polymarket.com/events"
        self.telegram_token = os.getenv('TELEGRAM_BOT_TOKEN', '')
        self.telegram_chat_id = os.getenv('TELEGRAM_CHAT_ID', '')
        self.discord_webhook = os.getenv('DISCORD_WEBHOOK_URL', '')
        self.slack_webhook = os.getenv('SLACK_WEBHOOK_URL', '')
        
        self.results = {
            'gamma_api': {'status': 'unknown', 'details': ''},
            'telegram': {'status': 'unknown', 'details': ''},
            'webhook': {'status': 'unknown', 'details': ''},
            'markets_found': 0,
            'markets_with_rewards': 0,
        }
    
    async def test_gamma_api(self):
        """Test Gamma API endpoint"""
        print("\n" + "="*60)
        print("🔍 TEST 1: GAMMA API")
        print("="*60)
        
        try:
            async with aiohttp.ClientSession() as session:
                params = {
                    'closed': 'false',
                    'order': 'id',
                    'ascending': 'false',
                    'limit': 100
                }
                
                print(f"📡 Đang gọi API: {self.gamma_api_url}")
                print(f"📋 Parameters: {params}")
                
                async with session.get(self.gamma_api_url, params=params, timeout=10) as response:
                    status = response.status
                    print(f"📊 HTTP Status: {status}")
                    
                    if status == 200:
                        data = await response.json()
                        
                        if isinstance(data, list):
                            total_events = len(data)
                            total_markets = 0
                            markets_with_rewards = 0
                            
                            print(f"✅ API hoạt động! Nhận được {total_events} events")
                            
                            # Phân tích chi tiết
                            for event in data[:5]:  # Chỉ xem 5 events đầu
                                event_markets = event.get('markets', [])
                                total_markets += len(event_markets)
                                
                                for market in event_markets:
                                    rewards_min_size = market.get('rewardsMinSize', 0)
                                    rewards_max_spread = market.get('rewardsMaxSpread', 0)
                                    
                                    if rewards_min_size > 0 or rewards_max_spread > 0:
                                        markets_with_rewards += 1
                            
                            self.results['markets_found'] = total_markets
                            self.results['markets_with_rewards'] = markets_with_rewards
                            
                            print(f"\n📈 Thống kê:")
                            print(f"   - Tổng events: {total_events}")
                            print(f"   - Tổng markets (5 events đầu): {total_markets}")
                            print(f"   - Markets có rewards: {markets_with_rewards}")
                            
                            # Hiển thị ví dụ market có rewards
                            if markets_with_rewards > 0:
                                print(f"\n✨ Ví dụ market có rewards:")
                                for event in data[:10]:
                                    for market in event.get('markets', []):
                                        if market.get('rewardsMinSize', 0) > 0:
                                            print(f"   - {market.get('question', 'Unknown')}")
                                            print(f"     Rewards Min Size: {market.get('rewardsMinSize')}")
                                            print(f"     Volume: ${market.get('volume', 0):,.0f}")
                                            print(f"     Liquidity: ${market.get('liquidity', 0):,.0f}")
                                            break
                                    if markets_with_rewards > 0:
                                        break
                            else:
                                print(f"\n⚠️  KHÔNG TÌM THẤY MARKET NÀO CÓ REWARDS!")
                                print(f"   Nguyên nhân có thể:")
                                print(f"   1. Polymarket tạm thời không có chương trình rewards")
                                print(f"   2. API không trả về đầy đủ thông tin rewards")
                                print(f"   3. Cần kiểm tra endpoint khác")
                            
                            self.results['gamma_api']['status'] = 'success'
                            self.results['gamma_api']['details'] = f"{total_events} events, {markets_with_rewards} markets with rewards"
                        else:
                            print(f"⚠️  API trả về dữ liệu không đúng format (không phải list)")
                            print(f"   Response type: {type(data)}")
                            self.results['gamma_api']['status'] = 'warning'
                            self.results['gamma_api']['details'] = 'Invalid response format'
                    else:
                        print(f"❌ API trả về lỗi: HTTP {status}")
                        text = await response.text()
                        print(f"   Response: {text[:200]}")
                        self.results['gamma_api']['status'] = 'error'
                        self.results['gamma_api']['details'] = f"HTTP {status}"
                        
        except asyncio.TimeoutError:
            print(f"❌ Timeout khi gọi API (>10s)")
            self.results['gamma_api']['status'] = 'error'
            self.results['gamma_api']['details'] = 'Timeout'
        except Exception as e:
            print(f"❌ Lỗi khi test API: {e}")
            self.results['gamma_api']['status'] = 'error'
            self.results['gamma_api']['details'] = str(e)
    
    async def test_telegram(self):
        """Test Telegram bot"""
        print("\n" + "="*60)
        print("📱 TEST 2: TELEGRAM BOT")
        print("="*60)
        
        if not self.telegram_token or not self.telegram_chat_id:
            print("⚠️  Telegram chưa được cấu hình trong .env")
            self.results['telegram']['status'] = 'not_configured'
            return
        
        try:
            url = f"https://api.telegram.org/bot{self.telegram_token}/sendMessage"
            
            message = f"""
🔧 <b>Bot Diagnostics Test</b>
━━━━━━━━━━━━━━━━━━━━━━
⏰ Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
📊 Status: Testing Telegram alerts
━━━━━━━━━━━━━━━━━━━━━━
This is a test message from diagnostics script.
            """
            
            data = {
                'chat_id': self.telegram_chat_id,
                'text': message.strip(),
                'parse_mode': 'HTML'
            }
            
            print(f"📡 Đang gửi test message tới Telegram...")
            print(f"   Bot Token: {self.telegram_token[:20]}...")
            print(f"   Chat ID: {self.telegram_chat_id}")
            
            async with aiohttp.ClientSession() as session:
                async with session.post(url, json=data) as response:
                    status = response.status
                    result = await response.json()
                    
                    if status == 200 and result.get('ok'):
                        print(f"✅ Telegram hoạt động tốt!")
                        print(f"   Message ID: {result.get('result', {}).get('message_id')}")
                        self.results['telegram']['status'] = 'success'
                        self.results['telegram']['details'] = 'Message sent successfully'
                    else:
                        print(f"❌ Telegram lỗi: {result}")
                        self.results['telegram']['status'] = 'error'
                        self.results['telegram']['details'] = str(result)
                        
        except Exception as e:
            print(f"❌ Lỗi khi test Telegram: {e}")
            self.results['telegram']['status'] = 'error'
            self.results['telegram']['details'] = str(e)
    
    async def test_webhook(self):
        """Test webhook (Discord/Slack)"""
        print("\n" + "="*60)
        print("🔗 TEST 3: WEBHOOK")
        print("="*60)
        
        webhook_url = self.discord_webhook if self.discord_webhook and 'discord.com' in self.discord_webhook else self.slack_webhook
        
        if not webhook_url or 'hooks.slack.com' in webhook_url or '...' in webhook_url:
            print("⚠️  Webhook chưa được cấu hình đúng trong .env")
            print(f"   Discord URL: {self.discord_webhook}")
            print(f"   Slack URL: {self.slack_webhook}")
            self.results['webhook']['status'] = 'not_configured'
            return
        
        try:
            message = f"🔧 Bot Diagnostics Test - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            
            data = {
                'content': message,  # Discord format
                'text': message,     # Slack format
                'username': 'Polymarket Bot Diagnostics'
            }
            
            print(f"📡 Đang gửi test message tới webhook...")
            print(f"   URL: {webhook_url[:50]}...")
            
            async with aiohttp.ClientSession() as session:
                async with session.post(webhook_url, json=data) as response:
                    status = response.status
                    
                    print(f"📊 HTTP Status: {status}")
                    
                    if status in [200, 204]:
                        print(f"✅ Webhook hoạt động tốt!")
                        self.results['webhook']['status'] = 'success'
                        self.results['webhook']['details'] = f"HTTP {status}"
                    elif status == 405:
                        print(f"❌ Webhook lỗi: HTTP 405 Method Not Allowed")
                        print(f"   Nguyên nhân: Endpoint không chấp nhận POST requests")
                        print(f"   Giải pháp:")
                        print(f"   1. Kiểm tra lại webhook URL")
                        print(f"   2. Tạo webhook mới trên Discord/Slack")
                        print(f"   3. Đảm bảo webhook chấp nhận POST requests")
                        self.results['webhook']['status'] = 'error'
                        self.results['webhook']['details'] = 'HTTP 405 - Method Not Allowed'
                    else:
                        text = await response.text()
                        print(f"❌ Webhook lỗi: HTTP {status}")
                        print(f"   Response: {text[:200]}")
                        self.results['webhook']['status'] = 'error'
                        self.results['webhook']['details'] = f"HTTP {status}"
                        
        except Exception as e:
            print(f"❌ Lỗi khi test webhook: {e}")
            self.results['webhook']['status'] = 'error'
            self.results['webhook']['details'] = str(e)
    
    def print_summary(self):
        """In tóm tắt kết quả"""
        print("\n" + "="*60)
        print("📋 TÓM TẮT KẾT QUẢ CHẨN ĐOÁN")
        print("="*60)
        
        # Gamma API
        status_icon = "✅" if self.results['gamma_api']['status'] == 'success' else "❌"
        print(f"\n{status_icon} Gamma API: {self.results['gamma_api']['status'].upper()}")
        print(f"   {self.results['gamma_api']['details']}")
        
        # Telegram
        status_icon = "✅" if self.results['telegram']['status'] == 'success' else ("⚠️" if self.results['telegram']['status'] == 'not_configured' else "❌")
        print(f"\n{status_icon} Telegram: {self.results['telegram']['status'].upper()}")
        print(f"   {self.results['telegram']['details']}")
        
        # Webhook
        status_icon = "✅" if self.results['webhook']['status'] == 'success' else ("⚠️" if self.results['webhook']['status'] == 'not_configured' else "❌")
        print(f"\n{status_icon} Webhook: {self.results['webhook']['status'].upper()}")
        print(f"   {self.results['webhook']['details']}")
        
        # Recommendations
        print("\n" + "="*60)
        print("💡 KHUYẾN NGHỊ")
        print("="*60)
        
        if self.results['markets_with_rewards'] == 0:
            print("\n🔴 VẤN ĐỀ NGHIÊM TRỌNG: Không tìm thấy markets có rewards!")
            print("   Nguyên nhân:")
            print("   1. Polymarket có thể tạm ngưng chương trình rewards")
            print("   2. API không trả về đầy đủ thông tin rewards")
            print("   3. Cần kiểm tra trực tiếp trên https://polymarket.com/rewards")
            print("\n   Giải pháp:")
            print("   1. Truy cập https://polymarket.com/rewards để xác nhận")
            print("   2. Nếu có rewards trên website, cần cập nhật API endpoint")
            print("   3. Nếu không có rewards, bot sẽ không hoạt động được")
        
        if self.results['webhook']['status'] == 'error' and 'HTTP 405' in self.results['webhook']['details']:
            print("\n🔴 VẤN ĐỀ: Webhook không chấp nhận POST requests")
            print("   Giải pháp:")
            print("   1. Tạo webhook mới trên Discord:")
            print("      - Vào Server Settings > Integrations > Webhooks")
            print("      - Tạo New Webhook")
            print("      - Copy Webhook URL")
            print("      - Cập nhật DISCORD_WEBHOOK_URL trong .env")
            print("   2. Hoặc tắt webhook trong config.yaml:")
            print("      webhook_enabled: false")
        
        print("\n" + "="*60)


async def main():
    """Chạy tất cả các tests"""
    print("🔧 BẮT ĐẦU CHẨN ĐOÁN BOT")
    print("="*60)
    
    diagnostics = BotDiagnostics()
    
    # Chạy các tests
    await diagnostics.test_gamma_api()
    await diagnostics.test_telegram()
    await diagnostics.test_webhook()
    
    # In tóm tắt
    diagnostics.print_summary()
    
    print("\n✅ HOÀN THÀNH CHẨN ĐOÁN!")


if __name__ == "__main__":
    asyncio.run(main())

