# 🔧 Tóm Tắt: Khắc Phục Lỗi psutil Trên VPS

## 📋 **Vấn Đề**

Bot đang chạy trên VPS Linux nhưng thiếu module `psutil`, gây ra lỗi:

```
ModuleNotFoundError: No module named 'psutil'
```

**Nguyên nhân**: 
- Module `psutil` đã được thêm vào `requirements.txt` trong lần tối ưu hóa
- Module đã được cài đặt trên máy **Windows local**
- Nhưng **chưa được cài đặt trên VPS Linux** (`/home/farmpoly/farmpoly/`)

---

## ✅ **Giải Pháp Nhanh** (Khuyến Nghị)

### **Cách 1: Chạy Quick Fix Script**

1. **SSH vào VPS:**
```bash
ssh user@your-vps-ip
```

2. **Di chuyển vào thư mục bot:**
```bash
cd /home/farmpoly/farmpoly
```

3. **Chạy quick fix script:**
```bash
bash scripts/quick_fix_vps.sh
```

4. **Restart bot:**
```bash
python3 main.py
```

---

### **Cách 2: Cài Đặt Thủ Công**

1. **SSH vào VPS:**
```bash
ssh user@your-vps-ip
```

2. **Di chuyển vào thư mục bot:**
```bash
cd /home/farmpoly/farmpoly
```

3. **Cài đặt psutil:**
```bash
pip3 install psutil --user
```

4. **Verify:**
```bash
python3 -c "import psutil; print('✅ OK')"
```

5. **Restart bot:**
```bash
python3 main.py
```

---

### **Cách 3: Cài Đặt Tất Cả Dependencies** (Khuyến Nghị Nhất)

1. **SSH vào VPS:**
```bash
ssh user@your-vps-ip
cd /home/farmpoly/farmpoly
```

2. **Chạy full installation script:**
```bash
bash scripts/vps_install_dependencies.sh
```

3. **Script sẽ tự động:**
   - ✅ Check Python & pip version
   - ✅ Upgrade pip
   - ✅ Cài đặt psutil
   - ✅ Cài đặt tất cả dependencies từ requirements.txt
   - ✅ Cài đặt Playwright browsers
   - ✅ Verify tất cả modules

4. **Restart bot:**
```bash
python3 main.py
```

---

## 🔍 **Verify Thành Công**

Sau khi cài đặt, check log để verify:

```bash
tail -f log.md
```

**Kết quả mong đợi:**
```
2025-11-03 XX:XX:XX - __main__ - INFO - ✅ Using MarketScannerV2 (Playwright + Gamma API)
2025-11-03 XX:XX:XX - monitoring_system - INFO - ✅ Monitoring System initialized
2025-11-03 XX:XX:XX - circuit_breaker - INFO - ✅ Circuit Breaker 'gamma_api' initialized
2025-11-03 XX:XX:XX - market_scanner_v2 - INFO - 🔍 Fetching from Gamma API...
2025-11-03 XX:XX:XX - market_scanner_v2 - INFO - ✅ Got 83 markets from API
```

**KHÔNG còn lỗi** `ModuleNotFoundError`!

---

## 📊 **Checklist**

- [ ] SSH vào VPS
- [ ] `cd /home/farmpoly/farmpoly`
- [ ] Chạy `bash scripts/quick_fix_vps.sh` HOẶC `pip3 install psutil --user`
- [ ] Verify: `python3 -c "import psutil; print('OK')"`
- [ ] Restart bot: `python3 main.py`
- [ ] Check log: `tail -f log.md`
- [ ] Verify không còn lỗi ModuleNotFoundError
- [ ] Verify bot tìm thấy ~83 markets

---

## 🚨 **Troubleshooting**

### **Nếu pip3 không tìm thấy:**
```bash
sudo apt-get update
sudo apt-get install -y python3-pip
```

### **Nếu pip install thất bại:**
```bash
pip3 install --upgrade pip --user
pip3 install psutil --user
```

### **Nếu vẫn lỗi sau khi cài:**
```bash
# Check Python path
which python3
python3 -m site

# Cài đặt trực tiếp
python3 -m pip install psutil --user
```

### **Check dependencies khác:**
```bash
python3 scripts/check_dependencies.py
```

---

## 📁 **Files Đã Tạo**

1. **VPS_FIX_INSTRUCTIONS.md** - Hướng dẫn chi tiết
2. **scripts/vps_install_dependencies.sh** - Full installation script
3. **scripts/quick_fix_vps.sh** - Quick fix script (chỉ cài psutil)
4. **scripts/check_dependencies.py** - Dependency verification script
5. **VPS_PSUTIL_FIX_SUMMARY.md** - File này

---

## 🎯 **Tóm Tắt**

| Vấn Đề | Nguyên Nhân | Giải Pháp | Status |
|--------|-------------|-----------|--------|
| ModuleNotFoundError: psutil | Chưa cài trên VPS | `pip3 install psutil --user` | ⏳ Chờ thực hiện |

**Thời gian ước tính**: 2-5 phút

**Độ khó**: ⭐ Dễ (chỉ cần chạy 1 lệnh)

---

## ✅ **Kết Quả Mong Đợi**

Sau khi hoàn thành:
- ✅ Bot chạy không lỗi
- ✅ Monitoring system hoạt động
- ✅ Circuit breaker hoạt động  
- ✅ Tìm thấy ~83 markets
- ✅ Hourly reports được gửi
- ✅ Health checks mỗi 30 giây

---

## 📞 **Cần Hỗ Trợ?**

Nếu vẫn gặp vấn đề, cung cấp:
1. Output của `python3 --version`
2. Output của `pip3 --version`
3. Output của `pip3 install psutil`
4. Log mới nhất: `tail -20 log.md`

