# Polymarket Trading Bot Architecture

## System Overview
A competitive market-making bot for Polymarket using CLOB API with 8 specialized modules.

## Core Modules

### 1. Market Scanner Module
- Scrapes /rewards page every 5 seconds
- Filters: comp < 2 bars, reward > $300, min_shares < 500
- Technologies: BeautifulSoup, Selenium for dynamic content

### 2. Market Selection AI
- Scoring algorithm: (reward/competition) * (1/volume_spike)
- Focus on sports and illiquid markets
- ML-based market evaluation

### 3. Order Management
- Dynamic spread: Mid ± 0.8-1.5¢
- Position size: 200-500 shares
- Dual-side liquidity provision

### 4. Position Monitor
- WebSocket real-time monitoring (10s intervals)
- Auto-cancel conditions:
  - Partial fill > 10%
  - Volume spike > 2x
  - Price movement > 2¢

### 5. Risk Management
- Max 5% capital per market
- Auto-hedging on one-sided fills
- YES/NO arbitrage detection

### 6. Wallet Management
- 5-10 wallet rotation
- Human-like behavior simulation
- Random size/time variation (±20%)

### 7. ML Prediction & Alerts
- PyTorch model for fill prediction
- Telegram/Discord notifications
- 80% fill risk threshold alerts

### 8. Daily Optimization
- UTC 00:00 payout calculation
- Market redeployment strategy
- Performance analytics

## Technical Stack
- **Async Framework**: Python asyncio
- **APIs**: py-clob-client, WebSocket
- **ML**: PyTorch for predictions
- **Data**: BeautifulSoup, Selenium
- **Deployment**: VPS multi-instance
- **Config**: YAML-based settings