# Polymarket Trading Bot - Advanced Market Making System

## 🚀 Overview

A sophisticated trading bot for Polymarket using CLOB API with 8 competitive modules designed to compete in the top 1% of traders. The bot implements advanced strategies including ML-based fill prediction, dynamic spread adjustment, multi-wallet rotation, and real-time risk management.

## ⚡ Key Features

### 8 Core Modules

1. **Market Scanner Pro** - 5-second scraping of rewards page for opportunities
2. **AI Market Selector** - ML-powered market scoring and selection
3. **Dynamic Order Manager** - Intelligent spread and size management
4. **Position Monitor** - Real-time WebSocket monitoring with auto-cancellation
5. **Risk Shield** - Portfolio risk management and auto-hedging
6. **Wallet Manager** - Multi-wallet rotation with human-like behavior
7. **ML Predictor** - PyTorch model for fill prediction and alerts
8. **Daily Optimizer** - Automated strategy optimization at UTC 00:00

## 📊 Performance Targets

- **Daily Profit Target**: $100-150
- **Fill Rate**: 30-50%
- **Win Rate**: >60%
- **Max Drawdown**: $500
- **Capital Efficiency**: 80%

## 🛠️ Installation

### Prerequisites

- Python 3.8+
- Chrome/Chromium browser (for Selenium)
- PostgreSQL (optional)
- Redis (optional)

### Setup Steps

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/polymarket-bot.git
cd polymarket-bot
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Install ChromeDriver**
```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install chromium-chromedriver

# macOS
brew install chromedriver

# Or download manually from https://chromedriver.chromium.org/
```

4. **Configure environment**
```bash
cp .env.example .env
# Edit .env with your wallet keys and API credentials
nano .env
```

5. **Configure strategy**
```bash
# Edit config.yaml to adjust trading parameters
nano config.yaml
```

6. **Initialize wallets**
```bash
# Fund your wallets with USDC and MATIC on Polygon
# Minimum recommended: $1000 USDC + 10 MATIC per wallet
```

## 🚦 Usage

### Starting the Bot

```bash
# Standard mode
python main.py

# With custom config
python main.py --config custom_config.yaml

# Debug mode
python main.py --debug

# Dry run (no real orders)
python main.py --dry-run
```

### Monitoring

The bot provides real-time monitoring through:
- Console logs
- Telegram alerts (if configured)
- Discord/Slack webhooks (if configured)
- Performance dashboard (access logs)

### Commands

While running, the bot responds to signals:
- `CTRL+C` - Graceful shutdown (cancels all orders)
- `SIGUSR1` - Force rebalancing
- `SIGUSR2` - Dump performance stats

## ⚙️ Configuration

### Key Parameters (config.yaml)

```yaml
market_scanner:
  interval: 5  # Scanning frequency (seconds)
  min_reward: 300  # Minimum reward threshold
  max_competition_bars: 2  # Competition filter

order_management:
  spread_min: 0.008  # Tightest spread (0.8¢)
  spread_max: 0.015  # Widest spread (1.5¢)
  size_min: 200  # Minimum position size
  size_max: 500  # Maximum position size

risk_management:
  max_capital_per_market: 0.05  # 5% max per market
  enable_hedging: true  # Auto-hedging enabled
```

### Alert Setup

1. **Telegram**:
   - Create bot via @BotFather
   - Get bot token and chat ID
   - Add to .env file

2. **Discord**:
   - Create webhook in server settings
   - Add webhook URL to .env

## 📈 Strategy Details

### Market Selection Algorithm

```
Score = (Reward / Competition) × (1 / Volume_Spike) × Category_Weight
```

- Prioritizes: Sports, entertainment, illiquid markets
- Avoids: High competition (>2 bars), volume spikes >2x

### Order Placement

- **Spread Calculation**: Dynamic based on market conditions
- **Both Sides**: Always provides liquidity on YES and NO
- **Size Variation**: ±20% jitter for human-like behavior

### Risk Management

- Maximum 5% capital per market
- Automatic hedging when exposure >60% on one side
- Portfolio rebalancing every 30 minutes
- Daily loss limit: $500

## 🤖 Machine Learning

The bot uses a 4-layer neural network for fill prediction:
- **Input**: 20 features (market data, timing, competition)
- **Architecture**: 20→64→32→16→1
- **Training**: Hourly updates on historical data
- **Accuracy Target**: >75%

## 📊 Performance Monitoring

### Daily Reports Include

- Total P&L
- Fill rate by market category
- Win/loss ratio
- Optimal trading hours
- Strategy adjustments

### Metrics Tracked

- Order fill rate
- Average spread captured
- Capital utilization
- Risk-adjusted returns
- Market timing effectiveness

## 🔧 Advanced Features

### Backtesting

```bash
# Run 30-day backtest
python backtest.py --days 30

# Specific date range
python backtest.py --start 2024-01-01 --end 2024-01-31
```

### Database Integration

Optional PostgreSQL for:
- Trade history
- Performance analytics
- Strategy optimization data

### Multi-Instance Deployment

```bash
# Run multiple instances on different VPS
python deploy.py --instances 3 --config production.yaml
```

## ⚠️ Risk Disclaimer

**IMPORTANT**: Trading involves substantial risk. This bot is for educational purposes. 
- Start with small amounts
- Test thoroughly in dry-run mode
- Monitor actively during initial deployment
- Never risk more than you can afford to lose

## 🛡️ Security Best Practices

1. **Never commit private keys** to version control
2. **Use encrypted wallet storage** in production
3. **Implement IP whitelisting** for API access
4. **Regular security audits** of dependencies
5. **Monitor for unusual activity**

## 📝 Compliance Note

This bot operates within Polymarket's terms of service:
- No wash trading
- No market manipulation
- Legitimate market making only
- Complies with rate limits

## 🔄 Updates & Maintenance

### Daily Tasks
- Review optimization reports
- Check wallet balances
- Monitor alert channels

### Weekly Tasks
- Analyze performance trends
- Adjust strategy parameters
- Update ML model training data

### Monthly Tasks
- Full strategy review
- Wallet rotation
- Security audit

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create feature branch
3. Add tests for new features
4. Submit pull request

## 📞 Support

- GitHub Issues: Bug reports and feature requests
- Telegram Group: [Join community]
- Documentation: [Full docs]

## 📄 License

MIT License - See LICENSE file for details

## ⭐ Acknowledgments

- Polymarket for CLOB API
- py-clob-client developers
- Community contributors

---

**Remember**: Success in trading requires discipline, continuous learning, and risk management. Start small, learn continuously, and scale gradually.

**Target**: Beat aesparing2 and reach top 1% 🎯