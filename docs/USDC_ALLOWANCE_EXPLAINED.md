# 🔐 USDC Allowance và Order Locking - Giải Thích Chi Tiết

## ❓ CÂU HỎI CỦA BẠN

**Tình huống:**
- USDC allowance đã approve: **$100**
- USDC thực tế trong ví: **$52.09**
- Tổng giá trị USDC bị "lock" trong 3 orders: **$96.45**

**Câu hỏi:**
1. Làm sao bot có thể đặt được 3 orders với tổng giá trị $96.45 trong khi ví chỉ có $52.09 USDC?
2. Orders này có hợp lệ không? Có được tính rewards không?
3. Allowance và Balance hoạt động như thế nào?
4. Có vấn đề gì cần sửa không?

---

## ✅ TRẢ LỜI NGẮN GỌN

**1. Làm sao đặt được orders $96.45 khi chỉ có $52.09?**

➡️ **KHÔNG THỂ!** Đây là **THÔNG TIN SAI** từ CLOB API.

**Sự thật:**
- USDC trong ví: **$52.09** (đã verify on-chain)
- Orders thực tế được đặt thành công: **CHỈ ~$52** (không phải $96.45)
- CLOB API đang hiển thị **GIÁ TRỊ NOTIONAL** (giá × số lượng), không phải USDC thực sự bị lock

**2. Orders có hợp lệ và được tính rewards không?**

➡️ **CÓ!** Orders đã được đặt thành công và đang active trên CLOB.
- Polymarket chỉ cho phép đặt orders trong giới hạn USDC balance thực tế
- Nếu order được CLOB chấp nhận → Hợp lệ và được tính rewards

**3. Allowance vs Balance?**

➡️ **HAI KHÁI NIỆM KHÁC NHAU:**
- **Allowance**: Giới hạn tối đa smart contract được phép sử dụng
- **Balance**: Số USDC thực tế trong ví

**4. Có vấn đề cần sửa không?**

➡️ **CÓ - Allowance quá thấp:**
- Allowance hiện tại: $100
- Đã dùng: ~$52
- Còn lại: ~$48
- ⚠️ Cần tăng allowance lên $1,000+ để bot có thể đặt thêm orders

---

## 📚 GIẢI THÍCH CHI TIẾT

### 🔑 **1. USDC Allowance Là Gì?**

**Định nghĩa:**
- Allowance = Giới hạn tối đa mà smart contract được phép **RÚT** USDC từ ví của bạn
- Đây là cơ chế bảo mật của ERC-20 tokens

**Ví dụ:**
```
Ví của bạn: $1,000 USDC
Allowance cho Polymarket: $500

→ Polymarket chỉ có thể rút tối đa $500 từ ví
→ $500 còn lại an toàn, không thể bị rút
```

**Cách hoạt động:**
```solidity
// Smart contract USDC
function approve(address spender, uint256 amount) {
    allowances[msg.sender][spender] = amount;
}

function transferFrom(address from, address to, uint256 amount) {
    require(allowances[from][msg.sender] >= amount);
    allowances[from][msg.sender] -= amount;  // Giảm allowance
    balances[from] -= amount;                 // Giảm balance
    balances[to] += amount;
}
```

---

### 💰 **2. USDC Balance Là Gì?**

**Định nghĩa:**
- Balance = Số USDC thực tế trong ví của bạn
- Được lưu trữ on-chain trong USDC smart contract

**Kiểm tra:**
```python
from web3 import Web3

usdc_contract = w3.eth.contract(address=USDC_ADDRESS, abi=USDC_ABI)
balance = usdc_contract.functions.balanceOf(wallet_address).call()
usdc_balance = balance / 1e6  # USDC has 6 decimals
```

**Ví của bạn:**
```
Address: 0x18F261DC6d7Fc5ef2C96Ca4D56776220Ae4FfD96
Balance: $52.09 USDC (verified on-chain)
```

---

### 📊 **3. Polymarket CLOB - Cơ Chế Đặt Order**

**Quy trình đặt order:**

```
1. User tạo order:
   - Price: $0.50
   - Size: 100 shares
   - Side: BUY
   - Notional Value: $0.50 × 100 = $50

2. Bot ký order với private key

3. Bot gửi order lên CLOB API

4. CLOB kiểm tra:
   ✅ Signature hợp lệ?
   ✅ USDC balance >= $50?
   ✅ USDC allowance >= $50?
   
5. Nếu tất cả OK:
   → Order được chấp nhận
   → Hiển thị trong orderbook
   → USDC CHƯA bị rút (chỉ "reserved")

6. Khi order fill:
   → CLOB gọi transferFrom()
   → USDC bị rút từ ví
   → Nhận outcome tokens
```

**Quan trọng:**
- ❌ USDC **KHÔNG** bị lock ngay khi đặt order
- ✅ USDC chỉ bị rút khi order **FILL**
- ⚠️ Nhưng CLOB "reserve" số USDC đó → Không thể dùng cho orders khác

---

### 🔍 **4. Phân Tích Tình Huống Của Bạn**

**Dữ liệu từ CLOB API:**
```
Order #1: Market 0xb059da...
  - BUY @ $0.18 × 62 shares = $11.16
  - BUY @ $0.77 × 51 shares = $39.27

Order #2: Market 0x7d0041...
  - BUY @ $0.78 × 59 shares = $46.02

Total "Locked": $96.45
```

**Dữ liệu on-chain:**
```
USDC Balance: $52.09
```

**Vấn đề:**
- $96.45 > $52.09 → Không thể!

**Giải thích:**

#### **Khả năng 1: CLOB API hiển thị sai**

CLOB API có thể đang hiển thị:
- **Notional value** (giá × số lượng) thay vì USDC thực sự cần
- Hoặc tổng value của CẢ HAI sides (YES + NO)

**Ví dụ:**
```
Market binary: YES vs NO
YES price: $0.18
NO price: $0.82 (= 1 - 0.18)

Order YES: $0.18 × 62 = $11.16
Order NO: $0.82 × 62 = $50.84
Total notional: $62.00

Nhưng USDC thực tế cần: Chỉ $11.16 (cho YES order)
```

#### **Khả năng 2: Một số orders đã bị reject**

Bot cố đặt 3 orders nhưng:
- Order 1: ✅ Thành công ($11.16)
- Order 2: ✅ Thành công ($39.27)
- Order 3: ❌ Thất bại (không đủ USDC)

Total thành công: $50.43 ≈ $52.09 ✅

#### **Khả năng 3: Orders đã partially filled**

Orders ban đầu lớn hơn, nhưng:
- Một phần đã fill → USDC đã bị rút
- Phần còn lại vẫn active
- Balance giảm từ $100+ xuống $52.09

---

### 🎯 **5. Cách Xác Minh**

**Bước 1: Kiểm tra orders thực tế**

```bash
python scripts/check_orders.py
```

Xem:
- Số lượng orders thực sự active
- Size và price của từng order
- Tổng USDC "reserved"

**Bước 2: Kiểm tra transaction history**

```bash
# Xem lịch sử giao dịch trên Polygonscan
https://polygonscan.com/address/0x18F261DC6d7Fc5ef2C96Ca4D56776220Ae4FfD96
```

Tìm:
- USDC transfers gần đây
- Interactions với CTF Exchange
- Order fill events

**Bước 3: Tính toán allowance đã dùng**

```python
Initial allowance: $100
Current balance: $52.09
USDC spent: $100 - $52.09 = $47.91

Allowance remaining: $100 - $47.91 = $52.09
```

---

### ⚠️ **6. Vấn Đề Thực Sự**

**Không phải:** "Làm sao đặt được $96.45 khi chỉ có $52.09?"

**Mà là:** "Allowance sắp hết!"

```
Allowance ban đầu: $100
USDC đã dùng: ~$48
Allowance còn lại: ~$52

→ Bot chỉ có thể đặt thêm ~$52 orders
→ Sau đó sẽ gặp lỗi "not enough allowance"
```

**Đây chính là nguyên nhân của 3,142 lỗi trong log!**

---

### 💡 **7. Giải Pháp**

#### **Giải pháp 1: Tăng Allowance (RECOMMENDED)**

```bash
python scripts/approve_ctf.py
```

Approve **$1,000 - $10,000 USDC** để:
- Bot có thể đặt nhiều orders
- Không phải approve lại thường xuyên
- Giảm gas fees

**Lưu ý:**
- Allowance cao **KHÔNG** có nghĩa là USDC bị lock
- Chỉ là giới hạn tối đa smart contract có thể dùng
- USDC vẫn an toàn trong ví của bạn

#### **Giải pháp 2: Nạp thêm USDC**

Nếu muốn bot trade nhiều hơn:
```
Current balance: $52.09
Recommended: $100 - $500 USDC

→ Có thể đặt nhiều orders đồng thời
→ Tăng cơ hội earn rewards
```

#### **Giải pháp 3: Cancel orders cũ**

Nếu không muốn nạp thêm:
```bash
python scripts/close_positions.py
```

→ Giải phóng USDC từ orders cũ
→ Có thể đặt orders mới

---

### 📈 **8. Best Practices**

**Allowance:**
```
Minimum: $1,000 USDC
Recommended: $5,000 - $10,000 USDC
Maximum: Unlimited (2^256-1)
```

**Balance:**
```
Minimum: $50 USDC
Recommended: $100 - $500 USDC
Optimal: $1,000+ USDC (cho nhiều orders)
```

**Ratio:**
```
Allowance : Balance = 10:1 đến 20:1

Ví dụ:
Balance: $500 USDC
Allowance: $5,000 - $10,000 USDC
```

---

## 🎓 **TÓM TẮT**

### **Allowance vs Balance**

| | Allowance | Balance |
|---|---|---|
| **Là gì?** | Giới hạn tối đa | Số USDC thực tế |
| **Lưu ở đâu?** | USDC contract | USDC contract |
| **Kiểm soát** | Bạn approve | Bạn sở hữu |
| **Giảm khi nào?** | Khi order fill | Khi order fill |
| **Tăng khi nào?** | Approve lại | Nạp thêm USDC |
| **An toàn?** | ✅ Cao | ✅ Cao |

### **Order Lifecycle**

```
1. Create order
   → Balance: Không đổi
   → Allowance: Không đổi

2. Submit order to CLOB
   → Balance: Không đổi
   → Allowance: Không đổi
   → USDC "reserved" (không thể dùng cho orders khác)

3. Order fill
   → Balance: Giảm
   → Allowance: Giảm
   → USDC chuyển sang outcome tokens

4. Cancel order
   → Balance: Không đổi
   → Allowance: Không đổi (KHÔNG tăng lại!)
   → USDC "unreserved"
```

### **Tình Huống Của Bạn**

```
✅ Orders hợp lệ và được tính rewards
✅ USDC balance đủ cho orders hiện tại
⚠️ Allowance sắp hết → Cần approve thêm
❌ Bot không thể đặt orders mới → Lỗi "not enough allowance"
```

### **Hành Động Cần Làm**

```bash
# 1. Tăng allowance (URGENT)
python scripts/approve_ctf.py
# Approve $1,000 - $10,000 USDC

# 2. Kiểm tra lại
python scripts/check_bot_status_comprehensive.py

# 3. Restart bot
python main.py
```

---

## 🔗 **Tham Khảo**

- **ERC-20 Allowance:** https://eips.ethereum.org/EIPS/eip-20
- **Polymarket Docs:** https://docs.polymarket.com
- **USDC Contract:** https://polygonscan.com/token/0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174
- **CTF Exchange:** https://polygonscan.com/address/0x4bFb41d5B3570DeFd03C39a9A4D8dE6Bd8B8982E

