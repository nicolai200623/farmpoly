"""
Test market scanner với cấu hình mới
Kiểm tra xem bot có tìm thấy markets không
"""

import asyncio
import sys
import os
import yaml

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from market_scanner_v2 import MarketScannerV2
import logging

# Setup logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


async def test_scanner():
    """Test market scanner"""
    print("="*80)
    print("🔍 TEST MARKET SCANNER VỚI CẤU HÌNH MỚI")
    print("="*80)
    
    # Load config
    try:
        with open('config.yaml', 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
        scanner_config = config.get('market_scanner', {})
    except Exception as e:
        print(f"❌ Không thể load config: {e}")
        scanner_config = {
            'min_reward': 10,
            'max_competition_bars': 5,
            'min_shares': 500
        }
    
    print(f"\n📋 Cấu hình scanner:")
    print(f"   - Min reward: ${scanner_config.get('min_reward', 10)}")
    print(f"   - Max competition: {scanner_config.get('max_competition_bars', 5)} bars")
    print(f"   - Min shares: {scanner_config.get('min_shares', 500)}")
    
    # Create scanner
    scanner = MarketScannerV2(scanner_config)
    
    # Initialize browser
    print(f"\n🌐 Khởi tạo Playwright browser...")
    await scanner.initialize()
    
    # Scan markets
    print(f"\n🔍 Bắt đầu quét markets...")
    markets = await scanner.scan_rewards_page()
    
    # Display results
    print(f"\n{'='*80}")
    print(f"📊 KẾT QUẢ QUÉT")
    print(f"{'='*80}")
    
    if len(markets) == 0:
        print(f"\n❌ KHÔNG TÌM THẤY MARKETS NÀO!")
        print(f"\n💡 Nguyên nhân có thể:")
        print(f"   1. Tất cả markets đều bị lọc bởi tiêu chí (reward, competition)")
        print(f"   2. API không trả về markets có rewards")
        print(f"   3. Cần kiểm tra logs ở trên để xem chi tiết")
    else:
        print(f"\n✅ Tìm thấy {len(markets)} markets!")
        print(f"\n📋 Danh sách markets:")
        
        for i, market in enumerate(markets[:10], 1):  # Chỉ hiển thị 10 markets đầu
            print(f"\n{i}. {market['question'][:70]}")
            print(f"   💰 Reward: ${market['reward']:.0f}")
            print(f"   📊 Competition: {market['competition_bars']} bars")
            print(f"   📈 Volume: ${market.get('volume', 0):,.0f}")
            print(f"   💧 Liquidity: ${market.get('liquidity', 0):,.0f}")
            print(f"   📏 Min shares: {market.get('min_shares', 0)}")
            print(f"   ⭐ Score: {market.get('score', 0):.1f}")
            
            # Hiển thị thông tin rewards chi tiết nếu có
            if 'rewards_min_size' in market:
                print(f"   🎁 Rewards details:")
                print(f"      - Min size: {market.get('rewards_min_size', 0)}")
                print(f"      - Max spread: {market.get('rewards_max_spread', 0)}")
                print(f"      - UMA reward: {market.get('uma_reward', 0)}")
        
        if len(markets) > 10:
            print(f"\n... và {len(markets) - 10} markets khác")
    
    # Close browser
    await scanner.close()
    
    print(f"\n{'='*80}")
    print(f"✅ HOÀN THÀNH TEST!")
    print(f"{'='*80}")
    
    return markets


async def main():
    """Main function"""
    try:
        markets = await test_scanner()
        
        # Summary
        print(f"\n📝 TÓM TẮT:")
        print(f"   - Tổng markets tìm thấy: {len(markets)}")
        
        if len(markets) > 0:
            print(f"\n✅ Bot CÓ THỂ hoạt động với {len(markets)} markets!")
            print(f"\n💡 Bước tiếp theo:")
            print(f"   1. Kiểm tra xem các markets này có phù hợp không")
            print(f"   2. Điều chỉnh tiêu chí lọc trong config.yaml nếu cần")
            print(f"   3. Chạy bot với: python main.py")
        else:
            print(f"\n❌ Bot KHÔNG THỂ hoạt động - không có markets!")
            print(f"\n💡 Giải pháp:")
            print(f"   1. Giảm min_reward trong config.yaml (hiện tại: 10)")
            print(f"   2. Tăng max_competition_bars (hiện tại: 5)")
            print(f"   3. Kiểm tra logs để xem tại sao markets bị reject")
            print(f"   4. Xem xét chuyển sang chiến lược market making thông thường")
        
    except Exception as e:
        print(f"\n❌ Lỗi khi test: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(main())

