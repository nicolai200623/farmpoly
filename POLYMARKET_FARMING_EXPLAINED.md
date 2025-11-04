# 📚 HƯỚNG DẪN TOÀN DIỆN: POLYMARKET FARMING BOT

---

## 1️⃣ **QUY TRÌNH HOẠT ĐỘNG CỦA BOT**

### **🔍 A. Market Scanning (Quét Markets)**

Bot quét markets theo chu kỳ **5 giây** (có thể điều chỉnh):

```
┌─────────────────────────────────────────────────────────┐
│  BƯỚC 1: Fetch Markets từ 2 nguồn                       │
├─────────────────────────────────────────────────────────┤
│  ✅ Nguồn 1: Gamma API (ưu tiên)                        │
│     - URL: https://gamma-api.polymarket.com/events      │
│     - Tốc độ: Nhanh (~1-2 giây)                         │
│     - Độ tin cậy: Cao                                   │
│                                                          │
│  ⚠️  Nguồn 2: Playwright Scraping (fallback)            │
│     - URL: https://polymarket.com/rewards               │
│     - Tốc độ: Chậm (~10-15 giây)                        │
│     - Chỉ dùng khi API fail                             │
└─────────────────────────────────────────────────────────┘
```

**Ví dụ kết quả scan:**
```
🔍 Fetching from Gamma API...
✅ Got 118 markets from API
📊 Filter results: 15/118 markets passed
```

---

### **🎯 B. Market Selection (Chọn Markets)**

Bot lọc markets dựa trên **nhiều tiêu chí**:

#### **Bộ Lọc Cơ Bản:**

| Tiêu Chí | Giá Trị | Ý Nghĩa |
|----------|---------|---------|
| **Min Reward** | ≥ $50 | Phần thưởng tối thiểu |
| **Max Competition** | ≤ 3 bars | Cạnh tranh không quá cao |
| **Min Shares** | ≤ 500 | Yêu cầu shares không quá lớn |

#### **Hệ Thống Scoring AI:**

Bot tính điểm cho mỗi market dựa trên **7 yếu tố**:

```python
Total Score = 
    25% × Reward Score          # Phần thưởng cao = điểm cao
  + 20% × Competition Score     # Cạnh tranh thấp = điểm cao
  + 15% × Volume Spike Score    # Volume tăng đột biến = điểm cao
  + 10% × Liquidity Score       # Thanh khoản thấp = điểm cao (dễ farm)
  + 10% × Category Score        # Sports/Crypto = điểm cao
  + 10% × Price Efficiency      # Spread tốt = điểm cao
  + 10% × Timing Score          # Gần deadline = điểm cao
```

**Bonus điểm:**
- ✅ Sports markets: +20%
- ✅ Illiquid markets (< $5k): +15%

**Ví dụ:**
```
Market A: "Will Lakers win tonight?"
  - Reward: $200 → Score: 0.8
  - Competition: 1 bar → Score: 0.9
  - Category: Sports → Bonus +20%
  → Total Score: 0.85 → ✅ SELECTED

Market B: "Bitcoin price prediction"
  - Reward: $50 → Score: 0.3
  - Competition: 4 bars → Score: 0.2
  → Total Score: 0.25 → ❌ REJECTED
```

---

### **📊 C. Order Placement (Đặt Lệnh)**

Bot sử dụng chiến lược **Market Making** (cung cấp thanh khoản 2 bên):

#### **Cách Hoạt Động:**

```
Market: "Will Lakers win tonight?"
Current Price: $0.55 (55% YES, 45% NO)

Bot đặt 2 orders đồng thời:
┌──────────────────────────────────────────────┐
│  YES Order (Buy)                             │
│  - Price: $0.54 (mid - spread)               │
│  - Size: 300 shares                          │
│  - Value: 300 × $0.54 = $162 USDC            │
├──────────────────────────────────────────────┤
│  NO Order (Buy)                              │
│  - Price: $0.45 (1 - mid - spread)           │
│  - Size: 300 shares                          │
│  - Value: 300 × $0.45 = $135 USDC            │
└──────────────────────────────────────────────┘

Total Capital Locked: $162 + $135 = $297 USDC
```

#### **Dynamic Spread:**

Bot tự động điều chỉnh spread dựa trên:
- **Volatility:** Biến động cao → spread lớn (0.015)
- **Liquidity:** Thanh khoản thấp → spread nhỏ (0.005)
- **Competition:** Cạnh tranh cao → spread nhỏ

**Ví dụ:**
```
Low volatility market: Spread = 0.005 (0.5 cents)
High volatility market: Spread = 0.015 (1.5 cents)
```

---

### **🛡️ D. Position Management (Quản Lý Vị Thế)**

Bot monitor positions **real-time** qua WebSocket và tự động cancel nếu:

#### **Điều Kiện Auto-Cancel:**

| Điều Kiện | Threshold | Lý Do |
|-----------|-----------|-------|
| **Partial Fill** | > 10% filled | Tránh bị fill không mong muốn |
| **Volume Spike** | Volume tăng > 2x | Market đang "nóng", rủi ro cao |
| **Price Movement** | Giá di chuyển > 2 cents | Giá không còn hợp lý |
| **Time Limit** | > 1 giờ | Order quá lâu, cancel và re-place |

**Ví dụ:**
```
Order placed: YES @ $0.54, size 300
After 10 minutes: 50 shares filled (16.7%)
→ ❌ AUTO-CANCEL (partial fill > 10%)
→ Bot re-place order mới với giá tốt hơn
```

---

### **💰 E. Reward Claiming (Claim Phần Thưởng)**

**⚠️ QUAN TRỌNG:** Bot hiện tại **KHÔNG TỰ ĐỘNG CLAIM** rewards!

Lý do:
- Polymarket rewards phức tạp, có nhiều loại
- Cần manual verification để tránh nhầm lẫn
- Đang disable trong config: `reward_management.enabled: false`

**Cách claim thủ công:**
1. Vào https://polymarket.com/rewards
2. Check rewards available
3. Click "Claim" manually
4. Withdraw về wallet

---

## 2️⃣ **CHIẾN LƯỢC FARMING VỚI NHIỀU VÍ**

### **🤔 Tại Sao Cần Nhiều Ví?**

#### **Lý Do 1: Tránh Detection**

Polymarket có thể phát hiện và giới hạn bot nếu:
- 1 ví đặt quá nhiều orders
- 1 ví trade quá thường xuyên
- Pattern giống bot (orders đều đặn, timing giống nhau)

**Giải pháp:** Rotate giữa nhiều ví → Mỗi ví ít orders hơn → Khó phát hiện

#### **Lý Do 2: Tăng Throughput**

Với 1 ví:
```
Max concurrent markets: 10
Capital per market: 5% × $1000 = $50
Total exposure: 10 × $50 = $500 USDC
```

Với 5 ví:
```
Each wallet: $200 USDC
Max concurrent markets per wallet: 10
Total markets: 5 × 10 = 50 markets
Total exposure: 5 × $500 = $2,500 USDC
```

#### **Lý Do 3: Risk Diversification**

Nếu 1 ví bị:
- Hack
- Frozen
- Rate limited

→ Các ví khác vẫn hoạt động bình thường

---

### **💵 Vốn Tối Thiểu Cho Mỗi Ví**

#### **Công Thức Tính:**

```
Min Capital Per Wallet = 
    (Max Concurrent Markets) × (Capital Per Market)

Với config mặc định:
    = 10 markets × (5% × Total Capital)
    = 10 × 0.05 × Total Capital
    = 0.5 × Total Capital
```

#### **Ví Dụ Cụ Thể:**

| Total Capital | Num Wallets | Capital/Wallet | Max Markets/Wallet | Total Markets |
|---------------|-------------|----------------|-------------------|---------------|
| $100 | 1 | $100 | 2 | 2 |
| $500 | 2 | $250 | 5 | 10 |
| $1,000 | 5 | $200 | 4 | 20 |
| $5,000 | 10 | $500 | 10 | 100 |

**Khuyến nghị:**
- **Testing:** 1 ví, $100 USDC
- **Small-scale:** 2-3 ví, $200-300/ví
- **Production:** 5-10 ví, $500-1000/ví

---

### **📊 Phân Bổ Vốn Giữa Các Ví**

Bot tự động phân bổ **đều** giữa các ví:

```python
# Trong config.yaml
total_capital: 1000  # $1,000 USDC
num_wallets: 5       # 5 wallets

# Bot tự động tính:
capital_per_wallet = 1000 / 5 = $200 USDC/wallet
```

**Rotation Strategy:**

Bot rotate ví theo **round-robin**:
```
Scan 1: Market A → Wallet 1
Scan 2: Market B → Wallet 2
Scan 3: Market C → Wallet 3
Scan 4: Market D → Wallet 4
Scan 5: Market E → Wallet 5
Scan 6: Market F → Wallet 1 (quay lại)
```

---

### **🔐 Approval Cho Từng Ví**

**CÓ!** Mỗi ví cần approve USDC **riêng biệt**.

#### **Ví Dụ:**

Bạn có 5 ví, mỗi ví $200 USDC:

```bash
# Wallet 1
Address: 0xAAA...
USDC Balance: 200 USDC
Approval needed: 200 USDC (hoặc 1,000 USDC cho production)

# Wallet 2
Address: 0xBBB...
USDC Balance: 200 USDC
Approval needed: 200 USDC

# ... tương tự cho 3 ví còn lại
```

**Script `approve_wallets.py` tự động approve TẤT CẢ ví:**

```bash
python scripts/approve_wallets.py

# Output:
💰 How much USDC should each wallet be approved for?
Enter amount (default 10000): 200

⚠️  You are about to approve 200 USDC for 5 wallets
Continue? (yes/no): yes

✅ APPROVED - 0xAAA... (200 USDC)
✅ APPROVED - 0xBBB... (200 USDC)
✅ APPROVED - 0xCCC... (200 USDC)
✅ APPROVED - 0xDDD... (200 USDC)
✅ APPROVED - 0xEEE... (200 USDC)
```

---

## 3️⃣ **YÊU CẦU APPROVAL 1,000 USDC**

### **🤔 Tại Sao 1,000 USDC?**

#### **Lý Do 1: Đủ Cho Nhiều Orders**

Với `max_concurrent_markets: 10`:

```
Mỗi market cần: ~$100-200 USDC (2 orders YES + NO)
10 markets × $150 = $1,500 USDC

Nhưng không phải tất cả markets đều active cùng lúc
→ Thực tế cần: ~$1,000 USDC
```

#### **Lý Do 2: Approval Không Tăng Lại**

**QUAN TRỌNG:** Approval hoạt động như "hạn mức tín dụng":

```
Initial approval: 1,000 USDC

Place order 1: 200 USDC → Allowance: 800 USDC
Place order 2: 150 USDC → Allowance: 650 USDC
Cancel order 1: 200 USDC → Allowance: 650 USDC (KHÔNG tăng!)
Order 2 filled → Allowance: 650 USDC (KHÔNG tăng!)
```

**Kết luận:** Allowance chỉ **giảm**, không **tăng** → Cần approve số lớn từ đầu

#### **Lý Do 3: Tránh Re-Approve Thường Xuyên**

| Approval Amount | Re-Approve Frequency | Gas Fees/Month |
|-----------------|---------------------|----------------|
| 100 USDC | Mỗi ngày | ~$0.30-1.50 |
| 1,000 USDC | Mỗi tuần | ~$0.10-0.30 |
| 10,000 USDC | Mỗi tháng | ~$0.01-0.05 |

---

### **📊 1,000 USDC Cho MỖI VÍ Hay TỔNG?**

**TRẢLỜI: MỖI VÍ!**

```
Scenario: 5 wallets, mỗi wallet $200 USDC

❌ SAI: Approve tổng 1,000 USDC cho tất cả ví
   → Không thể! Mỗi ví là 1 address riêng biệt

✅ ĐÚNG: Approve 1,000 USDC cho MỖI ví
   → Wallet 1: 1,000 USDC approval
   → Wallet 2: 1,000 USDC approval
   → ... (5 ví)
   → Total approvals: 5 × 1,000 = 5,000 USDC
```

**Nhưng chỉ cần USDC balance đủ trong mỗi ví:**
```
Wallet 1: 200 USDC balance, 1,000 USDC approval ✅ OK
   → Chỉ có thể dùng tối đa 200 USDC
   → Approval 1,000 chỉ là "hạn mức", không phải "số tiền"
```

---

### **💡 Scenario: 5 Ví × 100 USDC**

**Setup:**
```yaml
total_capital: 500  # $500 USDC total
num_wallets: 5      # 5 wallets
# → Each wallet: $100 USDC
```

**Option A: Approve 100 USDC/ví (TEST MODE)**
```
Wallet 1: 100 USDC balance, 100 USDC approval
Wallet 2: 100 USDC balance, 100 USDC approval
... (5 ví)

✅ Bot hoạt động được
⚠️  Giới hạn: Mỗi ví chỉ 1-2 markets
⚠️  Cần re-approve thường xuyên (mỗi 1-2 ngày)
```

**Option B: Approve 1,000 USDC/ví (RECOMMENDED)**
```
Wallet 1: 100 USDC balance, 1,000 USDC approval
Wallet 2: 100 USDC balance, 1,000 USDC approval
... (5 ví)

✅ Bot hoạt động tốt hơn
✅ Không cần re-approve thường xuyên
✅ Sẵn sàng scale up (chỉ cần nạp thêm USDC)
⚠️  Vẫn chỉ dùng được 100 USDC/ví (do balance)
```

**Khuyến nghị:** Dùng Option B!
- Approve 1 lần, dùng lâu dài
- Khi có thêm vốn, chỉ cần nạp USDC vào ví (không cần approve lại)

---

## 4️⃣ **SO SÁNH CHIẾN LƯỢC**

### **Option A: 1 Ví × 1,000 USDC**

```yaml
total_capital: 1000
num_wallets: 1
```

| Ưu Điểm | Nhược Điểm |
|---------|------------|
| ✅ Đơn giản, dễ quản lý | ❌ Dễ bị phát hiện là bot |
| ✅ Chỉ cần 1 lần approve | ❌ Nếu ví bị hack → mất hết |
| ✅ Gas fees thấp | ❌ Giới hạn throughput |
| ✅ Dễ track performance | ❌ Risk tập trung |

**Phù hợp:** Testing, học cách dùng bot

---

### **Option B: 10 Ví × 100 USDC**

```yaml
total_capital: 1000
num_wallets: 10
```

| Ưu Điểm | Nhược Điểm |
|---------|------------|
| ✅ Khó phát hiện (distributed) | ❌ Phức tạp hơn |
| ✅ Risk phân tán | ❌ Cần approve 10 lần |
| ✅ Throughput cao hơn | ❌ Gas fees cao hơn |
| ✅ Giống human trader | ❌ Khó track performance |

**Phù hợp:** Production, farming nghiêm túc

---

### **📊 Hiệu Quả Farming:**

| Metric | 1 Ví × $1k | 10 Ví × $100 |
|--------|------------|--------------|
| **Max Markets** | 10-20 | 50-100 |
| **Detection Risk** | Cao | Thấp |
| **Setup Time** | 5 phút | 30 phút |
| **Gas Fees** | $0.01 | $0.10 |
| **Reward Potential** | 100% | 150-200% |

**Kết luận:** Option B tốt hơn cho farming, nhưng phức tạp hơn

---

## 5️⃣ **LOGIC APPROVAL CHI TIẾT**

### **🔍 Approval vs Order Size**

**Câu hỏi:** Nếu mỗi order chỉ 50 USDC, tại sao cần approve 1,000 USDC?

**Trả lời:**

```
Approval ≠ Số tiền bị lock
Approval = Hạn mức tối đa bot có thể dùng

Ví dụ:
Approval: 1,000 USDC
Balance: 200 USDC

Order 1: 50 USDC → ✅ OK (balance đủ)
Order 2: 50 USDC → ✅ OK
Order 3: 50 USDC → ✅ OK
Order 4: 50 USDC → ✅ OK
Order 5: 50 USDC → ❌ FAIL (balance chỉ còn 0)

Allowance sau 4 orders: 1,000 - 200 = 800 USDC
```

---

### **⚡ Approval Có Bị "Tiêu Hao" Không?**

**CÓ!** Mỗi lần đặt order, allowance **giảm đi**:

```
Initial state:
  Balance: 1,000 USDC
  Allowance: 1,000 USDC

Place order: 200 USDC
  Balance: 1,000 USDC (không đổi, chưa fill)
  Allowance: 800 USDC (giảm!)

Cancel order:
  Balance: 1,000 USDC
  Allowance: 800 USDC (KHÔNG tăng lại!)

Order filled:
  Balance: 800 USDC (giảm 200)
  Allowance: 800 USDC (không đổi)
```

**Kết luận:** Allowance chỉ giảm, không tăng → Cần approve số lớn

---

### **📈 Tính Toán Approval Cần Thiết**

```python
Required Approval = 
    Max Concurrent Markets 
    × Average Capital Per Market 
    × Safety Factor

Ví dụ:
    = 10 markets
    × $150/market
    × 1.5 (safety factor)
    = $2,250 USDC

→ Khuyến nghị: 1,000-10,000 USDC
```

**Safety Factor** để:
- Đủ cho orders bị cancel và re-place
- Đủ cho price adjustments
- Tránh phải re-approve thường xuyên

---

## 🎯 **TÓM TẮT & KHUYẾN NGHỊ**

### **Cho Testing (Bạn đang ở đây):**
```yaml
total_capital: 100
num_wallets: 1
approval_per_wallet: 100 USDC
max_concurrent_markets: 2
```

### **Cho Small-Scale:**
```yaml
total_capital: 500
num_wallets: 2-3
approval_per_wallet: 1,000 USDC
max_concurrent_markets: 5
```

### **Cho Production:**
```yaml
total_capital: 5000
num_wallets: 10
approval_per_wallet: 10,000 USDC
max_concurrent_markets: 10
```

---

**Câu hỏi thêm? Hỏi tôi bất cứ lúc nào!** 🚀

