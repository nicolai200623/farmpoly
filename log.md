2025-11-07 01:35:13,454 - __main__ - INFO - Shutdown signal received
2025-11-07 01:35:15,939 - __main__ - INFO - Shutting down bot...
2025-11-07 01:35:15,940 - order_manager - INFO - Cancelled 0 orders
2025-11-07 01:35:15,940 - __main__ - INFO - Bot shutdown complete
2025-11-07 01:36:44,303 - __main__ - INFO - âœ… Using MarketScannerV2 (Playwright + Gamma API)
2025-11-07 01:36:47,646 - __main__ - INFO - ðŸ“‚ Loading config from: config.yaml
2025-11-07 01:36:47,675 - __main__ - INFO - âœ… Config loaded successfully
2025-11-07 01:36:47,675 - __main__ - INFO -    - min_reward: 10
2025-11-07 01:36:47,675 - __main__ - INFO -    - max_competition_bars: 3
2025-11-07 01:36:47,675 - __main__ - INFO -    - interval: 60s
2025-11-07 01:36:47,675 - __main__ - INFO - âœ… Telegram alerts configured (Chat ID: -1003157421030)
2025-11-07 01:36:47,675 - __main__ - INFO - âœ… Webhook alerts configured
2025-11-07 01:36:47,675 - telegram_notifier - INFO - âœ… Telegram Notifier initialized (Chat ID: -1003157421030)
2025-11-07 01:36:47,675 - __main__ - INFO - âœ… Telegram Notifier initialized
2025-11-07 01:36:47,675 - market_scanner_v2 - INFO - ðŸ“Š Market Scanner initialized with min_reward=$10, max_competition=3
2025-11-07 01:36:47,675 - market_scanner_v2 - INFO - ðŸŽ¯ Target categories: crypto, sports, politics, science, entertainment
2025-11-07 01:36:47,675 - circuit_breaker - INFO - âœ… Circuit Breaker 'playwright_scraper' initialized (threshold=3, timeout=60s)
2025-11-07 01:36:47,675 - circuit_breaker - INFO - âœ… Circuit Breaker 'playwright_scraper' initialized (threshold=3, timeout=120s)
2025-11-07 01:36:47,675 - order_manager - INFO - CLOB client initialized successfully (read-only mode)
2025-11-07 01:36:47,684 - wallet_manager - INFO - Loading REAL wallets from .env
2025-11-07 01:36:47,690 - wallet_manager - INFO - âœ… Loaded wallet 1: 0x18F261DC...Ae4FfD96
2025-11-07 01:36:47,690 - wallet_manager - INFO - âœ… Successfully loaded 1 real wallets
2025-11-07 01:36:47,697 - ml_predictor - INFO - No pre-trained model found, using new model
2025-11-07 01:36:47,698 - monitoring_system - INFO - âœ… Monitoring System initialized
2025-11-07 01:36:47,699 - __main__ - INFO - âœ… Monitoring System enabled
2025-11-07 01:36:47,699 - __main__ - INFO - â­ï¸  Reward Manager disabled in config
2025-11-07 01:36:48,404 - profit_taking_manager - INFO - âœ… CLOB client initialized with API credentials
2025-11-07 01:36:48,405 - profit_taking_manager - INFO - âœ… Profit Taking Manager initialized
2025-11-07 01:36:48,405 - profit_taking_manager - INFO -    - Min profit: 5%
2025-11-07 01:36:48,405 - profit_taking_manager - INFO -    - Target profit: 10%
2025-11-07 01:36:48,405 - profit_taking_manager - INFO -    - Max profit: 150%
2025-11-07 01:36:48,405 - profit_taking_manager - INFO -    - Check interval: 300s
2025-11-07 01:36:48,405 - __main__ - INFO - âœ… Profit Taking Manager enabled
2025-11-07 01:36:48,405 - __main__ - INFO - All modules initialized successfully
2025-11-07 01:36:48,405 - __main__ - INFO - ðŸš€ Starting Polymarket Trading Bot...
2025-11-07 01:36:49,373 - __main__ - INFO - âœ… Startup alert sent via TelegramNotifier
2025-11-07 01:36:49,373 - __main__ - INFO - ðŸ” Checking USDC approval for wallets...
2025-11-07 01:36:49,594 - usdc_approver - INFO - âœ… Connected to Polygon RPC: https://polygon-mainnet.g.alchemy.com/v2/FQJnJWsEQ...
2025-11-07 01:36:49,594 - __main__ - INFO -    Checking wallet: 0x18F261DC...Ae4FfD96
2025-11-07 01:36:49,959 - __main__ - INFO -    Raw allowance: 100000000 (base units)
2025-11-07 01:36:49,960 - __main__ - INFO -    Allowance in USDC: 100.00 USDC
2025-11-07 01:36:49,960 - __main__ - INFO -    Required minimum: 100 USDC (test mode)
2025-11-07 01:36:49,960 - __main__ - INFO - âœ… USDC approval OK (100 USDC)
2025-11-07 01:36:49,960 - __main__ - WARNING -    âš ï¸  Running in TEST MODE with 100 USDC
2025-11-07 01:36:49,960 - __main__ - WARNING -    For production, approve at least 1,000 USDC
2025-11-07 01:36:49,960 - __main__ - INFO - ðŸ” Starting market scanning loop
2025-11-07 01:36:49,960 - market_scanner_v2 - INFO - ðŸŒ Scraping markets from /rewards page using Playwright...
2025-11-07 01:36:49,960 - playwright_rewards_scraper - INFO - ðŸŒ Fetching markets from /rewards API...
2025-11-07 01:36:49,961 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 1 (cursor: MA==)...
2025-11-07 01:36:49,961 - __main__ - INFO - ðŸ“¦ Starting order management loop
2025-11-07 01:36:49,961 - __main__ - INFO - ðŸ‘ï¸  Starting position monitoring loop
2025-11-07 01:36:49,961 - __main__ - INFO - ðŸ›¡ï¸  Starting risk management loop
2025-11-07 01:36:49,961 - __main__ - INFO - ðŸ¤– Starting ML training loop
2025-11-07 01:36:49,961 - ml_predictor - INFO - Insufficient training data: 0 samples
2025-11-07 01:36:49,961 - __main__ - INFO - ML model updated successfully
2025-11-07 01:36:49,961 - __main__ - INFO - ðŸ“Š Starting daily optimization loop
2025-11-07 01:36:49,962 - __main__ - INFO - ðŸ¥ Starting health monitoring loop
2025-11-07 01:36:50,964 - __main__ - INFO - ðŸ“ˆ Starting hourly report loop
2025-11-07 01:36:50,964 - __main__ - INFO - ðŸ’° Starting automated profit taking loop
2025-11-07 01:36:50,964 - profit_taking_manager - INFO - ðŸ” Checking positions for wallet: 0x18F261DC...Ae4FfD96
2025-11-07 01:36:51,295 - profit_taking_manager - INFO - ðŸ“Š Found 3 active positions
2025-11-07 01:36:51,295 - profit_taking_manager - INFO - 
ðŸ“ˆ Position: Charlotte 49ers vs. East Carolina
2025-11-07 01:36:51,295 - profit_taking_manager - INFO -    Shares: 259.00 @ $0.1494
2025-11-07 01:36:51,295 - profit_taking_manager - INFO -    Current: $0.0385
2025-11-07 01:36:51,295 - profit_taking_manager - INFO -    P&L: $-28.73 (-74.23%)
2025-11-07 01:36:51,295 - profit_taking_manager - INFO -    â¸ï¸  Losing position - NOT closing (manual decision required)
2025-11-07 01:36:51,295 - profit_taking_manager - INFO - 
ðŸ“ˆ Position: Will Google Gemini 3 score at least 70% on the Fro
2025-11-07 01:36:51,295 - profit_taking_manager - INFO -    Shares: 68.00 @ $0.3900
2025-11-07 01:36:51,296 - profit_taking_manager - INFO -    Current: $0.0700
2025-11-07 01:36:51,296 - profit_taking_manager - INFO -    P&L: $-21.76 (-82.05%)
2025-11-07 01:36:51,296 - profit_taking_manager - INFO -    â¸ï¸  Losing position - NOT closing (manual decision required)
2025-11-07 01:36:51,296 - profit_taking_manager - INFO - 
ðŸ“ˆ Position: Syracuse vs. Miami
2025-11-07 01:36:51,296 - profit_taking_manager - INFO -    Shares: 66.00 @ $0.4900
2025-11-07 01:36:51,296 - profit_taking_manager - INFO -    Current: $0.0580
2025-11-07 01:36:51,296 - profit_taking_manager - INFO -    P&L: $-28.51 (-88.16%)
2025-11-07 01:36:51,296 - profit_taking_manager - INFO -    â¸ï¸  Losing position - NOT closing (manual decision required)
2025-11-07 01:36:51,296 - __main__ - INFO - â³ Next profit check in 300s
2025-11-07 01:36:51,956 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 1
2025-11-07 01:36:51,957 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 2 (cursor: MTAw)...
2025-11-07 01:36:52,722 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 2
2025-11-07 01:36:52,722 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 3 (cursor: MjAw)...
2025-11-07 01:36:53,150 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 3
2025-11-07 01:36:53,151 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 4 (cursor: MzAw)...
2025-11-07 01:36:53,572 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 4
2025-11-07 01:36:53,573 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 5 (cursor: NDAw)...
2025-11-07 01:36:54,011 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 5
2025-11-07 01:36:54,012 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 6 (cursor: NTAw)...
2025-11-07 01:36:54,662 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 6
2025-11-07 01:36:54,663 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 7 (cursor: NjAw)...
2025-11-07 01:36:55,344 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 7
2025-11-07 01:36:55,345 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 8 (cursor: NzAw)...
2025-11-07 01:36:55,996 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 8
2025-11-07 01:36:55,996 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 9 (cursor: ODAw)...
2025-11-07 01:36:56,693 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 9
2025-11-07 01:36:56,694 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 10 (cursor: OTAw)...
2025-11-07 01:36:57,362 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 10
2025-11-07 01:36:57,363 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 11 (cursor: MTAwMA==)...
2025-11-07 01:36:57,846 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 11
2025-11-07 01:36:57,846 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 12 (cursor: MTEwMA==)...
2025-11-07 01:36:58,514 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 12
2025-11-07 01:36:58,515 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 13 (cursor: MTIwMA==)...
2025-11-07 01:36:59,186 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 13
2025-11-07 01:36:59,186 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 14 (cursor: MTMwMA==)...
2025-11-07 01:36:59,629 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 14
2025-11-07 01:36:59,630 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 15 (cursor: MTQwMA==)...
2025-11-07 01:37:00,072 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 15
2025-11-07 01:37:00,073 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 16 (cursor: MTUwMA==)...
2025-11-07 01:37:00,519 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 16
2025-11-07 01:37:00,519 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 17 (cursor: MTYwMA==)...
2025-11-07 01:37:01,172 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 17
2025-11-07 01:37:01,173 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 18 (cursor: MTcwMA==)...
2025-11-07 01:37:01,868 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 18
2025-11-07 01:37:01,868 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 19 (cursor: MTgwMA==)...
2025-11-07 01:37:02,526 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 19
2025-11-07 01:37:02,527 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 20 (cursor: MTkwMA==)...
2025-11-07 01:37:03,176 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 20
2025-11-07 01:37:03,177 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 21 (cursor: MjAwMA==)...
2025-11-07 01:37:03,854 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 21
2025-11-07 01:37:03,854 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 22 (cursor: MjEwMA==)...
2025-11-07 01:37:04,523 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 22
2025-11-07 01:37:04,523 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 23 (cursor: MjIwMA==)...
2025-11-07 01:37:05,206 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 23
2025-11-07 01:37:05,207 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 24 (cursor: MjMwMA==)...
2025-11-07 01:37:05,862 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 24
2025-11-07 01:37:05,862 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 25 (cursor: MjQwMA==)...
2025-11-07 01:37:06,286 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 25
2025-11-07 01:37:06,287 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 26 (cursor: MjUwMA==)...
2025-11-07 01:37:06,929 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 26
2025-11-07 01:37:06,930 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 27 (cursor: MjYwMA==)...
2025-11-07 01:37:07,592 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 27
2025-11-07 01:37:07,592 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 28 (cursor: MjcwMA==)...
2025-11-07 01:37:08,227 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 28
2025-11-07 01:37:08,227 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 29 (cursor: MjgwMA==)...
2025-11-07 01:37:08,664 - playwright_rewards_scraper - INFO - âœ… Got 42 markets on page 29
2025-11-07 01:37:08,665 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 30 (cursor: LTE=)...
2025-11-07 01:37:08,926 - playwright_rewards_scraper - INFO - âœ… No more markets on page 30
2025-11-07 01:37:08,927 - playwright_rewards_scraper - INFO - âœ… Fetched 2840 total unique markets from /rewards API
2025-11-07 01:37:08,976 - market_scanner_v2 - INFO - âœ… Got 2840 markets from /rewards page
2025-11-07 01:37:08,976 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Kanye visit Israel by December 31?
2025-11-07 01:37:08,976 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:37:08,976 - market_scanner_v2 - INFO -    - Estimated Reward: $50 (based on volume=$64)
2025-11-07 01:37:08,976 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,976 - market_scanner_v2 - INFO -    - Competition: 0.539847 bars, Score: -28.98
2025-11-07 01:37:08,976 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,976 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Ukraine win Miss Universe 2025?
2025-11-07 01:37:08,976 - market_scanner_v2 - INFO -    - Category: science
2025-11-07 01:37:08,976 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$61)
2025-11-07 01:37:08,976 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,976 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.01
2025-11-07 01:37:08,976 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,977 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will China win Miss Universe 2025?
2025-11-07 01:37:08,977 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:37:08,977 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$66)
2025-11-07 01:37:08,977 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,977 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.01
2025-11-07 01:37:08,977 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,977 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Great Britain win Miss Universe 2025?
2025-11-07 01:37:08,977 - market_scanner_v2 - INFO -    - Category: science
2025-11-07 01:37:08,977 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$66)
2025-11-07 01:37:08,977 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,977 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.01
2025-11-07 01:37:08,977 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,977 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Spain win Miss Universe 2025?
2025-11-07 01:37:08,977 - market_scanner_v2 - INFO -    - Category: science
2025-11-07 01:37:08,977 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$66)
2025-11-07 01:37:08,977 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,977 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.01
2025-11-07 01:37:08,977 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,977 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel win Miss Universe 2025?
2025-11-07 01:37:08,977 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:37:08,977 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$66)
2025-11-07 01:37:08,977 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,977 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.01
2025-11-07 01:37:08,977 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,977 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Russia win Miss Universe 2025?
2025-11-07 01:37:08,977 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:37:08,978 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$61)
2025-11-07 01:37:08,978 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,978 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.01
2025-11-07 01:37:08,978 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,978 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Palestine win Miss Universe 2025?
2025-11-07 01:37:08,978 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:37:08,978 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$66)
2025-11-07 01:37:08,978 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,978 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.01
2025-11-07 01:37:08,978 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,978 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Howard Hughes Holdings (HHH) beat quarterly earnings?
2025-11-07 01:37:08,978 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:37:08,978 - market_scanner_v2 - INFO -    - Estimated Reward: $50 (based on volume=$110)
2025-11-07 01:37:08,978 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,978 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 25.01
2025-11-07 01:37:08,978 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,978 - market_scanner_v2 - INFO - âœ… ACCEPTED: Airbnb (ABNB) Up or Down on November 7?
2025-11-07 01:37:08,978 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:37:08,978 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$687)
2025-11-07 01:37:08,978 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,978 - market_scanner_v2 - INFO -    - Competition: 0.136 bars, Score: -3.53
2025-11-07 01:37:08,978 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,978 - market_scanner_v2 - INFO - âœ… ACCEPTED: Palantir (PLTR) Up or Down on November 7?
2025-11-07 01:37:08,978 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:37:08,978 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$30)
2025-11-07 01:37:08,978 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,979 - market_scanner_v2 - INFO -    - Competition: 1.260037 bars, Score: -116.00
2025-11-07 01:37:08,979 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,979 - market_scanner_v2 - INFO - âœ… ACCEPTED: NVIDIA (NVDA) Up or Down on November 7?
2025-11-07 01:37:08,979 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:37:08,979 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$71)
2025-11-07 01:37:08,979 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,979 - market_scanner_v2 - INFO -    - Competition: 0.29784 bars, Score: -19.78
2025-11-07 01:37:08,979 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,979 - market_scanner_v2 - INFO - âœ… ACCEPTED: Hang Seng (HSI) Up or Down on November 7?
2025-11-07 01:37:08,979 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:37:08,979 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$51)
2025-11-07 01:37:08,979 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,979 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-07 01:37:08,979 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,979 - market_scanner_v2 - INFO - âœ… ACCEPTED: Tesla (TSLA) Up or Down on November 7?
2025-11-07 01:37:08,979 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:37:08,979 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$184)
2025-11-07 01:37:08,979 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,979 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.02
2025-11-07 01:37:08,979 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,979 - market_scanner_v2 - INFO - âœ… ACCEPTED: DAX (DAX) Up or Down on November 7?
2025-11-07 01:37:08,979 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:37:08,979 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$24)
2025-11-07 01:37:08,979 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,979 - market_scanner_v2 - INFO -    - Competition: 0.765417 bars, Score: -66.54
2025-11-07 01:37:08,979 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,980 - market_scanner_v2 - INFO - âœ… ACCEPTED: FTSE 100 (UKX) Up or Down on November 7?
2025-11-07 01:37:08,980 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:37:08,980 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$150)
2025-11-07 01:37:08,980 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,980 - market_scanner_v2 - INFO -    - Competition: 0.765417 bars, Score: -66.53
2025-11-07 01:37:08,980 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,980 - market_scanner_v2 - INFO - âœ… ACCEPTED: Meta (META) Up or Down on November 7?
2025-11-07 01:37:08,980 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:37:08,980 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2)
2025-11-07 01:37:08,980 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,980 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.00
2025-11-07 01:37:08,980 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,980 - market_scanner_v2 - INFO - âœ… ACCEPTED: Dow Jones (DJI) Up or Down on November 7?
2025-11-07 01:37:08,980 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:37:08,980 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2)
2025-11-07 01:37:08,980 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,980 - market_scanner_v2 - INFO -    - Competition: 1.224667 bars, Score: -112.47
2025-11-07 01:37:08,980 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,980 - market_scanner_v2 - INFO - âœ… ACCEPTED: Google (GOOGL) Up or Down on November 7?
2025-11-07 01:37:08,980 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:37:08,980 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2)
2025-11-07 01:37:08,980 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,980 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.00
2025-11-07 01:37:08,980 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,980 - market_scanner_v2 - INFO - âœ… ACCEPTED: Amazon (AMZN) Up or Down on November 7?
2025-11-07 01:37:08,980 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:37:08,980 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$108)
2025-11-07 01:37:08,981 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,981 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-07 01:37:08,981 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,981 - market_scanner_v2 - INFO - âœ… ACCEPTED: Nasdaq 100 (NDX) Up or Down on November 7?
2025-11-07 01:37:08,981 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:37:08,981 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$64)
2025-11-07 01:37:08,981 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,981 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-07 01:37:08,981 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,981 - market_scanner_v2 - INFO - âœ… ACCEPTED: Microsoft (MSFT) Up or Down on November 7?
2025-11-07 01:37:08,981 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:37:08,981 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$150)
2025-11-07 01:37:08,981 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,981 - market_scanner_v2 - INFO -    - Competition: 0.820527 bars, Score: -72.04
2025-11-07 01:37:08,981 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,981 - market_scanner_v2 - INFO - âœ… ACCEPTED: Nikkei 225 (NIK) Up or Down on November 7?
2025-11-07 01:37:08,981 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:37:08,981 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$56)
2025-11-07 01:37:08,981 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,981 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-07 01:37:08,981 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,981 - market_scanner_v2 - INFO - âœ… ACCEPTED: COMEX Gold Futures (GC=F) Up or Down on November 7?
2025-11-07 01:37:08,981 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:37:08,981 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$4)
2025-11-07 01:37:08,981 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,981 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.00
2025-11-07 01:37:08,981 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,981 - market_scanner_v2 - INFO - âœ… ACCEPTED: S&P 500 (SPX) Up or Down on November 7?
2025-11-07 01:37:08,982 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:37:08,982 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$187)
2025-11-07 01:37:08,982 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,982 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.02
2025-11-07 01:37:08,982 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,982 - market_scanner_v2 - INFO - âœ… ACCEPTED: Apple (AAPL) Up or Down on November 7?
2025-11-07 01:37:08,982 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:37:08,982 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$12)
2025-11-07 01:37:08,982 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,982 - market_scanner_v2 - INFO -    - Competition: 0.051 bars, Score: 4.90
2025-11-07 01:37:08,982 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,982 - market_scanner_v2 - INFO - âœ… ACCEPTED: Consensys IPO closing market cap above $3B?
2025-11-07 01:37:08,982 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:37:08,982 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$660)
2025-11-07 01:37:08,982 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,982 - market_scanner_v2 - INFO -    - Competition: 2.756071 bars, Score: -265.54
2025-11-07 01:37:08,982 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,982 - market_scanner_v2 - INFO - âœ… ACCEPTED: Trump announces new drug boat strike by November 7?
2025-11-07 01:37:08,982 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:37:08,982 - market_scanner_v2 - INFO -    - Estimated Reward: $15 (based on volume=$6592)
2025-11-07 01:37:08,982 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,982 - market_scanner_v2 - INFO -    - Competition: 1.481333 bars, Score: -139.97
2025-11-07 01:37:08,982 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,982 - market_scanner_v2 - INFO - âœ… ACCEPTED: Trump announces new drug boat strike by November 14?
2025-11-07 01:37:08,982 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:37:08,983 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$11390)
2025-11-07 01:37:08,983 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,983 - market_scanner_v2 - INFO -    - Competition: 0.823877 bars, Score: -76.25
2025-11-07 01:37:08,983 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,983 - market_scanner_v2 - INFO - âœ… ACCEPTED: NYMEX Crude Oil Futures (WTI) (CL=F) Up or Down on November 
2025-11-07 01:37:08,983 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:37:08,983 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2243)
2025-11-07 01:37:08,983 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,983 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.22
2025-11-07 01:37:08,983 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,983 - market_scanner_v2 - INFO - âœ… ACCEPTED: COMEX Silver Futures (SI=F) Up or Down on November 6?
2025-11-07 01:37:08,983 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:37:08,983 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$735)
2025-11-07 01:37:08,983 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,983 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.07
2025-11-07 01:37:08,983 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,983 - market_scanner_v2 - INFO - âœ… ACCEPTED: COMEX Gold Futures (GC=F) Up or Down on November 6?
2025-11-07 01:37:08,983 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:37:08,983 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$855)
2025-11-07 01:37:08,983 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,983 - market_scanner_v2 - INFO -    - Competition: 2.429 bars, Score: -232.81
2025-11-07 01:37:08,983 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,984 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Catalin Drula finish second in the 2025 Bucharest mayor
2025-11-07 01:37:08,984 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:37:08,984 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$709)
2025-11-07 01:37:08,984 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,984 - market_scanner_v2 - INFO -    - Competition: 0.760555 bars, Score: -70.98
2025-11-07 01:37:08,984 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,984 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Google Gemini 3 score at least 40% on Humanityâ€™s Last E
2025-11-07 01:37:08,984 - market_scanner_v2 - INFO -    - Category: science
2025-11-07 01:37:08,984 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$1131)
2025-11-07 01:37:08,984 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,984 - market_scanner_v2 - INFO -    - Competition: 2.727311 bars, Score: -262.62
2025-11-07 01:37:08,984 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,984 - market_scanner_v2 - INFO - âœ… ACCEPTED: U.S. Closes Airspace due to Government Shutdown?
2025-11-07 01:37:08,984 - market_scanner_v2 - INFO -    - Category: science
2025-11-07 01:37:08,984 - market_scanner_v2 - INFO -    - Estimated Reward: $50 (based on volume=$14330)
2025-11-07 01:37:08,984 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,984 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 26.43
2025-11-07 01:37:08,984 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,984 - market_scanner_v2 - INFO - âœ… ACCEPTED: NYMEX Crude Oil Futures (WTI) (CL=F) Up or Down on November 
2025-11-07 01:37:08,984 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:37:08,984 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$130)
2025-11-07 01:37:08,985 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,985 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-07 01:37:08,985 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,985 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Asia" or "Asian" 8+ times during C5+1 Summit
2025-11-07 01:37:08,985 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:37:08,985 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$7842)
2025-11-07 01:37:08,985 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,985 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.78
2025-11-07 01:37:08,985 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,985 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Million" or "Billion" or "Trillion" 12+ time
2025-11-07 01:37:08,985 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:37:08,985 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$6712)
2025-11-07 01:37:08,985 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,985 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.67
2025-11-07 01:37:08,985 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,985 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Thank you" 8+ times during C5+1 Summit on No
2025-11-07 01:37:08,985 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:37:08,985 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$8507)
2025-11-07 01:37:08,985 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,985 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.85
2025-11-07 01:37:08,985 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,985 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Biden" or "Obama" 4+ times during C5+1 Summi
2025-11-07 01:37:08,985 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:37:08,985 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$4101)
2025-11-07 01:37:08,985 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,985 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.41
2025-11-07 01:37:08,985 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,986 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Russia" or "China" 4+ times during C5+1 Summ
2025-11-07 01:37:08,986 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:37:08,986 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$7641)
2025-11-07 01:37:08,986 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,986 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.76
2025-11-07 01:37:08,986 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,986 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Nuclear" 2+ times during C5+1 Summit on Nove
2025-11-07 01:37:08,986 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:37:08,986 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$2305)
2025-11-07 01:37:08,986 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,986 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.23
2025-11-07 01:37:08,986 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,986 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Caspian Sea" during C5+1 Summit on November 
2025-11-07 01:37:08,986 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:37:08,986 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$6274)
2025-11-07 01:37:08,986 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,986 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.63
2025-11-07 01:37:08,986 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,986 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Boeing" during C5+1 Summit on November 6?
2025-11-07 01:37:08,986 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:37:08,986 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$4640)
2025-11-07 01:37:08,986 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,986 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.46
2025-11-07 01:37:08,986 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,986 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Rare Earth" or "Critical Mineral" during C5+
2025-11-07 01:37:08,986 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:37:08,986 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$8309)
2025-11-07 01:37:08,986 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,987 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.83
2025-11-07 01:37:08,987 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,987 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Energy" during C5+1 Summit on November 6?
2025-11-07 01:37:08,987 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:37:08,987 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$9825)
2025-11-07 01:37:08,987 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,987 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.98
2025-11-07 01:37:08,987 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,987 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Drug" during C5+1 Summit on November 6?
2025-11-07 01:37:08,987 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:37:08,987 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$2410)
2025-11-07 01:37:08,987 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,987 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.24
2025-11-07 01:37:08,987 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,987 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Soviet" during C5+1 Summit on November 6?
2025-11-07 01:37:08,987 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:37:08,987 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$3623)
2025-11-07 01:37:08,987 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,987 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.36
2025-11-07 01:37:08,987 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,987 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Best Equipment" during C5+1 Summit on Novemb
2025-11-07 01:37:08,987 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:37:08,987 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$548)
2025-11-07 01:37:08,987 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,987 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.05
2025-11-07 01:37:08,987 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,987 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Investment" during C5+1 Summit on November 6
2025-11-07 01:37:08,988 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:37:08,988 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$3839)
2025-11-07 01:37:08,988 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,988 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.38
2025-11-07 01:37:08,988 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,988 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Middle East" during C5+1 Summit on November 
2025-11-07 01:37:08,988 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:37:08,988 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$150)
2025-11-07 01:37:08,988 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,988 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.01
2025-11-07 01:37:08,988 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,988 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Azerbaijan" during C5+1 Summit on November 6
2025-11-07 01:37:08,988 - market_scanner_v2 - INFO -    - Category: science
2025-11-07 01:37:08,988 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$2317)
2025-11-07 01:37:08,988 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,988 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.23
2025-11-07 01:37:08,988 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,988 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "President Xi" during C5+1 Summit on November
2025-11-07 01:37:08,988 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:37:08,988 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$2352)
2025-11-07 01:37:08,988 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,988 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.24
2025-11-07 01:37:08,988 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,988 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Afghanistan" during C5+1 Summit on November 
2025-11-07 01:37:08,988 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:37:08,988 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$820)
2025-11-07 01:37:08,989 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,989 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.08
2025-11-07 01:37:08,989 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,989 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Eight wars" during C5+1 Summit on November 6
2025-11-07 01:37:08,989 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:37:08,989 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$3294)
2025-11-07 01:37:08,989 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,989 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.33
2025-11-07 01:37:08,989 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,989 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Dead Country" during C5+1 Summit on November
2025-11-07 01:37:08,989 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:37:08,989 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$3079)
2025-11-07 01:37:08,989 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,989 - market_scanner_v2 - INFO -    - Competition: 1.701 bars, Score: -164.79
2025-11-07 01:37:08,989 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,989 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Crypto" or "AI" during C5+1 Summit on Novemb
2025-11-07 01:37:08,989 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:37:08,989 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$6332)
2025-11-07 01:37:08,989 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,989 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.63
2025-11-07 01:37:08,989 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,989 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Claude pass Grok by November 15 on the UnifAI Polyarena
2025-11-07 01:37:08,989 - market_scanner_v2 - INFO -    - Category: science
2025-11-07 01:37:08,989 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$462)
2025-11-07 01:37:08,989 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,989 - market_scanner_v2 - INFO -    - Competition: 1.088 bars, Score: -103.75
2025-11-07 01:37:08,989 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,990 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Airbnb (ABNB) finish week of November 10 above $115?
2025-11-07 01:37:08,990 - market_scanner_v2 - INFO -    - Category: science
2025-11-07 01:37:08,990 - market_scanner_v2 - INFO -    - Estimated Reward: $15 (based on volume=$50)
2025-11-07 01:37:08,990 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,990 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 7.51
2025-11-07 01:37:08,990 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,990 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Airbnb (ABNB) finish week of November 10 above $125?
2025-11-07 01:37:08,990 - market_scanner_v2 - INFO -    - Category: science
2025-11-07 01:37:08,990 - market_scanner_v2 - INFO -    - Estimated Reward: $15 (based on volume=$694)
2025-11-07 01:37:08,990 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,990 - market_scanner_v2 - INFO -    - Competition: 0.10988 bars, Score: -3.42
2025-11-07 01:37:08,990 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,990 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Airbnb (ABNB) finish week of November 10 above $135?
2025-11-07 01:37:08,990 - market_scanner_v2 - INFO -    - Category: science
2025-11-07 01:37:08,990 - market_scanner_v2 - INFO -    - Estimated Reward: $15 (based on volume=$20)
2025-11-07 01:37:08,990 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,990 - market_scanner_v2 - INFO -    - Competition: 2.159934 bars, Score: -208.49
2025-11-07 01:37:08,990 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,990 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Netflix (NFLX) finish week of November 10 above $1,070?
2025-11-07 01:37:08,990 - market_scanner_v2 - INFO -    - Category: entertainment
2025-11-07 01:37:08,990 - market_scanner_v2 - INFO -    - Estimated Reward: $15 (based on volume=$150)
2025-11-07 01:37:08,990 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,990 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 7.51
2025-11-07 01:37:08,990 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,991 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Airbnb (ABNB) close above $140 end of November?
2025-11-07 01:37:08,991 - market_scanner_v2 - INFO -    - Category: science
2025-11-07 01:37:08,991 - market_scanner_v2 - INFO -    - Estimated Reward: $15 (based on volume=$104)
2025-11-07 01:37:08,991 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,991 - market_scanner_v2 - INFO -    - Competition: 1.60472 bars, Score: -152.96
2025-11-07 01:37:08,991 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,991 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Netflix (NFLX) close above $1,080 end of November?
2025-11-07 01:37:08,991 - market_scanner_v2 - INFO -    - Category: entertainment
2025-11-07 01:37:08,991 - market_scanner_v2 - INFO -    - Estimated Reward: $15 (based on volume=$125)
2025-11-07 01:37:08,991 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,991 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 7.51
2025-11-07 01:37:08,991 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,992 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Microstrategy announce a Bitcoin purchase November 4-10
2025-11-07 01:37:08,992 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:37:08,992 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$10868)
2025-11-07 01:37:08,992 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,992 - market_scanner_v2 - INFO -    - Competition: 1.075971 bars, Score: -101.51
2025-11-07 01:37:08,992 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,992 - market_scanner_v2 - INFO - âœ… ACCEPTED: Hezbollah strike on Israel by December 31?
2025-11-07 01:37:08,992 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:37:08,992 - market_scanner_v2 - INFO -    - Estimated Reward: $50 (based on volume=$14904)
2025-11-07 01:37:08,992 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,992 - market_scanner_v2 - INFO -    - Competition: 1.250694 bars, Score: -98.58
2025-11-07 01:37:08,992 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,992 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Airbnb reach $136 in November?
2025-11-07 01:37:08,992 - market_scanner_v2 - INFO -    - Category: science
2025-11-07 01:37:08,992 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$5)
2025-11-07 01:37:08,992 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,992 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.00
2025-11-07 01:37:08,992 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,993 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Lebanon on November 7?
2025-11-07 01:37:08,993 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:37:08,993 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$11321)
2025-11-07 01:37:08,993 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,993 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 11.13
2025-11-07 01:37:08,993 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,993 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Lebanon on November 8?
2025-11-07 01:37:08,993 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:37:08,993 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2258)
2025-11-07 01:37:08,993 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,993 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.23
2025-11-07 01:37:08,993 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,993 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Lebanon on November 11?
2025-11-07 01:37:08,993 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:37:08,993 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$906)
2025-11-07 01:37:08,993 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,993 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.09
2025-11-07 01:37:08,994 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,994 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Lebanon on November 12?
2025-11-07 01:37:08,994 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:37:08,994 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$609)
2025-11-07 01:37:08,994 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,994 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.06
2025-11-07 01:37:08,994 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,994 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Lebanon on November 13?
2025-11-07 01:37:08,994 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:37:08,994 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$491)
2025-11-07 01:37:08,994 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,994 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.05
2025-11-07 01:37:08,994 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,994 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Lebanon on November 14?
2025-11-07 01:37:08,994 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:37:08,994 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$1346)
2025-11-07 01:37:08,994 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,994 - market_scanner_v2 - INFO -    - Competition: 0.790598 bars, Score: -68.93
2025-11-07 01:37:08,994 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,994 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Gaza on November 7?
2025-11-07 01:37:08,994 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:37:08,994 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$1948)
2025-11-07 01:37:08,994 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,994 - market_scanner_v2 - INFO -    - Competition: 2.6611 bars, Score: -255.92
2025-11-07 01:37:08,994 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,994 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Gaza on November 8?
2025-11-07 01:37:08,995 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:37:08,995 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$702)
2025-11-07 01:37:08,995 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,995 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.07
2025-11-07 01:37:08,995 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,995 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Gaza on November 9?
2025-11-07 01:37:08,995 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:37:08,995 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$205)
2025-11-07 01:37:08,995 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,995 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.02
2025-11-07 01:37:08,995 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,995 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Gaza on November 10?
2025-11-07 01:37:08,995 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:37:08,995 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$279)
2025-11-07 01:37:08,995 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,995 - market_scanner_v2 - INFO -    - Competition: 2.916227 bars, Score: -281.59
2025-11-07 01:37:08,995 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,995 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Gaza on November 11?
2025-11-07 01:37:08,995 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:37:08,995 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$58)
2025-11-07 01:37:08,995 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,995 - market_scanner_v2 - INFO -    - Competition: 1.922306 bars, Score: -182.22
2025-11-07 01:37:08,995 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,995 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Gaza on November 14?
2025-11-07 01:37:08,995 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:37:08,995 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$265)
2025-11-07 01:37:08,995 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,996 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.03
2025-11-07 01:37:08,996 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,996 - market_scanner_v2 - INFO - âœ… ACCEPTED: Park Sung-jae in jail by November 30?
2025-11-07 01:37:08,996 - market_scanner_v2 - INFO -    - Category: science
2025-11-07 01:37:08,996 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$3469)
2025-11-07 01:37:08,996 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,996 - market_scanner_v2 - INFO -    - Competition: 1.202566 bars, Score: -114.91
2025-11-07 01:37:08,996 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,996 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Elon Musk post 140-159 tweets from October 31 to Novemb
2025-11-07 01:37:08,996 - market_scanner_v2 - INFO -    - Category: entertainment
2025-11-07 01:37:08,996 - market_scanner_v2 - INFO -    - Estimated Reward: $200 (based on volume=$225332)
2025-11-07 01:37:08,996 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,996 - market_scanner_v2 - INFO -    - Competition: 0.143511 bars, Score: 108.18
2025-11-07 01:37:08,996 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,996 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Elon Musk post 160-179 tweets from October 31 to Novemb
2025-11-07 01:37:08,996 - market_scanner_v2 - INFO -    - Category: entertainment
2025-11-07 01:37:08,996 - market_scanner_v2 - INFO -    - Estimated Reward: $130 (based on volume=$164904)
2025-11-07 01:37:08,996 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,996 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 81.49
2025-11-07 01:37:08,996 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,996 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Elon Musk post 180-199 tweets from October 31 to Novemb
2025-11-07 01:37:08,996 - market_scanner_v2 - INFO -    - Category: entertainment
2025-11-07 01:37:08,996 - market_scanner_v2 - INFO -    - Estimated Reward: $30 (based on volume=$161389)
2025-11-07 01:37:08,996 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,996 - market_scanner_v2 - INFO -    - Competition: 2.750939 bars, Score: -243.96
2025-11-07 01:37:08,997 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,997 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Stable launch a token in 2025?
2025-11-07 01:37:08,997 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:37:08,997 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$211226)
2025-11-07 01:37:08,997 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,997 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 26.12
2025-11-07 01:37:08,997 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,998 - market_scanner_v2 - INFO - âœ… ACCEPTED: Canton FDV above $3B one day after launch?
2025-11-07 01:37:08,998 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:37:08,998 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$1115)
2025-11-07 01:37:08,998 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,998 - market_scanner_v2 - INFO -    - Competition: 2.546799 bars, Score: -244.57
2025-11-07 01:37:08,998 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,998 - market_scanner_v2 - INFO - âœ… ACCEPTED: Canton FDV above $5B one day after launch?
2025-11-07 01:37:08,998 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:37:08,998 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$857)
2025-11-07 01:37:08,998 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,998 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.09
2025-11-07 01:37:08,998 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,998 - market_scanner_v2 - INFO - âœ… ACCEPTED: Canton FDV above $10B one day after launch?
2025-11-07 01:37:08,998 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:37:08,998 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$725)
2025-11-07 01:37:08,998 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,998 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.07
2025-11-07 01:37:08,998 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,998 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will the next Dutch government be GL/PvdA + VVD + D66?
2025-11-07 01:37:08,998 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:37:08,999 - market_scanner_v2 - INFO -    - Estimated Reward: $30 (based on volume=$23278)
2025-11-07 01:37:08,999 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,999 - market_scanner_v2 - INFO -    - Competition: 0.000444 bars, Score: 17.28
2025-11-07 01:37:08,999 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,999 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump establish a Gaza â€œBoard of Peaceâ€ in 2025?
2025-11-07 01:37:08,999 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:37:08,999 - market_scanner_v2 - INFO -    - Estimated Reward: $30 (based on volume=$6039)
2025-11-07 01:37:08,999 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:08,999 - market_scanner_v2 - INFO -    - Competition: 1.9152 bars, Score: -175.92
2025-11-07 01:37:08,999 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:08,999 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will the Government shutdown end November 12-15?
2025-11-07 01:37:09,000 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:37:09,000 - market_scanner_v2 - INFO -    - Estimated Reward: $200 (based on volume=$112624)
2025-11-07 01:37:09,000 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:09,000 - market_scanner_v2 - INFO -    - Competition: 2.826148 bars, Score: -171.35
2025-11-07 01:37:09,000 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:09,000 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will MetaMask launch a token in 2025?
2025-11-07 01:37:09,000 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:37:09,001 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$231159)
2025-11-07 01:37:09,001 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:09,001 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 28.12
2025-11-07 01:37:09,001 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:09,001 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will MetaMask launch a token by September 30, 2026?
2025-11-07 01:37:09,001 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:37:09,001 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$507)
2025-11-07 01:37:09,001 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:09,001 - market_scanner_v2 - INFO -    - Competition: 0.03808 bars, Score: 6.24
2025-11-07 01:37:09,001 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:09,001 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Matt Van Epps win TN-7 Special Election?
2025-11-07 01:37:09,001 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:37:09,001 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$2908)
2025-11-07 01:37:09,001 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:09,001 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.29
2025-11-07 01:37:09,001 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:09,002 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Russia capture Rodynske by December 31?
2025-11-07 01:37:09,002 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:37:09,002 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$11725)
2025-11-07 01:37:09,002 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:09,002 - market_scanner_v2 - INFO -    - Competition: 2.925501 bars, Score: -286.38
2025-11-07 01:37:09,002 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:09,002 - market_scanner_v2 - INFO - âœ… ACCEPTED: US x Venezuela military engagement by November 14?
2025-11-07 01:37:09,002 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:37:09,002 - market_scanner_v2 - INFO -    - Estimated Reward: $100 (based on volume=$79998)
2025-11-07 01:37:09,002 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:09,002 - market_scanner_v2 - INFO -    - Competition: 2.753472 bars, Score: -217.35
2025-11-07 01:37:09,002 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:09,002 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Gemini 3.0 be released by November 15?
2025-11-07 01:37:09,002 - market_scanner_v2 - INFO -    - Category: science
2025-11-07 01:37:09,002 - market_scanner_v2 - INFO -    - Estimated Reward: $200 (based on volume=$227154)
2025-11-07 01:37:09,002 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:09,002 - market_scanner_v2 - INFO -    - Competition: 0.933612 bars, Score: 29.35
2025-11-07 01:37:09,002 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:09,003 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Katie Wilson win the 2025 Seattle mayoral election?
2025-11-07 01:37:09,003 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:37:09,003 - market_scanner_v2 - INFO -    - Estimated Reward: $30 (based on volume=$51648)
2025-11-07 01:37:09,003 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:09,003 - market_scanner_v2 - INFO -    - Competition: 2.258143 bars, Score: -205.65
2025-11-07 01:37:09,003 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:09,003 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Roaring Kitty tweet again by December 31?
2025-11-07 01:37:09,003 - market_scanner_v2 - INFO -    - Category: science
2025-11-07 01:37:09,003 - market_scanner_v2 - INFO -    - Estimated Reward: $15 (based on volume=$213)
2025-11-07 01:37:09,003 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:09,003 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 7.52
2025-11-07 01:37:09,003 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:09,004 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Russia capture Kostyantynivka by December 31?
2025-11-07 01:37:09,004 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:37:09,004 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$20214)
2025-11-07 01:37:09,004 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:37:09,004 - market_scanner_v2 - INFO -    - Competition: 2.449 bars, Score: -237.88
2025-11-07 01:37:09,004 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:37:09,004 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 99/2840 markets passed
2025-11-07 01:37:09,004 - market_scanner_v2 - INFO -    - 2342 rejected: reward < $10
2025-11-07 01:37:09,005 - market_scanner_v2 - INFO -    - 205 rejected: competition > 3
2025-11-07 01:37:09,005 - market_scanner_v2 - INFO -    - 173 rejected: category not in ['crypto', 'sports', 'politics', 'science', 'entertainment']
2025-11-07 01:37:09,005 - market_scanner_v2 - INFO -    - 21 rejected: volume = 0 (no liquidity)
2025-11-07 01:37:09,005 - market_scanner_v2 - INFO - ðŸ” Verifying orderbook for top 50 markets...
2025-11-07 01:37:13,058 - market_scanner_v2 - INFO -    Progress: 10/50 markets verified...
2025-11-07 01:37:17,546 - market_scanner_v2 - INFO -    Progress: 20/50 markets verified...
2025-11-07 01:37:22,953 - market_scanner_v2 - INFO -    Progress: 30/50 markets verified...
2025-11-07 01:37:27,502 - market_scanner_v2 - INFO -    Progress: 40/50 markets verified...
2025-11-07 01:37:32,012 - market_scanner_v2 - INFO -    Progress: 50/50 markets verified...
2025-11-07 01:37:32,459 - market_scanner_v2 - INFO - âœ… Found 99 qualifying markets (from 2840 total)
2025-11-07 01:37:32,462 - market_selector - INFO - Selected 2 markets from 99 candidates
2025-11-07 01:37:33,806 - order_manager - INFO - ðŸ“Š Orderbook for market 653215:
2025-11-07 01:37:33,806 - order_manager - INFO -    Best Bid: $0.0010 (0.10Â¢)
2025-11-07 01:37:33,806 - order_manager - INFO -    Best Ask: $0.9990 (99.90Â¢)
2025-11-07 01:37:33,807 - order_manager - INFO -    Mid Price: $0.5000 (50.00Â¢)
2025-11-07 01:37:33,807 - order_manager - INFO -    Spread: $0.9980 (99.80Â¢)
2025-11-07 01:37:33,807 - order_manager - INFO -    Spread %: 99800.00%
2025-11-07 01:37:33,807 - order_manager - INFO -    Top 3 Bids:
2025-11-07 01:37:33,807 - order_manager - INFO -       1. $0.0010 (0.10Â¢) x 21339
2025-11-07 01:37:33,807 - order_manager - INFO -       2. $0.0020 (0.20Â¢) x 10017
2025-11-07 01:37:33,807 - order_manager - INFO -       3. $0.0030 (0.30Â¢) x 200
2025-11-07 01:37:33,807 - order_manager - INFO -    Top 3 Asks:
2025-11-07 01:37:33,807 - order_manager - INFO -       1. $0.9990 (99.90Â¢) x 13736
2025-11-07 01:37:33,807 - order_manager - INFO -       2. $0.9980 (99.80Â¢) x 10010
2025-11-07 01:37:33,807 - order_manager - INFO -       3. $0.9970 (99.70Â¢) x 10000
2025-11-07 01:37:33,807 - order_manager - INFO - ðŸ’° Calculated prices:
2025-11-07 01:37:33,807 - order_manager - INFO -    Midpoint: $0.5000 (50.00Â¢)
2025-11-07 01:37:33,807 - order_manager - INFO -    YES: $0.0010 (0.10Â¢) at position 2
2025-11-07 01:37:33,807 - order_manager - INFO -    YES spread from mid: 99.80%
2025-11-07 01:37:33,807 - order_manager - INFO -    NO: $0.0010 (0.10Â¢) at position 2
2025-11-07 01:37:33,807 - order_manager - INFO -    NO as YES equivalent: $0.9990 (99.90Â¢)
2025-11-07 01:37:33,807 - order_manager - INFO -    NO spread from mid: 99.80%
2025-11-07 01:37:33,807 - order_manager - INFO -    Max spread: 99.80% (allowed: 3.50%)
2025-11-07 01:37:33,807 - order_manager - WARNING - âŒ Calculated prices exceed max spread (99.80% > 3.50%)
2025-11-07 01:37:33,808 - order_manager - WARNING -    This indicates orderbook is too thin or position 2-3 is too far from midpoint
2025-11-07 01:37:33,808 - order_manager - WARNING -    REJECTING market to avoid placing order at position #1 (best bid/ask)
2025-11-07 01:37:33,808 - order_manager - WARNING -    Reason: Adjusting to max spread would place order too close to best bid/ask
2025-11-07 01:37:33,808 - order_manager - WARNING -    â†’ High risk of being filled immediately!
2025-11-07 01:37:33,808 - order_manager - WARNING - Could not calculate valid prices for market 653215
2025-11-07 01:37:33,808 - __main__ - WARNING - âš ï¸  Skipped market 653215 - could not prepare valid order (spread too high or orderbook too thin)
2025-11-07 01:37:34,153 - order_manager - INFO - ðŸ“Š Orderbook for market 663184:
2025-11-07 01:37:34,154 - order_manager - INFO -    Best Bid: $0.0100 (1.00Â¢)
2025-11-07 01:37:34,154 - order_manager - INFO -    Best Ask: $0.9900 (99.00Â¢)
2025-11-07 01:37:34,154 - order_manager - INFO -    Mid Price: $0.5000 (50.00Â¢)
2025-11-07 01:37:34,154 - order_manager - INFO -    Spread: $0.9800 (98.00Â¢)
2025-11-07 01:37:34,154 - order_manager - INFO -    Spread %: 9800.00%
2025-11-07 01:37:34,154 - order_manager - INFO -    Top 3 Bids:
2025-11-07 01:37:34,154 - order_manager - INFO -       1. $0.0100 (1.00Â¢) x 16
2025-11-07 01:37:34,154 - order_manager - INFO -       2. $0.0300 (3.00Â¢) x 233
2025-11-07 01:37:34,154 - order_manager - INFO -       3. $0.0500 (5.00Â¢) x 17
2025-11-07 01:37:34,154 - order_manager - INFO -    Top 3 Asks:
2025-11-07 01:37:34,154 - order_manager - INFO -       1. $0.9900 (99.00Â¢) x 18
2025-11-07 01:37:34,154 - order_manager - INFO -       2. $0.9800 (98.00Â¢) x 350
2025-11-07 01:37:34,154 - order_manager - INFO -       3. $0.9700 (97.00Â¢) x 10
2025-11-07 01:37:34,154 - order_manager - INFO - ðŸ’° Calculated prices:
2025-11-07 01:37:34,154 - order_manager - INFO -    Midpoint: $0.5000 (50.00Â¢)
2025-11-07 01:37:34,154 - order_manager - INFO -    YES: $0.0290 (2.90Â¢) at position 2
2025-11-07 01:37:34,154 - order_manager - INFO -    YES spread from mid: 94.20%
2025-11-07 01:37:34,154 - order_manager - INFO -    NO: $0.0190 (1.90Â¢) at position 2
2025-11-07 01:37:34,154 - order_manager - INFO -    NO as YES equivalent: $0.9810 (98.10Â¢)
2025-11-07 01:37:34,154 - order_manager - INFO -    NO spread from mid: 96.20%
2025-11-07 01:37:34,154 - order_manager - INFO -    Max spread: 96.20% (allowed: 3.50%)
2025-11-07 01:37:34,155 - order_manager - WARNING - âŒ Calculated prices exceed max spread (96.20% > 3.50%)
2025-11-07 01:37:34,155 - order_manager - WARNING -    This indicates orderbook is too thin or position 2-3 is too far from midpoint
2025-11-07 01:37:34,155 - order_manager - WARNING -    REJECTING market to avoid placing order at position #1 (best bid/ask)
2025-11-07 01:37:34,155 - order_manager - WARNING -    Reason: Adjusting to max spread would place order too close to best bid/ask
2025-11-07 01:37:34,155 - order_manager - WARNING -    â†’ High risk of being filled immediately!
2025-11-07 01:37:34,155 - order_manager - WARNING - Could not calculate valid prices for market 663184
2025-11-07 01:37:34,155 - __main__ - WARNING - âš ï¸  Skipped market 663184 - could not prepare valid order (spread too high or orderbook too thin)
2025-11-07 01:38:43,697 - market_scanner_v2 - INFO - ðŸŒ Scraping markets from /rewards page using Playwright...
2025-11-07 01:38:43,698 - playwright_rewards_scraper - INFO - ðŸŒ Fetching markets from /rewards API...
2025-11-07 01:38:43,698 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 1 (cursor: MA==)...
2025-11-07 01:38:44,134 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 1
2025-11-07 01:38:44,135 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 2 (cursor: MTAw)...
2025-11-07 01:38:44,557 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 2
2025-11-07 01:38:44,558 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 3 (cursor: MjAw)...
2025-11-07 01:38:45,342 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 3
2025-11-07 01:38:45,343 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 4 (cursor: MzAw)...
2025-11-07 01:38:45,993 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 4
2025-11-07 01:38:45,993 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 5 (cursor: NDAw)...
2025-11-07 01:38:46,409 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 5
2025-11-07 01:38:46,410 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 6 (cursor: NTAw)...
2025-11-07 01:38:47,064 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 6
2025-11-07 01:38:47,065 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 7 (cursor: NjAw)...
2025-11-07 01:38:47,483 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 7
2025-11-07 01:38:47,484 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 8 (cursor: NzAw)...
2025-11-07 01:38:47,932 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 8
2025-11-07 01:38:47,932 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 9 (cursor: ODAw)...
2025-11-07 01:38:48,559 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 9
2025-11-07 01:38:48,560 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 10 (cursor: OTAw)...
2025-11-07 01:38:49,233 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 10
2025-11-07 01:38:49,233 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 11 (cursor: MTAwMA==)...
2025-11-07 01:38:49,680 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 11
2025-11-07 01:38:49,680 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 12 (cursor: MTEwMA==)...
2025-11-07 01:38:50,335 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 12
2025-11-07 01:38:50,335 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 13 (cursor: MTIwMA==)...
2025-11-07 01:38:50,974 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 13
2025-11-07 01:38:50,975 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 14 (cursor: MTMwMA==)...
2025-11-07 01:38:51,631 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 14
2025-11-07 01:38:51,632 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 15 (cursor: MTQwMA==)...
2025-11-07 01:38:52,299 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 15
2025-11-07 01:38:52,300 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 16 (cursor: MTUwMA==)...
2025-11-07 01:38:52,950 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 16
2025-11-07 01:38:52,951 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 17 (cursor: MTYwMA==)...
2025-11-07 01:38:53,750 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 17
2025-11-07 01:38:53,751 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 18 (cursor: MTcwMA==)...
2025-11-07 01:38:54,981 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 18
2025-11-07 01:38:54,983 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 19 (cursor: MTgwMA==)...
2025-11-07 01:38:55,469 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 19
2025-11-07 01:38:55,470 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 20 (cursor: MTkwMA==)...
2025-11-07 01:38:55,948 - ml_predictor - INFO - Alert sent: ðŸš¨ <b>MONITORING ALERT</b>

ðŸ”´ KhÃ´ng quÃ©t markets trong 82s!
2025-11-07 01:38:55,948 - monitoring_system - INFO - Alert sent: no_scan
2025-11-07 01:38:55,948 - __main__ - WARNING - âš ï¸ Health check failed: 2 issues
2025-11-07 01:38:55,948 - __main__ - WARNING -    - ðŸ”´ KhÃ´ng quÃ©t markets trong 82s!
2025-11-07 01:38:55,948 - __main__ - WARNING -    - âš ï¸ API cháº­m: 44.2s trung bÃ¬nh
2025-11-07 01:38:56,178 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 20
2025-11-07 01:38:56,179 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 21 (cursor: MjAwMA==)...
2025-11-07 01:38:56,840 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 21
2025-11-07 01:38:56,841 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 22 (cursor: MjEwMA==)...
2025-11-07 01:38:57,489 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 22
2025-11-07 01:38:57,490 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 23 (cursor: MjIwMA==)...
2025-11-07 01:38:57,980 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 23
2025-11-07 01:38:57,981 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 24 (cursor: MjMwMA==)...
2025-11-07 01:38:58,665 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 24
2025-11-07 01:38:58,666 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 25 (cursor: MjQwMA==)...
2025-11-07 01:38:59,316 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 25
2025-11-07 01:38:59,316 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 26 (cursor: MjUwMA==)...
2025-11-07 01:38:59,983 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 26
2025-11-07 01:38:59,984 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 27 (cursor: MjYwMA==)...
2025-11-07 01:39:00,484 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 27
2025-11-07 01:39:00,485 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 28 (cursor: MjcwMA==)...
2025-11-07 01:39:01,123 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 28
2025-11-07 01:39:01,124 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 29 (cursor: MjgwMA==)...
2025-11-07 01:39:01,766 - playwright_rewards_scraper - INFO - âœ… Got 40 markets on page 29
2025-11-07 01:39:01,767 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 30 (cursor: LTE=)...
2025-11-07 01:39:02,036 - playwright_rewards_scraper - INFO - âœ… No more markets on page 30
2025-11-07 01:39:02,037 - playwright_rewards_scraper - INFO - âœ… Fetched 2840 total unique markets from /rewards API
2025-11-07 01:39:02,086 - market_scanner_v2 - INFO - âœ… Got 2840 markets from /rewards page
2025-11-07 01:39:02,087 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Kanye visit Israel by December 31?
2025-11-07 01:39:02,087 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:39:02,087 - market_scanner_v2 - INFO -    - Estimated Reward: $50 (based on volume=$64)
2025-11-07 01:39:02,087 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,087 - market_scanner_v2 - INFO -    - Competition: 0.539847 bars, Score: -28.98
2025-11-07 01:39:02,087 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,087 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Ukraine win Miss Universe 2025?
2025-11-07 01:39:02,087 - market_scanner_v2 - INFO -    - Category: science
2025-11-07 01:39:02,087 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$61)
2025-11-07 01:39:02,087 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,087 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.01
2025-11-07 01:39:02,087 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,087 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will China win Miss Universe 2025?
2025-11-07 01:39:02,087 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:39:02,087 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$66)
2025-11-07 01:39:02,087 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,087 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.01
2025-11-07 01:39:02,087 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,087 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Great Britain win Miss Universe 2025?
2025-11-07 01:39:02,088 - market_scanner_v2 - INFO -    - Category: science
2025-11-07 01:39:02,088 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$66)
2025-11-07 01:39:02,088 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,088 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.01
2025-11-07 01:39:02,088 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,088 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Spain win Miss Universe 2025?
2025-11-07 01:39:02,088 - market_scanner_v2 - INFO -    - Category: science
2025-11-07 01:39:02,088 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$66)
2025-11-07 01:39:02,088 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,088 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.01
2025-11-07 01:39:02,088 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,088 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel win Miss Universe 2025?
2025-11-07 01:39:02,088 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:39:02,088 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$66)
2025-11-07 01:39:02,088 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,088 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.01
2025-11-07 01:39:02,088 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,088 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Russia win Miss Universe 2025?
2025-11-07 01:39:02,088 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:39:02,088 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$61)
2025-11-07 01:39:02,088 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,088 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.01
2025-11-07 01:39:02,088 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,089 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Palestine win Miss Universe 2025?
2025-11-07 01:39:02,089 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:39:02,089 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$66)
2025-11-07 01:39:02,089 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,089 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.01
2025-11-07 01:39:02,089 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,089 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Howard Hughes Holdings (HHH) beat quarterly earnings?
2025-11-07 01:39:02,089 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:39:02,089 - market_scanner_v2 - INFO -    - Estimated Reward: $50 (based on volume=$110)
2025-11-07 01:39:02,089 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,089 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 25.01
2025-11-07 01:39:02,089 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,089 - market_scanner_v2 - INFO - âœ… ACCEPTED: Airbnb (ABNB) Up or Down on November 7?
2025-11-07 01:39:02,089 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:39:02,089 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$687)
2025-11-07 01:39:02,089 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,089 - market_scanner_v2 - INFO -    - Competition: 0.136 bars, Score: -3.53
2025-11-07 01:39:02,089 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,089 - market_scanner_v2 - INFO - âœ… ACCEPTED: Palantir (PLTR) Up or Down on November 7?
2025-11-07 01:39:02,089 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:39:02,089 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$30)
2025-11-07 01:39:02,089 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,089 - market_scanner_v2 - INFO -    - Competition: 1.260037 bars, Score: -116.00
2025-11-07 01:39:02,089 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,090 - market_scanner_v2 - INFO - âœ… ACCEPTED: NVIDIA (NVDA) Up or Down on November 7?
2025-11-07 01:39:02,090 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:39:02,090 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$71)
2025-11-07 01:39:02,090 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,090 - market_scanner_v2 - INFO -    - Competition: 0.29784 bars, Score: -19.78
2025-11-07 01:39:02,090 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,090 - market_scanner_v2 - INFO - âœ… ACCEPTED: Hang Seng (HSI) Up or Down on November 7?
2025-11-07 01:39:02,090 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:39:02,090 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$51)
2025-11-07 01:39:02,090 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,090 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-07 01:39:02,090 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,090 - market_scanner_v2 - INFO - âœ… ACCEPTED: Tesla (TSLA) Up or Down on November 7?
2025-11-07 01:39:02,090 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:39:02,090 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$184)
2025-11-07 01:39:02,090 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,090 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.02
2025-11-07 01:39:02,090 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,090 - market_scanner_v2 - INFO - âœ… ACCEPTED: DAX (DAX) Up or Down on November 7?
2025-11-07 01:39:02,090 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:39:02,090 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$24)
2025-11-07 01:39:02,090 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,090 - market_scanner_v2 - INFO -    - Competition: 0.765417 bars, Score: -66.54
2025-11-07 01:39:02,090 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,090 - market_scanner_v2 - INFO - âœ… ACCEPTED: FTSE 100 (UKX) Up or Down on November 7?
2025-11-07 01:39:02,090 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:39:02,090 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$150)
2025-11-07 01:39:02,091 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,091 - market_scanner_v2 - INFO -    - Competition: 0.765417 bars, Score: -66.53
2025-11-07 01:39:02,091 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,091 - market_scanner_v2 - INFO - âœ… ACCEPTED: Meta (META) Up or Down on November 7?
2025-11-07 01:39:02,091 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:39:02,091 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2)
2025-11-07 01:39:02,091 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,091 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.00
2025-11-07 01:39:02,091 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,091 - market_scanner_v2 - INFO - âœ… ACCEPTED: Dow Jones (DJI) Up or Down on November 7?
2025-11-07 01:39:02,091 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:39:02,091 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2)
2025-11-07 01:39:02,091 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,091 - market_scanner_v2 - INFO -    - Competition: 1.224667 bars, Score: -112.47
2025-11-07 01:39:02,091 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,091 - market_scanner_v2 - INFO - âœ… ACCEPTED: Google (GOOGL) Up or Down on November 7?
2025-11-07 01:39:02,091 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:39:02,091 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2)
2025-11-07 01:39:02,091 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,091 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.00
2025-11-07 01:39:02,091 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,091 - market_scanner_v2 - INFO - âœ… ACCEPTED: Amazon (AMZN) Up or Down on November 7?
2025-11-07 01:39:02,091 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:39:02,091 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$108)
2025-11-07 01:39:02,091 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,092 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-07 01:39:02,092 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,092 - market_scanner_v2 - INFO - âœ… ACCEPTED: Nasdaq 100 (NDX) Up or Down on November 7?
2025-11-07 01:39:02,092 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:39:02,092 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$64)
2025-11-07 01:39:02,092 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,092 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-07 01:39:02,092 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,092 - market_scanner_v2 - INFO - âœ… ACCEPTED: Microsoft (MSFT) Up or Down on November 7?
2025-11-07 01:39:02,092 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:39:02,092 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$150)
2025-11-07 01:39:02,092 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,092 - market_scanner_v2 - INFO -    - Competition: 0.820527 bars, Score: -72.04
2025-11-07 01:39:02,092 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,092 - market_scanner_v2 - INFO - âœ… ACCEPTED: Nikkei 225 (NIK) Up or Down on November 7?
2025-11-07 01:39:02,092 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:39:02,092 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$56)
2025-11-07 01:39:02,092 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,092 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-07 01:39:02,092 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,092 - market_scanner_v2 - INFO - âœ… ACCEPTED: S&P 500 (SPX) Up or Down on November 7?
2025-11-07 01:39:02,092 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:39:02,092 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$187)
2025-11-07 01:39:02,092 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,092 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.02
2025-11-07 01:39:02,092 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,093 - market_scanner_v2 - INFO - âœ… ACCEPTED: Apple (AAPL) Up or Down on November 7?
2025-11-07 01:39:02,093 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:39:02,093 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$12)
2025-11-07 01:39:02,093 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,093 - market_scanner_v2 - INFO -    - Competition: 0.051 bars, Score: 4.90
2025-11-07 01:39:02,093 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,093 - market_scanner_v2 - INFO - âœ… ACCEPTED: Consensys IPO closing market cap above $3B?
2025-11-07 01:39:02,093 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:39:02,093 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$660)
2025-11-07 01:39:02,093 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,093 - market_scanner_v2 - INFO -    - Competition: 2.756071 bars, Score: -265.54
2025-11-07 01:39:02,093 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,093 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel allow independent journalists into Gaza by Decem
2025-11-07 01:39:02,093 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:39:02,093 - market_scanner_v2 - INFO -    - Estimated Reward: $60 (based on volume=$9837)
2025-11-07 01:39:02,093 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,093 - market_scanner_v2 - INFO -    - Competition: 1.65968 bars, Score: -134.98
2025-11-07 01:39:02,093 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,093 - market_scanner_v2 - INFO - âœ… ACCEPTED: Trump announces new drug boat strike by November 7?
2025-11-07 01:39:02,093 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:39:02,093 - market_scanner_v2 - INFO -    - Estimated Reward: $15 (based on volume=$6592)
2025-11-07 01:39:02,094 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,094 - market_scanner_v2 - INFO -    - Competition: 1.481333 bars, Score: -139.97
2025-11-07 01:39:02,094 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,094 - market_scanner_v2 - INFO - âœ… ACCEPTED: Trump announces new drug boat strike by November 14?
2025-11-07 01:39:02,094 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:39:02,094 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$11390)
2025-11-07 01:39:02,094 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,094 - market_scanner_v2 - INFO -    - Competition: 0.823877 bars, Score: -76.25
2025-11-07 01:39:02,094 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,094 - market_scanner_v2 - INFO - âœ… ACCEPTED: NYMEX Crude Oil Futures (WTI) (CL=F) Up or Down on November 
2025-11-07 01:39:02,094 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:39:02,094 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2243)
2025-11-07 01:39:02,094 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,094 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.22
2025-11-07 01:39:02,094 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,094 - market_scanner_v2 - INFO - âœ… ACCEPTED: COMEX Silver Futures (SI=F) Up or Down on November 6?
2025-11-07 01:39:02,094 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:39:02,094 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$735)
2025-11-07 01:39:02,094 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,094 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.07
2025-11-07 01:39:02,095 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,095 - market_scanner_v2 - INFO - âœ… ACCEPTED: COMEX Gold Futures (GC=F) Up or Down on November 6?
2025-11-07 01:39:02,095 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:39:02,095 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$855)
2025-11-07 01:39:02,095 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,095 - market_scanner_v2 - INFO -    - Competition: 2.429 bars, Score: -232.81
2025-11-07 01:39:02,095 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,095 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Catalin Drula finish second in the 2025 Bucharest mayor
2025-11-07 01:39:02,095 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:39:02,095 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$709)
2025-11-07 01:39:02,095 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,095 - market_scanner_v2 - INFO -    - Competition: 0.760555 bars, Score: -70.98
2025-11-07 01:39:02,095 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,095 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Google Gemini 3 score at least 40% on Humanityâ€™s Last E
2025-11-07 01:39:02,095 - market_scanner_v2 - INFO -    - Category: science
2025-11-07 01:39:02,095 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$1131)
2025-11-07 01:39:02,095 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,095 - market_scanner_v2 - INFO -    - Competition: 2.727311 bars, Score: -262.62
2025-11-07 01:39:02,095 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,095 - market_scanner_v2 - INFO - âœ… ACCEPTED: U.S. Closes Airspace due to Government Shutdown?
2025-11-07 01:39:02,095 - market_scanner_v2 - INFO -    - Category: science
2025-11-07 01:39:02,095 - market_scanner_v2 - INFO -    - Estimated Reward: $50 (based on volume=$14330)
2025-11-07 01:39:02,095 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,096 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 26.43
2025-11-07 01:39:02,096 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,096 - market_scanner_v2 - INFO - âœ… ACCEPTED: NYMEX Crude Oil Futures (WTI) (CL=F) Up or Down on November 
2025-11-07 01:39:02,096 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:39:02,096 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$130)
2025-11-07 01:39:02,096 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,096 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-07 01:39:02,096 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,096 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Asia" or "Asian" 8+ times during C5+1 Summit
2025-11-07 01:39:02,096 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:39:02,096 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$7842)
2025-11-07 01:39:02,096 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,096 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.78
2025-11-07 01:39:02,096 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,096 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Million" or "Billion" or "Trillion" 12+ time
2025-11-07 01:39:02,096 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:39:02,096 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$6712)
2025-11-07 01:39:02,096 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,096 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.67
2025-11-07 01:39:02,096 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,096 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Thank you" 8+ times during C5+1 Summit on No
2025-11-07 01:39:02,096 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:39:02,096 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$8507)
2025-11-07 01:39:02,096 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,096 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.85
2025-11-07 01:39:02,096 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,097 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Biden" or "Obama" 4+ times during C5+1 Summi
2025-11-07 01:39:02,097 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:39:02,097 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$4101)
2025-11-07 01:39:02,097 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,097 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.41
2025-11-07 01:39:02,097 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,097 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Russia" or "China" 4+ times during C5+1 Summ
2025-11-07 01:39:02,097 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:39:02,097 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$7641)
2025-11-07 01:39:02,097 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,097 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.76
2025-11-07 01:39:02,097 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,097 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Nuclear" 2+ times during C5+1 Summit on Nove
2025-11-07 01:39:02,097 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:39:02,097 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$2305)
2025-11-07 01:39:02,097 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,097 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.23
2025-11-07 01:39:02,097 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,097 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Caspian Sea" during C5+1 Summit on November 
2025-11-07 01:39:02,097 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:39:02,097 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$6274)
2025-11-07 01:39:02,097 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,097 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.63
2025-11-07 01:39:02,097 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,098 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Boeing" during C5+1 Summit on November 6?
2025-11-07 01:39:02,098 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:39:02,098 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$4640)
2025-11-07 01:39:02,098 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,098 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.46
2025-11-07 01:39:02,098 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,098 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Rare Earth" or "Critical Mineral" during C5+
2025-11-07 01:39:02,098 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:39:02,098 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$8309)
2025-11-07 01:39:02,098 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,098 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.83
2025-11-07 01:39:02,098 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,098 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Energy" during C5+1 Summit on November 6?
2025-11-07 01:39:02,098 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:39:02,098 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$9825)
2025-11-07 01:39:02,098 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,098 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.98
2025-11-07 01:39:02,098 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,098 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Drug" during C5+1 Summit on November 6?
2025-11-07 01:39:02,098 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:39:02,098 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$2410)
2025-11-07 01:39:02,098 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,098 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.24
2025-11-07 01:39:02,098 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,098 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Soviet" during C5+1 Summit on November 6?
2025-11-07 01:39:02,098 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:39:02,099 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$3623)
2025-11-07 01:39:02,099 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,099 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.36
2025-11-07 01:39:02,099 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,099 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Best Equipment" during C5+1 Summit on Novemb
2025-11-07 01:39:02,099 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:39:02,099 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$548)
2025-11-07 01:39:02,099 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,099 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.05
2025-11-07 01:39:02,099 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,099 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Investment" during C5+1 Summit on November 6
2025-11-07 01:39:02,099 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:39:02,099 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$3839)
2025-11-07 01:39:02,099 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,099 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.38
2025-11-07 01:39:02,099 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,099 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Middle East" during C5+1 Summit on November 
2025-11-07 01:39:02,099 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:39:02,099 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$150)
2025-11-07 01:39:02,099 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,099 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.01
2025-11-07 01:39:02,099 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,099 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Azerbaijan" during C5+1 Summit on November 6
2025-11-07 01:39:02,099 - market_scanner_v2 - INFO -    - Category: science
2025-11-07 01:39:02,099 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$2317)
2025-11-07 01:39:02,099 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,099 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.23
2025-11-07 01:39:02,099 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,100 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "President Xi" during C5+1 Summit on November
2025-11-07 01:39:02,100 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:39:02,100 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$2352)
2025-11-07 01:39:02,100 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,100 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.24
2025-11-07 01:39:02,100 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,100 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Afghanistan" during C5+1 Summit on November 
2025-11-07 01:39:02,100 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:39:02,100 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$820)
2025-11-07 01:39:02,100 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,100 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.08
2025-11-07 01:39:02,100 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,100 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Eight wars" during C5+1 Summit on November 6
2025-11-07 01:39:02,100 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:39:02,100 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$3294)
2025-11-07 01:39:02,100 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,100 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.33
2025-11-07 01:39:02,100 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,100 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Dead Country" during C5+1 Summit on November
2025-11-07 01:39:02,100 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:39:02,100 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$3079)
2025-11-07 01:39:02,100 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,100 - market_scanner_v2 - INFO -    - Competition: 1.701 bars, Score: -164.79
2025-11-07 01:39:02,100 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,100 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Crypto" or "AI" during C5+1 Summit on Novemb
2025-11-07 01:39:02,100 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:39:02,100 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$6332)
2025-11-07 01:39:02,100 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,100 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.63
2025-11-07 01:39:02,101 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,101 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Claude pass Grok by November 15 on the UnifAI Polyarena
2025-11-07 01:39:02,101 - market_scanner_v2 - INFO -    - Category: science
2025-11-07 01:39:02,101 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$462)
2025-11-07 01:39:02,101 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,101 - market_scanner_v2 - INFO -    - Competition: 1.088 bars, Score: -103.75
2025-11-07 01:39:02,101 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,101 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Airbnb (ABNB) finish week of November 10 above $115?
2025-11-07 01:39:02,101 - market_scanner_v2 - INFO -    - Category: science
2025-11-07 01:39:02,101 - market_scanner_v2 - INFO -    - Estimated Reward: $15 (based on volume=$50)
2025-11-07 01:39:02,101 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,101 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 7.51
2025-11-07 01:39:02,101 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,101 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Airbnb (ABNB) finish week of November 10 above $125?
2025-11-07 01:39:02,101 - market_scanner_v2 - INFO -    - Category: science
2025-11-07 01:39:02,101 - market_scanner_v2 - INFO -    - Estimated Reward: $15 (based on volume=$694)
2025-11-07 01:39:02,101 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,101 - market_scanner_v2 - INFO -    - Competition: 0.10988 bars, Score: -3.42
2025-11-07 01:39:02,101 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,101 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Airbnb (ABNB) finish week of November 10 above $135?
2025-11-07 01:39:02,101 - market_scanner_v2 - INFO -    - Category: science
2025-11-07 01:39:02,101 - market_scanner_v2 - INFO -    - Estimated Reward: $15 (based on volume=$20)
2025-11-07 01:39:02,101 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,101 - market_scanner_v2 - INFO -    - Competition: 2.159934 bars, Score: -208.49
2025-11-07 01:39:02,101 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,101 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Netflix (NFLX) finish week of November 10 above $1,070?
2025-11-07 01:39:02,102 - market_scanner_v2 - INFO -    - Category: entertainment
2025-11-07 01:39:02,102 - market_scanner_v2 - INFO -    - Estimated Reward: $15 (based on volume=$150)
2025-11-07 01:39:02,102 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,102 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 7.51
2025-11-07 01:39:02,102 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,102 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Airbnb (ABNB) close above $140 end of November?
2025-11-07 01:39:02,102 - market_scanner_v2 - INFO -    - Category: science
2025-11-07 01:39:02,102 - market_scanner_v2 - INFO -    - Estimated Reward: $15 (based on volume=$104)
2025-11-07 01:39:02,102 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,102 - market_scanner_v2 - INFO -    - Competition: 1.60472 bars, Score: -152.96
2025-11-07 01:39:02,102 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,102 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Netflix (NFLX) close above $1,080 end of November?
2025-11-07 01:39:02,102 - market_scanner_v2 - INFO -    - Category: entertainment
2025-11-07 01:39:02,102 - market_scanner_v2 - INFO -    - Estimated Reward: $15 (based on volume=$125)
2025-11-07 01:39:02,102 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,102 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 7.51
2025-11-07 01:39:02,102 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,103 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Microstrategy announce a Bitcoin purchase November 4-10
2025-11-07 01:39:02,103 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:39:02,103 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$10868)
2025-11-07 01:39:02,103 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,103 - market_scanner_v2 - INFO -    - Competition: 1.474 bars, Score: -141.31
2025-11-07 01:39:02,103 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,103 - market_scanner_v2 - INFO - âœ… ACCEPTED: Hezbollah strike on Israel by December 31?
2025-11-07 01:39:02,103 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:39:02,103 - market_scanner_v2 - INFO -    - Estimated Reward: $50 (based on volume=$14904)
2025-11-07 01:39:02,103 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,103 - market_scanner_v2 - INFO -    - Competition: 1.250694 bars, Score: -98.58
2025-11-07 01:39:02,104 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,104 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Airbnb reach $136 in November?
2025-11-07 01:39:02,104 - market_scanner_v2 - INFO -    - Category: science
2025-11-07 01:39:02,104 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$5)
2025-11-07 01:39:02,104 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,104 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.00
2025-11-07 01:39:02,104 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,104 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Lebanon on November 7?
2025-11-07 01:39:02,104 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:39:02,104 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$11321)
2025-11-07 01:39:02,104 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,104 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 11.13
2025-11-07 01:39:02,105 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,105 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Lebanon on November 8?
2025-11-07 01:39:02,105 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:39:02,105 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2258)
2025-11-07 01:39:02,105 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,105 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.23
2025-11-07 01:39:02,105 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,105 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Lebanon on November 11?
2025-11-07 01:39:02,105 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:39:02,105 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$906)
2025-11-07 01:39:02,105 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,105 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.09
2025-11-07 01:39:02,105 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,105 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Lebanon on November 12?
2025-11-07 01:39:02,105 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:39:02,105 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$609)
2025-11-07 01:39:02,105 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,105 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.06
2025-11-07 01:39:02,105 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,105 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Lebanon on November 13?
2025-11-07 01:39:02,105 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:39:02,105 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$491)
2025-11-07 01:39:02,105 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,105 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.05
2025-11-07 01:39:02,105 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,105 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Lebanon on November 14?
2025-11-07 01:39:02,105 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:39:02,106 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$1346)
2025-11-07 01:39:02,106 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,106 - market_scanner_v2 - INFO -    - Competition: 0.790598 bars, Score: -68.93
2025-11-07 01:39:02,106 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,106 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Gaza on November 7?
2025-11-07 01:39:02,106 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:39:02,106 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$1948)
2025-11-07 01:39:02,106 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,106 - market_scanner_v2 - INFO -    - Competition: 2.6611 bars, Score: -255.92
2025-11-07 01:39:02,106 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,106 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Gaza on November 8?
2025-11-07 01:39:02,106 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:39:02,106 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$702)
2025-11-07 01:39:02,106 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,106 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.07
2025-11-07 01:39:02,106 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,106 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Gaza on November 9?
2025-11-07 01:39:02,106 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:39:02,106 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$205)
2025-11-07 01:39:02,106 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,106 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.02
2025-11-07 01:39:02,106 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,106 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Gaza on November 10?
2025-11-07 01:39:02,106 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:39:02,106 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$279)
2025-11-07 01:39:02,106 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,106 - market_scanner_v2 - INFO -    - Competition: 2.916227 bars, Score: -281.59
2025-11-07 01:39:02,106 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,107 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Gaza on November 11?
2025-11-07 01:39:02,107 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:39:02,107 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$58)
2025-11-07 01:39:02,107 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,107 - market_scanner_v2 - INFO -    - Competition: 1.922306 bars, Score: -182.22
2025-11-07 01:39:02,107 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,107 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Gaza on November 14?
2025-11-07 01:39:02,107 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:39:02,107 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$265)
2025-11-07 01:39:02,107 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,107 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.03
2025-11-07 01:39:02,107 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,107 - market_scanner_v2 - INFO - âœ… ACCEPTED: Park Sung-jae in jail by November 30?
2025-11-07 01:39:02,107 - market_scanner_v2 - INFO -    - Category: science
2025-11-07 01:39:02,107 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$3469)
2025-11-07 01:39:02,107 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,107 - market_scanner_v2 - INFO -    - Competition: 1.202566 bars, Score: -114.91
2025-11-07 01:39:02,107 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,107 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Elon Musk post 140-159 tweets from October 31 to Novemb
2025-11-07 01:39:02,107 - market_scanner_v2 - INFO -    - Category: entertainment
2025-11-07 01:39:02,107 - market_scanner_v2 - INFO -    - Estimated Reward: $200 (based on volume=$225332)
2025-11-07 01:39:02,107 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,107 - market_scanner_v2 - INFO -    - Competition: 0.248687 bars, Score: 97.66
2025-11-07 01:39:02,107 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,107 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Elon Musk post 160-179 tweets from October 31 to Novemb
2025-11-07 01:39:02,108 - market_scanner_v2 - INFO -    - Category: entertainment
2025-11-07 01:39:02,108 - market_scanner_v2 - INFO -    - Estimated Reward: $130 (based on volume=$164904)
2025-11-07 01:39:02,108 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,108 - market_scanner_v2 - INFO -    - Competition: 0.009777 bars, Score: 80.51
2025-11-07 01:39:02,108 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,108 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Elon Musk post 180-199 tweets from October 31 to Novemb
2025-11-07 01:39:02,108 - market_scanner_v2 - INFO -    - Category: entertainment
2025-11-07 01:39:02,108 - market_scanner_v2 - INFO -    - Estimated Reward: $30 (based on volume=$161389)
2025-11-07 01:39:02,108 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,108 - market_scanner_v2 - INFO -    - Competition: 0.899767 bars, Score: -58.84
2025-11-07 01:39:02,108 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,109 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Stable launch a token in 2025?
2025-11-07 01:39:02,109 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:39:02,109 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$211226)
2025-11-07 01:39:02,109 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,109 - market_scanner_v2 - INFO -    - Competition: 0.2176 bars, Score: 4.36
2025-11-07 01:39:02,109 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,109 - market_scanner_v2 - INFO - âœ… ACCEPTED: Canton FDV above $3B one day after launch?
2025-11-07 01:39:02,109 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:39:02,109 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$1115)
2025-11-07 01:39:02,109 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,109 - market_scanner_v2 - INFO -    - Competition: 2.750882 bars, Score: -264.98
2025-11-07 01:39:02,109 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,109 - market_scanner_v2 - INFO - âœ… ACCEPTED: Canton FDV above $5B one day after launch?
2025-11-07 01:39:02,109 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:39:02,109 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$857)
2025-11-07 01:39:02,109 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,109 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.09
2025-11-07 01:39:02,109 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,109 - market_scanner_v2 - INFO - âœ… ACCEPTED: Canton FDV above $10B one day after launch?
2025-11-07 01:39:02,109 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:39:02,110 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$725)
2025-11-07 01:39:02,110 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,110 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.07
2025-11-07 01:39:02,110 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,110 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will the next Dutch government be GL/PvdA + VVD + D66?
2025-11-07 01:39:02,110 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:39:02,110 - market_scanner_v2 - INFO -    - Estimated Reward: $30 (based on volume=$23278)
2025-11-07 01:39:02,110 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,110 - market_scanner_v2 - INFO -    - Competition: 0.168006 bars, Score: 0.53
2025-11-07 01:39:02,110 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,111 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump establish a Gaza â€œBoard of Peaceâ€ in 2025?
2025-11-07 01:39:02,111 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:39:02,111 - market_scanner_v2 - INFO -    - Estimated Reward: $30 (based on volume=$6039)
2025-11-07 01:39:02,111 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,111 - market_scanner_v2 - INFO -    - Competition: 1.9152 bars, Score: -175.92
2025-11-07 01:39:02,111 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,111 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will the Government shutdown end November 12-15?
2025-11-07 01:39:02,111 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:39:02,111 - market_scanner_v2 - INFO -    - Estimated Reward: $200 (based on volume=$112624)
2025-11-07 01:39:02,111 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,111 - market_scanner_v2 - INFO -    - Competition: 2.887381 bars, Score: -177.48
2025-11-07 01:39:02,111 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,112 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will MetaMask launch a token in 2025?
2025-11-07 01:39:02,112 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:39:02,112 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$231159)
2025-11-07 01:39:02,112 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,112 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 28.12
2025-11-07 01:39:02,112 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,112 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will MetaMask launch a token by June 30?
2025-11-07 01:39:02,112 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:39:02,112 - market_scanner_v2 - INFO -    - Estimated Reward: $30 (based on volume=$10120)
2025-11-07 01:39:02,112 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,112 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 16.01
2025-11-07 01:39:02,112 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,112 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will MetaMask launch a token by September 30, 2026?
2025-11-07 01:39:02,112 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:39:02,113 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$507)
2025-11-07 01:39:02,113 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,113 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.05
2025-11-07 01:39:02,113 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,113 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Matt Van Epps win TN-7 Special Election?
2025-11-07 01:39:02,113 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:39:02,113 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$2908)
2025-11-07 01:39:02,113 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,113 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.29
2025-11-07 01:39:02,113 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,113 - market_scanner_v2 - INFO - âœ… ACCEPTED: US x Venezuela military engagement by November 14?
2025-11-07 01:39:02,113 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:39:02,113 - market_scanner_v2 - INFO -    - Estimated Reward: $100 (based on volume=$79998)
2025-11-07 01:39:02,113 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,114 - market_scanner_v2 - INFO -    - Competition: 2.753472 bars, Score: -217.35
2025-11-07 01:39:02,114 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,114 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Gemini 3.0 be released by November 15?
2025-11-07 01:39:02,114 - market_scanner_v2 - INFO -    - Category: science
2025-11-07 01:39:02,114 - market_scanner_v2 - INFO -    - Estimated Reward: $200 (based on volume=$227154)
2025-11-07 01:39:02,114 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,114 - market_scanner_v2 - INFO -    - Competition: 0.933612 bars, Score: 29.35
2025-11-07 01:39:02,114 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,114 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Katie Wilson win the 2025 Seattle mayoral election?
2025-11-07 01:39:02,114 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:39:02,114 - market_scanner_v2 - INFO -    - Estimated Reward: $30 (based on volume=$51648)
2025-11-07 01:39:02,115 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,115 - market_scanner_v2 - INFO -    - Competition: 2.258143 bars, Score: -205.65
2025-11-07 01:39:02,115 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,115 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Roaring Kitty tweet again by December 31?
2025-11-07 01:39:02,115 - market_scanner_v2 - INFO -    - Category: science
2025-11-07 01:39:02,115 - market_scanner_v2 - INFO -    - Estimated Reward: $15 (based on volume=$213)
2025-11-07 01:39:02,115 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,115 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 7.52
2025-11-07 01:39:02,115 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,115 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Russia capture Kostyantynivka by December 31?
2025-11-07 01:39:02,115 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:39:02,115 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$20214)
2025-11-07 01:39:02,116 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:39:02,116 - market_scanner_v2 - INFO -    - Competition: 2.449 bars, Score: -237.88
2025-11-07 01:39:02,116 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:39:02,116 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 99/2840 markets passed
2025-11-07 01:39:02,116 - market_scanner_v2 - INFO -    - 2344 rejected: reward < $10
2025-11-07 01:39:02,116 - market_scanner_v2 - INFO -    - 204 rejected: competition > 3
2025-11-07 01:39:02,117 - market_scanner_v2 - INFO -    - 173 rejected: category not in ['crypto', 'sports', 'politics', 'science', 'entertainment']
2025-11-07 01:39:02,117 - market_scanner_v2 - INFO -    - 20 rejected: volume = 0 (no liquidity)
2025-11-07 01:39:02,117 - market_scanner_v2 - INFO - ðŸ” Verifying orderbook for top 50 markets...
2025-11-07 01:39:06,114 - market_scanner_v2 - INFO -    Progress: 10/50 markets verified...
2025-11-07 01:39:10,577 - market_scanner_v2 - INFO -    Progress: 20/50 markets verified...
2025-11-07 01:39:15,056 - market_scanner_v2 - INFO -    Progress: 30/50 markets verified...
2025-11-07 01:39:19,561 - market_scanner_v2 - INFO -    Progress: 40/50 markets verified...
2025-11-07 01:39:24,026 - market_scanner_v2 - INFO -    Progress: 50/50 markets verified...
2025-11-07 01:39:24,484 - market_scanner_v2 - INFO - âœ… Found 99 qualifying markets (from 2840 total)
2025-11-07 01:39:24,488 - market_selector - INFO - Selected 2 markets from 99 candidates
2025-11-07 01:39:25,796 - order_manager - INFO - ðŸ“Š Orderbook for market 653215:
2025-11-07 01:39:25,796 - order_manager - INFO -    Best Bid: $0.0010 (0.10Â¢)
2025-11-07 01:39:25,796 - order_manager - INFO -    Best Ask: $0.9990 (99.90Â¢)
2025-11-07 01:39:25,796 - order_manager - INFO -    Mid Price: $0.5000 (50.00Â¢)
2025-11-07 01:39:25,796 - order_manager - INFO -    Spread: $0.9980 (99.80Â¢)
2025-11-07 01:39:25,796 - order_manager - INFO -    Spread %: 99800.00%
2025-11-07 01:39:25,796 - order_manager - INFO -    Top 3 Bids:
2025-11-07 01:39:25,796 - order_manager - INFO -       1. $0.0010 (0.10Â¢) x 21339
2025-11-07 01:39:25,797 - order_manager - INFO -       2. $0.0020 (0.20Â¢) x 10017
2025-11-07 01:39:25,797 - order_manager - INFO -       3. $0.0030 (0.30Â¢) x 200
2025-11-07 01:39:25,797 - order_manager - INFO -    Top 3 Asks:
2025-11-07 01:39:25,797 - order_manager - INFO -       1. $0.9990 (99.90Â¢) x 13736
2025-11-07 01:39:25,797 - order_manager - INFO -       2. $0.9980 (99.80Â¢) x 10010
2025-11-07 01:39:25,797 - order_manager - INFO -       3. $0.9970 (99.70Â¢) x 10000
2025-11-07 01:39:25,797 - order_manager - INFO - ðŸ’° Calculated prices:
2025-11-07 01:39:25,797 - order_manager - INFO -    Midpoint: $0.5000 (50.00Â¢)
2025-11-07 01:39:25,797 - order_manager - INFO -    YES: $0.0020 (0.20Â¢) at position 3
2025-11-07 01:39:25,797 - order_manager - INFO -    YES spread from mid: 99.60%
2025-11-07 01:39:25,797 - order_manager - INFO -    NO: $0.0020 (0.20Â¢) at position 3
2025-11-07 01:39:25,797 - order_manager - INFO -    NO as YES equivalent: $0.9980 (99.80Â¢)
2025-11-07 01:39:25,797 - order_manager - INFO -    NO spread from mid: 99.60%
2025-11-07 01:39:25,797 - order_manager - INFO -    Max spread: 99.60% (allowed: 3.50%)
2025-11-07 01:39:25,797 - order_manager - WARNING - âŒ Calculated prices exceed max spread (99.60% > 3.50%)
2025-11-07 01:39:25,798 - order_manager - WARNING -    This indicates orderbook is too thin or position 2-3 is too far from midpoint
2025-11-07 01:39:25,798 - order_manager - WARNING -    REJECTING market to avoid placing order at position #1 (best bid/ask)
2025-11-07 01:39:25,798 - order_manager - WARNING -    Reason: Adjusting to max spread would place order too close to best bid/ask
2025-11-07 01:39:25,798 - order_manager - WARNING -    â†’ High risk of being filled immediately!
2025-11-07 01:39:25,798 - order_manager - WARNING - Could not calculate valid prices for market 653215
2025-11-07 01:39:25,798 - __main__ - WARNING - âš ï¸  Skipped market 653215 - could not prepare valid order (spread too high or orderbook too thin)
2025-11-07 01:39:26,155 - order_manager - INFO - ðŸ“Š Orderbook for market 663184:
2025-11-07 01:39:26,155 - order_manager - INFO -    Best Bid: $0.0100 (1.00Â¢)
2025-11-07 01:39:26,155 - order_manager - INFO -    Best Ask: $0.9900 (99.00Â¢)
2025-11-07 01:39:26,155 - order_manager - INFO -    Mid Price: $0.5000 (50.00Â¢)
2025-11-07 01:39:26,155 - order_manager - INFO -    Spread: $0.9800 (98.00Â¢)
2025-11-07 01:39:26,155 - order_manager - INFO -    Spread %: 9800.00%
2025-11-07 01:39:26,155 - order_manager - INFO -    Top 3 Bids:
2025-11-07 01:39:26,155 - order_manager - INFO -       1. $0.0100 (1.00Â¢) x 16
2025-11-07 01:39:26,156 - order_manager - INFO -       2. $0.0300 (3.00Â¢) x 233
2025-11-07 01:39:26,156 - order_manager - INFO -       3. $0.0500 (5.00Â¢) x 17
2025-11-07 01:39:26,156 - order_manager - INFO -    Top 3 Asks:
2025-11-07 01:39:26,156 - order_manager - INFO -       1. $0.9900 (99.00Â¢) x 18
2025-11-07 01:39:26,156 - order_manager - INFO -       2. $0.9800 (98.00Â¢) x 350
2025-11-07 01:39:26,156 - order_manager - INFO -       3. $0.9700 (97.00Â¢) x 10
2025-11-07 01:39:26,156 - order_manager - INFO - ðŸ’° Calculated prices:
2025-11-07 01:39:26,156 - order_manager - INFO -    Midpoint: $0.5000 (50.00Â¢)
2025-11-07 01:39:26,156 - order_manager - INFO -    YES: $0.0490 (4.90Â¢) at position 3
2025-11-07 01:39:26,156 - order_manager - INFO -    YES spread from mid: 90.20%
2025-11-07 01:39:26,156 - order_manager - INFO -    NO: $0.0290 (2.90Â¢) at position 3
2025-11-07 01:39:26,156 - order_manager - INFO -    NO as YES equivalent: $0.9710 (97.10Â¢)
2025-11-07 01:39:26,156 - order_manager - INFO -    NO spread from mid: 94.20%
2025-11-07 01:39:26,156 - order_manager - INFO -    Max spread: 94.20% (allowed: 3.50%)
2025-11-07 01:39:26,156 - order_manager - WARNING - âŒ Calculated prices exceed max spread (94.20% > 3.50%)
2025-11-07 01:39:26,156 - order_manager - WARNING -    This indicates orderbook is too thin or position 2-3 is too far from midpoint
2025-11-07 01:39:26,156 - order_manager - WARNING -    REJECTING market to avoid placing order at position #1 (best bid/ask)
2025-11-07 01:39:26,156 - order_manager - WARNING -    Reason: Adjusting to max spread would place order too close to best bid/ask
2025-11-07 01:39:26,156 - order_manager - WARNING -    â†’ High risk of being filled immediately!
2025-11-07 01:39:26,156 - order_manager - WARNING - Could not calculate valid prices for market 663184
2025-11-07 01:39:26,156 - __main__ - WARNING - âš ï¸  Skipped market 663184 - could not prepare valid order (spread too high or orderbook too thin)
2025-11-07 01:40:29,166 - __main__ - WARNING - âš ï¸ Health check failed: 2 issues
2025-11-07 01:40:29,167 - __main__ - WARNING -    - ðŸ”´ KhÃ´ng quÃ©t markets trong 64s!
2025-11-07 01:40:29,167 - __main__ - WARNING -    - âš ï¸ API cháº­m: 43.3s trung bÃ¬nh
2025-11-07 01:40:34,153 - market_scanner_v2 - INFO - ðŸŒ Scraping markets from /rewards page using Playwright...
2025-11-07 01:40:34,153 - playwright_rewards_scraper - INFO - ðŸŒ Fetching markets from /rewards API...
2025-11-07 01:40:34,153 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 1 (cursor: MA==)...
2025-11-07 01:40:34,601 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 1
2025-11-07 01:40:34,602 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 2 (cursor: MTAw)...
2025-11-07 01:40:35,264 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 2
2025-11-07 01:40:35,264 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 3 (cursor: MjAw)...
2025-11-07 01:40:35,930 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 3
2025-11-07 01:40:35,930 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 4 (cursor: MzAw)...
2025-11-07 01:40:36,788 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 4
2025-11-07 01:40:36,789 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 5 (cursor: NDAw)...
2025-11-07 01:40:37,440 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 5
2025-11-07 01:40:37,441 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 6 (cursor: NTAw)...
2025-11-07 01:40:38,067 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 6
2025-11-07 01:40:38,068 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 7 (cursor: NjAw)...
2025-11-07 01:40:38,702 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 7
2025-11-07 01:40:38,703 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 8 (cursor: NzAw)...
2025-11-07 01:40:39,378 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 8
2025-11-07 01:40:39,378 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 9 (cursor: ODAw)...
2025-11-07 01:40:39,877 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 9
2025-11-07 01:40:39,877 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 10 (cursor: OTAw)...
2025-11-07 01:40:40,746 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 10
2025-11-07 01:40:40,747 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 11 (cursor: MTAwMA==)...
2025-11-07 01:40:41,413 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 11
2025-11-07 01:40:41,414 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 12 (cursor: MTEwMA==)...
2025-11-07 01:40:42,072 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 12
2025-11-07 01:40:42,072 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 13 (cursor: MTIwMA==)...
2025-11-07 01:40:42,735 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 13
2025-11-07 01:40:42,735 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 14 (cursor: MTMwMA==)...
2025-11-07 01:40:43,392 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 14
2025-11-07 01:40:43,393 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 15 (cursor: MTQwMA==)...
2025-11-07 01:40:44,073 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 15
2025-11-07 01:40:44,074 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 16 (cursor: MTUwMA==)...
2025-11-07 01:40:44,718 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 16
2025-11-07 01:40:44,719 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 17 (cursor: MTYwMA==)...
2025-11-07 01:40:47,368 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 17
2025-11-07 01:40:47,368 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 18 (cursor: MTcwMA==)...
2025-11-07 01:40:47,802 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 18
2025-11-07 01:40:47,803 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 19 (cursor: MTgwMA==)...
2025-11-07 01:40:48,494 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 19
2025-11-07 01:40:48,495 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 20 (cursor: MTkwMA==)...
2025-11-07 01:40:49,163 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 20
2025-11-07 01:40:49,164 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 21 (cursor: MjAwMA==)...
2025-11-07 01:40:49,601 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 21
2025-11-07 01:40:49,602 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 22 (cursor: MjEwMA==)...
2025-11-07 01:40:50,338 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 22
2025-11-07 01:40:50,339 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 23 (cursor: MjIwMA==)...
2025-11-07 01:40:50,802 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 23
2025-11-07 01:40:50,802 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 24 (cursor: MjMwMA==)...
2025-11-07 01:40:51,286 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 24
2025-11-07 01:40:51,287 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 25 (cursor: MjQwMA==)...
2025-11-07 01:40:51,746 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 25
2025-11-07 01:40:51,746 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 26 (cursor: MjUwMA==)...
2025-11-07 01:40:52,604 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 26
2025-11-07 01:40:52,605 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 27 (cursor: MjYwMA==)...
2025-11-07 01:40:53,038 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 27
2025-11-07 01:40:53,039 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 28 (cursor: MjcwMA==)...
2025-11-07 01:40:53,592 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 28
2025-11-07 01:40:53,592 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 29 (cursor: MjgwMA==)...
2025-11-07 01:40:54,246 - playwright_rewards_scraper - INFO - âœ… Got 40 markets on page 29
2025-11-07 01:40:54,246 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 30 (cursor: LTE=)...
2025-11-07 01:40:54,532 - playwright_rewards_scraper - INFO - âœ… No more markets on page 30
2025-11-07 01:40:54,533 - playwright_rewards_scraper - INFO - âœ… Fetched 2839 total unique markets from /rewards API
2025-11-07 01:40:54,582 - market_scanner_v2 - INFO - âœ… Got 2839 markets from /rewards page
2025-11-07 01:40:54,582 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Kanye visit Israel by December 31?
2025-11-07 01:40:54,583 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:40:54,583 - market_scanner_v2 - INFO -    - Estimated Reward: $50 (based on volume=$64)
2025-11-07 01:40:54,583 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,583 - market_scanner_v2 - INFO -    - Competition: 1.029487 bars, Score: -77.94
2025-11-07 01:40:54,583 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,583 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Ukraine win Miss Universe 2025?
2025-11-07 01:40:54,583 - market_scanner_v2 - INFO -    - Category: science
2025-11-07 01:40:54,583 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$61)
2025-11-07 01:40:54,583 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,583 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.01
2025-11-07 01:40:54,583 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,583 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will China win Miss Universe 2025?
2025-11-07 01:40:54,583 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:40:54,583 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$66)
2025-11-07 01:40:54,583 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,583 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.01
2025-11-07 01:40:54,583 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,583 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Great Britain win Miss Universe 2025?
2025-11-07 01:40:54,583 - market_scanner_v2 - INFO -    - Category: science
2025-11-07 01:40:54,583 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$66)
2025-11-07 01:40:54,583 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,584 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.01
2025-11-07 01:40:54,584 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,584 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Spain win Miss Universe 2025?
2025-11-07 01:40:54,584 - market_scanner_v2 - INFO -    - Category: science
2025-11-07 01:40:54,584 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$66)
2025-11-07 01:40:54,584 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,584 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.01
2025-11-07 01:40:54,584 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,584 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel win Miss Universe 2025?
2025-11-07 01:40:54,584 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:40:54,584 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$66)
2025-11-07 01:40:54,584 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,584 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.01
2025-11-07 01:40:54,584 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,584 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Russia win Miss Universe 2025?
2025-11-07 01:40:54,584 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:40:54,584 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$61)
2025-11-07 01:40:54,584 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,584 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.01
2025-11-07 01:40:54,584 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,584 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Palestine win Miss Universe 2025?
2025-11-07 01:40:54,584 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:40:54,584 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$66)
2025-11-07 01:40:54,584 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,584 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.01
2025-11-07 01:40:54,584 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,585 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Howard Hughes Holdings (HHH) beat quarterly earnings?
2025-11-07 01:40:54,585 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:40:54,585 - market_scanner_v2 - INFO -    - Estimated Reward: $50 (based on volume=$110)
2025-11-07 01:40:54,585 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,585 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 25.01
2025-11-07 01:40:54,585 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,585 - market_scanner_v2 - INFO - âœ… ACCEPTED: Airbnb (ABNB) Up or Down on November 7?
2025-11-07 01:40:54,585 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:40:54,585 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$687)
2025-11-07 01:40:54,585 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,585 - market_scanner_v2 - INFO -    - Competition: 0.272 bars, Score: -17.13
2025-11-07 01:40:54,585 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,585 - market_scanner_v2 - INFO - âœ… ACCEPTED: Palantir (PLTR) Up or Down on November 7?
2025-11-07 01:40:54,585 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:40:54,585 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$30)
2025-11-07 01:40:54,585 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,585 - market_scanner_v2 - INFO -    - Competition: 1.294037 bars, Score: -119.40
2025-11-07 01:40:54,585 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,585 - market_scanner_v2 - INFO - âœ… ACCEPTED: NVIDIA (NVDA) Up or Down on November 7?
2025-11-07 01:40:54,585 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:40:54,585 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$71)
2025-11-07 01:40:54,585 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,585 - market_scanner_v2 - INFO -    - Competition: 0.43384 bars, Score: -33.38
2025-11-07 01:40:54,585 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,585 - market_scanner_v2 - INFO - âœ… ACCEPTED: Hang Seng (HSI) Up or Down on November 7?
2025-11-07 01:40:54,586 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:40:54,586 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$51)
2025-11-07 01:40:54,586 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,586 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-07 01:40:54,586 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,586 - market_scanner_v2 - INFO - âœ… ACCEPTED: Tesla (TSLA) Up or Down on November 7?
2025-11-07 01:40:54,586 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:40:54,586 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$184)
2025-11-07 01:40:54,586 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,586 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.02
2025-11-07 01:40:54,586 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,586 - market_scanner_v2 - INFO - âœ… ACCEPTED: DAX (DAX) Up or Down on November 7?
2025-11-07 01:40:54,586 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:40:54,586 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$24)
2025-11-07 01:40:54,586 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,586 - market_scanner_v2 - INFO -    - Competition: 1.071583 bars, Score: -97.16
2025-11-07 01:40:54,586 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,586 - market_scanner_v2 - INFO - âœ… ACCEPTED: FTSE 100 (UKX) Up or Down on November 7?
2025-11-07 01:40:54,586 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:40:54,586 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$150)
2025-11-07 01:40:54,586 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,586 - market_scanner_v2 - INFO -    - Competition: 1.071583 bars, Score: -97.14
2025-11-07 01:40:54,586 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,586 - market_scanner_v2 - INFO - âœ… ACCEPTED: Meta (META) Up or Down on November 7?
2025-11-07 01:40:54,586 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:40:54,586 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2)
2025-11-07 01:40:54,586 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,586 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.00
2025-11-07 01:40:54,586 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,587 - market_scanner_v2 - INFO - âœ… ACCEPTED: Dow Jones (DJI) Up or Down on November 7?
2025-11-07 01:40:54,587 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:40:54,587 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2)
2025-11-07 01:40:54,587 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,587 - market_scanner_v2 - INFO -    - Competition: 1.530833 bars, Score: -143.08
2025-11-07 01:40:54,587 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,587 - market_scanner_v2 - INFO - âœ… ACCEPTED: Google (GOOGL) Up or Down on November 7?
2025-11-07 01:40:54,587 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:40:54,587 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2)
2025-11-07 01:40:54,587 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,587 - market_scanner_v2 - INFO -    - Competition: 0.45925 bars, Score: -35.92
2025-11-07 01:40:54,587 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,587 - market_scanner_v2 - INFO - âœ… ACCEPTED: Amazon (AMZN) Up or Down on November 7?
2025-11-07 01:40:54,587 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:40:54,587 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$108)
2025-11-07 01:40:54,587 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,587 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-07 01:40:54,587 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,587 - market_scanner_v2 - INFO - âœ… ACCEPTED: Nasdaq 100 (NDX) Up or Down on November 7?
2025-11-07 01:40:54,587 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:40:54,587 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$64)
2025-11-07 01:40:54,587 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,587 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-07 01:40:54,587 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,587 - market_scanner_v2 - INFO - âœ… ACCEPTED: Microsoft (MSFT) Up or Down on November 7?
2025-11-07 01:40:54,587 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:40:54,587 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$150)
2025-11-07 01:40:54,588 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,588 - market_scanner_v2 - INFO -    - Competition: 1.126693 bars, Score: -102.65
2025-11-07 01:40:54,588 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,588 - market_scanner_v2 - INFO - âœ… ACCEPTED: Nikkei 225 (NIK) Up or Down on November 7?
2025-11-07 01:40:54,588 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:40:54,588 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$56)
2025-11-07 01:40:54,588 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,588 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-07 01:40:54,588 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,588 - market_scanner_v2 - INFO - âœ… ACCEPTED: S&P 500 (SPX) Up or Down on November 7?
2025-11-07 01:40:54,588 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:40:54,588 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$187)
2025-11-07 01:40:54,588 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,588 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.02
2025-11-07 01:40:54,588 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,588 - market_scanner_v2 - INFO - âœ… ACCEPTED: Apple (AAPL) Up or Down on November 7?
2025-11-07 01:40:54,588 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:40:54,588 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$12)
2025-11-07 01:40:54,588 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,588 - market_scanner_v2 - INFO -    - Competition: 0.085 bars, Score: 1.50
2025-11-07 01:40:54,588 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,588 - market_scanner_v2 - INFO - âœ… ACCEPTED: Consensys IPO closing market cap above $3B?
2025-11-07 01:40:54,588 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:40:54,588 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$660)
2025-11-07 01:40:54,588 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,588 - market_scanner_v2 - INFO -    - Competition: 2.756071 bars, Score: -265.54
2025-11-07 01:40:54,588 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,589 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel allow independent journalists into Gaza by Decem
2025-11-07 01:40:54,589 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:40:54,589 - market_scanner_v2 - INFO -    - Estimated Reward: $60 (based on volume=$9837)
2025-11-07 01:40:54,589 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,589 - market_scanner_v2 - INFO -    - Competition: 2.414158 bars, Score: -210.43
2025-11-07 01:40:54,589 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,589 - market_scanner_v2 - INFO - âœ… ACCEPTED: Trump announces new drug boat strike by November 7?
2025-11-07 01:40:54,589 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:40:54,589 - market_scanner_v2 - INFO -    - Estimated Reward: $15 (based on volume=$6592)
2025-11-07 01:40:54,589 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,589 - market_scanner_v2 - INFO -    - Competition: 1.481333 bars, Score: -139.97
2025-11-07 01:40:54,589 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,589 - market_scanner_v2 - INFO - âœ… ACCEPTED: Trump announces new drug boat strike by November 14?
2025-11-07 01:40:54,589 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:40:54,589 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$11390)
2025-11-07 01:40:54,589 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,589 - market_scanner_v2 - INFO -    - Competition: 0.823877 bars, Score: -76.25
2025-11-07 01:40:54,589 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,589 - market_scanner_v2 - INFO - âœ… ACCEPTED: NYMEX Crude Oil Futures (WTI) (CL=F) Up or Down on November 
2025-11-07 01:40:54,590 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:40:54,590 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2243)
2025-11-07 01:40:54,590 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,590 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.22
2025-11-07 01:40:54,590 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,590 - market_scanner_v2 - INFO - âœ… ACCEPTED: COMEX Silver Futures (SI=F) Up or Down on November 6?
2025-11-07 01:40:54,590 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:40:54,590 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$735)
2025-11-07 01:40:54,590 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,590 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.07
2025-11-07 01:40:54,590 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,590 - market_scanner_v2 - INFO - âœ… ACCEPTED: COMEX Gold Futures (GC=F) Up or Down on November 6?
2025-11-07 01:40:54,590 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:40:54,590 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$855)
2025-11-07 01:40:54,590 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,590 - market_scanner_v2 - INFO -    - Competition: 2.429 bars, Score: -232.81
2025-11-07 01:40:54,590 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,590 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Catalin Drula finish second in the 2025 Bucharest mayor
2025-11-07 01:40:54,590 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:40:54,590 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$709)
2025-11-07 01:40:54,590 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,590 - market_scanner_v2 - INFO -    - Competition: 0.760555 bars, Score: -70.98
2025-11-07 01:40:54,590 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,590 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Google Gemini 3 score at least 40% on Humanityâ€™s Last E
2025-11-07 01:40:54,590 - market_scanner_v2 - INFO -    - Category: science
2025-11-07 01:40:54,591 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$1131)
2025-11-07 01:40:54,591 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,591 - market_scanner_v2 - INFO -    - Competition: 2.727311 bars, Score: -262.62
2025-11-07 01:40:54,591 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,591 - market_scanner_v2 - INFO - âœ… ACCEPTED: U.S. Closes Airspace due to Government Shutdown?
2025-11-07 01:40:54,591 - market_scanner_v2 - INFO -    - Category: science
2025-11-07 01:40:54,591 - market_scanner_v2 - INFO -    - Estimated Reward: $50 (based on volume=$14330)
2025-11-07 01:40:54,591 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,591 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 26.43
2025-11-07 01:40:54,591 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,591 - market_scanner_v2 - INFO - âœ… ACCEPTED: NYMEX Crude Oil Futures (WTI) (CL=F) Up or Down on November 
2025-11-07 01:40:54,591 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:40:54,591 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$130)
2025-11-07 01:40:54,591 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,591 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-07 01:40:54,591 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,591 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Asia" or "Asian" 8+ times during C5+1 Summit
2025-11-07 01:40:54,591 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:40:54,591 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$7842)
2025-11-07 01:40:54,591 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,591 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.78
2025-11-07 01:40:54,591 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,591 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Million" or "Billion" or "Trillion" 12+ time
2025-11-07 01:40:54,592 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:40:54,592 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$6712)
2025-11-07 01:40:54,592 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,592 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.67
2025-11-07 01:40:54,592 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,592 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Thank you" 8+ times during C5+1 Summit on No
2025-11-07 01:40:54,592 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:40:54,592 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$8507)
2025-11-07 01:40:54,592 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,592 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.85
2025-11-07 01:40:54,592 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,592 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Biden" or "Obama" 4+ times during C5+1 Summi
2025-11-07 01:40:54,592 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:40:54,592 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$4101)
2025-11-07 01:40:54,592 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,592 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.41
2025-11-07 01:40:54,592 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,592 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Russia" or "China" 4+ times during C5+1 Summ
2025-11-07 01:40:54,592 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:40:54,592 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$7641)
2025-11-07 01:40:54,592 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,592 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.76
2025-11-07 01:40:54,592 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,592 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Nuclear" 2+ times during C5+1 Summit on Nove
2025-11-07 01:40:54,592 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:40:54,592 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$2305)
2025-11-07 01:40:54,592 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,592 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.23
2025-11-07 01:40:54,593 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,593 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Caspian Sea" during C5+1 Summit on November 
2025-11-07 01:40:54,593 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:40:54,593 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$6274)
2025-11-07 01:40:54,593 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,593 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.63
2025-11-07 01:40:54,593 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,593 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Boeing" during C5+1 Summit on November 6?
2025-11-07 01:40:54,593 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:40:54,593 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$4640)
2025-11-07 01:40:54,593 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,593 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.46
2025-11-07 01:40:54,593 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,593 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Rare Earth" or "Critical Mineral" during C5+
2025-11-07 01:40:54,593 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:40:54,593 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$8309)
2025-11-07 01:40:54,593 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,593 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.83
2025-11-07 01:40:54,593 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,593 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Energy" during C5+1 Summit on November 6?
2025-11-07 01:40:54,593 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:40:54,593 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$9825)
2025-11-07 01:40:54,593 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,593 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.98
2025-11-07 01:40:54,593 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,593 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Drug" during C5+1 Summit on November 6?
2025-11-07 01:40:54,593 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:40:54,593 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$2410)
2025-11-07 01:40:54,594 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,594 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.24
2025-11-07 01:40:54,594 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,594 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Soviet" during C5+1 Summit on November 6?
2025-11-07 01:40:54,594 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:40:54,594 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$3623)
2025-11-07 01:40:54,594 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,594 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.36
2025-11-07 01:40:54,594 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,594 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Best Equipment" during C5+1 Summit on Novemb
2025-11-07 01:40:54,594 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:40:54,594 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$548)
2025-11-07 01:40:54,594 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,594 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.05
2025-11-07 01:40:54,594 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,594 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Investment" during C5+1 Summit on November 6
2025-11-07 01:40:54,594 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:40:54,594 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$3839)
2025-11-07 01:40:54,594 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,594 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.38
2025-11-07 01:40:54,594 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,594 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Middle East" during C5+1 Summit on November 
2025-11-07 01:40:54,594 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:40:54,594 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$150)
2025-11-07 01:40:54,594 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,594 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.01
2025-11-07 01:40:54,594 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,594 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Azerbaijan" during C5+1 Summit on November 6
2025-11-07 01:40:54,594 - market_scanner_v2 - INFO -    - Category: science
2025-11-07 01:40:54,595 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$2317)
2025-11-07 01:40:54,595 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,595 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.23
2025-11-07 01:40:54,595 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,595 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "President Xi" during C5+1 Summit on November
2025-11-07 01:40:54,595 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:40:54,595 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$2352)
2025-11-07 01:40:54,595 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,595 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.24
2025-11-07 01:40:54,595 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,595 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Afghanistan" during C5+1 Summit on November 
2025-11-07 01:40:54,595 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:40:54,595 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$820)
2025-11-07 01:40:54,595 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,595 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.08
2025-11-07 01:40:54,595 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,595 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Eight wars" during C5+1 Summit on November 6
2025-11-07 01:40:54,595 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:40:54,595 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$3294)
2025-11-07 01:40:54,595 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,595 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.33
2025-11-07 01:40:54,595 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,595 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Dead Country" during C5+1 Summit on November
2025-11-07 01:40:54,595 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:40:54,595 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$3079)
2025-11-07 01:40:54,595 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,595 - market_scanner_v2 - INFO -    - Competition: 1.701 bars, Score: -164.79
2025-11-07 01:40:54,596 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,596 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Crypto" or "AI" during C5+1 Summit on Novemb
2025-11-07 01:40:54,596 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:40:54,596 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$6332)
2025-11-07 01:40:54,596 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,596 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.63
2025-11-07 01:40:54,596 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,596 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Claude pass Grok by November 15 on the UnifAI Polyarena
2025-11-07 01:40:54,596 - market_scanner_v2 - INFO -    - Category: science
2025-11-07 01:40:54,596 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$462)
2025-11-07 01:40:54,596 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,596 - market_scanner_v2 - INFO -    - Competition: 1.088 bars, Score: -103.75
2025-11-07 01:40:54,596 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,596 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Airbnb (ABNB) finish week of November 10 above $115?
2025-11-07 01:40:54,596 - market_scanner_v2 - INFO -    - Category: science
2025-11-07 01:40:54,596 - market_scanner_v2 - INFO -    - Estimated Reward: $15 (based on volume=$50)
2025-11-07 01:40:54,596 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,596 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 7.51
2025-11-07 01:40:54,596 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,596 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Airbnb (ABNB) finish week of November 10 above $125?
2025-11-07 01:40:54,596 - market_scanner_v2 - INFO -    - Category: science
2025-11-07 01:40:54,596 - market_scanner_v2 - INFO -    - Estimated Reward: $15 (based on volume=$694)
2025-11-07 01:40:54,596 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,596 - market_scanner_v2 - INFO -    - Competition: 0.15252 bars, Score: -7.68
2025-11-07 01:40:54,596 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,596 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Airbnb (ABNB) finish week of November 10 above $135?
2025-11-07 01:40:54,597 - market_scanner_v2 - INFO -    - Category: science
2025-11-07 01:40:54,597 - market_scanner_v2 - INFO -    - Estimated Reward: $15 (based on volume=$20)
2025-11-07 01:40:54,597 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,597 - market_scanner_v2 - INFO -    - Competition: 2.159934 bars, Score: -208.49
2025-11-07 01:40:54,597 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,597 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Netflix (NFLX) finish week of November 10 above $1,070?
2025-11-07 01:40:54,597 - market_scanner_v2 - INFO -    - Category: entertainment
2025-11-07 01:40:54,597 - market_scanner_v2 - INFO -    - Estimated Reward: $15 (based on volume=$150)
2025-11-07 01:40:54,597 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,597 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 7.51
2025-11-07 01:40:54,597 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,597 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Airbnb (ABNB) close above $140 end of November?
2025-11-07 01:40:54,597 - market_scanner_v2 - INFO -    - Category: science
2025-11-07 01:40:54,597 - market_scanner_v2 - INFO -    - Estimated Reward: $15 (based on volume=$104)
2025-11-07 01:40:54,597 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,597 - market_scanner_v2 - INFO -    - Competition: 1.60472 bars, Score: -152.96
2025-11-07 01:40:54,598 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,598 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Netflix (NFLX) close above $1,080 end of November?
2025-11-07 01:40:54,598 - market_scanner_v2 - INFO -    - Category: entertainment
2025-11-07 01:40:54,598 - market_scanner_v2 - INFO -    - Estimated Reward: $15 (based on volume=$125)
2025-11-07 01:40:54,598 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,598 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 7.51
2025-11-07 01:40:54,598 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,598 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Microstrategy announce a Bitcoin purchase November 4-10
2025-11-07 01:40:54,598 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:40:54,598 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$10868)
2025-11-07 01:40:54,598 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,598 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 6.09
2025-11-07 01:40:54,598 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,598 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Elon Musk post 220-239 tweets from November 4 to Novemb
2025-11-07 01:40:54,598 - market_scanner_v2 - INFO -    - Category: entertainment
2025-11-07 01:40:54,599 - market_scanner_v2 - INFO -    - Estimated Reward: $21 (based on volume=$14327)
2025-11-07 01:40:54,599 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,599 - market_scanner_v2 - INFO -    - Competition: 2.907286 bars, Score: -278.80
2025-11-07 01:40:54,599 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,599 - market_scanner_v2 - INFO - âœ… ACCEPTED: Hezbollah strike on Israel by December 31?
2025-11-07 01:40:54,599 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:40:54,599 - market_scanner_v2 - INFO -    - Estimated Reward: $50 (based on volume=$14904)
2025-11-07 01:40:54,599 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,599 - market_scanner_v2 - INFO -    - Competition: 1.250694 bars, Score: -98.58
2025-11-07 01:40:54,599 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,599 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Airbnb reach $136 in November?
2025-11-07 01:40:54,599 - market_scanner_v2 - INFO -    - Category: science
2025-11-07 01:40:54,599 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$5)
2025-11-07 01:40:54,599 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,599 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.00
2025-11-07 01:40:54,599 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,600 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Lebanon on November 7?
2025-11-07 01:40:54,600 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:40:54,600 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$11321)
2025-11-07 01:40:54,600 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,600 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 11.13
2025-11-07 01:40:54,600 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,600 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Lebanon on November 8?
2025-11-07 01:40:54,600 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:40:54,600 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2258)
2025-11-07 01:40:54,600 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,600 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.23
2025-11-07 01:40:54,600 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,600 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Lebanon on November 11?
2025-11-07 01:40:54,600 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:40:54,600 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$906)
2025-11-07 01:40:54,600 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,600 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.09
2025-11-07 01:40:54,601 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,601 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Lebanon on November 12?
2025-11-07 01:40:54,601 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:40:54,601 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$609)
2025-11-07 01:40:54,601 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,601 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.06
2025-11-07 01:40:54,601 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,601 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Lebanon on November 13?
2025-11-07 01:40:54,601 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:40:54,601 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$491)
2025-11-07 01:40:54,601 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,601 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.05
2025-11-07 01:40:54,601 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,601 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Lebanon on November 14?
2025-11-07 01:40:54,601 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:40:54,601 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$1346)
2025-11-07 01:40:54,601 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,601 - market_scanner_v2 - INFO -    - Competition: 0.790598 bars, Score: -68.93
2025-11-07 01:40:54,601 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,601 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Gaza on November 7?
2025-11-07 01:40:54,601 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:40:54,601 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$1948)
2025-11-07 01:40:54,601 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,601 - market_scanner_v2 - INFO -    - Competition: 2.6611 bars, Score: -255.92
2025-11-07 01:40:54,601 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,601 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Gaza on November 8?
2025-11-07 01:40:54,601 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:40:54,602 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$702)
2025-11-07 01:40:54,602 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,602 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.07
2025-11-07 01:40:54,602 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,602 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Gaza on November 9?
2025-11-07 01:40:54,602 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:40:54,602 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$205)
2025-11-07 01:40:54,602 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,602 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.02
2025-11-07 01:40:54,602 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,602 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Gaza on November 10?
2025-11-07 01:40:54,602 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:40:54,602 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$279)
2025-11-07 01:40:54,602 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,602 - market_scanner_v2 - INFO -    - Competition: 2.916227 bars, Score: -281.59
2025-11-07 01:40:54,602 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,602 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Gaza on November 11?
2025-11-07 01:40:54,602 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:40:54,602 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$58)
2025-11-07 01:40:54,602 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,602 - market_scanner_v2 - INFO -    - Competition: 1.922306 bars, Score: -182.22
2025-11-07 01:40:54,602 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,602 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Gaza on November 14?
2025-11-07 01:40:54,602 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:40:54,602 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$265)
2025-11-07 01:40:54,602 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,602 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.03
2025-11-07 01:40:54,602 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,603 - market_scanner_v2 - INFO - âœ… ACCEPTED: Park Sung-jae in jail by November 30?
2025-11-07 01:40:54,603 - market_scanner_v2 - INFO -    - Category: science
2025-11-07 01:40:54,603 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$3469)
2025-11-07 01:40:54,603 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,603 - market_scanner_v2 - INFO -    - Competition: 1.202566 bars, Score: -114.91
2025-11-07 01:40:54,603 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,603 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Elon Musk post 140-159 tweets from October 31 to Novemb
2025-11-07 01:40:54,603 - market_scanner_v2 - INFO -    - Category: entertainment
2025-11-07 01:40:54,603 - market_scanner_v2 - INFO -    - Estimated Reward: $200 (based on volume=$225332)
2025-11-07 01:40:54,603 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,603 - market_scanner_v2 - INFO -    - Competition: 0.144732 bars, Score: 108.06
2025-11-07 01:40:54,603 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,603 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Elon Musk post 160-179 tweets from October 31 to Novemb
2025-11-07 01:40:54,603 - market_scanner_v2 - INFO -    - Category: entertainment
2025-11-07 01:40:54,603 - market_scanner_v2 - INFO -    - Estimated Reward: $130 (based on volume=$164904)
2025-11-07 01:40:54,603 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,603 - market_scanner_v2 - INFO -    - Competition: 0.032933 bars, Score: 78.20
2025-11-07 01:40:54,603 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,604 - market_scanner_v2 - INFO - âœ… ACCEPTED: Canton FDV above $3B one day after launch?
2025-11-07 01:40:54,604 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:40:54,604 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$1115)
2025-11-07 01:40:54,605 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,605 - market_scanner_v2 - INFO -    - Competition: 2.780549 bars, Score: -267.94
2025-11-07 01:40:54,605 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,605 - market_scanner_v2 - INFO - âœ… ACCEPTED: Canton FDV above $5B one day after launch?
2025-11-07 01:40:54,605 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:40:54,605 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$857)
2025-11-07 01:40:54,605 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,605 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.09
2025-11-07 01:40:54,605 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,605 - market_scanner_v2 - INFO - âœ… ACCEPTED: Canton FDV above $10B one day after launch?
2025-11-07 01:40:54,605 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:40:54,605 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$725)
2025-11-07 01:40:54,605 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,605 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.07
2025-11-07 01:40:54,605 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,605 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will the next Dutch government be GL/PvdA + VVD + D66?
2025-11-07 01:40:54,605 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:40:54,605 - market_scanner_v2 - INFO -    - Estimated Reward: $30 (based on volume=$23278)
2025-11-07 01:40:54,605 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,605 - market_scanner_v2 - INFO -    - Competition: 0.887037 bars, Score: -71.38
2025-11-07 01:40:54,605 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,606 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump establish a Gaza â€œBoard of Peaceâ€ in 2025?
2025-11-07 01:40:54,606 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:40:54,606 - market_scanner_v2 - INFO -    - Estimated Reward: $30 (based on volume=$6039)
2025-11-07 01:40:54,606 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,606 - market_scanner_v2 - INFO -    - Competition: 1.9152 bars, Score: -175.92
2025-11-07 01:40:54,606 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,607 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will MetaMask launch a token in 2025?
2025-11-07 01:40:54,607 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:40:54,607 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$231159)
2025-11-07 01:40:54,607 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,607 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 28.12
2025-11-07 01:40:54,607 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,607 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will MetaMask launch a token by September 30, 2026?
2025-11-07 01:40:54,607 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-07 01:40:54,607 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$507)
2025-11-07 01:40:54,608 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,608 - market_scanner_v2 - INFO -    - Competition: 0.480281 bars, Score: -37.98
2025-11-07 01:40:54,608 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,608 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Matt Van Epps win TN-7 Special Election?
2025-11-07 01:40:54,608 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:40:54,608 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$2908)
2025-11-07 01:40:54,608 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,608 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.29
2025-11-07 01:40:54,608 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,608 - market_scanner_v2 - INFO - âœ… ACCEPTED: US x Venezuela military engagement by November 14?
2025-11-07 01:40:54,608 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:40:54,608 - market_scanner_v2 - INFO -    - Estimated Reward: $100 (based on volume=$79998)
2025-11-07 01:40:54,608 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,609 - market_scanner_v2 - INFO -    - Competition: 2.753472 bars, Score: -217.35
2025-11-07 01:40:54,609 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,609 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Katie Wilson win the 2025 Seattle mayoral election?
2025-11-07 01:40:54,609 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:40:54,609 - market_scanner_v2 - INFO -    - Estimated Reward: $30 (based on volume=$51648)
2025-11-07 01:40:54,609 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,609 - market_scanner_v2 - INFO -    - Competition: 2.258143 bars, Score: -205.65
2025-11-07 01:40:54,609 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,609 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Roaring Kitty tweet again by December 31?
2025-11-07 01:40:54,609 - market_scanner_v2 - INFO -    - Category: science
2025-11-07 01:40:54,609 - market_scanner_v2 - INFO -    - Estimated Reward: $15 (based on volume=$213)
2025-11-07 01:40:54,609 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,609 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 7.52
2025-11-07 01:40:54,609 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,610 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Russia capture Kostyantynivka by December 31?
2025-11-07 01:40:54,610 - market_scanner_v2 - INFO -    - Category: politics
2025-11-07 01:40:54,610 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$20214)
2025-11-07 01:40:54,610 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-07 01:40:54,610 - market_scanner_v2 - INFO -    - Competition: 2.449 bars, Score: -237.88
2025-11-07 01:40:54,610 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-07 01:40:54,611 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 95/2839 markets passed
2025-11-07 01:40:54,611 - market_scanner_v2 - INFO -    - 2344 rejected: reward < $10
2025-11-07 01:40:54,611 - market_scanner_v2 - INFO -    - 208 rejected: competition > 3
2025-11-07 01:40:54,611 - market_scanner_v2 - INFO -    - 173 rejected: category not in ['crypto', 'sports', 'politics', 'science', 'entertainment']
2025-11-07 01:40:54,611 - market_scanner_v2 - INFO -    - 19 rejected: volume = 0 (no liquidity)
2025-11-07 01:40:54,611 - market_scanner_v2 - INFO - ðŸ” Verifying orderbook for top 50 markets...
2025-11-07 01:40:58,676 - market_scanner_v2 - INFO -    Progress: 10/50 markets verified...
2025-11-07 01:41:00,169 - __main__ - WARNING - âš ï¸ Health check failed: 2 issues
2025-11-07 01:41:00,170 - __main__ - WARNING -    - ðŸ”´ KhÃ´ng quÃ©t markets trong 95s!
2025-11-07 01:41:00,170 - __main__ - WARNING -    - âš ï¸ API cháº­m: 43.3s trung bÃ¬nh
2025-11-07 01:41:03,801 - market_scanner_v2 - INFO -    Progress: 20/50 markets verified...
2025-11-07 01:41:08,218 - market_scanner_v2 - INFO -    Progress: 30/50 markets verified...
2025-11-07 01:41:12,603 - market_scanner_v2 - INFO -    Progress: 40/50 markets verified...
2025-11-07 01:41:17,042 - market_scanner_v2 - INFO -    Progress: 50/50 markets verified...
2025-11-07 01:41:17,464 - market_scanner_v2 - INFO - âœ… Found 95 qualifying markets (from 2839 total)
2025-11-07 01:41:17,468 - market_selector - INFO - Selected 2 markets from 95 candidates
2025-11-07 01:41:18,910 - order_manager - INFO - ðŸ“Š Orderbook for market 653215:
2025-11-07 01:41:18,911 - order_manager - INFO -    Best Bid: $0.0010 (0.10Â¢)
2025-11-07 01:41:18,911 - order_manager - INFO -    Best Ask: $0.9990 (99.90Â¢)
2025-11-07 01:41:18,911 - order_manager - INFO -    Mid Price: $0.5000 (50.00Â¢)
2025-11-07 01:41:18,911 - order_manager - INFO -    Spread: $0.9980 (99.80Â¢)
2025-11-07 01:41:18,911 - order_manager - INFO -    Spread %: 99800.00%
2025-11-07 01:41:18,911 - order_manager - INFO -    Top 3 Bids:
2025-11-07 01:41:18,911 - order_manager - INFO -       1. $0.0010 (0.10Â¢) x 21339
2025-11-07 01:41:18,911 - order_manager - INFO -       2. $0.0020 (0.20Â¢) x 10017
2025-11-07 01:41:18,911 - order_manager - INFO -       3. $0.0030 (0.30Â¢) x 200
2025-11-07 01:41:18,911 - order_manager - INFO -    Top 3 Asks:
2025-11-07 01:41:18,911 - order_manager - INFO -       1. $0.9990 (99.90Â¢) x 13736
2025-11-07 01:41:18,911 - order_manager - INFO -       2. $0.9980 (99.80Â¢) x 10010
2025-11-07 01:41:18,911 - order_manager - INFO -       3. $0.9970 (99.70Â¢) x 10000
2025-11-07 01:41:18,911 - order_manager - INFO - ðŸ’° Calculated prices:
2025-11-07 01:41:18,911 - order_manager - INFO -    Midpoint: $0.5000 (50.00Â¢)
2025-11-07 01:41:18,911 - order_manager - INFO -    YES: $0.0020 (0.20Â¢) at position 3
2025-11-07 01:41:18,911 - order_manager - INFO -    YES spread from mid: 99.60%
2025-11-07 01:41:18,911 - order_manager - INFO -    NO: $0.0020 (0.20Â¢) at position 3
2025-11-07 01:41:18,912 - order_manager - INFO -    NO as YES equivalent: $0.9980 (99.80Â¢)
2025-11-07 01:41:18,912 - order_manager - INFO -    NO spread from mid: 99.60%
2025-11-07 01:41:18,912 - order_manager - INFO -    Max spread: 99.60% (allowed: 3.50%)
2025-11-07 01:41:18,912 - order_manager - WARNING - âŒ Calculated prices exceed max spread (99.60% > 3.50%)
2025-11-07 01:41:18,912 - order_manager - WARNING -    This indicates orderbook is too thin or position 2-3 is too far from midpoint
2025-11-07 01:41:18,912 - order_manager - WARNING -    REJECTING market to avoid placing order at position #1 (best bid/ask)
2025-11-07 01:41:18,912 - order_manager - WARNING -    Reason: Adjusting to max spread would place order too close to best bid/ask
2025-11-07 01:41:18,912 - order_manager - WARNING -    â†’ High risk of being filled immediately!
2025-11-07 01:41:18,912 - order_manager - WARNING - Could not calculate valid prices for market 653215
2025-11-07 01:41:18,912 - __main__ - WARNING - âš ï¸  Skipped market 653215 - could not prepare valid order (spread too high or orderbook too thin)
2025-11-07 01:41:19,243 - order_manager - INFO - ðŸ“Š Orderbook for market 663184:
2025-11-07 01:41:19,243 - order_manager - INFO -    Best Bid: $0.0100 (1.00Â¢)
2025-11-07 01:41:19,243 - order_manager - INFO -    Best Ask: $0.9900 (99.00Â¢)
2025-11-07 01:41:19,244 - order_manager - INFO -    Mid Price: $0.5000 (50.00Â¢)
2025-11-07 01:41:19,244 - order_manager - INFO -    Spread: $0.9800 (98.00Â¢)
2025-11-07 01:41:19,244 - order_manager - INFO -    Spread %: 9800.00%
2025-11-07 01:41:19,244 - order_manager - INFO -    Top 3 Bids:
2025-11-07 01:41:19,244 - order_manager - INFO -       1. $0.0100 (1.00Â¢) x 16
2025-11-07 01:41:19,244 - order_manager - INFO -       2. $0.0300 (3.00Â¢) x 233
2025-11-07 01:41:19,244 - order_manager - INFO -       3. $0.0400 (4.00Â¢) x 10
2025-11-07 01:41:19,244 - order_manager - INFO -    Top 3 Asks:
2025-11-07 01:41:19,244 - order_manager - INFO -       1. $0.9900 (99.00Â¢) x 18
2025-11-07 01:41:19,244 - order_manager - INFO -       2. $0.9800 (98.00Â¢) x 350
2025-11-07 01:41:19,244 - order_manager - INFO -       3. $0.9700 (97.00Â¢) x 10
2025-11-07 01:41:19,244 - order_manager - INFO - ðŸ’° Calculated prices:
2025-11-07 01:41:19,244 - order_manager - INFO -    Midpoint: $0.5000 (50.00Â¢)
2025-11-07 01:41:19,244 - order_manager - INFO -    YES: $0.0390 (3.90Â¢) at position 3
2025-11-07 01:41:19,244 - order_manager - INFO -    YES spread from mid: 92.20%
2025-11-07 01:41:19,244 - order_manager - INFO -    NO: $0.0290 (2.90Â¢) at position 3
2025-11-07 01:41:19,244 - order_manager - INFO -    NO as YES equivalent: $0.9710 (97.10Â¢)
2025-11-07 01:41:19,244 - order_manager - INFO -    NO spread from mid: 94.20%
2025-11-07 01:41:19,244 - order_manager - INFO -    Max spread: 94.20% (allowed: 3.50%)
2025-11-07 01:41:19,244 - order_manager - WARNING - âŒ Calculated prices exceed max spread (94.20% > 3.50%)
2025-11-07 01:41:19,244 - order_manager - WARNING -    This indicates orderbook is too thin or position 2-3 is too far from midpoint
2025-11-07 01:41:19,244 - order_manager - WARNING -    REJECTING market to avoid placing order at position #1 (best bid/ask)
2025-11-07 01:41:19,244 - order_manager - WARNING -    Reason: Adjusting to max spread would place order too close to best bid/ask
2025-11-07 01:41:19,244 - order_manager - WARNING -    â†’ High risk of being filled immediately!
2025-11-07 01:41:19,244 - order_manager - WARNING - Could not calculate valid prices for market 663184
2025-11-07 01:41:19,244 - __main__ - WARNING - âš ï¸  Skipped market 663184 - could not prepare valid order (spread too high or orderbook too thin)
2025-11-07 01:41:51,297 - profit_taking_manager - INFO - ðŸ” Checking positions for wallet: 0x18F261DC...Ae4FfD96
2025-11-07 01:41:51,628 - profit_taking_manager - INFO - ðŸ“Š Found 3 active positions
2025-11-07 01:41:51,629 - profit_taking_manager - INFO - 
ðŸ“ˆ Position: Charlotte 49ers vs. East Carolina
2025-11-07 01:41:51,629 - profit_taking_manager - INFO -    Shares: 259.00 @ $0.1494
2025-11-07 01:41:51,629 - profit_taking_manager - INFO -    Current: $0.0385
2025-11-07 01:41:51,629 - profit_taking_manager - INFO -    P&L: $-28.73 (-74.23%)
2025-11-07 01:41:51,629 - profit_taking_manager - INFO -    â¸ï¸  Losing position - NOT closing (manual decision required)
2025-11-07 01:41:51,629 - profit_taking_manager - INFO - 
ðŸ“ˆ Position: Will Google Gemini 3 score at least 70% on the Fro
2025-11-07 01:41:51,629 - profit_taking_manager - INFO -    Shares: 68.00 @ $0.3900
2025-11-07 01:41:51,629 - profit_taking_manager - INFO -    Current: $0.0700
2025-11-07 01:41:51,629 - profit_taking_manager - INFO -    P&L: $-21.76 (-82.05%)
2025-11-07 01:41:51,629 - profit_taking_manager - INFO -    â¸ï¸  Losing position - NOT closing (manual decision required)
2025-11-07 01:41:51,629 - profit_taking_manager - INFO - 
ðŸ“ˆ Position: Syracuse vs. Miami
2025-11-07 01:41:51,629 - profit_taking_manager - INFO -    Shares: 66.00 @ $0.4900
2025-11-07 01:41:51,629 - profit_taking_manager - INFO -    Current: $0.0580
2025-11-07 01:41:51,629 - profit_taking_manager - INFO -    P&L: $-28.51 (-88.16%)
2025-11-07 01:41:51,629 - profit_taking_manager - INFO -    â¸ï¸  Losing position - NOT closing (manual decision required)
2025-11-07 01:41:51,629 - __main__ - INFO - â³ Next profit check in 300s
