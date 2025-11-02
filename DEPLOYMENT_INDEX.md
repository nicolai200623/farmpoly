# 📚 Farmpoly Bot - Deployment Documentation Index

## 🎯 Chọn Hướng Dẫn Phù Hợp

### 🚀 Bạn muốn deploy trên VPS Ubuntu?
→ **[VPS_QUICKSTART.md](VPS_QUICKSTART.md)** - Deploy trong 5-15 phút  
→ **[VPS_UBUNTU_DEPLOYMENT.md](VPS_UBUNTU_DEPLOYMENT.md)** - Hướng dẫn chi tiết đầy đủ  
→ **[HUONG_DAN_VPS_NHANH.md](HUONG_DAN_VPS_NHANH.md)** - Hướng dẫn tiếng Việt

### 🧪 Bạn muốn test trước khi deploy?
→ **[TESTNET_DEPLOYMENT.md](TESTNET_DEPLOYMENT.md)** - Test với demo mode hoặc vốn nhỏ

### 📖 Bạn muốn hiểu cách sử dụng bot?
→ **[USER_GUIDE.md](USER_GUIDE.md)** - Hướng dẫn sử dụng chi tiết  
→ **[QUICKSTART.md](QUICKSTART.md)** - Bắt đầu nhanh

### 🔧 Bạn muốn setup từ đầu?
→ **[SETUP_GUIDE.md](SETUP_GUIDE.md)** - Hướng dẫn setup đầy đủ

### 📊 Bạn muốn xem tổng quan dự án?
→ **[PROJECT_OVERVIEW.md](PROJECT_OVERVIEW.md)** - Tổng quan kiến trúc  
→ **[DEPLOYMENT_SUMMARY.md](DEPLOYMENT_SUMMARY.md)** - Tóm tắt deployment

---

## 📋 Tài Liệu Theo Mục Đích

### 1️⃣ Deploy Lên VPS (Ubuntu 22.04)

| File | Mô Tả | Thời Gian | Độ Khó |
|------|-------|-----------|--------|
| **VPS_QUICKSTART.md** | Deploy siêu nhanh với scripts tự động | 5-15 phút | ⭐ Dễ |
| **VPS_UBUNTU_DEPLOYMENT.md** | Hướng dẫn chi tiết từng bước | 20-30 phút | ⭐⭐ Trung bình |
| **HUONG_DAN_VPS_NHANH.md** | Hướng dẫn tiếng Việt, dễ hiểu | 15-20 phút | ⭐ Dễ |

**Khuyến nghị:** Bắt đầu với **VPS_QUICKSTART.md** nếu bạn muốn nhanh nhất.

---

### 2️⃣ Testing & Demo

| File | Mô Tả | Phù Hợp Với |
|------|-------|-------------|
| **TESTNET_DEPLOYMENT.md** | Test với demo mode hoặc vốn nhỏ | Người mới, muốn test an toàn |

**3 Options:**
- **Option 1:** Demo Mode - Không cần tiền thật
- **Option 2:** Small Capital Test - Test với $50-100
- **Option 3:** Component Testing - Test từng module

---

### 3️⃣ Setup & Configuration

| File | Mô Tả | Khi Nào Dùng |
|------|-------|--------------|
| **SETUP_GUIDE.md** | Setup đầy đủ từ A-Z | Setup lần đầu trên máy local |
| **QUICKSTART.md** | Bắt đầu nhanh | Đã có môi trường Python |
| **config.yaml** | File cấu hình bot | Customize bot behavior |

---

### 4️⃣ User Guides

| File | Mô Tả | Nội Dung |
|------|-------|----------|
| **USER_GUIDE.md** | Hướng dẫn sử dụng đầy đủ | Cách dùng, monitoring, troubleshooting |
| **PROJECT_OVERVIEW.md** | Tổng quan dự án | Kiến trúc, modules, workflow |

---

### 5️⃣ Scripts & Automation

| Script | Mô Tả | Sử Dụng |
|--------|-------|---------|
| **scripts/vps_setup.sh** | Setup VPS tự động | `./vps_setup.sh` |
| **scripts/quick_deploy.sh** | Deploy bot tự động | `./quick_deploy.sh` |
| **scripts/monitor.sh** | Monitoring dashboard | `./monitor.sh` |
| **scripts/check_wallets.py** | Kiểm tra ví | `python scripts/check_wallets.py` |
| **scripts/approve_wallets.py** | Approve USDC | `python scripts/approve_wallets.py` |

**Chi tiết:** Xem [scripts/README.md](scripts/README.md)

---

## 🎯 Workflow Khuyến Nghị

### Cho Người Mới Bắt Đầu

```
1. Đọc PROJECT_OVERVIEW.md (hiểu bot làm gì)
   ↓
2. Đọc TESTNET_DEPLOYMENT.md (test demo mode)
   ↓
3. Chạy tests: python tests/run_tests.py
   ↓
4. Test với vốn nhỏ ($50-100)
   ↓
5. Deploy lên VPS: VPS_QUICKSTART.md
   ↓
6. Monitor & optimize
```

### Cho Người Có Kinh Nghiệm

```
1. Clone repo
   ↓
2. Đọc VPS_QUICKSTART.md
   ↓
3. Run: ./scripts/vps_setup.sh
   ↓
4. Configure .env & config.yaml
   ↓
5. Run: ./scripts/quick_deploy.sh
   ↓
6. Monitor: ./scripts/monitor.sh
```

---

## 📖 Chi Tiết Từng File

### VPS_QUICKSTART.md
**Mục đích:** Deploy nhanh nhất có thể  
**Nội dung:**
- 2 cách deploy (tự động & thủ công)
- One-liner commands
- Troubleshooting nhanh
- Emergency stop procedures

**Dùng khi:** Bạn cần deploy ngay, có VPS sẵn

---

### VPS_UBUNTU_DEPLOYMENT.md
**Mục đích:** Hướng dẫn chi tiết, đầy đủ  
**Nội dung:**
- 8 bước setup chi tiết
- Systemd service configuration
- Security hardening
- Log rotation
- Monitoring setup
- Troubleshooting đầy đủ

**Dùng khi:** Bạn muốn hiểu rõ từng bước, setup production

---

### HUONG_DAN_VPS_NHANH.md
**Mục đích:** Hướng dẫn tiếng Việt, dễ hiểu  
**Nội dung:**
- Tương tự VPS_UBUNTU_DEPLOYMENT.md
- Ngôn ngữ tiếng Việt
- Giải thích chi tiết hơn
- Tips & tricks

**Dùng khi:** Bạn thích đọc tiếng Việt

---

### TESTNET_DEPLOYMENT.md
**Mục đích:** Test an toàn trước khi deploy  
**Nội dung:**
- Demo mode (không cần tiền)
- Small capital test ($50-100)
- Component testing
- Success checklist

**Dùng khi:** Lần đầu dùng bot, muốn test

---

### SETUP_GUIDE.md
**Mục đích:** Setup từ đầu trên máy local  
**Nội dung:**
- Cài Python, dependencies
- Setup wallets
- Configure bot
- Run tests

**Dùng khi:** Setup lần đầu, development

---

### USER_GUIDE.md
**Mục đích:** Hướng dẫn sử dụng hàng ngày  
**Nội dung:**
- Cách start/stop bot
- Monitoring
- Troubleshooting
- Best practices

**Dùng khi:** Bot đã chạy, cần quản lý

---

### PROJECT_OVERVIEW.md
**Mục đích:** Hiểu kiến trúc bot  
**Nội dung:**
- 8 modules chính
- Workflow
- Features
- Technical details

**Dùng khi:** Muốn hiểu bot hoạt động như thế nào

---

## 🚀 Quick Start Paths

### Path 1: Fastest (5 minutes)
```bash
# On VPS
wget https://raw.githubusercontent.com/nicolai200623/farmpoly/master/scripts/vps_setup.sh
chmod +x vps_setup.sh && ./vps_setup.sh

cd ~/projects
git clone https://github.com/nicolai200623/farmpoly.git
cd farmpoly

# Configure .env
cp .env.example .env
nano .env  # Add private keys

# Deploy
chmod +x scripts/quick_deploy.sh
./scripts/quick_deploy.sh
```

### Path 2: Safe Testing (30 minutes)
```bash
# Read first
cat TESTNET_DEPLOYMENT.md

# Test demo mode
USE_DEMO_WALLETS=true python main.py

# Test with small capital
# Follow TESTNET_DEPLOYMENT.md Option 2
```

### Path 3: Full Setup (1 hour)
```bash
# Read documentation
cat VPS_UBUNTU_DEPLOYMENT.md

# Follow step by step
# Manual setup for full control
```

---

## 📞 Support & Resources

### Documentation
- All `.md` files in root directory
- `scripts/README.md` for script details
- Inline comments in code

### Troubleshooting
- Check logs: `tail -f logs/polymarket_bot.log`
- Run tests: `python tests/run_tests.py`
- View errors: `sudo journalctl -u farmpoly-bot -n 50`

### Community
- GitHub Issues
- Discord (if available)

---

## ✅ Checklist Tổng Hợp

### Pre-Deployment
- [ ] Đọc PROJECT_OVERVIEW.md
- [ ] Đọc deployment guide phù hợp
- [ ] Có VPS Ubuntu 22.04 (nếu deploy VPS)
- [ ] Có 2+ wallets với private keys
- [ ] Có USDC + MATIC trong wallets
- [ ] Có Alchemy/Infura RPC key

### During Deployment
- [ ] VPS updated & secured
- [ ] Dependencies installed
- [ ] .env configured
- [ ] config.yaml configured
- [ ] Tests passed
- [ ] USDC approved
- [ ] Bot started

### Post-Deployment
- [ ] Logs monitoring
- [ ] Wallets checked
- [ ] Orders verified
- [ ] Performance tracked
- [ ] Backups setup

---

**Chúc bạn deploy thành công! 🚀**

Bắt đầu với file phù hợp nhất với nhu cầu của bạn từ danh sách trên.

