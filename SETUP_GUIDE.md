# 📖 Polymarket Bot - Hướng Dẫn Cài Đặt Chi Tiết

Tài liệu này hướng dẫn từng bước để cài đặt và chạy Polymarket Trading Bot.

## 📋 Mục Lục

1. [Chuẩn Bị](#1-chuẩn-bị)
2. [Cài Đặt Môi Trường](#2-cài-đặt-môi-trường)
3. [Cấu Hình Ví](#3-cấu-hình-ví)
4. [Cấu Hình Bot](#4-cấu-hình-bot)
5. [Chạy Thử Nghiệm](#5-chạy-thử-nghiệm)
6. [Triển Khai Production](#6-triển-khai-production)
7. [Giám Sát và Bảo Trì](#7-giám-sát-và-bảo-trì)

---

## 1. Chuẩn Bị

### 1.1 Yêu Cầu Hệ Thống

**Phần Cứng:**
- CPU: 2 cores trở lên
- RAM: 4GB minimum, 8GB khuyến nghị
- Ổ cứng: 10GB trống
- Kết nối internet ổn định (tốc độ >10Mbps)

**Phần Mềm:**
- Hệ điều hành: Ubuntu 20.04+ / macOS 11+ / Windows 10+
- Python 3.8 hoặc cao hơn
- Git
- Chrome/Chromium browser

### 1.2 Kiến Thức Cần Thiết

- Hiểu biết cơ bản về cryptocurrency và blockchain
- Biết sử dụng terminal/command line
- Hiểu về market making và trading
- Kiến thức về quản lý rủi ro

### 1.3 Tài Khoản và Vốn

**Tài khoản cần thiết:**
- Ví Polygon (MetaMask hoặc tương tự)
- Tài khoản Polymarket (để hiểu platform)
- (Tùy chọn) Telegram account cho alerts
- (Tùy chọn) Discord/Slack cho notifications

**Vốn khuyến nghị:**
- Vốn test: $100-500 USDC
- Vốn production: $1,000-10,000 USDC
- MATIC cho gas: ~10 MATIC mỗi ví
- Số lượng ví: 5-10 ví

---

## 2. Cài Đặt Môi Trường

### 2.1 Cài Đặt Python

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install python3.8 python3-pip python3-venv
python3 --version  # Kiểm tra version
```

**macOS:**
```bash
brew install python@3.8
python3 --version
```

**Windows:**
- Download từ [python.org](https://www.python.org/downloads/)
- Chọn "Add Python to PATH" khi cài đặt
- Mở Command Prompt và kiểm tra: `python --version`

### 2.2 Clone Repository

```bash
# Clone project
git clone https://github.com/yourusername/polymarket-bot.git
cd polymarket-bot

# Kiểm tra files
ls -la
```

### 2.3 Tạo Virtual Environment

```bash
# Tạo virtual environment
python3 -m venv venv

# Kích hoạt virtual environment
# Linux/macOS:
source venv/bin/activate

# Windows:
venv\Scripts\activate

# Kiểm tra
which python  # Linux/macOS
where python  # Windows
```

### 2.4 Cài Đặt Dependencies

```bash
# Upgrade pip
pip install --upgrade pip

# Cài đặt requirements
pip install -r requirements.txt

# Kiểm tra cài đặt
pip list
```

### 2.5 Cài Đặt ChromeDriver

**Ubuntu/Debian:**
```bash
# Cài Chrome
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo apt-get install -f

# Cài ChromeDriver
sudo apt-get install chromium-chromedriver

# Kiểm tra
chromedriver --version
google-chrome --version
```

**macOS:**
```bash
# Cài Chrome
brew install --cask google-chrome

# Cài ChromeDriver
brew install chromedriver

# Kiểm tra
chromedriver --version
```

**Windows:**
1. Download Chrome từ [google.com/chrome](https://www.google.com/chrome/)
2. Download ChromeDriver từ [chromedriver.chromium.org](https://chromedriver.chromium.org/)
3. Giải nén và thêm vào PATH

### 2.6 Tạo Thư Mục Cần Thiết

```bash
# Tạo các thư mục
mkdir -p logs models data backups

# Kiểm tra cấu trúc
tree -L 1
```

---

## 3. Cấu Hình Ví

### 3.1 Tạo Ví Mới

**Cách 1: Sử dụng Python**
```bash
python3 << EOF
from eth_account import Account
import secrets

# Tạo 5 ví
for i in range(5):
    priv = secrets.token_hex(32)
    private_key = "0x" + priv
    acct = Account.from_key(private_key)
    print(f"Wallet {i+1}:")
    print(f"  Address: {acct.address}")
    print(f"  Private Key: {private_key}")
    print()
EOF
```

**Cách 2: Sử dụng MetaMask**
1. Cài đặt MetaMask extension
2. Tạo ví mới
3. Export private key (Settings > Security & Privacy > Reveal Private Key)

### 3.2 Nạp Tiền Vào Ví

**Bước 1: Chuyển USDC lên Polygon**
```
1. Mua USDC trên exchange (Binance, Coinbase, etc.)
2. Withdraw USDC về ví Polygon
   - Network: Polygon (MATIC)
   - Token: USDC
   - Địa chỉ: Địa chỉ ví của bạn
```

**Bước 2: Nạp MATIC cho gas**
```
1. Mua MATIC trên exchange
2. Withdraw về ví Polygon
   - Mỗi ví cần ~10 MATIC
   - MATIC dùng để trả gas fees
```

**Bước 3: Kiểm tra số dư**
```bash
# Sử dụng script kiểm tra
python3 << EOF
from web3 import Web3

w3 = Web3(Web3.HTTPProvider('https://polygon-rpc.com'))

# Thay địa chỉ ví của bạn
address = "0xYourWalletAddress"

# Kiểm tra MATIC
matic_balance = w3.eth.get_balance(address)
print(f"MATIC: {w3.from_wei(matic_balance, 'ether')}")

# Kiểm tra USDC (cần thêm code cho ERC20)
EOF
```

### 3.3 Cấu Hình Private Keys

```bash
# Copy file mẫu
cp .env.example .env

# Chỉnh sửa .env
nano .env
```

Thêm private keys vào file `.env`:
```bash
# Thêm private keys (phân cách bằng dấu phẩy)
WALLET_PRIVATE_KEYS=0xkey1,0xkey2,0xkey3,0xkey4,0xkey5

# Ví chính để funding (tùy chọn)
MAIN_WALLET_PRIVATE_KEY=0xmainkey
```

**⚠️ BẢO MẬT:**
- KHÔNG BAO GIỜ share private keys
- KHÔNG commit file .env lên git
- Backup private keys ở nơi an toàn
- Sử dụng ví riêng cho bot, không dùng ví chính

---

## 4. Cấu Hình Bot

### 4.1 Cấu Hình Cơ Bản

Chỉnh sửa `config.yaml`:

```yaml
# Vốn giao dịch
TOTAL_CAPITAL=5000  # Tổng vốn USD

# Thông số quét thị trường
market_scanner:
  interval: 5  # Quét mỗi 5 giây
  min_reward: 300  # Phần thưởng tối thiểu $300
  max_competition_bars: 2  # Tối đa 2 thanh cạnh tranh

# Quản lý lệnh
order_management:
  spread_min: 0.008  # Spread tối thiểu 0.8 cent
  spread_max: 0.015  # Spread tối đa 1.5 cent
  size_min: 200  # Kích thước tối thiểu 200 shares
  size_max: 500  # Kích thước tối đa 500 shares

# Quản lý rủi ro
risk_management:
  max_capital_per_market: 0.05  # Tối đa 5% vốn/thị trường
  enable_hedging: true  # Bật tự động hedge
```

### 4.2 Cấu Hình Alerts (Tùy Chọn)

**Telegram:**
```bash
# 1. Tạo bot với @BotFather
# 2. Lấy bot token
# 3. Lấy chat ID (nhắn tin cho bot rồi truy cập):
#    https://api.telegram.org/bot<TOKEN>/getUpdates

# Thêm vào .env
TELEGRAM_BOT_TOKEN=123456789:ABCdefGHIjklMNOpqrsTUVwxyz
TELEGRAM_CHAT_ID=123456789
```

**Discord:**
```bash
# 1. Tạo webhook trong Discord server
# 2. Copy webhook URL
# 3. Thêm vào .env
DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/...
```

### 4.3 Cấu Hình RPC

```bash
# Trong .env, thêm RPC URL
POLYGON_RPC_URL=https://polygon-rpc.com

# Hoặc sử dụng Infura/Alchemy (khuyến nghị)
INFURA_PROJECT_ID=your_project_id
POLYGON_RPC_URL=https://polygon-mainnet.infura.io/v3/your_project_id
```

---

## 5. Chạy Thử Nghiệm

### 5.1 Test Mode

```bash
# Chạy ở chế độ test (không đặt lệnh thật)
TEST_MODE=true python main.py
```

Kiểm tra:
- ✅ Bot khởi động thành công
- ✅ Kết nối được với Polymarket
- ✅ Quét được thị trường
- ✅ Tính toán spread và size đúng
- ✅ Không có lỗi

### 5.2 Paper Trading

```bash
# Chạy với vốn ảo
PAPER_TRADING=true PAPER_TRADING_CAPITAL=10000 python main.py
```

Theo dõi trong 1-2 giờ:
- Xem log: `tail -f logs/polymarket_bot.log`
- Kiểm tra hiệu suất
- Đánh giá chiến lược

### 5.3 Chạy Với Vốn Nhỏ

```bash
# Chạy thật với vốn nhỏ ($100-500)
# Chỉnh trong .env:
TOTAL_CAPITAL=100

# Chạy bot
python main.py
```

Giám sát chặt chẽ:
- Kiểm tra mỗi 15-30 phút
- Xem log liên tục
- Kiểm tra số dư ví
- Theo dõi lệnh trên Polymarket

---

## 6. Triển Khai Production

### 6.1 Chạy Như Service (Linux)

Tạo file `/etc/systemd/system/polymarket-bot.service`:

```ini
[Unit]
Description=Polymarket Trading Bot
After=network.target

[Service]
Type=simple
User=youruser
WorkingDirectory=/home/youruser/polymarket-bot
Environment="PATH=/home/youruser/polymarket-bot/venv/bin"
ExecStart=/home/youruser/polymarket-bot/venv/bin/python main.py
Restart=always
RestartSec=10
StandardOutput=append:/home/youruser/polymarket-bot/logs/service.log
StandardError=append:/home/youruser/polymarket-bot/logs/service_error.log

[Install]
WantedBy=multi-user.target
```

Kích hoạt service:
```bash
# Reload systemd
sudo systemctl daemon-reload

# Enable service
sudo systemctl enable polymarket-bot

# Start service
sudo systemctl start polymarket-bot

# Kiểm tra status
sudo systemctl status polymarket-bot

# Xem logs
sudo journalctl -u polymarket-bot -f
```

### 6.2 Chạy Với Screen (Alternative)

```bash
# Cài đặt screen
sudo apt install screen

# Tạo session mới
screen -S polymarket-bot

# Chạy bot
python main.py

# Detach: Ctrl+A, D
# Reattach: screen -r polymarket-bot
```

### 6.3 Auto-Restart Script

Tạo file `run_bot.sh`:
```bash
#!/bin/bash

while true; do
    echo "Starting bot at $(date)"
    python main.py
    echo "Bot stopped at $(date). Restarting in 10 seconds..."
    sleep 10
done
```

Chạy:
```bash
chmod +x run_bot.sh
./run_bot.sh
```

---

## 7. Giám Sát và Bảo Trì

### 7.1 Giám Sát Hàng Ngày

**Kiểm tra logs:**
```bash
# Xem log realtime
tail -f logs/polymarket_bot.log

# Tìm lỗi
grep ERROR logs/polymarket_bot.log

# Xem hiệu suất
grep "Performance" logs/polymarket_bot.log
```

**Kiểm tra số dư ví:**
```bash
# Script kiểm tra nhanh
python3 << EOF
from wallet_manager import WalletManager
import yaml

config = yaml.safe_load(open('config.yaml'))
wm = WalletManager(config['wallet_management'])

import asyncio
balances = asyncio.run(wm.check_wallet_balances())
for addr, bal in balances.items():
    print(f"{addr}: {bal['usdc']} USDC, {bal['matic']} MATIC")
EOF
```

### 7.2 Backup Dữ Liệu

```bash
# Tạo script backup
cat > backup.sh << 'EOF'
#!/bin/bash
DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="backups/$DATE"

mkdir -p $BACKUP_DIR
cp -r logs $BACKUP_DIR/
cp -r data $BACKUP_DIR/
cp -r models $BACKUP_DIR/
cp config.yaml $BACKUP_DIR/

echo "Backup completed: $BACKUP_DIR"
EOF

chmod +x backup.sh

# Chạy backup
./backup.sh

# Tự động backup hàng ngày (crontab)
crontab -e
# Thêm dòng:
0 0 * * * /path/to/polymarket-bot/backup.sh
```

### 7.3 Cập Nhật Bot

```bash
# Pull code mới
git pull origin main

# Cập nhật dependencies
pip install -r requirements.txt --upgrade

# Restart bot
sudo systemctl restart polymarket-bot
```

### 7.4 Troubleshooting

**Bot không khởi động:**
```bash
# Kiểm tra Python version
python --version

# Kiểm tra dependencies
pip check

# Xem log chi tiết
DEBUG_MODE=true python main.py
```

**Lỗi ChromeDriver:**
```bash
# Cập nhật ChromeDriver
sudo apt update
sudo apt install --only-upgrade chromium-chromedriver

# Kiểm tra version match
chromedriver --version
google-chrome --version
```

**Lỗi kết nối:**
```bash
# Test RPC
curl https://polygon-rpc.com

# Thử RPC khác
POLYGON_RPC_URL=https://rpc-mainnet.matic.network python main.py
```

---

## 📞 Hỗ Trợ

Nếu gặp vấn đề:
1. Kiểm tra logs: `logs/polymarket_bot.log`
2. Xem lại cấu hình: `config.yaml` và `.env`
3. Chạy test: `python test_bot.py`
4. Tham khảo FAQ trong README.md
5. Mở issue trên GitHub

---

## ⚠️ Lưu Ý Quan Trọng

1. **Bắt đầu nhỏ**: Test với $100-500 trước
2. **Giám sát chặt**: Đặc biệt trong 1-2 tuần đầu
3. **Backup thường xuyên**: Backup logs và data
4. **Bảo mật**: Không share private keys
5. **Tuân thủ**: Đọc và tuân thủ ToS của Polymarket
6. **Rủi ro**: Chỉ trade với tiền bạn có thể mất

---

**Chúc bạn thành công! 🚀**

