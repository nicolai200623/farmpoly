# 🎁 Automated Reward Checking & Withdrawal Guide

## Overview

The Polymarket Trading Bot now includes an **automated reward checking and withdrawal system** that periodically monitors your trading wallets for available rewards and automatically transfers them to a secure withdrawal wallet when they reach a specified threshold.

## Features

✅ **Automated Reward Checking** - Periodically scans all trading wallets for available USDC rewards  
✅ **Smart Withdrawal** - Automatically withdraws rewards when threshold is met  
✅ **Configurable Thresholds** - Set minimum reward amount before withdrawal  
✅ **Flexible Intervals** - Configure how often to check for rewards  
✅ **Error Handling** - Robust retry logic for failed withdrawals  
✅ **Comprehensive Logging** - Track all reward checks and withdrawals  
✅ **Statistics Tracking** - Monitor total withdrawals and amounts  
✅ **Gas Price Protection** - Avoid withdrawals during high gas periods  

---

## Quick Setup

### 1. Configure Withdrawal Wallet

Edit your `.env` file and add your withdrawal wallet address:

```bash
# Wallet address to receive withdrawn rewards
REWARD_WITHDRAWAL_WALLET=0xYourSecureWalletAddressHere

# Minimum reward threshold (in USDC)
MIN_REWARD_THRESHOLD=10.0

# Check interval (in seconds) - 3600 = 1 hour
REWARD_CHECK_INTERVAL=3600
```

### 2. Enable in Configuration

The feature is enabled by default in `config.yaml`. You can customize settings:

```yaml
reward_management:
  enabled: true
  check_interval: 3600  # Check every 1 hour
  min_withdrawal_threshold: 10.0  # Withdraw when >= $10
  max_gas_price: 500  # Don't withdraw if gas > 500 Gwei
```

### 3. Start the Bot

The reward management system will automatically start with the bot:

```bash
python main.py
```

---

## Configuration Options

### Environment Variables (.env)

| Variable | Description | Default | Example |
|----------|-------------|---------|---------|
| `REWARD_WITHDRAWAL_WALLET` | Wallet address to receive rewards | None (required) | `0x742d35Cc...` |
| `MIN_REWARD_THRESHOLD` | Minimum USDC before withdrawal | 10.0 | `25.0` |
| `REWARD_CHECK_INTERVAL` | Seconds between checks | 3600 | `7200` (2 hours) |
| `POLYMARKET_REWARD_CONTRACT` | Custom reward contract (optional) | Empty | `0x...` |

### Config File (config.yaml)

```yaml
reward_management:
  # Enable/disable the feature
  enabled: true
  
  # Check interval (seconds)
  # 3600 = 1 hour, 7200 = 2 hours, 14400 = 4 hours, 86400 = 24 hours
  check_interval: 3600
  
  # Minimum threshold (USDC)
  min_withdrawal_threshold: 10.0
  
  # Maximum gas price (Gwei)
  max_gas_price: 500
  
  # Retry settings
  max_retry_attempts: 3
  retry_delay: 300  # 5 minutes
  
  # Alert settings
  alert_on_withdrawal: true
  alert_on_withdrawal_failure: true
  alert_on_threshold_reached: true
  
  # Safety limits
  max_withdrawal_per_day: 1000.0  # Maximum USDC per day
```

---

## How It Works

### 1. Reward Checking

The system periodically checks all trading wallets for USDC balances:

```
Every [check_interval] seconds:
  ├─ Check USDC balance for each wallet
  ├─ Compare against min_withdrawal_threshold
  └─ Log total rewards across all wallets
```

### 2. Automatic Withdrawal

When a wallet's rewards meet the threshold:

```
If wallet_balance >= min_withdrawal_threshold:
  ├─ Verify withdrawal wallet is configured
  ├─ Check current gas price
  ├─ Build USDC transfer transaction
  ├─ Sign with wallet's private key
  ├─ Send transaction to blockchain
  ├─ Wait for confirmation
  └─ Update statistics
```

### 3. Transaction Flow

```
Trading Wallet → [USDC Transfer] → Withdrawal Wallet
     ↓
  Rewards earned from trading
     ↓
  Automatically detected
     ↓
  Transferred when threshold met
```

---

## Usage Examples

### Example 1: Conservative Setup (Daily Withdrawals)

```bash
# .env
REWARD_WITHDRAWAL_WALLET=0xYourSecureWallet
MIN_REWARD_THRESHOLD=50.0
REWARD_CHECK_INTERVAL=86400  # Check once per day
```

**Use case:** You want to withdraw rewards once daily when you have at least $50.

### Example 2: Aggressive Setup (Frequent Withdrawals)

```bash
# .env
REWARD_WITHDRAWAL_WALLET=0xYourSecureWallet
MIN_REWARD_THRESHOLD=5.0
REWARD_CHECK_INTERVAL=3600  # Check every hour
```

**Use case:** You want to withdraw small amounts frequently to minimize exposure.

### Example 3: High-Volume Setup

```bash
# .env
REWARD_WITHDRAWAL_WALLET=0xYourSecureWallet
MIN_REWARD_THRESHOLD=100.0
REWARD_CHECK_INTERVAL=14400  # Check every 4 hours
```

**Use case:** You're trading with high capital and want to withdraw larger amounts less frequently.

---

## Monitoring & Logs

### Log Messages

The system provides detailed logging:

```
✅ Reward Manager initialized
   Check interval: 1.0h
   Min withdrawal threshold: $10.00
   Withdrawal wallet: 0x742d35Cc...

🔍 Checking rewards...
💰 Total rewards across 5 wallets: $45.23 USDC

💸 Withdrawing $45.23 USDC from 0x742d35Cc... to 0x853d955a...
📤 Transaction sent: 0xabcd1234...
⏳ Waiting for confirmation...
✅ Withdrawal successful! TX: 0xabcd1234...
   Amount: $45.23 USDC
   Gas used: 65432

📊 Reward Manager Statistics:
   Total checks: 24
   Total withdrawals: 3
   Total withdrawn: $125.50 USDC
   Failed withdrawals: 0
   Check errors: 0
```

### Statistics Tracking

Access statistics programmatically:

```python
stats = reward_manager.get_statistics()
print(f"Total withdrawn: ${stats['total_withdrawn_amount']:.2f}")
print(f"Success rate: {stats['total_withdrawals'] / (stats['total_withdrawals'] + stats['failed_withdrawals']):.1%}")
```

---

## Security Best Practices

### 🔐 Withdrawal Wallet Security

1. **Use a separate secure wallet** for receiving rewards
2. **Never use a hot wallet** that's actively trading
3. **Consider a hardware wallet** for maximum security
4. **Enable 2FA** on any services managing this wallet

### 🛡️ Private Key Protection

1. **Never commit `.env`** to version control
2. **Use encrypted storage** for production deployments
3. **Rotate keys regularly** if compromised
4. **Monitor withdrawal wallet** for unauthorized activity

### ⚠️ Gas Price Protection

The system automatically checks gas prices before withdrawal:

```python
if gas_price > max_gas_price:
    logger.warning("Gas price too high, skipping withdrawal")
    # Will retry on next check
```

---

## Troubleshooting

### Issue: No withdrawals happening

**Check:**
1. Is `REWARD_WITHDRAWAL_WALLET` set in `.env`?
2. Are rewards above `MIN_REWARD_THRESHOLD`?
3. Is the feature enabled in `config.yaml`?
4. Check logs for error messages

### Issue: Withdrawal failed

**Common causes:**
1. **Insufficient gas** - Ensure wallets have MATIC for gas fees
2. **High gas prices** - System waits for lower gas prices
3. **Invalid withdrawal wallet** - Verify address is correct
4. **Network issues** - Check RPC connection

**Solution:**
```bash
# Check wallet balances
python scripts/check_wallets.py

# Verify configuration
cat .env | grep REWARD

# Check logs
tail -f logs/polymarket_bot.log | grep -i reward
```

### Issue: Rewards not detected

**Check:**
1. Are wallets actually earning rewards?
2. Is the RPC URL working?
3. Check USDC contract address is correct (Polygon: `0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174`)

---

## Advanced Configuration

### Custom Check Intervals

```yaml
# Check every 30 minutes
check_interval: 1800

# Check every 6 hours
check_interval: 21600

# Check once per day at midnight (use with daily_optimization)
check_interval: 86400
```

### Dynamic Thresholds

You can modify thresholds based on market conditions:

```python
# In your custom script
if high_volatility:
    reward_manager.min_withdrawal_threshold = 5.0  # Withdraw more frequently
else:
    reward_manager.min_withdrawal_threshold = 50.0  # Accumulate more
```

### Multiple Withdrawal Wallets

For advanced users managing multiple strategies:

```python
# Custom logic to route rewards to different wallets
if wallet['strategy'] == 'aggressive':
    withdrawal_wallet = '0xWallet1...'
else:
    withdrawal_wallet = '0xWallet2...'
```

---

## Testing

### Run Unit Tests

```bash
# Test reward manager
python -m pytest tests/test_reward_manager.py -v

# Test specific function
python -m pytest tests/test_reward_manager.py::TestRewardManager::test_check_rewards_async -v
```

### Manual Testing

```bash
# Set low threshold for testing
export MIN_REWARD_THRESHOLD=0.1

# Run bot in test mode
python main.py
```

---

## FAQ

**Q: How much gas does a withdrawal cost?**  
A: Typically 50,000-100,000 gas. At 50 Gwei, this is ~0.005 MATIC ($0.003-0.006).

**Q: Can I disable automatic withdrawal?**  
A: Yes, set `enabled: false` in `config.yaml` under `reward_management`.

**Q: What happens if withdrawal fails?**  
A: The system logs the error and retries on the next check interval.

**Q: Can I withdraw to multiple wallets?**  
A: Currently supports one withdrawal wallet. Modify `reward_manager.py` for custom logic.

**Q: Does this work with testnet?**  
A: Yes, configure your RPC URL to a testnet and use testnet wallets.

---

## Support

For issues or questions:
1. Check logs: `tail -f logs/polymarket_bot.log`
2. Review configuration: `cat config.yaml`
3. Test wallets: `python scripts/check_wallets.py`
4. Open an issue on GitHub with logs and configuration

---

## Changelog

### v1.0.0 (2025-11-03)
- ✅ Initial release
- ✅ Automated reward checking
- ✅ Automatic withdrawal to configured wallet
- ✅ Configurable thresholds and intervals
- ✅ Comprehensive error handling
- ✅ Statistics tracking
- ✅ Gas price protection

---

**⚠️ Disclaimer:** This feature handles real funds. Always test with small amounts first and monitor closely. Never risk more than you can afford to lose.

