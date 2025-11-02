# ⚡ VPS Quick Start - 5 Phút Deploy Bot

## 🎯 Mục Tiêu
Deploy Farmpoly bot lên VPS Ubuntu 22.04 trong **5-15 phút**.

---

## 📋 Yêu Cầu Trước Khi Bắt Đầu

- ✅ VPS Ubuntu 22.04.5 LTS
- ✅ SSH access (root hoặc sudo user)
- ✅ 2 wallet addresses với private keys
- ✅ Mỗi wallet có: 25 USDC + 0.5 MATIC
- ✅ Alchemy/Infura RPC key (free)

---

## 🚀 Cách 1: Deploy Siêu Nhanh (5 phút)

### Bước 1: SSH vào VPS
```bash
ssh your_username@YOUR_VPS_IP
```

### Bước 2: Download & Run Setup Script
```bash
# Download script
wget https://raw.githubusercontent.com/nicolai200623/farmpoly/master/scripts/vps_setup.sh

# Make executable
chmod +x vps_setup.sh

# Run
./vps_setup.sh
```

⏱️ **Thời gian:** ~5 phút

### Bước 3: Clone Repository
```bash
cd ~/projects
git clone https://github.com/nicolai200623/farmpoly.git
cd farmpoly
```

### Bước 4: Cấu Hình .env
```bash
cp .env.example .env
nano .env
```

**Thêm vào file .env:**
```bash
USE_DEMO_WALLETS=false
WALLET_1_PK=0xYOUR_PRIVATE_KEY_1
WALLET_2_PK=0xYOUR_PRIVATE_KEY_2
POLYGON_RPC_URL=https://polygon-mainnet.g.alchemy.com/v2/YOUR_KEY
```

**Lưu:** `Ctrl+O` → `Enter` → `Ctrl+X`

### Bước 5: Deploy
```bash
chmod +x scripts/quick_deploy.sh
./scripts/quick_deploy.sh
```

⏱️ **Thời gian:** ~10 phút

### Bước 6: Verify
```bash
# Check status
sudo systemctl status farmpoly-bot

# View logs
tail -f logs/polymarket_bot.log
```

**✅ XONG! Bot đang chạy!**

---

## 🔧 Cách 2: Deploy Thủ Công (15 phút)

### 1. Update VPS
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y git python3 python3-pip python3-venv
```

### 2. Cài Playwright Dependencies
```bash
sudo apt install -y libnss3 libnspr4 libatk1.0-0 libatk-bridge2.0-0 \
    libcups2 libdrm2 libdbus-1-3 libxkbcommon0 libxcomposite1 \
    libxdamage1 libxfixes3 libxrandr2 libgbm1 libpango-1.0-0 \
    libcairo2 libasound2 fonts-liberation
```

### 3. Clone & Setup
```bash
mkdir -p ~/projects && cd ~/projects
git clone https://github.com/nicolai200623/farmpoly.git
cd farmpoly

# Create venv
python3 -m venv venv
source venv/bin/activate

# Install
pip install --upgrade pip
pip install -r requirements.txt
playwright install chromium
```

### 4. Configure
```bash
cp .env.example .env
nano .env  # Add private keys
chmod 600 .env
mkdir -p logs data models backups
```

### 5. Create Service
```bash
sudo nano /etc/systemd/system/farmpoly-bot.service
```

**Paste this (replace `your_username`):**
```ini
[Unit]
Description=Farmpoly Polymarket Trading Bot
After=network.target

[Service]
Type=simple
User=your_username
WorkingDirectory=/home/your_username/projects/farmpoly
Environment="PATH=/home/your_username/projects/farmpoly/venv/bin"
ExecStart=/home/your_username/projects/farmpoly/venv/bin/python main.py
Restart=always
RestartSec=10
StandardOutput=append:/home/your_username/projects/farmpoly/logs/systemd.log
StandardError=append:/home/your_username/projects/farmpoly/logs/systemd-error.log

[Install]
WantedBy=multi-user.target
```

### 6. Start
```bash
sudo systemctl daemon-reload
sudo systemctl enable farmpoly-bot
sudo systemctl start farmpoly-bot
sudo systemctl status farmpoly-bot
```

---

## 📊 Monitoring

### Dashboard
```bash
cd ~/projects/farmpoly
chmod +x scripts/monitor.sh
./scripts/monitor.sh
```

### Manual Commands
```bash
# Status
sudo systemctl status farmpoly-bot

# Logs (real-time)
tail -f ~/projects/farmpoly/logs/polymarket_bot.log

# System logs
sudo journalctl -u farmpoly-bot -f

# Check wallets
cd ~/projects/farmpoly && source venv/bin/activate
python scripts/check_wallets.py
```

---

## 🎮 Control Commands

```bash
# Start
sudo systemctl start farmpoly-bot

# Stop
sudo systemctl stop farmpoly-bot

# Restart
sudo systemctl restart farmpoly-bot

# Status
sudo systemctl status farmpoly-bot

# Logs
tail -f ~/projects/farmpoly/logs/polymarket_bot.log
```

---

## ⚠️ Pre-Flight Checklist

Trước khi start bot, đảm bảo:

- [ ] `.env` có private keys
- [ ] `.env` có quyền 600 (`chmod 600 .env`)
- [ ] Wallets có USDC + MATIC
- [ ] USDC đã approve: `python scripts/approve_wallets.py`
- [ ] Tests pass: `python tests/run_tests.py`
- [ ] `config.yaml` đã configure (capital, risk settings)

---

## 🔥 One-Liner Commands

```bash
# Full setup (run on fresh VPS)
wget https://raw.githubusercontent.com/nicolai200623/farmpoly/master/scripts/vps_setup.sh && chmod +x vps_setup.sh && ./vps_setup.sh

# Deploy bot (run in project dir)
cd ~/projects/farmpoly && chmod +x scripts/quick_deploy.sh && ./scripts/quick_deploy.sh

# Monitor bot
cd ~/projects/farmpoly && chmod +x scripts/monitor.sh && ./scripts/monitor.sh

# Restart & view logs
sudo systemctl restart farmpoly-bot && sudo journalctl -u farmpoly-bot -f
```

---

## 🆘 Troubleshooting

### Bot không start
```bash
# View errors
sudo journalctl -u farmpoly-bot -n 50

# Run manually
cd ~/projects/farmpoly
source venv/bin/activate
python main.py
```

### Playwright errors
```bash
source venv/bin/activate
pip install --force-reinstall playwright
playwright install chromium
sudo playwright install-deps chromium
```

### Permission errors
```bash
cd ~/projects/farmpoly
chmod 600 .env
chmod 755 logs data models backups
chmod +x scripts/*.sh
```

### Low memory
```bash
# Add 2GB swap
sudo fallocate -l 2G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
```

---

## 📚 Documentation

- **Full Guide:** `VPS_UBUNTU_DEPLOYMENT.md`
- **Quick Guide (Vietnamese):** `HUONG_DAN_VPS_NHANH.md`
- **Testing Guide:** `TESTNET_DEPLOYMENT.md`
- **User Manual:** `USER_GUIDE.md`

---

## 💡 Tips

1. **Start small:** $50-100 first
2. **Monitor closely:** Check every 30 min on day 1
3. **Use screen/tmux:** For persistent sessions
4. **Backup .env:** Keep private keys safe
5. **Update regularly:** `git pull` for latest code

---

## 🎯 After Deployment

### First Hour
- [ ] Check logs every 10 minutes
- [ ] Verify bot is scanning markets
- [ ] Check if orders are placed
- [ ] Monitor for errors

### First Day
- [ ] Check logs every hour
- [ ] Verify wallet balances
- [ ] Check PnL
- [ ] Monitor gas costs

### First Week
- [ ] Daily PnL review
- [ ] Optimize config if needed
- [ ] Scale up if profitable
- [ ] Adjust risk settings

---

## 🚨 Emergency Stop

```bash
# Stop bot immediately
sudo systemctl stop farmpoly-bot

# Cancel all orders (run in project dir)
cd ~/projects/farmpoly
source venv/bin/activate
python -c "
from py_clob_client.client import ClobClient
import os
from dotenv import load_dotenv

load_dotenv()

for i in range(1, 3):
    pk = os.getenv(f'WALLET_{i}_PK')
    if pk:
        client = ClobClient('https://clob.polymarket.com', key=pk)
        orders = client.get_orders()
        for order in orders:
            if order['status'] == 'OPEN':
                client.cancel_order(order['id'])
                print(f'Cancelled {order[\"id\"]}')
"
```

---

**Good luck! 🚀**

Need help? Check the full documentation in `VPS_UBUNTU_DEPLOYMENT.md`

