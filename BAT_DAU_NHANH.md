# 🚀 Bắt Đầu Nhanh - Deploy Bot Lên VPS

## ⚡ 3 Bước Deploy (5 phút)

### Bước 1: Setup VPS
```bash
# SSH vào VPS
ssh your_user@YOUR_VPS_IP

# Download và chạy script setup
wget https://raw.githubusercontent.com/nicolai200623/farmpoly/master/scripts/vps_setup.sh
chmod +x vps_setup.sh
./vps_setup.sh
```

### Bước 2: Clone & Configure
```bash
# Clone repository
cd ~/projects
git clone https://github.com/nicolai200623/farmpoly.git
cd farmpoly

# Tạo file .env
cp .env.example .env
nano .env
```

**Thêm vào .env:**
```bash
USE_DEMO_WALLETS=false
WALLET_1_PK=0xYOUR_PRIVATE_KEY_1
WALLET_2_PK=0xYOUR_PRIVATE_KEY_2
POLYGON_RPC_URL=https://polygon-mainnet.g.alchemy.com/v2/YOUR_KEY
```

**Lưu:** `Ctrl+O` → `Enter` → `Ctrl+X`

### Bước 3: Deploy
```bash
# Chạy script deploy
chmod +x scripts/quick_deploy.sh
./scripts/quick_deploy.sh
```

**✅ XONG! Bot đã chạy!**

---

## 📊 Kiểm Tra Bot

### Xem Status
```bash
sudo systemctl status farmpoly-bot
```

### Xem Logs
```bash
tail -f ~/projects/farmpoly/logs/polymarket_bot.log
```

### Dashboard Monitoring
```bash
cd ~/projects/farmpoly
chmod +x scripts/monitor.sh
./scripts/monitor.sh
```

---

## 🎮 Quản Lý Bot

```bash
# Start bot
sudo systemctl start farmpoly-bot

# Stop bot
sudo systemctl stop farmpoly-bot

# Restart bot
sudo systemctl restart farmpoly-bot

# Xem logs
tail -f ~/projects/farmpoly/logs/polymarket_bot.log
```

---

## 📚 Tài Liệu Chi Tiết

### Chọn Hướng Dẫn Phù Hợp:

1. **VPS_QUICKSTART.md** - Deploy nhanh 5-15 phút
2. **VPS_UBUNTU_DEPLOYMENT.md** - Hướng dẫn đầy đủ 20-30 phút
3. **HUONG_DAN_VPS_NHANH.md** - Hướng dẫn tiếng Việt chi tiết
4. **DEPLOYMENT_INDEX.md** - Index tất cả tài liệu

### Scripts Hữu Ích:

- `scripts/vps_setup.sh` - Setup VPS tự động
- `scripts/quick_deploy.sh` - Deploy bot tự động
- `scripts/monitor.sh` - Dashboard monitoring
- `scripts/check_wallets.py` - Kiểm tra ví
- `scripts/approve_wallets.py` - Approve USDC

---

## ⚠️ Checklist Quan Trọng

Trước khi chạy bot:

- [ ] VPS Ubuntu 22.04 đã setup
- [ ] File `.env` đã có private keys
- [ ] Wallets có USDC + MATIC
- [ ] USDC đã approve (`python scripts/approve_wallets.py`)
- [ ] Tests đã pass (`python tests/run_tests.py`)
- [ ] Bot đã start (`sudo systemctl start farmpoly-bot`)

---

## 🆘 Gặp Vấn Đề?

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
source venv/bin/activate
pip install --force-reinstall playwright
playwright install chromium
sudo playwright install-deps chromium
```

### Thiếu memory
```bash
# Tạo swap 2GB
sudo fallocate -l 2G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
```

---

## 💡 Tips Quan Trọng

1. **Bắt đầu nhỏ:** Test với $50-100 trước
2. **Monitor thường xuyên:** Check logs mỗi 30 phút ngày đầu
3. **Backup .env:** Lưu private keys an toàn
4. **Dùng monitoring:** Chạy `./scripts/monitor.sh`
5. **Update thường xuyên:** `git pull` để có code mới

---

## 🎯 Sau Khi Deploy

### Ngày 1
- Check logs mỗi 30 phút
- Verify orders được place
- Monitor errors
- Check wallet balances

### Tuần 1
- Review PnL hàng ngày
- Analyze fill rate
- Optimize config nếu cần
- Check gas costs

### Tháng 1
- Nếu profitable: tăng capital 50%
- Nếu loss: optimize hoặc dừng
- Review strategy

---

## 📞 Cần Trợ Giúp?

### Xem Tài Liệu
- **DEPLOYMENT_INDEX.md** - Index tất cả tài liệu
- **VPS_UBUNTU_DEPLOYMENT.md** - Hướng dẫn đầy đủ
- **HUONG_DAN_VPS_NHANH.md** - Hướng dẫn tiếng Việt

### Xem Logs
```bash
# Bot logs
tail -f ~/projects/farmpoly/logs/polymarket_bot.log

# System logs
sudo journalctl -u farmpoly-bot -f

# Tìm errors
grep "ERROR" ~/projects/farmpoly/logs/polymarket_bot.log
```

---

**Chúc bạn thành công! 🚀**

Bắt đầu với 3 bước trên, sau đó đọc tài liệu chi tiết nếu cần.

