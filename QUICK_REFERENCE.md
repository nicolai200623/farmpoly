# 📋 QUICK REFERENCE - POLYMARKET FARMING BOT

---

## 🎯 **CÁC SCENARIOS PHỔ BIẾN**

### **Scenario 1: Testing với 1 ví, 100 USDC**

```yaml
# config.yaml
total_capital: 100
num_wallets: 1

# market_selection
max_concurrent_markets: 2  # Giảm xuống 2
```

**Approval:**
```bash
python scripts/approve_wallets.py
# Nhập: 100
```

**Kết quả:**
- ✅ Bot hoạt động
- ⚠️ Chỉ 1-2 markets cùng lúc
- ⚠️ Cần re-approve mỗi 1-2 ngày

---

### **Scenario 2: Small-scale với 3 ví, 500 USDC**

```yaml
# config.yaml
total_capital: 500
num_wallets: 3
# → Mỗi ví: $166 USDC

# market_selection
max_concurrent_markets: 5
```

**Approval:**
```bash
python scripts/approve_wallets.py
# Nhập: 1000  ← Approve 1,000 cho mỗi ví
```

**Kết quả:**
- ✅ Bot hoạt động tốt
- ✅ 3 × 5 = 15 markets tối đa
- ✅ Không cần re-approve thường xuyên

---

### **Scenario 3: Production với 10 ví, 5,000 USDC**

```yaml
# config.yaml
total_capital: 5000
num_wallets: 10
# → Mỗi ví: $500 USDC

# market_selection
max_concurrent_markets: 10
```

**Approval:**
```bash
python scripts/approve_wallets.py
# Nhập: 10000  ← Approve 10,000 cho mỗi ví
```

**Kết quả:**
- ✅ Bot hoạt động tối ưu
- ✅ 10 × 10 = 100 markets tối đa
- ✅ Không cần re-approve trong tháng

---

## 💰 **TÍNH TOÁN NHANH**

### **Vốn Cần Thiết Cho Mỗi Ví:**

```
Min Capital Per Wallet = 
    Max Concurrent Markets × $50

Ví dụ:
    max_concurrent_markets: 10
    → Min: 10 × $50 = $500/ví
```

### **Approval Khuyến Nghị:**

| Vốn/Ví | Approval Test | Approval Production |
|---------|---------------|---------------------|
| $100 | 100 USDC | 1,000 USDC |
| $200 | 200 USDC | 1,000 USDC |
| $500 | 500 USDC | 5,000 USDC |
| $1,000 | 1,000 USDC | 10,000 USDC |

**Quy tắc:** Approval = 5-10× vốn thực tế

---

## 🔧 **COMMANDS THƯỜNG DÙNG**

### **Check Approval Status:**
```bash
python scripts/check_approval_status.py
```

### **Approve Wallets:**
```bash
python scripts/approve_wallets.py
```

### **Start Bot:**
```bash
python main.py
```

### **Check Logs:**
```bash
tail -f log.md
```

### **Stop Bot:**
```bash
pkill -f main.py
```

---

## 📊 **HIỂU LOG OUTPUT**

### **Approval Check:**
```
🔍 Checking USDC approval for wallets...
   Checking wallet: 0x18F261DC...Ae4FfD96
   Raw allowance: 100000000 (base units)
   Allowance in USDC: 100.00 USDC
   Required minimum: 100 USDC (test mode)
✅ USDC approval OK (100 USDC)
   ⚠️  Running in TEST MODE with 100 USDC
```

**Ý nghĩa:**
- ✅ Approval đủ
- ⚠️ Đang test mode (< 1,000 USDC)

---

### **Market Scanning:**
```
🔍 Fetching from Gamma API...
✅ Got 118 markets from API
📊 Filter results: 15/118 markets passed
   - 83 rejected: reward < $50
   - 20 rejected: competition > 3
```

**Ý nghĩa:**
- 118 markets từ API
- 15 markets đủ điều kiện
- 103 markets bị reject

---

### **Market Selection:**
```
Selected 5 markets from 15 candidates
```

**Ý nghĩa:**
- Chọn 5 markets tốt nhất
- Từ 15 markets đủ điều kiện

---

### **Order Placement:**
```
Prepared order for market abc123 with spread 0.0080
✅ Placed YES order: 300 shares @ $0.54
✅ Placed NO order: 300 shares @ $0.45
```

**Ý nghĩa:**
- Đặt 2 orders (YES + NO)
- Spread: 0.8 cents
- Total capital: ~$297 USDC

---

## ⚠️ **TROUBLESHOOTING**

### **Lỗi: "USDC approval needed"**

**Nguyên nhân:** Allowance < 100 USDC

**Giải pháp:**
```bash
python scripts/approve_wallets.py
```

---

### **Lỗi: "Selected 0 markets"**

**Nguyên nhân:** Không có markets đủ điều kiện

**Giải pháp:**
```yaml
# Giảm threshold trong config.yaml
market_scanner:
  min_reward: 30  # Giảm từ 50
  max_competition_bars: 4  # Tăng từ 3
```

---

### **Lỗi: "RPC connection failed"**

**Nguyên nhân:** RPC endpoint không hoạt động

**Giải pháp:**
```yaml
# Đổi RPC trong config.yaml
rpc_url: "https://polygon-rpc.com"
```

---

### **Lỗi: "Insufficient balance"**

**Nguyên nhân:** Ví không đủ USDC

**Giải pháp:**
1. Check balance: `python scripts/check_approval_status.py`
2. Nạp thêm USDC vào ví

---

## 🎯 **CHECKLIST TRƯỚC KHI CHẠY BOT**

- [ ] ✅ Đã có ít nhất 1 ví với private key trong `.env`
- [ ] ✅ Mỗi ví có đủ USDC (≥ $100)
- [ ] ✅ Mỗi ví có đủ MATIC cho gas (≥ 0.5 MATIC)
- [ ] ✅ Đã approve USDC cho tất cả ví
- [ ] ✅ Đã config `total_capital` và `num_wallets` đúng
- [ ] ✅ Đã điều chỉnh `max_concurrent_markets` phù hợp
- [ ] ✅ Đã test với `python scripts/check_approval_status.py`

---

## 📈 **LỘ TRÌNH SCALE UP**

### **Week 1: Testing**
```
Vốn: $100
Ví: 1
Approval: 100 USDC
Markets: 1-2
Mục tiêu: Học cách dùng bot
```

### **Week 2-4: Small-scale**
```
Vốn: $500
Ví: 2-3
Approval: 1,000 USDC/ví
Markets: 10-15
Mục tiêu: Kiếm lợi nhuận nhỏ
```

### **Month 2+: Production**
```
Vốn: $2,000-5,000
Ví: 5-10
Approval: 10,000 USDC/ví
Markets: 50-100
Mục tiêu: Maximize profit
```

---

## 🔑 **KEY TAKEAWAYS**

1. **Approval ≠ Số tiền bị lock**
   - Approval = Hạn mức tối đa
   - Chỉ dùng số tiền có trong balance

2. **Mỗi ví cần approve riêng**
   - 5 ví = 5 lần approve
   - Script tự động approve tất cả

3. **Allowance chỉ giảm, không tăng**
   - Cancel order → allowance KHÔNG tăng
   - Order fill → allowance KHÔNG tăng
   - Cần approve số lớn từ đầu

4. **Multi-wallet tốt hơn single wallet**
   - Khó phát hiện
   - Risk phân tán
   - Throughput cao hơn

5. **Start small, scale up**
   - Test với $100 trước
   - Sau đó tăng dần
   - Không rush!

---

## 📞 **HỖ TRỢ**

Nếu gặp vấn đề:

1. **Check logs:** `tail -f log.md`
2. **Check approval:** `python scripts/check_approval_status.py`
3. **Read docs:** `POLYMARKET_FARMING_EXPLAINED.md`
4. **Ask for help** với logs đầy đủ

---

**Good luck farming! 🚀**

