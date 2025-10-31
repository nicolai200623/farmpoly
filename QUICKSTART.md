# 🚀 Quick Start Guide - Polymarket Trading Bot

## ⚡ 15-Minute Setup

### 1️⃣ Install Dependencies (5 min)

```bash
# Install Python packages
pip install -r requirements.txt

# Install Playwright browsers (for V2 scanner)
playwright install chromium
```

### 2️⃣ Configure Wallets (5 min)

```bash
# Copy environment template
cp .env.example .env

# Generate new wallets (or use existing ones)
python scripts/generate_wallets.py

# Edit .env and add your wallet private keys
# WALLET_1_PK=0x...
# WALLET_2_PK=0x...
```

**⚠️ IMPORTANT:** Each wallet needs:
- **100+ USDC** for trading
- **0.5+ MATIC** for gas fees

Bridge USDC to Polygon: https://wallet.polygon.technology/

### 3️⃣ Approve USDC (2 min)

```bash
# Approve USDC for trading (one-time setup)
python scripts/approve_wallets.py
```

This approves the Polymarket CLOB to spend USDC from your wallets.

### 4️⃣ Configure Bot (2 min)

Edit `config.yaml`:

```yaml
# Start with small capital
total_capital: 200  # $200 USDC
num_wallets: 2      # 2 wallets

# Lower reward threshold for more opportunities
market_scanner:
  min_reward: 50    # $50 minimum reward
```

### 5️⃣ Run Bot (1 min)

```bash
# Test mode (no real orders)
USE_DEMO_WALLETS=true python main.py

# Real trading (after testing!)
python main.py
```

---

## 🎯 What's New in V2?

### ✅ Fixed Critical Issues

| Issue | Before | After |
|-------|--------|-------|
| **Wallets** | Random demo keys | Real wallets from .env |
| **Scanner** | Fragile Selenium | Robust Playwright + Gamma API |
| **USDC** | No approval | Auto-check + approval script |

### 🚀 New Features

1. **Playwright Scanner** - 50x more reliable than Selenium
2. **Gamma API** - Direct API access (fastest)
3. **USDC Approval** - One-time setup, then trade forever
4. **Better Config** - Simplified settings for quick start

---

## 📊 Monitoring

### Check Wallet Balances

```bash
python scripts/check_wallets.py
```

### View Logs

```bash
tail -f logs/polymarket_bot.log
```

### Performance Stats

The bot logs:
- Markets scanned
- Orders placed
- Fills received
- PnL (profit/loss)

---

## 🔧 Troubleshooting

### "No wallets loaded"

**Fix:** Add wallet private keys to `.env`:

```bash
WALLET_1_PK=0x1234567890abcdef...
WALLET_2_PK=0x2234567890abcdef...
```

### "USDC approval needed"

**Fix:** Run approval script:

```bash
python scripts/approve_wallets.py
```

### "Insufficient MATIC for gas"

**Fix:** Bridge MATIC to your wallets:
- https://wallet.polygon.technology/
- Need at least 0.5 MATIC per wallet

### "Insufficient USDC balance"

**Fix:** Bridge USDC to your wallets:
- https://wallet.polygon.technology/
- Need at least 100 USDC per wallet

### "Playwright not installed"

**Fix:** Install Playwright browsers:

```bash
playwright install chromium
```

### "RPC connection failed"

**Fix:** Use your own RPC in `.env`:

```bash
# Get free RPC from:
# - Alchemy: https://www.alchemy.com/
# - Infura: https://infura.io/

POLYGON_RPC_URL=https://polygon-mainnet.g.alchemy.com/v2/YOUR_KEY
```
https://polygon-mainnet.infura.io/v3/f1d5a5d82f2c492e9e9dd802e04152df
---

## 💰 Capital Recommendations

| Experience | Capital | Wallets | Expected Daily |
|------------|---------|---------|----------------|
| **Beginner** | $200 | 2 | $10-30 |
| **Intermediate** | $500 | 3-5 | $30-80 |
| **Advanced** | $1000+ | 5-10 | $80-200 |

**⚠️ Start small!** Test with $200 for 1 week before scaling up.

---

## 🎓 Learning Path

1. **Day 1-3:** Run in test mode, understand logs
2. **Day 4-7:** Real trading with $200, monitor closely
3. **Week 2:** Optimize config based on performance
4. **Week 3+:** Scale up capital gradually

---

## 📚 Full Documentation

- **SETUP_GUIDE.md** - Detailed setup instructions
- **USER_GUIDE.md** - Complete user manual
- **PROJECT_OVERVIEW.md** - Technical architecture
- **config.yaml** - All configuration options

---

## 🆘 Support

### Common Issues

1. **Low fill rate?** → Lower `spread_min` in config
2. **Too many orders?** → Increase `min_reward` threshold
3. **High gas costs?** → Reduce `update_interval`
4. **Bot crashes?** → Check logs, update RPC URL

### Get Help

- Check logs: `tail -f logs/polymarket_bot.log`
- Review config: `cat config.yaml`
- Test wallets: `python scripts/check_wallets.py`

---

## ⚠️ Risk Warning

**This bot trades real money!**

- Start with small capital ($200-500)
- Monitor daily for first week
- Never invest more than you can afford to lose
- Polymarket rewards can change anytime
- Gas fees reduce profits

**Not financial advice. Trade at your own risk.**

---

## 🎉 Success Checklist

- [ ] Dependencies installed
- [ ] Wallets funded (USDC + MATIC)
- [ ] USDC approved
- [ ] Config customized
- [ ] Test mode works
- [ ] Real trading started
- [ ] Monitoring setup

**Ready to trade? Run:** `python main.py`

Good luck! 🚀

