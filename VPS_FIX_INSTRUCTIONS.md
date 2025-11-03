# 🔧 Hướng Dẫn Khắc Phục Lỗi psutil Trên VPS

## 🎯 Vấn Đề

Bot đang chạy trên VPS Linux (`/home/farmpoly/farmpoly/`) nhưng thiếu module `psutil`.

Log cho thấy:
```
File "/home/farmpoly/farmpoly/monitoring_system.py", line 11, in <module>
    import psutil
ModuleNotFoundError: No module named 'psutil'
```

---

## ✅ Giải Pháp

### **Bước 1: SSH vào VPS**

```bash
ssh user@your-vps-ip
# Hoặc dùng PuTTY nếu trên Windows
```

### **Bước 2: Di chuyển vào thư mục bot**

```bash
cd /home/farmpoly/farmpoly
```

### **Bước 3: Cài đặt psutil**

**Option A: Cài đặt chỉ psutil**
```bash
pip install psutil
# Hoặc nếu dùng pip3
pip3 install psutil
```

**Option B: Cài đặt tất cả dependencies từ requirements.txt** (Khuyến nghị)
```bash
pip install -r requirements.txt
# Hoặc
pip3 install -r requirements.txt
```

### **Bước 4: Verify cài đặt thành công**

```bash
python3 -c "import psutil; print(f'✅ psutil version: {psutil.__version__}')"
```

Kết quả mong đợi:
```
✅ psutil version: 7.1.3
```

### **Bước 5: Restart bot**

```bash
# Nếu bot đang chạy với systemd
sudo systemctl restart farmpoly

# Hoặc nếu chạy với screen/tmux
# Kill process cũ và chạy lại
pkill -f main.py
python3 main.py
```

---

## 🔍 Kiểm Tra Thêm

### **Check Python version trên VPS:**
```bash
python3 --version
```

### **Check pip version:**
```bash
pip3 --version
```

### **Check tất cả dependencies:**
```bash
python3 scripts/check_dependencies.py
```

### **Check log để verify bot chạy thành công:**
```bash
tail -f log.md
# Hoặc
tail -f logs/polymarket_bot.log
```

---

## 📊 Expected Output Sau Khi Fix

Khi bot chạy thành công, bạn sẽ thấy:

```
2025-11-03 XX:XX:XX - __main__ - INFO - ✅ Using MarketScannerV2 (Playwright + Gamma API)
2025-11-03 XX:XX:XX - monitoring_system - INFO - ✅ Monitoring System initialized
2025-11-03 XX:XX:XX - circuit_breaker - INFO - ✅ Circuit Breaker 'gamma_api' initialized
2025-11-03 XX:XX:XX - circuit_breaker - INFO - ✅ Circuit Breaker 'playwright_scraper' initialized
2025-11-03 XX:XX:XX - market_scanner_v2 - INFO - 🔍 Fetching from Gamma API...
2025-11-03 XX:XX:XX - market_scanner_v2 - INFO - ✅ Got 83 markets from API
```

**KHÔNG còn lỗi** `ModuleNotFoundError: No module named 'psutil'`

---

## 🚨 Troubleshooting

### **Nếu pip install thất bại:**

1. **Update pip:**
```bash
pip3 install --upgrade pip
```

2. **Cài đặt với user flag:**
```bash
pip3 install --user psutil
```

3. **Dùng sudo (nếu có quyền):**
```bash
sudo pip3 install psutil
```

### **Nếu vẫn lỗi sau khi cài:**

1. **Check Python path:**
```bash
which python3
python3 -m site
```

2. **Cài đặt trực tiếp vào Python path:**
```bash
python3 -m pip install psutil
```

3. **Check xem có nhiều Python versions:**
```bash
ls -la /usr/bin/python*
```

---

## 📝 Alternative: Tạm Thời Disable Monitoring

Nếu không thể cài psutil ngay, bạn có thể tạm thời disable monitoring system:

### **Sửa file main.py trên VPS:**

```python
# Comment out monitoring import
# from monitoring_system import MonitoringSystem

# Comment out monitoring initialization trong _initialize_modules()
# self.modules['monitoring'] = MonitoringSystem(...)

# Comment out monitoring loops trong run()
# self._monitoring_loop(),
# self._hourly_report_loop()
```

**Lưu ý**: Cách này chỉ nên dùng tạm thời. Monitoring system rất hữu ích để theo dõi bot!

---

## ✅ Checklist

- [ ] SSH vào VPS
- [ ] `cd /home/farmpoly/farmpoly`
- [ ] `pip3 install psutil` hoặc `pip3 install -r requirements.txt`
- [ ] `python3 -c "import psutil; print('OK')"`
- [ ] Restart bot
- [ ] Check log: `tail -f log.md`
- [ ] Verify không còn lỗi ModuleNotFoundError

---

## 🎉 Kết Quả Mong Đợi

Sau khi hoàn thành:
- ✅ Bot chạy không lỗi
- ✅ Monitoring system hoạt động
- ✅ Circuit breaker hoạt động
- ✅ Tìm thấy ~83 markets
- ✅ Hourly reports được gửi

---

## 📞 Nếu Cần Hỗ Trợ

Nếu vẫn gặp vấn đề, hãy cung cấp:
1. Output của `python3 --version`
2. Output của `pip3 --version`
3. Output của `pip3 install psutil`
4. Log mới nhất từ `tail -20 log.md`

