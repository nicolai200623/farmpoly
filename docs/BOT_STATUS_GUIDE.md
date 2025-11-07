# Hướng Dẫn Kiểm Tra Trạng Thái Bot Polymarket

## 📋 Tổng Quan

Tài liệu này hướng dẫn cách kiểm tra trạng thái hoạt động của Polymarket Trading Bot, bao gồm:
- Số dư ví và allowance
- Các lệnh đang hoạt động
- Positions hiện tại
- Rewards (nếu có)
- Phân tích log và troubleshooting

---

## 🔧 Scripts Kiểm Tra

### 1. **Kiểm Tra Toàn Diện** (Recommended)

```bash
python scripts/check_bot_status_comprehensive.py
```

**Chức năng:**
- ✅ Kiểm tra số dư MATIC và USDC
- ✅ Kiểm tra USDC allowance cho CTF Exchange
- ✅ Liệt kê tất cả lệnh đang active
- ✅ Hiển thị positions hiện tại với P&L
- ✅ Kiểm tra rewards (nếu API có sẵn)
- ✅ Phân tích log để tìm lỗi gần đây

**Output mẫu:**
```
======================================================================
                          1. WALLET BALANCES
======================================================================

   Wallet: 0x18F261DC...Ae4FfD96
   MATIC Balance: 17.1740 MATIC
   USDC.e Balance: $52.09

======================================================================
                          2. USDC ALLOWANCE
======================================================================

   Current Allowance: $100.00 USDC
   ⚠️  Allowance is OK but low for production

======================================================================
                           3. ACTIVE ORDERS
======================================================================

   Found 3 active order(s):
   Total USDC Locked in Orders: $96.45
```

---

### 2. **Kiểm Tra Markets Đang Pending**

```bash
python scripts/check_pending_markets.py
```

**Chức năng:**
- 📊 Phân tích log để tìm markets bot đang cố đặt lệnh
- 📈 Thống kê số lần thử đặt lệnh cho mỗi market
- ✅ Tính success rate của việc đặt lệnh
- 🔍 Hiển thị thông tin chi tiết về từng market
- 💡 Đưa ra khuyến nghị dựa trên phân tích

**Output mẫu:**
```
======================================================================
                     TOP MARKETS (Most Attempted)
======================================================================

Market ID: 668774
   Attempts: 651
   Question: FIDE World Cup 2025 - Michael Adams vs Lorenzo Lodici
   Volume: $16.67
   Active: True

======================================================================
                          ORDER SUCCESS RATE
======================================================================

   Total Attempts: 788
   Successful: 3
   Failed: 785
   Success Rate: 0.4%
   ❌ Very low success rate! Check balance and allowance
```

---

### 3. **Kiểm Tra Số Dư Ví Nhanh**

```bash
python scripts/check_wallets.py
```

**Chức năng:**
- Kiểm tra nhanh số dư MATIC và USDC
- Đơn giản, nhanh chóng

---

### 4. **Kiểm Tra Allowance**

```bash
python scripts/check_approval_status.py
```

**Chức năng:**
- Kiểm tra USDC allowance cho CTF Exchange
- Xác định có cần approve thêm không

---

## 📊 Kết Quả Kiểm Tra Hiện Tại

### Trạng Thái Ví (Ngày 2025-11-07)

```
Wallet: 0x18F261DC6d7Fc5ef2C96Ca4D56776220Ae4FfD96
├── MATIC: 17.1740 (✅ Đủ cho gas)
├── USDC: $52.09 (✅ Đủ cho trading)
└── Allowance: $100.00 (⚠️ Thấp cho production)
```

### Lệnh Đang Hoạt Động

Bot hiện có **3 lệnh active** với tổng **$96.45 USDC bị lock**:

1. **Market 0xb059da...** (FIDE World Cup)
   - BUY @ $0.18 - Size: 62 shares - Locked: $11.16
   - BUY @ $0.77 - Size: 51 shares - Locked: $39.27

2. **Market 0x7d0041...** (FIDE World Cup)
   - BUY @ $0.78 - Size: 59 shares - Locked: $46.02

### Positions Hiện Tại

Bot có **3 positions**:
- Charlotte 49ers: 259 shares
- Yes (Unknown market): 68 shares  
- Syracuse: 66 shares

**Lưu ý:** API không trả về giá và P&L chính xác, cần kiểm tra trên UI Polymarket.

### Phân Tích Log

**Vấn đề phát hiện:**
- ❌ **3,142 lỗi "not enough balance / allowance"**
- ❌ **Success rate chỉ 0.4%** (3/788 attempts)
- ⚠️ Bot đang stuck ở 2 markets:
  - Market 668774: 651 attempts
  - Market 668773: 137 attempts

---

## 🔍 API Endpoints Sử dụng

### 1. **Blockchain (Polygon)**

```python
# RPC Endpoint
POLYGON_RPC = "https://polygon-mainnet.g.alchemy.com/v2/YOUR_KEY"

# USDC Contract
USDC_ADDRESS = "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174"

# CTF Exchange
CTF_EXCHANGE = "0x4bFb41d5B3570DeFd03C39a9A4D8dE6Bd8B8982E"
```

**Cách kiểm tra:**
```python
from web3 import Web3

w3 = Web3(Web3.HTTPProvider(POLYGON_RPC))

# Check USDC balance
usdc_contract = w3.eth.contract(address=USDC_ADDRESS, abi=USDC_ABI)
balance = usdc_contract.functions.balanceOf(wallet_address).call()
usdc_balance = balance / 1e6  # USDC has 6 decimals

# Check allowance
allowance = usdc_contract.functions.allowance(
    wallet_address, 
    CTF_EXCHANGE
).call()
usdc_allowance = allowance / 1e6
```

### 2. **Polymarket CLOB API**

```python
# Base URL
CLOB_HOST = "https://clob.polymarket.com"

# Endpoints
GET /orders          # Get active orders
GET /positions       # Get positions
GET /book?token_id=  # Get orderbook
POST /order          # Place order
DELETE /order        # Cancel order
```

**Cách sử dụng:**
```python
from py_clob_client.client import ClobClient

client = ClobClient(
    host="https://clob.polymarket.com",
    key=private_key,
    chain_id=137
)

# Set API credentials
client.set_api_creds(client.create_or_derive_api_creds())

# Get orders
orders = client.get_orders()

# Get orderbook
book = client.get_order_book(token_id)
```

### 3. **Polymarket Data API**

```python
# Positions endpoint
DATA_API = "https://data-api.polymarket.com/positions"

params = {
    "user": wallet_address,
    "sizeThreshold": 0.01,
    "limit": 500
}

response = requests.get(DATA_API, params=params)
positions = response.json()
```

### 4. **Polymarket Gamma API**

```python
# Market info endpoint
GAMMA_API = "https://gamma-api.polymarket.com/markets/{market_id}"

response = requests.get(GAMMA_API)
market_info = response.json()
```

### 5. **Rewards API** (Không khả dụng công khai)

Polymarket không cung cấp public API để kiểm tra rewards. Cần kiểm tra thủ công tại:
- https://polymarket.com/rewards

---

## 🛠️ Troubleshooting

### Vấn Đề 1: "not enough balance / allowance"

**Triệu chứng:**
- Log đầy lỗi "PolyApiException: not enough balance / allowance"
- Success rate rất thấp (<1%)
- Bot không thể đặt lệnh

**Nguyên nhân:**
1. Không đủ USDC trong ví
2. USDC allowance quá thấp
3. USDC đang bị lock trong orders khác

**Giải pháp:**

```bash
# 1. Kiểm tra số dư
python scripts/check_wallets.py

# 2. Kiểm tra allowance
python scripts/check_approval_status.py

# 3. Nếu allowance thấp, approve thêm
python scripts/approve_ctf.py

# 4. Nếu USDC bị lock, cancel orders
python scripts/close_positions.py
```

**Khuyến nghị:**
- Allowance tối thiểu: $1,000 USDC
- USDC balance tối thiểu: $100-500 USDC
- Luôn giữ 0.5-1 MATIC cho gas

---

### Vấn Đề 2: Bot Stuck Ở Một Market

**Triệu chứng:**
- Bot cố đặt lệnh cho cùng 1 market hàng trăm lần
- Market có thể đã đóng hoặc không còn rewards

**Giải pháp:**

```bash
# 1. Kiểm tra market details
python scripts/check_pending_markets.py
# Nhập market ID khi được hỏi

# 2. Restart bot để refresh market list
# Stop bot (Ctrl+C)
# Start lại: python main.py
```

---

### Vấn Đề 3: Positions Không Hiển Thị P&L

**Nguyên nhân:**
- Data API không trả về đầy đủ thông tin
- Positions có thể đã closed nhưng chưa settled

**Giải pháp:**
- Kiểm tra trực tiếp trên Polymarket UI
- URL: https://polymarket.com/portfolio

---

## 📈 Monitoring Best Practices

### 1. **Kiểm Tra Định Kỳ**

```bash
# Mỗi 1 giờ
python scripts/check_bot_status_comprehensive.py

# Mỗi 6 giờ
python scripts/check_pending_markets.py
```

### 2. **Theo Dõi Metrics**

Các chỉ số quan trọng:
- ✅ **Success Rate** > 50%
- ✅ **USDC Balance** > $50
- ✅ **Allowance** > $1,000
- ✅ **MATIC** > 0.5
- ✅ **Balance Errors** < 10/hour

### 3. **Alerts**

Cần cảnh báo khi:
- ❌ Success rate < 10%
- ❌ USDC balance < $20
- ❌ Allowance < $100
- ❌ MATIC < 0.1
- ❌ Balance errors > 100/hour

---

## 🔗 Useful Links

- **Polymarket UI:** https://polymarket.com
- **Portfolio:** https://polymarket.com/portfolio
- **Rewards:** https://polymarket.com/rewards
- **Polygon Explorer:** https://polygonscan.com/address/0x18F261DC6d7Fc5ef2C96Ca4D56776220Ae4FfD96
- **USDC Contract:** https://polygonscan.com/token/0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174

---

## 📞 Support

Nếu gặp vấn đề:
1. Chạy `python scripts/check_bot_status_comprehensive.py`
2. Chạy `python scripts/check_pending_markets.py`
3. Kiểm tra log.md
4. Tham khảo phần Troubleshooting ở trên

