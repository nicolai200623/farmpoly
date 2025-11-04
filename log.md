2025-11-04 00:57:03,262 - __main__ - INFO - âœ… Using MarketScannerV2 (Playwright + Gamma API)
2025-11-04 00:57:12,438 - __main__ - INFO - âœ… Telegram alerts configured (Chat ID: -1003157421030)
2025-11-04 00:57:12,439 - __main__ - INFO - âœ… Webhook alerts configured
2025-11-04 00:57:12,440 - circuit_breaker - INFO - âœ… Circuit Breaker 'gamma_api' initialized (threshold=5, timeout=60s)
2025-11-04 00:57:12,440 - circuit_breaker - INFO - âœ… Circuit Breaker 'playwright_scraper' initialized (threshold=3, timeout=120s)
2025-11-04 00:57:12,440 - order_manager - INFO - CLOB client initialized successfully (read-only mode)
2025-11-04 00:57:12,452 - wallet_manager - INFO - Loading REAL wallets from .env
2025-11-04 00:57:12,462 - wallet_manager - INFO - âœ… Loaded wallet 1: 0x18F261DC...Ae4FfD96
2025-11-04 00:57:12,463 - wallet_manager - INFO - âœ… Successfully loaded 1 real wallets
2025-11-04 00:57:12,484 - ml_predictor - INFO - No pre-trained model found, using new model
2025-11-04 00:57:12,485 - monitoring_system - INFO - âœ… Monitoring System initialized
2025-11-04 00:57:12,485 - __main__ - INFO - âœ… Monitoring System enabled
2025-11-04 00:57:12,485 - __main__ - INFO - â­ï¸  Reward Manager disabled in config
2025-11-04 00:57:12,485 - __main__ - INFO - All modules initialized successfully
2025-11-04 00:57:12,485 - __main__ - INFO - ðŸš€ Starting Polymarket Trading Bot...
2025-11-04 00:57:13,210 - ml_predictor - INFO - Alert sent: ðŸš€ <b>Polymarket Bot Started</b>
â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”
â° Time: 2025-11-04 00:57:12
ðŸ’¼ Wallets: 1
ðŸ“Š Status: Running
â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”
Bot is now scanning markets and placing orders.
2025-11-04 00:57:13,210 - __main__ - INFO - âœ… Startup alert sent
2025-11-04 00:57:13,210 - __main__ - INFO - ðŸ” Checking USDC approval for wallets...
2025-11-04 00:57:13,351 - usdc_approver - INFO - âœ… Connected to Polygon RPC: https://polygon-mainnet.g.alchemy.com/v2/FQJnJWsEQ...
2025-11-04 00:57:13,351 - __main__ - INFO -    Checking wallet: 0x18F261DC...Ae4FfD96
2025-11-04 00:57:13,493 - __main__ - INFO -    Raw allowance: 100000000 (base units)
2025-11-04 00:57:13,493 - __main__ - INFO -    Allowance in USDC: 100.00 USDC
2025-11-04 00:57:13,493 - __main__ - INFO -    Required minimum: 100 USDC (test mode)
2025-11-04 00:57:13,493 - __main__ - INFO - âœ… USDC approval OK (100 USDC)
2025-11-04 00:57:13,493 - __main__ - WARNING -    âš ï¸  Running in TEST MODE with 100 USDC
2025-11-04 00:57:13,493 - __main__ - WARNING -    For production, approve at least 1,000 USDC
2025-11-04 00:57:13,493 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 00:57:13,494 - ml_predictor - INFO - Insufficient training data: 0 samples
2025-11-04 00:57:13,494 - __main__ - INFO - ML model updated successfully
2025-11-04 00:57:15,237 - market_scanner_v2 - INFO - âœ… Fetched 131 markets from API
2025-11-04 00:57:15,239 - market_scanner_v2 - INFO - âœ… Got 131 markets from API
2025-11-04 00:57:15,240 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 131/131 markets passed
2025-11-04 00:57:15,240 - market_scanner_v2 - INFO - âœ… Found 131 qualifying markets (from 131 total)
2025-11-04 00:57:15,243 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 00:57:20,239 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 00:57:20,983 - market_scanner_v2 - INFO - âœ… Fetched 131 markets from API
2025-11-04 00:57:20,987 - market_scanner_v2 - INFO - âœ… Got 131 markets from API
2025-11-04 00:57:20,988 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 131/131 markets passed
2025-11-04 00:57:20,988 - market_scanner_v2 - INFO - âœ… Found 131 qualifying markets (from 131 total)
2025-11-04 00:57:20,991 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 00:57:26,964 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 00:57:27,821 - market_scanner_v2 - INFO - âœ… Fetched 131 markets from API
2025-11-04 00:57:27,824 - market_scanner_v2 - INFO - âœ… Got 131 markets from API
2025-11-04 00:57:27,826 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 131/131 markets passed
2025-11-04 00:57:27,826 - market_scanner_v2 - INFO - âœ… Found 131 qualifying markets (from 131 total)
2025-11-04 00:57:27,828 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 00:57:33,434 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 00:57:34,299 - market_scanner_v2 - INFO - âœ… Fetched 131 markets from API
2025-11-04 00:57:34,302 - market_scanner_v2 - INFO - âœ… Got 131 markets from API
2025-11-04 00:57:34,304 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 131/131 markets passed
2025-11-04 00:57:34,304 - market_scanner_v2 - INFO - âœ… Found 131 qualifying markets (from 131 total)
2025-11-04 00:57:34,306 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 00:57:39,155 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 00:57:39,967 - market_scanner_v2 - INFO - âœ… Fetched 131 markets from API
2025-11-04 00:57:39,970 - market_scanner_v2 - INFO - âœ… Got 131 markets from API
2025-11-04 00:57:39,971 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 131/131 markets passed
2025-11-04 00:57:39,972 - market_scanner_v2 - INFO - âœ… Found 131 qualifying markets (from 131 total)
2025-11-04 00:57:39,974 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 00:57:45,592 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 00:57:46,304 - market_scanner_v2 - INFO - âœ… Fetched 131 markets from API
2025-11-04 00:57:46,307 - market_scanner_v2 - INFO - âœ… Got 131 markets from API
2025-11-04 00:57:46,308 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 131/131 markets passed
2025-11-04 00:57:46,308 - market_scanner_v2 - INFO - âœ… Found 131 qualifying markets (from 131 total)
2025-11-04 00:57:46,311 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 00:57:51,110 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 00:57:51,859 - market_scanner_v2 - INFO - âœ… Fetched 131 markets from API
2025-11-04 00:57:51,862 - market_scanner_v2 - INFO - âœ… Got 131 markets from API
2025-11-04 00:57:51,863 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 131/131 markets passed
2025-11-04 00:57:51,863 - market_scanner_v2 - INFO - âœ… Found 131 qualifying markets (from 131 total)
2025-11-04 00:57:51,865 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 00:57:56,710 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 00:57:57,692 - market_scanner_v2 - INFO - âœ… Fetched 131 markets from API
2025-11-04 00:57:57,695 - market_scanner_v2 - INFO - âœ… Got 131 markets from API
2025-11-04 00:57:57,697 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 131/131 markets passed
2025-11-04 00:57:57,697 - market_scanner_v2 - INFO - âœ… Found 131 qualifying markets (from 131 total)
2025-11-04 00:57:57,699 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 00:58:02,401 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 00:58:03,195 - market_scanner_v2 - INFO - âœ… Fetched 131 markets from API
2025-11-04 00:58:03,198 - market_scanner_v2 - INFO - âœ… Got 131 markets from API
2025-11-04 00:58:03,199 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 131/131 markets passed
2025-11-04 00:58:03,199 - market_scanner_v2 - INFO - âœ… Found 131 qualifying markets (from 131 total)
2025-11-04 00:58:03,202 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 00:58:08,467 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 00:58:09,255 - market_scanner_v2 - INFO - âœ… Fetched 131 markets from API
2025-11-04 00:58:09,258 - market_scanner_v2 - INFO - âœ… Got 131 markets from API
2025-11-04 00:58:09,258 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 131/131 markets passed
2025-11-04 00:58:09,259 - market_scanner_v2 - INFO - âœ… Found 131 qualifying markets (from 131 total)
2025-11-04 00:58:09,261 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 00:58:13,632 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 00:58:14,420 - market_scanner_v2 - INFO - âœ… Fetched 131 markets from API
2025-11-04 00:58:14,424 - market_scanner_v2 - INFO - âœ… Got 131 markets from API
2025-11-04 00:58:14,425 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 131/131 markets passed
2025-11-04 00:58:14,426 - market_scanner_v2 - INFO - âœ… Found 131 qualifying markets (from 131 total)
2025-11-04 00:58:14,428 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 00:58:19,147 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 00:58:19,937 - market_scanner_v2 - INFO - âœ… Fetched 131 markets from API
2025-11-04 00:58:19,940 - market_scanner_v2 - INFO - âœ… Got 131 markets from API
2025-11-04 00:58:19,941 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 131/131 markets passed
2025-11-04 00:58:19,941 - market_scanner_v2 - INFO - âœ… Found 131 qualifying markets (from 131 total)
2025-11-04 00:58:19,943 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 00:58:25,021 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 00:58:25,809 - market_scanner_v2 - INFO - âœ… Fetched 131 markets from API
2025-11-04 00:58:25,812 - market_scanner_v2 - INFO - âœ… Got 131 markets from API
2025-11-04 00:58:25,813 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 131/131 markets passed
2025-11-04 00:58:25,813 - market_scanner_v2 - INFO - âœ… Found 131 qualifying markets (from 131 total)
2025-11-04 00:58:25,815 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 00:58:30,334 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 00:58:31,125 - market_scanner_v2 - INFO - âœ… Fetched 131 markets from API
2025-11-04 00:58:31,127 - market_scanner_v2 - INFO - âœ… Got 131 markets from API
2025-11-04 00:58:31,128 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 131/131 markets passed
2025-11-04 00:58:31,128 - market_scanner_v2 - INFO - âœ… Found 131 qualifying markets (from 131 total)
2025-11-04 00:58:31,130 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 00:58:36,106 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 00:58:36,936 - market_scanner_v2 - INFO - âœ… Fetched 131 markets from API
2025-11-04 00:58:36,943 - market_scanner_v2 - INFO - âœ… Got 131 markets from API
2025-11-04 00:58:36,945 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 131/131 markets passed
2025-11-04 00:58:36,945 - market_scanner_v2 - INFO - âœ… Found 131 qualifying markets (from 131 total)
2025-11-04 00:58:36,952 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 00:58:42,036 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 00:58:42,793 - market_scanner_v2 - INFO - âœ… Fetched 131 markets from API
2025-11-04 00:58:42,796 - market_scanner_v2 - INFO - âœ… Got 131 markets from API
2025-11-04 00:58:42,797 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 131/131 markets passed
2025-11-04 00:58:42,797 - market_scanner_v2 - INFO - âœ… Found 131 qualifying markets (from 131 total)
2025-11-04 00:58:42,799 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 00:58:47,510 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 00:58:48,291 - market_scanner_v2 - INFO - âœ… Fetched 131 markets from API
2025-11-04 00:58:48,294 - market_scanner_v2 - INFO - âœ… Got 131 markets from API
2025-11-04 00:58:48,295 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 131/131 markets passed
2025-11-04 00:58:48,295 - market_scanner_v2 - INFO - âœ… Found 131 qualifying markets (from 131 total)
2025-11-04 00:58:48,297 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 00:58:54,140 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 00:58:54,929 - market_scanner_v2 - INFO - âœ… Fetched 131 markets from API
2025-11-04 00:58:54,931 - market_scanner_v2 - INFO - âœ… Got 131 markets from API
2025-11-04 00:58:54,932 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 131/131 markets passed
2025-11-04 00:58:54,933 - market_scanner_v2 - INFO - âœ… Found 131 qualifying markets (from 131 total)
2025-11-04 00:58:54,935 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 00:58:59,487 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 00:59:00,269 - market_scanner_v2 - INFO - âœ… Fetched 131 markets from API
2025-11-04 00:59:00,271 - market_scanner_v2 - INFO - âœ… Got 131 markets from API
2025-11-04 00:59:00,272 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 131/131 markets passed
2025-11-04 00:59:00,272 - market_scanner_v2 - INFO - âœ… Found 131 qualifying markets (from 131 total)
2025-11-04 00:59:00,274 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 00:59:04,605 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 00:59:05,363 - market_scanner_v2 - INFO - âœ… Fetched 131 markets from API
2025-11-04 00:59:05,365 - market_scanner_v2 - INFO - âœ… Got 131 markets from API
2025-11-04 00:59:05,366 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 131/131 markets passed
2025-11-04 00:59:05,366 - market_scanner_v2 - INFO - âœ… Found 131 qualifying markets (from 131 total)
2025-11-04 00:59:05,368 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 00:59:10,320 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 00:59:11,083 - market_scanner_v2 - INFO - âœ… Fetched 131 markets from API
2025-11-04 00:59:11,087 - market_scanner_v2 - INFO - âœ… Got 131 markets from API
2025-11-04 00:59:11,088 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 131/131 markets passed
2025-11-04 00:59:11,088 - market_scanner_v2 - INFO - âœ… Found 131 qualifying markets (from 131 total)
2025-11-04 00:59:11,090 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 00:59:16,223 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 00:59:16,977 - market_scanner_v2 - INFO - âœ… Fetched 131 markets from API
2025-11-04 00:59:16,981 - market_scanner_v2 - INFO - âœ… Got 131 markets from API
2025-11-04 00:59:16,982 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 131/131 markets passed
2025-11-04 00:59:16,982 - market_scanner_v2 - INFO - âœ… Found 131 qualifying markets (from 131 total)
2025-11-04 00:59:16,984 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 00:59:22,187 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 00:59:22,945 - market_scanner_v2 - INFO - âœ… Fetched 131 markets from API
2025-11-04 00:59:22,947 - market_scanner_v2 - INFO - âœ… Got 131 markets from API
2025-11-04 00:59:22,948 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 131/131 markets passed
2025-11-04 00:59:22,948 - market_scanner_v2 - INFO - âœ… Found 131 qualifying markets (from 131 total)
2025-11-04 00:59:22,950 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 00:59:28,151 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 00:59:28,957 - market_scanner_v2 - INFO - âœ… Fetched 131 markets from API
2025-11-04 00:59:28,960 - market_scanner_v2 - INFO - âœ… Got 131 markets from API
2025-11-04 00:59:28,961 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 131/131 markets passed
2025-11-04 00:59:28,961 - market_scanner_v2 - INFO - âœ… Found 131 qualifying markets (from 131 total)
2025-11-04 00:59:28,963 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 00:59:33,535 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 00:59:34,347 - market_scanner_v2 - INFO - âœ… Fetched 131 markets from API
2025-11-04 00:59:34,350 - market_scanner_v2 - INFO - âœ… Got 131 markets from API
2025-11-04 00:59:34,351 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 131/131 markets passed
2025-11-04 00:59:34,351 - market_scanner_v2 - INFO - âœ… Found 131 qualifying markets (from 131 total)
2025-11-04 00:59:34,353 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 00:59:40,145 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 00:59:40,938 - market_scanner_v2 - INFO - âœ… Fetched 131 markets from API
2025-11-04 00:59:40,941 - market_scanner_v2 - INFO - âœ… Got 131 markets from API
2025-11-04 00:59:40,942 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 131/131 markets passed
2025-11-04 00:59:40,943 - market_scanner_v2 - INFO - âœ… Found 131 qualifying markets (from 131 total)
2025-11-04 00:59:40,945 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 00:59:45,830 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 00:59:46,607 - market_scanner_v2 - INFO - âœ… Fetched 131 markets from API
2025-11-04 00:59:46,609 - market_scanner_v2 - INFO - âœ… Got 131 markets from API
2025-11-04 00:59:46,610 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 131/131 markets passed
2025-11-04 00:59:46,611 - market_scanner_v2 - INFO - âœ… Found 131 qualifying markets (from 131 total)
2025-11-04 00:59:46,612 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 00:59:51,705 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 00:59:52,504 - market_scanner_v2 - INFO - âœ… Fetched 131 markets from API
2025-11-04 00:59:52,507 - market_scanner_v2 - INFO - âœ… Got 131 markets from API
2025-11-04 00:59:52,508 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 131/131 markets passed
2025-11-04 00:59:52,509 - market_scanner_v2 - INFO - âœ… Found 131 qualifying markets (from 131 total)
2025-11-04 00:59:52,511 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 00:59:56,737 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 00:59:57,522 - market_scanner_v2 - INFO - âœ… Fetched 131 markets from API
2025-11-04 00:59:57,524 - market_scanner_v2 - INFO - âœ… Got 131 markets from API
2025-11-04 00:59:57,525 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 131/131 markets passed
2025-11-04 00:59:57,526 - market_scanner_v2 - INFO - âœ… Found 131 qualifying markets (from 131 total)
2025-11-04 00:59:57,527 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:00:01,843 - ml_predictor - INFO - Alert sent: âœ… <b>Hourly Report</b>
â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”
â° Time: 2025-11-04 01:00:01

ðŸ“Š <b>Performance (Last 60 min)</b>
   â€¢ Scans: 29
   â€¢ Markets found: 3799 (131.0/scan)
   â€¢ Orders placed: 0
   â€¢ Orders filled: 0 (0.0%)
   â€¢ Profit: $0.00
   â€¢ Errors: 0 (0.0%)

ðŸ’» <b>System Health</b>
   â€¢ CPU: 62.7%
   â€¢ RAM: 82.0%
   â€¢ Bot RAM: 461 MB
        

âš ï¸ <b>Issues:</b>
   â€¢ âš ï¸ RAM cao: 82.0%

â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”
2025-11-04 01:00:01,848 - monitoring_system - INFO - âœ… Hourly report sent
2025-11-04 01:00:02,278 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:00:02,724 - market_scanner_v2 - INFO - âœ… Fetched 131 markets from API
2025-11-04 01:00:02,732 - market_scanner_v2 - INFO - âœ… Got 131 markets from API
2025-11-04 01:00:02,740 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 131/131 markets passed
2025-11-04 01:00:02,741 - market_scanner_v2 - INFO - âœ… Found 131 qualifying markets (from 131 total)
2025-11-04 01:00:02,743 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:00:08,378 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:00:09,243 - market_scanner_v2 - INFO - âœ… Fetched 131 markets from API
2025-11-04 01:00:09,252 - market_scanner_v2 - INFO - âœ… Got 131 markets from API
2025-11-04 01:00:09,255 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 131/131 markets passed
2025-11-04 01:00:09,256 - market_scanner_v2 - INFO - âœ… Found 131 qualifying markets (from 131 total)
2025-11-04 01:00:09,265 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:00:15,140 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:00:15,962 - market_scanner_v2 - INFO - âœ… Fetched 131 markets from API
2025-11-04 01:00:15,965 - market_scanner_v2 - INFO - âœ… Got 131 markets from API
2025-11-04 01:00:15,978 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 131/131 markets passed
2025-11-04 01:00:15,978 - market_scanner_v2 - INFO - âœ… Found 131 qualifying markets (from 131 total)
2025-11-04 01:00:15,980 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:00:21,725 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:00:22,452 - market_scanner_v2 - INFO - âœ… Fetched 131 markets from API
2025-11-04 01:00:22,456 - market_scanner_v2 - INFO - âœ… Got 131 markets from API
2025-11-04 01:00:22,457 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 131/131 markets passed
2025-11-04 01:00:22,457 - market_scanner_v2 - INFO - âœ… Found 131 qualifying markets (from 131 total)
2025-11-04 01:00:22,460 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:00:27,121 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:00:27,905 - market_scanner_v2 - INFO - âœ… Fetched 131 markets from API
2025-11-04 01:00:27,908 - market_scanner_v2 - INFO - âœ… Got 131 markets from API
2025-11-04 01:00:27,909 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 131/131 markets passed
2025-11-04 01:00:27,909 - market_scanner_v2 - INFO - âœ… Found 131 qualifying markets (from 131 total)
2025-11-04 01:00:27,912 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:00:32,309 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:00:33,090 - market_scanner_v2 - INFO - âœ… Fetched 131 markets from API
2025-11-04 01:00:33,092 - market_scanner_v2 - INFO - âœ… Got 131 markets from API
2025-11-04 01:00:33,093 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 131/131 markets passed
2025-11-04 01:00:33,093 - market_scanner_v2 - INFO - âœ… Found 131 qualifying markets (from 131 total)
2025-11-04 01:00:33,096 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:00:37,688 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:00:38,461 - market_scanner_v2 - INFO - âœ… Fetched 131 markets from API
2025-11-04 01:00:38,464 - market_scanner_v2 - INFO - âœ… Got 131 markets from API
2025-11-04 01:00:38,465 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 131/131 markets passed
2025-11-04 01:00:38,465 - market_scanner_v2 - INFO - âœ… Found 131 qualifying markets (from 131 total)
2025-11-04 01:00:38,467 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:00:43,656 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:00:44,421 - market_scanner_v2 - INFO - âœ… Fetched 131 markets from API
2025-11-04 01:00:44,424 - market_scanner_v2 - INFO - âœ… Got 131 markets from API
2025-11-04 01:00:44,425 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 131/131 markets passed
2025-11-04 01:00:44,426 - market_scanner_v2 - INFO - âœ… Found 131 qualifying markets (from 131 total)
2025-11-04 01:00:44,428 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:00:49,941 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:00:51,547 - market_scanner_v2 - INFO - âœ… Fetched 131 markets from API
2025-11-04 01:00:51,549 - market_scanner_v2 - INFO - âœ… Got 131 markets from API
2025-11-04 01:00:51,550 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 131/131 markets passed
2025-11-04 01:00:51,551 - market_scanner_v2 - INFO - âœ… Found 131 qualifying markets (from 131 total)
2025-11-04 01:00:51,553 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:00:56,804 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:00:57,601 - market_scanner_v2 - INFO - âœ… Fetched 131 markets from API
2025-11-04 01:00:57,604 - market_scanner_v2 - INFO - âœ… Got 131 markets from API
2025-11-04 01:00:57,605 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 131/131 markets passed
2025-11-04 01:00:57,605 - market_scanner_v2 - INFO - âœ… Found 131 qualifying markets (from 131 total)
2025-11-04 01:00:57,607 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:01:03,248 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:01:04,045 - market_scanner_v2 - INFO - âœ… Fetched 135 markets from API
2025-11-04 01:01:04,050 - market_scanner_v2 - INFO - âœ… Got 135 markets from API
2025-11-04 01:01:04,051 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 135/135 markets passed
2025-11-04 01:01:04,052 - market_scanner_v2 - INFO - âœ… Found 135 qualifying markets (from 135 total)
2025-11-04 01:01:04,054 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:01:08,677 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:01:09,456 - market_scanner_v2 - INFO - âœ… Fetched 135 markets from API
2025-11-04 01:01:09,460 - market_scanner_v2 - INFO - âœ… Got 135 markets from API
2025-11-04 01:01:09,462 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 135/135 markets passed
2025-11-04 01:01:09,462 - market_scanner_v2 - INFO - âœ… Found 135 qualifying markets (from 135 total)
2025-11-04 01:01:09,464 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:01:13,854 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:01:14,471 - market_scanner_v2 - INFO - âœ… Fetched 135 markets from API
2025-11-04 01:01:14,474 - market_scanner_v2 - INFO - âœ… Got 135 markets from API
2025-11-04 01:01:14,475 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 135/135 markets passed
2025-11-04 01:01:14,476 - market_scanner_v2 - INFO - âœ… Found 135 qualifying markets (from 135 total)
2025-11-04 01:01:14,478 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:01:18,624 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:01:19,251 - market_scanner_v2 - INFO - âœ… Fetched 135 markets from API
2025-11-04 01:01:19,253 - market_scanner_v2 - INFO - âœ… Got 135 markets from API
2025-11-04 01:01:19,254 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 135/135 markets passed
2025-11-04 01:01:19,254 - market_scanner_v2 - INFO - âœ… Found 135 qualifying markets (from 135 total)
2025-11-04 01:01:19,256 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:01:24,236 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:01:24,860 - market_scanner_v2 - INFO - âœ… Fetched 135 markets from API
2025-11-04 01:01:24,864 - market_scanner_v2 - INFO - âœ… Got 135 markets from API
2025-11-04 01:01:24,865 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 135/135 markets passed
2025-11-04 01:01:24,866 - market_scanner_v2 - INFO - âœ… Found 135 qualifying markets (from 135 total)
2025-11-04 01:01:24,868 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:01:29,611 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:01:30,411 - market_scanner_v2 - INFO - âœ… Fetched 135 markets from API
2025-11-04 01:01:30,414 - market_scanner_v2 - INFO - âœ… Got 135 markets from API
2025-11-04 01:01:30,416 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 135/135 markets passed
2025-11-04 01:01:30,416 - market_scanner_v2 - INFO - âœ… Found 135 qualifying markets (from 135 total)
2025-11-04 01:01:30,420 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:01:34,462 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:01:35,056 - market_scanner_v2 - INFO - âœ… Fetched 135 markets from API
2025-11-04 01:01:35,059 - market_scanner_v2 - INFO - âœ… Got 135 markets from API
2025-11-04 01:01:35,061 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 135/135 markets passed
2025-11-04 01:01:35,061 - market_scanner_v2 - INFO - âœ… Found 135 qualifying markets (from 135 total)
2025-11-04 01:01:35,063 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:01:40,962 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:01:41,725 - market_scanner_v2 - INFO - âœ… Fetched 135 markets from API
2025-11-04 01:01:41,728 - market_scanner_v2 - INFO - âœ… Got 135 markets from API
2025-11-04 01:01:41,729 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 135/135 markets passed
2025-11-04 01:01:41,730 - market_scanner_v2 - INFO - âœ… Found 135 qualifying markets (from 135 total)
2025-11-04 01:01:41,732 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:01:46,921 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:01:47,518 - market_scanner_v2 - INFO - âœ… Fetched 135 markets from API
2025-11-04 01:01:47,521 - market_scanner_v2 - INFO - âœ… Got 135 markets from API
2025-11-04 01:01:47,523 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 135/135 markets passed
2025-11-04 01:01:47,523 - market_scanner_v2 - INFO - âœ… Found 135 qualifying markets (from 135 total)
2025-11-04 01:01:47,525 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:01:53,532 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:01:54,126 - market_scanner_v2 - INFO - âœ… Fetched 135 markets from API
2025-11-04 01:01:54,128 - market_scanner_v2 - INFO - âœ… Got 135 markets from API
2025-11-04 01:01:54,129 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 135/135 markets passed
2025-11-04 01:01:54,130 - market_scanner_v2 - INFO - âœ… Found 135 qualifying markets (from 135 total)
2025-11-04 01:01:54,131 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:02:00,010 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:02:00,632 - market_scanner_v2 - INFO - âœ… Fetched 134 markets from API
2025-11-04 01:02:00,635 - market_scanner_v2 - INFO - âœ… Got 134 markets from API
2025-11-04 01:02:00,636 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 134/134 markets passed
2025-11-04 01:02:00,636 - market_scanner_v2 - INFO - âœ… Found 134 qualifying markets (from 134 total)
2025-11-04 01:02:00,639 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:02:06,316 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:02:07,083 - market_scanner_v2 - INFO - âœ… Fetched 129 markets from API
2025-11-04 01:02:07,085 - market_scanner_v2 - INFO - âœ… Got 129 markets from API
2025-11-04 01:02:07,087 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 129/129 markets passed
2025-11-04 01:02:07,087 - market_scanner_v2 - INFO - âœ… Found 129 qualifying markets (from 129 total)
2025-11-04 01:02:07,089 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:02:12,462 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:02:13,085 - market_scanner_v2 - INFO - âœ… Fetched 129 markets from API
2025-11-04 01:02:13,088 - market_scanner_v2 - INFO - âœ… Got 129 markets from API
2025-11-04 01:02:13,090 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 129/129 markets passed
2025-11-04 01:02:13,090 - market_scanner_v2 - INFO - âœ… Found 129 qualifying markets (from 129 total)
2025-11-04 01:02:13,092 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:02:17,392 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:02:18,264 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:02:18,267 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:02:18,268 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:02:18,268 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:02:18,270 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:02:24,538 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:02:25,352 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:02:25,354 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:02:25,355 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:02:25,355 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:02:25,357 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:02:30,433 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:02:31,044 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:02:31,052 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:02:31,059 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:02:31,060 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:02:31,062 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:02:35,831 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:02:36,424 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:02:36,428 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:02:36,429 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:02:36,429 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:02:36,430 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:02:42,188 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:02:43,163 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:02:43,165 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:02:43,166 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:02:43,166 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:02:43,168 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:02:48,445 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:02:49,060 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:02:49,062 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:02:49,063 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:02:49,063 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:02:49,065 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:02:54,004 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:02:55,563 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:02:55,565 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:02:55,566 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:02:55,566 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:02:55,568 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:03:00,362 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:03:00,938 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:03:00,941 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:03:00,942 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:03:00,943 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:03:00,944 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:03:06,322 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:03:06,919 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:03:06,922 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:03:06,923 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:03:06,923 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:03:06,925 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:03:11,751 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:03:12,343 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:03:12,346 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:03:12,347 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:03:12,347 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:03:12,349 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:03:17,784 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:03:18,344 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:03:18,346 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:03:18,346 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:03:18,347 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:03:18,348 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:03:22,848 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:03:23,413 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:03:23,415 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:03:23,416 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:03:23,416 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:03:23,418 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:03:28,501 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:03:29,277 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:03:29,281 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:03:29,283 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:03:29,283 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:03:29,285 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:03:34,181 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:03:34,789 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:03:34,792 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:03:34,793 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:03:34,793 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:03:34,795 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:03:39,591 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:03:40,358 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:03:40,361 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:03:40,362 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:03:40,363 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:03:40,364 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:03:44,656 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:03:45,437 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:03:45,439 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:03:45,440 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:03:45,440 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:03:45,442 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:03:50,851 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:03:51,444 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:03:51,446 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:03:51,447 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:03:51,447 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:03:51,449 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:03:55,928 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:03:56,518 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:03:56,520 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:03:56,520 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:03:56,521 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:03:56,522 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:04:01,568 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:04:02,173 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:04:02,175 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:04:02,176 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:04:02,177 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:04:02,178 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:04:06,421 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:04:07,001 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:04:07,004 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:04:07,006 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:04:07,006 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:04:07,008 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:04:12,219 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:04:12,839 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:04:12,841 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:04:12,842 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:04:12,842 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:04:12,844 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:04:17,262 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:04:17,890 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:04:17,893 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:04:17,894 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:04:17,895 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:04:17,897 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:04:22,819 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:04:23,457 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:04:23,459 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:04:23,460 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:04:23,460 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:04:23,462 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:04:28,859 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:04:29,474 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:04:29,476 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:04:29,477 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:04:29,478 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:04:29,482 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:04:35,229 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:04:36,046 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:04:36,049 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:04:36,050 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:04:36,050 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:04:36,051 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:04:41,416 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:04:42,182 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:04:42,184 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:04:42,185 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:04:42,185 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:04:42,187 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:04:47,844 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:04:48,485 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:04:48,488 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:04:48,489 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:04:48,489 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:04:48,491 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:04:54,434 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:04:55,039 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:04:55,041 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:04:55,042 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:04:55,042 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:04:55,045 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:05:00,574 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:05:01,213 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:05:01,217 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:05:01,219 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:05:01,219 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:05:01,225 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:05:06,303 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:05:06,744 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:05:06,748 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:05:06,749 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:05:06,750 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:05:06,751 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:05:12,667 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:05:13,269 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:05:13,272 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:05:13,273 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:05:13,273 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:05:13,275 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:05:17,929 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:05:18,779 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:05:18,782 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:05:18,783 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:05:18,783 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:05:18,784 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:05:23,620 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:05:24,215 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:05:24,217 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:05:24,218 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:05:24,219 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:05:24,220 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:05:29,555 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:05:31,337 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:05:31,339 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:05:31,340 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:05:31,341 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:05:31,343 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:05:37,128 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:05:37,753 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:05:37,756 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:05:37,757 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:05:37,757 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:05:37,759 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:05:43,000 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:05:43,563 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:05:43,565 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:05:43,565 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:05:43,565 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:05:43,567 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:05:48,894 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:05:49,482 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:05:49,484 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:05:49,486 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:05:49,486 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:05:49,488 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:05:55,060 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:05:55,647 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:05:55,649 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:05:55,650 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:05:55,650 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:05:55,652 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:05:59,679 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:06:00,518 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:06:00,522 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:06:00,523 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:06:00,523 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:06:00,525 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:06:04,710 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:06:05,313 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:06:05,315 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:06:05,316 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:06:05,316 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:06:05,318 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:06:10,738 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:06:11,325 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:06:11,327 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:06:11,328 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:06:11,328 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:06:11,331 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:06:16,054 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:06:16,648 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:06:16,651 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:06:16,652 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:06:16,653 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:06:16,655 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:06:21,461 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:06:22,090 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:06:22,093 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:06:22,095 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:06:22,095 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:06:22,097 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:06:26,727 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:06:27,314 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:06:27,316 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:06:27,317 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:06:27,317 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:06:27,319 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:06:32,566 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:06:33,152 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:06:33,155 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:06:33,156 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:06:33,157 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:06:33,159 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:06:37,862 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:06:38,651 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:06:38,654 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:06:38,655 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:06:38,656 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:06:38,658 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:06:43,634 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:06:44,227 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:06:44,230 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:06:44,232 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:06:44,232 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:06:44,234 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:06:49,763 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:06:50,537 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:06:50,540 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:06:50,541 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:06:50,542 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:06:50,544 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:06:55,506 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:06:56,144 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:06:56,146 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:06:56,147 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:06:56,147 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:06:56,149 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:07:01,662 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:07:02,253 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:07:02,257 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:07:02,258 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:07:02,258 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:07:02,260 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:07:08,176 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:07:08,766 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:07:08,769 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:07:08,770 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:07:08,771 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:07:08,772 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:07:14,768 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:07:15,367 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:07:15,370 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:07:15,370 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:07:15,371 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:07:15,373 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:07:21,326 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:07:21,949 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:07:21,953 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:07:21,954 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:07:21,954 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:07:21,956 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:07:27,038 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:07:27,631 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:07:27,633 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:07:27,635 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:07:27,635 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:07:27,637 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:07:32,008 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:07:32,618 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:07:32,622 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:07:32,623 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:07:32,623 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:07:32,625 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:07:36,734 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:07:37,341 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:07:37,344 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:07:37,346 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:07:37,346 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:07:37,348 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:07:42,532 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:07:43,088 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:07:43,092 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:07:43,093 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:07:43,093 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:07:43,095 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:07:47,844 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:07:48,581 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:07:48,583 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:07:48,584 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:07:48,585 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:07:48,586 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:07:54,314 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:07:55,133 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:07:55,137 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:07:55,138 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:07:55,138 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:07:55,140 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:08:00,984 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:08:01,544 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:08:01,546 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:08:01,547 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:08:01,547 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:08:01,549 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:08:06,558 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:08:07,345 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:08:07,348 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:08:07,349 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:08:07,349 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:08:07,351 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:08:11,896 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:08:12,518 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:08:12,521 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:08:12,522 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:08:12,523 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:08:12,525 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:08:17,983 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:08:18,597 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:08:18,599 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:08:18,600 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:08:18,601 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:08:18,603 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:08:23,496 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:08:24,134 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:08:24,135 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:08:24,136 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:08:24,136 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:08:24,138 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:08:29,830 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:08:30,575 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:08:30,577 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:08:30,578 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:08:30,578 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:08:30,580 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:08:35,549 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:08:36,605 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:08:36,608 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:08:36,609 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:08:36,609 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:08:36,611 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:08:41,518 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:08:42,124 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:08:42,126 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:08:42,127 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:08:42,127 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:08:42,129 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:08:47,505 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:08:48,136 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:08:48,138 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:08:48,139 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:08:48,139 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:08:48,141 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:08:52,890 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:08:53,518 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:08:53,520 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:08:53,522 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:08:53,522 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:08:53,524 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:08:59,270 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:08:59,883 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:08:59,886 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:08:59,888 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:08:59,888 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:08:59,890 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:09:05,204 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:09:05,997 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:09:06,000 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:09:06,001 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:09:06,002 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:09:06,004 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:09:10,837 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:09:11,580 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:09:11,583 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:09:11,584 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:09:11,584 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:09:11,586 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:09:16,384 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:09:16,940 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:09:16,943 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:09:16,944 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:09:16,944 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:09:16,947 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:09:21,177 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:09:22,020 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:09:22,024 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:09:22,025 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:09:22,025 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:09:22,028 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:09:27,060 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:09:27,679 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:09:27,682 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:09:27,684 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:09:27,684 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:09:27,686 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:09:33,558 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:09:34,146 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:09:34,150 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:09:34,151 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:09:34,152 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:09:34,154 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:09:39,033 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:09:39,603 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:09:39,608 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:09:39,609 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:09:39,609 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:09:39,611 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:09:43,884 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:09:44,472 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:09:44,475 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:09:44,476 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:09:44,476 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:09:44,478 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:09:48,743 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:09:49,464 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:09:49,466 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:09:49,467 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:09:49,468 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:09:49,469 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:09:53,618 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:09:54,246 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:09:54,250 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:09:54,251 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:09:54,251 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:09:54,253 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:09:58,899 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:09:59,514 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:09:59,516 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:09:59,517 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:09:59,517 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:09:59,519 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:10:05,030 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:10:05,603 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:10:05,607 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:10:05,608 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:10:05,608 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:10:05,610 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:10:09,716 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:10:10,345 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:10:10,347 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:10:10,348 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:10:10,348 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:10:10,350 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:10:15,619 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:10:16,208 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:10:16,211 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:10:16,212 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:10:16,213 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:10:16,215 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:10:22,036 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:10:22,633 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:10:22,636 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:10:22,637 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:10:22,637 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:10:22,639 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:10:27,857 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:10:28,653 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:10:28,656 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:10:28,658 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:10:28,658 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:10:28,660 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:10:33,322 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:10:33,944 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:10:33,948 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:10:33,949 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:10:33,949 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:10:33,951 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:10:38,050 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:10:38,661 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:10:38,664 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:10:38,665 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:10:38,665 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:10:38,667 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:10:43,143 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:10:43,770 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:10:43,773 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:10:43,774 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:10:43,775 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:10:43,776 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:10:49,269 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:10:49,887 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:10:49,891 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:10:49,892 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:10:49,893 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:10:49,895 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:10:54,672 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:10:55,285 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:10:55,287 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:10:55,288 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:10:55,288 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:10:55,290 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:10:59,934 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:11:00,568 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:11:00,571 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:11:00,572 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:11:00,573 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:11:00,575 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:11:05,431 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:11:06,021 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:11:06,025 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:11:06,026 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:11:06,026 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:11:06,028 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:11:11,601 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:11:12,185 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:11:12,187 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:11:12,189 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:11:12,189 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:11:12,191 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:11:16,947 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:11:17,545 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:11:17,551 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:11:17,552 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:11:17,552 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:11:17,554 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:11:21,777 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:11:22,397 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:11:22,399 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:11:22,400 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:11:22,400 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:11:22,402 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:11:27,171 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:11:27,791 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:11:27,794 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:11:27,795 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:11:27,795 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:11:27,797 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:11:31,811 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:11:32,422 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:11:32,426 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:11:32,427 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:11:32,427 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:11:32,428 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:11:37,682 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:11:38,263 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:11:38,265 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:11:38,266 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:11:38,266 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:11:38,268 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:11:43,316 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:11:43,919 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:11:43,922 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:11:43,923 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:11:43,923 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:11:43,924 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:11:48,899 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:11:49,516 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:11:49,518 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:11:49,519 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:11:49,520 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:11:49,521 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:11:55,415 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:11:56,049 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:11:56,052 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:11:56,053 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:11:56,053 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:11:56,055 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:12:01,859 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:12:02,512 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:12:02,520 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:12:02,522 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:12:02,523 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:12:02,527 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:12:07,013 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:12:07,619 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:12:07,622 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:12:07,623 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:12:07,623 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:12:07,625 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:12:12,595 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:12:13,638 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:12:13,640 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:12:13,641 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:12:13,642 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:12:13,643 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:12:19,342 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:12:19,927 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:12:19,929 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:12:19,930 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:12:19,930 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:12:19,932 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:12:24,774 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:12:25,389 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:12:25,391 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:12:25,392 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:12:25,392 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:12:25,394 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:12:29,895 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:12:30,492 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:12:30,494 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:12:30,496 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:12:30,496 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:12:30,498 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:12:36,428 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:12:41,642 - market_scanner_v2 - WARNING - âš ï¸  API returned status 500
2025-11-04 01:12:41,643 - market_scanner_v2 - WARNING - âš ï¸  No markets from API
2025-11-04 01:12:41,643 - market_scanner_v2 - WARNING - âš ï¸  Trying Playwright scraping...
2025-11-04 01:12:43,435 - market_scanner_v2 - INFO - âœ… Playwright browser initialized
2025-11-04 01:12:59,909 - market_scanner_v2 - WARNING - âš ï¸  Timeout waiting for market cards
2025-11-04 01:13:07,052 - market_scanner_v2 - INFO - âœ… Found 0 qualifying markets (from 0 total)
2025-11-04 01:13:07,052 - market_selector - INFO - Selected 0 markets from 0 candidates
2025-11-04 01:13:11,427 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:13:13,109 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:13:13,111 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:13:13,112 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:13:13,112 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:13:13,114 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:13:17,118 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:13:17,887 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:13:17,890 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:13:17,891 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:13:17,891 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:13:17,893 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:13:22,657 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:13:22,862 - market_scanner_v2 - WARNING - âš ï¸  API returned status 500
2025-11-04 01:13:22,863 - market_scanner_v2 - WARNING - âš ï¸  No markets from API
2025-11-04 01:13:22,863 - market_scanner_v2 - WARNING - âš ï¸  Trying Playwright scraping...
2025-11-04 01:13:37,711 - market_scanner_v2 - WARNING - âš ï¸  Timeout waiting for market cards
2025-11-04 01:13:40,900 - market_scanner_v2 - INFO - âœ… Found 0 qualifying markets (from 0 total)
2025-11-04 01:13:40,900 - market_selector - INFO - Selected 0 markets from 0 candidates
2025-11-04 01:13:46,623 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:13:47,223 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:13:47,225 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:13:47,226 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:13:47,227 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:13:47,228 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:13:52,792 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:13:53,613 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:13:53,617 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:13:53,618 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:13:53,618 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:13:53,620 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:13:58,002 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:13:58,584 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:13:58,590 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:13:58,591 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:13:58,591 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:13:58,593 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:14:04,496 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:14:05,149 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:14:05,153 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:14:05,160 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:14:05,160 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:14:05,162 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:14:10,205 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:14:10,821 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:14:10,831 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:14:10,833 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:14:10,833 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:14:10,839 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:14:16,154 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:14:17,676 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:14:17,684 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:14:17,685 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:14:17,687 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:14:17,689 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:14:23,634 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:14:24,277 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:14:24,284 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:14:24,290 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:14:24,290 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:14:24,292 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:14:28,489 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:14:29,318 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:14:29,326 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:14:29,327 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:14:29,327 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:14:29,334 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:14:33,871 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:14:34,500 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:14:34,507 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:14:34,508 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:14:34,508 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:14:34,515 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:14:38,758 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:14:39,752 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:14:39,759 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:14:39,760 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:14:39,761 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:14:39,767 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:14:44,686 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:14:45,304 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:14:45,313 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:14:45,318 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:14:45,318 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:14:45,320 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:14:50,953 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:14:51,575 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:14:51,583 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:14:51,584 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:14:51,584 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:14:51,590 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:14:55,679 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:14:56,327 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:14:56,337 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:14:56,338 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:14:56,338 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:14:56,340 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:15:00,530 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:15:01,384 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:15:01,408 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:15:01,409 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:15:01,409 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:15:01,433 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:15:06,077 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:15:06,727 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:15:06,732 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:15:06,733 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:15:06,733 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:15:06,751 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:15:12,658 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:15:13,343 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:15:13,350 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:15:13,352 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:15:13,352 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:15:13,358 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:15:18,513 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:15:19,698 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:15:19,706 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:15:19,707 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:15:19,707 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:15:19,709 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:15:24,596 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:15:25,291 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:15:25,299 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:15:25,300 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:15:25,300 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:15:25,306 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:15:29,857 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:15:30,739 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:15:30,749 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:15:30,754 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:15:30,755 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:15:30,762 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:15:35,950 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:15:36,635 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:15:36,642 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:15:36,643 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:15:36,643 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:15:36,645 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:15:42,016 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:15:42,696 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:15:42,703 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:15:42,705 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:15:42,705 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:15:42,711 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:15:47,733 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:15:48,360 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:15:48,372 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:15:48,378 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:15:48,378 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:15:48,380 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:15:53,022 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:15:53,806 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:15:53,808 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:15:53,809 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:15:53,809 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:15:53,815 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:15:59,598 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:16:00,241 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:16:00,257 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:16:00,270 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:16:00,271 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:16:00,273 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:16:05,886 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:16:06,926 - market_scanner_v2 - INFO - âœ… Fetched 129 markets from API
2025-11-04 01:16:06,935 - market_scanner_v2 - INFO - âœ… Got 129 markets from API
2025-11-04 01:16:06,936 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 129/129 markets passed
2025-11-04 01:16:06,936 - market_scanner_v2 - INFO - âœ… Found 129 qualifying markets (from 129 total)
2025-11-04 01:16:06,942 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:16:11,644 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:16:12,294 - market_scanner_v2 - INFO - âœ… Fetched 129 markets from API
2025-11-04 01:16:12,297 - market_scanner_v2 - INFO - âœ… Got 129 markets from API
2025-11-04 01:16:12,302 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 129/129 markets passed
2025-11-04 01:16:12,303 - market_scanner_v2 - INFO - âœ… Found 129 qualifying markets (from 129 total)
2025-11-04 01:16:12,305 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:16:17,122 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:16:17,766 - market_scanner_v2 - INFO - âœ… Fetched 129 markets from API
2025-11-04 01:16:17,774 - market_scanner_v2 - INFO - âœ… Got 129 markets from API
2025-11-04 01:16:17,775 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 129/129 markets passed
2025-11-04 01:16:17,775 - market_scanner_v2 - INFO - âœ… Found 129 qualifying markets (from 129 total)
2025-11-04 01:16:17,782 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:16:22,979 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:16:23,658 - market_scanner_v2 - INFO - âœ… Fetched 129 markets from API
2025-11-04 01:16:23,666 - market_scanner_v2 - INFO - âœ… Got 129 markets from API
2025-11-04 01:16:23,667 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 129/129 markets passed
2025-11-04 01:16:23,667 - market_scanner_v2 - INFO - âœ… Found 129 qualifying markets (from 129 total)
2025-11-04 01:16:23,674 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:16:28,440 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:16:29,087 - market_scanner_v2 - INFO - âœ… Fetched 129 markets from API
2025-11-04 01:16:29,095 - market_scanner_v2 - INFO - âœ… Got 129 markets from API
2025-11-04 01:16:29,096 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 129/129 markets passed
2025-11-04 01:16:29,097 - market_scanner_v2 - INFO - âœ… Found 129 qualifying markets (from 129 total)
2025-11-04 01:16:29,103 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:16:33,149 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:16:33,757 - market_scanner_v2 - INFO - âœ… Fetched 129 markets from API
2025-11-04 01:16:33,764 - market_scanner_v2 - INFO - âœ… Got 129 markets from API
2025-11-04 01:16:33,765 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 129/129 markets passed
2025-11-04 01:16:33,765 - market_scanner_v2 - INFO - âœ… Found 129 qualifying markets (from 129 total)
2025-11-04 01:16:33,771 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:16:39,582 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:16:40,226 - market_scanner_v2 - INFO - âœ… Fetched 129 markets from API
2025-11-04 01:16:40,229 - market_scanner_v2 - INFO - âœ… Got 129 markets from API
2025-11-04 01:16:40,235 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 129/129 markets passed
2025-11-04 01:16:40,235 - market_scanner_v2 - INFO - âœ… Found 129 qualifying markets (from 129 total)
2025-11-04 01:16:40,237 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:16:44,444 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:16:45,268 - market_scanner_v2 - INFO - âœ… Fetched 129 markets from API
2025-11-04 01:16:45,275 - market_scanner_v2 - INFO - âœ… Got 129 markets from API
2025-11-04 01:16:45,276 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 129/129 markets passed
2025-11-04 01:16:45,277 - market_scanner_v2 - INFO - âœ… Found 129 qualifying markets (from 129 total)
2025-11-04 01:16:45,283 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:16:49,898 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:16:50,501 - market_scanner_v2 - INFO - âœ… Fetched 129 markets from API
2025-11-04 01:16:50,508 - market_scanner_v2 - INFO - âœ… Got 129 markets from API
2025-11-04 01:16:50,509 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 129/129 markets passed
2025-11-04 01:16:50,514 - market_scanner_v2 - INFO - âœ… Found 129 qualifying markets (from 129 total)
2025-11-04 01:16:50,516 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:16:56,306 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:16:57,140 - market_scanner_v2 - INFO - âœ… Fetched 129 markets from API
2025-11-04 01:16:57,147 - market_scanner_v2 - INFO - âœ… Got 129 markets from API
2025-11-04 01:16:57,148 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 129/129 markets passed
2025-11-04 01:16:57,148 - market_scanner_v2 - INFO - âœ… Found 129 qualifying markets (from 129 total)
2025-11-04 01:16:57,154 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:17:02,508 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:17:03,318 - market_scanner_v2 - INFO - âœ… Fetched 129 markets from API
2025-11-04 01:17:03,323 - market_scanner_v2 - INFO - âœ… Got 129 markets from API
2025-11-04 01:17:03,324 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 129/129 markets passed
2025-11-04 01:17:03,325 - market_scanner_v2 - INFO - âœ… Found 129 qualifying markets (from 129 total)
2025-11-04 01:17:03,331 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:17:07,338 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:17:08,013 - market_scanner_v2 - INFO - âœ… Fetched 129 markets from API
2025-11-04 01:17:08,021 - market_scanner_v2 - INFO - âœ… Got 129 markets from API
2025-11-04 01:17:08,022 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 129/129 markets passed
2025-11-04 01:17:08,022 - market_scanner_v2 - INFO - âœ… Found 129 qualifying markets (from 129 total)
2025-11-04 01:17:08,024 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:17:12,396 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:17:13,011 - market_scanner_v2 - INFO - âœ… Fetched 129 markets from API
2025-11-04 01:17:13,019 - market_scanner_v2 - INFO - âœ… Got 129 markets from API
2025-11-04 01:17:13,020 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 129/129 markets passed
2025-11-04 01:17:13,020 - market_scanner_v2 - INFO - âœ… Found 129 qualifying markets (from 129 total)
2025-11-04 01:17:13,027 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:17:17,313 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:17:17,924 - market_scanner_v2 - INFO - âœ… Fetched 125 markets from API
2025-11-04 01:17:17,931 - market_scanner_v2 - INFO - âœ… Got 125 markets from API
2025-11-04 01:17:17,932 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 125/125 markets passed
2025-11-04 01:17:17,932 - market_scanner_v2 - INFO - âœ… Found 125 qualifying markets (from 125 total)
2025-11-04 01:17:17,939 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:17:23,650 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:17:24,299 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:17:24,307 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:17:24,308 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:17:24,308 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:17:24,314 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:17:28,517 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:17:29,155 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:17:29,163 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:17:29,164 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:17:29,164 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:17:29,171 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:17:34,166 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:17:34,937 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:17:34,946 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:17:34,947 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:17:34,947 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:17:34,949 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:17:39,300 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:17:39,951 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:17:39,960 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:17:39,961 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:17:39,962 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:17:39,963 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:17:44,218 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:17:44,873 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:17:44,881 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:17:44,886 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:17:44,887 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:17:44,889 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:17:50,746 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:17:51,365 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:17:51,372 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:17:51,378 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:17:51,378 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:17:51,380 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:17:56,693 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:17:57,361 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:17:57,377 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:17:57,391 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:17:57,392 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:17:57,398 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:18:01,655 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:18:02,492 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:18:02,499 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:18:02,500 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:18:02,500 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:18:02,507 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:18:07,162 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:18:07,816 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:18:07,823 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:18:07,824 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:18:07,825 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:18:07,831 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:18:13,626 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:18:14,333 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:18:14,341 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:18:14,346 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:18:14,347 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:18:14,348 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:18:20,336 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:18:20,937 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:18:20,945 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:18:20,950 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:18:20,951 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:18:20,952 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:18:26,078 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:18:26,894 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:18:26,897 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:18:26,902 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:18:26,903 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:18:26,905 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:18:30,957 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:18:31,595 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:18:31,603 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:18:31,604 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:18:31,604 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:18:31,610 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:18:37,251 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:18:37,895 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:18:37,903 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:18:37,904 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:18:37,905 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:18:37,911 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:18:42,776 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:18:43,661 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:18:43,669 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:18:43,674 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:18:43,675 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:18:43,677 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:18:48,543 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:18:49,298 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:18:49,306 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:18:49,307 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:18:49,307 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:18:49,309 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:18:54,667 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:18:55,330 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:18:55,338 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:18:55,339 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:18:55,339 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:18:55,341 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:19:01,317 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:19:01,928 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:19:01,934 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:19:01,935 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:19:01,936 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:19:01,942 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:19:06,218 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:19:07,087 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:19:07,094 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:19:07,096 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:19:07,096 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:19:07,103 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:19:11,768 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:19:12,576 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:19:12,583 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:19:12,584 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:19:12,584 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:19:12,591 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:19:17,038 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:19:17,635 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:19:17,643 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:19:17,644 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:19:17,644 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:19:17,651 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:19:23,435 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:19:24,231 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:19:24,238 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:19:24,239 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:19:24,240 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:19:24,241 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:19:29,541 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:19:30,216 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:19:30,223 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:19:30,224 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:19:30,225 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:19:30,231 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:19:36,092 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:19:36,735 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:19:36,744 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:19:36,745 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:19:36,745 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:19:36,770 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:19:41,787 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:19:42,436 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:19:42,445 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:19:42,451 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:19:42,451 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:19:42,453 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:19:48,229 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:19:48,884 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:19:48,892 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:19:48,893 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:19:48,893 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:19:48,900 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:19:54,639 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:19:55,339 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:19:55,347 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:19:55,348 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:19:55,348 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:19:55,354 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:20:01,041 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:20:01,624 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:20:01,632 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:20:01,641 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:20:01,642 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:20:01,644 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:20:06,155 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:20:06,892 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:20:06,907 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:20:06,908 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:20:06,908 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:20:06,917 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:20:11,331 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:20:11,968 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:20:11,976 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:20:11,977 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:20:11,982 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:20:11,984 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:20:17,448 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:20:20,325 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:20:20,346 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:20:20,348 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:20:20,348 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:20:20,354 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:20:26,319 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:20:26,936 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:20:26,944 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:20:26,945 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:20:26,950 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:20:26,952 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:20:31,165 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:20:31,791 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:20:31,799 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:20:31,800 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:20:31,800 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:20:31,807 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:20:37,186 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:20:37,828 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:20:37,835 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:20:37,836 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:20:37,836 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:20:37,843 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:20:41,982 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:20:42,644 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:20:42,652 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:20:42,653 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:20:42,653 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:20:42,659 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:20:46,732 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:20:47,367 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:20:47,375 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:20:47,376 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:20:47,376 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:20:47,383 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:20:53,047 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:20:53,657 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:20:53,665 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:20:53,670 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:20:53,671 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:20:53,673 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:20:59,111 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:21:00,735 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:21:00,741 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:21:00,743 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:21:00,743 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:21:00,745 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:21:06,190 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:21:07,153 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:21:07,163 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:21:07,164 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:21:07,164 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:21:07,171 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:21:11,460 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:21:12,279 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:21:12,286 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:21:12,287 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:21:12,288 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:21:12,294 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:21:18,271 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:21:18,938 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:21:18,941 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:21:18,947 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:21:18,947 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:21:18,949 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:21:24,416 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:21:25,315 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:21:25,323 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:21:25,324 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:21:25,324 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:21:25,329 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:21:31,682 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:21:32,313 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:21:32,316 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:21:32,322 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:21:32,322 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:21:32,325 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:21:37,912 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:21:38,776 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:21:38,783 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:21:38,784 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:21:38,784 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:21:38,790 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:21:43,658 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:21:44,251 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:21:44,258 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:21:44,259 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:21:44,260 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:21:44,266 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:21:49,600 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:21:50,218 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:21:50,221 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:21:50,226 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:21:50,227 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:21:50,229 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:21:56,037 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:21:56,690 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:21:56,693 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:21:56,698 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:21:56,699 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:21:56,701 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:22:02,686 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:22:03,282 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:22:03,285 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:22:03,290 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:22:03,291 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:22:03,293 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:22:07,355 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:22:07,990 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:22:07,997 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:22:07,999 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:22:07,999 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:22:08,001 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:22:13,283 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:22:13,899 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:22:13,906 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:22:13,907 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:22:13,908 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:22:13,914 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:22:18,951 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:22:19,945 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:22:19,952 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:22:19,958 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:22:19,958 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:22:19,960 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:22:25,842 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:22:26,427 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:22:26,429 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:22:26,434 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:22:26,435 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:22:26,437 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:22:31,841 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:22:32,494 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:22:32,497 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:22:32,502 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:22:32,503 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:22:32,505 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:22:37,584 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:22:38,193 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:22:38,197 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:22:38,202 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:22:38,203 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:22:38,205 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:22:42,646 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:22:43,289 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:22:43,299 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:22:43,300 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:22:43,300 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:22:43,307 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:22:47,440 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:22:48,091 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:22:48,098 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:22:48,099 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:22:48,099 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:22:48,101 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:22:53,766 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:22:54,422 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:22:54,424 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:22:54,430 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:22:54,430 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:22:54,432 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:22:59,925 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:23:00,813 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:23:00,816 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:23:00,817 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:23:00,817 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:23:00,823 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:23:04,967 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:23:05,620 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:23:05,628 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:23:05,633 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:23:05,634 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:23:05,636 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:23:10,306 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:23:10,924 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:23:10,931 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:23:10,932 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:23:10,933 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:23:10,939 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:23:16,881 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:23:17,520 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:23:17,527 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:23:17,528 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:23:17,528 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:23:17,535 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:23:22,363 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:23:22,977 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:23:22,985 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:23:22,990 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:23:22,991 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:23:22,993 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:23:27,170 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:23:27,963 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:23:27,970 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:23:27,972 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:23:27,972 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:23:27,978 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:23:33,289 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:23:33,924 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:23:33,932 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:23:33,933 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:23:33,933 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:23:33,939 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:23:39,008 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:23:39,651 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:23:39,658 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:23:39,660 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:23:39,660 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:23:39,666 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:23:44,951 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:23:45,745 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:23:45,752 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:23:45,758 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:23:45,758 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:23:45,760 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:23:50,516 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:23:51,171 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:23:51,179 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:23:51,181 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:23:51,181 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:23:51,190 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:23:55,386 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:23:56,307 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:23:56,314 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:23:56,315 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:23:56,316 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:23:56,322 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:24:01,797 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:24:02,493 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:24:02,500 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:24:02,506 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:24:02,506 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:24:02,508 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:24:08,437 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:24:09,136 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:24:09,150 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:24:09,151 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:24:09,151 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:24:09,158 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:24:14,634 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:24:15,350 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:24:15,358 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:24:15,359 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:24:15,360 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:24:15,366 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:24:19,793 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:24:20,647 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:24:20,655 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:24:20,657 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:24:20,657 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:24:20,659 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:24:26,645 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:24:32,423 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:24:32,434 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:24:32,435 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:24:32,436 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:24:32,442 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:24:37,705 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:24:38,371 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:24:38,378 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:24:38,379 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:24:38,380 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:24:38,385 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:24:43,864 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:24:44,569 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:24:44,576 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:24:44,577 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:24:44,582 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:24:44,584 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:24:49,375 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:24:50,033 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:24:50,040 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:24:50,046 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:24:50,047 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:24:50,048 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:24:55,446 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:24:56,102 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:24:56,110 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:24:56,111 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:24:56,111 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:24:56,113 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:25:01,458 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:25:02,182 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:25:02,190 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:25:02,191 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:25:02,191 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:25:02,193 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:25:06,890 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:25:07,547 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:25:07,549 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:25:07,554 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:25:07,555 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:25:07,556 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:25:12,567 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:25:13,210 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:25:13,218 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:25:13,219 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:25:13,219 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:25:13,221 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:25:17,315 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:25:17,905 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:25:17,912 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:25:17,918 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:25:17,918 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:25:17,920 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:25:22,534 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:25:23,160 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:25:23,167 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:25:23,168 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:25:23,169 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:25:23,175 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:25:28,753 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:25:29,451 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:25:29,466 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:25:29,467 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:25:29,467 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:25:29,469 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:25:33,930 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:25:34,576 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:25:34,584 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:25:34,585 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:25:34,590 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:25:34,592 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:25:39,773 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:25:40,430 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:25:40,438 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:25:40,439 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:25:40,439 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:25:40,446 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:25:45,498 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:25:46,139 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:25:46,146 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:25:46,147 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:25:46,147 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:25:46,154 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:25:51,691 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:25:52,299 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:25:52,308 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:25:52,309 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:25:52,309 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:25:52,316 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:25:57,407 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:25:58,026 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:25:58,034 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:25:58,035 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:25:58,035 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:25:58,037 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:26:03,707 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:26:04,321 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:26:04,328 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:26:04,334 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:26:04,334 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:26:04,336 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:26:09,182 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:26:10,770 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:26:10,778 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:26:10,779 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:26:10,779 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:26:10,781 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:26:16,187 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:26:16,851 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:26:16,856 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:26:16,862 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:26:16,862 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:26:16,864 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:26:22,203 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:26:22,847 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:26:22,855 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:26:22,856 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:26:22,856 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:26:22,862 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:26:28,783 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:26:29,407 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:26:29,431 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:26:29,432 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:26:29,432 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:26:29,447 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:26:34,868 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:26:35,533 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:26:35,540 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:26:35,547 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:26:35,547 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:26:35,553 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:26:39,643 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:26:40,417 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:26:40,424 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:26:40,425 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:26:40,430 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:26:40,432 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:26:45,404 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:26:46,542 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:26:46,545 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:26:46,550 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:26:46,551 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:26:46,553 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:26:51,265 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:26:51,936 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:26:51,962 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:26:51,963 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:26:51,964 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:26:51,978 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:26:57,713 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:26:58,350 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:26:58,358 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:26:58,359 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:26:58,359 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:26:58,361 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:27:02,392 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:27:03,219 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:27:03,227 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:27:03,228 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:27:03,228 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:27:03,234 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:27:07,365 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:27:08,032 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:27:08,039 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:27:08,040 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:27:08,040 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:27:08,046 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:27:12,726 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:27:13,392 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:27:13,399 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:27:13,400 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:27:13,401 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:27:13,407 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:27:18,742 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:27:19,352 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:27:19,360 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:27:19,361 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:27:19,361 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:27:19,367 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:27:24,897 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:27:25,523 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:27:25,530 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:27:25,531 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:27:25,531 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:27:25,538 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:27:30,737 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:27:31,392 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:27:31,399 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:27:31,400 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:27:31,400 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:27:31,406 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:27:35,659 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:27:36,566 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:27:36,574 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:27:36,575 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:27:36,575 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:27:36,577 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:27:40,953 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:27:41,564 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:27:41,571 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:27:41,572 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:27:41,572 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:27:41,579 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:27:47,007 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:27:47,636 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:27:47,641 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:27:47,646 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:27:47,647 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:27:47,648 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:27:53,422 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:27:54,074 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:27:54,077 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:27:54,082 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:27:54,083 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:27:54,085 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:27:59,705 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:28:00,328 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:28:00,335 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:28:00,336 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:28:00,336 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:28:00,342 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:28:06,207 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:28:06,857 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:28:06,864 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:28:06,870 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:28:06,870 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:28:06,872 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:28:12,211 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:28:12,854 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:28:12,862 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:28:12,863 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:28:12,863 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:28:12,865 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:28:18,179 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:28:18,819 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:28:18,827 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:28:18,828 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:28:18,828 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:28:18,835 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:28:24,803 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:28:25,630 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:28:25,635 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:28:25,636 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:28:25,637 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:28:25,643 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:28:30,954 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:28:31,596 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:28:31,604 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:28:31,605 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:28:31,624 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:28:31,631 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:28:36,982 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:28:37,611 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:28:37,618 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:28:37,619 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:28:37,619 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:28:37,628 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:28:42,952 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:28:43,595 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:28:43,602 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:28:43,603 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:28:43,603 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:28:43,605 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:28:48,086 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:28:48,684 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:28:48,692 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:28:48,693 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:28:48,693 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:28:48,699 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:28:54,565 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:28:55,245 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:28:55,252 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:28:55,259 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:28:55,259 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:28:55,261 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:29:01,125 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:29:01,756 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:29:01,764 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:29:01,765 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:29:01,765 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:29:01,772 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:29:06,006 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:29:06,659 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:29:06,666 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:29:06,667 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:29:06,668 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:29:06,674 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:29:12,311 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:29:12,957 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:29:12,965 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:29:12,970 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:29:12,971 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:29:12,973 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:29:17,663 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:29:18,510 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:29:18,518 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:29:18,520 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:29:18,520 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:29:18,526 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:29:22,783 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:29:23,405 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:29:23,412 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:29:23,422 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:29:23,422 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:29:23,424 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:29:28,226 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:29:29,343 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:29:29,363 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:29:29,365 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:29:29,365 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:29:29,379 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:29:34,032 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:29:34,654 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:29:34,657 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:29:34,662 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:29:34,662 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:29:34,664 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:29:39,154 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:29:40,241 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:29:40,247 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:29:40,248 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:29:40,249 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:29:40,255 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:29:44,939 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:29:45,583 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:29:45,590 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:29:45,591 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:29:45,591 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:29:45,593 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:29:51,539 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:29:52,136 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:29:52,140 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:29:52,146 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:29:52,146 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:29:52,148 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:29:57,090 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:29:57,751 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:29:57,759 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:29:57,761 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:29:57,761 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:29:57,767 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:30:02,203 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:30:02,861 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:30:02,869 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:30:02,874 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:30:02,874 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:30:02,876 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:30:07,078 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:30:07,732 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:30:07,740 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:30:07,741 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:30:07,741 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:30:07,747 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:30:11,758 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:30:12,606 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:30:12,614 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:30:12,615 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:30:12,616 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:30:12,622 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:30:18,750 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:30:19,399 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:30:19,407 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:30:19,408 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:30:19,408 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:30:19,415 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:30:24,768 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:30:25,419 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:30:25,427 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:30:25,428 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:30:25,428 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:30:25,435 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:30:31,309 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:30:31,960 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:30:31,968 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:30:31,973 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:30:31,974 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:30:31,976 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:30:36,288 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:30:36,958 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:30:36,966 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:30:36,967 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:30:36,967 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:30:36,969 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:30:42,592 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:30:43,223 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:30:43,231 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:30:43,232 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:30:43,232 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:30:43,239 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:30:48,190 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:30:49,803 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:30:49,811 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:30:49,812 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:30:49,812 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:30:49,819 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:30:54,090 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:30:54,924 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:30:54,931 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:30:54,932 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:30:54,932 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:30:54,939 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:31:00,395 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:31:01,043 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:31:01,051 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:31:01,052 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:31:01,052 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:31:01,058 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:31:06,659 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:31:07,321 - market_scanner_v2 - INFO - âœ… Fetched 129 markets from API
2025-11-04 01:31:07,329 - market_scanner_v2 - INFO - âœ… Got 129 markets from API
2025-11-04 01:31:07,334 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 129/129 markets passed
2025-11-04 01:31:07,335 - market_scanner_v2 - INFO - âœ… Found 129 qualifying markets (from 129 total)
2025-11-04 01:31:07,342 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:31:12,181 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:31:12,855 - market_scanner_v2 - INFO - âœ… Fetched 129 markets from API
2025-11-04 01:31:12,863 - market_scanner_v2 - INFO - âœ… Got 129 markets from API
2025-11-04 01:31:12,864 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 129/129 markets passed
2025-11-04 01:31:12,865 - market_scanner_v2 - INFO - âœ… Found 129 qualifying markets (from 129 total)
2025-11-04 01:31:12,872 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:31:18,200 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:31:18,818 - market_scanner_v2 - INFO - âœ… Fetched 129 markets from API
2025-11-04 01:31:18,825 - market_scanner_v2 - INFO - âœ… Got 129 markets from API
2025-11-04 01:31:18,827 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 129/129 markets passed
2025-11-04 01:31:18,827 - market_scanner_v2 - INFO - âœ… Found 129 qualifying markets (from 129 total)
2025-11-04 01:31:18,834 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:31:24,598 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:31:25,230 - market_scanner_v2 - INFO - âœ… Fetched 129 markets from API
2025-11-04 01:31:25,237 - market_scanner_v2 - INFO - âœ… Got 129 markets from API
2025-11-04 01:31:25,239 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 129/129 markets passed
2025-11-04 01:31:25,239 - market_scanner_v2 - INFO - âœ… Found 129 qualifying markets (from 129 total)
2025-11-04 01:31:25,247 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:31:29,636 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:31:30,335 - market_scanner_v2 - INFO - âœ… Fetched 129 markets from API
2025-11-04 01:31:30,343 - market_scanner_v2 - INFO - âœ… Got 129 markets from API
2025-11-04 01:31:30,344 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 129/129 markets passed
2025-11-04 01:31:30,344 - market_scanner_v2 - INFO - âœ… Found 129 qualifying markets (from 129 total)
2025-11-04 01:31:30,351 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:31:35,836 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:31:36,479 - market_scanner_v2 - INFO - âœ… Fetched 129 markets from API
2025-11-04 01:31:36,486 - market_scanner_v2 - INFO - âœ… Got 129 markets from API
2025-11-04 01:31:36,487 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 129/129 markets passed
2025-11-04 01:31:36,487 - market_scanner_v2 - INFO - âœ… Found 129 qualifying markets (from 129 total)
2025-11-04 01:31:36,494 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:31:40,618 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:31:41,277 - market_scanner_v2 - INFO - âœ… Fetched 129 markets from API
2025-11-04 01:31:41,285 - market_scanner_v2 - INFO - âœ… Got 129 markets from API
2025-11-04 01:31:41,290 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 129/129 markets passed
2025-11-04 01:31:41,290 - market_scanner_v2 - INFO - âœ… Found 129 qualifying markets (from 129 total)
2025-11-04 01:31:41,293 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:31:46,168 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:31:46,804 - market_scanner_v2 - INFO - âœ… Fetched 129 markets from API
2025-11-04 01:31:46,811 - market_scanner_v2 - INFO - âœ… Got 129 markets from API
2025-11-04 01:31:46,818 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 129/129 markets passed
2025-11-04 01:31:46,818 - market_scanner_v2 - INFO - âœ… Found 129 qualifying markets (from 129 total)
2025-11-04 01:31:46,820 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:31:52,265 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:31:52,975 - market_scanner_v2 - INFO - âœ… Fetched 129 markets from API
2025-11-04 01:31:52,982 - market_scanner_v2 - INFO - âœ… Got 129 markets from API
2025-11-04 01:31:52,983 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 129/129 markets passed
2025-11-04 01:31:52,983 - market_scanner_v2 - INFO - âœ… Found 129 qualifying markets (from 129 total)
2025-11-04 01:31:52,990 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:31:58,261 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:31:58,887 - market_scanner_v2 - INFO - âœ… Fetched 129 markets from API
2025-11-04 01:31:58,894 - market_scanner_v2 - INFO - âœ… Got 129 markets from API
2025-11-04 01:31:58,896 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 129/129 markets passed
2025-11-04 01:31:58,896 - market_scanner_v2 - INFO - âœ… Found 129 qualifying markets (from 129 total)
2025-11-04 01:31:58,902 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:32:03,288 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:32:03,955 - market_scanner_v2 - INFO - âœ… Fetched 129 markets from API
2025-11-04 01:32:03,963 - market_scanner_v2 - INFO - âœ… Got 129 markets from API
2025-11-04 01:32:03,964 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 129/129 markets passed
2025-11-04 01:32:03,965 - market_scanner_v2 - INFO - âœ… Found 129 qualifying markets (from 129 total)
2025-11-04 01:32:03,971 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:32:09,818 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:32:10,456 - market_scanner_v2 - INFO - âœ… Fetched 129 markets from API
2025-11-04 01:32:10,464 - market_scanner_v2 - INFO - âœ… Got 129 markets from API
2025-11-04 01:32:10,465 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 129/129 markets passed
2025-11-04 01:32:10,470 - market_scanner_v2 - INFO - âœ… Found 129 qualifying markets (from 129 total)
2025-11-04 01:32:10,472 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:32:15,193 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:32:15,831 - market_scanner_v2 - INFO - âœ… Fetched 129 markets from API
2025-11-04 01:32:15,838 - market_scanner_v2 - INFO - âœ… Got 129 markets from API
2025-11-04 01:32:15,839 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 129/129 markets passed
2025-11-04 01:32:15,839 - market_scanner_v2 - INFO - âœ… Found 129 qualifying markets (from 129 total)
2025-11-04 01:32:15,841 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:32:22,763 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:32:23,510 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:32:23,513 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:32:23,518 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:32:23,519 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:32:23,521 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:32:28,923 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:32:29,579 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:32:29,587 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:32:29,588 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:32:29,588 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:32:29,595 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:32:34,084 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:32:34,731 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:32:34,739 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:32:34,740 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:32:34,741 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:32:34,747 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:32:38,865 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:32:39,541 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:32:39,548 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:32:39,549 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:32:39,554 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:32:39,556 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:32:43,892 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:32:44,544 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:32:44,552 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:32:44,553 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:32:44,553 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:32:44,559 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:32:49,050 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:32:49,686 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:32:49,693 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:32:49,695 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:32:49,695 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:32:49,697 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:32:55,312 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:32:55,964 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:32:55,971 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:32:55,972 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:32:55,972 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:32:55,978 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:33:01,234 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:33:01,904 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:33:01,911 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:33:01,912 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:33:01,912 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:33:01,918 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:33:05,924 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:33:06,585 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:33:06,593 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:33:06,598 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:33:06,599 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:33:06,601 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:33:12,189 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:33:12,859 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:33:12,867 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:33:12,868 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:33:12,868 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:33:12,875 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:33:18,100 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:33:18,720 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:33:18,728 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:33:18,729 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:33:18,729 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:33:18,735 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:33:24,772 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:33:25,435 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:33:25,450 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:33:25,452 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:33:25,452 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:33:25,462 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:33:30,811 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:33:31,450 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:33:31,458 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:33:31,459 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:33:31,459 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:33:31,461 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:33:36,945 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:33:37,596 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:33:37,603 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:33:37,604 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:33:37,604 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:33:37,608 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:33:42,729 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:33:48,433 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:33:48,436 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:33:48,443 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:33:48,444 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:33:48,446 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:33:53,104 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:33:53,743 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:33:53,747 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:33:53,748 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:33:53,748 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:33:53,750 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:33:59,380 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:34:00,009 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:34:00,012 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:34:00,012 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:34:00,013 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:34:00,015 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:34:04,676 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:34:05,370 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:34:05,373 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:34:05,374 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:34:05,375 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:34:05,377 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:34:11,322 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:34:11,926 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:34:11,929 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:34:11,930 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:34:11,930 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:34:11,932 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:34:16,466 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:34:17,090 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:34:17,093 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:34:17,094 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:34:17,094 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:34:17,097 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:34:22,347 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:34:22,969 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:34:22,971 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:34:22,972 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:34:22,973 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:34:22,974 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:34:28,784 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:34:29,402 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:34:29,406 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:34:29,407 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:34:29,407 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:34:29,409 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:34:34,320 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:34:34,933 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:34:34,937 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:34:34,938 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:34:34,938 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:34:34,940 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:34:39,684 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:34:40,299 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:34:40,302 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:34:40,304 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:34:40,304 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:34:40,306 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:34:45,703 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:34:46,297 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:34:46,299 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:34:46,301 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:34:46,301 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:34:46,303 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:34:50,729 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:34:51,334 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:34:51,337 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:34:51,338 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:34:51,338 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:34:51,340 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:34:55,973 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:34:57,808 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:34:57,810 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:34:57,811 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:34:57,812 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:34:57,813 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:35:02,354 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:35:03,014 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:35:03,016 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:35:03,017 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:35:03,018 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:35:03,019 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:35:07,773 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:35:08,464 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:35:08,466 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:35:08,467 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:35:08,468 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:35:08,469 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:35:14,203 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:35:14,863 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:35:14,866 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:35:14,867 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:35:14,867 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:35:14,869 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:35:19,380 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:35:19,980 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:35:19,983 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:35:19,984 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:35:19,984 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:35:19,987 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:35:25,172 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:35:25,740 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:35:25,742 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:35:25,743 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:35:25,743 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:35:25,745 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:35:30,868 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:35:31,492 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:35:31,498 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:35:31,499 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:35:31,499 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:35:31,501 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:35:36,451 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:35:37,017 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:35:37,020 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:35:37,021 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:35:37,022 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:35:37,024 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:35:42,277 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:35:43,086 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:35:43,089 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:35:43,091 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:35:43,091 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:35:43,093 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:35:47,812 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:35:48,421 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:35:48,424 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:35:48,425 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:35:48,425 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:35:48,427 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:35:54,042 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:35:54,672 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:35:54,675 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:35:54,676 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:35:54,676 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:35:54,678 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:35:59,791 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:36:00,353 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:36:00,355 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:36:00,356 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:36:00,356 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:36:00,358 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:36:05,702 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:36:06,297 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:36:06,299 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:36:06,300 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:36:06,300 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:36:06,302 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:36:10,985 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:36:11,604 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:36:11,608 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:36:11,609 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:36:11,609 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:36:11,611 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:36:17,089 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:36:17,707 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:36:17,709 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:36:17,710 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:36:17,710 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:36:17,712 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:36:23,161 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:36:23,775 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:36:23,778 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:36:23,778 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:36:23,779 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:36:23,781 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:36:28,388 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:36:28,999 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:36:29,002 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:36:29,003 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:36:29,004 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:36:29,005 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:36:33,643 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:36:34,267 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:36:34,270 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:36:34,271 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:36:34,271 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:36:34,273 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:36:40,087 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:36:40,692 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:36:40,694 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:36:40,695 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:36:40,696 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:36:40,697 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:36:45,462 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:36:46,033 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:36:46,035 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:36:46,036 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:36:46,037 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:36:46,038 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:36:50,724 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:36:51,327 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:36:51,331 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:36:51,332 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:36:51,332 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:36:51,335 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:36:56,984 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:36:57,590 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:36:57,592 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:36:57,593 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:36:57,593 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:36:57,596 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:37:02,376 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:37:02,937 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:37:02,940 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:37:02,941 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:37:02,941 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:37:02,943 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:37:08,798 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:37:09,574 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:37:09,576 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:37:09,578 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:37:09,578 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:37:09,580 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:37:14,164 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:37:14,770 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:37:14,772 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:37:14,773 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:37:14,774 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:37:14,775 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:37:19,802 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:37:20,422 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:37:20,424 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:37:20,425 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:37:20,425 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:37:20,427 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:37:24,680 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:37:25,301 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:37:25,303 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:37:25,304 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:37:25,304 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:37:25,306 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:37:29,381 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:37:30,010 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:37:30,014 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:37:30,015 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:37:30,015 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:37:30,017 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:37:34,966 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:37:35,621 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:37:35,624 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:37:35,626 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:37:35,626 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:37:35,628 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:37:39,954 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:37:40,580 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:37:40,582 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:37:40,584 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:37:40,584 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:37:40,586 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:37:46,550 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:37:47,188 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:37:47,192 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:37:47,193 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:37:47,193 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:37:47,196 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:37:51,742 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:37:52,379 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:37:52,382 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:37:52,383 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:37:52,384 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:37:52,386 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:37:57,276 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:37:57,903 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:37:57,907 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:37:57,908 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:37:57,908 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:37:57,910 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:38:02,755 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:38:03,839 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:38:03,843 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:38:03,844 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:38:03,844 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:38:03,847 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:38:08,907 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:38:09,520 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:38:09,523 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:38:09,524 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:38:09,524 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:38:09,527 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:38:14,646 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:38:15,698 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:38:15,702 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:38:15,703 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:38:15,704 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:38:15,706 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:38:21,606 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:38:22,169 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:38:22,172 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:38:22,173 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:38:22,173 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:38:22,175 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:38:27,674 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:38:28,264 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:38:28,266 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:38:28,268 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:38:28,268 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:38:28,271 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:38:32,775 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:38:33,397 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:38:33,400 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:38:33,401 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:38:33,402 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:38:33,404 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:38:38,428 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:38:39,048 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:38:39,051 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:38:39,052 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:38:39,052 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:38:39,054 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:38:44,102 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:38:44,661 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:38:44,664 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:38:44,665 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:38:44,671 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:38:44,678 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:38:49,083 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:38:49,894 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:38:49,897 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:38:49,899 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:38:49,899 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:38:49,901 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:38:54,510 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:38:55,105 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:38:55,108 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:38:55,109 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:38:55,109 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:38:55,111 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:38:59,312 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:38:59,924 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:38:59,927 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:38:59,928 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:38:59,928 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:38:59,930 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:39:05,815 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:39:06,443 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:39:06,447 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:39:06,448 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:39:06,449 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:39:06,451 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:39:12,412 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:39:13,021 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:39:13,023 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:39:13,024 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:39:13,025 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:39:13,026 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:39:18,308 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:39:18,922 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:39:18,924 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:39:18,924 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:39:18,925 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:39:18,927 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:39:23,337 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:39:24,025 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:39:24,028 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:39:24,029 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:39:24,029 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:39:24,031 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:39:29,220 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:39:29,790 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:39:29,793 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:39:29,794 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:39:29,794 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:39:29,796 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:39:34,356 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:39:34,967 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:39:34,969 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:39:34,970 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:39:34,970 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:39:34,972 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:39:40,618 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:39:41,355 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:39:41,357 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:39:41,358 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:39:41,358 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:39:41,360 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:39:45,534 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:39:46,147 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:39:46,149 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:39:46,150 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:39:46,151 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:39:46,152 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:39:50,573 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:39:51,213 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:39:51,216 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:39:51,217 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:39:51,218 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:39:51,220 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:39:56,758 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:39:57,420 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:39:57,422 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:39:57,423 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:39:57,424 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:39:57,426 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:40:02,046 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:40:02,649 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:40:02,651 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:40:02,652 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:40:02,653 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:40:02,655 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:40:07,832 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:40:08,472 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:40:08,474 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:40:08,475 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:40:08,476 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:40:08,478 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:40:12,547 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:40:13,107 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:40:13,109 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:40:13,110 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:40:13,110 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:40:13,112 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:40:18,723 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:40:19,381 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:40:19,384 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:40:19,385 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:40:19,385 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:40:19,387 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:40:23,538 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:40:24,168 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:40:24,170 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:40:24,171 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:40:24,171 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:40:24,173 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:40:30,114 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:40:30,740 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:40:30,743 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:40:30,745 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:40:30,745 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:40:30,747 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:40:35,892 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:40:36,531 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:40:36,534 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:40:36,535 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:40:36,535 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:40:36,537 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:40:41,327 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:40:41,987 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:40:41,990 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:40:41,991 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:40:41,991 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:40:41,993 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:40:47,280 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:40:47,851 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:40:47,855 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:40:47,857 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:40:47,857 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:40:47,859 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:40:52,779 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:40:53,416 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:40:53,423 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:40:53,424 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:40:53,424 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:40:53,430 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:40:57,606 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:40:58,240 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:40:58,244 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:40:58,245 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:40:58,245 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:40:58,247 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:41:03,143 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:41:03,741 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:41:03,744 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:41:03,746 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:41:03,746 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:41:03,748 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:41:09,828 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:41:10,550 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:41:10,553 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:41:10,554 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:41:10,554 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:41:10,557 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:41:15,174 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:41:15,734 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:41:15,738 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:41:15,739 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:41:15,739 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:41:15,740 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:41:20,243 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:41:20,854 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:41:20,856 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:41:20,857 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:41:20,857 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:41:20,859 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:41:25,547 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:41:26,172 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:41:26,175 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:41:26,175 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:41:26,176 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:41:26,178 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:41:31,051 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:41:31,628 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:41:31,631 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:41:31,633 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:41:31,633 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:41:31,635 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:41:37,179 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:41:37,859 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:41:37,861 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:41:37,862 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:41:37,862 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:41:37,864 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:41:42,353 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:41:43,000 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:41:43,004 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:41:43,005 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:41:43,005 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:41:43,006 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:41:48,137 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:41:48,773 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:41:48,776 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:41:48,777 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:41:48,777 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:41:48,779 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:41:53,762 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:41:54,375 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:41:54,379 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:41:54,380 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:41:54,380 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:41:54,382 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:41:59,724 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:42:00,355 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:42:00,359 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:42:00,360 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:42:00,360 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:42:00,363 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:42:06,013 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:42:06,648 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:42:06,650 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:42:06,651 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:42:06,651 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:42:06,653 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:42:11,836 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:42:12,467 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:42:12,470 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:42:12,472 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:42:12,472 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:42:12,474 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:42:16,669 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:42:17,265 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:42:17,268 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:42:17,269 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:42:17,269 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:42:17,271 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:42:21,785 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:42:22,379 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:42:22,382 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:42:22,383 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:42:22,383 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:42:22,385 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:42:28,119 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:42:28,685 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:42:28,688 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:42:28,690 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:42:28,690 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:42:28,692 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:42:33,580 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:42:34,199 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:42:34,202 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:42:34,203 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:42:34,203 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:42:34,204 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:42:39,849 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:42:40,468 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:42:40,471 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:42:40,472 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:42:40,472 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:42:40,474 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:42:45,001 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:42:45,577 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:42:45,580 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:42:45,581 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:42:45,582 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:42:45,583 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:42:50,140 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:42:50,745 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:42:50,748 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:42:50,749 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:42:50,749 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:42:50,751 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:42:56,485 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:42:57,042 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:42:57,045 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:42:57,046 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:42:57,046 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:42:57,048 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:43:01,826 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:43:02,430 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:43:02,433 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:43:02,435 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:43:02,436 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:43:02,437 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:43:08,385 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:43:08,988 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:43:08,992 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:43:08,994 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:43:08,994 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:43:08,997 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:43:14,307 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:43:14,935 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:43:14,938 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:43:14,939 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:43:14,940 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:43:14,942 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:43:20,913 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:43:21,535 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:43:21,537 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:43:21,538 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:43:21,539 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:43:21,540 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:43:26,342 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:43:26,942 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:43:26,945 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:43:26,946 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:43:26,946 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:43:26,948 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:43:32,578 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:43:33,196 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:43:33,200 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:43:33,202 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:43:33,202 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:43:33,204 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:43:37,449 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:43:38,028 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:43:38,031 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:43:38,032 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:43:38,033 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:43:38,035 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:43:43,824 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:43:44,873 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:43:44,877 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:43:44,878 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:43:44,878 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:43:44,880 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:43:49,284 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:43:49,863 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:43:49,867 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:43:49,869 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:43:49,869 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:43:49,871 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:43:55,515 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:43:56,095 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:43:56,098 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:43:56,099 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:43:56,099 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:43:56,100 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:44:00,637 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:44:01,246 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:44:01,248 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:44:01,250 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:44:01,250 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:44:01,252 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:44:06,252 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:44:06,798 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:44:06,800 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:44:06,801 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:44:06,802 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:44:06,803 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:44:11,686 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:44:12,485 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:44:12,488 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:44:12,490 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:44:12,490 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:44:12,492 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:44:17,808 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:44:18,426 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:44:18,429 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:44:18,430 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:44:18,430 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:44:18,432 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:44:22,736 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:44:23,352 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:44:23,354 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:44:23,355 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:44:23,355 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:44:23,357 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:44:28,224 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:44:28,842 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:44:28,845 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:44:28,846 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:44:28,846 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:44:28,848 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:44:34,696 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:44:35,307 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:44:35,310 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:44:35,311 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:44:35,311 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:44:35,312 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:44:40,899 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:44:41,482 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:44:41,484 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:44:41,485 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:44:41,486 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:44:41,487 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:44:47,083 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:44:47,642 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:44:47,645 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:44:47,646 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:44:47,646 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:44:47,648 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:44:53,621 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:44:54,224 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:44:54,227 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:44:54,229 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:44:54,229 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:44:54,231 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:44:58,421 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:44:59,035 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:44:59,037 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:44:59,038 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:44:59,038 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:44:59,040 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:45:04,585 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:45:05,217 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:45:05,220 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:45:05,221 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:45:05,221 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:45:05,223 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:45:11,038 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:45:11,637 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:45:11,639 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:45:11,640 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:45:11,640 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:45:11,642 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:45:17,863 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:45:18,487 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:45:18,490 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:45:18,491 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:45:18,491 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:45:18,493 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:45:23,976 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:45:24,592 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:45:24,595 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:45:24,596 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:45:24,596 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:45:24,597 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:45:29,125 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:45:29,733 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:45:29,735 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:45:29,736 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:45:29,736 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:45:29,738 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:45:35,531 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:45:36,152 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:45:36,155 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:45:36,156 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:45:36,156 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:45:36,157 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:45:40,924 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:45:41,535 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:45:41,538 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:45:41,539 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:45:41,539 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:45:41,541 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:45:45,782 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:45:46,405 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:45:46,407 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:45:46,408 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:45:46,408 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:45:46,410 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:45:52,166 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:45:52,726 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:45:52,729 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:45:52,730 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:45:52,730 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:45:52,732 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:45:58,293 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:45:58,897 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:45:58,900 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:45:58,901 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:45:58,901 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:45:58,903 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:46:04,437 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:46:05,054 - market_scanner_v2 - INFO - âœ… Fetched 129 markets from API
2025-11-04 01:46:05,057 - market_scanner_v2 - INFO - âœ… Got 129 markets from API
2025-11-04 01:46:05,058 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 129/129 markets passed
2025-11-04 01:46:05,058 - market_scanner_v2 - INFO - âœ… Found 129 qualifying markets (from 129 total)
2025-11-04 01:46:05,060 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:46:09,968 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:46:10,757 - market_scanner_v2 - INFO - âœ… Fetched 129 markets from API
2025-11-04 01:46:10,759 - market_scanner_v2 - INFO - âœ… Got 129 markets from API
2025-11-04 01:46:10,760 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 129/129 markets passed
2025-11-04 01:46:10,761 - market_scanner_v2 - INFO - âœ… Found 129 qualifying markets (from 129 total)
2025-11-04 01:46:10,763 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:46:15,187 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:46:15,821 - market_scanner_v2 - INFO - âœ… Fetched 129 markets from API
2025-11-04 01:46:15,831 - market_scanner_v2 - INFO - âœ… Got 129 markets from API
2025-11-04 01:46:15,832 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 129/129 markets passed
2025-11-04 01:46:15,832 - market_scanner_v2 - INFO - âœ… Found 129 qualifying markets (from 129 total)
2025-11-04 01:46:15,843 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:46:20,427 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:46:21,059 - market_scanner_v2 - INFO - âœ… Fetched 129 markets from API
2025-11-04 01:46:21,063 - market_scanner_v2 - INFO - âœ… Got 129 markets from API
2025-11-04 01:46:21,064 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 129/129 markets passed
2025-11-04 01:46:21,064 - market_scanner_v2 - INFO - âœ… Found 129 qualifying markets (from 129 total)
2025-11-04 01:46:21,067 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:46:26,672 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:46:27,389 - market_scanner_v2 - INFO - âœ… Fetched 129 markets from API
2025-11-04 01:46:27,391 - market_scanner_v2 - INFO - âœ… Got 129 markets from API
2025-11-04 01:46:27,392 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 129/129 markets passed
2025-11-04 01:46:27,392 - market_scanner_v2 - INFO - âœ… Found 129 qualifying markets (from 129 total)
2025-11-04 01:46:27,394 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:46:32,924 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:46:33,553 - market_scanner_v2 - INFO - âœ… Fetched 129 markets from API
2025-11-04 01:46:33,561 - market_scanner_v2 - INFO - âœ… Got 129 markets from API
2025-11-04 01:46:33,566 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 129/129 markets passed
2025-11-04 01:46:33,567 - market_scanner_v2 - INFO - âœ… Found 129 qualifying markets (from 129 total)
2025-11-04 01:46:33,574 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:46:38,683 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:46:39,521 - market_scanner_v2 - INFO - âœ… Fetched 129 markets from API
2025-11-04 01:46:39,527 - market_scanner_v2 - INFO - âœ… Got 129 markets from API
2025-11-04 01:46:39,530 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 129/129 markets passed
2025-11-04 01:46:39,531 - market_scanner_v2 - INFO - âœ… Found 129 qualifying markets (from 129 total)
2025-11-04 01:46:39,533 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:46:45,332 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:46:45,958 - market_scanner_v2 - INFO - âœ… Fetched 129 markets from API
2025-11-04 01:46:45,962 - market_scanner_v2 - INFO - âœ… Got 129 markets from API
2025-11-04 01:46:45,963 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 129/129 markets passed
2025-11-04 01:46:45,963 - market_scanner_v2 - INFO - âœ… Found 129 qualifying markets (from 129 total)
2025-11-04 01:46:45,966 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:46:50,876 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:46:51,492 - market_scanner_v2 - INFO - âœ… Fetched 129 markets from API
2025-11-04 01:46:51,494 - market_scanner_v2 - INFO - âœ… Got 129 markets from API
2025-11-04 01:46:51,495 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 129/129 markets passed
2025-11-04 01:46:51,495 - market_scanner_v2 - INFO - âœ… Found 129 qualifying markets (from 129 total)
2025-11-04 01:46:51,498 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:46:56,011 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:46:56,577 - market_scanner_v2 - INFO - âœ… Fetched 129 markets from API
2025-11-04 01:46:56,580 - market_scanner_v2 - INFO - âœ… Got 129 markets from API
2025-11-04 01:46:56,581 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 129/129 markets passed
2025-11-04 01:46:56,582 - market_scanner_v2 - INFO - âœ… Found 129 qualifying markets (from 129 total)
2025-11-04 01:46:56,584 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:47:02,002 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:47:02,663 - market_scanner_v2 - INFO - âœ… Fetched 129 markets from API
2025-11-04 01:47:02,671 - market_scanner_v2 - INFO - âœ… Got 129 markets from API
2025-11-04 01:47:02,672 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 129/129 markets passed
2025-11-04 01:47:02,672 - market_scanner_v2 - INFO - âœ… Found 129 qualifying markets (from 129 total)
2025-11-04 01:47:02,679 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:47:06,840 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:47:07,448 - market_scanner_v2 - INFO - âœ… Fetched 129 markets from API
2025-11-04 01:47:07,456 - market_scanner_v2 - INFO - âœ… Got 129 markets from API
2025-11-04 01:47:07,457 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 129/129 markets passed
2025-11-04 01:47:07,462 - market_scanner_v2 - INFO - âœ… Found 129 qualifying markets (from 129 total)
2025-11-04 01:47:07,464 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:47:12,202 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:47:12,805 - market_scanner_v2 - INFO - âœ… Fetched 129 markets from API
2025-11-04 01:47:12,812 - market_scanner_v2 - INFO - âœ… Got 129 markets from API
2025-11-04 01:47:12,813 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 129/129 markets passed
2025-11-04 01:47:12,818 - market_scanner_v2 - INFO - âœ… Found 129 qualifying markets (from 129 total)
2025-11-04 01:47:12,820 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:47:18,220 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:47:18,873 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:47:18,880 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:47:18,886 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:47:18,886 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:47:18,889 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:47:24,166 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:47:24,808 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:47:24,810 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:47:24,811 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:47:24,811 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:47:24,813 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:47:29,076 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:47:29,671 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:47:29,674 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:47:29,675 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:47:29,675 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:47:29,678 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:47:34,225 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:47:34,819 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:47:34,821 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:47:34,822 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:47:34,822 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:47:34,824 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:47:40,606 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:47:41,232 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:47:41,235 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:47:41,236 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:47:41,236 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:47:41,238 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:47:45,666 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:47:46,257 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:47:46,259 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:47:46,260 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:47:46,261 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:47:46,263 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:47:51,082 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:47:51,723 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:47:51,726 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:47:51,727 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:47:51,727 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:47:51,729 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:47:57,018 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:47:57,641 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:47:57,644 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:47:57,645 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:47:57,645 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:47:57,647 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:48:01,923 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:48:02,542 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:48:02,545 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:48:02,546 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:48:02,546 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:48:02,548 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:48:07,952 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:48:08,572 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:48:08,575 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:48:08,576 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:48:08,576 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:48:08,578 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:48:12,584 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:48:13,182 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:48:13,185 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:48:13,186 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:48:13,187 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:48:13,188 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:48:18,057 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:48:18,637 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:48:18,641 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:48:18,642 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:48:18,642 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:48:18,644 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:48:23,887 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:48:24,448 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:48:24,451 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:48:24,452 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:48:24,452 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:48:24,454 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:48:30,048 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:48:30,668 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:48:30,670 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:48:30,671 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:48:30,671 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:48:30,672 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:48:35,646 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:48:36,276 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:48:36,278 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:48:36,280 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:48:36,280 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:48:36,282 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:48:40,437 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:48:41,021 - market_scanner_v2 - INFO - âœ… Fetched 119 markets from API
2025-11-04 01:48:41,024 - market_scanner_v2 - INFO - âœ… Got 119 markets from API
2025-11-04 01:48:41,025 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 119/119 markets passed
2025-11-04 01:48:41,025 - market_scanner_v2 - INFO - âœ… Found 119 qualifying markets (from 119 total)
2025-11-04 01:48:41,026 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:48:45,532 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:48:46,099 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:48:46,101 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:48:46,102 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:48:46,102 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:48:46,104 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:48:51,635 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:48:52,201 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:48:52,203 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:48:52,204 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:48:52,205 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:48:52,207 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:48:57,565 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:48:58,173 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:48:58,175 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:48:58,176 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:48:58,176 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:48:58,178 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:49:03,924 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:49:04,537 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:49:04,540 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:49:04,541 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:49:04,541 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:49:04,543 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:49:09,672 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:49:10,272 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:49:10,274 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:49:10,275 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:49:10,275 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:49:10,277 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:49:15,130 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:49:15,704 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:49:15,708 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:49:15,709 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:49:15,709 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:49:15,711 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:49:20,836 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:49:21,430 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:49:21,432 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:49:21,433 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:49:21,434 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:49:21,435 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:49:27,025 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:49:27,635 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:49:27,637 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:49:27,639 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:49:27,639 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:49:27,641 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:49:33,282 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:49:33,868 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:49:33,871 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:49:33,872 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:49:33,872 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:49:33,874 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:49:38,522 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:49:39,115 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:49:39,119 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:49:39,120 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:49:39,120 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:49:39,122 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:49:44,394 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:49:45,026 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:49:45,029 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:49:45,030 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:49:45,030 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:49:45,032 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:49:50,071 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:49:50,694 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:49:50,697 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:49:50,698 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:49:50,698 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:49:50,701 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:49:55,712 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:49:56,928 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:49:56,931 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:49:56,933 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:49:56,933 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:49:56,935 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:50:01,280 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:50:01,877 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:50:01,879 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:50:01,880 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:50:01,880 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:50:01,882 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:50:07,542 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:50:08,121 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:50:08,124 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:50:08,125 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:50:08,125 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:50:08,127 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:50:12,534 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:50:13,310 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:50:13,313 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:50:13,314 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:50:13,315 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:50:13,316 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:50:18,912 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:50:19,541 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:50:19,545 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:50:19,546 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:50:19,546 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:50:19,548 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:50:25,277 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:50:25,866 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:50:25,869 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:50:25,870 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:50:25,870 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:50:25,872 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:50:29,910 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:50:30,533 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:50:30,535 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:50:30,536 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:50:30,537 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:50:30,539 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:50:35,002 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:50:35,603 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:50:35,606 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:50:35,606 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:50:35,607 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:50:35,608 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:50:39,678 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:50:40,314 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:50:40,317 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:50:40,326 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:50:40,326 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:50:40,328 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:50:44,962 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:50:45,565 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:50:45,567 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:50:45,568 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:50:45,568 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:50:45,570 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:50:50,483 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:50:51,072 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:50:51,076 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:50:51,077 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:50:51,077 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:50:51,079 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:50:56,527 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:50:57,380 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:50:57,384 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:50:57,385 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:50:57,385 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:50:57,387 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:51:02,010 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:51:02,623 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:51:02,626 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:51:02,627 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:51:02,628 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:51:02,630 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:51:06,798 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:51:07,420 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:51:07,422 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:51:07,423 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:51:07,424 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:51:07,426 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:51:12,587 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:51:13,225 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:51:13,228 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:51:13,229 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:51:13,229 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:51:13,231 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:51:19,056 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:51:19,686 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:51:19,688 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:51:19,689 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:51:19,689 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:51:19,691 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:51:25,597 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:51:26,235 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:51:26,238 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:51:26,239 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:51:26,240 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:51:26,242 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:51:30,449 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:51:31,080 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:51:31,084 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:51:31,085 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:51:31,085 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:51:31,087 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:51:35,893 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:51:36,496 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:51:36,499 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:51:36,499 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:51:36,500 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:51:36,503 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:51:42,250 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:51:42,837 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:51:42,841 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:51:42,842 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:51:42,842 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:51:42,844 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:51:48,675 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:51:49,278 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:51:49,281 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:51:49,282 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:51:49,282 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:51:49,284 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:51:55,210 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:51:56,013 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:51:56,017 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:51:56,018 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:51:56,019 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:51:56,021 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:52:00,915 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:52:01,530 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:52:01,532 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:52:01,533 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:52:01,534 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:52:01,536 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:52:05,595 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:52:06,166 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:52:06,168 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:52:06,169 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:52:06,170 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:52:06,172 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:52:10,764 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:52:11,369 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:52:11,371 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:52:11,372 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:52:11,372 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:52:11,374 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:52:15,378 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:52:16,017 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:52:16,020 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:52:16,020 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:52:16,021 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:52:16,023 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:52:21,983 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:52:22,603 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:52:22,607 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:52:22,608 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:52:22,609 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:52:22,611 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:52:27,373 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:52:28,100 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:52:28,103 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:52:28,103 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:52:28,104 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:52:28,105 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:52:32,233 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:52:32,844 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:52:32,847 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:52:32,848 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:52:32,848 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:52:32,851 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:52:37,094 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:52:37,683 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:52:37,686 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:52:37,686 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:52:37,687 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:52:37,688 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:52:43,415 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:52:44,009 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:52:44,012 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:52:44,013 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:52:44,013 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:52:44,015 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:52:48,708 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:52:49,314 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:52:49,317 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:52:49,318 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:52:49,318 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:52:49,320 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:52:54,789 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:52:55,350 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:52:55,353 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:52:55,354 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:52:55,354 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:52:55,356 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:53:01,179 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:53:01,736 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:53:01,738 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:53:01,739 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:53:01,740 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:53:01,741 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:53:06,135 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:53:06,748 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:53:06,750 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:53:06,751 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:53:06,751 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:53:06,752 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:53:12,124 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:53:12,747 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:53:12,750 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:53:12,751 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:53:12,751 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:53:12,753 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:53:17,557 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:53:18,426 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:53:18,429 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:53:18,430 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:53:18,430 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:53:18,431 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:53:22,523 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:53:23,132 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:53:23,135 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:53:23,136 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:53:23,136 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:53:23,138 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:53:28,091 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:53:28,713 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:53:28,717 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:53:28,718 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:53:28,719 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:53:28,721 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:53:34,410 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:53:35,039 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:53:35,043 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:53:35,044 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:53:35,045 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:53:35,047 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:53:40,161 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:53:40,792 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:53:40,794 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:53:40,795 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:53:40,796 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:53:40,797 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:53:46,624 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:53:47,254 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:53:47,258 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:53:47,259 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:53:47,260 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:53:47,262 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:53:53,238 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:53:53,845 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:53:53,850 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:53:53,851 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:53:53,851 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:53:53,853 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:53:57,945 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:53:58,565 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:53:58,571 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:53:58,572 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:53:58,573 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:53:58,576 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:54:02,643 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:54:03,217 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:54:03,220 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:54:03,222 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:54:03,222 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:54:03,223 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:54:08,042 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:54:08,668 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:54:08,672 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:54:08,673 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:54:08,674 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:54:08,675 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:54:13,327 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:54:13,965 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:54:13,967 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:54:13,970 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:54:13,970 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:54:13,972 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:54:18,920 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:54:19,539 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:54:19,542 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:54:19,543 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:54:19,543 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:54:19,545 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:54:24,772 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:54:25,394 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:54:25,397 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:54:25,398 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:54:25,398 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:54:25,400 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:54:29,688 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:54:30,294 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:54:30,297 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:54:30,298 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:54:30,298 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:54:30,300 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:54:35,936 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:54:36,552 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:54:36,555 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:54:36,556 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:54:36,556 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:54:36,557 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:54:41,103 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:54:41,669 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:54:41,672 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:54:41,673 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:54:41,673 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:54:41,675 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:54:45,759 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:54:46,334 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:54:46,337 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:54:46,338 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:54:46,338 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:54:46,340 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:54:52,195 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:54:52,785 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:54:52,788 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:54:52,789 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:54:52,789 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:54:52,791 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:54:58,052 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:54:58,683 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:54:58,690 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:54:58,691 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:54:58,691 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:54:58,693 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:55:03,174 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:55:03,764 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:55:03,767 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:55:03,768 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:55:03,769 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:55:03,770 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:55:08,154 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:55:08,729 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:55:08,732 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:55:08,733 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:55:08,733 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:55:08,736 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:55:12,858 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:55:13,446 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:55:13,449 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:55:13,450 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:55:13,450 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:55:13,452 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:55:17,988 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:55:18,556 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:55:18,560 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:55:18,561 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:55:18,562 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:55:18,564 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:55:23,314 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:55:23,911 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:55:23,913 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:55:23,914 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:55:23,914 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:55:23,916 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:55:29,006 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:55:29,591 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:55:29,594 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:55:29,595 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:55:29,595 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:55:29,597 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:55:34,993 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:55:35,631 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:55:35,635 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:55:35,636 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:55:35,636 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:55:35,638 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:55:40,958 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:55:41,618 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:55:41,621 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:55:41,627 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:55:41,627 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:55:41,634 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:55:47,028 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:55:47,671 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:55:47,679 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:55:47,680 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:55:47,680 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:55:47,687 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:55:52,755 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:55:53,408 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:55:53,417 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:55:53,422 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:55:53,423 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:55:53,425 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:55:58,596 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:55:59,242 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:55:59,245 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:55:59,251 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:55:59,251 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:55:59,253 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:56:04,302 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:56:04,932 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:56:04,940 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:56:04,941 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:56:04,946 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:56:04,948 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:56:10,547 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:56:11,173 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:56:11,180 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:56:11,181 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:56:11,181 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:56:11,187 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:56:16,456 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:56:17,067 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:56:17,074 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:56:17,075 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:56:17,075 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:56:17,077 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:56:22,745 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:56:23,359 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:56:23,362 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:56:23,364 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:56:23,364 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:56:23,366 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:56:29,012 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:56:29,639 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:56:29,641 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:56:29,642 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:56:29,642 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:56:29,644 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:56:34,051 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:56:34,663 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:56:34,665 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:56:34,666 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:56:34,666 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:56:34,668 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:56:39,952 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:56:40,574 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:56:40,578 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:56:40,579 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:56:40,580 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:56:40,582 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:56:46,229 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:56:46,824 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:56:46,828 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:56:46,829 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:56:46,829 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:56:46,831 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:56:52,113 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:56:52,734 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:56:52,737 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:56:52,738 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:56:52,738 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:56:52,740 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:56:57,769 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:56:58,391 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:56:58,393 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:56:58,398 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:56:58,398 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:56:58,399 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:57:04,023 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:57:04,600 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:57:04,603 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:57:04,604 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:57:04,604 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:57:04,606 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:57:10,956 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:57:11,597 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:57:11,599 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:57:11,600 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:57:11,601 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:57:11,602 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:57:13,496 - ml_predictor - INFO - Insufficient training data: 0 samples
2025-11-04 01:57:13,497 - __main__ - INFO - ML model updated successfully
2025-11-04 01:57:17,272 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:57:17,884 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:57:17,887 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:57:17,888 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:57:17,888 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:57:17,890 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:57:22,245 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:57:22,857 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:57:22,860 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:57:22,862 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:57:22,862 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:57:22,864 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:57:28,334 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:57:28,896 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:57:28,899 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:57:28,900 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:57:28,901 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:57:28,902 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:57:33,126 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:57:33,708 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:57:33,710 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:57:33,711 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:57:33,711 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:57:33,713 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:57:39,323 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:57:39,911 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:57:39,914 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:57:39,915 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:57:39,916 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:57:39,918 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:57:45,150 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:57:45,737 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:57:45,739 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:57:45,740 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:57:45,740 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:57:45,742 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:57:51,662 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:57:52,249 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:57:52,253 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:57:52,254 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:57:52,254 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:57:52,256 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:57:57,945 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:57:58,712 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:57:58,715 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:57:58,716 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:57:58,716 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:57:58,718 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:58:03,282 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:58:03,896 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:58:03,899 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:58:03,900 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:58:03,900 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:58:03,902 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:58:08,797 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:58:09,410 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:58:09,413 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:58:09,414 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:58:09,414 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:58:09,416 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:58:14,672 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:58:15,252 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:58:15,254 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:58:15,255 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:58:15,255 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:58:15,257 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:58:21,253 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:58:21,872 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:58:21,876 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:58:21,877 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:58:21,877 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:58:21,879 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:58:27,363 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:58:28,173 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:58:28,176 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:58:28,178 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:58:28,178 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:58:28,180 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:58:33,065 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:58:33,650 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:58:33,653 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:58:33,654 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:58:33,654 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:58:33,656 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:58:39,611 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:58:40,199 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:58:40,202 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:58:40,203 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:58:40,203 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:58:40,205 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:58:45,249 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:58:45,838 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:58:45,841 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:58:45,842 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:58:45,842 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:58:45,844 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:58:50,393 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:58:51,004 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:58:51,006 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:58:51,007 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:58:51,007 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:58:51,010 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:58:56,764 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:58:57,364 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:58:57,366 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:58:57,367 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:58:57,367 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:58:57,369 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:59:01,860 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:59:02,742 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:59:02,745 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:59:02,746 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:59:02,746 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:59:02,748 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:59:07,479 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:59:08,073 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:59:08,075 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:59:08,076 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:59:08,077 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:59:08,079 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:59:12,816 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:59:13,433 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:59:13,435 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:59:13,436 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:59:13,436 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:59:13,438 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:59:18,038 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:59:18,681 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:59:18,688 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:59:18,689 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:59:18,694 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:59:18,695 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:59:23,354 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:59:23,996 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:59:24,000 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:59:24,001 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:59:24,002 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:59:24,004 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:59:29,248 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:59:29,836 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:59:29,839 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:59:29,840 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:59:29,841 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:59:29,843 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:59:35,057 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:59:35,666 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:59:35,668 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:59:35,669 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:59:35,670 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:59:35,672 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:59:40,142 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:59:40,747 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:59:40,750 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:59:40,751 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:59:40,751 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:59:40,753 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:59:45,985 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:59:46,608 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:59:46,611 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:59:46,612 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:59:46,612 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:59:46,614 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:59:51,796 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:59:52,359 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:59:52,362 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:59:52,363 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:59:52,363 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:59:52,364 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 01:59:57,852 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 01:59:58,479 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 01:59:58,481 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 01:59:58,482 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 01:59:58,482 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 01:59:58,484 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 02:00:01,750 - ml_predictor - INFO - Alert sent: âœ… <b>Hourly Report</b>
â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”
â° Time: 2025-11-04 02:00:01

ðŸ“Š <b>Performance (Last 60 min)</b>
   â€¢ Scans: 100
   â€¢ Markets found: 11800 (118.0/scan)
   â€¢ Orders placed: 0
   â€¢ Orders filled: 0 (0.0%)
   â€¢ Profit: $0.00
   â€¢ Errors: 0 (0.0%)

ðŸ’» <b>System Health</b>
   â€¢ CPU: 39.0%
   â€¢ RAM: 69.8%
   â€¢ Bot RAM: 138 MB
        
â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”
2025-11-04 02:00:01,751 - monitoring_system - INFO - âœ… Hourly report sent
2025-11-04 02:00:02,698 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:00:03,306 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 02:00:03,309 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 02:00:03,317 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 02:00:03,318 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 02:00:03,319 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 02:00:08,970 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:00:09,737 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 02:00:09,751 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 02:00:09,752 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 02:00:09,753 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 02:00:09,769 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 02:00:15,658 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:00:17,081 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 02:00:17,099 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 02:00:17,100 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 02:00:17,100 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 02:00:17,109 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 02:00:21,761 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:00:22,496 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 02:00:22,512 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 02:00:22,512 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 02:00:22,513 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 02:00:22,528 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 02:00:27,098 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:00:27,824 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 02:00:27,840 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 02:00:27,841 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 02:00:27,847 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 02:00:27,855 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 02:00:33,658 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:00:34,303 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 02:00:34,309 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 02:00:34,310 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 02:00:34,311 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 02:00:34,312 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 02:00:39,925 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:00:40,516 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 02:00:40,523 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 02:00:40,524 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 02:00:40,524 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 02:00:40,530 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 02:00:44,708 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:00:45,350 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 02:00:45,353 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 02:00:45,358 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 02:00:45,358 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 02:00:45,360 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 02:00:51,330 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:00:51,967 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 02:00:51,974 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 02:00:51,975 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 02:00:51,975 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 02:00:51,977 - market_selector - ERROR - Market selection error: 'title'
2025-11-04 02:00:56,173 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:00:56,754 - market_scanner_v2 - INFO - âœ… Fetched 118 markets from API
2025-11-04 02:00:56,757 - market_scanner_v2 - INFO - âœ… Got 118 markets from API
2025-11-04 02:00:56,758 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 118/118 markets passed
2025-11-04 02:00:56,759 - market_scanner_v2 - INFO - âœ… Found 118 qualifying markets (from 118 total)
2025-11-04 02:00:56,760 - market_selector - ERROR - Market selection error: 'title'
