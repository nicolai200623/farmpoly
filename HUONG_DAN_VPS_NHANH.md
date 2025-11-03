# 🚀 Hướng Dẫn Deploy Nhanh trên VPS Ubuntu 22.04

## 📌 Tóm Tắt Nhanh

Hướng dẫn này giúp bạn deploy Farmpoly bot lên VPS Ubuntu 22.04.5 LTS trong **15-20 phút**.

---

## ⚡ Cách 1: Deploy Tự Động (Khuyến Nghị)

### Bước 1: Kết nối VPS

```bash
ssh your_username@YOUR_VPS_IP
```

### Bước 2: Chạy Script Setup

```bash
# Download và chạy script setup
curl -o vps_setup.sh https://raw.githubusercontent.com/nicolai200623/farmpoly/master/scripts/vps_setup.sh
chmod +x vps_setup.sh
./vps_setup.sh
```

### Bước 3: Clone Repository

```bash
cd ~/projects
git clone https://github.com/nicolai200623/farmpoly.git
cd farmpoly
```

### Bước 4: Cấu Hình

```bash
# Copy file .env
cp .env.example .env

# Chỉnh sửa .env (thêm private keys)
nano .env
```

**Nội dung cần thêm vào `.env`:**
```bash
USE_DEMO_WALLETS=false
WALLET_1_PK=0xYOUR_PRIVATE_KEY_HERE
WALLET_2_PK=0xYOUR_PRIVATE_KEY_HERE
POLYGON_RPC_URL=https://polygon-mainnet.g.alchemy.com/v2/YOUR_KEY
```

**Lưu file:** `Ctrl+O`, `Enter`, `Ctrl+X`

### Bước 5: Deploy

```bash
# Chạy script deploy tự động
chmod +x scripts/quick_deploy.sh
./scripts/quick_deploy.sh
```

Script sẽ tự động:
- ✅ Tạo virtual environment
- ✅ Cài đặt dependencies
- ✅ Chạy tests
- ✅ Tạo systemd service
- ✅ Start bot

### Bước 6: Kiểm Tra

```bash
# Xem trạng thái bot
sudo systemctl status farmpoly-bot

# Xem logs
tail -f logs/polymarket_bot.log
```

**✅ XONG! Bot đã chạy!**

---

## 🔧 Cách 2: Deploy Thủ Công

### 1. Chuẩn Bị VPS

```bash
# Update hệ thống
sudo apt update && sudo apt upgrade -y

# Cài tools cơ bản
sudo apt install -y git curl wget vim htop python3 python3-pip python3-venv
```

### 2. Cài Dependencies cho Playwright

```bash
sudo apt install -y \
    libnss3 libnspr4 libatk1.0-0 libatk-bridge2.0-0 \
    libcups2 libdrm2 libdbus-1-3 libxkbcommon0 \
    libxcomposite1 libxdamage1 libxfixes3 libxrandr2 \
    libgbm1 libpango-1.0-0 libcairo2 libasound2 \
    fonts-liberation
```

### 3. Clone Project

```bash
mkdir -p ~/projects
cd ~/projects
git clone https://github.com/nicolai200623/farmpoly.git
cd farmpoly
```

### 4. Setup Virtual Environment

```bash
# Tạo venv
python3 -m venv venv

# Activate
source venv/bin/activate

# Cài packages
pip install --upgrade pip
pip install -r requirements.txt

# Cài Playwright
playwright install chromium
```

### 5. Cấu Hình

```bash
# Tạo .env
cp .env.example .env
nano .env

# Thêm private keys và RPC URL
# Lưu: Ctrl+O, Enter, Ctrl+X

# Bảo mật .env
chmod 600 .env

# Tạo thư mục
mkdir -p logs data models backups
```

### 6. Test

```bash
# Chạy tests
python tests/run_tests.py

# Test import
python -c "from market_scanner_v2 import MarketScannerV2; print('OK')"
```

### 7. Tạo Systemd Service

```bash
# Tạo file service
sudo nano /etc/systemd/system/farmpoly-bot.service
```

**Nội dung (thay `your_username` bằng username của bạn):**

```ini
[Unit]
Description=Farmpoly Polymarket Trading Bot
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/home/farmpoly/farmpoly
Environment="PATH=/home/farmpoly/farmpoly/venv/bin"
ExecStart=/home/farmpoly/farmpoly/venv/bin/python main.py
Restart=always
RestartSec=10
StandardOutput=append:/home/farmpoly/farmpoly/logs/systemd.log
StandardError=append:/home/farmpoly/farmpoly/logs/systemd-error.log

[Install]
WantedBy=multi-user.target
```

### 8. Start Bot

```bash
# Reload systemd
sudo systemctl daemon-reload

# Enable auto-start
sudo systemctl enable farmpoly-bot

# Start bot
sudo systemctl start farmpoly-bot

# Check status
sudo systemctl status farmpoly-bot
```

---

## 📊 Monitoring

### Dashboard Tự Động

```bash
# Chạy monitoring dashboard
cd ~/projects/farmpoly
chmod +x scripts/monitor.sh
./scripts/monitor.sh
```

### Lệnh Thủ Công

```bash
# Xem logs real-time
tail -f ~/projects/farmpoly/logs/polymarket_bot.log

# Xem system logs
sudo journalctl -u farmpoly-bot -f

# Check status
sudo systemctl status farmpoly-bot

# Check wallets
cd ~/projects/farmpoly
source venv/bin/activate
python scripts/check_wallets.py
```

---

## 🎮 Quản Lý Bot

### Start/Stop/Restart

```bash
# Start
sudo systemctl start farmpoly-bot

# Stop
sudo systemctl stop farmpoly-bot

# Restart
sudo systemctl restart farmpoly-bot

# Status
sudo systemctl status farmpoly-bot
```

### Update Code

```bash
# Stop bot
sudo systemctl stop farmpoly-bot

# Pull latest code
cd ~/projects/farmpoly
git pull

# Restart bot
sudo systemctl start farmpoly-bot
```

---

## ⚠️ Checklist Trước Khi Chạy

- [ ] VPS đã update (`sudo apt update && sudo apt upgrade`)
- [ ] Python 3.9+ đã cài (`python3 --version`)
- [ ] Dependencies đã cài (`pip list`)
- [ ] Playwright browsers đã cài (`playwright install chromium`)
- [ ] File `.env` đã có private keys
- [ ] File `.env` có quyền 600 (`chmod 600 .env`)
- [ ] Wallets đã có USDC + MATIC
- [ ] USDC đã approve (`python scripts/approve_wallets.py`)
- [ ] Tests đã pass (`python tests/run_tests.py`)
- [ ] Systemd service đã tạo
- [ ] Bot đã start (`sudo systemctl start farmpoly-bot`)

---

## 🔥 Lệnh Hay Dùng

```bash
# Xem logs 100 dòng cuối
tail -n 100 ~/projects/farmpoly/logs/polymarket_bot.log

# Tìm errors trong logs
grep "ERROR" ~/projects/farmpoly/logs/polymarket_bot.log

# Xem resource usage
htop

# Xem disk space
df -h

# Xem memory
free -h

# Restart bot nhanh
sudo systemctl restart farmpoly-bot && sudo journalctl -u farmpoly-bot -f
```

---

## 🆘 Troubleshooting

### Bot không start

```bash
# Xem lỗi
sudo journalctl -u farmpoly-bot -n 50

# Chạy thủ công để debug
cd ~/projects/farmpoly
source venv/bin/activate
python main.py
```

### Playwright lỗi

```bash
# Reinstall Playwright
source venv/bin/activate
pip install --force-reinstall playwright
playwright install chromium

# Cài system dependencies
sudo playwright install-deps chromium
```

### Thiếu memory

```bash
# Tạo swap file 2GB
sudo fallocate -l 2G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile

# Make permanent
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
```

### Permission denied

```bash
# Fix permissions
cd ~/projects/farmpoly
chmod 600 .env
chmod 755 logs data models backups
chmod +x scripts/*.sh
```

---

## 📞 Liên Hệ & Tài Liệu

### Tài Liệu Chi Tiết

- `VPS_UBUNTU_DEPLOYMENT.md` - Hướng dẫn đầy đủ
- `TESTNET_DEPLOYMENT.md` - Hướng dẫn test
- `USER_GUIDE.md` - Hướng dẫn sử dụng
- `config.yaml` - Cấu hình bot

### Scripts Hữu Ích

- `scripts/vps_setup.sh` - Setup VPS tự động
- `scripts/quick_deploy.sh` - Deploy nhanh
- `scripts/monitor.sh` - Monitoring dashboard
- `scripts/check_wallets.py` - Kiểm tra ví
- `scripts/approve_wallets.py` - Approve USDC

---

## 💡 Tips

1. **Bắt đầu nhỏ:** Test với $50-100 trước
2. **Monitor thường xuyên:** Check logs mỗi 30 phút trong ngày đầu
3. **Backup:** Backup `.env` và `config.yaml` thường xuyên
4. **Security:** Không share private keys, dùng SSH keys thay password
5. **Updates:** Pull code mới thường xuyên (`git pull`)

---

## 🎯 Sau Khi Deploy

### Ngày 1: Monitor Sát

- Check logs mỗi 30 phút
- Verify orders được place
- Check wallet balances
- Monitor errors

### Tuần 1: Đánh Giá

- Review PnL
- Analyze fill rate
- Check gas costs
- Optimize config nếu cần

### Tháng 1: Scale

- Nếu profitable: tăng capital 50%
- Nếu loss: optimize hoặc dừng
- Review và adjust strategy

---

**Chúc bạn thành công! 🚀**

Nếu có vấn đề, check logs và documentation chi tiết trong `VPS_UBUNTU_DEPLOYMENT.md`

