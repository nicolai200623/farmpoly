2025-11-10 14:13:30,169 - __main__ - INFO - âœ… Using MarketScannerV2 (Playwright + Gamma API)
2025-11-10 14:13:34,146 - __main__ - INFO - ðŸ“‚ Loading config from: config.yaml
2025-11-10 14:13:34,178 - __main__ - INFO - âœ… Config loaded successfully
2025-11-10 14:13:34,179 - __main__ - INFO -    - min_reward: 20
2025-11-10 14:13:34,179 - __main__ - INFO -    - max_competition_bars: 3
2025-11-10 14:13:34,179 - __main__ - INFO -    - interval: 60s
2025-11-10 14:13:34,179 - __main__ - INFO - âœ… Telegram alerts configured (Chat ID: -1003157421030)
2025-11-10 14:13:34,179 - __main__ - INFO - âœ… Webhook alerts configured
2025-11-10 14:13:34,179 - telegram_notifier - INFO - âœ… Telegram Notifier initialized (Chat ID: -1003157421030)
2025-11-10 14:13:34,179 - __main__ - INFO - âœ… Telegram Notifier initialized
2025-11-10 14:13:34,179 - __main__ - INFO - âœ… OrderBook WebSocket initialized
2025-11-10 14:13:34,179 - market_scanner_v2 - INFO - ðŸ“Š Market Scanner initialized with:
2025-11-10 14:13:34,179 - market_scanner_v2 - INFO -    - min_reward: $20
2025-11-10 14:13:34,179 - market_scanner_v2 - INFO -    - max_competition_bars: 3
2025-11-10 14:13:34,179 - market_scanner_v2 - INFO -    - target_categories: ALL (no filter)
2025-11-10 14:13:34,179 - market_scanner_v2 - INFO - âœ… CLOB client initialized for orderbook verification (spread check enabled)
2025-11-10 14:13:34,179 - circuit_breaker - INFO - âœ… Circuit Breaker 'playwright_scraper' initialized (threshold=3, timeout=60s)
2025-11-10 14:13:34,179 - circuit_breaker - INFO - âœ… Circuit Breaker 'playwright_scraper' initialized (threshold=3, timeout=120s)
2025-11-10 14:13:34,179 - order_manager - INFO - CLOB client initialized successfully (read-only mode)
2025-11-10 14:13:34,188 - wallet_manager - INFO - Loading REAL wallets from .env
2025-11-10 14:13:34,194 - wallet_manager - INFO - âœ… Loaded wallet 1: 0x18F261DC...Ae4FfD96
2025-11-10 14:13:34,194 - wallet_manager - INFO - âœ… Successfully loaded 1 real wallets
2025-11-10 14:13:34,204 - ml_predictor - INFO - No pre-trained model found, using new model
2025-11-10 14:13:34,204 - monitoring_system - INFO - âœ… Monitoring System initialized
2025-11-10 14:13:34,204 - __main__ - INFO - âœ… Monitoring System enabled
2025-11-10 14:13:34,204 - __main__ - INFO - â­ï¸  Reward Manager disabled in config
2025-11-10 14:13:34,918 - profit_taking_manager - INFO - âœ… CLOB client initialized with API credentials
2025-11-10 14:13:34,919 - profit_taking_manager - INFO - âœ… Profit Taking Manager initialized
2025-11-10 14:13:34,919 - profit_taking_manager - INFO -    - Min profit: 50%
2025-11-10 14:13:34,919 - profit_taking_manager - INFO -    - Target profit: 50%
2025-11-10 14:13:34,919 - profit_taking_manager - INFO -    - Max profit: 150%
2025-11-10 14:13:34,919 - profit_taking_manager - INFO -    - Check interval: 300s
2025-11-10 14:13:34,919 - __main__ - INFO - âœ… Profit Taking Manager enabled
2025-11-10 14:13:34,920 - __main__ - INFO - âœ… Order Repositioner enabled
2025-11-10 14:13:34,920 - __main__ - INFO - All modules initialized successfully
2025-11-10 14:13:34,920 - __main__ - INFO - ðŸš€ Starting Polymarket Trading Bot...
2025-11-10 14:13:35,928 - __main__ - INFO - âœ… Startup alert sent via TelegramNotifier
2025-11-10 14:13:35,929 - __main__ - INFO - ðŸ” Checking USDC approval for wallets...
2025-11-10 14:13:36,288 - usdc_approver - INFO - âœ… Connected to Polygon RPC: https://polygon-mainnet.g.alchemy.com/v2/FQJnJWsEQ...
2025-11-10 14:13:36,288 - __main__ - INFO -    Checking wallet: 0x18F261DC...Ae4FfD96
2025-11-10 14:13:36,607 - __main__ - INFO -    Raw allowance: 920321200 (base units)
2025-11-10 14:13:36,607 - __main__ - INFO -    Allowance in USDC: 920.32 USDC
2025-11-10 14:13:36,608 - __main__ - INFO -    Required minimum: 100 USDC (test mode)
2025-11-10 14:13:36,608 - __main__ - INFO - âœ… USDC approval OK (920 USDC)
2025-11-10 14:13:36,608 - __main__ - WARNING -    âš ï¸  Running in TEST MODE with 920 USDC
2025-11-10 14:13:36,608 - __main__ - WARNING -    For production, approve at least 1,000 USDC
2025-11-10 14:13:36,608 - __main__ - INFO - ðŸ” Starting market scanning loop
2025-11-10 14:13:36,608 - market_scanner_v2 - INFO - ðŸŒ Scraping markets from /rewards page using Playwright...
2025-11-10 14:13:36,608 - playwright_rewards_scraper - INFO - ðŸŒ Fetching markets from /rewards API...
2025-11-10 14:13:36,608 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 1 (cursor: MA==)...
2025-11-10 14:13:36,609 - __main__ - INFO - ðŸ“¦ Starting order management loop
2025-11-10 14:13:36,609 - __main__ - INFO - ðŸ‘ï¸  Starting position monitoring loop
2025-11-10 14:13:36,609 - __main__ - INFO - ðŸ›¡ï¸  Starting risk management loop
2025-11-10 14:13:36,609 - __main__ - INFO - ðŸ¤– Starting ML training loop
2025-11-10 14:13:36,609 - ml_predictor - INFO - Insufficient training data: 0 samples
2025-11-10 14:13:36,609 - __main__ - INFO - ML model updated successfully
2025-11-10 14:13:36,609 - __main__ - INFO - ðŸ“Š Starting daily optimization loop
2025-11-10 14:13:36,609 - __main__ - INFO - ðŸ¥ Starting health monitoring loop
2025-11-10 14:13:37,611 - __main__ - INFO - ðŸ“ˆ Starting hourly report loop
2025-11-10 14:13:37,612 - __main__ - INFO - ðŸ“¡ Starting OrderBook WebSocket loop
2025-11-10 14:13:37,612 - orderbook_websocket - INFO - ðŸ”Œ Connecting to WebSocket: wss://ws-subscriptions-clob.polymarket.com/ws/market
2025-11-10 14:13:37,616 - __main__ - INFO - ðŸ’° Starting automated profit taking loop
2025-11-10 14:13:37,617 - profit_taking_manager - INFO - ðŸ” Checking positions for wallet: 0x18F261DC...Ae4FfD96
2025-11-10 14:13:37,992 - profit_taking_manager - INFO - ðŸ“Š Found 8 active positions
2025-11-10 14:13:37,992 - profit_taking_manager - WARNING - âš ï¸  Skipping position FIDE World Cup 2025 - Shant Sa - invalid data (shares=113.0, avg=0.09, current=0.0)
2025-11-10 14:13:37,992 - profit_taking_manager - INFO - 
ðŸ“ˆ Position: Will Google Gemini 3 score at least 70% on the Fro
2025-11-10 14:13:37,992 - profit_taking_manager - INFO -    Shares: 68.00 @ $0.3900
2025-11-10 14:13:37,992 - profit_taking_manager - INFO -    Current: $0.0700
2025-11-10 14:13:37,992 - profit_taking_manager - INFO -    P&L: $-21.76 (-82.05%)
2025-11-10 14:13:37,992 - profit_taking_manager - INFO -    â¸ï¸  Losing position - NOT closing (manual decision required)
2025-11-10 14:13:37,992 - profit_taking_manager - WARNING - âš ï¸  Skipping position Syracuse vs. Miami - invalid data (shares=66.0, avg=0.49, current=0.0)
2025-11-10 14:13:37,993 - profit_taking_manager - WARNING - âš ï¸  Skipping position FIDE World Cup 2025 - Michael  - invalid data (shares=65.001889, avg=0.180036, current=0.0)
2025-11-10 14:13:37,993 - profit_taking_manager - INFO - 
ðŸ“ˆ Position: Weed rescheduled in 2025?
2025-11-10 14:13:37,993 - profit_taking_manager - INFO -    Shares: 54.43 @ $0.1100
2025-11-10 14:13:37,993 - profit_taking_manager - INFO -    Current: $0.1050
2025-11-10 14:13:37,993 - profit_taking_manager - INFO -    P&L: $-0.27 (-4.55%)
2025-11-10 14:13:37,993 - profit_taking_manager - INFO -    â¸ï¸  Losing position - NOT closing (manual decision required)
2025-11-10 14:13:37,993 - profit_taking_manager - INFO - 
ðŸ“ˆ Position: Supreme Court vacancy in 2025?
2025-11-10 14:13:37,993 - profit_taking_manager - INFO -    Shares: 44.21 @ $0.0600
2025-11-10 14:13:37,993 - profit_taking_manager - INFO -    Current: $0.0500
2025-11-10 14:13:37,993 - profit_taking_manager - INFO -    P&L: $-0.44 (-16.67%)
2025-11-10 14:13:37,993 - profit_taking_manager - INFO -    â¸ï¸  Losing position - NOT closing (manual decision required)
2025-11-10 14:13:37,993 - profit_taking_manager - INFO - 
ðŸ“ˆ Position: Dan Clancy out as Twitch CEO in 2025?
2025-11-10 14:13:37,993 - profit_taking_manager - INFO -    Shares: 30.78 @ $0.0900
2025-11-10 14:13:37,993 - profit_taking_manager - INFO -    Current: $0.0800
2025-11-10 14:13:37,993 - profit_taking_manager - INFO -    P&L: $-0.31 (-11.11%)
2025-11-10 14:13:37,993 - profit_taking_manager - INFO -    â¸ï¸  Losing position - NOT closing (manual decision required)
2025-11-10 14:13:37,993 - profit_taking_manager - WARNING - âš ï¸  Skipping position Charlotte 49ers vs. East Carol - invalid data (shares=0.017509, avg=0.14942, current=0.0)
2025-11-10 14:13:37,993 - __main__ - INFO - â³ Next profit check in 300s
2025-11-10 14:13:37,993 - __main__ - INFO - ðŸ”„ Starting automated order repositioning loop
2025-11-10 14:13:37,993 - order_repositioner - INFO - ðŸ”„ Starting order repositioning loop
2025-11-10 14:13:38,503 - orderbook_websocket - INFO - âœ… WebSocket connected successfully
2025-11-10 14:13:38,694 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 1
2025-11-10 14:13:38,695 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 2 (cursor: MTAw)...
2025-11-10 14:13:39,390 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 2
2025-11-10 14:13:39,391 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 3 (cursor: MjAw)...
2025-11-10 14:13:39,843 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 3
2025-11-10 14:13:39,843 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 4 (cursor: MzAw)...
2025-11-10 14:13:40,521 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 4
2025-11-10 14:13:40,522 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 5 (cursor: NDAw)...
2025-11-10 14:13:41,213 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 5
2025-11-10 14:13:41,214 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 6 (cursor: NTAw)...
2025-11-10 14:13:41,674 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 6
2025-11-10 14:13:41,675 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 7 (cursor: NjAw)...
2025-11-10 14:13:42,134 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 7
2025-11-10 14:13:42,135 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 8 (cursor: NzAw)...
2025-11-10 14:13:42,602 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 8
2025-11-10 14:13:42,603 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 9 (cursor: ODAw)...
2025-11-10 14:13:43,258 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 9
2025-11-10 14:13:43,259 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 10 (cursor: OTAw)...
2025-11-10 14:13:43,896 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 10
2025-11-10 14:13:43,897 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 11 (cursor: MTAwMA==)...
2025-11-10 14:13:44,545 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 11
2025-11-10 14:13:44,546 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 12 (cursor: MTEwMA==)...
2025-11-10 14:13:44,994 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 12
2025-11-10 14:13:44,994 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 13 (cursor: MTIwMA==)...
2025-11-10 14:13:45,646 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 13
2025-11-10 14:13:45,648 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 14 (cursor: MTMwMA==)...
2025-11-10 14:13:46,312 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 14
2025-11-10 14:13:46,312 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 15 (cursor: MTQwMA==)...
2025-11-10 14:13:46,966 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 15
2025-11-10 14:13:46,966 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 16 (cursor: MTUwMA==)...
2025-11-10 14:13:47,640 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 16
2025-11-10 14:13:47,641 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 17 (cursor: MTYwMA==)...
2025-11-10 14:13:48,342 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 17
2025-11-10 14:13:48,343 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 18 (cursor: MTcwMA==)...
2025-11-10 14:13:49,017 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 18
2025-11-10 14:13:49,018 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 19 (cursor: MTgwMA==)...
2025-11-10 14:13:49,688 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 19
2025-11-10 14:13:49,689 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 20 (cursor: MTkwMA==)...
2025-11-10 14:13:50,368 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 20
2025-11-10 14:13:50,369 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 21 (cursor: MjAwMA==)...
2025-11-10 14:13:50,829 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 21
2025-11-10 14:13:50,829 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 22 (cursor: MjEwMA==)...
2025-11-10 14:13:51,523 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 22
2025-11-10 14:13:51,524 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 23 (cursor: MjIwMA==)...
2025-11-10 14:13:51,975 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 23
2025-11-10 14:13:51,975 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 24 (cursor: MjMwMA==)...
2025-11-10 14:13:52,631 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 24
2025-11-10 14:13:52,632 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 25 (cursor: MjQwMA==)...
2025-11-10 14:13:55,010 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 25
2025-11-10 14:13:55,011 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 26 (cursor: MjUwMA==)...
2025-11-10 14:13:55,768 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 26
2025-11-10 14:13:55,768 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 27 (cursor: MjYwMA==)...
2025-11-10 14:13:56,446 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 27
2025-11-10 14:13:56,451 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 28 (cursor: MjcwMA==)...
2025-11-10 14:13:57,027 - playwright_rewards_scraper - INFO - âœ… Got 14 markets on page 28
2025-11-10 14:13:57,027 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 29 (cursor: LTE=)...
2025-11-10 14:13:57,281 - playwright_rewards_scraper - INFO - âœ… No more markets on page 29
2025-11-10 14:13:57,282 - playwright_rewards_scraper - INFO - âœ… Fetched 2713 total unique markets from /rewards API
2025-11-10 14:13:57,329 - market_scanner_v2 - INFO - âœ… Got 2713 markets from /rewards page
2025-11-10 14:13:57,329 - market_scanner_v2 - INFO - âœ… ACCEPTED: Hang Seng (HSI) Up or Down on November 10?
2025-11-10 14:13:57,330 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:13:57,330 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$82)
2025-11-10 14:13:57,330 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:13:57,330 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-10 14:13:57,330 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:13:57,330 - market_scanner_v2 - INFO - âœ… ACCEPTED: DAX (DAX) Up or Down on November 10?
2025-11-10 14:13:57,330 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:13:57,330 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$7463)
2025-11-10 14:13:57,330 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:13:57,330 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.75
2025-11-10 14:13:57,330 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:13:57,330 - market_scanner_v2 - INFO - âœ… ACCEPTED: FTSE 100 (UKX) Up or Down on November 10?
2025-11-10 14:13:57,330 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:13:57,330 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$7424)
2025-11-10 14:13:57,330 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:13:57,330 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.74
2025-11-10 14:13:57,330 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:13:57,330 - market_scanner_v2 - INFO - âœ… ACCEPTED: Dow Jones (DJI) Up or Down on November 10?
2025-11-10 14:13:57,330 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:13:57,330 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$245)
2025-11-10 14:13:57,330 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:13:57,330 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.02
2025-11-10 14:13:57,330 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:13:57,330 - market_scanner_v2 - INFO - âœ… ACCEPTED: Nasdaq 100 (NDX) Up or Down on November 10?
2025-11-10 14:13:57,330 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:13:57,331 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$260)
2025-11-10 14:13:57,331 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:13:57,331 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.03
2025-11-10 14:13:57,331 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:13:57,331 - market_scanner_v2 - INFO - âœ… ACCEPTED: Nikkei 225 (NIK) Up or Down on November 10?
2025-11-10 14:13:57,331 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:13:57,331 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$76)
2025-11-10 14:13:57,331 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:13:57,331 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-10 14:13:57,331 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:13:57,331 - market_scanner_v2 - INFO - âœ… ACCEPTED: S&P 500 (SPX) Up or Down on November 10?
2025-11-10 14:13:57,331 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:13:57,331 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$79)
2025-11-10 14:13:57,331 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:13:57,331 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-10 14:13:57,331 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:13:57,331 - market_scanner_v2 - INFO - âœ… ACCEPTED: Airbnb (ABNB) Up or Down on November 10?
2025-11-10 14:13:57,331 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:13:57,331 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$31)
2025-11-10 14:13:57,331 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:13:57,331 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.00
2025-11-10 14:13:57,331 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:13:57,331 - market_scanner_v2 - INFO - âœ… ACCEPTED: Opendoor (OPEN) Up or Down on November 10?
2025-11-10 14:13:57,331 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:13:57,331 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$7420)
2025-11-10 14:13:57,331 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:13:57,331 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.74
2025-11-10 14:13:57,332 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:13:57,332 - market_scanner_v2 - INFO - âœ… ACCEPTED: Palantir (PLTR) Up or Down on November 10?
2025-11-10 14:13:57,332 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:13:57,332 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$6)
2025-11-10 14:13:57,332 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:13:57,332 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.00
2025-11-10 14:13:57,332 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:13:57,332 - market_scanner_v2 - INFO - âœ… ACCEPTED: Netflix (NFLX) Up or Down on November 10?
2025-11-10 14:13:57,332 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:13:57,332 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$50)
2025-11-10 14:13:57,332 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:13:57,332 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-10 14:13:57,332 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:13:57,332 - market_scanner_v2 - INFO - âœ… ACCEPTED: NVIDIA (NVDA) Up or Down on November 10?
2025-11-10 14:13:57,332 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:13:57,332 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$382)
2025-11-10 14:13:57,332 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:13:57,332 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.04
2025-11-10 14:13:57,332 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:13:57,332 - market_scanner_v2 - INFO - âœ… ACCEPTED: Meta (META) Up or Down on November 10?
2025-11-10 14:13:57,332 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:13:57,332 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$1)
2025-11-10 14:13:57,332 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:13:57,332 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.00
2025-11-10 14:13:57,332 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:13:57,332 - market_scanner_v2 - INFO - âœ… ACCEPTED: Google (GOOGL) Up or Down on November 10?
2025-11-10 14:13:57,332 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:13:57,332 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$27)
2025-11-10 14:13:57,332 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:13:57,333 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.00
2025-11-10 14:13:57,333 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:13:57,333 - market_scanner_v2 - INFO - âœ… ACCEPTED: Amazon (AMZN) Up or Down on November 10?
2025-11-10 14:13:57,333 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:13:57,333 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$135)
2025-11-10 14:13:57,333 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:13:57,333 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-10 14:13:57,333 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:13:57,333 - market_scanner_v2 - INFO - âœ… ACCEPTED: Microsoft (MSFT) Up or Down on November 10?
2025-11-10 14:13:57,333 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:13:57,333 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$489)
2025-11-10 14:13:57,333 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:13:57,333 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.05
2025-11-10 14:13:57,333 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:13:57,333 - market_scanner_v2 - INFO - âœ… ACCEPTED: Apple (AAPL) Up or Down on November 10?
2025-11-10 14:13:57,333 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:13:57,333 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$119)
2025-11-10 14:13:57,333 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:13:57,333 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-10 14:13:57,333 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:13:57,338 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 17/2713 markets passed
2025-11-10 14:13:57,338 - market_scanner_v2 - INFO -    - 2568 rejected: reward < $20
2025-11-10 14:13:57,338 - market_scanner_v2 - INFO -    - 82 rejected: competition > 3
2025-11-10 14:13:57,338 - market_scanner_v2 - INFO -    - 22 rejected: categorical event outcomes (event_slug != market_slug)
2025-11-10 14:13:57,338 - market_scanner_v2 - INFO -    - 24 rejected: volume = 0 (no liquidity)
2025-11-10 14:13:57,339 - market_scanner_v2 - INFO - ðŸ” Verifying orderbook for top 17 markets...
2025-11-10 14:14:01,458 - market_scanner_v2 - INFO -    Progress: 10/17 markets verified...
2025-11-10 14:14:05,096 - market_scanner_v2 - INFO -    - 17 markets rejected: no orderbook (no bids or asks)
2025-11-10 14:14:05,096 - market_scanner_v2 - INFO - âœ… Found 0 qualifying markets (from 2713 total)
2025-11-10 14:14:05,099 - market_selector - INFO - Selected 0 markets from 0 candidates
2025-11-10 14:15:10,624 - market_scanner_v2 - INFO - ðŸŒ Scraping markets from /rewards page using Playwright...
2025-11-10 14:15:10,626 - playwright_rewards_scraper - INFO - ðŸŒ Fetching markets from /rewards API...
2025-11-10 14:15:10,627 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 1 (cursor: MA==)...
2025-11-10 14:15:11,089 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 1
2025-11-10 14:15:11,090 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 2 (cursor: MTAw)...
2025-11-10 14:15:11,719 - ml_predictor - INFO - Alert sent: ðŸš¨ <b>MONITORING ALERT</b>

ðŸ”´ KhÃ´ng quÃ©t markets trong 65s!
2025-11-10 14:15:11,719 - monitoring_system - INFO - Alert sent: no_scan
2025-11-10 14:15:11,719 - __main__ - WARNING - âš ï¸ Health check failed: 2 issues
2025-11-10 14:15:11,719 - __main__ - WARNING -    - ðŸ”´ KhÃ´ng quÃ©t markets trong 65s!
2025-11-10 14:15:11,720 - __main__ - WARNING -    - âš ï¸ API cháº­m: 28.5s trung bÃ¬nh
2025-11-10 14:15:11,740 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 2
2025-11-10 14:15:11,741 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 3 (cursor: MjAw)...
2025-11-10 14:15:12,431 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 3
2025-11-10 14:15:12,432 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 4 (cursor: MzAw)...
2025-11-10 14:15:13,097 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 4
2025-11-10 14:15:13,098 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 5 (cursor: NDAw)...
2025-11-10 14:15:13,536 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 5
2025-11-10 14:15:13,536 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 6 (cursor: NTAw)...
2025-11-10 14:15:14,198 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 6
2025-11-10 14:15:14,198 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 7 (cursor: NjAw)...
2025-11-10 14:15:14,891 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 7
2025-11-10 14:15:14,892 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 8 (cursor: NzAw)...
2025-11-10 14:15:15,584 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 8
2025-11-10 14:15:15,584 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 9 (cursor: ODAw)...
2025-11-10 14:15:16,242 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 9
2025-11-10 14:15:16,242 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 10 (cursor: OTAw)...
2025-11-10 14:15:16,953 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 10
2025-11-10 14:15:16,954 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 11 (cursor: MTAwMA==)...
2025-11-10 14:15:17,656 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 11
2025-11-10 14:15:17,657 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 12 (cursor: MTEwMA==)...
2025-11-10 14:15:18,323 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 12
2025-11-10 14:15:18,324 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 13 (cursor: MTIwMA==)...
2025-11-10 14:15:19,010 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 13
2025-11-10 14:15:19,011 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 14 (cursor: MTMwMA==)...
2025-11-10 14:15:19,732 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 14
2025-11-10 14:15:19,733 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 15 (cursor: MTQwMA==)...
2025-11-10 14:15:20,400 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 15
2025-11-10 14:15:20,402 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 16 (cursor: MTUwMA==)...
2025-11-10 14:15:21,264 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 16
2025-11-10 14:15:21,265 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 17 (cursor: MTYwMA==)...
2025-11-10 14:15:21,931 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 17
2025-11-10 14:15:21,932 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 18 (cursor: MTcwMA==)...
2025-11-10 14:15:22,445 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 18
2025-11-10 14:15:22,445 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 19 (cursor: MTgwMA==)...
2025-11-10 14:15:23,117 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 19
2025-11-10 14:15:23,117 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 20 (cursor: MTkwMA==)...
2025-11-10 14:15:23,782 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 20
2025-11-10 14:15:23,782 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 21 (cursor: MjAwMA==)...
2025-11-10 14:15:24,490 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 21
2025-11-10 14:15:24,490 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 22 (cursor: MjEwMA==)...
2025-11-10 14:15:24,954 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 22
2025-11-10 14:15:24,955 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 23 (cursor: MjIwMA==)...
2025-11-10 14:15:25,660 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 23
2025-11-10 14:15:25,661 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 24 (cursor: MjMwMA==)...
2025-11-10 14:15:26,317 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 24
2025-11-10 14:15:26,318 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 25 (cursor: MjQwMA==)...
2025-11-10 14:15:26,994 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 25
2025-11-10 14:15:26,994 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 26 (cursor: MjUwMA==)...
2025-11-10 14:15:27,666 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 26
2025-11-10 14:15:27,667 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 27 (cursor: MjYwMA==)...
2025-11-10 14:15:28,333 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 27
2025-11-10 14:15:28,333 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 28 (cursor: MjcwMA==)...
2025-11-10 14:15:28,781 - playwright_rewards_scraper - INFO - âœ… Got 14 markets on page 28
2025-11-10 14:15:28,781 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 29 (cursor: LTE=)...
2025-11-10 14:15:29,236 - playwright_rewards_scraper - INFO - âœ… No more markets on page 29
2025-11-10 14:15:29,237 - playwright_rewards_scraper - INFO - âœ… Fetched 2713 total unique markets from /rewards API
2025-11-10 14:15:29,283 - market_scanner_v2 - INFO - âœ… Got 2713 markets from /rewards page
2025-11-10 14:15:29,283 - market_scanner_v2 - INFO - âœ… ACCEPTED: Hang Seng (HSI) Up or Down on November 10?
2025-11-10 14:15:29,283 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:15:29,283 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$82)
2025-11-10 14:15:29,283 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:15:29,283 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-10 14:15:29,283 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:15:29,283 - market_scanner_v2 - INFO - âœ… ACCEPTED: DAX (DAX) Up or Down on November 10?
2025-11-10 14:15:29,283 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:15:29,283 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$7463)
2025-11-10 14:15:29,283 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:15:29,283 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.75
2025-11-10 14:15:29,283 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:15:29,283 - market_scanner_v2 - INFO - âœ… ACCEPTED: FTSE 100 (UKX) Up or Down on November 10?
2025-11-10 14:15:29,283 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:15:29,283 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$7424)
2025-11-10 14:15:29,284 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:15:29,284 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.74
2025-11-10 14:15:29,284 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:15:29,284 - market_scanner_v2 - INFO - âœ… ACCEPTED: Dow Jones (DJI) Up or Down on November 10?
2025-11-10 14:15:29,284 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:15:29,284 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$245)
2025-11-10 14:15:29,284 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:15:29,284 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.02
2025-11-10 14:15:29,284 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:15:29,284 - market_scanner_v2 - INFO - âœ… ACCEPTED: Nasdaq 100 (NDX) Up or Down on November 10?
2025-11-10 14:15:29,284 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:15:29,284 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$260)
2025-11-10 14:15:29,284 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:15:29,284 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.03
2025-11-10 14:15:29,284 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:15:29,284 - market_scanner_v2 - INFO - âœ… ACCEPTED: Nikkei 225 (NIK) Up or Down on November 10?
2025-11-10 14:15:29,284 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:15:29,284 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$76)
2025-11-10 14:15:29,284 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:15:29,284 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-10 14:15:29,284 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:15:29,284 - market_scanner_v2 - INFO - âœ… ACCEPTED: S&P 500 (SPX) Up or Down on November 10?
2025-11-10 14:15:29,284 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:15:29,284 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$79)
2025-11-10 14:15:29,284 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:15:29,284 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-10 14:15:29,284 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:15:29,284 - market_scanner_v2 - INFO - âœ… ACCEPTED: Airbnb (ABNB) Up or Down on November 10?
2025-11-10 14:15:29,285 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:15:29,285 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$31)
2025-11-10 14:15:29,285 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:15:29,285 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.00
2025-11-10 14:15:29,285 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:15:29,285 - market_scanner_v2 - INFO - âœ… ACCEPTED: Opendoor (OPEN) Up or Down on November 10?
2025-11-10 14:15:29,285 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:15:29,285 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$7420)
2025-11-10 14:15:29,285 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:15:29,285 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.74
2025-11-10 14:15:29,285 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:15:29,285 - market_scanner_v2 - INFO - âœ… ACCEPTED: Palantir (PLTR) Up or Down on November 10?
2025-11-10 14:15:29,285 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:15:29,285 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$6)
2025-11-10 14:15:29,285 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:15:29,285 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.00
2025-11-10 14:15:29,285 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:15:29,285 - market_scanner_v2 - INFO - âœ… ACCEPTED: Netflix (NFLX) Up or Down on November 10?
2025-11-10 14:15:29,285 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:15:29,285 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$50)
2025-11-10 14:15:29,285 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:15:29,285 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-10 14:15:29,285 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:15:29,285 - market_scanner_v2 - INFO - âœ… ACCEPTED: NVIDIA (NVDA) Up or Down on November 10?
2025-11-10 14:15:29,285 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:15:29,285 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$382)
2025-11-10 14:15:29,285 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:15:29,286 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.04
2025-11-10 14:15:29,286 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:15:29,286 - market_scanner_v2 - INFO - âœ… ACCEPTED: Meta (META) Up or Down on November 10?
2025-11-10 14:15:29,286 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:15:29,286 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$1)
2025-11-10 14:15:29,286 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:15:29,286 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.00
2025-11-10 14:15:29,286 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:15:29,286 - market_scanner_v2 - INFO - âœ… ACCEPTED: Google (GOOGL) Up or Down on November 10?
2025-11-10 14:15:29,286 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:15:29,286 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$27)
2025-11-10 14:15:29,286 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:15:29,286 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.00
2025-11-10 14:15:29,286 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:15:29,286 - market_scanner_v2 - INFO - âœ… ACCEPTED: Amazon (AMZN) Up or Down on November 10?
2025-11-10 14:15:29,286 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:15:29,286 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$135)
2025-11-10 14:15:29,286 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:15:29,286 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-10 14:15:29,286 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:15:29,286 - market_scanner_v2 - INFO - âœ… ACCEPTED: Microsoft (MSFT) Up or Down on November 10?
2025-11-10 14:15:29,286 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:15:29,286 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$489)
2025-11-10 14:15:29,286 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:15:29,286 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.05
2025-11-10 14:15:29,286 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:15:29,287 - market_scanner_v2 - INFO - âœ… ACCEPTED: Apple (AAPL) Up or Down on November 10?
2025-11-10 14:15:29,287 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:15:29,287 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$119)
2025-11-10 14:15:29,287 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:15:29,287 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-10 14:15:29,287 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:15:29,292 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 17/2713 markets passed
2025-11-10 14:15:29,292 - market_scanner_v2 - INFO -    - 2568 rejected: reward < $20
2025-11-10 14:15:29,292 - market_scanner_v2 - INFO -    - 85 rejected: competition > 3
2025-11-10 14:15:29,292 - market_scanner_v2 - INFO -    - 19 rejected: categorical event outcomes (event_slug != market_slug)
2025-11-10 14:15:29,292 - market_scanner_v2 - INFO -    - 24 rejected: volume = 0 (no liquidity)
2025-11-10 14:15:29,292 - market_scanner_v2 - INFO - ðŸ” Verifying orderbook for top 17 markets...
2025-11-10 14:15:33,392 - market_scanner_v2 - INFO -    Progress: 10/17 markets verified...
2025-11-10 14:15:37,015 - market_scanner_v2 - INFO -    - 17 markets rejected: no orderbook (no bids or asks)
2025-11-10 14:15:37,015 - market_scanner_v2 - INFO - âœ… Found 0 qualifying markets (from 2713 total)
2025-11-10 14:15:37,018 - market_selector - INFO - Selected 0 markets from 0 candidates
2025-11-10 14:16:41,159 - market_scanner_v2 - INFO - ðŸŒ Scraping markets from /rewards page using Playwright...
2025-11-10 14:16:41,159 - playwright_rewards_scraper - INFO - ðŸŒ Fetching markets from /rewards API...
2025-11-10 14:16:41,159 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 1 (cursor: MA==)...
2025-11-10 14:16:41,834 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 1
2025-11-10 14:16:41,834 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 2 (cursor: MTAw)...
2025-11-10 14:16:42,556 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 2
2025-11-10 14:16:42,557 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 3 (cursor: MjAw)...
2025-11-10 14:16:43,216 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 3
2025-11-10 14:16:43,216 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 4 (cursor: MzAw)...
2025-11-10 14:16:44,729 - __main__ - WARNING - âš ï¸ Health check failed: 2 issues
2025-11-10 14:16:44,729 - __main__ - WARNING -    - ðŸ”´ KhÃ´ng quÃ©t markets trong 67s!
2025-11-10 14:16:44,729 - __main__ - WARNING -    - âš ï¸ API cháº­m: 27.4s trung bÃ¬nh
2025-11-10 14:16:44,733 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 4
2025-11-10 14:16:44,733 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 5 (cursor: NDAw)...
2025-11-10 14:16:45,404 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 5
2025-11-10 14:16:45,405 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 6 (cursor: NTAw)...
2025-11-10 14:16:45,880 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 6
2025-11-10 14:16:45,880 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 7 (cursor: NjAw)...
2025-11-10 14:16:46,534 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 7
2025-11-10 14:16:46,535 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 8 (cursor: NzAw)...
2025-11-10 14:16:47,182 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 8
2025-11-10 14:16:47,183 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 9 (cursor: ODAw)...
2025-11-10 14:16:47,854 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 9
2025-11-10 14:16:47,855 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 10 (cursor: OTAw)...
2025-11-10 14:16:48,692 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 10
2025-11-10 14:16:48,693 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 11 (cursor: MTAwMA==)...
2025-11-10 14:16:49,139 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 11
2025-11-10 14:16:49,139 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 12 (cursor: MTEwMA==)...
2025-11-10 14:16:49,599 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 12
2025-11-10 14:16:49,600 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 13 (cursor: MTIwMA==)...
2025-11-10 14:16:50,299 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 13
2025-11-10 14:16:50,300 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 14 (cursor: MTMwMA==)...
2025-11-10 14:16:50,975 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 14
2025-11-10 14:16:50,976 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 15 (cursor: MTQwMA==)...
2025-11-10 14:16:51,643 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 15
2025-11-10 14:16:51,644 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 16 (cursor: MTUwMA==)...
2025-11-10 14:16:52,306 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 16
2025-11-10 14:16:52,307 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 17 (cursor: MTYwMA==)...
2025-11-10 14:16:52,976 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 17
2025-11-10 14:16:52,976 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 18 (cursor: MTcwMA==)...
2025-11-10 14:16:53,635 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 18
2025-11-10 14:16:53,636 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 19 (cursor: MTgwMA==)...
2025-11-10 14:16:54,320 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 19
2025-11-10 14:16:54,320 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 20 (cursor: MTkwMA==)...
2025-11-10 14:16:55,068 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 20
2025-11-10 14:16:55,068 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 21 (cursor: MjAwMA==)...
2025-11-10 14:16:55,748 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 21
2025-11-10 14:16:55,748 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 22 (cursor: MjEwMA==)...
2025-11-10 14:16:56,429 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 22
2025-11-10 14:16:56,430 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 23 (cursor: MjIwMA==)...
2025-11-10 14:16:56,912 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 23
2025-11-10 14:16:56,913 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 24 (cursor: MjMwMA==)...
2025-11-10 14:16:57,583 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 24
2025-11-10 14:16:57,584 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 25 (cursor: MjQwMA==)...
2025-11-10 14:16:58,239 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 25
2025-11-10 14:16:58,239 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 26 (cursor: MjUwMA==)...
2025-11-10 14:16:59,109 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 26
2025-11-10 14:16:59,110 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 27 (cursor: MjYwMA==)...
2025-11-10 14:16:59,766 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 27
2025-11-10 14:16:59,767 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 28 (cursor: MjcwMA==)...
2025-11-10 14:17:00,225 - playwright_rewards_scraper - INFO - âœ… Got 14 markets on page 28
2025-11-10 14:17:00,225 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 29 (cursor: LTE=)...
2025-11-10 14:17:00,493 - playwright_rewards_scraper - INFO - âœ… No more markets on page 29
2025-11-10 14:17:00,493 - playwright_rewards_scraper - INFO - âœ… Fetched 2713 total unique markets from /rewards API
2025-11-10 14:17:00,539 - market_scanner_v2 - INFO - âœ… Got 2713 markets from /rewards page
2025-11-10 14:17:00,539 - market_scanner_v2 - INFO - âœ… ACCEPTED: Hang Seng (HSI) Up or Down on November 10?
2025-11-10 14:17:00,539 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:17:00,539 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$82)
2025-11-10 14:17:00,539 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:17:00,539 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-10 14:17:00,539 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:17:00,539 - market_scanner_v2 - INFO - âœ… ACCEPTED: DAX (DAX) Up or Down on November 10?
2025-11-10 14:17:00,539 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:17:00,539 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$7463)
2025-11-10 14:17:00,539 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:17:00,539 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.75
2025-11-10 14:17:00,540 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:17:00,540 - market_scanner_v2 - INFO - âœ… ACCEPTED: FTSE 100 (UKX) Up or Down on November 10?
2025-11-10 14:17:00,540 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:17:00,540 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$7424)
2025-11-10 14:17:00,540 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:17:00,540 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.74
2025-11-10 14:17:00,540 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:17:00,540 - market_scanner_v2 - INFO - âœ… ACCEPTED: Dow Jones (DJI) Up or Down on November 10?
2025-11-10 14:17:00,540 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:17:00,540 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$245)
2025-11-10 14:17:00,540 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:17:00,540 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.02
2025-11-10 14:17:00,540 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:17:00,540 - market_scanner_v2 - INFO - âœ… ACCEPTED: Nasdaq 100 (NDX) Up or Down on November 10?
2025-11-10 14:17:00,540 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:17:00,540 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$260)
2025-11-10 14:17:00,540 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:17:00,540 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.03
2025-11-10 14:17:00,540 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:17:00,540 - market_scanner_v2 - INFO - âœ… ACCEPTED: Nikkei 225 (NIK) Up or Down on November 10?
2025-11-10 14:17:00,540 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:17:00,540 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$76)
2025-11-10 14:17:00,540 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:17:00,540 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-10 14:17:00,540 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:17:00,540 - market_scanner_v2 - INFO - âœ… ACCEPTED: S&P 500 (SPX) Up or Down on November 10?
2025-11-10 14:17:00,540 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:17:00,541 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$79)
2025-11-10 14:17:00,541 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:17:00,541 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-10 14:17:00,541 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:17:00,541 - market_scanner_v2 - INFO - âœ… ACCEPTED: Airbnb (ABNB) Up or Down on November 10?
2025-11-10 14:17:00,541 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:17:00,541 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$31)
2025-11-10 14:17:00,541 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:17:00,541 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.00
2025-11-10 14:17:00,541 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:17:00,541 - market_scanner_v2 - INFO - âœ… ACCEPTED: Opendoor (OPEN) Up or Down on November 10?
2025-11-10 14:17:00,541 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:17:00,541 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$7420)
2025-11-10 14:17:00,541 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:17:00,541 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.74
2025-11-10 14:17:00,541 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:17:00,541 - market_scanner_v2 - INFO - âœ… ACCEPTED: Palantir (PLTR) Up or Down on November 10?
2025-11-10 14:17:00,541 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:17:00,541 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$6)
2025-11-10 14:17:00,541 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:17:00,541 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.00
2025-11-10 14:17:00,541 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:17:00,541 - market_scanner_v2 - INFO - âœ… ACCEPTED: Netflix (NFLX) Up or Down on November 10?
2025-11-10 14:17:00,541 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:17:00,541 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$50)
2025-11-10 14:17:00,541 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:17:00,541 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-10 14:17:00,541 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:17:00,542 - market_scanner_v2 - INFO - âœ… ACCEPTED: NVIDIA (NVDA) Up or Down on November 10?
2025-11-10 14:17:00,542 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:17:00,542 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$382)
2025-11-10 14:17:00,542 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:17:00,542 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.04
2025-11-10 14:17:00,542 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:17:00,542 - market_scanner_v2 - INFO - âœ… ACCEPTED: Meta (META) Up or Down on November 10?
2025-11-10 14:17:00,542 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:17:00,542 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$1)
2025-11-10 14:17:00,542 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:17:00,542 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.00
2025-11-10 14:17:00,542 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:17:00,542 - market_scanner_v2 - INFO - âœ… ACCEPTED: Google (GOOGL) Up or Down on November 10?
2025-11-10 14:17:00,542 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:17:00,542 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$27)
2025-11-10 14:17:00,542 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:17:00,542 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.00
2025-11-10 14:17:00,542 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:17:00,542 - market_scanner_v2 - INFO - âœ… ACCEPTED: Amazon (AMZN) Up or Down on November 10?
2025-11-10 14:17:00,542 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:17:00,542 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$135)
2025-11-10 14:17:00,542 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:17:00,542 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-10 14:17:00,542 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:17:00,542 - market_scanner_v2 - INFO - âœ… ACCEPTED: Microsoft (MSFT) Up or Down on November 10?
2025-11-10 14:17:00,542 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:17:00,542 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$489)
2025-11-10 14:17:00,543 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:17:00,543 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.05
2025-11-10 14:17:00,543 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:17:00,543 - market_scanner_v2 - INFO - âœ… ACCEPTED: Apple (AAPL) Up or Down on November 10?
2025-11-10 14:17:00,543 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:17:00,543 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$119)
2025-11-10 14:17:00,543 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:17:00,543 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-10 14:17:00,543 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:17:00,547 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 17/2713 markets passed
2025-11-10 14:17:00,548 - market_scanner_v2 - INFO -    - 2568 rejected: reward < $20
2025-11-10 14:17:00,548 - market_scanner_v2 - INFO -    - 85 rejected: competition > 3
2025-11-10 14:17:00,548 - market_scanner_v2 - INFO -    - 19 rejected: categorical event outcomes (event_slug != market_slug)
2025-11-10 14:17:00,548 - market_scanner_v2 - INFO -    - 24 rejected: volume = 0 (no liquidity)
2025-11-10 14:17:00,548 - market_scanner_v2 - INFO - ðŸ” Verifying orderbook for top 17 markets...
2025-11-10 14:17:04,654 - market_scanner_v2 - INFO -    Progress: 10/17 markets verified...
2025-11-10 14:17:08,324 - market_scanner_v2 - INFO -    - 17 markets rejected: no orderbook (no bids or asks)
2025-11-10 14:17:08,324 - market_scanner_v2 - INFO - âœ… Found 0 qualifying markets (from 2713 total)
2025-11-10 14:17:08,327 - market_selector - INFO - Selected 0 markets from 0 candidates
2025-11-10 14:18:00,889 - market_scanner_v2 - INFO - ðŸŒ Scraping markets from /rewards page using Playwright...
2025-11-10 14:18:00,889 - playwright_rewards_scraper - INFO - ðŸŒ Fetching markets from /rewards API...
2025-11-10 14:18:00,889 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 1 (cursor: MA==)...
2025-11-10 14:18:01,557 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 1
2025-11-10 14:18:01,557 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 2 (cursor: MTAw)...
2025-11-10 14:18:02,239 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 2
2025-11-10 14:18:02,240 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 3 (cursor: MjAw)...
2025-11-10 14:18:02,907 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 3
2025-11-10 14:18:02,907 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 4 (cursor: MzAw)...
2025-11-10 14:18:03,637 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 4
2025-11-10 14:18:03,637 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 5 (cursor: NDAw)...
2025-11-10 14:18:04,284 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 5
2025-11-10 14:18:04,285 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 6 (cursor: NTAw)...
2025-11-10 14:18:04,936 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 6
2025-11-10 14:18:04,936 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 7 (cursor: NjAw)...
2025-11-10 14:18:05,803 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 7
2025-11-10 14:18:05,803 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 8 (cursor: NzAw)...
2025-11-10 14:18:06,458 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 8
2025-11-10 14:18:06,459 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 9 (cursor: ODAw)...
2025-11-10 14:18:07,257 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 9
2025-11-10 14:18:07,258 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 10 (cursor: OTAw)...
2025-11-10 14:18:07,979 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 10
2025-11-10 14:18:07,980 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 11 (cursor: MTAwMA==)...
2025-11-10 14:18:08,638 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 11
2025-11-10 14:18:08,639 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 12 (cursor: MTEwMA==)...
2025-11-10 14:18:09,348 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 12
2025-11-10 14:18:09,349 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 13 (cursor: MTIwMA==)...
2025-11-10 14:18:10,029 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 13
2025-11-10 14:18:10,030 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 14 (cursor: MTMwMA==)...
2025-11-10 14:18:10,709 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 14
2025-11-10 14:18:10,710 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 15 (cursor: MTQwMA==)...
2025-11-10 14:18:11,351 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 15
2025-11-10 14:18:11,352 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 16 (cursor: MTUwMA==)...
2025-11-10 14:18:12,026 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 16
2025-11-10 14:18:12,027 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 17 (cursor: MTYwMA==)...
2025-11-10 14:18:12,687 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 17
2025-11-10 14:18:12,688 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 18 (cursor: MTcwMA==)...
2025-11-10 14:18:13,144 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 18
2025-11-10 14:18:13,145 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 19 (cursor: MTgwMA==)...
2025-11-10 14:18:13,812 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 19
2025-11-10 14:18:13,813 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 20 (cursor: MTkwMA==)...
2025-11-10 14:18:14,492 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 20
2025-11-10 14:18:14,493 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 21 (cursor: MjAwMA==)...
2025-11-10 14:18:15,176 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 21
2025-11-10 14:18:15,176 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 22 (cursor: MjEwMA==)...
2025-11-10 14:18:15,829 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 22
2025-11-10 14:18:15,829 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 23 (cursor: MjIwMA==)...
2025-11-10 14:18:16,522 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 23
2025-11-10 14:18:16,523 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 24 (cursor: MjMwMA==)...
2025-11-10 14:18:17,740 - __main__ - WARNING - âš ï¸ Health check failed: 2 issues
2025-11-10 14:18:17,741 - __main__ - WARNING -    - ðŸ”´ KhÃ´ng quÃ©t markets trong 68s!
2025-11-10 14:18:17,741 - __main__ - WARNING -    - âš ï¸ API cháº­m: 27.4s trung bÃ¬nh
2025-11-10 14:18:17,744 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 24
2025-11-10 14:18:17,744 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 25 (cursor: MjQwMA==)...
2025-11-10 14:18:18,434 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 25
2025-11-10 14:18:18,435 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 26 (cursor: MjUwMA==)...
2025-11-10 14:18:19,107 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 26
2025-11-10 14:18:19,108 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 27 (cursor: MjYwMA==)...
2025-11-10 14:18:19,773 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 27
2025-11-10 14:18:19,774 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 28 (cursor: MjcwMA==)...
2025-11-10 14:18:20,228 - playwright_rewards_scraper - INFO - âœ… Got 14 markets on page 28
2025-11-10 14:18:20,228 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 29 (cursor: LTE=)...
2025-11-10 14:18:20,673 - playwright_rewards_scraper - INFO - âœ… No more markets on page 29
2025-11-10 14:18:20,674 - playwright_rewards_scraper - INFO - âœ… Fetched 2713 total unique markets from /rewards API
2025-11-10 14:18:20,721 - market_scanner_v2 - INFO - âœ… Got 2713 markets from /rewards page
2025-11-10 14:18:20,722 - market_scanner_v2 - INFO - âœ… ACCEPTED: Hang Seng (HSI) Up or Down on November 10?
2025-11-10 14:18:20,722 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:18:20,722 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$82)
2025-11-10 14:18:20,722 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:18:20,722 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-10 14:18:20,722 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:18:20,722 - market_scanner_v2 - INFO - âœ… ACCEPTED: DAX (DAX) Up or Down on November 10?
2025-11-10 14:18:20,722 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:18:20,722 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$7463)
2025-11-10 14:18:20,722 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:18:20,722 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.75
2025-11-10 14:18:20,722 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:18:20,722 - market_scanner_v2 - INFO - âœ… ACCEPTED: FTSE 100 (UKX) Up or Down on November 10?
2025-11-10 14:18:20,722 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:18:20,722 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$7424)
2025-11-10 14:18:20,722 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:18:20,722 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.74
2025-11-10 14:18:20,722 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:18:20,722 - market_scanner_v2 - INFO - âœ… ACCEPTED: Dow Jones (DJI) Up or Down on November 10?
2025-11-10 14:18:20,722 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:18:20,723 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$245)
2025-11-10 14:18:20,723 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:18:20,723 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.02
2025-11-10 14:18:20,723 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:18:20,723 - market_scanner_v2 - INFO - âœ… ACCEPTED: Nasdaq 100 (NDX) Up or Down on November 10?
2025-11-10 14:18:20,723 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:18:20,723 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$260)
2025-11-10 14:18:20,723 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:18:20,723 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.03
2025-11-10 14:18:20,723 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:18:20,723 - market_scanner_v2 - INFO - âœ… ACCEPTED: Nikkei 225 (NIK) Up or Down on November 10?
2025-11-10 14:18:20,723 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:18:20,723 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$76)
2025-11-10 14:18:20,723 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:18:20,723 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-10 14:18:20,723 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:18:20,723 - market_scanner_v2 - INFO - âœ… ACCEPTED: S&P 500 (SPX) Up or Down on November 10?
2025-11-10 14:18:20,723 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:18:20,723 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$79)
2025-11-10 14:18:20,723 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:18:20,723 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-10 14:18:20,723 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:18:20,723 - market_scanner_v2 - INFO - âœ… ACCEPTED: Airbnb (ABNB) Up or Down on November 10?
2025-11-10 14:18:20,723 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:18:20,724 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$31)
2025-11-10 14:18:20,724 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:18:20,724 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.00
2025-11-10 14:18:20,724 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:18:20,724 - market_scanner_v2 - INFO - âœ… ACCEPTED: Opendoor (OPEN) Up or Down on November 10?
2025-11-10 14:18:20,724 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:18:20,724 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$7420)
2025-11-10 14:18:20,724 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:18:20,724 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.74
2025-11-10 14:18:20,724 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:18:20,724 - market_scanner_v2 - INFO - âœ… ACCEPTED: Palantir (PLTR) Up or Down on November 10?
2025-11-10 14:18:20,724 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:18:20,724 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$6)
2025-11-10 14:18:20,724 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:18:20,724 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.00
2025-11-10 14:18:20,724 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:18:20,724 - market_scanner_v2 - INFO - âœ… ACCEPTED: Netflix (NFLX) Up or Down on November 10?
2025-11-10 14:18:20,724 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:18:20,724 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$50)
2025-11-10 14:18:20,724 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:18:20,724 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-10 14:18:20,724 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:18:20,724 - market_scanner_v2 - INFO - âœ… ACCEPTED: NVIDIA (NVDA) Up or Down on November 10?
2025-11-10 14:18:20,724 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:18:20,724 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$382)
2025-11-10 14:18:20,725 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:18:20,725 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.04
2025-11-10 14:18:20,725 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:18:20,725 - market_scanner_v2 - INFO - âœ… ACCEPTED: Tesla (TSLA) Up or Down on November 10?
2025-11-10 14:18:20,725 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:18:20,725 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$7454)
2025-11-10 14:18:20,725 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:18:20,725 - market_scanner_v2 - INFO -    - Competition: 0.55522 bars, Score: -44.78
2025-11-10 14:18:20,725 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:18:20,725 - market_scanner_v2 - INFO - âœ… ACCEPTED: Meta (META) Up or Down on November 10?
2025-11-10 14:18:20,725 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:18:20,725 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$1)
2025-11-10 14:18:20,725 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:18:20,725 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.00
2025-11-10 14:18:20,725 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:18:20,725 - market_scanner_v2 - INFO - âœ… ACCEPTED: Google (GOOGL) Up or Down on November 10?
2025-11-10 14:18:20,725 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:18:20,725 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$27)
2025-11-10 14:18:20,725 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:18:20,725 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.00
2025-11-10 14:18:20,725 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:18:20,725 - market_scanner_v2 - INFO - âœ… ACCEPTED: Amazon (AMZN) Up or Down on November 10?
2025-11-10 14:18:20,725 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:18:20,725 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$135)
2025-11-10 14:18:20,725 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:18:20,726 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-10 14:18:20,726 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:18:20,726 - market_scanner_v2 - INFO - âœ… ACCEPTED: Microsoft (MSFT) Up or Down on November 10?
2025-11-10 14:18:20,726 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:18:20,726 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$489)
2025-11-10 14:18:20,726 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:18:20,726 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.05
2025-11-10 14:18:20,726 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:18:20,726 - market_scanner_v2 - INFO - âœ… ACCEPTED: Apple (AAPL) Up or Down on November 10?
2025-11-10 14:18:20,726 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:18:20,726 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$119)
2025-11-10 14:18:20,726 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:18:20,726 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-10 14:18:20,726 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:18:20,726 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will more than 2.8 million people travel through a TSA check
2025-11-10 14:18:20,726 - market_scanner_v2 - INFO -    - Category: other
2025-11-10 14:18:20,726 - market_scanner_v2 - INFO -    - Estimated Reward: $30 (based on volume=$12141)
2025-11-10 14:18:20,726 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:18:20,726 - market_scanner_v2 - INFO -    - Competition: 2.646745 bars, Score: -248.46
2025-11-10 14:18:20,726 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:18:20,732 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 19/2713 markets passed
2025-11-10 14:18:20,732 - market_scanner_v2 - INFO -    - 2568 rejected: reward < $20
2025-11-10 14:18:20,732 - market_scanner_v2 - INFO -    - 86 rejected: competition > 3
2025-11-10 14:18:20,732 - market_scanner_v2 - INFO -    - 16 rejected: categorical event outcomes (event_slug != market_slug)
2025-11-10 14:18:20,733 - market_scanner_v2 - INFO -    - 24 rejected: volume = 0 (no liquidity)
2025-11-10 14:18:20,733 - market_scanner_v2 - INFO - ðŸ” Verifying orderbook for top 19 markets...
2025-11-10 14:18:24,892 - market_scanner_v2 - INFO -    Progress: 10/19 markets verified...
2025-11-10 14:18:29,498 - market_scanner_v2 - INFO -    - 19 markets rejected: no orderbook (no bids or asks)
2025-11-10 14:18:29,498 - market_scanner_v2 - INFO - âœ… Found 0 qualifying markets (from 2713 total)
2025-11-10 14:18:29,501 - market_selector - INFO - Selected 0 markets from 0 candidates
2025-11-10 14:18:37,994 - profit_taking_manager - INFO - ðŸ” Checking positions for wallet: 0x18F261DC...Ae4FfD96
2025-11-10 14:18:38,340 - profit_taking_manager - INFO - ðŸ“Š Found 8 active positions
2025-11-10 14:18:38,340 - profit_taking_manager - WARNING - âš ï¸  Skipping position FIDE World Cup 2025 - Shant Sa - invalid data (shares=113.0, avg=0.09, current=0.0)
2025-11-10 14:18:38,340 - profit_taking_manager - INFO - 
ðŸ“ˆ Position: Will Google Gemini 3 score at least 70% on the Fro
2025-11-10 14:18:38,340 - profit_taking_manager - INFO -    Shares: 68.00 @ $0.3900
2025-11-10 14:18:38,340 - profit_taking_manager - INFO -    Current: $0.0700
2025-11-10 14:18:38,340 - profit_taking_manager - INFO -    P&L: $-21.76 (-82.05%)
2025-11-10 14:18:38,340 - profit_taking_manager - INFO -    â¸ï¸  Losing position - NOT closing (manual decision required)
2025-11-10 14:18:38,340 - profit_taking_manager - WARNING - âš ï¸  Skipping position Syracuse vs. Miami - invalid data (shares=66.0, avg=0.49, current=0.0)
2025-11-10 14:18:38,340 - profit_taking_manager - WARNING - âš ï¸  Skipping position FIDE World Cup 2025 - Michael  - invalid data (shares=65.001889, avg=0.180036, current=0.0)
2025-11-10 14:18:38,340 - profit_taking_manager - INFO - 
ðŸ“ˆ Position: Weed rescheduled in 2025?
2025-11-10 14:18:38,340 - profit_taking_manager - INFO -    Shares: 54.43 @ $0.1100
2025-11-10 14:18:38,341 - profit_taking_manager - INFO -    Current: $0.1050
2025-11-10 14:18:38,341 - profit_taking_manager - INFO -    P&L: $-0.27 (-4.55%)
2025-11-10 14:18:38,341 - profit_taking_manager - INFO -    â¸ï¸  Losing position - NOT closing (manual decision required)
2025-11-10 14:18:38,341 - profit_taking_manager - INFO - 
ðŸ“ˆ Position: Supreme Court vacancy in 2025?
2025-11-10 14:18:38,341 - profit_taking_manager - INFO -    Shares: 44.21 @ $0.0600
2025-11-10 14:18:38,341 - profit_taking_manager - INFO -    Current: $0.0500
2025-11-10 14:18:38,341 - profit_taking_manager - INFO -    P&L: $-0.44 (-16.67%)
2025-11-10 14:18:38,341 - profit_taking_manager - INFO -    â¸ï¸  Losing position - NOT closing (manual decision required)
2025-11-10 14:18:38,341 - profit_taking_manager - INFO - 
ðŸ“ˆ Position: Dan Clancy out as Twitch CEO in 2025?
2025-11-10 14:18:38,341 - profit_taking_manager - INFO -    Shares: 30.78 @ $0.0900
2025-11-10 14:18:38,341 - profit_taking_manager - INFO -    Current: $0.0800
2025-11-10 14:18:38,341 - profit_taking_manager - INFO -    P&L: $-0.31 (-11.11%)
2025-11-10 14:18:38,341 - profit_taking_manager - INFO -    â¸ï¸  Losing position - NOT closing (manual decision required)
2025-11-10 14:18:38,341 - profit_taking_manager - WARNING - âš ï¸  Skipping position Charlotte 49ers vs. East Carol - invalid data (shares=0.017509, avg=0.14942, current=0.0)
2025-11-10 14:18:38,341 - __main__ - INFO - â³ Next profit check in 300s
2025-11-10 14:19:33,866 - market_scanner_v2 - INFO - ðŸŒ Scraping markets from /rewards page using Playwright...
2025-11-10 14:19:33,867 - playwright_rewards_scraper - INFO - ðŸŒ Fetching markets from /rewards API...
2025-11-10 14:19:33,867 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 1 (cursor: MA==)...
2025-11-10 14:19:34,544 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 1
2025-11-10 14:19:34,545 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 2 (cursor: MTAw)...
2025-11-10 14:19:35,228 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 2
2025-11-10 14:19:35,229 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 3 (cursor: MjAw)...
2025-11-10 14:19:35,884 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 3
2025-11-10 14:19:35,885 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 4 (cursor: MzAw)...
2025-11-10 14:19:36,605 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 4
2025-11-10 14:19:36,606 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 5 (cursor: NDAw)...
2025-11-10 14:19:37,247 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 5
2025-11-10 14:19:37,248 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 6 (cursor: NTAw)...
2025-11-10 14:19:37,912 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 6
2025-11-10 14:19:37,913 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 7 (cursor: NjAw)...
2025-11-10 14:19:38,552 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 7
2025-11-10 14:19:38,553 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 8 (cursor: NzAw)...
2025-11-10 14:19:39,189 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 8
2025-11-10 14:19:39,190 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 9 (cursor: ODAw)...
2025-11-10 14:19:40,060 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 9
2025-11-10 14:19:40,061 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 10 (cursor: OTAw)...
2025-11-10 14:19:40,700 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 10
2025-11-10 14:19:40,701 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 11 (cursor: MTAwMA==)...
2025-11-10 14:19:41,326 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 11
2025-11-10 14:19:41,326 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 12 (cursor: MTEwMA==)...
2025-11-10 14:19:41,768 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 12
2025-11-10 14:19:41,769 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 13 (cursor: MTIwMA==)...
2025-11-10 14:19:42,412 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 13
2025-11-10 14:19:42,413 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 14 (cursor: MTMwMA==)...
2025-11-10 14:19:43,088 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 14
2025-11-10 14:19:43,088 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 15 (cursor: MTQwMA==)...
2025-11-10 14:19:43,765 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 15
2025-11-10 14:19:43,766 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 16 (cursor: MTUwMA==)...
2025-11-10 14:19:44,427 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 16
2025-11-10 14:19:44,428 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 17 (cursor: MTYwMA==)...
2025-11-10 14:19:44,900 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 17
2025-11-10 14:19:44,901 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 18 (cursor: MTcwMA==)...
2025-11-10 14:19:45,554 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 18
2025-11-10 14:19:45,555 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 19 (cursor: MTgwMA==)...
2025-11-10 14:19:46,416 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 19
2025-11-10 14:19:46,416 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 20 (cursor: MTkwMA==)...
2025-11-10 14:19:46,861 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 20
2025-11-10 14:19:46,862 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 21 (cursor: MjAwMA==)...
2025-11-10 14:19:47,503 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 21
2025-11-10 14:19:47,504 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 22 (cursor: MjEwMA==)...
2025-11-10 14:19:48,167 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 22
2025-11-10 14:19:48,168 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 23 (cursor: MjIwMA==)...
2025-11-10 14:19:49,010 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 23
2025-11-10 14:19:49,011 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 24 (cursor: MjMwMA==)...
2025-11-10 14:19:49,433 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 24
2025-11-10 14:19:49,434 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 25 (cursor: MjQwMA==)...
2025-11-10 14:19:50,752 - __main__ - WARNING - âš ï¸ Health check failed: 2 issues
2025-11-10 14:19:50,752 - __main__ - WARNING -    - ðŸ”´ KhÃ´ng quÃ©t markets trong 80s!
2025-11-10 14:19:50,752 - __main__ - WARNING -    - âš ï¸ API cháº­m: 27.7s trung bÃ¬nh
2025-11-10 14:19:50,755 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 25
2025-11-10 14:19:50,756 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 26 (cursor: MjUwMA==)...
2025-11-10 14:19:51,183 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 26
2025-11-10 14:19:51,183 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 27 (cursor: MjYwMA==)...
2025-11-10 14:19:51,817 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 27
2025-11-10 14:19:51,818 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 28 (cursor: MjcwMA==)...
2025-11-10 14:19:52,237 - playwright_rewards_scraper - INFO - âœ… Got 14 markets on page 28
2025-11-10 14:19:52,237 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 29 (cursor: LTE=)...
2025-11-10 14:19:52,502 - playwright_rewards_scraper - INFO - âœ… No more markets on page 29
2025-11-10 14:19:52,503 - playwright_rewards_scraper - INFO - âœ… Fetched 2713 total unique markets from /rewards API
2025-11-10 14:19:52,576 - market_scanner_v2 - INFO - âœ… Got 2713 markets from /rewards page
2025-11-10 14:19:52,577 - market_scanner_v2 - INFO - âœ… ACCEPTED: Hang Seng (HSI) Up or Down on November 10?
2025-11-10 14:19:52,577 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:19:52,577 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$82)
2025-11-10 14:19:52,577 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:19:52,577 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-10 14:19:52,577 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:19:52,577 - market_scanner_v2 - INFO - âœ… ACCEPTED: DAX (DAX) Up or Down on November 10?
2025-11-10 14:19:52,577 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:19:52,577 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$7463)
2025-11-10 14:19:52,577 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:19:52,577 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.75
2025-11-10 14:19:52,577 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:19:52,578 - market_scanner_v2 - INFO - âœ… ACCEPTED: FTSE 100 (UKX) Up or Down on November 10?
2025-11-10 14:19:52,578 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:19:52,578 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$7424)
2025-11-10 14:19:52,578 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:19:52,578 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.74
2025-11-10 14:19:52,578 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:19:52,578 - market_scanner_v2 - INFO - âœ… ACCEPTED: Dow Jones (DJI) Up or Down on November 10?
2025-11-10 14:19:52,578 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:19:52,578 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$245)
2025-11-10 14:19:52,578 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:19:52,578 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.02
2025-11-10 14:19:52,578 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:19:52,578 - market_scanner_v2 - INFO - âœ… ACCEPTED: Nasdaq 100 (NDX) Up or Down on November 10?
2025-11-10 14:19:52,578 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:19:52,578 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$260)
2025-11-10 14:19:52,578 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:19:52,578 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.03
2025-11-10 14:19:52,578 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:19:52,578 - market_scanner_v2 - INFO - âœ… ACCEPTED: Nikkei 225 (NIK) Up or Down on November 10?
2025-11-10 14:19:52,578 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:19:52,578 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$76)
2025-11-10 14:19:52,578 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:19:52,578 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-10 14:19:52,578 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:19:52,578 - market_scanner_v2 - INFO - âœ… ACCEPTED: S&P 500 (SPX) Up or Down on November 10?
2025-11-10 14:19:52,578 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:19:52,578 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$79)
2025-11-10 14:19:52,579 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:19:52,579 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-10 14:19:52,579 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:19:52,579 - market_scanner_v2 - INFO - âœ… ACCEPTED: Airbnb (ABNB) Up or Down on November 10?
2025-11-10 14:19:52,579 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:19:52,579 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$31)
2025-11-10 14:19:52,579 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:19:52,579 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.00
2025-11-10 14:19:52,579 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:19:52,579 - market_scanner_v2 - INFO - âœ… ACCEPTED: Opendoor (OPEN) Up or Down on November 10?
2025-11-10 14:19:52,579 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:19:52,579 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$7420)
2025-11-10 14:19:52,579 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:19:52,579 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.74
2025-11-10 14:19:52,579 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:19:52,579 - market_scanner_v2 - INFO - âœ… ACCEPTED: Palantir (PLTR) Up or Down on November 10?
2025-11-10 14:19:52,579 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:19:52,579 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$6)
2025-11-10 14:19:52,579 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:19:52,579 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.00
2025-11-10 14:19:52,579 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:19:52,579 - market_scanner_v2 - INFO - âœ… ACCEPTED: Netflix (NFLX) Up or Down on November 10?
2025-11-10 14:19:52,579 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:19:52,580 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$50)
2025-11-10 14:19:52,580 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:19:52,580 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-10 14:19:52,580 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:19:52,580 - market_scanner_v2 - INFO - âœ… ACCEPTED: NVIDIA (NVDA) Up or Down on November 10?
2025-11-10 14:19:52,580 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:19:52,580 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$382)
2025-11-10 14:19:52,580 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:19:52,580 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.04
2025-11-10 14:19:52,580 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:19:52,580 - market_scanner_v2 - INFO - âœ… ACCEPTED: Tesla (TSLA) Up or Down on November 10?
2025-11-10 14:19:52,580 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:19:52,580 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$7454)
2025-11-10 14:19:52,580 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:19:52,580 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.75
2025-11-10 14:19:52,580 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:19:52,580 - market_scanner_v2 - INFO - âœ… ACCEPTED: Meta (META) Up or Down on November 10?
2025-11-10 14:19:52,580 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:19:52,580 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$1)
2025-11-10 14:19:52,580 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:19:52,580 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.00
2025-11-10 14:19:52,580 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:19:52,580 - market_scanner_v2 - INFO - âœ… ACCEPTED: Google (GOOGL) Up or Down on November 10?
2025-11-10 14:19:52,580 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:19:52,580 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$27)
2025-11-10 14:19:52,580 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:19:52,580 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.00
2025-11-10 14:19:52,580 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:19:52,581 - market_scanner_v2 - INFO - âœ… ACCEPTED: Amazon (AMZN) Up or Down on November 10?
2025-11-10 14:19:52,581 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:19:52,581 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$135)
2025-11-10 14:19:52,581 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:19:52,581 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-10 14:19:52,581 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:19:52,581 - market_scanner_v2 - INFO - âœ… ACCEPTED: Microsoft (MSFT) Up or Down on November 10?
2025-11-10 14:19:52,581 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:19:52,581 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$489)
2025-11-10 14:19:52,581 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:19:52,581 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.05
2025-11-10 14:19:52,581 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:19:52,581 - market_scanner_v2 - INFO - âœ… ACCEPTED: Apple (AAPL) Up or Down on November 10?
2025-11-10 14:19:52,581 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:19:52,581 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$119)
2025-11-10 14:19:52,581 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:19:52,581 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-10 14:19:52,581 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:19:52,582 - market_scanner_v2 - INFO - âœ… ACCEPTED: Nothing Ever Happens: November
2025-11-10 14:19:52,582 - market_scanner_v2 - INFO -    - Category: other
2025-11-10 14:19:52,582 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$43272)
2025-11-10 14:19:52,582 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:19:52,582 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 14.33
2025-11-10 14:19:52,582 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:19:52,587 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 19/2713 markets passed
2025-11-10 14:19:52,587 - market_scanner_v2 - INFO -    - 2568 rejected: reward < $20
2025-11-10 14:19:52,587 - market_scanner_v2 - INFO -    - 85 rejected: competition > 3
2025-11-10 14:19:52,587 - market_scanner_v2 - INFO -    - 17 rejected: categorical event outcomes (event_slug != market_slug)
2025-11-10 14:19:52,587 - market_scanner_v2 - INFO -    - 24 rejected: volume = 0 (no liquidity)
2025-11-10 14:19:52,587 - market_scanner_v2 - INFO - ðŸ” Verifying orderbook for top 19 markets...
2025-11-10 14:19:56,664 - market_scanner_v2 - INFO -    Progress: 10/19 markets verified...
2025-11-10 14:20:01,238 - market_scanner_v2 - INFO -    - 19 markets rejected: no orderbook (no bids or asks)
2025-11-10 14:20:01,239 - market_scanner_v2 - INFO - âœ… Found 0 qualifying markets (from 2713 total)
2025-11-10 14:20:01,242 - market_selector - INFO - Selected 0 markets from 0 candidates
2025-11-10 14:20:52,760 - market_scanner_v2 - INFO - ðŸŒ Scraping markets from /rewards page using Playwright...
2025-11-10 14:20:52,760 - playwright_rewards_scraper - INFO - ðŸŒ Fetching markets from /rewards API...
2025-11-10 14:20:52,760 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 1 (cursor: MA==)...
2025-11-10 14:20:53,434 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 1
2025-11-10 14:20:53,435 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 2 (cursor: MTAw)...
2025-11-10 14:20:54,094 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 2
2025-11-10 14:20:54,094 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 3 (cursor: MjAw)...
2025-11-10 14:20:54,756 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 3
2025-11-10 14:20:54,757 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 4 (cursor: MzAw)...
2025-11-10 14:20:55,407 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 4
2025-11-10 14:20:55,408 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 5 (cursor: NDAw)...
2025-11-10 14:20:55,849 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 5
2025-11-10 14:20:55,849 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 6 (cursor: NTAw)...
2025-11-10 14:20:56,548 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 6
2025-11-10 14:20:56,549 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 7 (cursor: NjAw)...
2025-11-10 14:20:57,209 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 7
2025-11-10 14:20:57,210 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 8 (cursor: NzAw)...
2025-11-10 14:20:57,896 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 8
2025-11-10 14:20:57,897 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 9 (cursor: ODAw)...
2025-11-10 14:20:58,594 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 9
2025-11-10 14:20:58,595 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 10 (cursor: OTAw)...
2025-11-10 14:20:59,234 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 10
2025-11-10 14:20:59,234 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 11 (cursor: MTAwMA==)...
2025-11-10 14:20:59,913 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 11
2025-11-10 14:20:59,913 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 12 (cursor: MTEwMA==)...
2025-11-10 14:21:00,555 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 12
2025-11-10 14:21:00,556 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 13 (cursor: MTIwMA==)...
2025-11-10 14:21:01,200 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 13
2025-11-10 14:21:01,201 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 14 (cursor: MTMwMA==)...
2025-11-10 14:21:01,918 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 14
2025-11-10 14:21:01,918 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 15 (cursor: MTQwMA==)...
2025-11-10 14:21:02,598 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 15
2025-11-10 14:21:02,598 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 16 (cursor: MTUwMA==)...
2025-11-10 14:21:03,240 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 16
2025-11-10 14:21:03,241 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 17 (cursor: MTYwMA==)...
2025-11-10 14:21:03,916 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 17
2025-11-10 14:21:03,917 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 18 (cursor: MTcwMA==)...
2025-11-10 14:21:04,587 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 18
2025-11-10 14:21:04,588 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 19 (cursor: MTgwMA==)...
2025-11-10 14:21:05,300 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 19
2025-11-10 14:21:05,300 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 20 (cursor: MTkwMA==)...
2025-11-10 14:21:05,970 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 20
2025-11-10 14:21:05,971 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 21 (cursor: MjAwMA==)...
2025-11-10 14:21:06,388 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 21
2025-11-10 14:21:06,388 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 22 (cursor: MjEwMA==)...
2025-11-10 14:21:07,089 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 22
2025-11-10 14:21:07,089 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 23 (cursor: MjIwMA==)...
2025-11-10 14:21:07,756 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 23
2025-11-10 14:21:07,756 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 24 (cursor: MjMwMA==)...
2025-11-10 14:21:08,400 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 24
2025-11-10 14:21:08,402 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 25 (cursor: MjQwMA==)...
2025-11-10 14:21:09,060 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 25
2025-11-10 14:21:09,060 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 26 (cursor: MjUwMA==)...
2025-11-10 14:21:09,731 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 26
2025-11-10 14:21:09,732 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 27 (cursor: MjYwMA==)...
2025-11-10 14:21:10,388 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 27
2025-11-10 14:21:10,388 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 28 (cursor: MjcwMA==)...
2025-11-10 14:21:10,849 - playwright_rewards_scraper - INFO - âœ… Got 14 markets on page 28
2025-11-10 14:21:10,849 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 29 (cursor: LTE=)...
2025-11-10 14:21:11,114 - playwright_rewards_scraper - INFO - âœ… No more markets on page 29
2025-11-10 14:21:11,115 - playwright_rewards_scraper - INFO - âœ… Fetched 2713 total unique markets from /rewards API
2025-11-10 14:21:11,161 - market_scanner_v2 - INFO - âœ… Got 2713 markets from /rewards page
2025-11-10 14:21:11,161 - market_scanner_v2 - INFO - âœ… ACCEPTED: Hang Seng (HSI) Up or Down on November 10?
2025-11-10 14:21:11,161 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:21:11,161 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$82)
2025-11-10 14:21:11,161 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:21:11,161 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-10 14:21:11,161 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:21:11,161 - market_scanner_v2 - INFO - âœ… ACCEPTED: DAX (DAX) Up or Down on November 10?
2025-11-10 14:21:11,161 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:21:11,161 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$7463)
2025-11-10 14:21:11,161 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:21:11,162 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.75
2025-11-10 14:21:11,162 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:21:11,162 - market_scanner_v2 - INFO - âœ… ACCEPTED: FTSE 100 (UKX) Up or Down on November 10?
2025-11-10 14:21:11,162 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:21:11,162 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$7424)
2025-11-10 14:21:11,162 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:21:11,162 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.74
2025-11-10 14:21:11,162 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:21:11,162 - market_scanner_v2 - INFO - âœ… ACCEPTED: Dow Jones (DJI) Up or Down on November 10?
2025-11-10 14:21:11,162 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:21:11,162 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$245)
2025-11-10 14:21:11,162 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:21:11,162 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.02
2025-11-10 14:21:11,162 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:21:11,162 - market_scanner_v2 - INFO - âœ… ACCEPTED: Nasdaq 100 (NDX) Up or Down on November 10?
2025-11-10 14:21:11,162 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:21:11,162 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$260)
2025-11-10 14:21:11,162 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:21:11,163 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.03
2025-11-10 14:21:11,163 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:21:11,163 - market_scanner_v2 - INFO - âœ… ACCEPTED: Nikkei 225 (NIK) Up or Down on November 10?
2025-11-10 14:21:11,163 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:21:11,163 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$76)
2025-11-10 14:21:11,163 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:21:11,163 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-10 14:21:11,163 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:21:11,163 - market_scanner_v2 - INFO - âœ… ACCEPTED: S&P 500 (SPX) Up or Down on November 10?
2025-11-10 14:21:11,163 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:21:11,163 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$79)
2025-11-10 14:21:11,163 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:21:11,163 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-10 14:21:11,163 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:21:11,163 - market_scanner_v2 - INFO - âœ… ACCEPTED: Airbnb (ABNB) Up or Down on November 10?
2025-11-10 14:21:11,163 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:21:11,163 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$31)
2025-11-10 14:21:11,163 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:21:11,163 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.00
2025-11-10 14:21:11,163 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:21:11,163 - market_scanner_v2 - INFO - âœ… ACCEPTED: Opendoor (OPEN) Up or Down on November 10?
2025-11-10 14:21:11,163 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:21:11,163 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$7420)
2025-11-10 14:21:11,163 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:21:11,163 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.74
2025-11-10 14:21:11,164 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:21:11,164 - market_scanner_v2 - INFO - âœ… ACCEPTED: Palantir (PLTR) Up or Down on November 10?
2025-11-10 14:21:11,164 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:21:11,164 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$6)
2025-11-10 14:21:11,164 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:21:11,164 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.00
2025-11-10 14:21:11,164 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:21:11,164 - market_scanner_v2 - INFO - âœ… ACCEPTED: Netflix (NFLX) Up or Down on November 10?
2025-11-10 14:21:11,164 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:21:11,164 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$50)
2025-11-10 14:21:11,164 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:21:11,164 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-10 14:21:11,164 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:21:11,164 - market_scanner_v2 - INFO - âœ… ACCEPTED: NVIDIA (NVDA) Up or Down on November 10?
2025-11-10 14:21:11,164 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:21:11,164 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$382)
2025-11-10 14:21:11,164 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:21:11,164 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.04
2025-11-10 14:21:11,164 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:21:11,164 - market_scanner_v2 - INFO - âœ… ACCEPTED: Tesla (TSLA) Up or Down on November 10?
2025-11-10 14:21:11,164 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:21:11,164 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$7454)
2025-11-10 14:21:11,164 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:21:11,164 - market_scanner_v2 - INFO -    - Competition: 2.22088 bars, Score: -211.34
2025-11-10 14:21:11,164 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:21:11,164 - market_scanner_v2 - INFO - âœ… ACCEPTED: Meta (META) Up or Down on November 10?
2025-11-10 14:21:11,164 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:21:11,164 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$1)
2025-11-10 14:21:11,164 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:21:11,165 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.00
2025-11-10 14:21:11,165 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:21:11,165 - market_scanner_v2 - INFO - âœ… ACCEPTED: Google (GOOGL) Up or Down on November 10?
2025-11-10 14:21:11,165 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:21:11,165 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$27)
2025-11-10 14:21:11,165 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:21:11,165 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.00
2025-11-10 14:21:11,165 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:21:11,165 - market_scanner_v2 - INFO - âœ… ACCEPTED: Amazon (AMZN) Up or Down on November 10?
2025-11-10 14:21:11,165 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:21:11,165 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$135)
2025-11-10 14:21:11,165 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:21:11,165 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-10 14:21:11,165 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:21:11,165 - market_scanner_v2 - INFO - âœ… ACCEPTED: Microsoft (MSFT) Up or Down on November 10?
2025-11-10 14:21:11,165 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:21:11,165 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$489)
2025-11-10 14:21:11,165 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:21:11,165 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.05
2025-11-10 14:21:11,165 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:21:11,165 - market_scanner_v2 - INFO - âœ… ACCEPTED: Apple (AAPL) Up or Down on November 10?
2025-11-10 14:21:11,165 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:21:11,165 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$119)
2025-11-10 14:21:11,165 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:21:11,165 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-10 14:21:11,165 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:21:11,169 - market_scanner_v2 - INFO - âœ… ACCEPTED: First to 5k: Gold or ETH?
2025-11-10 14:21:11,169 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:21:11,169 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$3771)
2025-11-10 14:21:11,169 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:21:11,169 - market_scanner_v2 - INFO -    - Competition: 1.741126 bars, Score: -163.74
2025-11-10 14:21:11,169 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:21:11,171 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 19/2713 markets passed
2025-11-10 14:21:11,171 - market_scanner_v2 - INFO -    - 2574 rejected: reward < $20
2025-11-10 14:21:11,171 - market_scanner_v2 - INFO -    - 79 rejected: competition > 3
2025-11-10 14:21:11,171 - market_scanner_v2 - INFO -    - 17 rejected: categorical event outcomes (event_slug != market_slug)
2025-11-10 14:21:11,171 - market_scanner_v2 - INFO -    - 24 rejected: volume = 0 (no liquidity)
2025-11-10 14:21:11,171 - market_scanner_v2 - INFO - ðŸ” Verifying orderbook for top 19 markets...
2025-11-10 14:21:15,330 - market_scanner_v2 - INFO -    Progress: 10/19 markets verified...
2025-11-10 14:21:19,883 - market_scanner_v2 - INFO -    - 19 markets rejected: no orderbook (no bids or asks)
2025-11-10 14:21:19,883 - market_scanner_v2 - INFO - âœ… Found 0 qualifying markets (from 2713 total)
2025-11-10 14:21:19,886 - market_selector - INFO - Selected 0 markets from 0 candidates
2025-11-10 14:22:26,790 - ml_predictor - INFO - Alert sent: ðŸš¨ <b>MONITORING ALERT</b>

ðŸ”´ KhÃ´ng quÃ©t markets trong 65s!
2025-11-10 14:22:26,790 - monitoring_system - INFO - Alert sent: no_scan
2025-11-10 14:22:26,790 - __main__ - WARNING - âš ï¸ Health check failed: 2 issues
2025-11-10 14:22:26,790 - __main__ - WARNING -    - ðŸ”´ KhÃ´ng quÃ©t markets trong 65s!
2025-11-10 14:22:26,790 - __main__ - WARNING -    - âš ï¸ API cháº­m: 27.5s trung bÃ¬nh
2025-11-10 14:22:31,042 - market_scanner_v2 - INFO - ðŸŒ Scraping markets from /rewards page using Playwright...
2025-11-10 14:22:31,042 - playwright_rewards_scraper - INFO - ðŸŒ Fetching markets from /rewards API...
2025-11-10 14:22:31,042 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 1 (cursor: MA==)...
2025-11-10 14:22:31,757 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 1
2025-11-10 14:22:31,758 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 2 (cursor: MTAw)...
2025-11-10 14:22:32,402 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 2
2025-11-10 14:22:32,403 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 3 (cursor: MjAw)...
2025-11-10 14:22:33,067 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 3
2025-11-10 14:22:33,068 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 4 (cursor: MzAw)...
2025-11-10 14:22:33,704 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 4
2025-11-10 14:22:33,704 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 5 (cursor: NDAw)...
2025-11-10 14:22:34,334 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 5
2025-11-10 14:22:34,335 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 6 (cursor: NTAw)...
2025-11-10 14:22:34,987 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 6
2025-11-10 14:22:34,988 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 7 (cursor: NjAw)...
2025-11-10 14:22:35,878 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 7
2025-11-10 14:22:35,878 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 8 (cursor: NzAw)...
2025-11-10 14:22:36,614 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 8
2025-11-10 14:22:36,614 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 9 (cursor: ODAw)...
2025-11-10 14:22:37,266 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 9
2025-11-10 14:22:37,267 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 10 (cursor: OTAw)...
2025-11-10 14:22:37,955 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 10
2025-11-10 14:22:37,956 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 11 (cursor: MTAwMA==)...
2025-11-10 14:22:38,764 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 11
2025-11-10 14:22:38,764 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 12 (cursor: MTEwMA==)...
2025-11-10 14:22:39,430 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 12
2025-11-10 14:22:39,431 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 13 (cursor: MTIwMA==)...
2025-11-10 14:22:40,111 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 13
2025-11-10 14:22:40,112 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 14 (cursor: MTMwMA==)...
2025-11-10 14:22:40,774 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 14
2025-11-10 14:22:40,774 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 15 (cursor: MTQwMA==)...
2025-11-10 14:22:41,438 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 15
2025-11-10 14:22:41,439 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 16 (cursor: MTUwMA==)...
2025-11-10 14:22:42,102 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 16
2025-11-10 14:22:42,103 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 17 (cursor: MTYwMA==)...
2025-11-10 14:22:42,777 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 17
2025-11-10 14:22:42,778 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 18 (cursor: MTcwMA==)...
2025-11-10 14:22:43,428 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 18
2025-11-10 14:22:43,429 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 19 (cursor: MTgwMA==)...
2025-11-10 14:22:44,109 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 19
2025-11-10 14:22:44,109 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 20 (cursor: MTkwMA==)...
2025-11-10 14:22:44,769 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 20
2025-11-10 14:22:44,769 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 21 (cursor: MjAwMA==)...
2025-11-10 14:22:45,414 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 21
2025-11-10 14:22:45,415 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 22 (cursor: MjEwMA==)...
2025-11-10 14:22:46,052 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 22
2025-11-10 14:22:46,053 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 23 (cursor: MjIwMA==)...
2025-11-10 14:22:46,735 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 23
2025-11-10 14:22:46,736 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 24 (cursor: MjMwMA==)...
2025-11-10 14:22:47,387 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 24
2025-11-10 14:22:47,388 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 25 (cursor: MjQwMA==)...
2025-11-10 14:22:47,811 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 25
2025-11-10 14:22:47,811 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 26 (cursor: MjUwMA==)...
2025-11-10 14:22:48,250 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 26
2025-11-10 14:22:48,251 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 27 (cursor: MjYwMA==)...
2025-11-10 14:22:48,688 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 27
2025-11-10 14:22:48,689 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 28 (cursor: MjcwMA==)...
2025-11-10 14:22:49,098 - playwright_rewards_scraper - INFO - âœ… Got 14 markets on page 28
2025-11-10 14:22:49,098 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 29 (cursor: LTE=)...
2025-11-10 14:22:49,352 - playwright_rewards_scraper - INFO - âœ… No more markets on page 29
2025-11-10 14:22:49,353 - playwright_rewards_scraper - INFO - âœ… Fetched 2713 total unique markets from /rewards API
2025-11-10 14:22:49,400 - market_scanner_v2 - INFO - âœ… Got 2713 markets from /rewards page
2025-11-10 14:22:49,400 - market_scanner_v2 - INFO - âœ… ACCEPTED: Hang Seng (HSI) Up or Down on November 10?
2025-11-10 14:22:49,400 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:22:49,400 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$82)
2025-11-10 14:22:49,400 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:22:49,400 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-10 14:22:49,400 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:22:49,400 - market_scanner_v2 - INFO - âœ… ACCEPTED: DAX (DAX) Up or Down on November 10?
2025-11-10 14:22:49,400 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:22:49,400 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$7463)
2025-11-10 14:22:49,400 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:22:49,400 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.75
2025-11-10 14:22:49,400 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:22:49,401 - market_scanner_v2 - INFO - âœ… ACCEPTED: FTSE 100 (UKX) Up or Down on November 10?
2025-11-10 14:22:49,401 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:22:49,401 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$7424)
2025-11-10 14:22:49,401 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:22:49,401 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.74
2025-11-10 14:22:49,401 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:22:49,401 - market_scanner_v2 - INFO - âœ… ACCEPTED: Dow Jones (DJI) Up or Down on November 10?
2025-11-10 14:22:49,401 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:22:49,401 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$245)
2025-11-10 14:22:49,401 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:22:49,401 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.02
2025-11-10 14:22:49,401 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:22:49,401 - market_scanner_v2 - INFO - âœ… ACCEPTED: Nasdaq 100 (NDX) Up or Down on November 10?
2025-11-10 14:22:49,401 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:22:49,401 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$260)
2025-11-10 14:22:49,401 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:22:49,401 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.03
2025-11-10 14:22:49,401 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:22:49,401 - market_scanner_v2 - INFO - âœ… ACCEPTED: Nikkei 225 (NIK) Up or Down on November 10?
2025-11-10 14:22:49,401 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:22:49,401 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$76)
2025-11-10 14:22:49,401 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:22:49,401 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-10 14:22:49,401 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:22:49,401 - market_scanner_v2 - INFO - âœ… ACCEPTED: S&P 500 (SPX) Up or Down on November 10?
2025-11-10 14:22:49,401 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:22:49,401 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$79)
2025-11-10 14:22:49,401 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:22:49,401 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-10 14:22:49,402 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:22:49,402 - market_scanner_v2 - INFO - âœ… ACCEPTED: Airbnb (ABNB) Up or Down on November 10?
2025-11-10 14:22:49,402 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:22:49,402 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$31)
2025-11-10 14:22:49,402 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:22:49,402 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.00
2025-11-10 14:22:49,402 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:22:49,402 - market_scanner_v2 - INFO - âœ… ACCEPTED: Opendoor (OPEN) Up or Down on November 10?
2025-11-10 14:22:49,402 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:22:49,402 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$7420)
2025-11-10 14:22:49,402 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:22:49,402 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.74
2025-11-10 14:22:49,402 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:22:49,402 - market_scanner_v2 - INFO - âœ… ACCEPTED: Palantir (PLTR) Up or Down on November 10?
2025-11-10 14:22:49,402 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:22:49,402 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$6)
2025-11-10 14:22:49,402 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:22:49,402 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.00
2025-11-10 14:22:49,402 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:22:49,402 - market_scanner_v2 - INFO - âœ… ACCEPTED: Netflix (NFLX) Up or Down on November 10?
2025-11-10 14:22:49,402 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:22:49,402 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$50)
2025-11-10 14:22:49,402 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:22:49,402 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-10 14:22:49,402 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:22:49,402 - market_scanner_v2 - INFO - âœ… ACCEPTED: NVIDIA (NVDA) Up or Down on November 10?
2025-11-10 14:22:49,402 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:22:49,403 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$382)
2025-11-10 14:22:49,403 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:22:49,403 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.04
2025-11-10 14:22:49,403 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:22:49,403 - market_scanner_v2 - INFO - âœ… ACCEPTED: Meta (META) Up or Down on November 10?
2025-11-10 14:22:49,403 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:22:49,403 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$1)
2025-11-10 14:22:49,403 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:22:49,403 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.00
2025-11-10 14:22:49,403 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:22:49,403 - market_scanner_v2 - INFO - âœ… ACCEPTED: Google (GOOGL) Up or Down on November 10?
2025-11-10 14:22:49,403 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:22:49,403 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$27)
2025-11-10 14:22:49,403 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:22:49,403 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.00
2025-11-10 14:22:49,403 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:22:49,403 - market_scanner_v2 - INFO - âœ… ACCEPTED: Amazon (AMZN) Up or Down on November 10?
2025-11-10 14:22:49,403 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:22:49,403 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$135)
2025-11-10 14:22:49,403 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:22:49,403 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-10 14:22:49,403 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:22:49,403 - market_scanner_v2 - INFO - âœ… ACCEPTED: Microsoft (MSFT) Up or Down on November 10?
2025-11-10 14:22:49,403 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:22:49,403 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$489)
2025-11-10 14:22:49,403 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:22:49,403 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.05
2025-11-10 14:22:49,403 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:22:49,404 - market_scanner_v2 - INFO - âœ… ACCEPTED: Apple (AAPL) Up or Down on November 10?
2025-11-10 14:22:49,404 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:22:49,404 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$119)
2025-11-10 14:22:49,404 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:22:49,404 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-10 14:22:49,404 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:22:49,407 - market_scanner_v2 - INFO - âœ… ACCEPTED: First to 5k: Gold or ETH?
2025-11-10 14:22:49,407 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:22:49,407 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$3771)
2025-11-10 14:22:49,407 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:22:49,407 - market_scanner_v2 - INFO -    - Competition: 1.305845 bars, Score: -120.21
2025-11-10 14:22:49,407 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:22:49,409 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 18/2713 markets passed
2025-11-10 14:22:49,409 - market_scanner_v2 - INFO -    - 2574 rejected: reward < $20
2025-11-10 14:22:49,409 - market_scanner_v2 - INFO -    - 77 rejected: competition > 3
2025-11-10 14:22:49,409 - market_scanner_v2 - INFO -    - 20 rejected: categorical event outcomes (event_slug != market_slug)
2025-11-10 14:22:49,409 - market_scanner_v2 - INFO -    - 24 rejected: volume = 0 (no liquidity)
2025-11-10 14:22:49,409 - market_scanner_v2 - INFO - ðŸ” Verifying orderbook for top 18 markets...
2025-11-10 14:22:53,520 - market_scanner_v2 - INFO -    Progress: 10/18 markets verified...
2025-11-10 14:22:57,794 - __main__ - WARNING - âš ï¸ Health check failed: 2 issues
2025-11-10 14:22:57,794 - __main__ - WARNING -    - ðŸ”´ KhÃ´ng quÃ©t markets trong 97s!
2025-11-10 14:22:57,794 - __main__ - WARNING -    - âš ï¸ API cháº­m: 27.5s trung bÃ¬nh
2025-11-10 14:22:58,383 - market_scanner_v2 - INFO -    - 18 markets rejected: no orderbook (no bids or asks)
2025-11-10 14:22:58,383 - market_scanner_v2 - INFO - âœ… Found 0 qualifying markets (from 2713 total)
2025-11-10 14:22:58,386 - market_selector - INFO - Selected 0 markets from 0 candidates
2025-11-10 14:23:38,344 - profit_taking_manager - INFO - ðŸ” Checking positions for wallet: 0x18F261DC...Ae4FfD96
2025-11-10 14:23:38,694 - profit_taking_manager - INFO - ðŸ“Š Found 8 active positions
2025-11-10 14:23:38,694 - profit_taking_manager - WARNING - âš ï¸  Skipping position FIDE World Cup 2025 - Shant Sa - invalid data (shares=113.0, avg=0.09, current=0.0)
2025-11-10 14:23:38,694 - profit_taking_manager - INFO - 
ðŸ“ˆ Position: Will Google Gemini 3 score at least 70% on the Fro
2025-11-10 14:23:38,694 - profit_taking_manager - INFO -    Shares: 68.00 @ $0.3900
2025-11-10 14:23:38,694 - profit_taking_manager - INFO -    Current: $0.0700
2025-11-10 14:23:38,694 - profit_taking_manager - INFO -    P&L: $-21.76 (-82.05%)
2025-11-10 14:23:38,694 - profit_taking_manager - INFO -    â¸ï¸  Losing position - NOT closing (manual decision required)
2025-11-10 14:23:38,694 - profit_taking_manager - WARNING - âš ï¸  Skipping position Syracuse vs. Miami - invalid data (shares=66.0, avg=0.49, current=0.0)
2025-11-10 14:23:38,694 - profit_taking_manager - WARNING - âš ï¸  Skipping position FIDE World Cup 2025 - Michael  - invalid data (shares=65.001889, avg=0.180036, current=0.0)
2025-11-10 14:23:38,695 - profit_taking_manager - INFO - 
ðŸ“ˆ Position: Weed rescheduled in 2025?
2025-11-10 14:23:38,695 - profit_taking_manager - INFO -    Shares: 54.43 @ $0.1100
2025-11-10 14:23:38,695 - profit_taking_manager - INFO -    Current: $0.1050
2025-11-10 14:23:38,695 - profit_taking_manager - INFO -    P&L: $-0.27 (-4.55%)
2025-11-10 14:23:38,695 - profit_taking_manager - INFO -    â¸ï¸  Losing position - NOT closing (manual decision required)
2025-11-10 14:23:38,695 - profit_taking_manager - INFO - 
ðŸ“ˆ Position: Supreme Court vacancy in 2025?
2025-11-10 14:23:38,695 - profit_taking_manager - INFO -    Shares: 44.21 @ $0.0600
2025-11-10 14:23:38,695 - profit_taking_manager - INFO -    Current: $0.0500
2025-11-10 14:23:38,695 - profit_taking_manager - INFO -    P&L: $-0.44 (-16.67%)
2025-11-10 14:23:38,695 - profit_taking_manager - INFO -    â¸ï¸  Losing position - NOT closing (manual decision required)
2025-11-10 14:23:38,695 - profit_taking_manager - INFO - 
ðŸ“ˆ Position: Dan Clancy out as Twitch CEO in 2025?
2025-11-10 14:23:38,695 - profit_taking_manager - INFO -    Shares: 30.78 @ $0.0900
2025-11-10 14:23:38,695 - profit_taking_manager - INFO -    Current: $0.0800
2025-11-10 14:23:38,695 - profit_taking_manager - INFO -    P&L: $-0.31 (-11.11%)
2025-11-10 14:23:38,695 - profit_taking_manager - INFO -    â¸ï¸  Losing position - NOT closing (manual decision required)
2025-11-10 14:23:38,695 - profit_taking_manager - WARNING - âš ï¸  Skipping position Charlotte 49ers vs. East Carol - invalid data (shares=0.017509, avg=0.14942, current=0.0)
2025-11-10 14:23:38,695 - __main__ - INFO - â³ Next profit check in 300s
2025-11-10 14:23:59,801 - __main__ - WARNING - âš ï¸ Health check failed: 2 issues
2025-11-10 14:23:59,801 - __main__ - WARNING -    - ðŸ”´ KhÃ´ng quÃ©t markets trong 60s!
2025-11-10 14:23:59,801 - __main__ - WARNING -    - âš ï¸ API cháº­m: 27.5s trung bÃ¬nh
2025-11-10 14:24:01,988 - market_scanner_v2 - INFO - ðŸŒ Scraping markets from /rewards page using Playwright...
2025-11-10 14:24:01,988 - playwright_rewards_scraper - INFO - ðŸŒ Fetching markets from /rewards API...
2025-11-10 14:24:01,988 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 1 (cursor: MA==)...
2025-11-10 14:24:02,669 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 1
2025-11-10 14:24:02,670 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 2 (cursor: MTAw)...
2025-11-10 14:24:03,313 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 2
2025-11-10 14:24:03,314 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 3 (cursor: MjAw)...
2025-11-10 14:24:03,951 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 3
2025-11-10 14:24:03,951 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 4 (cursor: MzAw)...
2025-11-10 14:24:04,632 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 4
2025-11-10 14:24:04,633 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 5 (cursor: NDAw)...
2025-11-10 14:24:05,294 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 5
2025-11-10 14:24:05,295 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 6 (cursor: NTAw)...
2025-11-10 14:24:05,943 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 6
2025-11-10 14:24:05,944 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 7 (cursor: NjAw)...
2025-11-10 14:24:06,602 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 7
2025-11-10 14:24:06,603 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 8 (cursor: NzAw)...
2025-11-10 14:24:07,301 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 8
2025-11-10 14:24:07,302 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 9 (cursor: ODAw)...
2025-11-10 14:24:07,999 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 9
2025-11-10 14:24:07,999 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 10 (cursor: OTAw)...
2025-11-10 14:24:08,643 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 10
2025-11-10 14:24:08,644 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 11 (cursor: MTAwMA==)...
2025-11-10 14:24:09,324 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 11
2025-11-10 14:24:09,324 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 12 (cursor: MTEwMA==)...
2025-11-10 14:24:09,777 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 12
2025-11-10 14:24:09,777 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 13 (cursor: MTIwMA==)...
2025-11-10 14:24:10,452 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 13
2025-11-10 14:24:10,453 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 14 (cursor: MTMwMA==)...
2025-11-10 14:24:11,114 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 14
2025-11-10 14:24:11,115 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 15 (cursor: MTQwMA==)...
2025-11-10 14:24:11,809 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 15
2025-11-10 14:24:11,810 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 16 (cursor: MTUwMA==)...
2025-11-10 14:24:12,464 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 16
2025-11-10 14:24:12,464 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 17 (cursor: MTYwMA==)...
2025-11-10 14:24:13,139 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 17
2025-11-10 14:24:13,140 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 18 (cursor: MTcwMA==)...
2025-11-10 14:24:13,797 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 18
2025-11-10 14:24:13,798 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 19 (cursor: MTgwMA==)...
2025-11-10 14:24:14,212 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 19
2025-11-10 14:24:14,212 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 20 (cursor: MTkwMA==)...
2025-11-10 14:24:14,856 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 20
2025-11-10 14:24:14,857 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 21 (cursor: MjAwMA==)...
2025-11-10 14:24:15,729 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 21
2025-11-10 14:24:15,730 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 22 (cursor: MjEwMA==)...
2025-11-10 14:24:16,389 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 22
2025-11-10 14:24:16,390 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 23 (cursor: MjIwMA==)...
2025-11-10 14:24:17,045 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 23
2025-11-10 14:24:17,046 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 24 (cursor: MjMwMA==)...
2025-11-10 14:24:17,677 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 24
2025-11-10 14:24:17,678 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 25 (cursor: MjQwMA==)...
2025-11-10 14:24:18,438 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 25
2025-11-10 14:24:18,438 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 26 (cursor: MjUwMA==)...
2025-11-10 14:24:19,056 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 26
2025-11-10 14:24:19,056 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 27 (cursor: MjYwMA==)...
2025-11-10 14:24:19,723 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 27
2025-11-10 14:24:19,724 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 28 (cursor: MjcwMA==)...
2025-11-10 14:24:20,154 - playwright_rewards_scraper - INFO - âœ… Got 14 markets on page 28
2025-11-10 14:24:20,154 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 29 (cursor: LTE=)...
2025-11-10 14:24:20,454 - playwright_rewards_scraper - INFO - âœ… No more markets on page 29
2025-11-10 14:24:20,454 - playwright_rewards_scraper - INFO - âœ… Fetched 2713 total unique markets from /rewards API
2025-11-10 14:24:20,502 - market_scanner_v2 - INFO - âœ… Got 2713 markets from /rewards page
2025-11-10 14:24:20,503 - market_scanner_v2 - INFO - âœ… ACCEPTED: Hang Seng (HSI) Up or Down on November 10?
2025-11-10 14:24:20,503 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:24:20,503 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$82)
2025-11-10 14:24:20,503 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:24:20,503 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-10 14:24:20,503 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:24:20,503 - market_scanner_v2 - INFO - âœ… ACCEPTED: DAX (DAX) Up or Down on November 10?
2025-11-10 14:24:20,503 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:24:20,503 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$7463)
2025-11-10 14:24:20,503 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:24:20,503 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.75
2025-11-10 14:24:20,503 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:24:20,503 - market_scanner_v2 - INFO - âœ… ACCEPTED: FTSE 100 (UKX) Up or Down on November 10?
2025-11-10 14:24:20,503 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:24:20,503 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$7424)
2025-11-10 14:24:20,503 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:24:20,503 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.74
2025-11-10 14:24:20,503 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:24:20,504 - market_scanner_v2 - INFO - âœ… ACCEPTED: Dow Jones (DJI) Up or Down on November 10?
2025-11-10 14:24:20,504 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:24:20,504 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$245)
2025-11-10 14:24:20,504 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:24:20,504 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.02
2025-11-10 14:24:20,504 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:24:20,504 - market_scanner_v2 - INFO - âœ… ACCEPTED: Nasdaq 100 (NDX) Up or Down on November 10?
2025-11-10 14:24:20,504 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:24:20,504 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$260)
2025-11-10 14:24:20,504 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:24:20,504 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.03
2025-11-10 14:24:20,504 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:24:20,504 - market_scanner_v2 - INFO - âœ… ACCEPTED: Nikkei 225 (NIK) Up or Down on November 10?
2025-11-10 14:24:20,504 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:24:20,504 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$76)
2025-11-10 14:24:20,504 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:24:20,504 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-10 14:24:20,504 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:24:20,504 - market_scanner_v2 - INFO - âœ… ACCEPTED: S&P 500 (SPX) Up or Down on November 10?
2025-11-10 14:24:20,504 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:24:20,504 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$79)
2025-11-10 14:24:20,504 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:24:20,504 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-10 14:24:20,504 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:24:20,505 - market_scanner_v2 - INFO - âœ… ACCEPTED: Airbnb (ABNB) Up or Down on November 10?
2025-11-10 14:24:20,505 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:24:20,505 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$31)
2025-11-10 14:24:20,505 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:24:20,505 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.00
2025-11-10 14:24:20,505 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:24:20,505 - market_scanner_v2 - INFO - âœ… ACCEPTED: Opendoor (OPEN) Up or Down on November 10?
2025-11-10 14:24:20,505 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:24:20,505 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$7420)
2025-11-10 14:24:20,505 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:24:20,505 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.74
2025-11-10 14:24:20,505 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:24:20,505 - market_scanner_v2 - INFO - âœ… ACCEPTED: Palantir (PLTR) Up or Down on November 10?
2025-11-10 14:24:20,505 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:24:20,505 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$6)
2025-11-10 14:24:20,505 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:24:20,505 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.00
2025-11-10 14:24:20,505 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:24:20,505 - market_scanner_v2 - INFO - âœ… ACCEPTED: Netflix (NFLX) Up or Down on November 10?
2025-11-10 14:24:20,505 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:24:20,505 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$50)
2025-11-10 14:24:20,505 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:24:20,505 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-10 14:24:20,506 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:24:20,506 - market_scanner_v2 - INFO - âœ… ACCEPTED: NVIDIA (NVDA) Up or Down on November 10?
2025-11-10 14:24:20,506 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:24:20,506 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$382)
2025-11-10 14:24:20,506 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:24:20,506 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.04
2025-11-10 14:24:20,506 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:24:20,506 - market_scanner_v2 - INFO - âœ… ACCEPTED: Tesla (TSLA) Up or Down on November 10?
2025-11-10 14:24:20,506 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:24:20,506 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$7454)
2025-11-10 14:24:20,506 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:24:20,506 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.75
2025-11-10 14:24:20,506 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:24:20,506 - market_scanner_v2 - INFO - âœ… ACCEPTED: Meta (META) Up or Down on November 10?
2025-11-10 14:24:20,506 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:24:20,506 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$1)
2025-11-10 14:24:20,506 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:24:20,506 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.00
2025-11-10 14:24:20,506 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:24:20,506 - market_scanner_v2 - INFO - âœ… ACCEPTED: Google (GOOGL) Up or Down on November 10?
2025-11-10 14:24:20,506 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:24:20,506 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$27)
2025-11-10 14:24:20,506 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:24:20,507 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.00
2025-11-10 14:24:20,507 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:24:20,507 - market_scanner_v2 - INFO - âœ… ACCEPTED: Amazon (AMZN) Up or Down on November 10?
2025-11-10 14:24:20,507 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:24:20,507 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$135)
2025-11-10 14:24:20,507 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:24:20,507 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-10 14:24:20,507 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:24:20,507 - market_scanner_v2 - INFO - âœ… ACCEPTED: Microsoft (MSFT) Up or Down on November 10?
2025-11-10 14:24:20,507 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:24:20,507 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$489)
2025-11-10 14:24:20,507 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:24:20,507 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.05
2025-11-10 14:24:20,507 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:24:20,507 - market_scanner_v2 - INFO - âœ… ACCEPTED: Apple (AAPL) Up or Down on November 10?
2025-11-10 14:24:20,507 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:24:20,507 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$119)
2025-11-10 14:24:20,507 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:24:20,507 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-10 14:24:20,507 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:24:20,511 - market_scanner_v2 - INFO - âœ… ACCEPTED: First to 5k: Gold or ETH?
2025-11-10 14:24:20,511 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:24:20,511 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$3771)
2025-11-10 14:24:20,511 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:24:20,511 - market_scanner_v2 - INFO -    - Competition: 1.305845 bars, Score: -120.21
2025-11-10 14:24:20,511 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:24:20,513 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 19/2713 markets passed
2025-11-10 14:24:20,513 - market_scanner_v2 - INFO -    - 2574 rejected: reward < $20
2025-11-10 14:24:20,513 - market_scanner_v2 - INFO -    - 75 rejected: competition > 3
2025-11-10 14:24:20,514 - market_scanner_v2 - INFO -    - 21 rejected: categorical event outcomes (event_slug != market_slug)
2025-11-10 14:24:20,514 - market_scanner_v2 - INFO -    - 24 rejected: volume = 0 (no liquidity)
2025-11-10 14:24:20,514 - market_scanner_v2 - INFO - ðŸ” Verifying orderbook for top 19 markets...
2025-11-10 14:24:24,554 - market_scanner_v2 - INFO -    Progress: 10/19 markets verified...
2025-11-10 14:24:29,088 - market_scanner_v2 - INFO -    - 19 markets rejected: no orderbook (no bids or asks)
2025-11-10 14:24:29,089 - market_scanner_v2 - INFO - âœ… Found 0 qualifying markets (from 2713 total)
2025-11-10 14:24:29,092 - market_selector - INFO - Selected 0 markets from 0 candidates
2025-11-10 14:25:17,840 - market_scanner_v2 - INFO - ðŸŒ Scraping markets from /rewards page using Playwright...
2025-11-10 14:25:17,840 - playwright_rewards_scraper - INFO - ðŸŒ Fetching markets from /rewards API...
2025-11-10 14:25:17,841 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 1 (cursor: MA==)...
2025-11-10 14:25:18,539 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 1
2025-11-10 14:25:18,540 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 2 (cursor: MTAw)...
2025-11-10 14:25:19,195 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 2
2025-11-10 14:25:19,196 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 3 (cursor: MjAw)...
2025-11-10 14:25:19,841 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 3
2025-11-10 14:25:19,842 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 4 (cursor: MzAw)...
2025-11-10 14:25:20,483 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 4
2025-11-10 14:25:20,484 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 5 (cursor: NDAw)...
2025-11-10 14:25:20,888 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 5
2025-11-10 14:25:20,889 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 6 (cursor: NTAw)...
2025-11-10 14:25:21,532 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 6
2025-11-10 14:25:21,533 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 7 (cursor: NjAw)...
2025-11-10 14:25:22,189 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 7
2025-11-10 14:25:22,189 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 8 (cursor: NzAw)...
2025-11-10 14:25:22,616 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 8
2025-11-10 14:25:22,617 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 9 (cursor: ODAw)...
2025-11-10 14:25:23,294 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 9
2025-11-10 14:25:23,294 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 10 (cursor: OTAw)...
2025-11-10 14:25:23,960 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 10
2025-11-10 14:25:23,960 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 11 (cursor: MTAwMA==)...
2025-11-10 14:25:24,629 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 11
2025-11-10 14:25:24,629 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 12 (cursor: MTEwMA==)...
2025-11-10 14:25:25,245 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 12
2025-11-10 14:25:25,245 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 13 (cursor: MTIwMA==)...
2025-11-10 14:25:25,659 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 13
2025-11-10 14:25:25,660 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 14 (cursor: MTMwMA==)...
2025-11-10 14:25:26,089 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 14
2025-11-10 14:25:26,090 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 15 (cursor: MTQwMA==)...
2025-11-10 14:25:26,723 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 15
2025-11-10 14:25:26,724 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 16 (cursor: MTUwMA==)...
2025-11-10 14:25:27,366 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 16
2025-11-10 14:25:27,367 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 17 (cursor: MTYwMA==)...
2025-11-10 14:25:28,050 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 17
2025-11-10 14:25:28,051 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 18 (cursor: MTcwMA==)...
2025-11-10 14:25:28,467 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 18
2025-11-10 14:25:28,468 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 19 (cursor: MTgwMA==)...
2025-11-10 14:25:29,124 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 19
2025-11-10 14:25:29,125 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 20 (cursor: MTkwMA==)...
2025-11-10 14:25:29,801 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 20
2025-11-10 14:25:29,801 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 21 (cursor: MjAwMA==)...
2025-11-10 14:25:30,443 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 21
2025-11-10 14:25:30,444 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 22 (cursor: MjEwMA==)...
2025-11-10 14:25:31,090 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 22
2025-11-10 14:25:31,091 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 23 (cursor: MjIwMA==)...
2025-11-10 14:25:31,729 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 23
2025-11-10 14:25:31,729 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 24 (cursor: MjMwMA==)...
2025-11-10 14:25:32,811 - __main__ - WARNING - âš ï¸ Health check failed: 2 issues
2025-11-10 14:25:32,812 - __main__ - WARNING -    - ðŸ”´ KhÃ´ng quÃ©t markets trong 63s!
2025-11-10 14:25:32,812 - __main__ - WARNING -    - âš ï¸ API cháº­m: 27.5s trung bÃ¬nh
2025-11-10 14:25:32,815 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 24
2025-11-10 14:25:32,815 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 25 (cursor: MjQwMA==)...
2025-11-10 14:25:33,467 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 25
2025-11-10 14:25:33,468 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 26 (cursor: MjUwMA==)...
2025-11-10 14:25:34,127 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 26
2025-11-10 14:25:34,127 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 27 (cursor: MjYwMA==)...
2025-11-10 14:25:34,778 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 27
2025-11-10 14:25:34,778 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 28 (cursor: MjcwMA==)...
2025-11-10 14:25:35,194 - playwright_rewards_scraper - INFO - âœ… Got 14 markets on page 28
2025-11-10 14:25:35,194 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 29 (cursor: LTE=)...
2025-11-10 14:25:35,503 - playwright_rewards_scraper - INFO - âœ… No more markets on page 29
2025-11-10 14:25:35,504 - playwright_rewards_scraper - INFO - âœ… Fetched 2713 total unique markets from /rewards API
2025-11-10 14:25:35,550 - market_scanner_v2 - INFO - âœ… Got 2713 markets from /rewards page
2025-11-10 14:25:35,550 - market_scanner_v2 - INFO - âœ… ACCEPTED: Hang Seng (HSI) Up or Down on November 10?
2025-11-10 14:25:35,550 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:25:35,550 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$82)
2025-11-10 14:25:35,550 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:25:35,551 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-10 14:25:35,551 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:25:35,551 - market_scanner_v2 - INFO - âœ… ACCEPTED: DAX (DAX) Up or Down on November 10?
2025-11-10 14:25:35,551 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:25:35,551 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$7463)
2025-11-10 14:25:35,551 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:25:35,551 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.75
2025-11-10 14:25:35,551 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:25:35,551 - market_scanner_v2 - INFO - âœ… ACCEPTED: FTSE 100 (UKX) Up or Down on November 10?
2025-11-10 14:25:35,551 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:25:35,551 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$7424)
2025-11-10 14:25:35,551 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:25:35,551 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.74
2025-11-10 14:25:35,551 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:25:35,551 - market_scanner_v2 - INFO - âœ… ACCEPTED: Dow Jones (DJI) Up or Down on November 10?
2025-11-10 14:25:35,551 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:25:35,551 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$245)
2025-11-10 14:25:35,551 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:25:35,551 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.02
2025-11-10 14:25:35,551 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:25:35,551 - market_scanner_v2 - INFO - âœ… ACCEPTED: Nasdaq 100 (NDX) Up or Down on November 10?
2025-11-10 14:25:35,551 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:25:35,551 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$260)
2025-11-10 14:25:35,551 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:25:35,551 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.03
2025-11-10 14:25:35,551 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:25:35,551 - market_scanner_v2 - INFO - âœ… ACCEPTED: Nikkei 225 (NIK) Up or Down on November 10?
2025-11-10 14:25:35,552 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:25:35,552 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$76)
2025-11-10 14:25:35,552 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:25:35,552 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-10 14:25:35,552 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:25:35,552 - market_scanner_v2 - INFO - âœ… ACCEPTED: S&P 500 (SPX) Up or Down on November 10?
2025-11-10 14:25:35,552 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:25:35,552 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$79)
2025-11-10 14:25:35,552 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:25:35,552 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-10 14:25:35,552 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:25:35,552 - market_scanner_v2 - INFO - âœ… ACCEPTED: Airbnb (ABNB) Up or Down on November 10?
2025-11-10 14:25:35,552 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:25:35,552 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$31)
2025-11-10 14:25:35,552 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:25:35,552 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.00
2025-11-10 14:25:35,552 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:25:35,552 - market_scanner_v2 - INFO - âœ… ACCEPTED: Opendoor (OPEN) Up or Down on November 10?
2025-11-10 14:25:35,552 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:25:35,552 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$7420)
2025-11-10 14:25:35,552 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:25:35,552 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.74
2025-11-10 14:25:35,552 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:25:35,552 - market_scanner_v2 - INFO - âœ… ACCEPTED: Palantir (PLTR) Up or Down on November 10?
2025-11-10 14:25:35,552 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:25:35,552 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$6)
2025-11-10 14:25:35,552 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:25:35,552 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.00
2025-11-10 14:25:35,552 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:25:35,552 - market_scanner_v2 - INFO - âœ… ACCEPTED: Netflix (NFLX) Up or Down on November 10?
2025-11-10 14:25:35,553 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:25:35,553 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$50)
2025-11-10 14:25:35,553 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:25:35,553 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-10 14:25:35,553 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:25:35,553 - market_scanner_v2 - INFO - âœ… ACCEPTED: NVIDIA (NVDA) Up or Down on November 10?
2025-11-10 14:25:35,553 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:25:35,553 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$382)
2025-11-10 14:25:35,553 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:25:35,553 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.04
2025-11-10 14:25:35,553 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:25:35,553 - market_scanner_v2 - INFO - âœ… ACCEPTED: Tesla (TSLA) Up or Down on November 10?
2025-11-10 14:25:35,553 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:25:35,553 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$7454)
2025-11-10 14:25:35,553 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:25:35,553 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.75
2025-11-10 14:25:35,553 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:25:35,553 - market_scanner_v2 - INFO - âœ… ACCEPTED: Meta (META) Up or Down on November 10?
2025-11-10 14:25:35,553 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:25:35,553 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$1)
2025-11-10 14:25:35,553 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:25:35,553 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.00
2025-11-10 14:25:35,554 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:25:35,554 - market_scanner_v2 - INFO - âœ… ACCEPTED: Google (GOOGL) Up or Down on November 10?
2025-11-10 14:25:35,554 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:25:35,554 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$27)
2025-11-10 14:25:35,554 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:25:35,554 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.00
2025-11-10 14:25:35,554 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:25:35,554 - market_scanner_v2 - INFO - âœ… ACCEPTED: Amazon (AMZN) Up or Down on November 10?
2025-11-10 14:25:35,554 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:25:35,554 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$135)
2025-11-10 14:25:35,554 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:25:35,554 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-10 14:25:35,554 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:25:35,554 - market_scanner_v2 - INFO - âœ… ACCEPTED: Microsoft (MSFT) Up or Down on November 10?
2025-11-10 14:25:35,554 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:25:35,554 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$489)
2025-11-10 14:25:35,554 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:25:35,554 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.05
2025-11-10 14:25:35,554 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:25:35,554 - market_scanner_v2 - INFO - âœ… ACCEPTED: Apple (AAPL) Up or Down on November 10?
2025-11-10 14:25:35,554 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:25:35,554 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$119)
2025-11-10 14:25:35,554 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:25:35,554 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-10 14:25:35,554 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:25:35,558 - market_scanner_v2 - INFO - âœ… ACCEPTED: First to 5k: Gold or ETH?
2025-11-10 14:25:35,558 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:25:35,558 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$3771)
2025-11-10 14:25:35,558 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:25:35,558 - market_scanner_v2 - INFO -    - Competition: 1.305845 bars, Score: -120.21
2025-11-10 14:25:35,558 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:25:35,560 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 19/2713 markets passed
2025-11-10 14:25:35,560 - market_scanner_v2 - INFO -    - 2574 rejected: reward < $20
2025-11-10 14:25:35,560 - market_scanner_v2 - INFO -    - 74 rejected: competition > 3
2025-11-10 14:25:35,560 - market_scanner_v2 - INFO -    - 22 rejected: categorical event outcomes (event_slug != market_slug)
2025-11-10 14:25:35,560 - market_scanner_v2 - INFO -    - 24 rejected: volume = 0 (no liquidity)
2025-11-10 14:25:35,560 - market_scanner_v2 - INFO - ðŸ” Verifying orderbook for top 19 markets...
2025-11-10 14:25:39,701 - market_scanner_v2 - INFO -    Progress: 10/19 markets verified...
2025-11-10 14:25:44,246 - market_scanner_v2 - INFO -    - 19 markets rejected: no orderbook (no bids or asks)
2025-11-10 14:25:44,246 - market_scanner_v2 - INFO - âœ… Found 0 qualifying markets (from 2713 total)
2025-11-10 14:25:44,249 - market_selector - INFO - Selected 0 markets from 0 candidates
2025-11-10 14:26:41,223 - market_scanner_v2 - INFO - ðŸŒ Scraping markets from /rewards page using Playwright...
2025-11-10 14:26:41,223 - playwright_rewards_scraper - INFO - ðŸŒ Fetching markets from /rewards API...
2025-11-10 14:26:41,223 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 1 (cursor: MA==)...
2025-11-10 14:26:41,886 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 1
2025-11-10 14:26:41,886 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 2 (cursor: MTAw)...
2025-11-10 14:26:42,389 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 2
2025-11-10 14:26:42,390 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 3 (cursor: MjAw)...
2025-11-10 14:26:42,805 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 3
2025-11-10 14:26:42,806 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 4 (cursor: MzAw)...
2025-11-10 14:26:43,464 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 4
2025-11-10 14:26:43,465 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 5 (cursor: NDAw)...
2025-11-10 14:26:43,882 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 5
2025-11-10 14:26:43,883 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 6 (cursor: NTAw)...
2025-11-10 14:26:44,356 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 6
2025-11-10 14:26:44,357 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 7 (cursor: NjAw)...
2025-11-10 14:26:44,800 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 7
2025-11-10 14:26:44,801 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 8 (cursor: NzAw)...
2025-11-10 14:26:45,471 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 8
2025-11-10 14:26:45,471 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 9 (cursor: ODAw)...
2025-11-10 14:26:46,128 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 9
2025-11-10 14:26:46,128 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 10 (cursor: OTAw)...
2025-11-10 14:26:46,776 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 10
2025-11-10 14:26:46,777 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 11 (cursor: MTAwMA==)...
2025-11-10 14:26:47,418 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 11
2025-11-10 14:26:47,419 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 12 (cursor: MTEwMA==)...
2025-11-10 14:26:47,837 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 12
2025-11-10 14:26:47,838 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 13 (cursor: MTIwMA==)...
2025-11-10 14:26:48,252 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 13
2025-11-10 14:26:48,253 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 14 (cursor: MTMwMA==)...
2025-11-10 14:26:48,668 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 14
2025-11-10 14:26:48,669 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 15 (cursor: MTQwMA==)...
2025-11-10 14:26:49,146 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 15
2025-11-10 14:26:49,146 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 16 (cursor: MTUwMA==)...
2025-11-10 14:26:49,793 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 16
2025-11-10 14:26:49,794 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 17 (cursor: MTYwMA==)...
2025-11-10 14:26:50,441 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 17
2025-11-10 14:26:50,442 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 18 (cursor: MTcwMA==)...
2025-11-10 14:26:51,110 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 18
2025-11-10 14:26:51,111 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 19 (cursor: MTgwMA==)...
2025-11-10 14:26:51,758 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 19
2025-11-10 14:26:51,759 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 20 (cursor: MTkwMA==)...
2025-11-10 14:26:52,198 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 20
2025-11-10 14:26:52,199 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 21 (cursor: MjAwMA==)...
2025-11-10 14:26:52,839 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 21
2025-11-10 14:26:52,840 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 22 (cursor: MjEwMA==)...
2025-11-10 14:26:53,496 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 22
2025-11-10 14:26:53,497 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 23 (cursor: MjIwMA==)...
2025-11-10 14:26:53,923 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 23
2025-11-10 14:26:53,924 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 24 (cursor: MjMwMA==)...
2025-11-10 14:26:55,364 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 24
2025-11-10 14:26:55,365 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 25 (cursor: MjQwMA==)...
2025-11-10 14:26:56,044 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 25
2025-11-10 14:26:56,045 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 26 (cursor: MjUwMA==)...
2025-11-10 14:26:56,691 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 26
2025-11-10 14:26:56,691 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 27 (cursor: MjYwMA==)...
2025-11-10 14:26:57,334 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 27
2025-11-10 14:26:57,334 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 28 (cursor: MjcwMA==)...
2025-11-10 14:26:57,770 - playwright_rewards_scraper - INFO - âœ… Got 14 markets on page 28
2025-11-10 14:26:57,770 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 29 (cursor: LTE=)...
2025-11-10 14:26:58,031 - playwright_rewards_scraper - INFO - âœ… No more markets on page 29
2025-11-10 14:26:58,032 - playwright_rewards_scraper - INFO - âœ… Fetched 2713 total unique markets from /rewards API
2025-11-10 14:26:58,078 - market_scanner_v2 - INFO - âœ… Got 2713 markets from /rewards page
2025-11-10 14:26:58,078 - market_scanner_v2 - INFO - âœ… ACCEPTED: Hang Seng (HSI) Up or Down on November 10?
2025-11-10 14:26:58,078 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:26:58,078 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$82)
2025-11-10 14:26:58,079 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:26:58,079 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-10 14:26:58,079 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:26:58,079 - market_scanner_v2 - INFO - âœ… ACCEPTED: DAX (DAX) Up or Down on November 10?
2025-11-10 14:26:58,079 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:26:58,079 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$7463)
2025-11-10 14:26:58,079 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:26:58,079 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.75
2025-11-10 14:26:58,079 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:26:58,079 - market_scanner_v2 - INFO - âœ… ACCEPTED: FTSE 100 (UKX) Up or Down on November 10?
2025-11-10 14:26:58,079 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:26:58,079 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$7424)
2025-11-10 14:26:58,079 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:26:58,079 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.74
2025-11-10 14:26:58,079 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:26:58,079 - market_scanner_v2 - INFO - âœ… ACCEPTED: Dow Jones (DJI) Up or Down on November 10?
2025-11-10 14:26:58,079 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:26:58,079 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$245)
2025-11-10 14:26:58,079 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:26:58,079 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.02
2025-11-10 14:26:58,079 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:26:58,079 - market_scanner_v2 - INFO - âœ… ACCEPTED: Nasdaq 100 (NDX) Up or Down on November 10?
2025-11-10 14:26:58,079 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:26:58,079 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$260)
2025-11-10 14:26:58,079 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:26:58,079 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.03
2025-11-10 14:26:58,080 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:26:58,080 - market_scanner_v2 - INFO - âœ… ACCEPTED: Nikkei 225 (NIK) Up or Down on November 10?
2025-11-10 14:26:58,080 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:26:58,080 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$76)
2025-11-10 14:26:58,080 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:26:58,080 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-10 14:26:58,080 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:26:58,080 - market_scanner_v2 - INFO - âœ… ACCEPTED: S&P 500 (SPX) Up or Down on November 10?
2025-11-10 14:26:58,080 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:26:58,080 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$79)
2025-11-10 14:26:58,080 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:26:58,080 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-10 14:26:58,080 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:26:58,080 - market_scanner_v2 - INFO - âœ… ACCEPTED: Airbnb (ABNB) Up or Down on November 10?
2025-11-10 14:26:58,080 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:26:58,080 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$31)
2025-11-10 14:26:58,080 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:26:58,080 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.00
2025-11-10 14:26:58,080 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:26:58,080 - market_scanner_v2 - INFO - âœ… ACCEPTED: Opendoor (OPEN) Up or Down on November 10?
2025-11-10 14:26:58,080 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:26:58,080 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$7420)
2025-11-10 14:26:58,080 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:26:58,080 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.74
2025-11-10 14:26:58,080 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:26:58,080 - market_scanner_v2 - INFO - âœ… ACCEPTED: Palantir (PLTR) Up or Down on November 10?
2025-11-10 14:26:58,080 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:26:58,080 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$6)
2025-11-10 14:26:58,081 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:26:58,081 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.00
2025-11-10 14:26:58,081 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:26:58,081 - market_scanner_v2 - INFO - âœ… ACCEPTED: Netflix (NFLX) Up or Down on November 10?
2025-11-10 14:26:58,081 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:26:58,081 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$50)
2025-11-10 14:26:58,081 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:26:58,081 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-10 14:26:58,081 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:26:58,081 - market_scanner_v2 - INFO - âœ… ACCEPTED: NVIDIA (NVDA) Up or Down on November 10?
2025-11-10 14:26:58,081 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:26:58,081 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$382)
2025-11-10 14:26:58,081 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:26:58,081 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.04
2025-11-10 14:26:58,081 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:26:58,081 - market_scanner_v2 - INFO - âœ… ACCEPTED: Tesla (TSLA) Up or Down on November 10?
2025-11-10 14:26:58,081 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:26:58,081 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$7454)
2025-11-10 14:26:58,081 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:26:58,081 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.75
2025-11-10 14:26:58,081 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:26:58,081 - market_scanner_v2 - INFO - âœ… ACCEPTED: Meta (META) Up or Down on November 10?
2025-11-10 14:26:58,081 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:26:58,081 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$1)
2025-11-10 14:26:58,081 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:26:58,081 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.00
2025-11-10 14:26:58,081 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:26:58,081 - market_scanner_v2 - INFO - âœ… ACCEPTED: Google (GOOGL) Up or Down on November 10?
2025-11-10 14:26:58,081 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:26:58,082 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$27)
2025-11-10 14:26:58,082 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:26:58,082 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.00
2025-11-10 14:26:58,082 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:26:58,082 - market_scanner_v2 - INFO - âœ… ACCEPTED: Amazon (AMZN) Up or Down on November 10?
2025-11-10 14:26:58,082 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:26:58,082 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$135)
2025-11-10 14:26:58,082 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:26:58,082 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-10 14:26:58,082 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:26:58,082 - market_scanner_v2 - INFO - âœ… ACCEPTED: Microsoft (MSFT) Up or Down on November 10?
2025-11-10 14:26:58,082 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:26:58,082 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$489)
2025-11-10 14:26:58,082 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:26:58,082 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.05
2025-11-10 14:26:58,082 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:26:58,082 - market_scanner_v2 - INFO - âœ… ACCEPTED: Apple (AAPL) Up or Down on November 10?
2025-11-10 14:26:58,082 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:26:58,082 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$119)
2025-11-10 14:26:58,082 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:26:58,082 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-10 14:26:58,082 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:26:58,085 - market_scanner_v2 - INFO - âœ… ACCEPTED: First to 5k: Gold or ETH?
2025-11-10 14:26:58,085 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-10 14:26:58,085 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$3771)
2025-11-10 14:26:58,086 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-10 14:26:58,086 - market_scanner_v2 - INFO -    - Competition: 1.305845 bars, Score: -120.21
2025-11-10 14:26:58,086 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-10 14:26:58,088 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 19/2713 markets passed
2025-11-10 14:26:58,088 - market_scanner_v2 - INFO -    - 2574 rejected: reward < $20
2025-11-10 14:26:58,088 - market_scanner_v2 - INFO -    - 75 rejected: competition > 3
2025-11-10 14:26:58,088 - market_scanner_v2 - INFO -    - 21 rejected: categorical event outcomes (event_slug != market_slug)
2025-11-10 14:26:58,088 - market_scanner_v2 - INFO -    - 24 rejected: volume = 0 (no liquidity)
2025-11-10 14:26:58,088 - market_scanner_v2 - INFO - ðŸ” Verifying orderbook for top 19 markets...
2025-11-10 14:27:02,205 - market_scanner_v2 - INFO -    Progress: 10/19 markets verified...
2025-11-10 14:27:05,822 - __main__ - WARNING - âš ï¸ Health check failed: 2 issues
2025-11-10 14:27:05,822 - __main__ - WARNING -    - ðŸ”´ KhÃ´ng quÃ©t markets trong 81s!
2025-11-10 14:27:05,822 - __main__ - WARNING -    - âš ï¸ API cháº­m: 27.3s trung bÃ¬nh
2025-11-10 14:27:07,612 - market_scanner_v2 - INFO -    - 19 markets rejected: no orderbook (no bids or asks)
2025-11-10 14:27:07,613 - market_scanner_v2 - INFO - âœ… Found 0 qualifying markets (from 2713 total)
2025-11-10 14:27:07,616 - market_selector - INFO - Selected 0 markets from 0 candidates
