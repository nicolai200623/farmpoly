# 📱 Hướng Dẫn Thông Báo Telegram Chi Tiết

## 🎯 Tổng Quan

Hệ thống thông báo Telegram đã được nâng cấp để cung cấp thông tin chi tiết hơn về hoạt động của bot, giúp bạn theo dõi real-time mà không cần SSH vào VPS.

---

## 📋 Các Loại Thông Báo

### **1. 📝 Order Placed (Đặt Lệnh)**
Thông báo khi bot đặt lệnh mới.

**Nội dung:**
- Tên market
- Giá và size cho YES order
- Giá và size cho NO order
- Spread (%)

**Ví dụ:**
```
📝 Order Placed
━━━━━━━━━━━━━━━━━━━━━━
🎯 Market: Will Bitcoin hit $100k by end of 2024?

💰 YES Order
   • Price: $0.485
   • Size: 100 shares
   
💰 NO Order
   • Price: $0.515
   • Size: 100 shares

📊 Spread: 3.0%
⏰ 14:30:25
```

**Cấu hình:**
```yaml
notifications:
  order_placed: true  # Bật/tắt
```

---

### **2. 🚨 Order Filled (Lệnh Bị Fill) - QUAN TRỌNG!**
Thông báo khi lệnh bị fill (đặc biệt quan trọng vì chiến lược là tránh fill).

**Nội dung:**
- Tên market
- Side (YES/NO)
- Fill price và size
- P&L (nếu có)

**Ví dụ:**
```
🚨 ORDER FILLED! 🚨
━━━━━━━━━━━━━━━━━━━━━━
🎯 Market: Will Bitcoin hit $100k by end of 2024?

📊 Fill Details
   • Side: YES
   • Price: $0.485
   • Size: 50 shares
   • Order ID: order-abc-123...

📉 P&L: -$5.50

⏰ 14:35:12
```

**Cấu hình:**
```yaml
notifications:
  order_filled: true  # LUÔN BẬT!
```

**⚠️ LƯU Ý:** Notification này KHÔNG có cooldown - luôn gửi ngay lập tức!

---

### **3. 🚫 Order Cancelled (Hủy Lệnh)**
Thông báo khi bot hủy lệnh.

**Nội dung:**
- Tên market
- Order ID
- Lý do hủy

**Ví dụ:**
```
🚫 Order Cancelled
━━━━━━━━━━━━━━━━━━━━━━
🎯 Market: Will Bitcoin hit $100k by end of 2024?
🆔 Order ID: order-xyz-456...
📝 Reason: Partial fill threshold exceeded
⏰ 14:40:30
```

**Cấu hình:**
```yaml
notifications:
  order_cancelled: false  # Tắt mặc định (có thể spam)
```

**💡 TIP:** Chỉ bật nếu bạn muốn debug tại sao orders bị cancel.

---

### **4. 🔍 Markets Found (Tìm Thấy Markets)**
Thông báo khi tìm thấy markets mới đủ điều kiện (batch notification).

**Nội dung:**
- Tổng số markets tìm thấy
- Top 5 markets (nếu có nhiều hơn)
- Reward và competition cho mỗi market

**Ví dụ:**
```
🔍 New Markets Found
━━━━━━━━━━━━━━━━━━━━━━
📊 Total: 3 market(s)

1. Will Bitcoin hit $100k by end of 2024?
   💰 Reward: $250 | 📊 Competition: 1 bars

2. Will Trump win 2024 election?
   💰 Reward: $180 | 📊 Competition: 2 bars

3. Will Ethereum reach $5000 in 2024?
   💰 Reward: $150 | 📊 Competition: 0 bars

⏰ 14:45:00
```

**Cấu hình:**
```yaml
notifications:
  market_found: true  # Bật/tắt
```

**⏱️ Cooldown:** 60 giây (nhóm các markets tìm thấy trong 60s)

---

### **5. ⏭️ Markets Removed (Markets Bị Loại Bỏ)**
Thông báo khi markets bị loại bỏ khỏi danh sách (batch notification).

**Cấu hình:**
```yaml
notifications:
  market_removed: false  # Tắt mặc định (có thể spam)
```

---

### **6. ❌ Error (Lỗi)**
Thông báo khi có lỗi xảy ra.

**Nội dung:**
- Loại lỗi
- Nội dung lỗi
- Context (nếu có)

**Ví dụ:**
```
❌ Error Occurred
━━━━━━━━━━━━━━━━━━━━━━
🔴 Type: API Error
📝 Message: Failed to connect to Gamma API: Connection timeout
📍 Context: Market scanning loop
⏰ 14:50:15
```

**Cấu hình:**
```yaml
notifications:
  error: true  # Bật/tắt
```

**⏱️ Cooldown:** 30 giây

---

### **7. 🔴 Circuit Breaker**
Thông báo khi circuit breaker được kích hoạt hoặc phục hồi.

**Ví dụ:**
```
🔴 Circuit Breaker OPEN
━━━━━━━━━━━━━━━━━━━━━━
⚙️ Service: gamma_api
📊 Status: OPEN
⏰ 14:55:00

⚠️ Service temporarily disabled due to repeated failures
```

**Cấu hình:**
```yaml
notifications:
  circuit_breaker: true  # Bật/tắt
```

**⏱️ Cooldown:** 5 phút

---

### **8. ⚠️ Risk Alert (Cảnh Báo Rủi Ro)**
Thông báo về rủi ro cao.

**Ví dụ:**
```
⚠️ RISK ALERT
━━━━━━━━━━━━━━━━━━━━━━
🚨 Type: High Exposure

   • total_exposure: 850.00
   • max_allowed: 800.00
   • exposure_ratio: 0.85
   • action: Reduce positions

⏰ 15:00:00
```

**Cấu hình:**
```yaml
notifications:
  risk_alert: true  # Bật/tắt
```

**⏱️ Cooldown:** 5 phút

---

### **9. ⏰ Hourly Report (Báo Cáo Hàng Giờ)**
Báo cáo tổng hợp mỗi giờ.

**Nội dung:**
- Số lần scan
- Markets tìm thấy
- Orders placed/filled
- Profit
- System health (CPU, RAM)
- Issues (nếu có)

**Ví dụ:**
```
✅ Hourly Report
━━━━━━━━━━━━━━━━━━━━━━
⏰ 2024-01-15 15:00:00

📊 Last 60 Minutes
   • Scans: 120
   • Markets Found: 15
   • Orders Placed: 8
   • Orders Filled: 2
   • Profit: $12.50

💻 System
   • CPU: 45.2%
   • RAM: 62.8%

━━━━━━━━━━━━━━━━━━━━━━
```

**Cấu hình:**
```yaml
notifications:
  hourly_report: true  # Bật/tắt
```

---

### **10. 📊 Daily Report (Báo Cáo Hàng Ngày)**
Báo cáo chi tiết cuối ngày.

**Nội dung:**
- Total P&L
- Trading stats (orders, fill rate, markets)
- Rewards (estimated vs actual)
- Performance metrics (win rate, avg profit, best/worst trade)

**Ví dụ:**
```
📊 Daily Performance Report
━━━━━━━━━━━━━━━━━━━━━━
📅 Date: 2024-01-15

💰 P&L: +$45.80

📈 Trading Stats
   • Orders Placed: 156
   • Orders Filled: 12
   • Fill Rate: 7.7%
   • Markets Traded: 8

💰 Rewards
   • Estimated Rewards: $120.00
   • Actual Fills: -$74.20

📊 Performance
   • Win Rate: 58.3%
   • Avg Profit/Trade: $3.82
   • Best Trade: +$15.50
   • Worst Trade: -$12.30

━━━━━━━━━━━━━━━━━━━━━━
```

**Cấu hình:**
```yaml
notifications:
  daily_report: true  # Bật/tắt
```

---

### **11. 🚀 Startup / 🛑 Shutdown**
Thông báo khi bot khởi động hoặc tắt.

**Cấu hình:**
```yaml
alerts:
  alert_on_startup: true
  alert_on_shutdown: true
```

---

## ⚙️ Cấu Hình

### **File: `config.yaml`**

```yaml
alerts:
  # Telegram credentials (set in .env)
  telegram_enabled: true
  telegram_bot_token: ""  # Set in .env
  telegram_chat_id: ""  # Set in .env
  
  # Basic alerts
  alert_on_startup: true
  alert_on_shutdown: true
  alert_on_error: true
  alert_on_high_risk: true
  alert_on_daily_report: true
  
  # Detailed Notifications
  notifications:
    # Orders
    order_placed: true          # Thông báo khi đặt lệnh
    order_cancelled: false      # Thông báo khi hủy lệnh (có thể spam)
    order_filled: true          # Thông báo khi fill (QUAN TRỌNG!)
    
    # Markets
    market_found: true          # Thông báo khi tìm thấy markets
    market_removed: false       # Thông báo khi markets bị loại (có thể spam)
    
    # Errors & Alerts
    error: true                 # Thông báo lỗi
    circuit_breaker: true       # Thông báo circuit breaker
    risk_alert: true            # Thông báo rủi ro
    
    # Reports
    hourly_report: true         # Báo cáo hàng giờ
    daily_report: true          # Báo cáo hàng ngày
```

---

## 🧪 Test Notifications

Chạy script test để kiểm tra tất cả notifications:

```bash
python test_telegram_notifications.py
```

Script sẽ gửi 11 loại thông báo test để bạn xem trước.

---

## 💡 Khuyến Nghị Cấu Hình

### **Cấu hình Tối Thiểu (Ít spam nhất):**
```yaml
notifications:
  order_placed: false
  order_cancelled: false
  order_filled: true          # BẮT BUỘC!
  market_found: false
  market_removed: false
  error: true
  circuit_breaker: true
  risk_alert: true
  hourly_report: true
  daily_report: true
```

### **Cấu hình Cân Bằng (Khuyến nghị):**
```yaml
notifications:
  order_placed: true
  order_cancelled: false
  order_filled: true          # BẮT BUỘC!
  market_found: true
  market_removed: false
  error: true
  circuit_breaker: true
  risk_alert: true
  hourly_report: true
  daily_report: true
```

### **Cấu hình Debug (Tất cả):**
```yaml
notifications:
  order_placed: true
  order_cancelled: true
  order_filled: true
  market_found: true
  market_removed: true
  error: true
  circuit_breaker: true
  risk_alert: true
  hourly_report: true
  daily_report: true
```

---

## 🔧 Troubleshooting

### **Không nhận được thông báo?**

1. **Kiểm tra .env:**
   ```bash
   cat .env | grep TELEGRAM
   ```

2. **Test Telegram connection:**
   ```bash
   python scripts/test_telegram.py
   ```

3. **Kiểm tra config:**
   ```bash
   cat config.yaml | grep -A 15 "notifications:"
   ```

4. **Xem log:**
   ```bash
   tail -f log.md | grep -i telegram
   ```

---

## 📚 Files Liên Quan

- `telegram_notifier.py` - Module thông báo Telegram
- `config.yaml` - Cấu hình notifications
- `main.py` - Tích hợp notifications vào bot
- `order_manager.py` - Notifications cho orders
- `test_telegram_notifications.py` - Test script

---

## ✅ Checklist

- [ ] Đã cấu hình TELEGRAM_BOT_TOKEN trong .env
- [ ] Đã cấu hình TELEGRAM_CHAT_ID trong .env
- [ ] Đã test với `python test_telegram_notifications.py`
- [ ] Đã cấu hình notifications trong config.yaml
- [ ] Đã commit và push code lên GitHub
- [ ] Đã deploy lên VPS
- [ ] Đã restart bot và kiểm tra startup notification

---

**🎉 Hoàn thành! Bây giờ bạn có thể theo dõi bot real-time qua Telegram!**

