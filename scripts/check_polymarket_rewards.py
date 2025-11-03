"""
Script kiểm tra chi tiết markets trên Polymarket
Tìm hiểu tại sao không có rewards
"""

import asyncio
import aiohttp
import json
from datetime import datetime


async def check_all_endpoints():
    """Kiểm tra tất cả các endpoints có thể"""
    
    endpoints = [
        {
            'name': 'Gamma API - Events',
            'url': 'https://gamma-api.polymarket.com/events',
            'params': {'closed': 'false', 'limit': 10}
        },
        {
            'name': 'Gamma API - Markets',
            'url': 'https://gamma-api.polymarket.com/markets',
            'params': {'closed': 'false', 'limit': 10}
        },
        {
            'name': 'CLOB API - Markets',
            'url': 'https://clob.polymarket.com/markets',
            'params': {'limit': 10}
        },
        {
            'name': 'Polymarket API - Rewards',
            'url': 'https://polymarket.com/api/rewards',
            'params': {}
        },
    ]
    
    print("="*80)
    print("🔍 KIỂM TRA TẤT CẢ CÁC ENDPOINTS POLYMARKET")
    print("="*80)
    
    async with aiohttp.ClientSession() as session:
        for endpoint in endpoints:
            print(f"\n{'='*80}")
            print(f"📡 {endpoint['name']}")
            print(f"   URL: {endpoint['url']}")
            print(f"   Params: {endpoint['params']}")
            print(f"{'='*80}")
            
            try:
                async with session.get(
                    endpoint['url'], 
                    params=endpoint['params'],
                    timeout=10
                ) as response:
                    status = response.status
                    print(f"📊 Status: {status}")
                    
                    if status == 200:
                        try:
                            data = await response.json()
                            
                            # Phân tích dữ liệu
                            if isinstance(data, list):
                                print(f"✅ Nhận được {len(data)} items")
                                
                                # Xem item đầu tiên
                                if len(data) > 0:
                                    first_item = data[0]
                                    print(f"\n📋 Cấu trúc item đầu tiên:")
                                    print(f"   Keys: {list(first_item.keys())}")
                                    
                                    # Kiểm tra rewards fields
                                    reward_fields = [k for k in first_item.keys() if 'reward' in k.lower()]
                                    if reward_fields:
                                        print(f"\n💰 Reward fields tìm thấy: {reward_fields}")
                                        for field in reward_fields:
                                            print(f"   {field}: {first_item.get(field)}")
                                    else:
                                        print(f"\n⚠️  Không tìm thấy reward fields")
                                    
                                    # Nếu là events, kiểm tra markets bên trong
                                    if 'markets' in first_item:
                                        markets = first_item['markets']
                                        print(f"\n📊 Event có {len(markets)} markets")
                                        
                                        if len(markets) > 0:
                                            first_market = markets[0]
                                            print(f"   Market keys: {list(first_market.keys())}")
                                            
                                            reward_fields = [k for k in first_market.keys() if 'reward' in k.lower()]
                                            if reward_fields:
                                                print(f"   💰 Market reward fields: {reward_fields}")
                                                for field in reward_fields:
                                                    print(f"      {field}: {first_market.get(field)}")
                                    
                                    # In sample data
                                    print(f"\n📄 Sample data (first item):")
                                    print(json.dumps(first_item, indent=2)[:500] + "...")
                                    
                            elif isinstance(data, dict):
                                print(f"✅ Nhận được dict response")
                                print(f"   Keys: {list(data.keys())}")
                                print(f"\n📄 Sample data:")
                                print(json.dumps(data, indent=2)[:500] + "...")
                            else:
                                print(f"⚠️  Response type: {type(data)}")
                                
                        except json.JSONDecodeError:
                            text = await response.text()
                            print(f"⚠️  Response không phải JSON")
                            print(f"   Text: {text[:200]}")
                    else:
                        text = await response.text()
                        print(f"❌ Error: {text[:200]}")
                        
            except asyncio.TimeoutError:
                print(f"❌ Timeout")
            except Exception as e:
                print(f"❌ Error: {e}")
    
    # Kiểm tra rewards page trực tiếp
    print(f"\n{'='*80}")
    print(f"🌐 KIỂM TRA REWARDS PAGE")
    print(f"{'='*80}")
    print(f"\n📌 Hãy truy cập các URL sau để kiểm tra thủ công:")
    print(f"   1. https://polymarket.com/rewards")
    print(f"   2. https://polymarket.com/activity")
    print(f"   3. https://polymarket.com/")
    print(f"\n💡 Kiểm tra xem:")
    print(f"   - Có tab 'Rewards' không?")
    print(f"   - Có markets nào hiển thị rewards không?")
    print(f"   - Chương trình rewards có đang hoạt động không?")


async def check_specific_market():
    """Kiểm tra một market cụ thể"""
    print(f"\n{'='*80}")
    print(f"🎯 KIỂM TRA MARKET CỤ THỂ")
    print(f"{'='*80}")
    
    # Lấy một market ID từ API
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(
                'https://gamma-api.polymarket.com/events',
                params={'closed': 'false', 'limit': 1},
                timeout=10
            ) as response:
                if response.status == 200:
                    data = await response.json()
                    if len(data) > 0 and len(data[0].get('markets', [])) > 0:
                        market = data[0]['markets'][0]
                        market_id = market.get('id') or market.get('conditionId')
                        
                        print(f"\n📊 Market ID: {market_id}")
                        print(f"   Question: {market.get('question', 'Unknown')}")
                        print(f"   Volume: ${market.get('volume', 0):,.0f}")
                        print(f"   Liquidity: ${market.get('liquidity', 0):,.0f}")
                        
                        # Kiểm tra tất cả các fields
                        print(f"\n📋 Tất cả fields của market:")
                        for key, value in market.items():
                            if 'reward' in key.lower() or 'incentive' in key.lower():
                                print(f"   💰 {key}: {value}")
                            else:
                                print(f"   {key}: {value}")
                        
        except Exception as e:
            print(f"❌ Error: {e}")


async def main():
    """Main function"""
    print("🔍 BẮT ĐẦU KIỂM TRA CHI TIẾT POLYMARKET")
    print(f"⏰ Thời gian: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    await check_all_endpoints()
    await check_specific_market()
    
    print(f"\n{'='*80}")
    print(f"📝 KẾT LUẬN")
    print(f"{'='*80}")
    print(f"""
Dựa trên kết quả kiểm tra:

1. Nếu KHÔNG thấy bất kỳ reward fields nào:
   → Polymarket đã TẮT chương trình rewards
   → Bot sẽ KHÔNG hoạt động được với chiến lược rewards
   → Cần chuyển sang chiến lược khác (market making thông thường)

2. Nếu CÓ reward fields nhưng giá trị = 0:
   → Chương trình rewards tồn tại nhưng chưa có markets nào tham gia
   → Cần đợi Polymarket thêm markets vào chương trình

3. Nếu CÓ reward fields và giá trị > 0:
   → Bot có vấn đề về logic lọc markets
   → Cần điều chỉnh tiêu chí lọc trong config.yaml

🔗 Tham khảo:
   - Polymarket Docs: https://docs.polymarket.com/
   - Gamma API Docs: https://docs.polymarket.com/#gamma-markets-api
   - CLOB API Docs: https://docs.polymarket.com/#clob-api
    """)
    
    print(f"\n✅ HOÀN THÀNH KIỂM TRA!")


if __name__ == "__main__":
    asyncio.run(main())

