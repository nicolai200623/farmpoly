# 🤖 Polymarket Competitive Trading Bot - Tổng Quan Dự Án

## 📌 Giới Thiệu

Polymarket Competitive Trading Bot là một hệ thống giao dịch tự động tiên tiến được thiết kế để cạnh tranh trong chương trình phần thưởng của Polymarket. Bot sử dụng 8 module chuyên biệt kết hợp với Machine Learning để tối ưu hóa lợi nhuận và quản lý rủi ro.

## 🎯 Mục Tiêu

- **Mục tiêu chính**: Cạnh tranh trong top 1% traders trên Polymarket
- **Lợi nhuận mục tiêu**: $100-150/ngày
- **Tỷ lệ thắng**: >60%
- **Hiệu suất vốn**: 80%

## 🏗️ Kiến Trúc Hệ Thống

### Tổng Quan Kiến Trúc

```
┌─────────────────────────────────────────────────────────────┐
│                   POLYMARKET TRADING BOT                     │
│                     Main Orchestrator                        │
└──────────────────────┬──────────────────────────────────────┘
                       │
        ┌──────────────┼──────────────┐
        │              │              │
┌───────▼──────┐ ┌────▼─────┐ ┌─────▼──────┐
│   Market     │ │  Market  │ │   Order    │
│   Scanner    │ │ Selector │ │  Manager   │
│              │ │   (AI)   │ │            │
└──────────────┘ └──────────┘ └────────────┘
        │              │              │
┌───────▼──────┐ ┌────▼─────┐ ┌─────▼──────┐
│  Position    │ │   Risk   │ │   Wallet   │
│  Monitor     │ │  Manager │ │  Manager   │
│              │ │          │ │            │
└──────────────┘ └──────────┘ └────────────┘
        │              │
┌───────▼──────┐ ┌────▼─────┐
│     ML       │ │  Daily   │
│  Predictor   │ │Optimizer │
│  (PyTorch)   │ │          │
└──────────────┘ └──────────┘
```

### 8 Module Chính

#### 1. Market Scanner (market_scanner.py)
**Chức năng:**
- Quét trang /rewards của Polymarket mỗi 5 giây
- Sử dụng Selenium để scrape dynamic content
- Fetch data từ multiple API endpoints

**Bộ lọc:**
- Competition < 2 bars
- Reward > $300
- Min shares < 500
- Focus: Sports, entertainment, illiquid markets

**Công nghệ:**
- BeautifulSoup4 cho HTML parsing
- Selenium cho JavaScript rendering
- aiohttp cho async API calls

#### 2. Market Selector AI (market_selector.py)
**Chức năng:**
- Đánh giá và chọn thị trường tốt nhất
- Scoring algorithm: `(reward/competition) * (1/volume_spike)`

**Tiêu chí:**
- Reward cao, competition thấp
- Không có volume spike đột ngột
- Ưu tiên sports và illiquid markets
- ML-based market evaluation

#### 3. Order Manager (order_manager.py)
**Chức năng:**
- Đặt lệnh limit 2 bên (YES và NO)
- Dynamic spread: Mid ± 0.8-1.5¢
- Position size: 200-500 shares với jitter

**Tính năng:**
- Tích hợp py-clob-client
- Order lifecycle management
- Price improvement attempts
- Cancel and replace logic

#### 4. Position Monitor (position_monitor.py)
**Chức năng:**
- WebSocket real-time monitoring (10s intervals)
- Theo dõi fills và market conditions

**Auto-cancel khi:**
- Partial fill > 10%
- Volume spike > 2x
- Price movement > 2¢
- Position timeout (1 hour)

#### 5. Risk Manager (risk_manager.py)
**Chức năng:**
- Quản lý rủi ro portfolio
- Capital allocation
- Auto-hedging

**Giới hạn:**
- Max 5% capital per market
- Max 80% total exposure
- Max 3 markets per category
- Stop loss 15%

**Hedging:**
- Tự động hedge khi imbalance >60%
- Partial hedge (50% of imbalance)
- YES/NO arbitrage detection

#### 6. Wallet Manager (wallet_manager.py)
**Chức năng:**
- Quản lý 5-10 wallets
- Rotation với human-like behavior
- Jitter ±20% cho size và timing

**Human Simulation:**
- Random delays (0.5-2s)
- Time-of-day patterns
- Random breaks (5% chance)
- Cooldown periods (30s)

#### 7. ML Predictor (ml_predictor.py)
**Chức năng:**
- PyTorch neural network
- Dự đoán fill probability
- Alert khi risk >80%

**Architecture:**
- Input: 20 features
- Layers: 20→64→32→16→1
- Training: Hourly updates
- Target accuracy: >75%

**Features:**
- Market data (spread, volume, liquidity)
- Time features (hour, business hours)
- Competition metrics
- Historical performance

#### 8. Daily Optimizer (optimizer.py)
**Chức năng:**
- Chạy lúc UTC 00:00
- Tính toán daily P&L
- Strategy adjustment
- Performance analytics

**Optimization:**
- Payout calculation
- Market redeployment
- Parameter tuning
- Performance reports

## 🔧 Công Nghệ Sử Dụng

### Backend
- **Python 3.8+**: Core language
- **asyncio**: Async framework
- **aiohttp**: Async HTTP client
- **websockets**: Real-time data

### Blockchain
- **web3.py**: Ethereum interaction
- **eth-account**: Wallet management
- **py-clob-client**: Polymarket CLOB API

### Web Scraping
- **Selenium**: Dynamic content
- **BeautifulSoup4**: HTML parsing
- **lxml**: XML/HTML processing

### Machine Learning
- **PyTorch**: Neural networks
- **NumPy**: Numerical computing
- **Pandas**: Data analysis
- **scikit-learn**: ML utilities

### Configuration & Storage
- **PyYAML**: Config management
- **python-dotenv**: Environment variables
- **SQLite/PostgreSQL**: Optional database
- **Redis**: Optional caching

### Monitoring
- **Telegram Bot API**: Alerts
- **Discord/Slack Webhooks**: Notifications
- **Python logging**: Log management

## 📊 Chiến Lược Trading

### Market Selection Strategy

**Scoring Formula:**
```python
score = (reward / competition) * (1 / volume_spike) * category_weight

category_weights = {
    'sports': 1.0,
    'entertainment': 0.9,
    'crypto': 0.8,
    'politics': 0.6,
    'other': 0.3
}
```

**Filters:**
1. Competition bars ≤ 2
2. Reward ≥ $300
3. Min shares ≤ 500
4. No recent volume spike (>2x)
5. Liquidity < $10k (illiquid preferred)

### Order Placement Strategy

**Spread Calculation:**
```python
base_spread = (spread_min + spread_max) / 2
dynamic_spread = base_spread * spread_multiplier

# Adjust based on:
- Current market spread
- Volume imbalance
- Competition level
```

**Position Sizing:**
```python
base_size = (size_min + size_max) / 2
actual_size = base_size * (1 + random(-0.2, 0.2))  # ±20% jitter

# Round to human numbers sometimes
if random() < 0.3:
    actual_size = round_to_50_or_100(actual_size)
```

**Dual-Side Liquidity:**
- Always place both YES and NO orders
- Capture spread on both sides
- Maintain market neutrality

### Risk Management Strategy

**Capital Allocation:**
- Max 5% per market
- Max 80% total exposure
- 20% reserve for opportunities

**Hedging Rules:**
```python
if imbalance > 60%:
    hedge_size = abs(net_exposure) * 0.5
    place_hedge_order(opposite_side, hedge_size)
```

**Stop Loss:**
- Per market: -15%
- Daily: -$500
- Auto-exit on threshold

### ML Prediction Strategy

**Training:**
- Continuous learning from fills
- Hourly model updates
- 10,000 sample history

**Prediction:**
```python
fill_probability = model.predict(features)

if fill_probability > 0.8:
    cancel_order()  # Avoid adverse selection
    send_alert()
```

## 📈 Performance Metrics

### Key Metrics

**Profitability:**
- Daily P&L
- Win rate
- Average profit per trade
- ROI

**Efficiency:**
- Fill rate
- Spread captured
- Capital utilization
- Orders per day

**Risk:**
- Max drawdown
- Sharpe ratio
- Value at Risk (VaR)
- Exposure ratio

### Expected Performance

**Conservative (Spread 1.2-1.5¢):**
- Daily profit: $50-100
- Fill rate: 20-30%
- Win rate: 70%
- Risk: Low

**Moderate (Spread 0.8-1.2¢):**
- Daily profit: $100-150
- Fill rate: 30-50%
- Win rate: 60%
- Risk: Medium

**Aggressive (Spread 0.6-0.8¢):**
- Daily profit: $150-250
- Fill rate: 50-70%
- Win rate: 50%
- Risk: High

## 🔐 Bảo Mật

### Security Measures

**Wallet Security:**
- Private keys encrypted
- Never logged or displayed
- Separate wallets for bot
- Hardware wallet for main funds

**API Security:**
- Rate limiting
- Request signing
- IP whitelisting (optional)
- API key rotation

**Code Security:**
- .env not in git
- Secrets in environment variables
- Input validation
- Error handling

### Best Practices

1. **Never commit sensitive data**
2. **Use strong passwords**
3. **Enable 2FA everywhere**
4. **Regular security audits**
5. **Monitor for unusual activity**
6. **Backup regularly**
7. **Update dependencies**

## 📁 Cấu Trúc Thư Mục

```
polymarket-bot/
├── main.py                 # Main orchestrator
├── config.yaml            # Configuration
├── .env                   # Environment variables (not in git)
├── .env.example          # Example env file
├── requirements.txt      # Python dependencies
├── Dockerfile           # Docker image
├── docker-compose.yml   # Docker compose
├── .gitignore          # Git ignore rules
│
├── modules/            # Core modules (if organized)
│   ├── market_scanner.py
│   ├── market_selector.py
│   ├── order_manager.py
│   ├── position_monitor.py
│   ├── risk_manager.py
│   ├── wallet_manager.py
│   ├── ml_predictor.py
│   └── optimizer.py
│
├── scripts/           # Utility scripts
│   ├── check_wallets.py
│   ├── generate_wallets.py
│   └── backup.sh
│
├── logs/             # Log files
│   └── polymarket_bot.log
│
├── models/           # ML models
│   └── fill_predictor.pt
│
├── data/            # Data storage
│   ├── training_data.pkl
│   └── bot_data.db
│
├── backups/         # Backups
│   └── YYYYMMDD_HHMMSS/
│
└── docs/           # Documentation
    ├── README.md
    ├── SETUP_GUIDE.md
    ├── USER_GUIDE.md
    └── PROJECT_OVERVIEW.md
```

## 🚀 Deployment Options

### 1. Local Machine
- Chạy trực tiếp trên máy tính
- Dễ debug và monitor
- Cần máy luôn bật

### 2. VPS (Recommended)
- DigitalOcean, Linode, AWS EC2
- Uptime cao
- Chi phí: $5-20/tháng

### 3. Docker
- Portable và consistent
- Dễ deploy và scale
- Isolation tốt

### 4. Multi-Instance
- Chạy nhiều instance
- Diversification
- Higher throughput

## 📞 Support & Resources

### Documentation
- **README.md**: Tổng quan và quick start
- **SETUP_GUIDE.md**: Hướng dẫn cài đặt chi tiết
- **USER_GUIDE.md**: Hướng dẫn sử dụng
- **PROJECT_OVERVIEW.md**: Tài liệu này

### Community
- GitHub Issues
- Discord/Telegram
- Email support

### External Resources
- [Polymarket Docs](https://docs.polymarket.com/)
- [CLOB API Docs](https://docs.polymarket.com/api)
- [py-clob-client](https://github.com/Polymarket/py-clob-client)

## ⚠️ Disclaimer

**QUAN TRỌNG:**

1. **Rủi ro**: Trading có rủi ro. Chỉ trade với tiền bạn có thể mất.
2. **Không đảm bảo**: Không có đảm bảo lợi nhuận.
3. **Giáo dục**: Bot này chỉ cho mục đích giáo dục.
4. **Tuân thủ**: Đảm bảo tuân thủ luật pháp địa phương.
5. **Tự chịu trách nhiệm**: Bạn chịu trách nhiệm cho mọi quyết định.

## 📄 License

MIT License - See LICENSE file for details

---

**Version**: 1.0.0  
**Last Updated**: 2024  
**Author**: Polymarket Bot Team

---

*Tài liệu này cung cấp cái nhìn tổng quan về dự án. Xem các tài liệu khác để biết chi tiết.*

