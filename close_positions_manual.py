#!/usr/bin/env python3
"""
Script đóng vị thế thủ công (Manual Position Closer)
Cho phép đóng các vị thế đã fill một cách thủ công, không cần chờ đạt mức lãi

Tính năng:
- Hiển thị tất cả vị thế hiện tại với P&L
- Cho phép chọn vị thế cụ thể để đóng
- Đóng tất cả vị thế cùng lúc
- Đóng chỉ vị thế lãi hoặc lỗ
- Xác nhận trước khi đóng để tránh sai sót
"""

import os
import sys
import requests
from dotenv import load_dotenv
from py_clob_client.client import ClobClient
from py_clob_client.clob_types import OrderArgs, OrderType
from py_clob_client.constants import POLYGON
from py_clob_client.order_builder.constants import SELL
from typing import List, Dict, Optional
from web3 import Web3

# Load environment variables
load_dotenv()


class ManualPositionCloser:
    """Quản lý đóng vị thế thủ công"""
    
    def __init__(self):
        """Khởi tạo"""
        self.wallet_address = None
        self.client = None
        self.positions = []
        
    def initialize(self) -> bool:
        """Khởi tạo kết nối và lấy thông tin wallet"""
        try:
            # Get wallet private key
            private_key = os.getenv("WALLET_1_PK") or os.getenv("PRIVATE_KEY")
            if not private_key:
                print("❌ WALLET_1_PK hoặc PRIVATE_KEY không tìm thấy trong .env")
                return False
            
            # Remove 0x prefix if present
            if private_key.startswith('0x'):
                private_key = private_key[2:]
            
            # Get wallet address
            w3 = Web3()
            account = w3.eth.account.from_key(private_key)
            self.wallet_address = account.address
            
            # Initialize CLOB client
            self.client = ClobClient(
                host="https://clob.polymarket.com",
                key=private_key,
                chain_id=POLYGON
            )
            
            # Create API credentials
            try:
                self.client.set_api_creds(self.client.create_or_derive_api_creds())
            except Exception as e:
                print(f"⚠️  API credentials có thể đã tồn tại: {e}")
            
            print(f"✅ Đã kết nối với wallet: {self.wallet_address[:10]}...{self.wallet_address[-8:]}")
            return True
            
        except Exception as e:
            print(f"❌ Lỗi khởi tạo: {e}")
            import traceback
            traceback.print_exc()
            return False
    
    def fetch_positions(self) -> bool:
        """Lấy danh sách vị thế từ Polymarket Data API"""
        try:
            print(f"\n🔍 Đang tải vị thế từ Polymarket...")
            
            data_api_url = "https://data-api.polymarket.com/positions"
            params = {
                "user": self.wallet_address,
                "sizeThreshold": 0.01,
                "limit": 500
            }
            
            response = requests.get(data_api_url, params=params, timeout=10)
            response.raise_for_status()
            
            self.positions = response.json()
            
            if not self.positions:
                print("✅ Không có vị thế nào đang mở")
                return False
            
            print(f"✅ Tìm thấy {len(self.positions)} vị thế\n")
            return True
            
        except Exception as e:
            print(f"❌ Lỗi khi tải vị thế: {e}")
            import traceback
            traceback.print_exc()
            return False
    
    def display_positions(self):
        """Hiển thị danh sách vị thế với thông tin chi tiết"""
        if not self.positions:
            print("✅ Không có vị thế nào để hiển thị")
            return
        
        print("=" * 120)
        print("📊 DANH SÁCH VỊ THẾ HIỆN TẠI")
        print("=" * 120)
        print(f"{'#':<4} {'Market':<50} {'Outcome':<8} {'Shares':<12} {'Avg Price':<12} {'Cur Price':<12} {'P&L ($)':<12} {'P&L (%)':<10}")
        print("=" * 120)
        
        total_value = 0
        total_pnl = 0
        
        for i, pos in enumerate(self.positions, 1):
            title = pos.get('title', 'Unknown')[:48]
            outcome = pos.get('outcome', 'Unknown')[:6]
            size = float(pos.get('size', 0))
            avg_price = float(pos.get('avgPrice', 0))
            cur_price = float(pos.get('curPrice', 0))
            cash_pnl = float(pos.get('cashPnl', 0))
            percent_pnl = float(pos.get('percentPnl', 0))
            current_value = float(pos.get('currentValue', 0))
            
            total_value += current_value
            total_pnl += cash_pnl
            
            # Color coding for P&L
            pnl_symbol = "🟢" if cash_pnl >= 0 else "🔴"
            
            print(f"{i:<4} {title:<50} {outcome:<8} {size:<12.2f} ${avg_price:<11.4f} ${cur_price:<11.4f} {pnl_symbol}${cash_pnl:<10.2f} {percent_pnl:+.2f}%")
        
        print("=" * 120)
        print(f"{'TỔNG:':<4} {'':<50} {'':<8} {'':<12} {'':<12} {'':<12} ${total_pnl:<11.2f} ")
        print(f"Tổng giá trị hiện tại: ${total_value:.2f}")
        print("=" * 120 + "\n")
    
    def close_position(self, position: Dict, reason: str = "Manual close") -> bool:
        """Đóng một vị thế cụ thể"""
        try:
            title = position.get('title', 'Unknown')
            token_id = position.get('asset')
            size = float(position.get('size', 0))
            cur_price = float(position.get('curPrice', 0))
            cash_pnl = float(position.get('cashPnl', 0))
            
            print(f"\n🔄 Đang đóng vị thế: {title[:50]}")
            print(f"   Token ID: {token_id}")
            print(f"   Shares: {size:.2f}")
            print(f"   Giá hiện tại: ${cur_price:.4f}")
            print(f"   P&L dự kiến: ${cash_pnl:.2f}")
            
            # Tạo lệnh SELL với giá thấp hơn 1% để đảm bảo khớp nhanh
            sell_price = cur_price * 0.99
            
            # Tạo fresh signing client cho mỗi order
            private_key = os.getenv("WALLET_1_PK") or os.getenv("PRIVATE_KEY")
            if private_key.startswith('0x'):
                private_key = private_key[2:]
            
            signing_client = ClobClient(
                host="https://clob.polymarket.com",
                key=private_key,
                chain_id=POLYGON
            )
            
            # Set API credentials
            signing_client.set_api_creds(signing_client.create_or_derive_api_creds())
            
            # Tạo order
            order_args = OrderArgs(
                token_id=token_id,
                price=sell_price,
                size=size,
                side=SELL
            )
            
            # Sign và post order
            signed_order = signing_client.create_order(order_args)
            resp = signing_client.post_order(signed_order, OrderType.GTC)
            
            if resp and resp.get('success'):
                order_id = resp.get('orderID', 'unknown')
                print(f"   ✅ Đã đặt lệnh SELL thành công!")
                print(f"   Order ID: {order_id}")
                print(f"   Giá bán: ${sell_price:.4f}")
                print(f"   Dự kiến thu về: ${size * sell_price:.2f}")
                return True
            else:
                error_msg = resp.get('error', 'Unknown error') if resp else 'No response'
                print(f"   ❌ Lỗi đặt lệnh: {error_msg}")
                return False
                
        except Exception as e:
            print(f"   ❌ Lỗi đóng vị thế: {e}")
            import traceback
            traceback.print_exc()
            return False
    
    def close_selected_positions(self, indices: List[int]) -> Dict:
        """Đóng các vị thế được chọn"""
        results = {
            'success': 0,
            'failed': 0,
            'total': len(indices)
        }
        
        print(f"\n{'=' * 120}")
        print(f"🔄 ĐANG ĐÓNG {len(indices)} VỊ THẾ...")
        print(f"{'=' * 120}\n")
        
        for idx in indices:
            if 1 <= idx <= len(self.positions):
                position = self.positions[idx - 1]
                if self.close_position(position):
                    results['success'] += 1
                else:
                    results['failed'] += 1
            else:
                print(f"⚠️  Vị thế #{idx} không tồn tại")
                results['failed'] += 1
        
        return results
    
    def close_all_positions(self) -> Dict:
        """Đóng tất cả vị thế"""
        indices = list(range(1, len(self.positions) + 1))
        return self.close_selected_positions(indices)
    
    def close_profitable_positions(self) -> Dict:
        """Đóng chỉ các vị thế đang lãi"""
        profitable_indices = []
        for i, pos in enumerate(self.positions, 1):
            cash_pnl = float(pos.get('cashPnl', 0))
            if cash_pnl > 0:
                profitable_indices.append(i)
        
        if not profitable_indices:
            print("✅ Không có vị thế nào đang lãi")
            return {'success': 0, 'failed': 0, 'total': 0}
        
        print(f"💰 Tìm thấy {len(profitable_indices)} vị thế đang lãi")
        return self.close_selected_positions(profitable_indices)
    
    def close_losing_positions(self) -> Dict:
        """Đóng chỉ các vị thế đang lỗ"""
        losing_indices = []
        for i, pos in enumerate(self.positions, 1):
            cash_pnl = float(pos.get('cashPnl', 0))
            if cash_pnl < 0:
                losing_indices.append(i)
        
        if not losing_indices:
            print("✅ Không có vị thế nào đang lỗ")
            return {'success': 0, 'failed': 0, 'total': 0}
        
        print(f"⚠️  Tìm thấy {len(losing_indices)} vị thế đang lỗ")
        return self.close_selected_positions(losing_indices)


def print_menu():
    """Hiển thị menu lựa chọn"""
    print("\n" + "=" * 120)
    print("🎯 TÙY CHỌN ĐÓNG VỊ THẾ")
    print("=" * 120)
    print("1. Đóng vị thế cụ thể (nhập số thứ tự)")
    print("2. Đóng TẤT CẢ vị thế")
    print("3. Đóng chỉ vị thế ĐANG LÃI")
    print("4. Đóng chỉ vị thế ĐANG LỖ")
    print("5. Làm mới danh sách vị thế")
    print("0. Thoát")
    print("=" * 120)


def main():
    """Hàm chính"""
    print("\n" + "=" * 120)
    print("🎯 CÔNG CỤ ĐÓNG VỊ THẾ THỦ CÔNG - POLYMARKET")
    print("=" * 120 + "\n")
    
    # Khởi tạo
    closer = ManualPositionCloser()
    if not closer.initialize():
        print("❌ Không thể khởi tạo. Vui lòng kiểm tra .env file")
        return
    
    # Tải vị thế
    if not closer.fetch_positions():
        print("✅ Không có vị thế nào để đóng. Thoát chương trình.")
        return
    
    # Main loop
    while True:
        # Hiển thị vị thế
        closer.display_positions()
        
        # Hiển thị menu
        print_menu()
        
        try:
            choice = input("\nNhập lựa chọn của bạn: ").strip()
            
            if choice == "0":
                print("\n✅ Thoát chương trình. Tạm biệt!")
                break
            
            elif choice == "1":
                # Đóng vị thế cụ thể
                indices_input = input("Nhập số thứ tự vị thế (cách nhau bởi dấu phẩy, VD: 1,3,5): ").strip()
                try:
                    indices = [int(x.strip()) for x in indices_input.split(',')]
                    
                    # Xác nhận
                    print(f"\n⚠️  BẠN SẮP ĐÓNG {len(indices)} VỊ THẾ:")
                    for idx in indices:
                        if 1 <= idx <= len(closer.positions):
                            pos = closer.positions[idx - 1]
                            print(f"   #{idx}: {pos.get('title', 'Unknown')[:50]} - P&L: ${pos.get('cashPnl', 0):.2f}")
                    
                    confirm = input("\nGõ 'YES' để xác nhận: ").strip().upper()
                    if confirm == 'YES':
                        results = closer.close_selected_positions(indices)
                        print(f"\n📊 KẾT QUẢ: Thành công: {results['success']}, Thất bại: {results['failed']}")
                    else:
                        print("❌ Đã hủy")
                        
                except ValueError:
                    print("❌ Định dạng không hợp lệ. Vui lòng nhập số, VD: 1,2,3")
            
            elif choice == "2":
                # Đóng tất cả
                print(f"\n⚠️  CẢNH BÁO: BẠN SẮP ĐÓNG TẤT CẢ {len(closer.positions)} VỊ THẾ!")
                confirm = input("Gõ 'YES' để xác nhận: ").strip().upper()
                if confirm == 'YES':
                    results = closer.close_all_positions()
                    print(f"\n📊 KẾT QUẢ: Thành công: {results['success']}, Thất bại: {results['failed']}")
                else:
                    print("❌ Đã hủy")
            
            elif choice == "3":
                # Đóng vị thế lãi
                confirm = input("Đóng tất cả vị thế ĐANG LÃI? Gõ 'YES' để xác nhận: ").strip().upper()
                if confirm == 'YES':
                    results = closer.close_profitable_positions()
                    if results['total'] > 0:
                        print(f"\n📊 KẾT QUẢ: Thành công: {results['success']}, Thất bại: {results['failed']}")
                else:
                    print("❌ Đã hủy")
            
            elif choice == "4":
                # Đóng vị thế lỗ
                confirm = input("Đóng tất cả vị thế ĐANG LỖ? Gõ 'YES' để xác nhận: ").strip().upper()
                if confirm == 'YES':
                    results = closer.close_losing_positions()
                    if results['total'] > 0:
                        print(f"\n📊 KẾT QUẢ: Thành công: {results['success']}, Thất bại: {results['failed']}")
                else:
                    print("❌ Đã hủy")
            
            elif choice == "5":
                # Làm mới
                print("\n🔄 Đang làm mới danh sách vị thế...")
                closer.fetch_positions()
            
            else:
                print("❌ Lựa chọn không hợp lệ")
        
        except KeyboardInterrupt:
            print("\n\n✅ Đã dừng bởi người dùng. Tạm biệt!")
            break
        except Exception as e:
            print(f"❌ Lỗi: {e}")
            import traceback
            traceback.print_exc()


if __name__ == "__main__":
    main()

