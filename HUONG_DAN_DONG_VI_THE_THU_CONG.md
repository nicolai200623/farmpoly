# 🎯 HƯỚNG DẪN ĐÓNG VỊ THẾ THỦ CÔNG

## 📋 TỔNG QUAN

Script `close_positions_manual.py` cho phép bạn đóng các vị thế đã fill (khớp lệnh) một cách thủ công, không cần chờ đạt mức lãi tự động.

### ✨ Tính năng chính:

1. **Hiển thị vị thế chi tiết** - Xem tất cả vị thế với P&L realtime
2. **Đóng vị thế cụ thể** - Chọn vị thế nào muốn đóng
3. **Đóng tất cả** - Đóng toàn bộ vị thế cùng lúc
4. **Đóng theo điều kiện** - Chỉ đóng vị thế lãi hoặc lỗ
5. **Xác nhận an toàn** - Yêu cầu xác nhận trước khi đóng

---

## 🚀 CÁCH SỬ DỤNG

### 1. Chạy script

```bash
# Trên máy local
python close_positions_manual.py

# Trên VPS
python3 close_positions_manual.py
```

### 2. Script sẽ tự động:

✅ Kết nối với wallet từ `.env`  
✅ Tải danh sách vị thế từ Polymarket  
✅ Hiển thị bảng vị thế với P&L  

### 3. Chọn tùy chọn từ menu:

```
🎯 TÙY CHỌN ĐÓNG VỊ THẾ
════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
1. Đóng vị thế cụ thể (nhập số thứ tự)
2. Đóng TẤT CẢ vị thế
3. Đóng chỉ vị thế ĐANG LÃI
4. Đóng chỉ vị thế ĐANG LỖ
5. Làm mới danh sách vị thế
0. Thoát
════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
```

---

## 📊 VÍ DỤ SỬ DỤNG

### Ví dụ 1: Đóng vị thế cụ thể

```
Nhập lựa chọn của bạn: 1
Nhập số thứ tự vị thế (cách nhau bởi dấu phẩy, VD: 1,3,5): 2,5

⚠️  BẠN SẮP ĐÓNG 2 VỊ THẾ:
   #2: Will Bitcoin reach $100k by Dec 2024? - P&L: $12.50
   #5: Will Trump win 2024 election? - P&L: -$5.30

Gõ 'YES' để xác nhận: YES

🔄 ĐANG ĐÓNG 2 VỊ THẾ...
════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

🔄 Đang đóng vị thế: Will Bitcoin reach $100k by Dec 2024?
   Token ID: 0x1234...
   Shares: 100.00
   Giá hiện tại: $0.6500
   P&L dự kiến: $12.50
   ✅ Đã đặt lệnh SELL thành công!
   Order ID: abc123...
   Giá bán: $0.6435
   Dự kiến thu về: $64.35

🔄 Đang đóng vị thế: Will Trump win 2024 election?
   Token ID: 0x5678...
   Shares: 50.00
   Giá hiện tại: $0.4800
   P&L dự kiến: -$5.30
   ✅ Đã đặt lệnh SELL thành công!
   Order ID: def456...
   Giá bán: $0.4752
   Dự kiến thu về: $23.76

📊 KẾT QUẢ: Thành công: 2, Thất bại: 0
```

### Ví dụ 2: Đóng tất cả vị thế lãi

```
Nhập lựa chọn của bạn: 3
Đóng tất cả vị thế ĐANG LÃI? Gõ 'YES' để xác nhận: YES

💰 Tìm thấy 3 vị thế đang lãi

🔄 ĐANG ĐÓNG 3 VỊ THẾ...
════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
[Script sẽ đóng từng vị thế...]

📊 KẾT QUẢ: Thành công: 3, Thất bại: 0
```

### Ví dụ 3: Đóng tất cả vị thế

```
Nhập lựa chọn của bạn: 2

⚠️  CẢNH BÁO: BẠN SẮP ĐÓNG TẤT CẢ 5 VỊ THẾ!
Gõ 'YES' để xác nhận: YES

🔄 ĐANG ĐÓNG 5 VỊ THẾ...
════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
[Script sẽ đóng tất cả vị thế...]

📊 KẾT QUẢ: Thành công: 5, Thất bại: 0
```

---

## 🔍 HIỂU VỀ BẢNG VỊ THẾ

```
════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
📊 DANH SÁCH VỊ THẾ HIỆN TẠI
════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
#    Market                                             Outcome  Shares       Avg Price    Cur Price    P&L ($)      P&L (%)   
════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
1    Will Bitcoin reach $100k by Dec 2024?             Yes      100.00       $0.5200      $0.6500      🟢$13.00     +25.00%
2    Will Trump win 2024 election?                     No       50.00        $0.5500      $0.4800      🔴-$3.50     -6.36%
3    Will Ethereum reach $5k by year end?              Yes      75.00        $0.4000      $0.4500      🟢$3.75      +9.38%
════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
TỔNG:                                                                                                   $13.25       
Tổng giá trị hiện tại: $123.75
════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
```

### Giải thích các cột:

- **#** - Số thứ tự (dùng để chọn đóng)
- **Market** - Tên thị trường
- **Outcome** - Kết quả đặt cược (Yes/No)
- **Shares** - Số lượng shares đang nắm giữ
- **Avg Price** - Giá mua trung bình
- **Cur Price** - Giá hiện tại trên thị trường
- **P&L ($)** - Lãi/lỗ bằng USD
  - 🟢 = Đang lãi
  - 🔴 = Đang lỗ
- **P&L (%)** - Lãi/lỗ theo phần trăm

---

## ⚙️ CƠ CHẾ HOẠT ĐỘNG

### 1. Lấy thông tin vị thế

Script sử dụng **Polymarket Data API** để lấy vị thế realtime:

```
GET https://data-api.polymarket.com/positions?user={wallet_address}
```

### 2. Đóng vị thế

Khi đóng vị thế, script sẽ:

1. **Tạo lệnh SELL** với giá = giá hiện tại × 0.99 (giảm 1%)
   - Lý do: Đảm bảo lệnh khớp nhanh
   - Bạn có thể mất ~1% giá trị để đổi lấy tốc độ

2. **Ký và gửi lệnh** lên CLOB (Central Limit Order Book)

3. **Chờ khớp lệnh**
   - Lệnh được đặt ở chế độ GTC (Good Till Cancelled)
   - Thường khớp trong vài giây đến vài phút
   - Kiểm tra trên Polymarket.com để xem trạng thái

### 3. Xác minh kết quả

Sau khi đóng, bạn có thể:

- Chạy lại script để xem vị thế còn lại
- Kiểm tra trên https://polymarket.com/portfolio
- Xem lịch sử giao dịch trên blockchain

---

## ⚠️ LƯU Ý QUAN TRỌNG

### 1. Về giá bán

- Script đặt giá bán = **giá hiện tại × 0.99** (giảm 1%)
- Điều này đảm bảo lệnh khớp nhanh
- Bạn có thể mất ~1% giá trị để đổi lấy tốc độ
- Nếu muốn giá tốt hơn, có thể chỉnh sửa trong code (dòng 230)

### 2. Về phí gas

- Mỗi lệnh SELL tốn ~0.01-0.05 MATIC
- Đảm bảo có đủ MATIC trong wallet
- Nếu hết MATIC, lệnh sẽ thất bại

### 3. Về thời gian khớp lệnh

- Lệnh thường khớp trong **vài giây đến vài phút**
- Phụ thuộc vào thanh khoản thị trường
- Kiểm tra trên Polymarket để xác nhận

### 4. Về vị thế đang lỗ

- Script **KHÔNG** ngăn bạn đóng vị thế lỗ
- Hãy cân nhắc kỹ trước khi đóng vị thế lỗ
- Có thể thị trường sẽ phục hồi sau

### 5. Về xác nhận

- Script **YÊU CẦU** gõ 'YES' để xác nhận
- Điều này tránh đóng nhầm vị thế
- Hãy đọc kỹ thông tin trước khi xác nhận

---

## 🔧 KHẮC PHỤC SỰ CỐ

### Lỗi: "WALLET_1_PK không tìm thấy"

**Nguyên nhân:** File `.env` không có private key

**Giải pháp:**
```bash
# Kiểm tra file .env
cat .env | grep WALLET

# Đảm bảo có một trong hai:
WALLET_1_PK=your_private_key_here
# hoặc
PRIVATE_KEY=your_private_key_here
```

### Lỗi: "Không có vị thế nào"

**Nguyên nhân:** Wallet không có vị thế mở

**Giải pháp:**
- Kiểm tra trên https://polymarket.com/portfolio
- Đảm bảo đang dùng đúng wallet
- Vị thế có thể đã được đóng tự động bởi bot

### Lỗi: "Failed to place order"

**Nguyên nhân:** Có thể do:
- Hết MATIC (gas)
- Token ID không hợp lệ
- Vị thế đã được đóng

**Giải pháp:**
```bash
# 1. Kiểm tra MATIC balance
# Truy cập: https://polygonscan.com/address/{your_wallet}

# 2. Làm mới danh sách vị thế
# Chọn option 5 trong menu

# 3. Thử lại
```

### Lỗi: "API credentials may already exist"

**Không phải lỗi!** Đây chỉ là cảnh báo.

Script vẫn hoạt động bình thường.

---

## 🆚 SO SÁNH VỚI PROFIT TAKING TỰ ĐỘNG

| Tính năng | Profit Taking Tự động | Đóng thủ công |
|-----------|----------------------|---------------|
| **Khi nào đóng** | Khi đạt mức lãi cấu hình | Bất kỳ lúc nào |
| **Điều kiện** | Phải đạt min_profit_percentage | Không có điều kiện |
| **Vị thế lỗ** | Không đóng (nếu never_close_losing=true) | Có thể đóng |
| **Kiểm soát** | Tự động | Thủ công 100% |
| **Tốc độ** | Chậm (check mỗi 5 phút) | Ngay lập tức |
| **An toàn** | Cao (theo logic) | Phụ thuộc người dùng |

### Khi nào dùng Profit Taking tự động?

✅ Muốn bot tự động chốt lãi  
✅ Không muốn theo dõi liên tục  
✅ Tin tưởng vào logic của bot  

### Khi nào dùng Đóng thủ công?

✅ Cần đóng vị thế NGAY LẬP TỨC  
✅ Muốn đóng vị thế lỗ để cắt lỗ  
✅ Thị trường có biến động bất thường  
✅ Cần thanh khoản gấp  

---

## 📝 CẤU HÌNH NÂNG CAO

### Thay đổi giá bán

Mặc định script bán ở **99% giá hiện tại** để đảm bảo khớp nhanh.

Nếu muốn thay đổi, sửa file `close_positions_manual.py` dòng 230:

```python
# Mặc định: Giảm 1%
sell_price = cur_price * 0.99

# Giảm 0.5% (khớp chậm hơn nhưng giá tốt hơn)
sell_price = cur_price * 0.995

# Giảm 2% (khớp rất nhanh)
sell_price = cur_price * 0.98

# Bán đúng giá hiện tại (có thể không khớp)
sell_price = cur_price
```

### Thêm filter vị thế

Nếu muốn chỉ hiển thị vị thế của market cụ thể, sửa hàm `fetch_positions()`:

```python
# Thêm filter theo market name
self.positions = [
    pos for pos in response.json()
    if 'Bitcoin' in pos.get('title', '')  # Chỉ lấy vị thế có "Bitcoin"
]
```

---

## 🎯 BEST PRACTICES

### 1. Kiểm tra trước khi đóng

- Xem P&L hiện tại
- Cân nhắc xu hướng thị trường
- Kiểm tra thanh khoản (volume)

### 2. Đóng từng phần

Thay vì đóng tất cả, có thể:
- Đóng 50% vị thế để chốt lãi
- Giữ 50% để chờ lãi cao hơn

### 3. Theo dõi sau khi đóng

- Kiểm tra lệnh đã khớp chưa
- Xác nhận số dư USDC tăng
- Ghi chép lại P&L để phân tích

### 4. Backup trước khi đóng hàng loạt

```bash
# Chạy script để xem vị thế
python close_positions_manual.py

# Chọn option 5 để làm mới
# Chụp màn hình hoặc copy kết quả
# Sau đó mới đóng
```

---

## 📞 HỖ TRỢ

### Nếu gặp vấn đề:

1. **Kiểm tra log** - Script hiển thị lỗi chi tiết
2. **Kiểm tra .env** - Đảm bảo có WALLET_1_PK
3. **Kiểm tra MATIC** - Đảm bảo có đủ gas
4. **Kiểm tra Polymarket** - Xem vị thế trên web

### Debug mode:

Nếu cần debug chi tiết, chạy với Python debug:

```bash
python -u close_positions_manual.py 2>&1 | tee close_positions.log
```

Log sẽ được lưu vào file `close_positions.log`

---

## ✅ CHECKLIST TRƯỚC KHI ĐÓNG VỊ THẾ

- [ ] Đã kiểm tra P&L của vị thế
- [ ] Đã cân nhắc xu hướng thị trường
- [ ] Có đủ MATIC để trả gas
- [ ] Đã đọc kỹ thông tin xác nhận
- [ ] Đã backup/ghi chép thông tin vị thế
- [ ] Sẵn sàng chấp nhận mất ~1% giá trị để khớp nhanh

---

## 🎉 KẾT LUẬN

Script `close_positions_manual.py` là công cụ mạnh mẽ để quản lý vị thế thủ công.

**Ưu điểm:**
- ✅ Đóng vị thế ngay lập tức
- ✅ Kiểm soát 100%
- ✅ Giao diện thân thiện
- ✅ An toàn với xác nhận

**Nhược điểm:**
- ⚠️ Cần theo dõi thủ công
- ⚠️ Có thể mất ~1% giá trị
- ⚠️ Phụ thuộc vào quyết định người dùng

**Khuyến nghị:**
- Dùng kết hợp với Profit Taking tự động
- Chỉ đóng thủ công khi thực sự cần thiết
- Luôn kiểm tra kỹ trước khi xác nhận

---

**Chúc bạn trading thành công! 🚀**

