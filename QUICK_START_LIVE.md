# 🚀 HƯỚNG DẪN NHANH: CHẠY LIVE POLYMARKET BOT

## ⚡ TÓM TẮT NHANH

**Trạng thái hiện tại:** ⚠️ **CHƯA SẴN SÀNG** - Cần sửa 2-3 vấn đề trước khi chạy live

**Thời gian cần:** ~10-15 phút để sửa và kiểm tra

---

## 📋 CHECKLIST 3 BƯỚC

### ✅ BƯỚC 1: SỬA CODE (5 phút)

Chạy script tự động sửa hardcoded values:

```bash
python scripts/fix_hardcoded_values.py
```

Script này sẽ:
- ✅ Sửa `order_manager.py` để đọc CLOB host và chain_id từ config
- ✅ Sửa `wallet_manager.py` để đọc RPC URL từ config
- ✅ Tạo backup files tự động

**Kết quả mong đợi:** "ALL FIXES APPLIED SUCCESSFULLY!"

---

### ✅ BƯỚC 2: SỬA CONFIG (2 phút)

Mở file `config.yaml` và sửa 2 dòng:

```yaml
# Line 350-353
development:
  test_mode: false      # ❌ ĐỔI TỪ true → false
  paper_trading: false  # ❌ ĐỔI TỪ true → false
```

**Lưu ý:** Đây là thay đổi QUAN TRỌNG NHẤT! Nếu không sửa, bot sẽ chỉ chạy giả lập.

---

### ✅ BƯỚC 3: KIỂM TRA (5 phút)

Chạy checklist tương tác:

```bash
python scripts/pre_live_interactive_checklist.py
```

Script này sẽ kiểm tra:
1. ✅ Code đã được sửa chưa
2. ✅ Config đã đúng chưa
3. ✅ Wallet có đủ USDC và MATIC không
4. ✅ USDC đã được approve chưa

**Kết quả mong đợi:** "ALL CHECKS PASSED!"

---

## 🚀 CHẠY BOT

Sau khi tất cả checks pass:

```bash
python main.py
```

**Giám sát:**
- 📱 Telegram: Nhận thông báo real-time
- 📝 Logs: `tail -f logs/polymarket_bot.log`
- ⏱️ Thời gian: Giám sát ít nhất 1 giờ đầu

**Dừng bot:**
- Nhấn `Ctrl+C` để dừng an toàn

---

## ⚠️ CÁC VẤN ĐỀ ĐÃ PHÁT HIỆN

### 🔴 CRITICAL (BẮT BUỘC SỬA)

1. **Test mode đang BẬT**
   - File: `config.yaml` line 350
   - Sửa: `test_mode: false`
   - Hậu quả nếu không sửa: Bot chạy nhưng KHÔNG đặt lệnh thật

2. **Paper trading đang BẬT**
   - File: `config.yaml` line 353
   - Sửa: `paper_trading: false`
   - Hậu quả nếu không sửa: Chỉ giao dịch giả lập

### 🟡 HIGH (NÊN SỬA)

3. **Hardcoded CLOB settings**
   - File: `order_manager.py`
   - Sửa: Chạy `python scripts/fix_hardcoded_values.py`
   - Hậu quả nếu không sửa: Khó chuyển sang testnet sau này

4. **Hardcoded RPC URL**
   - File: `wallet_manager.py`
   - Sửa: Chạy `python scripts/fix_hardcoded_values.py`
   - Hậu quả nếu không sửa: Không dùng được RPC URL tùy chỉnh

---

## ✅ NHỮNG GÌ ĐÃ ĐÚNG

1. ✅ **Config đang trỏ đến Production**
   - Chain ID: 137 (Polygon Mainnet)
   - CLOB: https://clob.polymarket.com
   - Contracts: USDC.e + Polymarket Exchange (đúng addresses)

2. ✅ **Có các biện pháp bảo vệ**
   - Auto-cancel khi bị fill: 0.5%
   - Stop loss: 15%
   - Max position age: 10 phút
   - Telegram alerts

3. ✅ **Vốn khởi đầu an toàn**
   - Total capital: $100 USDC
   - Max per market: $20 (20%)

---

## 📊 SO SÁNH VỚI LẦN TRƯỚC

**Không có thông tin về lần deploy trước** để so sánh.

**Nếu bạn nhớ lần trước bị mất tiền, hãy kiểm tra:**
- [ ] Lần trước có bật `test_mode` không?
- [ ] Lần trước có approve USDC trước không?
- [ ] Lần trước spread có đủ rộng không?
- [ ] Lần trước có giám sát logs không?

---

## 🛡️ AN TOÀN KHI CHẠY LIVE

### Trước khi chạy:
- ✅ Chạy `python scripts/pre_live_interactive_checklist.py`
- ✅ Đọc kỹ file `PRE_LIVE_AUDIT_REPORT.md`
- ✅ Backup private keys ở nơi an toàn

### Trong khi chạy:
- 📱 Bật Telegram notifications
- 📝 Theo dõi logs real-time
- ⏱️ Giám sát ít nhất 1 giờ đầu
- 🚨 Sẵn sàng dừng bot nếu có vấn đề

### Sau khi chạy:
- 📊 Kiểm tra positions: `python scripts/check_positions_onchain.py`
- 💰 Kiểm tra balance: `python scripts/check_wallets.py`
- 📋 Kiểm tra orders: `python scripts/check_orders.py`

---

## 🆘 NẾU CÓ VẤN ĐỀ

### Bot không đặt lệnh:
1. Kiểm tra `test_mode` và `paper_trading` đã = false chưa
2. Kiểm tra USDC đã approve chưa
3. Kiểm tra logs có lỗi gì không

### Bot bị fill liên tục:
1. Tăng spread trong config.yaml
2. Giảm size trong config.yaml
3. Dừng bot và review strategy

### Mất kết nối:
1. Kiểm tra RPC URL còn hoạt động không
2. Kiểm tra internet connection
3. Bot sẽ tự reconnect

---

## 📞 HỖ TRỢ

**Tài liệu chi tiết:**
- `PRE_LIVE_AUDIT_REPORT.md` - Báo cáo kiểm tra đầy đủ
- `DEPLOYMENT_SUMMARY.md` - Tổng quan deployment
- `LIVE_TRADING_READY.md` - Hướng dẫn live trading

**Scripts hữu ích:**
- `scripts/fix_hardcoded_values.py` - Tự động sửa code
- `scripts/pre_live_interactive_checklist.py` - Checklist tương tác
- `scripts/check_wallets.py` - Kiểm tra balance
- `scripts/check_orders.py` - Kiểm tra orders
- `scripts/approve_usdc.py` - Approve USDC

---

## 🎯 TÓM TẮT

**3 bước để chạy live:**

```bash
# 1. Sửa code
python scripts/fix_hardcoded_values.py

# 2. Sửa config.yaml (test_mode: false, paper_trading: false)

# 3. Kiểm tra
python scripts/pre_live_interactive_checklist.py

# 4. Chạy!
python main.py
```

**Thời gian:** ~10-15 phút  
**Vốn khởi đầu:** $100 USDC (an toàn)  
**Giám sát:** 1 giờ đầu (bắt buộc)

---

**Chúc may mắn! 🍀**

