# 🚀 Hướng Dẫn Triển Khai Farmpoly Bot trên VPS Ubuntu 22.04.5 LTS

## 📋 Mục Lục
1. [Chuẩn Bị VPS](#1-chuẩn-bị-vps)
2. [Cài Đặt Dependencies](#2-cài-đặt-dependencies)
3. [Clone & Setup Project](#3-clone--setup-project)
4. [Cấu Hình Bot](#4-cấu-hình-bot)
5. [Chạy Bot với Systemd](#5-chạy-bot-với-systemd)
6. [Monitoring & Logs](#6-monitoring--logs)
7. [Bảo Mật](#7-bảo-mật)
8. [Troubleshooting](#8-troubleshooting)

---

## 1. Chuẩn Bị VPS

### 1.1. Kết Nối VPS

```bash
# Kết nối qua SSH
ssh root@YOUR_VPS_IP

# Hoặc nếu dùng user khác
ssh your_username@YOUR_VPS_IP
```

### 1.2. Update Hệ Thống

```bash
# Update package list
sudo apt update && sudo apt upgrade -y

# Cài đặt các tools cơ bản
sudo apt install -y git curl wget vim htop screen tmux build-essential
```

### 1.3. Tạo User Riêng (Recommended)

```bash
# Tạo user mới cho bot (không nên chạy bot với root)
sudo adduser farmpoly

# Thêm vào sudo group
sudo usermod -aG sudo farmpoly

# Chuyển sang user mới
su - farmpoly
```

---

## 2. Cài Đặt Dependencies

### 2.1. Cài Python 3.9+

```bash
# Kiểm tra phiên bản Python hiện tại
python3 --version

# Ubuntu 22.04 mặc định có Python 3.10, nếu cần cài mới:
sudo apt install -y python3 python3-pip python3-venv python3-dev

# Verify
python3 --version  # Should be 3.10+
pip3 --version
```

### 2.2. Cài Playwright & Chrome Dependencies

```bash
# Cài đặt dependencies cho Playwright
sudo apt install -y \
    libnss3 \
    libnspr4 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libdrm2 \
    libdbus-1-3 \
    libxkbcommon0 \
    libxcomposite1 \
    libxdamage1 \
    libxfixes3 \
    libxrandr2 \
    libgbm1 \
    libpango-1.0-0 \
    libcairo2 \
    libasound2 \
    libatspi2.0-0 \
    libwayland-client0

# Cài thêm fonts
sudo apt install -y fonts-liberation fonts-noto-color-emoji
```

### 2.3. Cài Git (nếu chưa có)

```bash
sudo apt install -y git
git --version
```

---

## 3. Clone & Setup Project

### 3.1. Clone Repository

```bash
# Tạo thư mục cho project
mkdir -p ~/projects
cd ~/projects

# Clone repository (thay YOUR_REPO_URL)
git clone https://github.com/nicolai200623/farmpoly.git
cd farmpoly

# Hoặc nếu đã có code trên máy local, upload lên VPS:
# scp -r c:\LAINP\Augment\Farmpoly farmpoly@YOUR_VPS_IP:~/projects/
```

### 3.2. Tạo Virtual Environment

```bash
# Tạo virtual environment
python3 -m venv venv

# Activate
source venv/bin/activate

# Verify
which python  # Should point to venv/bin/python
```

### 3.3. Cài Dependencies

```bash
# Upgrade pip
pip install --upgrade pip

# Cài requirements
pip install -r requirements.txt

# Cài Playwright browsers
playwright install chromium

# Verify installations
python -c "import web3; print('web3:', web3.__version__)"
python -c "import playwright; print('playwright: OK')"
python -c "import torch; print('torch:', torch.__version__)"
```

**⏱️ Lưu ý:** Quá trình cài đặt có thể mất 5-10 phút, đặc biệt là PyTorch.

---

## 4. Cấu Hình Bot

### 4.1. Tạo File .env

```bash
# Copy example
cp .env.example .env

# Edit với nano hoặc vim
nano .env
```

**Nội dung file `.env`:**

```bash
# ============================================
# WALLET CONFIGURATION
# ============================================
# Demo mode (set to false for real trading)
USE_DEMO_WALLETS=false

# Real wallet private keys (KEEP SECURE!)
WALLET_1_PK=0xYOUR_PRIVATE_KEY_1
WALLET_2_PK=0xYOUR_PRIVATE_KEY_2

# ============================================
# RPC CONFIGURATION
# ============================================
# Polygon RPC (get free key from Alchemy/Infura)
POLYGON_RPC_URL=https://polygon-mainnet.g.alchemy.com/v2/YOUR_ALCHEMY_KEY

# Backup RPC
POLYGON_RPC_BACKUP=https://polygon-rpc.com

# ============================================
# TELEGRAM ALERTS (Optional)
# ============================================
TELEGRAM_BOT_TOKEN=
TELEGRAM_CHAT_ID=

# ============================================
# SECURITY
# ============================================
# Set file permissions
chmod 600 .env
```

**🔐 Bảo mật quan trọng:**
```bash
# Đảm bảo .env không bị commit
echo ".env" >> .gitignore

# Set quyền chỉ owner đọc được
chmod 600 .env

# Verify
ls -la .env  # Should show: -rw------- (600)
```

### 4.2. Cấu Hình config.yaml

```bash
# Edit config
nano config.yaml
```

**Cấu hình conservative cho VPS:**

```yaml
# Capital Settings (Start small!)
total_capital: 100  # $100 USDC
num_wallets: 2

# Market Scanner (Conservative)
market_scanner:
  interval: 10  # Scan every 10 seconds
  min_reward: 100  # Higher threshold
  max_competition_bars: 2
  min_shares: 500

# Order Management (Small positions)
order_management:
  spread_min: 0.01  # 1 cent
  spread_max: 0.02  # 2 cents
  size_min: 100
  size_max: 200
  update_interval: 60

# Risk Management (Strict)
risk_management:
  max_capital_per_market: 0.1  # 10% max
  max_total_exposure: 0.5  # 50% max
  enable_stop_loss: true
  stop_loss_percentage: 0.10  # 10% stop loss

# Logging
logging:
  level: INFO
  log_to_file: true
  log_to_console: true
```

### 4.3. Tạo Thư Mục Logs

```bash
# Tạo các thư mục cần thiết
mkdir -p logs data models backups

# Set permissions
chmod 755 logs data models backups
```

### 4.4. Test Configuration

```bash
# Test import modules
python -c "
from market_scanner_v2 import MarketScannerV2
from wallet_manager import WalletManager
from risk_manager import RiskManager
print('✅ All modules imported successfully')
"

# Run unit tests
python tests/run_tests.py
```

---

## 5. Chạy Bot với Systemd

### 5.1. Tạo Systemd Service

```bash
# Tạo service file
sudo nano /etc/systemd/system/farmpoly-bot.service
```

**Nội dung file service:**

```ini
[Unit]
Description=Farmpoly Polymarket Trading Bot
After=network.target

[Service]
Type=simple
User=farmpoly
WorkingDirectory=/home/farmpoly/projects/farmpoly
Environment="PATH=/home/farmpoly/projects/farmpoly/venv/bin"
ExecStart=/home/farmpoly/projects/farmpoly/venv/bin/python main.py
Restart=always
RestartSec=10
StandardOutput=append:/home/farmpoly/projects/farmpoly/logs/systemd.log
StandardError=append:/home/farmpoly/projects/farmpoly/logs/systemd-error.log

# Security settings
NoNewPrivileges=true
PrivateTmp=true

[Install]
WantedBy=multi-user.target
```

**⚠️ Lưu ý:** Thay `farmpoly` bằng username của bạn nếu khác.

### 5.2. Enable & Start Service

```bash
# Reload systemd
sudo systemctl daemon-reload

# Enable auto-start on boot
sudo systemctl enable farmpoly-bot

# Start service
sudo systemctl start farmpoly-bot

# Check status
sudo systemctl status farmpoly-bot
```

**Output mong đợi:**
```
● farmpoly-bot.service - Farmpoly Polymarket Trading Bot
     Loaded: loaded (/etc/systemd/system/farmpoly-bot.service; enabled)
     Active: active (running) since ...
```

### 5.3. Quản Lý Service

```bash
# Stop bot
sudo systemctl stop farmpoly-bot

# Restart bot
sudo systemctl restart farmpoly-bot

# View logs
sudo journalctl -u farmpoly-bot -f

# View last 100 lines
sudo journalctl -u farmpoly-bot -n 100
```

---

## 6. Monitoring & Logs

### 6.1. Real-time Monitoring

```bash
# Terminal 1: Bot logs
tail -f logs/polymarket_bot.log

# Terminal 2: System logs
sudo journalctl -u farmpoly-bot -f

# Terminal 3: System resources
htop
```

### 6.2. Sử Dụng Screen/Tmux (Alternative)

Nếu không dùng systemd, có thể dùng screen:

```bash
# Cài screen
sudo apt install -y screen

# Tạo session mới
screen -S farmpoly

# Activate venv và chạy bot
cd ~/projects/farmpoly
source venv/bin/activate
python main.py

# Detach: Ctrl+A, then D

# Reattach
screen -r farmpoly

# List sessions
screen -ls
```

### 6.3. Log Rotation

```bash
# Tạo logrotate config
sudo nano /etc/logrotate.d/farmpoly-bot
```

**Nội dung:**
```
/home/farmpoly/projects/farmpoly/logs/*.log {
    daily
    rotate 30
    compress
    delaycompress
    notifempty
    create 0644 farmpoly farmpoly
    sharedscripts
    postrotate
        systemctl reload farmpoly-bot > /dev/null 2>&1 || true
    endscript
}
```

---

## 7. Bảo Mật

### 7.1. Firewall Setup

```bash
# Enable UFW firewall
sudo ufw enable

# Allow SSH (IMPORTANT!)
sudo ufw allow 22/tcp

# Check status
sudo ufw status
```

### 7.2. SSH Security

```bash
# Disable root login
sudo nano /etc/ssh/sshd_config

# Set these values:
# PermitRootLogin no
# PasswordAuthentication no  # If using SSH keys

# Restart SSH
sudo systemctl restart sshd
```

### 7.3. File Permissions

```bash
# Secure .env file
chmod 600 .env

# Secure private directories
chmod 700 ~/projects/farmpoly/logs
chmod 700 ~/projects/farmpoly/data

# Verify
ls -la
```

---

## 8. Troubleshooting

### 8.1. Bot Không Start

```bash
# Check service status
sudo systemctl status farmpoly-bot

# Check logs
sudo journalctl -u farmpoly-bot -n 50

# Check Python errors
cd ~/projects/farmpoly
source venv/bin/activate
python main.py  # Run manually to see errors
```

### 8.2. Playwright Errors

```bash
# Reinstall Playwright
pip install --force-reinstall playwright
playwright install chromium

# Install system dependencies
sudo playwright install-deps chromium
```

### 8.3. Memory Issues

```bash
# Check memory
free -h

# If low memory, add swap
sudo fallocate -l 2G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile

# Make permanent
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
```

### 8.4. Network Issues

```bash
# Test RPC connection
curl -X POST https://polygon-rpc.com \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","method":"eth_blockNumber","params":[],"id":1}'

# Test Polymarket API
curl https://polymarket.com/api/markets
```

---

## 📊 Quick Commands Cheat Sheet

```bash
# Start bot
sudo systemctl start farmpoly-bot

# Stop bot
sudo systemctl stop farmpoly-bot

# Restart bot
sudo systemctl restart farmpoly-bot

# View logs (real-time)
tail -f logs/polymarket_bot.log

# View system logs
sudo journalctl -u farmpoly-bot -f

# Check wallet balances
source venv/bin/activate && python scripts/check_wallets.py

# Run tests
source venv/bin/activate && python tests/run_tests.py

# Update code
git pull
sudo systemctl restart farmpoly-bot
```

---

## ✅ Deployment Checklist

- [ ] VPS updated & secured
- [ ] Python 3.9+ installed
- [ ] Dependencies installed
- [ ] Project cloned
- [ ] Virtual environment created
- [ ] `.env` configured with private keys
- [ ] `config.yaml` configured (conservative settings)
- [ ] Wallets funded (USDC + MATIC)
- [ ] USDC approved for CLOB
- [ ] Systemd service created
- [ ] Service enabled & started
- [ ] Logs monitoring setup
- [ ] Firewall configured
- [ ] SSH secured

---

## 🎯 Next Steps

1. **Monitor for 1 hour** - Check logs every 10 minutes
2. **Verify orders** - Check if bot places orders correctly
3. **Check performance** - Review PnL after 24 hours
4. **Optimize config** - Adjust based on results
5. **Scale gradually** - Increase capital if profitable

---

## 📞 Support

- **Logs:** `tail -f logs/polymarket_bot.log`
- **Status:** `sudo systemctl status farmpoly-bot`
- **Tests:** `python tests/run_tests.py`

**Good luck! 🚀**

