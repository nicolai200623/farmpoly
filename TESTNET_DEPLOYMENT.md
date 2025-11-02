# 🧪 Testnet Deployment Guide - Polymarket Trading Bot

## 📋 Tổng Quan

Hướng dẫn này sẽ giúp bạn deploy bot lên **Polygon Mumbai Testnet** để test an toàn trước khi chạy trên mainnet.

**⚠️ LƯU Ý:** Polymarket chỉ hoạt động trên **Polygon Mainnet**, không có testnet chính thức. Tuy nhiên, bạn có thể:
1. Test với **vốn nhỏ** trên mainnet ($50-100)
2. Sử dụng **demo mode** để test logic
3. Test từng component riêng lẻ

---

## 🎯 Chiến Lược Test An Toàn

### Option 1: Demo Mode (Recommended) ✅

Test bot logic mà không cần tiền thật.

### Option 2: Small Capital Test ✅

Test trên mainnet với vốn nhỏ ($50-100).

### Option 3: Component Testing ✅

Test từng module riêng lẻ.

---

## 🚀 OPTION 1: Demo Mode Testing

### Bước 1: Cài Đặt Dependencies

```bash
# Clone repository (nếu chưa có)
cd c:\LAINP\Augment\Farmpoly

# Install dependencies
pip install -r requirements.txt

# Install Playwright
pip install playwright
playwright install chromium
```

### Bước 2: Cấu Hình Demo Mode

Tạo file `.env`:

```bash
# Demo Mode - Không cần private keys thật
USE_DEMO_WALLETS=true

# RPC URL (public, free)
POLYGON_RPC_URL=https://polygon-rpc.com

# Optional: Telegram alerts (để trống nếu không dùng)
TELEGRAM_BOT_TOKEN=
TELEGRAM_CHAT_ID=
```

### Bước 3: Cấu Hình Bot

Edit `config.yaml`:

```yaml
# Demo mode settings
total_capital: 1000  # Virtual capital
num_wallets: 3       # Demo wallets

market_scanner:
  min_reward: 50
  max_competition: 100
  update_interval: 300  # 5 minutes

order_management:
  size_min: 100
  size_max: 300
  spread_min: 0.01
  spread_max: 0.03

# Disable real trading
dry_run: true  # IMPORTANT: No real orders!
```

### Bước 4: Chạy Tests

```bash
# Run unit tests
python tests/run_tests.py

# Should see: 37/37 tests pass ✅
```

### Bước 5: Chạy Bot Demo

```bash
# Run in demo mode
python main.py
```

**Kết quả mong đợi:**
```
⚠️  Using DEMO wallets - NOT for real trading!
⚠️  Initialized 3 DEMO wallets (NO REAL TRADING)
🔍 Scanning markets...
📊 Found 15 markets
✅ Filtered to 5 high-reward markets
💡 DRY RUN: Would place order on market XYZ
```

### Bước 6: Kiểm Tra Logs

```bash
# View logs
tail -f logs/polymarket_bot.log

# Check for:
# - Market scanning works
# - Filtering logic works
# - Order logic works (dry run)
# - No errors
```

---

## 🚀 OPTION 2: Small Capital Mainnet Test

### ⚠️ CẢNH BÁO

- Đây là **REAL MONEY** trên mainnet
- Chỉ dùng số tiền bạn có thể mất
- Bắt đầu với **$50-100 USDC**
- Monitor 24/7 trong tuần đầu

### Bước 1: Tạo Test Wallets

```bash
# Generate new wallets (KHÔNG dùng ví chính!)
python scripts/generate_wallets.py
```

**Output:**
```
🔐 Generated 5 wallets:

Wallet 1:
  Address: 0x1234...
  Private Key: 0xabcd...

Wallet 2:
  Address: 0x5678...
  Private Key: 0xef01...
```

**⚠️ LƯU PRIVATE KEYS AN TOÀN!**

### Bước 2: Fund Test Wallets

#### 2.1. Mua MATIC & USDC

**Option A: CEX (Binance, Coinbase)**
1. Mua MATIC trên exchange
2. Withdraw về Polygon network
3. Swap một phần MATIC → USDC

**Option B: Bridge từ Ethereum**
1. Có ETH/USDC trên Ethereum
2. Bridge qua Polygon: https://wallet.polygon.technology/
3. Chờ 7-8 phút

#### 2.2. Phân Bổ Vốn

Cho mỗi wallet:
- **25 USDC** - Vốn trading
- **0.5 MATIC** - Gas fees

**Tổng cho 2 wallets:**
- **50 USDC**
- **1 MATIC**

### Bước 3: Cấu Hình Real Wallets

Tạo file `.env`:

```bash
# Real wallets mode
USE_DEMO_WALLETS=false

# Wallet private keys (từ bước 1)
WALLET_1_PK=0xabcd1234...
WALLET_2_PK=0xef015678...

# RPC URL (recommended: use your own)
POLYGON_RPC_URL=https://polygon-mainnet.g.alchemy.com/v2/YOUR_KEY

# Optional: Telegram alerts
TELEGRAM_BOT_TOKEN=your_bot_token
TELEGRAM_CHAT_ID=your_chat_id
```

**🔐 Bảo Mật:**
```bash
# Make sure .env is in .gitignore
echo ".env" >> .gitignore

# Set file permissions (Linux/Mac)
chmod 600 .env
```

### Bước 4: Kiểm Tra Wallets

```bash
# Check balances
python scripts/check_wallets.py
```

**Output mong đợi:**
```
💰 Wallet Balances:

Wallet 1 (0x1234...):
  USDC: 25.00
  MATIC: 0.50
  ✅ Ready to trade

Wallet 2 (0x5678...):
  USDC: 25.00
  MATIC: 0.50
  ✅ Ready to trade

Total USDC: 50.00
Total MATIC: 1.00
```

### Bước 5: Approve USDC

```bash
# One-time approval for CLOB
python scripts/approve_wallets.py
```

**Interactive prompts:**
```
🔐 USDC Approval for Polymarket CLOB

Wallet 1 (0x1234...):
  Current allowance: 0 USDC
  Approve unlimited? (y/n): y
  
✅ Approval transaction sent: 0xabc...
⏳ Waiting for confirmation...
✅ Approved! Wallet 1 ready to trade

Wallet 2 (0x5678...):
  Current allowance: 0 USDC
  Approve unlimited? (y/n): y
  
✅ Approval transaction sent: 0xdef...
⏳ Waiting for confirmation...
✅ Approved! Wallet 2 ready to trade

🎉 All wallets approved!
```

**Gas cost:** ~0.01 MATIC per wallet

### Bước 6: Cấu Hình Conservative

Edit `config.yaml` cho test an toàn:

```yaml
# Conservative test settings
total_capital: 50    # $50 USDC total
num_wallets: 2       # 2 wallets

market_scanner:
  min_reward: 100    # Higher threshold = fewer trades
  max_competition: 50  # Lower competition
  update_interval: 600  # 10 minutes (slower)

order_management:
  size_min: 10       # Small orders
  size_max: 20       # Max $20 per order
  spread_min: 0.02   # 2% spread (conservative)
  spread_max: 0.05   # 5% max spread
  max_orders_per_market: 1  # Only 1 order per market

risk_management:
  max_capital_per_market: 0.2  # 20% max per market
  max_total_exposure: 0.5      # 50% max total
  enable_hedging: true
  stop_loss_percentage: 0.10   # 10% stop loss

# Real trading enabled
dry_run: false  # ⚠️ REAL ORDERS!
```

### Bước 7: Test Run (1 Hour)

```bash
# Start bot
python main.py
```

**Monitor trong terminal:**
```
🚀 Polymarket Trading Bot V2.0
💰 Capital: $50.00 USDC
👛 Wallets: 2 loaded
🔐 USDC approved: ✅

🔍 Scanning markets...
📊 Found 25 markets
✅ Filtered to 3 high-reward markets

📈 Market: "Will Bitcoin hit $100k?"
  Reward: $150
  Competition: 30
  Score: 8.5/10
  
💡 Placing order:
  Side: YES
  Size: $15
  Price: $0.52
  
✅ Order placed: 0x123abc...
⏳ Waiting for fill...
```

**Để chạy 1 giờ, sau đó:**
```bash
# Stop bot (Ctrl+C)
^C

# Check results
python scripts/check_wallets.py
```

### Bước 8: Đánh Giá Kết Quả

```bash
# View logs
cat logs/polymarket_bot.log | grep "PnL"

# Check wallet balances
python scripts/check_wallets.py
```

**Metrics để đánh giá:**
- **Orders placed:** Bao nhiêu orders?
- **Fill rate:** Bao nhiêu % được fill?
- **PnL:** Lãi/lỗ bao nhiêu?
- **Gas costs:** Chi phí gas?
- **Errors:** Có lỗi gì không?

**Kết quả tốt:**
- Fill rate > 30%
- PnL > 0 (hoặc loss < $5)
- No critical errors
- Gas costs < $2

**Kết quả xấu:**
- Fill rate < 10%
- Loss > $10
- Many errors
- Gas costs > $5

---

## 🚀 OPTION 3: Component Testing

Test từng module riêng lẻ.

### Test 1: Market Scanner

```bash
# Test scanner only
python -c "
import asyncio
from market_scanner_v2 import MarketScannerV2
import yaml

with open('config.yaml') as f:
    config = yaml.safe_load(f)

scanner = MarketScannerV2(config['market_scanner'])

async def test():
    markets = await scanner.scan_markets()
    print(f'Found {len(markets)} markets')
    for m in markets[:5]:
        print(f'  - {m[\"question\"]}: ${m[\"reward\"]}')

asyncio.run(test())
"
```

### Test 2: Wallet Manager

```bash
# Test wallet loading
python -c "
import asyncio
from wallet_manager import WalletManager
import yaml

with open('config.yaml') as f:
    config = yaml.safe_load(f)

manager = WalletManager(config)

async def test():
    wallet = await manager.get_next_wallet()
    print(f'Wallet: {wallet[\"address\"]}')
    print(f'Balance: Check manually')

asyncio.run(test())
"
```

### Test 3: USDC Approver

```bash
# Test approval check
python scripts/check_wallets.py
```

### Test 4: Risk Manager

```bash
# Run risk manager tests
python -m unittest tests.test_risk_manager -v
```

---

## 📊 Monitoring & Debugging

### Real-time Monitoring

```bash
# Terminal 1: Bot
python main.py

# Terminal 2: Logs
tail -f logs/polymarket_bot.log

# Terminal 3: Balances (every 5 min)
watch -n 300 python scripts/check_wallets.py
```

### Check Transactions

```bash
# View on PolygonScan
# https://polygonscan.com/address/YOUR_WALLET_ADDRESS
```

### Debug Mode

Edit `config.yaml`:

```yaml
logging:
  level: DEBUG  # More verbose logs
  console: true
  file: true
```

---

## 🛑 Emergency Stop

### Stop Bot Immediately

```bash
# Ctrl+C in terminal
^C

# Or kill process
pkill -f "python main.py"
```

### Cancel All Orders

```python
# Run this script
python -c "
from py_clob_client.client import ClobClient
import os
from dotenv import load_dotenv

load_dotenv()

# For each wallet
for i in range(1, 3):
    pk = os.getenv(f'WALLET_{i}_PK')
    if pk:
        client = ClobClient('https://clob.polymarket.com', key=pk)
        orders = client.get_orders()
        for order in orders:
            if order['status'] == 'OPEN':
                client.cancel_order(order['id'])
                print(f'Cancelled order {order[\"id\"]}')
"
```

---

## ✅ Success Checklist

### Pre-Launch
- [ ] Unit tests pass (37/37)
- [ ] Demo mode works
- [ ] Wallets funded (USDC + MATIC)
- [ ] USDC approved
- [ ] Config conservative
- [ ] Monitoring setup

### During Test
- [ ] Bot starts without errors
- [ ] Markets scanned successfully
- [ ] Orders placed (if opportunities)
- [ ] No critical errors in logs
- [ ] Balances tracked

### Post-Test
- [ ] Review logs
- [ ] Check PnL
- [ ] Analyze fill rate
- [ ] Calculate gas costs
- [ ] Decide: scale up or optimize

---

## 🎓 Next Steps After Successful Test

### If Test Went Well (PnL > 0, No Errors)

1. **Run for 24 hours** with same config
2. **Monitor closely** - check every 2-3 hours
3. **Analyze performance** - fill rate, PnL, gas
4. **Optimize config** - adjust based on data
5. **Scale gradually** - increase capital 50% per week

### If Test Had Issues

1. **Review logs** - identify errors
2. **Fix issues** - update code/config
3. **Re-run tests** - verify fixes
4. **Try again** - with fixes applied

---

## 📞 Support & Resources

### Documentation
- `SETUP_GUIDE.md` - Full setup guide
- `USER_GUIDE.md` - User manual
- `TEST_REPORT.md` - Test results
- `config.yaml` - All settings

### Troubleshooting
- Check logs: `tail -f logs/polymarket_bot.log`
- Test wallets: `python scripts/check_wallets.py`
- Run tests: `python tests/run_tests.py`

### Polymarket Resources
- Dashboard: https://polymarket.com/
- CLOB API: https://docs.polymarket.com/
- Discord: https://discord.gg/polymarket

---

## ⚠️ Final Warnings

1. **Start small** - $50-100 max for first test
2. **Monitor closely** - Check every hour first day
3. **Use test wallets** - NOT your main wallet
4. **Expect losses** - Testing costs money
5. **Be patient** - Takes time to optimize
6. **Stop if issues** - Don't let it run unmonitored

**This is real money. Trade responsibly!**

---

**Ready to deploy? Follow Option 1 (Demo) or Option 2 (Small Capital)!** 🚀

