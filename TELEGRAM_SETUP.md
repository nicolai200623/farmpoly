# 📱 TELEGRAM ALERTS SETUP

## 🎯 Mục đích

Nhận thông báo từ bot qua Telegram khi:
- ✅ Bot khởi động/tắt
- ✅ Đặt lệnh thành công
- ✅ Có lỗi xảy ra
- ✅ Báo cáo hiệu suất hàng ngày
- ✅ Đạt ngưỡng lợi nhuận/lỗ

---

## 📋 Yêu cầu

- Tài khoản Telegram
- 5-10 phút để setup

---

## 🔧 HƯỚNG DẪN SETUP

### Bước 1: Tạo Telegram Bot

1. **Mở Telegram** và tìm **@BotFather**

2. **Gửi lệnh:** `/newbot`

3. **Đặt tên bot:**
   ```
   BotFather: Alright, a new bot. How are we going to call it?
   You: Polymarket Trading Bot
   ```

4. **Đặt username bot** (phải kết thúc bằng `bot`):
   ```
   BotFather: Good. Now let's choose a username for your bot.
   You: polymarket_trading_bot
   ```

5. **Lưu Bot Token:**
   ```
   BotFather: Done! Congratulations on your new bot.
   
   Use this token to access the HTTP API:
   8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko
   
   Keep your token secure and store it safely...
   ```

   ⚠️ **LƯU Ý:** Token này là **MẬT** - không chia sẻ với ai!

---

### Bước 2: Lấy Chat ID

#### **Cách 1: Tự động (Khuyến nghị)**

1. **Tìm bot của bạn** trên Telegram (ví dụ: `@polymarket_trading_bot`)

2. **Gửi lệnh:** `/start`

3. **Mở trình duyệt** và truy cập:
   ```
   https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/getUpdates
   ```
   
   (Thay `8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko` bằng token của bạn)

4. **Tìm Chat ID** trong response:
   ```json
   {
     "ok": true,
     "result": [
       {
         "update_id": 123456789,
         "message": {
           "message_id": 1,
           "from": {...},
           "chat": {
             "id": -1003157421030,  ← ĐÂY LÀ CHAT ID
             "type": "private"
           },
           "text": "/start"
         }
       }
     ]
   }
   ```

5. **Lưu Chat ID:** `-1003157421030`

#### **Cách 2: Dùng @userinfobot**

1. **Tìm** `@userinfobot` trên Telegram

2. **Gửi lệnh:** `/start`

3. **Bot sẽ trả về** User ID của bạn

4. **Lưu ID** đó làm Chat ID

---

### Bước 3: Cấu hình .env

Mở file `.env` và thêm/sửa:

```bash
# ============================================
# ALERTS & NOTIFICATIONS
# ============================================
# Telegram Bot Configuration
TELEGRAM_BOT_TOKEN=8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko
TELEGRAM_CHAT_ID=-1003157421030
```

⚠️ **Thay bằng token và chat ID của bạn!**

---

### Bước 4: Test Telegram

Chạy script test:

```bash
# Windows
python scripts/test_telegram.py

# Linux/Mac
python3 scripts/test_telegram.py
```

**Kết quả mong đợi:**

```
============================================================
TELEGRAM BOT CONFIGURATION TEST
============================================================

1. CHECKING CONFIGURATION:
------------------------------------------------------------
✅ TELEGRAM_BOT_TOKEN: 8291644636:AAFoVcH...
✅ TELEGRAM_CHAT_ID: -1003157421030

2. CHECKING BOT INFO:
------------------------------------------------------------
✅ Bot connected successfully!
   Bot Name: Polymarket Trading Bot
   Bot Username: @polymarket_trading_bot
   Bot ID: 8291644636

3. SENDING TEST MESSAGE:
------------------------------------------------------------
📤 Sending test message to Telegram...
   Bot Token: 8291644636:AAFoVcH...
   Chat ID: -1003157421030
✅ Message sent successfully!
   Message ID: 123

============================================================
SUMMARY:
============================================================
✅ Telegram alerts are working correctly!

Next steps:
1. Check your Telegram app for the test message
2. Run the bot: python main.py
3. You should receive a startup notification
```

**Kiểm tra Telegram app:**

Bạn sẽ nhận được tin nhắn:

```
🧪 Telegram Test Message
━━━━━━━━━━━━━━━━━━━━━━
⏰ Time: 2025-11-03 12:30:45
✅ Status: Telegram alerts are working!
━━━━━━━━━━━━━━━━━━━━━━

If you see this message, your Telegram bot is configured correctly! 🎉
```

---

## 🚀 Chạy Bot với Telegram Alerts

```bash
python main.py
```

**Bạn sẽ nhận được:**

```
🚀 Polymarket Bot Started
━━━━━━━━━━━━━━━━━━━━━━
⏰ Time: 2025-11-03 12:35:00
💼 Wallets: 1
📊 Status: Running
━━━━━━━━━━━━━━━━━━━━━━
Bot is now scanning markets and placing orders.
```

---

## 📊 Các loại thông báo

### 1. **Startup Alert** (Khi bot khởi động)
```
🚀 Polymarket Bot Started
━━━━━━━━━━━━━━━━━━━━━━
⏰ Time: 2025-11-03 12:00:00
💼 Wallets: 1
📊 Status: Running
```

### 2. **Daily Performance Report** (Mỗi ngày lúc 00:00 UTC)
```
📊 Daily Performance Report
━━━━━━━━━━━━━━━━━━━━━━
💰 Daily P&L: $25.50
✅ Successful Trades: 15
📝 Total Fills: 20
❌ Cancelled Orders: 5
```

### 3. **Error Alerts** (Khi có lỗi)
```
❌ Error Alert
━━━━━━━━━━━━━━━━━━━━━━
⚠️ Failed to place order
Market: Will Trump win?
Error: Insufficient USDC balance
```

### 4. **High Risk Alerts** (Khi phát hiện rủi ro cao)
```
⚠️ High Risk Alert
━━━━━━━━━━━━━━━━━━━━━━
Market: Will Trump win?
Risk Score: 0.95
Action: Order cancelled
```

---

## ⚙️ Cấu hình nâng cao

### Tùy chỉnh alerts trong `config.yaml`:

```yaml
# Alerts and Notifications
alerts:
  # Telegram
  telegram_enabled: true
  telegram_bot_token: ""  # Set in .env
  telegram_chat_id: ""  # Set in .env

  # Alert levels
  alert_on_startup: true        # Thông báo khi khởi động
  alert_on_shutdown: true       # Thông báo khi tắt
  alert_on_error: true          # Thông báo khi có lỗi
  alert_on_high_risk: true      # Thông báo khi rủi ro cao
  alert_on_daily_report: true   # Báo cáo hàng ngày

  # Performance alerts
  alert_on_profit_threshold: 100  # Thông báo khi lời >= $100
  alert_on_loss_threshold: -50    # Thông báo khi lỗ >= $50
```

---

## 🔧 Troubleshooting

### ❌ "Telegram not configured in .env"

**Nguyên nhân:** Chưa set `TELEGRAM_BOT_TOKEN` hoặc `TELEGRAM_CHAT_ID`

**Giải pháp:**
1. Kiểm tra file `.env`
2. Đảm bảo có 2 dòng:
   ```
   TELEGRAM_BOT_TOKEN=your_token
   TELEGRAM_CHAT_ID=your_chat_id
   ```

---

### ❌ "Failed to send message! Status: 401"

**Nguyên nhân:** Bot token sai

**Giải pháp:**
1. Kiểm tra lại token từ @BotFather
2. Copy chính xác (không có khoảng trắng)
3. Update trong `.env`

---

### ❌ "Failed to send message! Status: 400 - Chat not found"

**Nguyên nhân:** Chat ID sai hoặc chưa gửi `/start` cho bot

**Giải pháp:**
1. Mở Telegram và tìm bot của bạn
2. Gửi lệnh `/start`
3. Lấy lại Chat ID theo hướng dẫn ở Bước 2

---

### ❌ "Failed to send message! Status: 403 - Forbidden"

**Nguyên nhân:** Bot bị block hoặc không có quyền gửi tin

**Giải pháp:**
1. Unblock bot trong Telegram
2. Gửi `/start` lại
3. Kiểm tra bot settings trong @BotFather

---

### ❌ Không nhận được tin nhắn

**Kiểm tra:**
1. ✅ Bot token đúng?
2. ✅ Chat ID đúng?
3. ✅ Đã gửi `/start` cho bot?
4. ✅ Bot không bị block?
5. ✅ Internet connection OK?

**Test:**
```bash
python scripts/test_telegram.py
```

---

## 📱 Sử dụng Group Chat

Nếu muốn nhận alerts trong group:

### Bước 1: Thêm bot vào group

1. Tạo group mới hoặc dùng group có sẵn
2. Add bot vào group
3. Promote bot thành admin (để gửi tin được)

### Bước 2: Lấy Group Chat ID

1. Gửi tin nhắn bất kỳ trong group
2. Truy cập:
   ```
   https://api.telegram.org/bot{TOKEN}/getUpdates
   ```
3. Tìm `"chat":{"id": -123456789, "type": "group"}`
4. Lưu Group Chat ID (số âm)

### Bước 3: Update .env

```bash
TELEGRAM_CHAT_ID=-123456789  # Group chat ID (số âm)
```

---

## 🎯 Best Practices

### 1. **Bảo mật Token**
- ❌ Không commit `.env` lên Git
- ❌ Không share token công khai
- ✅ Dùng `.gitignore` để exclude `.env`

### 2. **Test trước khi deploy**
```bash
python scripts/test_telegram.py
```

### 3. **Monitor alerts**
- Kiểm tra Telegram thường xuyên
- Đặt notification cho Telegram app
- Không tắt alerts quan trọng

### 4. **Backup configuration**
- Lưu bot token ở nơi an toàn
- Backup `.env` file
- Document setup process

---

## 📄 Files liên quan

- `.env` - Telegram configuration
- `config.yaml` - Alert settings
- `main.py` - Bot startup alerts
- `ml_predictor.py` - Alert sending logic
- `scripts/test_telegram.py` - Test script

---

## ✅ Checklist

- [ ] Tạo bot với @BotFather
- [ ] Lưu bot token
- [ ] Gửi `/start` cho bot
- [ ] Lấy chat ID
- [ ] Cấu hình `.env`
- [ ] Chạy `python scripts/test_telegram.py`
- [ ] Nhận được test message
- [ ] Chạy `python main.py`
- [ ] Nhận được startup alert

---

**Telegram alerts đã sẵn sàng! 🎉**

