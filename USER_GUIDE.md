# 📚 Polymarket Bot - Hướng Dẫn Sử Dụng

Tài liệu này hướng dẫn cách sử dụng và tối ưu hóa Polymarket Trading Bot.

## 📖 Mục Lục

1. [Khởi Động Bot](#1-khởi-động-bot)
2. [Giám Sát Hoạt Động](#2-giám-sát-hoạt-động)
3. [Tối Ưu Hóa Chiến Lược](#3-tối-ưu-hóa-chiến-lược)
4. [Quản Lý Rủi Ro](#4-quản-lý-rủi-ro)
5. [Xử Lý Sự Cố](#5-xử-lý-sự-cố)
6. [Best Practices](#6-best-practices)

---

## 1. Khởi Động Bot

### 1.1 Các Chế Độ Chạy

**Test Mode (Không đặt lệnh thật):**
```bash
TEST_MODE=true python main.py
```
- Sử dụng để test cấu hình
- Không tốn tiền
- Xem bot hoạt động như thế nào

**Paper Trading (Vốn ảo):**
```bash
PAPER_TRADING=true PAPER_TRADING_CAPITAL=10000 python main.py
```
- Mô phỏng trading với vốn ảo
- Đánh giá chiến lược
- Không rủi ro

**Production Mode (Chạy thật):**
```bash
python main.py
```
- Đặt lệnh thật trên Polymarket
- Sử dụng vốn thật
- Cần giám sát

**Debug Mode (Chi tiết):**
```bash
DEBUG_MODE=true VERBOSE_LOGGING=true python main.py
```
- Log chi tiết mọi hoạt động
- Dùng để troubleshoot
- File log sẽ lớn

### 1.2 Kiểm Tra Trước Khi Chạy

**Checklist:**
- [ ] Đã cấu hình `.env` với private keys
- [ ] Đã nạp USDC và MATIC vào ví
- [ ] Đã test với TEST_MODE
- [ ] Đã kiểm tra config.yaml
- [ ] Đã setup alerts (Telegram/Discord)
- [ ] Đã backup dữ liệu quan trọng

**Script kiểm tra:**
```bash
# Tạo file check.sh
cat > check.sh << 'EOF'
#!/bin/bash

echo "=== Pre-flight Check ==="

# Check Python
python --version || echo "❌ Python not found"

# Check dependencies
pip show py-clob-client > /dev/null && echo "✅ py-clob-client installed" || echo "❌ py-clob-client missing"

# Check .env
[ -f .env ] && echo "✅ .env exists" || echo "❌ .env missing"

# Check config
[ -f config.yaml ] && echo "✅ config.yaml exists" || echo "❌ config.yaml missing"

# Check directories
[ -d logs ] && echo "✅ logs directory exists" || echo "❌ logs directory missing"
[ -d models ] && echo "✅ models directory exists" || echo "❌ models directory missing"
[ -d data ] && echo "✅ data directory exists" || echo "❌ data directory missing"

echo "=== Check Complete ==="
EOF

chmod +x check.sh
./check.sh
```

### 1.3 Khởi Động Lần Đầu

```bash
# Bước 1: Activate virtual environment
source venv/bin/activate

# Bước 2: Kiểm tra cấu hình
python -c "import yaml; print(yaml.safe_load(open('config.yaml')))"

# Bước 3: Test mode
TEST_MODE=true python main.py

# Bước 4: Nếu OK, chạy thật với vốn nhỏ
# Sửa TOTAL_CAPITAL=100 trong .env
python main.py
```

---

## 2. Giám Sát Hoạt Động

### 2.1 Xem Logs Realtime

```bash
# Xem log chính
tail -f logs/polymarket_bot.log

# Xem chỉ errors
tail -f logs/polymarket_bot.log | grep ERROR

# Xem performance metrics
tail -f logs/polymarket_bot.log | grep "Performance\|P&L"
```

### 2.2 Dashboard Metrics

Bot tự động log các metrics quan trọng:

**Hiệu suất giao dịch:**
- Daily P&L (Lãi/lỗ hàng ngày)
- Total fills (Số lệnh được khớp)
- Successful trades (Giao dịch thành công)
- Cancelled orders (Lệnh bị hủy)

**Thị trường:**
- Markets scanned (Thị trường đã quét)
- Markets selected (Thị trường được chọn)
- Active positions (Vị thế đang mở)

**Rủi ro:**
- Total exposure (Tổng rủi ro)
- Capital utilization (Vốn đang sử dụng)
- Hedged positions (Vị thế đã hedge)

### 2.3 Telegram Alerts

Nếu đã cấu hình Telegram, bạn sẽ nhận:

**Alerts tự động:**
- 🚀 Bot khởi động/tắt
- ⚠️ Cảnh báo rủi ro cao (fill >80%)
- 💰 Lệnh được khớp
- ❌ Lệnh bị hủy
- 📊 Báo cáo hàng ngày (00:00 UTC)
- 🚨 Lỗi và exceptions

**Ví dụ alert:**
```
⚠️ High fill risk detected: 85% for market 0x1234...
Market: Will Bitcoin reach $100k?
Action: Order cancelled to avoid adverse selection
```

### 2.4 Kiểm Tra Số Dư Ví

```bash
# Script kiểm tra nhanh
python3 << 'EOF'
import asyncio
from web3 import Web3
import os
from dotenv import load_dotenv

load_dotenv()

w3 = Web3(Web3.HTTPProvider(os.getenv('POLYGON_RPC_URL', 'https://polygon-rpc.com')))

keys = os.getenv('WALLET_PRIVATE_KEYS', '').split(',')

for i, key in enumerate(keys):
    if not key:
        continue
    account = w3.eth.account.from_key(key)
    balance = w3.eth.get_balance(account.address)
    print(f"Wallet {i+1}: {account.address}")
    print(f"  MATIC: {w3.from_wei(balance, 'ether'):.4f}")
    print()
EOF
```

---

## 3. Tối Ưu Hóa Chiến Lược

### 3.1 Điều Chỉnh Thông Số

**Spread (Chênh lệch giá):**
```yaml
# config.yaml
order_management:
  spread_min: 0.008  # Tăng nếu bị fill quá nhiều
  spread_max: 0.015  # Giảm nếu không được fill
```

**Kích thước lệnh:**
```yaml
order_management:
  size_min: 200  # Tăng nếu muốn lợi nhuận cao hơn
  size_max: 500  # Giảm nếu muốn rủi ro thấp hơn
```

**Lọc thị trường:**
```yaml
market_scanner:
  min_reward: 300  # Tăng để chọn thị trường tốt hơn
  max_competition_bars: 2  # Giảm để tránh cạnh tranh
```

### 3.2 Phân Tích Hiệu Suất

**Xem báo cáo hàng ngày:**
```bash
# Tìm báo cáo trong logs
grep "Daily Performance Report" logs/polymarket_bot.log -A 10
```

**Phân tích theo category:**
```bash
# Xem fill rate theo loại thị trường
grep "fill_rate_by_category" logs/polymarket_bot.log
```

**Tìm giờ giao dịch tốt nhất:**
```bash
# Xem fill rate theo giờ
grep "fill_rate_by_hour" logs/polymarket_bot.log
```

### 3.3 A/B Testing

Chạy 2 instance với cấu hình khác nhau:

**Instance 1 (Conservative):**
```yaml
# config_conservative.yaml
order_management:
  spread_min: 0.012  # Spread rộng hơn
  spread_max: 0.020
risk_management:
  max_capital_per_market: 0.03  # Ít vốn hơn
```

**Instance 2 (Aggressive):**
```yaml
# config_aggressive.yaml
order_management:
  spread_min: 0.006  # Spread hẹp hơn
  spread_max: 0.012
risk_management:
  max_capital_per_market: 0.07  # Nhiều vốn hơn
```

So sánh kết quả sau 1 tuần.

---

## 4. Quản Lý Rủi Ro

### 4.1 Giới Hạn Rủi Ro

**Thiết lập giới hạn:**
```yaml
# config.yaml
risk_management:
  max_capital_per_market: 0.05  # Tối đa 5% vốn/thị trường
  max_total_exposure: 0.8  # Tối đa 80% tổng vốn
  enable_stop_loss: true
  stop_loss_percentage: 0.15  # Stop loss 15%
```

**Giám sát exposure:**
```bash
# Xem tổng exposure
grep "total_exposure" logs/polymarket_bot.log | tail -1
```

### 4.2 Hedging Tự Động

Bot tự động hedge khi:
- Imbalance >60% (một bên quá nhiều)
- Total exposure >70% vốn

**Kiểm tra hedging:**
```bash
# Xem các lệnh hedge
grep "Applied hedging" logs/polymarket_bot.log
```

### 4.3 Dừng Bot Khẩn Cấp

**Graceful shutdown:**
```bash
# Gửi SIGTERM (bot sẽ hủy tất cả lệnh)
pkill -TERM -f "python main.py"

# Hoặc Ctrl+C nếu chạy foreground
```

**Force stop:**
```bash
# Chỉ dùng khi cần thiết
pkill -9 -f "python main.py"

# Sau đó hủy lệnh thủ công trên Polymarket
```

### 4.4 Backup Trước Khi Thay Đổi

```bash
# Backup trước khi thay đổi config
./backup.sh

# Hoặc manual
cp config.yaml config.yaml.backup.$(date +%Y%m%d)
cp .env .env.backup.$(date +%Y%m%d)
```

---

## 5. Xử Lý Sự Cố

### 5.1 Bot Không Khởi Động

**Kiểm tra:**
```bash
# 1. Python version
python --version

# 2. Dependencies
pip check

# 3. Config syntax
python -c "import yaml; yaml.safe_load(open('config.yaml'))"

# 4. .env file
cat .env | grep -v "^#" | grep -v "^$"
```

**Chạy debug:**
```bash
DEBUG_MODE=true python main.py 2>&1 | tee debug.log
```

### 5.2 Lỗi ChromeDriver

```bash
# Kiểm tra version
chromedriver --version
google-chrome --version

# Cập nhật ChromeDriver
sudo apt update
sudo apt install --only-upgrade chromium-chromedriver

# Hoặc download manual
wget https://chromedriver.storage.googleapis.com/LATEST_RELEASE
```

### 5.3 Lỗi Kết Nối

**Test RPC:**
```bash
# Test Polygon RPC
curl -X POST https://polygon-rpc.com \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","method":"eth_blockNumber","params":[],"id":1}'
```

**Thử RPC khác:**
```bash
# Trong .env
POLYGON_RPC_URL=https://rpc-mainnet.matic.network
# Hoặc
POLYGON_RPC_URL=https://polygon-mainnet.infura.io/v3/YOUR_KEY
```

### 5.4 Lệnh Không Được Đặt

**Kiểm tra:**
1. Số dư USDC đủ không?
2. Số dư MATIC cho gas đủ không?
3. Private key đúng không?
4. Market còn mở không?

**Debug:**
```bash
# Xem chi tiết lỗi
grep "Error placing order" logs/polymarket_bot.log -A 5
```

### 5.5 Memory Leak

```bash
# Kiểm tra memory usage
ps aux | grep python

# Restart bot định kỳ (crontab)
0 */6 * * * systemctl restart polymarket-bot
```

---

## 6. Best Practices

### 6.1 Quy Trình Hàng Ngày

**Sáng (8:00 AM):**
- [ ] Kiểm tra báo cáo overnight
- [ ] Xem logs có lỗi không
- [ ] Kiểm tra số dư ví
- [ ] Review performance metrics

**Trưa (12:00 PM):**
- [ ] Kiểm tra active positions
- [ ] Xem có cần điều chỉnh không
- [ ] Monitor alerts

**Tối (8:00 PM):**
- [ ] Review daily performance
- [ ] Backup logs và data
- [ ] Plan cho ngày mai

**Trước khi ngủ:**
- [ ] Kiểm tra bot vẫn chạy
- [ ] Xem có alert nào không
- [ ] Set alerts cho overnight

### 6.2 Quy Trình Hàng Tuần

**Chủ nhật:**
- [ ] Phân tích performance tuần
- [ ] Điều chỉnh strategy nếu cần
- [ ] Backup toàn bộ data
- [ ] Update dependencies
- [ ] Review và optimize config

### 6.3 Quy Trình Hàng Tháng

**Đầu tháng:**
- [ ] Tính P&L tháng trước
- [ ] Rút lợi nhuận (nếu có)
- [ ] Rebalance vốn giữa các ví
- [ ] Security audit
- [ ] Rotate API keys
- [ ] Review và update strategy

### 6.4 Tips Tối Ưu

**1. Thời gian giao dịch:**
- Thị trường US: 9AM-5PM EST (active nhất)
- Thị trường crypto: 24/7 nhưng peak vào giờ US
- Sports: Trước và trong events

**2. Chọn thị trường:**
- Ưu tiên sports và entertainment
- Tránh thị trường có volume spike đột ngột
- Chọn thị trường có liquidity thấp (<$10k)

**3. Quản lý vốn:**
- Không bao giờ all-in
- Giữ 20% vốn dự phòng
- Rút lợi nhuận định kỳ

**4. Bảo mật:**
- Không share private keys
- Sử dụng 2FA cho tất cả accounts
- Backup thường xuyên
- Monitor cho unusual activity

### 6.5 Khi Nào Nên Dừng

**Dừng tạm thời nếu:**
- Thua lỗ >10% trong 1 ngày
- Có lỗi kỹ thuật nghiêm trọng
- Polymarket có vấn đề
- Cần điều chỉnh strategy lớn

**Dừng hoàn toàn nếu:**
- Không thể quản lý được rủi ro
- Thua lỗ >30% tổng vốn
- Không có thời gian giám sát
- Thay đổi ToS của Polymarket

---

## 📊 Metrics Quan Trọng

### Key Performance Indicators (KPIs)

**Profitability:**
- Daily P&L
- Weekly P&L
- Monthly P&L
- ROI (Return on Investment)

**Efficiency:**
- Fill rate (% lệnh được khớp)
- Win rate (% giao dịch có lời)
- Average spread captured
- Capital utilization

**Risk:**
- Max drawdown
- Sharpe ratio
- Value at Risk (VaR)
- Exposure ratio

**Operational:**
- Uptime (% thời gian bot chạy)
- Error rate
- Average response time
- Orders per day

---

## 🎯 Mục Tiêu Thực Tế

**Tuần 1-2 (Learning):**
- Mục tiêu: Break-even
- Focus: Học cách bot hoạt động
- Vốn: $100-500

**Tuần 3-4 (Optimization):**
- Mục tiêu: +5-10% profit
- Focus: Tối ưu hóa parameters
- Vốn: $500-1000

**Tháng 2-3 (Scaling):**
- Mục tiêu: +10-20% profit/tháng
- Focus: Scale up vốn
- Vốn: $1000-5000

**Tháng 4+ (Mature):**
- Mục tiêu: +15-30% profit/tháng
- Focus: Duy trì và optimize
- Vốn: $5000+

---

## 📞 Hỗ Trợ

**Tài liệu:**
- README.md - Tổng quan
- SETUP_GUIDE.md - Hướng dẫn cài đặt
- USER_GUIDE.md - Hướng dẫn sử dụng (file này)

**Community:**
- GitHub Issues
- Discord/Telegram group
- Email support

---

**Chúc bạn trading thành công! 📈**

*Remember: Patience, discipline, and risk management are keys to success.*

