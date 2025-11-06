2025-11-06 15:16:03,543 - __main__ - INFO - Shutdown signal received
2025-11-06 15:16:03,670 - __main__ - INFO - Shutting down bot...
2025-11-06 15:16:03,670 - order_manager - INFO - Cancelled 0 orders
2025-11-06 15:16:03,670 - __main__ - INFO - Bot shutdown complete
2025-11-06 15:17:34,787 - __main__ - INFO - âœ… Using MarketScannerV2 (Playwright + Gamma API)
2025-11-06 15:17:38,003 - __main__ - INFO - ðŸ“‚ Loading config from: config.yaml
2025-11-06 15:17:38,032 - __main__ - INFO - âœ… Config loaded successfully
2025-11-06 15:17:38,033 - __main__ - INFO -    - min_reward: 10
2025-11-06 15:17:38,033 - __main__ - INFO -    - max_competition_bars: 3
2025-11-06 15:17:38,033 - __main__ - INFO -    - interval: 60s
2025-11-06 15:17:38,033 - __main__ - INFO - âœ… Telegram alerts configured (Chat ID: -1003157421030)
2025-11-06 15:17:38,033 - __main__ - INFO - âœ… Webhook alerts configured
2025-11-06 15:17:38,033 - telegram_notifier - INFO - âœ… Telegram Notifier initialized (Chat ID: -1003157421030)
2025-11-06 15:17:38,033 - __main__ - INFO - âœ… Telegram Notifier initialized
2025-11-06 15:17:38,033 - market_scanner_v2 - INFO - ðŸ“Š Market Scanner initialized with min_reward=$10, max_competition=3
2025-11-06 15:17:38,033 - market_scanner_v2 - INFO - ðŸŽ¯ Target categories: crypto, sports, politics, science, entertainment
2025-11-06 15:17:38,033 - circuit_breaker - INFO - âœ… Circuit Breaker 'playwright_scraper' initialized (threshold=3, timeout=60s)
2025-11-06 15:17:38,033 - circuit_breaker - INFO - âœ… Circuit Breaker 'playwright_scraper' initialized (threshold=3, timeout=120s)
2025-11-06 15:17:38,033 - order_manager - INFO - CLOB client initialized successfully (read-only mode)
2025-11-06 15:17:38,042 - wallet_manager - INFO - Loading REAL wallets from .env
2025-11-06 15:17:38,048 - wallet_manager - INFO - âœ… Loaded wallet 1: 0x18F261DC...Ae4FfD96
2025-11-06 15:17:38,048 - wallet_manager - INFO - âœ… Successfully loaded 1 real wallets
2025-11-06 15:17:38,050 - ml_predictor - INFO - No pre-trained model found, using new model
2025-11-06 15:17:38,050 - monitoring_system - INFO - âœ… Monitoring System initialized
2025-11-06 15:17:38,050 - __main__ - INFO - âœ… Monitoring System enabled
2025-11-06 15:17:38,050 - __main__ - INFO - â­ï¸  Reward Manager disabled in config
2025-11-06 15:17:38,788 - profit_taking_manager - INFO - âœ… CLOB client initialized with API credentials
2025-11-06 15:17:38,789 - profit_taking_manager - INFO - âœ… Profit Taking Manager initialized
2025-11-06 15:17:38,789 - profit_taking_manager - INFO -    - Min profit: 5%
2025-11-06 15:17:38,789 - profit_taking_manager - INFO -    - Target profit: 10%
2025-11-06 15:17:38,789 - profit_taking_manager - INFO -    - Max profit: 150%
2025-11-06 15:17:38,789 - profit_taking_manager - INFO -    - Check interval: 300s
2025-11-06 15:17:38,789 - __main__ - INFO - âœ… Profit Taking Manager enabled
2025-11-06 15:17:38,789 - __main__ - INFO - All modules initialized successfully
2025-11-06 15:17:38,789 - __main__ - INFO - ðŸš€ Starting Polymarket Trading Bot...
2025-11-06 15:17:39,854 - __main__ - INFO - âœ… Startup alert sent via TelegramNotifier
2025-11-06 15:17:39,854 - __main__ - INFO - ðŸ” Checking USDC approval for wallets...
2025-11-06 15:17:40,060 - usdc_approver - INFO - âœ… Connected to Polygon RPC: https://polygon-mainnet.g.alchemy.com/v2/FQJnJWsEQ...
2025-11-06 15:17:40,060 - __main__ - INFO -    Checking wallet: 0x18F261DC...Ae4FfD96
2025-11-06 15:17:40,425 - __main__ - INFO -    Raw allowance: 16000000 (base units)
2025-11-06 15:17:40,425 - __main__ - INFO -    Allowance in USDC: 16.00 USDC
2025-11-06 15:17:40,425 - __main__ - INFO -    Required minimum: 100 USDC (test mode)
2025-11-06 15:17:40,425 - __main__ - WARNING - âš ï¸  USDC approval needed!
2025-11-06 15:17:40,425 - __main__ - WARNING -    Current: 16.00 USDC
2025-11-06 15:17:40,426 - __main__ - WARNING -    Required: 100 USDC (test mode)
2025-11-06 15:17:40,426 - __main__ - WARNING -    Run: python scripts/approve_wallets.py
2025-11-06 15:17:40,426 - __main__ - WARNING -    Or the bot may fail to place orders
2025-11-06 15:17:40,426 - __main__ - WARNING - 
2025-11-06 15:17:40,426 - __main__ - WARNING -    âš ï¸  NOTE: 100 USDC is for TESTING only!
2025-11-06 15:17:40,426 - __main__ - WARNING -    For production, approve at least 1,000 USDC
2025-11-06 15:17:40,426 - __main__ - INFO - ðŸ” Starting market scanning loop
2025-11-06 15:17:40,426 - market_scanner_v2 - INFO - ðŸŒ Scraping markets from /rewards page using Playwright...
2025-11-06 15:17:40,426 - playwright_rewards_scraper - INFO - ðŸŒ Fetching markets from /rewards API...
2025-11-06 15:17:40,426 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 1 (cursor: MA==)...
2025-11-06 15:17:40,427 - __main__ - INFO - ðŸ“¦ Starting order management loop
2025-11-06 15:17:40,427 - __main__ - INFO - ðŸ‘ï¸  Starting position monitoring loop
2025-11-06 15:17:40,427 - __main__ - INFO - ðŸ›¡ï¸  Starting risk management loop
2025-11-06 15:17:40,427 - __main__ - INFO - ðŸ¤– Starting ML training loop
2025-11-06 15:17:40,427 - ml_predictor - INFO - Insufficient training data: 0 samples
2025-11-06 15:17:40,427 - __main__ - INFO - ML model updated successfully
2025-11-06 15:17:40,427 - __main__ - INFO - ðŸ“Š Starting daily optimization loop
2025-11-06 15:17:40,427 - __main__ - INFO - ðŸ¥ Starting health monitoring loop
2025-11-06 15:17:41,430 - __main__ - INFO - ðŸ“ˆ Starting hourly report loop
2025-11-06 15:17:41,430 - __main__ - INFO - ðŸ’° Starting automated profit taking loop
2025-11-06 15:17:41,430 - profit_taking_manager - INFO - ðŸ” Checking positions for wallet: 0x18F261DC...Ae4FfD96
2025-11-06 15:17:41,799 - profit_taking_manager - INFO - ðŸ“Š Found 4 active positions
2025-11-06 15:17:41,800 - profit_taking_manager - INFO - 
ðŸ“ˆ Position: Charlotte 49ers vs. East Carolina
2025-11-06 15:17:41,800 - profit_taking_manager - INFO -    Shares: 259.00 @ $0.1494
2025-11-06 15:17:41,800 - profit_taking_manager - INFO -    Current: $0.0385
2025-11-06 15:17:41,800 - profit_taking_manager - INFO -    P&L: $-28.73 (-74.23%)
2025-11-06 15:17:41,800 - profit_taking_manager - INFO -    â¸ï¸  Losing position - NOT closing (manual decision required)
2025-11-06 15:17:41,800 - profit_taking_manager - INFO - 
ðŸ“ˆ Position: Will Google Gemini 3 score at least 70% on the Fro
2025-11-06 15:17:41,800 - profit_taking_manager - INFO -    Shares: 68.00 @ $0.3900
2025-11-06 15:17:41,800 - profit_taking_manager - INFO -    Current: $0.0800
2025-11-06 15:17:41,800 - profit_taking_manager - INFO -    P&L: $-21.08 (-79.49%)
2025-11-06 15:17:41,800 - profit_taking_manager - INFO -    â¸ï¸  Losing position - NOT closing (manual decision required)
2025-11-06 15:17:41,800 - profit_taking_manager - INFO - 
ðŸ“ˆ Position: Syracuse vs. Miami
2025-11-06 15:17:41,800 - profit_taking_manager - INFO -    Shares: 66.00 @ $0.4900
2025-11-06 15:17:41,800 - profit_taking_manager - INFO -    Current: $0.0475
2025-11-06 15:17:41,800 - profit_taking_manager - INFO -    P&L: $-29.20 (-90.31%)
2025-11-06 15:17:41,800 - profit_taking_manager - INFO -    â¸ï¸  Losing position - NOT closing (manual decision required)
2025-11-06 15:17:41,800 - profit_taking_manager - INFO - 
ðŸ“ˆ Position: Will Netflix dip to $1050 in November?
2025-11-06 15:17:41,801 - profit_taking_manager - INFO -    Shares: 50.00 @ $0.3400
2025-11-06 15:17:41,801 - profit_taking_manager - INFO -    Current: $0.7500
2025-11-06 15:17:41,801 - profit_taking_manager - INFO -    P&L: $20.50 (+120.59%)
2025-11-06 15:17:41,801 - profit_taking_manager - INFO -    ðŸŽ¯ CLOSING: target_profit_reached (120.59% >= 10%)
2025-11-06 15:17:41,801 - profit_taking_manager - INFO - 
ðŸ”„ Placing SELL order for Will Netflix dip to $1050 in November?
2025-11-06 15:17:41,801 - profit_taking_manager - INFO -    Token ID: 109176985745730388398013053205590535560490868817001794547246190093921488790462
2025-11-06 15:17:41,801 - profit_taking_manager - INFO -    Shares: 50.00
2025-11-06 15:17:41,801 - profit_taking_manager - INFO -    Price: $0.7500
2025-11-06 15:17:41,801 - profit_taking_manager - INFO - ðŸ”§ Creating fresh signing client for SELL order...
2025-11-06 15:17:41,805 - profit_taking_manager - INFO - ðŸ”‘ Setting API credentials...
2025-11-06 15:17:42,485 - profit_taking_manager - INFO - âœ… API credentials set successfully for SELL order
2025-11-06 15:17:42,486 - profit_taking_manager - INFO - ðŸ“ Creating and signing SELL order...
2025-11-06 15:17:43,511 - profit_taking_manager - INFO - ðŸ“¤ Posting SELL order to CLOB...
2025-11-06 15:17:43,835 - profit_taking_manager - ERROR - âŒ Error closing position: PolyApiException[status_code=400, error_message={'error': 'invalid signature'}]
Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/profit_taking_manager.py", line 274, in _close_position
    resp = signing_client.post_order(signed_order, OrderType.GTC)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'invalid signature'}]
2025-11-06 15:17:43,838 - __main__ - INFO - â³ Next profit check in 300s
2025-11-06 15:17:44,546 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 1
2025-11-06 15:17:44,546 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 2 (cursor: MTAw)...
2025-11-06 15:17:45,226 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 2
2025-11-06 15:17:45,227 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 3 (cursor: MjAw)...
2025-11-06 15:17:45,932 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 3
2025-11-06 15:17:45,933 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 4 (cursor: MzAw)...
2025-11-06 15:17:46,387 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 4
2025-11-06 15:17:46,388 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 5 (cursor: NDAw)...
2025-11-06 15:17:47,053 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 5
2025-11-06 15:17:47,054 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 6 (cursor: NTAw)...
2025-11-06 15:17:47,709 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 6
2025-11-06 15:17:47,709 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 7 (cursor: NjAw)...
2025-11-06 15:17:48,373 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 7
2025-11-06 15:17:48,374 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 8 (cursor: NzAw)...
2025-11-06 15:17:49,066 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 8
2025-11-06 15:17:49,067 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 9 (cursor: ODAw)...
2025-11-06 15:17:49,530 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 9
2025-11-06 15:17:49,531 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 10 (cursor: OTAw)...
2025-11-06 15:17:49,979 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 10
2025-11-06 15:17:49,980 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 11 (cursor: MTAwMA==)...
2025-11-06 15:17:50,692 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 11
2025-11-06 15:17:50,693 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 12 (cursor: MTEwMA==)...
2025-11-06 15:17:51,371 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 12
2025-11-06 15:17:51,371 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 13 (cursor: MTIwMA==)...
2025-11-06 15:17:52,170 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 13
2025-11-06 15:17:52,171 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 14 (cursor: MTMwMA==)...
2025-11-06 15:17:52,646 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 14
2025-11-06 15:17:52,647 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 15 (cursor: MTQwMA==)...
2025-11-06 15:17:53,323 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 15
2025-11-06 15:17:53,323 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 16 (cursor: MTUwMA==)...
2025-11-06 15:17:53,794 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 16
2025-11-06 15:17:53,794 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 17 (cursor: MTYwMA==)...
2025-11-06 15:17:54,494 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 17
2025-11-06 15:17:54,494 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 18 (cursor: MTcwMA==)...
2025-11-06 15:17:55,006 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 18
2025-11-06 15:17:55,007 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 19 (cursor: MTgwMA==)...
2025-11-06 15:17:55,674 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 19
2025-11-06 15:17:55,675 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 20 (cursor: MTkwMA==)...
2025-11-06 15:17:56,340 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 20
2025-11-06 15:17:56,340 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 21 (cursor: MjAwMA==)...
2025-11-06 15:17:57,012 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 21
2025-11-06 15:17:57,012 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 22 (cursor: MjEwMA==)...
2025-11-06 15:17:57,701 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 22
2025-11-06 15:17:57,701 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 23 (cursor: MjIwMA==)...
2025-11-06 15:17:58,174 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 23
2025-11-06 15:17:58,175 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 24 (cursor: MjMwMA==)...
2025-11-06 15:17:58,847 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 24
2025-11-06 15:17:58,848 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 25 (cursor: MjQwMA==)...
2025-11-06 15:17:59,530 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 25
2025-11-06 15:17:59,531 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 26 (cursor: MjUwMA==)...
2025-11-06 15:18:00,200 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 26
2025-11-06 15:18:00,200 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 27 (cursor: MjYwMA==)...
2025-11-06 15:18:00,901 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 27
2025-11-06 15:18:00,902 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 28 (cursor: MjcwMA==)...
2025-11-06 15:18:01,607 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 28
2025-11-06 15:18:01,608 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 29 (cursor: MjgwMA==)...
2025-11-06 15:18:02,089 - playwright_rewards_scraper - INFO - âœ… Got 39 markets on page 29
2025-11-06 15:18:02,089 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 30 (cursor: LTE=)...
2025-11-06 15:18:02,395 - playwright_rewards_scraper - INFO - âœ… No more markets on page 30
2025-11-06 15:18:02,395 - playwright_rewards_scraper - INFO - âœ… Fetched 2835 total unique markets from /rewards API
2025-11-06 15:18:02,446 - market_scanner_v2 - INFO - âœ… Got 2835 markets from /rewards page
2025-11-06 15:18:02,446 - market_scanner_v2 - INFO - âœ… ACCEPTED: Consensys IPO closing market cap above $3B?
2025-11-06 15:18:02,446 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:18:02,446 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$26)
2025-11-06 15:18:02,446 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,446 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.00
2025-11-06 15:18:02,446 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,447 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will any Google Gemini 3 model score at least 1600 on LMAren
2025-11-06 15:18:02,447 - market_scanner_v2 - INFO -    - Category: science
2025-11-06 15:18:02,447 - market_scanner_v2 - INFO -    - Estimated Reward: $50 (based on volume=$9)
2025-11-06 15:18:02,447 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,447 - market_scanner_v2 - INFO -    - Competition: 1.411208 bars, Score: -116.12
2025-11-06 15:18:02,447 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,447 - market_scanner_v2 - INFO - âœ… ACCEPTED: Trump announces new drug boat strike by November 14?
2025-11-06 15:18:02,447 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:18:02,447 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$776)
2025-11-06 15:18:02,447 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,447 - market_scanner_v2 - INFO -    - Competition: 0.91143 bars, Score: -86.07
2025-11-06 15:18:02,447 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,447 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will â€œFrankensteinâ€ be the top global Netflix movie this wee
2025-11-06 15:18:02,447 - market_scanner_v2 - INFO -    - Category: entertainment
2025-11-06 15:18:02,447 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$3041)
2025-11-06 15:18:02,447 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,447 - market_scanner_v2 - INFO -    - Competition: 2.592857 bars, Score: -248.98
2025-11-06 15:18:02,447 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,448 - market_scanner_v2 - INFO - âœ… ACCEPTED: Airbnb (ABNB) Up or Down on November 6?
2025-11-06 15:18:02,448 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:18:02,448 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$7056)
2025-11-06 15:18:02,448 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,448 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.71
2025-11-06 15:18:02,448 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,448 - market_scanner_v2 - INFO - âœ… ACCEPTED: Rocket Lab (RKLB) Up or Down on November 6?
2025-11-06 15:18:02,448 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:18:02,448 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$4439)
2025-11-06 15:18:02,448 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,448 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.44
2025-11-06 15:18:02,448 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,448 - market_scanner_v2 - INFO - âœ… ACCEPTED: Opendoor (OPEN) Up or Down on November 6?
2025-11-06 15:18:02,448 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:18:02,448 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$4345)
2025-11-06 15:18:02,448 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,448 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.43
2025-11-06 15:18:02,448 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,448 - market_scanner_v2 - INFO - âœ… ACCEPTED: Palantir (PLTR) Up or Down on November 6?
2025-11-06 15:18:02,448 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:18:02,449 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$3118)
2025-11-06 15:18:02,449 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,449 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.31
2025-11-06 15:18:02,449 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,449 - market_scanner_v2 - INFO - âœ… ACCEPTED: NYA (NYA) Up or Down on November 6?
2025-11-06 15:18:02,449 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:18:02,449 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$4776)
2025-11-06 15:18:02,449 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,449 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.48
2025-11-06 15:18:02,449 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,449 - market_scanner_v2 - INFO - âœ… ACCEPTED: Netflix (NFLX) Up or Down on November 6?
2025-11-06 15:18:02,449 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:18:02,449 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$1972)
2025-11-06 15:18:02,449 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,449 - market_scanner_v2 - INFO -    - Competition: 1.360417 bars, Score: -125.84
2025-11-06 15:18:02,449 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,449 - market_scanner_v2 - INFO - âœ… ACCEPTED: Russell 2000 (RUT) Up or Down on November 6?
2025-11-06 15:18:02,449 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:18:02,449 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2856)
2025-11-06 15:18:02,449 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,449 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.29
2025-11-06 15:18:02,449 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,450 - market_scanner_v2 - INFO - âœ… ACCEPTED: NVIDIA (NVDA) Up or Down on November 6?
2025-11-06 15:18:02,450 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:18:02,450 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2086)
2025-11-06 15:18:02,450 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,450 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.21
2025-11-06 15:18:02,450 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,450 - market_scanner_v2 - INFO - âœ… ACCEPTED: Hang Seng (HSI) Up or Down on November 6?
2025-11-06 15:18:02,450 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:18:02,450 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2965)
2025-11-06 15:18:02,450 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,450 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.30
2025-11-06 15:18:02,450 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,450 - market_scanner_v2 - INFO - âœ… ACCEPTED: Tesla (TSLA) Up or Down on November 6?
2025-11-06 15:18:02,450 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:18:02,450 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2431)
2025-11-06 15:18:02,450 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,450 - market_scanner_v2 - INFO -    - Competition: 2.698448 bars, Score: -259.60
2025-11-06 15:18:02,450 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,450 - market_scanner_v2 - INFO - âœ… ACCEPTED: DAX (DAX) Up or Down on November 6?
2025-11-06 15:18:02,450 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:18:02,450 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2020)
2025-11-06 15:18:02,451 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,451 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.20
2025-11-06 15:18:02,451 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,451 - market_scanner_v2 - INFO - âœ… ACCEPTED: Meta (META) Up or Down on November 6?
2025-11-06 15:18:02,451 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:18:02,451 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2728)
2025-11-06 15:18:02,451 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,451 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.27
2025-11-06 15:18:02,451 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,451 - market_scanner_v2 - INFO - âœ… ACCEPTED: FTSE 100 (UKX) Up or Down on November 6?
2025-11-06 15:18:02,451 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:18:02,451 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$4234)
2025-11-06 15:18:02,451 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,451 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.42
2025-11-06 15:18:02,451 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,451 - market_scanner_v2 - INFO - âœ… ACCEPTED: Google (GOOGL) Up or Down on November 6?
2025-11-06 15:18:02,451 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:18:02,451 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$908)
2025-11-06 15:18:02,451 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,451 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.09
2025-11-06 15:18:02,451 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,451 - market_scanner_v2 - INFO - âœ… ACCEPTED: Dow Jones (DJI) Up or Down on November 6?
2025-11-06 15:18:02,452 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:18:02,452 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$4720)
2025-11-06 15:18:02,452 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,452 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.47
2025-11-06 15:18:02,452 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,452 - market_scanner_v2 - INFO - âœ… ACCEPTED: NYMEX Crude Oil Futures (WTI) (CL=F) Up or Down on November 
2025-11-06 15:18:02,452 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:18:02,452 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$920)
2025-11-06 15:18:02,452 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,452 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.09
2025-11-06 15:18:02,452 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,452 - market_scanner_v2 - INFO - âœ… ACCEPTED: Amazon (AMZN) Up or Down on November 6?
2025-11-06 15:18:02,452 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:18:02,452 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$5350)
2025-11-06 15:18:02,452 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,452 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.53
2025-11-06 15:18:02,452 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,452 - market_scanner_v2 - INFO - âœ… ACCEPTED: Nasdaq 100 (NDX) Up or Down on November 6?
2025-11-06 15:18:02,452 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:18:02,452 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$5109)
2025-11-06 15:18:02,452 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,452 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.51
2025-11-06 15:18:02,452 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,453 - market_scanner_v2 - INFO - âœ… ACCEPTED: COMEX Silver Futures (SI=F) Up or Down on November 6?
2025-11-06 15:18:02,453 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:18:02,453 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$702)
2025-11-06 15:18:02,453 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,453 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.07
2025-11-06 15:18:02,453 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,453 - market_scanner_v2 - INFO - âœ… ACCEPTED: Microsoft (MSFT) Up or Down on November 6?
2025-11-06 15:18:02,453 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:18:02,453 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2377)
2025-11-06 15:18:02,453 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,453 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.24
2025-11-06 15:18:02,453 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,453 - market_scanner_v2 - INFO - âœ… ACCEPTED: Nikkei 225 (NIK) Up or Down on November 6?
2025-11-06 15:18:02,453 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:18:02,453 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2526)
2025-11-06 15:18:02,453 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,453 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.25
2025-11-06 15:18:02,453 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,453 - market_scanner_v2 - INFO - âœ… ACCEPTED: COMEX Gold Futures (GC=F) Up or Down on November 6?
2025-11-06 15:18:02,453 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:18:02,453 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$792)
2025-11-06 15:18:02,453 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,454 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.08
2025-11-06 15:18:02,454 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,454 - market_scanner_v2 - INFO - âœ… ACCEPTED: S&P 500 (SPX) Up or Down on November 6?
2025-11-06 15:18:02,454 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:18:02,454 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$4717)
2025-11-06 15:18:02,454 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,454 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.47
2025-11-06 15:18:02,454 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,454 - market_scanner_v2 - INFO - âœ… ACCEPTED: Apple (AAPL) Up or Down on November 6?
2025-11-06 15:18:02,454 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:18:02,454 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2700)
2025-11-06 15:18:02,454 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,454 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.27
2025-11-06 15:18:02,454 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,454 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump establish a Gaza â€œBoard of Peaceâ€ by March 31?
2025-11-06 15:18:02,454 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:18:02,454 - market_scanner_v2 - INFO -    - Estimated Reward: $40 (based on volume=$563)
2025-11-06 15:18:02,454 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,454 - market_scanner_v2 - INFO -    - Competition: 1.013447 bars, Score: -81.29
2025-11-06 15:18:02,454 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,455 - market_scanner_v2 - INFO - âœ… ACCEPTED: NYMEX Crude Oil Futures (WTI) (CL=F) Up or Down on November 
2025-11-06 15:18:02,455 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:18:02,455 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$307)
2025-11-06 15:18:02,455 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,455 - market_scanner_v2 - INFO -    - Competition: 0.225 bars, Score: -12.47
2025-11-06 15:18:02,455 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,455 - market_scanner_v2 - INFO - âœ… ACCEPTED: COMEX Silver Futures (SI=F) Up or Down on November 5?
2025-11-06 15:18:02,455 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:18:02,455 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2845)
2025-11-06 15:18:02,455 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,455 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.28
2025-11-06 15:18:02,455 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,455 - market_scanner_v2 - INFO - âœ… ACCEPTED: COMEX Gold Futures (GC=F) Up or Down on November 5?
2025-11-06 15:18:02,455 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:18:02,455 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$416)
2025-11-06 15:18:02,455 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,455 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.04
2025-11-06 15:18:02,455 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,456 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Nancy Pelosi announce her retirement by November 30?
2025-11-06 15:18:02,456 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:18:02,456 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$3188)
2025-11-06 15:18:02,456 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,456 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.32
2025-11-06 15:18:02,456 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,456 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Nancy Pelosi announce her retirement by June 30, 2026?
2025-11-06 15:18:02,456 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:18:02,456 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$5093)
2025-11-06 15:18:02,456 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,456 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.51
2025-11-06 15:18:02,456 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,456 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Thank you" 8+ times during C5+1 Summit on No
2025-11-06 15:18:02,456 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:18:02,456 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$2347)
2025-11-06 15:18:02,457 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,457 - market_scanner_v2 - INFO -    - Competition: 1.798042 bars, Score: -174.57
2025-11-06 15:18:02,457 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,457 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Biden" or "Obama" 4+ times during C5+1 Summi
2025-11-06 15:18:02,457 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:18:02,457 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$1845)
2025-11-06 15:18:02,457 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,457 - market_scanner_v2 - INFO -    - Competition: 1.854472 bars, Score: -180.26
2025-11-06 15:18:02,457 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,457 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Russia" or "China" 4+ times during C5+1 Summ
2025-11-06 15:18:02,457 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:18:02,457 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$2268)
2025-11-06 15:18:02,457 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,457 - market_scanner_v2 - INFO -    - Competition: 2.120998 bars, Score: -206.87
2025-11-06 15:18:02,457 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,458 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Nuclear" 2+ times during C5+1 Summit on Nove
2025-11-06 15:18:02,458 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:18:02,458 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$1111)
2025-11-06 15:18:02,458 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,458 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.11
2025-11-06 15:18:02,458 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,458 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Rare Earth" or "Critical Mineral" during C5+
2025-11-06 15:18:02,458 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:18:02,458 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$1486)
2025-11-06 15:18:02,458 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,458 - market_scanner_v2 - INFO -    - Competition: 2.641991 bars, Score: -259.05
2025-11-06 15:18:02,458 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,458 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Drug" during C5+1 Summit on November 6?
2025-11-06 15:18:02,458 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:18:02,458 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$1165)
2025-11-06 15:18:02,458 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,459 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.12
2025-11-06 15:18:02,459 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,459 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Soviet" during C5+1 Summit on November 6?
2025-11-06 15:18:02,459 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:18:02,459 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$923)
2025-11-06 15:18:02,459 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,459 - market_scanner_v2 - INFO -    - Competition: 1.430832 bars, Score: -137.99
2025-11-06 15:18:02,459 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,459 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Best Equipment" during C5+1 Summit on Novemb
2025-11-06 15:18:02,459 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:18:02,459 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$163)
2025-11-06 15:18:02,459 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,459 - market_scanner_v2 - INFO -    - Competition: 0.764207 bars, Score: -71.40
2025-11-06 15:18:02,459 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,459 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Middle East" during C5+1 Summit on November 
2025-11-06 15:18:02,460 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:18:02,460 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$235)
2025-11-06 15:18:02,460 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,460 - market_scanner_v2 - INFO -    - Competition: 1.070083 bars, Score: -101.98
2025-11-06 15:18:02,460 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,460 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Azerbaijan" during C5+1 Summit on November 6
2025-11-06 15:18:02,460 - market_scanner_v2 - INFO -    - Category: science
2025-11-06 15:18:02,460 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$3218)
2025-11-06 15:18:02,460 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,460 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.32
2025-11-06 15:18:02,460 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,460 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Afghanistan" during C5+1 Summit on November 
2025-11-06 15:18:02,460 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:18:02,460 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$335)
2025-11-06 15:18:02,460 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,460 - market_scanner_v2 - INFO -    - Competition: 0.771046 bars, Score: -72.07
2025-11-06 15:18:02,461 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,461 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Eight wars" during C5+1 Summit on November 6
2025-11-06 15:18:02,461 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:18:02,461 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$1260)
2025-11-06 15:18:02,461 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,461 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.13
2025-11-06 15:18:02,461 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,461 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Dead Country" during C5+1 Summit on November
2025-11-06 15:18:02,461 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:18:02,461 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$1372)
2025-11-06 15:18:02,461 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,461 - market_scanner_v2 - INFO -    - Competition: 0.32604 bars, Score: -27.47
2025-11-06 15:18:02,461 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,463 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Microstrategy announce a Bitcoin purchase November 4-10
2025-11-06 15:18:02,463 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:18:02,463 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$15265)
2025-11-06 15:18:02,463 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,463 - market_scanner_v2 - INFO -    - Competition: 0.102 bars, Score: -3.67
2025-11-06 15:18:02,463 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,463 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trumpâ€™s approval rating be less than 42.5 on November 7
2025-11-06 15:18:02,464 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:18:02,464 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$1937)
2025-11-06 15:18:02,464 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,464 - market_scanner_v2 - INFO -    - Competition: 0.988 bars, Score: -93.61
2025-11-06 15:18:02,464 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,464 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike 1 country in November 2025?
2025-11-06 15:18:02,464 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:18:02,464 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$2000)
2025-11-06 15:18:02,464 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,464 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.20
2025-11-06 15:18:02,464 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,464 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike 2 countries in November 2025?
2025-11-06 15:18:02,464 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:18:02,465 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$205)
2025-11-06 15:18:02,465 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,465 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.02
2025-11-06 15:18:02,465 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,465 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Netflix reach $1155 in November?
2025-11-06 15:18:02,465 - market_scanner_v2 - INFO -    - Category: entertainment
2025-11-06 15:18:02,465 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$118)
2025-11-06 15:18:02,465 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,465 - market_scanner_v2 - INFO -    - Competition: 2.477698 bars, Score: -237.76
2025-11-06 15:18:02,465 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,465 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Netflix dip to $1050 in November?
2025-11-06 15:18:02,465 - market_scanner_v2 - INFO -    - Category: entertainment
2025-11-06 15:18:02,466 - market_scanner_v2 - INFO -    - Estimated Reward: $30 (based on volume=$165)
2025-11-06 15:18:02,466 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,466 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 15.02
2025-11-06 15:18:02,466 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,466 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Lebanon on November 8?
2025-11-06 15:18:02,466 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:18:02,466 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$365)
2025-11-06 15:18:02,466 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,466 - market_scanner_v2 - INFO -    - Competition: 0.0123 bars, Score: 8.81
2025-11-06 15:18:02,466 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,466 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Lebanon on November 9?
2025-11-06 15:18:02,466 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:18:02,467 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$282)
2025-11-06 15:18:02,467 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,467 - market_scanner_v2 - INFO -    - Competition: 1.820336 bars, Score: -172.01
2025-11-06 15:18:02,467 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,467 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Lebanon on November 11?
2025-11-06 15:18:02,467 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:18:02,467 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$820)
2025-11-06 15:18:02,467 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,467 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.08
2025-11-06 15:18:02,467 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,467 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Lebanon on November 12?
2025-11-06 15:18:02,467 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:18:02,467 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$94)
2025-11-06 15:18:02,467 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,467 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-06 15:18:02,467 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,467 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Lebanon on November 13?
2025-11-06 15:18:02,467 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:18:02,467 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$20)
2025-11-06 15:18:02,467 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,467 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.00
2025-11-06 15:18:02,467 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,467 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Lebanon on November 14?
2025-11-06 15:18:02,468 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:18:02,468 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$486)
2025-11-06 15:18:02,468 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,468 - market_scanner_v2 - INFO -    - Competition: 0.0328 bars, Score: 6.77
2025-11-06 15:18:02,468 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,468 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Gaza on November 7?
2025-11-06 15:18:02,468 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:18:02,468 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$458)
2025-11-06 15:18:02,468 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,468 - market_scanner_v2 - INFO -    - Competition: 0.230433 bars, Score: -13.00
2025-11-06 15:18:02,468 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,468 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Gaza on November 8?
2025-11-06 15:18:02,468 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:18:02,468 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$143)
2025-11-06 15:18:02,468 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,468 - market_scanner_v2 - INFO -    - Competition: 1.196895 bars, Score: -109.68
2025-11-06 15:18:02,468 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,468 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Gaza on November 9?
2025-11-06 15:18:02,468 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:18:02,468 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$264)
2025-11-06 15:18:02,468 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,468 - market_scanner_v2 - INFO -    - Competition: 0.035403 bars, Score: 6.49
2025-11-06 15:18:02,469 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,469 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Gaza on November 11?
2025-11-06 15:18:02,469 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:18:02,469 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$173)
2025-11-06 15:18:02,469 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,469 - market_scanner_v2 - INFO -    - Competition: 2.485664 bars, Score: -238.55
2025-11-06 15:18:02,469 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,469 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel launch a major ground offensive in Lebanon by De
2025-11-06 15:18:02,469 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:18:02,469 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$1547)
2025-11-06 15:18:02,469 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,469 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.15
2025-11-06 15:18:02,469 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,469 - market_scanner_v2 - INFO - âœ… ACCEPTED: Park Sung-jae in jail by November 30?
2025-11-06 15:18:02,469 - market_scanner_v2 - INFO -    - Category: science
2025-11-06 15:18:02,469 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$2915)
2025-11-06 15:18:02,469 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,469 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.29
2025-11-06 15:18:02,469 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,469 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Elon Musk post 160-179 tweets from October 31 to Novemb
2025-11-06 15:18:02,470 - market_scanner_v2 - INFO -    - Category: entertainment
2025-11-06 15:18:02,470 - market_scanner_v2 - INFO -    - Estimated Reward: $130 (based on volume=$92649)
2025-11-06 15:18:02,470 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,470 - market_scanner_v2 - INFO -    - Competition: 1.52642 bars, Score: -78.38
2025-11-06 15:18:02,470 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,470 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Elon Musk post 180-199 tweets from October 31 to Novemb
2025-11-06 15:18:02,470 - market_scanner_v2 - INFO -    - Category: entertainment
2025-11-06 15:18:02,470 - market_scanner_v2 - INFO -    - Estimated Reward: $30 (based on volume=$92908)
2025-11-06 15:18:02,470 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,470 - market_scanner_v2 - INFO -    - Competition: 1.947167 bars, Score: -170.43
2025-11-06 15:18:02,470 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,470 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Elon Muskâ€™s $1T Tesla pay deal pass?
2025-11-06 15:18:02,470 - market_scanner_v2 - INFO -    - Category: entertainment
2025-11-06 15:18:02,470 - market_scanner_v2 - INFO -    - Estimated Reward: $50 (based on volume=$89521)
2025-11-06 15:18:02,470 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,470 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 33.95
2025-11-06 15:18:02,470 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,471 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Stable launch a token in 2025?
2025-11-06 15:18:02,471 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:18:02,471 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$78233)
2025-11-06 15:18:02,471 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,471 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 12.82
2025-11-06 15:18:02,471 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,472 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump establish a Gaza â€œBoard of Peaceâ€ in 2025?
2025-11-06 15:18:02,472 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:18:02,472 - market_scanner_v2 - INFO -    - Estimated Reward: $30 (based on volume=$9651)
2025-11-06 15:18:02,472 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,472 - market_scanner_v2 - INFO -    - Competition: 0.396333 bars, Score: -23.67
2025-11-06 15:18:02,472 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,473 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will the Government shutdown end November 8-11?
2025-11-06 15:18:02,473 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:18:02,473 - market_scanner_v2 - INFO -    - Estimated Reward: $200 (based on volume=$192333)
2025-11-06 15:18:02,473 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,473 - market_scanner_v2 - INFO -    - Competition: 2.388585 bars, Score: -119.63
2025-11-06 15:18:02,473 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,473 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will the Government shutdown end November 12-15?
2025-11-06 15:18:02,473 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:18:02,473 - market_scanner_v2 - INFO -    - Estimated Reward: $200 (based on volume=$106409)
2025-11-06 15:18:02,473 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,473 - market_scanner_v2 - INFO -    - Competition: 1.056382 bars, Score: 5.00
2025-11-06 15:18:02,473 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,474 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will MetaMask launch a token by September 30, 2026?
2025-11-06 15:18:02,474 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:18:02,474 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$191)
2025-11-06 15:18:02,474 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,474 - market_scanner_v2 - INFO -    - Competition: 0.770902 bars, Score: -67.07
2025-11-06 15:18:02,474 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,474 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Matt Van Epps win TN-7 Special Election?
2025-11-06 15:18:02,474 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:18:02,474 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$1695)
2025-11-06 15:18:02,475 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,475 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.17
2025-11-06 15:18:02,475 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,475 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Russia capture all of Pokrovsk by November 14?
2025-11-06 15:18:02,475 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:18:02,475 - market_scanner_v2 - INFO -    - Estimated Reward: $30 (based on volume=$13354)
2025-11-06 15:18:02,475 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,475 - market_scanner_v2 - INFO -    - Competition: 0.272272 bars, Score: -10.89
2025-11-06 15:18:02,475 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,475 - market_scanner_v2 - INFO - âœ… ACCEPTED: US x Venezuela military engagement by December 31?
2025-11-06 15:18:02,475 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:18:02,475 - market_scanner_v2 - INFO -    - Estimated Reward: $70 (based on volume=$150217)
2025-11-06 15:18:02,475 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,475 - market_scanner_v2 - INFO -    - Competition: 2.210871 bars, Score: -171.07
2025-11-06 15:18:02,475 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,475 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Russia capture Siversk by December 31?
2025-11-06 15:18:02,476 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:18:02,476 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$3536)
2025-11-06 15:18:02,476 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,476 - market_scanner_v2 - INFO -    - Competition: 2.764163 bars, Score: -271.06
2025-11-06 15:18:02,476 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,476 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Gemini 3.0 be released by November 15?
2025-11-06 15:18:02,476 - market_scanner_v2 - INFO -    - Category: science
2025-11-06 15:18:02,476 - market_scanner_v2 - INFO -    - Estimated Reward: $200 (based on volume=$495622)
2025-11-06 15:18:02,476 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,476 - market_scanner_v2 - INFO -    - Competition: 1.3223 bars, Score: 17.33
2025-11-06 15:18:02,476 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,476 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Gemini 3.0 be released by November 22?
2025-11-06 15:18:02,476 - market_scanner_v2 - INFO -    - Category: science
2025-11-06 15:18:02,476 - market_scanner_v2 - INFO -    - Estimated Reward: $50 (based on volume=$14533)
2025-11-06 15:18:02,476 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,476 - market_scanner_v2 - INFO -    - Competition: 0.243152 bars, Score: 2.14
2025-11-06 15:18:02,476 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,476 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Bruce Harrell win the 2025 Seattle mayoral election?
2025-11-06 15:18:02,477 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:18:02,477 - market_scanner_v2 - INFO -    - Estimated Reward: $30 (based on volume=$76518)
2025-11-06 15:18:02,477 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,477 - market_scanner_v2 - INFO -    - Competition: 1.287467 bars, Score: -106.09
2025-11-06 15:18:02,477 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,477 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Katie Wilson win the 2025 Seattle mayoral election?
2025-11-06 15:18:02,477 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:18:02,477 - market_scanner_v2 - INFO -    - Estimated Reward: $30 (based on volume=$77169)
2025-11-06 15:18:02,477 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,477 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 22.72
2025-11-06 15:18:02,477 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,477 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Russia capture Myrnohrad by November 7?
2025-11-06 15:18:02,477 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:18:02,477 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$7500)
2025-11-06 15:18:02,477 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,477 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.75
2025-11-06 15:18:02,477 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,478 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Oscar Piastri finish second in the 2025 Drivers Champio
2025-11-06 15:18:02,478 - market_scanner_v2 - INFO -    - Category: entertainment
2025-11-06 15:18:02,478 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$119)
2025-11-06 15:18:02,478 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,478 - market_scanner_v2 - INFO -    - Competition: 0.204 bars, Score: -15.39
2025-11-06 15:18:02,478 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,478 - market_scanner_v2 - INFO - âœ… ACCEPTED: TikTok sale announced in 2025?
2025-11-06 15:18:02,478 - market_scanner_v2 - INFO -    - Category: entertainment
2025-11-06 15:18:02,478 - market_scanner_v2 - INFO -    - Estimated Reward: $30 (based on volume=$6818)
2025-11-06 15:18:02,478 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:18:02,478 - market_scanner_v2 - INFO -    - Competition: 1.647389 bars, Score: -149.06
2025-11-06 15:18:02,478 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:18:02,479 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 84/2835 markets passed
2025-11-06 15:18:02,479 - market_scanner_v2 - INFO -    - 2517 rejected: reward < $10
2025-11-06 15:18:02,479 - market_scanner_v2 - INFO -    - 200 rejected: competition > 3
2025-11-06 15:18:02,479 - market_scanner_v2 - INFO -    - 31 rejected: category not in ['crypto', 'sports', 'politics', 'science', 'entertainment']
2025-11-06 15:18:02,479 - market_scanner_v2 - INFO -    - 3 rejected: volume = 0 (no liquidity)
2025-11-06 15:18:02,479 - market_scanner_v2 - INFO - ðŸ” Verifying orderbook for top 50 markets...
2025-11-06 15:18:19,852 - market_scanner_v2 - INFO - âœ… Found 84 qualifying markets (from 2835 total)
2025-11-06 15:18:19,856 - market_selector - INFO - Selected 2 markets from 84 candidates
2025-11-06 15:18:22,260 - order_manager - WARNING - âŒ Calculated prices exceed max spread (99.80% > 3.50%)
2025-11-06 15:18:22,261 - order_manager - WARNING -    This indicates orderbook is too thin or position 2-3 is too far from midpoint
2025-11-06 15:18:22,261 - order_manager - WARNING -    REJECTING market to avoid placing order at position #1 (best bid/ask)
2025-11-06 15:18:22,261 - order_manager - WARNING -    Reason: Adjusting to max spread would place order too close to best bid/ask
2025-11-06 15:18:22,261 - order_manager - WARNING -    â†’ High risk of being filled immediately!
2025-11-06 15:18:22,261 - order_manager - WARNING - Could not calculate valid prices for market 644988
2025-11-06 15:18:22,261 - __main__ - WARNING - âš ï¸  Skipped market 644988 - could not prepare valid order (spread too high or orderbook too thin)
2025-11-06 15:18:22,593 - order_manager - WARNING - âŒ Calculated prices exceed max spread (96.20% > 3.50%)
2025-11-06 15:18:22,593 - order_manager - WARNING -    This indicates orderbook is too thin or position 2-3 is too far from midpoint
2025-11-06 15:18:22,593 - order_manager - WARNING -    REJECTING market to avoid placing order at position #1 (best bid/ask)
2025-11-06 15:18:22,593 - order_manager - WARNING -    Reason: Adjusting to max spread would place order too close to best bid/ask
2025-11-06 15:18:22,593 - order_manager - WARNING -    â†’ High risk of being filled immediately!
2025-11-06 15:18:22,594 - order_manager - WARNING - Could not calculate valid prices for market 657210
2025-11-06 15:18:22,594 - __main__ - WARNING - âš ï¸  Skipped market 657210 - could not prepare valid order (spread too high or orderbook too thin)
2025-11-06 15:19:21,413 - market_scanner_v2 - INFO - ðŸŒ Scraping markets from /rewards page using Playwright...
2025-11-06 15:19:21,413 - playwright_rewards_scraper - INFO - ðŸŒ Fetching markets from /rewards API...
2025-11-06 15:19:21,414 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 1 (cursor: MA==)...
2025-11-06 15:19:22,872 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 1
2025-11-06 15:19:22,873 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 2 (cursor: MTAw)...
2025-11-06 15:19:23,748 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 2
2025-11-06 15:19:23,749 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 3 (cursor: MjAw)...
2025-11-06 15:19:23,919 - ml_predictor - INFO - Alert sent: ðŸš¨ <b>MONITORING ALERT</b>

ðŸ”´ KhÃ´ng quÃ©t markets trong 62s!
2025-11-06 15:19:23,920 - monitoring_system - INFO - Alert sent: no_scan
2025-11-06 15:19:23,920 - __main__ - WARNING - âš ï¸ Health check failed: 2 issues
2025-11-06 15:19:23,920 - __main__ - WARNING -    - ðŸ”´ KhÃ´ng quÃ©t markets trong 62s!
2025-11-06 15:19:23,920 - __main__ - WARNING -    - âš ï¸ API cháº­m: 42.2s trung bÃ¬nh
2025-11-06 15:19:24,232 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 3
2025-11-06 15:19:24,233 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 4 (cursor: MzAw)...
2025-11-06 15:19:24,674 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 4
2025-11-06 15:19:24,674 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 5 (cursor: NDAw)...
2025-11-06 15:19:25,120 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 5
2025-11-06 15:19:25,121 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 6 (cursor: NTAw)...
2025-11-06 15:19:25,843 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 6
2025-11-06 15:19:25,843 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 7 (cursor: NjAw)...
2025-11-06 15:19:26,707 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 7
2025-11-06 15:19:26,708 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 8 (cursor: NzAw)...
2025-11-06 15:19:27,430 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 8
2025-11-06 15:19:27,430 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 9 (cursor: ODAw)...
2025-11-06 15:19:28,138 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 9
2025-11-06 15:19:28,139 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 10 (cursor: OTAw)...
2025-11-06 15:19:28,958 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 10
2025-11-06 15:19:28,959 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 11 (cursor: MTAwMA==)...
2025-11-06 15:19:29,620 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 11
2025-11-06 15:19:29,620 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 12 (cursor: MTEwMA==)...
2025-11-06 15:19:30,274 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 12
2025-11-06 15:19:30,274 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 13 (cursor: MTIwMA==)...
2025-11-06 15:19:30,751 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 13
2025-11-06 15:19:30,752 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 14 (cursor: MTMwMA==)...
2025-11-06 15:19:31,402 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 14
2025-11-06 15:19:31,402 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 15 (cursor: MTQwMA==)...
2025-11-06 15:19:32,081 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 15
2025-11-06 15:19:32,081 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 16 (cursor: MTUwMA==)...
2025-11-06 15:19:32,737 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 16
2025-11-06 15:19:32,738 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 17 (cursor: MTYwMA==)...
2025-11-06 15:19:33,610 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 17
2025-11-06 15:19:33,611 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 18 (cursor: MTcwMA==)...
2025-11-06 15:19:34,323 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 18
2025-11-06 15:19:34,324 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 19 (cursor: MTgwMA==)...
2025-11-06 15:19:34,985 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 19
2025-11-06 15:19:34,986 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 20 (cursor: MTkwMA==)...
2025-11-06 15:19:35,658 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 20
2025-11-06 15:19:35,658 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 21 (cursor: MjAwMA==)...
2025-11-06 15:19:36,322 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 21
2025-11-06 15:19:36,323 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 22 (cursor: MjEwMA==)...
2025-11-06 15:19:37,005 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 22
2025-11-06 15:19:37,007 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 23 (cursor: MjIwMA==)...
2025-11-06 15:19:37,445 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 23
2025-11-06 15:19:37,445 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 24 (cursor: MjMwMA==)...
2025-11-06 15:19:38,227 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 24
2025-11-06 15:19:38,227 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 25 (cursor: MjQwMA==)...
2025-11-06 15:19:38,945 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 25
2025-11-06 15:19:38,945 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 26 (cursor: MjUwMA==)...
2025-11-06 15:19:39,416 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 26
2025-11-06 15:19:39,417 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 27 (cursor: MjYwMA==)...
2025-11-06 15:19:40,084 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 27
2025-11-06 15:19:40,085 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 28 (cursor: MjcwMA==)...
2025-11-06 15:19:40,543 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 28
2025-11-06 15:19:40,544 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 29 (cursor: MjgwMA==)...
2025-11-06 15:19:41,000 - playwright_rewards_scraper - INFO - âœ… Got 39 markets on page 29
2025-11-06 15:19:41,000 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 30 (cursor: LTE=)...
2025-11-06 15:19:41,316 - playwright_rewards_scraper - INFO - âœ… No more markets on page 30
2025-11-06 15:19:41,317 - playwright_rewards_scraper - INFO - âœ… Fetched 2835 total unique markets from /rewards API
2025-11-06 15:19:41,366 - market_scanner_v2 - INFO - âœ… Got 2835 markets from /rewards page
2025-11-06 15:19:41,366 - market_scanner_v2 - INFO - âœ… ACCEPTED: Consensys IPO closing market cap above $3B?
2025-11-06 15:19:41,366 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:19:41,366 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$26)
2025-11-06 15:19:41,366 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,366 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.00
2025-11-06 15:19:41,366 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,367 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will any Google Gemini 3 model score at least 1600 on LMAren
2025-11-06 15:19:41,367 - market_scanner_v2 - INFO -    - Category: science
2025-11-06 15:19:41,367 - market_scanner_v2 - INFO -    - Estimated Reward: $50 (based on volume=$9)
2025-11-06 15:19:41,367 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,367 - market_scanner_v2 - INFO -    - Competition: 1.411208 bars, Score: -116.12
2025-11-06 15:19:41,367 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,367 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will â€œFrankensteinâ€ be the top global Netflix movie this wee
2025-11-06 15:19:41,367 - market_scanner_v2 - INFO -    - Category: entertainment
2025-11-06 15:19:41,367 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$3041)
2025-11-06 15:19:41,367 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,367 - market_scanner_v2 - INFO -    - Competition: 0.922133 bars, Score: -81.91
2025-11-06 15:19:41,367 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,367 - market_scanner_v2 - INFO - âœ… ACCEPTED: Airbnb (ABNB) Up or Down on November 6?
2025-11-06 15:19:41,367 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:19:41,367 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$7056)
2025-11-06 15:19:41,367 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,367 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.71
2025-11-06 15:19:41,367 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,367 - market_scanner_v2 - INFO - âœ… ACCEPTED: Rocket Lab (RKLB) Up or Down on November 6?
2025-11-06 15:19:41,367 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:19:41,367 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$4439)
2025-11-06 15:19:41,368 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,368 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.44
2025-11-06 15:19:41,368 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,368 - market_scanner_v2 - INFO - âœ… ACCEPTED: Opendoor (OPEN) Up or Down on November 6?
2025-11-06 15:19:41,368 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:19:41,368 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$4345)
2025-11-06 15:19:41,368 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,368 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.43
2025-11-06 15:19:41,368 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,368 - market_scanner_v2 - INFO - âœ… ACCEPTED: Palantir (PLTR) Up or Down on November 6?
2025-11-06 15:19:41,368 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:19:41,368 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$3118)
2025-11-06 15:19:41,368 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,368 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.31
2025-11-06 15:19:41,368 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,368 - market_scanner_v2 - INFO - âœ… ACCEPTED: NYA (NYA) Up or Down on November 6?
2025-11-06 15:19:41,368 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:19:41,368 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$4776)
2025-11-06 15:19:41,368 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,368 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.48
2025-11-06 15:19:41,368 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,368 - market_scanner_v2 - INFO - âœ… ACCEPTED: Netflix (NFLX) Up or Down on November 6?
2025-11-06 15:19:41,368 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:19:41,368 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$1972)
2025-11-06 15:19:41,368 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,368 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.20
2025-11-06 15:19:41,369 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,369 - market_scanner_v2 - INFO - âœ… ACCEPTED: Russell 2000 (RUT) Up or Down on November 6?
2025-11-06 15:19:41,369 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:19:41,369 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2856)
2025-11-06 15:19:41,369 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,369 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.29
2025-11-06 15:19:41,369 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,369 - market_scanner_v2 - INFO - âœ… ACCEPTED: NVIDIA (NVDA) Up or Down on November 6?
2025-11-06 15:19:41,369 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:19:41,369 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2086)
2025-11-06 15:19:41,369 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,369 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.21
2025-11-06 15:19:41,369 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,369 - market_scanner_v2 - INFO - âœ… ACCEPTED: Hang Seng (HSI) Up or Down on November 6?
2025-11-06 15:19:41,369 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:19:41,369 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2965)
2025-11-06 15:19:41,369 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,369 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.30
2025-11-06 15:19:41,369 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,369 - market_scanner_v2 - INFO - âœ… ACCEPTED: Tesla (TSLA) Up or Down on November 6?
2025-11-06 15:19:41,369 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:19:41,369 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2431)
2025-11-06 15:19:41,369 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,369 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.24
2025-11-06 15:19:41,369 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,369 - market_scanner_v2 - INFO - âœ… ACCEPTED: DAX (DAX) Up or Down on November 6?
2025-11-06 15:19:41,369 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:19:41,370 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2020)
2025-11-06 15:19:41,370 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,370 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.20
2025-11-06 15:19:41,370 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,370 - market_scanner_v2 - INFO - âœ… ACCEPTED: Meta (META) Up or Down on November 6?
2025-11-06 15:19:41,370 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:19:41,370 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2728)
2025-11-06 15:19:41,370 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,370 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.27
2025-11-06 15:19:41,370 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,370 - market_scanner_v2 - INFO - âœ… ACCEPTED: FTSE 100 (UKX) Up or Down on November 6?
2025-11-06 15:19:41,370 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:19:41,370 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$4234)
2025-11-06 15:19:41,370 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,370 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.42
2025-11-06 15:19:41,370 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,370 - market_scanner_v2 - INFO - âœ… ACCEPTED: Google (GOOGL) Up or Down on November 6?
2025-11-06 15:19:41,370 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:19:41,370 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$908)
2025-11-06 15:19:41,370 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,370 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.09
2025-11-06 15:19:41,370 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,370 - market_scanner_v2 - INFO - âœ… ACCEPTED: Dow Jones (DJI) Up or Down on November 6?
2025-11-06 15:19:41,370 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:19:41,370 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$4720)
2025-11-06 15:19:41,370 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,371 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.47
2025-11-06 15:19:41,371 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,371 - market_scanner_v2 - INFO - âœ… ACCEPTED: NYMEX Crude Oil Futures (WTI) (CL=F) Up or Down on November 
2025-11-06 15:19:41,371 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:19:41,371 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$920)
2025-11-06 15:19:41,371 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,371 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.09
2025-11-06 15:19:41,371 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,371 - market_scanner_v2 - INFO - âœ… ACCEPTED: Amazon (AMZN) Up or Down on November 6?
2025-11-06 15:19:41,371 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:19:41,371 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$5350)
2025-11-06 15:19:41,371 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,371 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.53
2025-11-06 15:19:41,371 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,371 - market_scanner_v2 - INFO - âœ… ACCEPTED: Nasdaq 100 (NDX) Up or Down on November 6?
2025-11-06 15:19:41,371 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:19:41,371 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$5109)
2025-11-06 15:19:41,371 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,371 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.51
2025-11-06 15:19:41,371 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,371 - market_scanner_v2 - INFO - âœ… ACCEPTED: COMEX Silver Futures (SI=F) Up or Down on November 6?
2025-11-06 15:19:41,371 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:19:41,371 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$702)
2025-11-06 15:19:41,371 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,371 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.07
2025-11-06 15:19:41,371 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,372 - market_scanner_v2 - INFO - âœ… ACCEPTED: Microsoft (MSFT) Up or Down on November 6?
2025-11-06 15:19:41,372 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:19:41,372 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2377)
2025-11-06 15:19:41,372 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,372 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.24
2025-11-06 15:19:41,372 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,372 - market_scanner_v2 - INFO - âœ… ACCEPTED: Nikkei 225 (NIK) Up or Down on November 6?
2025-11-06 15:19:41,372 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:19:41,372 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2526)
2025-11-06 15:19:41,372 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,372 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.25
2025-11-06 15:19:41,372 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,372 - market_scanner_v2 - INFO - âœ… ACCEPTED: COMEX Gold Futures (GC=F) Up or Down on November 6?
2025-11-06 15:19:41,372 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:19:41,372 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$792)
2025-11-06 15:19:41,372 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,372 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.08
2025-11-06 15:19:41,372 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,372 - market_scanner_v2 - INFO - âœ… ACCEPTED: S&P 500 (SPX) Up or Down on November 6?
2025-11-06 15:19:41,372 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:19:41,372 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$4717)
2025-11-06 15:19:41,372 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,372 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.47
2025-11-06 15:19:41,372 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,372 - market_scanner_v2 - INFO - âœ… ACCEPTED: Apple (AAPL) Up or Down on November 6?
2025-11-06 15:19:41,372 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:19:41,372 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2700)
2025-11-06 15:19:41,372 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,373 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.27
2025-11-06 15:19:41,373 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,373 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump establish a Gaza â€œBoard of Peaceâ€ by March 31?
2025-11-06 15:19:41,373 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:19:41,373 - market_scanner_v2 - INFO -    - Estimated Reward: $40 (based on volume=$563)
2025-11-06 15:19:41,373 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,373 - market_scanner_v2 - INFO -    - Competition: 0.984622 bars, Score: -78.41
2025-11-06 15:19:41,373 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,373 - market_scanner_v2 - INFO - âœ… ACCEPTED: NYMEX Crude Oil Futures (WTI) (CL=F) Up or Down on November 
2025-11-06 15:19:41,373 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:19:41,373 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$307)
2025-11-06 15:19:41,373 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,373 - market_scanner_v2 - INFO -    - Competition: 0.225 bars, Score: -12.47
2025-11-06 15:19:41,373 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,373 - market_scanner_v2 - INFO - âœ… ACCEPTED: COMEX Silver Futures (SI=F) Up or Down on November 5?
2025-11-06 15:19:41,373 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:19:41,373 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2845)
2025-11-06 15:19:41,373 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,373 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.28
2025-11-06 15:19:41,373 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,374 - market_scanner_v2 - INFO - âœ… ACCEPTED: COMEX Gold Futures (GC=F) Up or Down on November 5?
2025-11-06 15:19:41,374 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:19:41,374 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$416)
2025-11-06 15:19:41,374 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,374 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.04
2025-11-06 15:19:41,374 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,374 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Nancy Pelosi announce her retirement by November 30?
2025-11-06 15:19:41,374 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:19:41,374 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$3188)
2025-11-06 15:19:41,374 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,374 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.32
2025-11-06 15:19:41,374 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,374 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Nancy Pelosi announce her retirement by June 30, 2026?
2025-11-06 15:19:41,374 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:19:41,374 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$5093)
2025-11-06 15:19:41,374 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,374 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.51
2025-11-06 15:19:41,374 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,374 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Thank you" 8+ times during C5+1 Summit on No
2025-11-06 15:19:41,374 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:19:41,374 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$2347)
2025-11-06 15:19:41,374 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,374 - market_scanner_v2 - INFO -    - Competition: 1.755251 bars, Score: -170.29
2025-11-06 15:19:41,374 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,374 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Biden" or "Obama" 4+ times during C5+1 Summi
2025-11-06 15:19:41,374 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:19:41,374 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$1845)
2025-11-06 15:19:41,375 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,375 - market_scanner_v2 - INFO -    - Competition: 1.854472 bars, Score: -180.26
2025-11-06 15:19:41,375 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,375 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Russia" or "China" 4+ times during C5+1 Summ
2025-11-06 15:19:41,375 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:19:41,375 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$2268)
2025-11-06 15:19:41,375 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,375 - market_scanner_v2 - INFO -    - Competition: 2.120998 bars, Score: -206.87
2025-11-06 15:19:41,375 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,375 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Nuclear" 2+ times during C5+1 Summit on Nove
2025-11-06 15:19:41,375 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:19:41,375 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$1111)
2025-11-06 15:19:41,375 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,375 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.11
2025-11-06 15:19:41,375 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,375 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Rare Earth" or "Critical Mineral" during C5+
2025-11-06 15:19:41,375 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:19:41,375 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$1486)
2025-11-06 15:19:41,375 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,375 - market_scanner_v2 - INFO -    - Competition: 2.641991 bars, Score: -259.05
2025-11-06 15:19:41,375 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,375 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Drug" during C5+1 Summit on November 6?
2025-11-06 15:19:41,375 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:19:41,375 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$1165)
2025-11-06 15:19:41,375 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,376 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.12
2025-11-06 15:19:41,376 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,376 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Soviet" during C5+1 Summit on November 6?
2025-11-06 15:19:41,376 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:19:41,376 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$923)
2025-11-06 15:19:41,376 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,376 - market_scanner_v2 - INFO -    - Competition: 1.430832 bars, Score: -137.99
2025-11-06 15:19:41,376 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,376 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Best Equipment" during C5+1 Summit on Novemb
2025-11-06 15:19:41,376 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:19:41,376 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$163)
2025-11-06 15:19:41,376 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,376 - market_scanner_v2 - INFO -    - Competition: 0.764207 bars, Score: -71.40
2025-11-06 15:19:41,376 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,376 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Middle East" during C5+1 Summit on November 
2025-11-06 15:19:41,376 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:19:41,376 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$235)
2025-11-06 15:19:41,376 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,376 - market_scanner_v2 - INFO -    - Competition: 1.070083 bars, Score: -101.98
2025-11-06 15:19:41,376 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,376 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Azerbaijan" during C5+1 Summit on November 6
2025-11-06 15:19:41,376 - market_scanner_v2 - INFO -    - Category: science
2025-11-06 15:19:41,376 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$3218)
2025-11-06 15:19:41,376 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,376 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.32
2025-11-06 15:19:41,376 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,376 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Afghanistan" during C5+1 Summit on November 
2025-11-06 15:19:41,377 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:19:41,377 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$335)
2025-11-06 15:19:41,377 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,377 - market_scanner_v2 - INFO -    - Competition: 0.771046 bars, Score: -72.07
2025-11-06 15:19:41,377 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,377 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Eight wars" during C5+1 Summit on November 6
2025-11-06 15:19:41,377 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:19:41,377 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$1260)
2025-11-06 15:19:41,377 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,377 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.13
2025-11-06 15:19:41,377 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,377 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Dead Country" during C5+1 Summit on November
2025-11-06 15:19:41,377 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:19:41,377 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$1372)
2025-11-06 15:19:41,377 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,377 - market_scanner_v2 - INFO -    - Competition: 0.45764 bars, Score: -40.63
2025-11-06 15:19:41,377 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,378 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Microstrategy announce a Bitcoin purchase November 4-10
2025-11-06 15:19:41,378 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:19:41,378 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$15265)
2025-11-06 15:19:41,378 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,378 - market_scanner_v2 - INFO -    - Competition: 0.102 bars, Score: -3.67
2025-11-06 15:19:41,378 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,378 - market_scanner_v2 - INFO - âœ… ACCEPTED: Hezbollah strike on Israel by December 31?
2025-11-06 15:19:41,378 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:19:41,378 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$1441)
2025-11-06 15:19:41,378 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,378 - market_scanner_v2 - INFO -    - Competition: 2.927318 bars, Score: -287.59
2025-11-06 15:19:41,378 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,379 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trumpâ€™s approval rating be less than 42.5 on November 7
2025-11-06 15:19:41,379 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:19:41,379 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$1937)
2025-11-06 15:19:41,379 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,379 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.19
2025-11-06 15:19:41,379 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,379 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will ChatGPT be #1 Free App in the US Apple App Store on Nov
2025-11-06 15:19:41,379 - market_scanner_v2 - INFO -    - Category: science
2025-11-06 15:19:41,379 - market_scanner_v2 - INFO -    - Estimated Reward: $30 (based on volume=$46878)
2025-11-06 15:19:41,379 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,379 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 19.69
2025-11-06 15:19:41,379 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,379 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Sora by OpenAI be #1 Free App in the US Apple App Store
2025-11-06 15:19:41,379 - market_scanner_v2 - INFO -    - Category: science
2025-11-06 15:19:41,379 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$18451)
2025-11-06 15:19:41,379 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,379 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 6.85
2025-11-06 15:19:41,379 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,379 - market_scanner_v2 - INFO - âœ… ACCEPTED: Choo Kyung-ho in jail by November 30?
2025-11-06 15:19:41,379 - market_scanner_v2 - INFO -    - Category: science
2025-11-06 15:19:41,379 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$21433)
2025-11-06 15:19:41,379 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,379 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 7.14
2025-11-06 15:19:41,379 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,379 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike 1 country in November 2025?
2025-11-06 15:19:41,379 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:19:41,380 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$2000)
2025-11-06 15:19:41,380 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,380 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.20
2025-11-06 15:19:41,380 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,380 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike 2 countries in November 2025?
2025-11-06 15:19:41,380 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:19:41,380 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$205)
2025-11-06 15:19:41,380 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,380 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.02
2025-11-06 15:19:41,380 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,380 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Airbnb reach $128 in November?
2025-11-06 15:19:41,380 - market_scanner_v2 - INFO -    - Category: science
2025-11-06 15:19:41,380 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$35)
2025-11-06 15:19:41,380 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,380 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.00
2025-11-06 15:19:41,380 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,380 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Netflix reach $1243 in November?
2025-11-06 15:19:41,380 - market_scanner_v2 - INFO -    - Category: entertainment
2025-11-06 15:19:41,380 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$40)
2025-11-06 15:19:41,380 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,380 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.00
2025-11-06 15:19:41,380 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,380 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Netflix reach $1155 in November?
2025-11-06 15:19:41,380 - market_scanner_v2 - INFO -    - Category: entertainment
2025-11-06 15:19:41,381 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$118)
2025-11-06 15:19:41,381 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,381 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-06 15:19:41,381 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,381 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Netflix dip to $1050 in November?
2025-11-06 15:19:41,381 - market_scanner_v2 - INFO -    - Category: entertainment
2025-11-06 15:19:41,381 - market_scanner_v2 - INFO -    - Estimated Reward: $30 (based on volume=$165)
2025-11-06 15:19:41,381 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,381 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 15.02
2025-11-06 15:19:41,381 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,381 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Lebanon on November 8?
2025-11-06 15:19:41,381 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:19:41,381 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$365)
2025-11-06 15:19:41,381 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,381 - market_scanner_v2 - INFO -    - Competition: 0.0123 bars, Score: 8.81
2025-11-06 15:19:41,382 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,382 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Lebanon on November 9?
2025-11-06 15:19:41,382 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:19:41,382 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$282)
2025-11-06 15:19:41,382 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,382 - market_scanner_v2 - INFO -    - Competition: 1.820336 bars, Score: -172.01
2025-11-06 15:19:41,382 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,382 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Lebanon on November 11?
2025-11-06 15:19:41,382 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:19:41,382 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$820)
2025-11-06 15:19:41,382 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,382 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.08
2025-11-06 15:19:41,382 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,382 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Lebanon on November 12?
2025-11-06 15:19:41,382 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:19:41,382 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$94)
2025-11-06 15:19:41,382 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,382 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-06 15:19:41,382 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,382 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Lebanon on November 13?
2025-11-06 15:19:41,382 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:19:41,382 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$20)
2025-11-06 15:19:41,382 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,382 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.00
2025-11-06 15:19:41,382 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,382 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Lebanon on November 14?
2025-11-06 15:19:41,382 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:19:41,382 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$486)
2025-11-06 15:19:41,383 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,383 - market_scanner_v2 - INFO -    - Competition: 0.0328 bars, Score: 6.77
2025-11-06 15:19:41,383 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,383 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Gaza on November 7?
2025-11-06 15:19:41,383 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:19:41,383 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$458)
2025-11-06 15:19:41,383 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,383 - market_scanner_v2 - INFO -    - Competition: 0.230433 bars, Score: -13.00
2025-11-06 15:19:41,383 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,383 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Gaza on November 8?
2025-11-06 15:19:41,383 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:19:41,383 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$143)
2025-11-06 15:19:41,383 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,383 - market_scanner_v2 - INFO -    - Competition: 1.104667 bars, Score: -100.45
2025-11-06 15:19:41,383 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,383 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Gaza on November 9?
2025-11-06 15:19:41,383 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:19:41,383 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$264)
2025-11-06 15:19:41,383 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,383 - market_scanner_v2 - INFO -    - Competition: 0.035403 bars, Score: 6.49
2025-11-06 15:19:41,383 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,383 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Gaza on November 11?
2025-11-06 15:19:41,383 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:19:41,383 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$173)
2025-11-06 15:19:41,383 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,383 - market_scanner_v2 - INFO -    - Competition: 2.485664 bars, Score: -238.55
2025-11-06 15:19:41,383 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,384 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel launch a major ground offensive in Lebanon by De
2025-11-06 15:19:41,384 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:19:41,384 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$1547)
2025-11-06 15:19:41,384 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,384 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.15
2025-11-06 15:19:41,384 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,384 - market_scanner_v2 - INFO - âœ… ACCEPTED: Park Sung-jae in jail by November 30?
2025-11-06 15:19:41,384 - market_scanner_v2 - INFO -    - Category: science
2025-11-06 15:19:41,384 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$2915)
2025-11-06 15:19:41,384 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,384 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.29
2025-11-06 15:19:41,384 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,384 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Elon Musk post 160-179 tweets from October 31 to Novemb
2025-11-06 15:19:41,384 - market_scanner_v2 - INFO -    - Category: entertainment
2025-11-06 15:19:41,384 - market_scanner_v2 - INFO -    - Estimated Reward: $130 (based on volume=$92649)
2025-11-06 15:19:41,384 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,384 - market_scanner_v2 - INFO -    - Competition: 0.787013 bars, Score: -4.44
2025-11-06 15:19:41,384 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,384 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Elon Muskâ€™s $1T Tesla pay deal pass?
2025-11-06 15:19:41,384 - market_scanner_v2 - INFO -    - Category: entertainment
2025-11-06 15:19:41,385 - market_scanner_v2 - INFO -    - Estimated Reward: $50 (based on volume=$89521)
2025-11-06 15:19:41,385 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,385 - market_scanner_v2 - INFO -    - Competition: 1.9368 bars, Score: -159.73
2025-11-06 15:19:41,385 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,385 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Stable launch a token in 2025?
2025-11-06 15:19:41,385 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:19:41,385 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$78233)
2025-11-06 15:19:41,385 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,385 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 12.82
2025-11-06 15:19:41,385 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,386 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump establish a Gaza â€œBoard of Peaceâ€ in 2025?
2025-11-06 15:19:41,386 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:19:41,386 - market_scanner_v2 - INFO -    - Estimated Reward: $30 (based on volume=$9651)
2025-11-06 15:19:41,386 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,386 - market_scanner_v2 - INFO -    - Competition: 0.396333 bars, Score: -23.67
2025-11-06 15:19:41,386 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,387 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will the Government shutdown end November 8-11?
2025-11-06 15:19:41,387 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:19:41,387 - market_scanner_v2 - INFO -    - Estimated Reward: $200 (based on volume=$192333)
2025-11-06 15:19:41,387 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,387 - market_scanner_v2 - INFO -    - Competition: 1.638298 bars, Score: -44.60
2025-11-06 15:19:41,387 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,387 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will the Government shutdown end November 12-15?
2025-11-06 15:19:41,387 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:19:41,387 - market_scanner_v2 - INFO -    - Estimated Reward: $200 (based on volume=$106409)
2025-11-06 15:19:41,387 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,387 - market_scanner_v2 - INFO -    - Competition: 1.245167 bars, Score: -13.88
2025-11-06 15:19:41,387 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,388 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will MetaMask launch a token by September 30, 2026?
2025-11-06 15:19:41,388 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:19:41,388 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$191)
2025-11-06 15:19:41,388 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,388 - market_scanner_v2 - INFO -    - Competition: 0.770902 bars, Score: -67.07
2025-11-06 15:19:41,388 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,388 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Matt Van Epps win TN-7 Special Election?
2025-11-06 15:19:41,388 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:19:41,388 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$1695)
2025-11-06 15:19:41,388 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,388 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.17
2025-11-06 15:19:41,388 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,388 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Russia capture all of Pokrovsk by November 14?
2025-11-06 15:19:41,389 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:19:41,389 - market_scanner_v2 - INFO -    - Estimated Reward: $30 (based on volume=$13354)
2025-11-06 15:19:41,389 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,389 - market_scanner_v2 - INFO -    - Competition: 0.272272 bars, Score: -10.89
2025-11-06 15:19:41,389 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,389 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Russia capture Siversk by December 31?
2025-11-06 15:19:41,389 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:19:41,389 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$3536)
2025-11-06 15:19:41,389 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,389 - market_scanner_v2 - INFO -    - Competition: 2.764163 bars, Score: -271.06
2025-11-06 15:19:41,389 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,389 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Gemini 3.0 be released by November 15?
2025-11-06 15:19:41,389 - market_scanner_v2 - INFO -    - Category: science
2025-11-06 15:19:41,389 - market_scanner_v2 - INFO -    - Estimated Reward: $200 (based on volume=$495622)
2025-11-06 15:19:41,389 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,389 - market_scanner_v2 - INFO -    - Competition: 2.7243 bars, Score: -122.87
2025-11-06 15:19:41,389 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,389 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Gemini 3.0 be released by November 22?
2025-11-06 15:19:41,389 - market_scanner_v2 - INFO -    - Category: science
2025-11-06 15:19:41,389 - market_scanner_v2 - INFO -    - Estimated Reward: $50 (based on volume=$14533)
2025-11-06 15:19:41,390 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,390 - market_scanner_v2 - INFO -    - Competition: 1.010687 bars, Score: -74.62
2025-11-06 15:19:41,390 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,390 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Bruce Harrell win the 2025 Seattle mayoral election?
2025-11-06 15:19:41,390 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:19:41,390 - market_scanner_v2 - INFO -    - Estimated Reward: $30 (based on volume=$76518)
2025-11-06 15:19:41,390 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,390 - market_scanner_v2 - INFO -    - Competition: 1.287467 bars, Score: -106.09
2025-11-06 15:19:41,390 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,390 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Katie Wilson win the 2025 Seattle mayoral election?
2025-11-06 15:19:41,390 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:19:41,390 - market_scanner_v2 - INFO -    - Estimated Reward: $30 (based on volume=$77169)
2025-11-06 15:19:41,390 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,390 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 22.72
2025-11-06 15:19:41,390 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,390 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Russia capture Myrnohrad by November 7?
2025-11-06 15:19:41,390 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:19:41,390 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$7500)
2025-11-06 15:19:41,390 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,390 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.75
2025-11-06 15:19:41,390 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,391 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Oscar Piastri finish second in the 2025 Drivers Champio
2025-11-06 15:19:41,391 - market_scanner_v2 - INFO -    - Category: entertainment
2025-11-06 15:19:41,391 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$119)
2025-11-06 15:19:41,391 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:19:41,391 - market_scanner_v2 - INFO -    - Competition: 0.204 bars, Score: -15.39
2025-11-06 15:19:41,391 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:19:41,392 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 86/2835 markets passed
2025-11-06 15:19:41,392 - market_scanner_v2 - INFO -    - 2517 rejected: reward < $10
2025-11-06 15:19:41,392 - market_scanner_v2 - INFO -    - 192 rejected: competition > 3
2025-11-06 15:19:41,392 - market_scanner_v2 - INFO -    - 37 rejected: category not in ['crypto', 'sports', 'politics', 'science', 'entertainment']
2025-11-06 15:19:41,392 - market_scanner_v2 - INFO -    - 3 rejected: volume = 0 (no liquidity)
2025-11-06 15:19:41,392 - market_scanner_v2 - INFO - ðŸ” Verifying orderbook for top 50 markets...
