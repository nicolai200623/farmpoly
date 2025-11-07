#!/usr/bin/env python3
"""
Test script cho close_positions_manual.py
Kiểm tra xem script có thể kết nối và lấy vị thế không
"""

import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_env_variables():
    """Test xem .env có đủ biến không"""
    print("\n" + "=" * 80)
    print("🔍 KIỂM TRA BIẾN MÔI TRƯỜNG")
    print("=" * 80)
    
    required_vars = ['WALLET_1_PK', 'PRIVATE_KEY', 'WALLET_ADDRESS']
    found_vars = []
    missing_vars = []
    
    for var in required_vars:
        value = os.getenv(var)
        if value:
            found_vars.append(var)
            if 'PK' in var or 'KEY' in var:
                print(f"✅ {var}: {value[:10]}...{value[-8:] if len(value) > 18 else ''}")
            else:
                print(f"✅ {var}: {value}")
        else:
            missing_vars.append(var)
            print(f"❌ {var}: Không tìm thấy")
    
    print("\n📊 Kết quả:")
    print(f"   Tìm thấy: {len(found_vars)}/{len(required_vars)}")
    
    # Cần ít nhất WALLET_1_PK hoặc PRIVATE_KEY
    has_key = os.getenv('WALLET_1_PK') or os.getenv('PRIVATE_KEY')
    if has_key:
        print("   ✅ Có private key để kết nối")
        return True
    else:
        print("   ❌ Thiếu private key (WALLET_1_PK hoặc PRIVATE_KEY)")
        return False


def test_imports():
    """Test xem có thể import các thư viện cần thiết không"""
    print("\n" + "=" * 80)
    print("🔍 KIỂM TRA THƯ VIỆN")
    print("=" * 80)
    
    libraries = [
        ('requests', 'requests'),
        ('py_clob_client.client', 'py-clob-client'),
        ('py_clob_client.clob_types', 'py-clob-client'),
        ('py_clob_client.constants', 'py-clob-client'),
        ('web3', 'web3'),
    ]
    
    success = True
    for module, package in libraries:
        try:
            __import__(module)
            print(f"✅ {package}")
        except ImportError as e:
            print(f"❌ {package}: {e}")
            success = False
    
    return success


def test_connection():
    """Test kết nối với Polymarket"""
    print("\n" + "=" * 80)
    print("🔍 KIỂM TRA KẾT NỐI POLYMARKET")
    print("=" * 80)
    
    try:
        import requests
        from web3 import Web3
        
        # Get wallet address
        private_key = os.getenv('WALLET_1_PK') or os.getenv('PRIVATE_KEY')
        if not private_key:
            print("❌ Không có private key")
            return False
        
        if private_key.startswith('0x'):
            private_key = private_key[2:]
        
        w3 = Web3()
        account = w3.eth.account.from_key(private_key)
        wallet_address = account.address
        
        print(f"✅ Wallet: {wallet_address[:10]}...{wallet_address[-8:]}")
        
        # Test Polymarket Data API
        print("\n🔗 Đang kết nối Polymarket Data API...")
        data_api_url = "https://data-api.polymarket.com/positions"
        params = {
            "user": wallet_address,
            "sizeThreshold": 0.01,
            "limit": 10
        }
        
        response = requests.get(data_api_url, params=params, timeout=10)
        
        if response.status_code == 200:
            positions = response.json()
            print(f"✅ Kết nối thành công!")
            print(f"   Số vị thế tìm thấy: {len(positions)}")
            
            if len(positions) > 0:
                print("\n📊 Vị thế đầu tiên:")
                pos = positions[0]
                print(f"   Market: {pos.get('title', 'Unknown')[:50]}")
                print(f"   Outcome: {pos.get('outcome', 'Unknown')}")
                print(f"   Size: {pos.get('size', 0)}")
                print(f"   P&L: ${pos.get('cashPnl', 0):.2f}")
            
            return True
        else:
            print(f"❌ Lỗi kết nối: {response.status_code}")
            print(f"   Response: {response.text[:200]}")
            return False
            
    except Exception as e:
        print(f"❌ Lỗi: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_clob_client():
    """Test khởi tạo CLOB client"""
    print("\n" + "=" * 80)
    print("🔍 KIỂM TRA CLOB CLIENT")
    print("=" * 80)
    
    try:
        from py_clob_client.client import ClobClient
        from py_clob_client.constants import POLYGON
        
        private_key = os.getenv('WALLET_1_PK') or os.getenv('PRIVATE_KEY')
        if not private_key:
            print("❌ Không có private key")
            return False
        
        if private_key.startswith('0x'):
            private_key = private_key[2:]
        
        print("🔧 Đang khởi tạo CLOB client...")
        client = ClobClient(
            host="https://clob.polymarket.com",
            key=private_key,
            chain_id=POLYGON
        )
        
        print("✅ CLOB client khởi tạo thành công")
        
        # Test API credentials
        print("\n🔑 Đang tạo API credentials...")
        try:
            client.set_api_creds(client.create_or_derive_api_creds())
            print("✅ API credentials tạo thành công")
        except Exception as e:
            print(f"⚠️  API credentials có thể đã tồn tại: {e}")
        
        return True
        
    except Exception as e:
        print(f"❌ Lỗi: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Chạy tất cả tests"""
    print("\n" + "=" * 80)
    print("🧪 TEST SCRIPT ĐÓNG VỊ THẾ THỦ CÔNG")
    print("=" * 80)
    
    results = {
        'env': test_env_variables(),
        'imports': test_imports(),
        'connection': test_connection(),
        'clob': test_clob_client()
    }
    
    print("\n" + "=" * 80)
    print("📊 KẾT QUẢ TỔNG HỢP")
    print("=" * 80)
    
    for test_name, result in results.items():
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{test_name.upper():<15} {status}")
    
    all_passed = all(results.values())
    
    print("\n" + "=" * 80)
    if all_passed:
        print("🎉 TẤT CẢ TESTS ĐỀU PASS!")
        print("✅ Script close_positions_manual.py sẵn sàng sử dụng")
        print("\nChạy script:")
        print("   python close_positions_manual.py")
    else:
        print("⚠️  MỘT SỐ TESTS THẤT BẠI")
        print("Vui lòng kiểm tra lại:")
        if not results['env']:
            print("   - File .env và các biến môi trường")
        if not results['imports']:
            print("   - Cài đặt thư viện: pip install -r requirements.txt")
        if not results['connection']:
            print("   - Kết nối internet và Polymarket API")
        if not results['clob']:
            print("   - CLOB client và API credentials")
    print("=" * 80 + "\n")
    
    return all_passed


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)

