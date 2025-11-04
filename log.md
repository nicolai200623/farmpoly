2025-11-04 05:09:49,848 - __main__ - INFO - âœ… Using MarketScannerV2 (Playwright + Gamma API)
2025-11-04 05:09:54,581 - __main__ - INFO - âœ… Telegram alerts configured (Chat ID: -1003157421030)
2025-11-04 05:09:54,581 - __main__ - INFO - âœ… Webhook alerts configured
2025-11-04 05:09:54,582 - circuit_breaker - INFO - âœ… Circuit Breaker 'gamma_api' initialized (threshold=5, timeout=60s)
2025-11-04 05:09:54,582 - circuit_breaker - INFO - âœ… Circuit Breaker 'playwright_scraper' initialized (threshold=3, timeout=120s)
2025-11-04 05:09:54,582 - order_manager - INFO - CLOB client initialized successfully (read-only mode)
2025-11-04 05:09:54,593 - wallet_manager - INFO - Loading REAL wallets from .env
2025-11-04 05:09:54,602 - wallet_manager - INFO - âœ… Loaded wallet 1: 0x18F261DC...Ae4FfD96
2025-11-04 05:09:54,602 - wallet_manager - INFO - âœ… Successfully loaded 1 real wallets
2025-11-04 05:09:54,610 - ml_predictor - INFO - No pre-trained model found, using new model
2025-11-04 05:09:54,610 - monitoring_system - INFO - âœ… Monitoring System initialized
2025-11-04 05:09:54,610 - __main__ - INFO - âœ… Monitoring System enabled
2025-11-04 05:09:54,610 - __main__ - INFO - â­ï¸  Reward Manager disabled in config
2025-11-04 05:09:54,611 - __main__ - INFO - All modules initialized successfully
2025-11-04 05:09:54,611 - __main__ - INFO - ðŸš€ Starting Polymarket Trading Bot...
2025-11-04 05:09:55,404 - ml_predictor - INFO - Alert sent: ðŸš€ <b>Polymarket Bot Started</b>
â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”
â° Time: 2025-11-04 05:09:54
ðŸ’¼ Wallets: 1
ðŸ“Š Status: Running
â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”
Bot is now scanning markets and placing orders.
2025-11-04 05:09:55,404 - __main__ - INFO - âœ… Startup alert sent
2025-11-04 05:09:55,404 - __main__ - INFO - ðŸ” Checking USDC approval for wallets...
2025-11-04 05:09:55,548 - usdc_approver - INFO - âœ… Connected to Polygon RPC: https://polygon-mainnet.g.alchemy.com/v2/FQJnJWsEQ...
2025-11-04 05:09:55,548 - __main__ - INFO -    Checking wallet: 0x18F261DC...Ae4FfD96
2025-11-04 05:09:55,731 - __main__ - INFO -    Raw allowance: 100000000 (base units)
2025-11-04 05:09:55,731 - __main__ - INFO -    Allowance in USDC: 100.00 USDC
2025-11-04 05:09:55,732 - __main__ - INFO -    Required minimum: 100 USDC (test mode)
2025-11-04 05:09:55,732 - __main__ - INFO - âœ… USDC approval OK (100 USDC)
2025-11-04 05:09:55,732 - __main__ - WARNING -    âš ï¸  Running in TEST MODE with 100 USDC
2025-11-04 05:09:55,732 - __main__ - WARNING -    For production, approve at least 1,000 USDC
2025-11-04 05:09:55,732 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 05:09:55,733 - ml_predictor - INFO - Insufficient training data: 0 samples
2025-11-04 05:09:55,733 - __main__ - INFO - ML model updated successfully
2025-11-04 05:09:57,468 - market_scanner_v2 - INFO - âœ… Fetched 112 markets from API
2025-11-04 05:09:57,470 - market_scanner_v2 - INFO - âœ… Got 112 markets from API
2025-11-04 05:09:57,471 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 108/112 markets passed
2025-11-04 05:09:57,471 - market_scanner_v2 - INFO -    - 4 rejected: competition > 2
2025-11-04 05:09:57,471 - market_scanner_v2 - INFO - âœ… Found 108 qualifying markets (from 112 total)
2025-11-04 05:09:57,473 - market_selector - INFO - Selected 3 markets from 108 candidates
2025-11-04 05:09:57,750 - order_manager - INFO - Prepared order for market 663837 with spread 0.0120
2025-11-04 05:09:57,751 - order_manager - INFO - Added order to pending queue: 663837
2025-11-04 05:09:57,751 - __main__ - INFO - Added market 663837 to pending orders
2025-11-04 05:09:58,041 - order_manager - INFO - Prepared order for market 663831 with spread 0.0120
2025-11-04 05:09:58,041 - order_manager - INFO - Added order to pending queue: 663831
2025-11-04 05:09:58,041 - __main__ - INFO - Added market 663831 to pending orders
2025-11-04 05:09:58,892 - order_manager - INFO - Prepared order for market 663830 with spread 0.0120
2025-11-04 05:09:58,893 - order_manager - INFO - Added order to pending queue: 663830
2025-11-04 05:09:58,893 - __main__ - INFO - Added market 663830 to pending orders
2025-11-04 05:09:58,896 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:09:59,496 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:09:59,497 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:00,301 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:00,302 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:00,995 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:04,416 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 05:10:05,171 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:05,330 - market_scanner_v2 - INFO - âœ… Fetched 112 markets from API
2025-11-04 05:10:05,333 - market_scanner_v2 - INFO - âœ… Got 112 markets from API
2025-11-04 05:10:05,334 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 108/112 markets passed
2025-11-04 05:10:05,334 - market_scanner_v2 - INFO -    - 4 rejected: competition > 2
2025-11-04 05:10:05,334 - market_scanner_v2 - INFO - âœ… Found 108 qualifying markets (from 112 total)
2025-11-04 05:10:05,336 - market_selector - INFO - Selected 7 markets from 108 candidates
2025-11-04 05:10:05,639 - order_manager - INFO - Prepared order for market 663864 with spread 0.0120
2025-11-04 05:10:05,640 - order_manager - INFO - Added order to pending queue: 663864
2025-11-04 05:10:05,640 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 05:10:05,951 - order_manager - INFO - Prepared order for market 663860 with spread 0.0120
2025-11-04 05:10:05,952 - order_manager - INFO - Added order to pending queue: 663860
2025-11-04 05:10:05,953 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 05:10:06,227 - order_manager - INFO - Prepared order for market 663862 with spread 0.0132
2025-11-04 05:10:06,228 - order_manager - INFO - Added order to pending queue: 663862
2025-11-04 05:10:06,228 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 05:10:06,521 - order_manager - INFO - Prepared order for market 663911 with spread 0.0132
2025-11-04 05:10:06,521 - order_manager - INFO - Added order to pending queue: 663911
2025-11-04 05:10:06,521 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 05:10:06,806 - order_manager - INFO - Prepared order for market 663891 with spread 0.0120
2025-11-04 05:10:06,807 - order_manager - INFO - Added order to pending queue: 663891
2025-11-04 05:10:06,807 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 05:10:07,104 - order_manager - INFO - Prepared order for market 663908 with spread 0.0132
2025-11-04 05:10:07,105 - order_manager - INFO - Added order to pending queue: 663908
2025-11-04 05:10:07,105 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 05:10:07,412 - order_manager - INFO - Prepared order for market 663895 with spread 0.0120
2025-11-04 05:10:07,413 - order_manager - INFO - Added order to pending queue: 663895
2025-11-04 05:10:07,413 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 05:10:07,414 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:07,415 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:07,952 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:07,953 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:09,380 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:12,662 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:13,055 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 05:10:13,999 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:14,001 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:14,567 - market_scanner_v2 - INFO - âœ… Fetched 112 markets from API
2025-11-04 05:10:14,569 - market_scanner_v2 - INFO - âœ… Got 112 markets from API
2025-11-04 05:10:14,570 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 108/112 markets passed
2025-11-04 05:10:14,570 - market_scanner_v2 - INFO -    - 4 rejected: competition > 2
2025-11-04 05:10:14,570 - market_scanner_v2 - INFO - âœ… Found 108 qualifying markets (from 112 total)
2025-11-04 05:10:14,572 - market_selector - INFO - Selected 7 markets from 108 candidates
2025-11-04 05:10:14,847 - order_manager - INFO - Prepared order for market 663864 with spread 0.0120
2025-11-04 05:10:14,848 - order_manager - INFO - Added order to pending queue: 663864
2025-11-04 05:10:14,848 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 05:10:15,137 - order_manager - INFO - Prepared order for market 663860 with spread 0.0120
2025-11-04 05:10:15,137 - order_manager - INFO - Added order to pending queue: 663860
2025-11-04 05:10:15,137 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 05:10:15,448 - order_manager - INFO - Prepared order for market 663862 with spread 0.0132
2025-11-04 05:10:15,449 - order_manager - INFO - Added order to pending queue: 663862
2025-11-04 05:10:15,449 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 05:10:15,757 - order_manager - INFO - Prepared order for market 663911 with spread 0.0132
2025-11-04 05:10:15,758 - order_manager - INFO - Added order to pending queue: 663911
2025-11-04 05:10:15,759 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 05:10:16,036 - order_manager - INFO - Prepared order for market 663891 with spread 0.0120
2025-11-04 05:10:16,036 - order_manager - INFO - Added order to pending queue: 663891
2025-11-04 05:10:16,037 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 05:10:16,346 - order_manager - INFO - Prepared order for market 663908 with spread 0.0132
2025-11-04 05:10:16,346 - order_manager - INFO - Added order to pending queue: 663908
2025-11-04 05:10:16,347 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 05:10:16,628 - order_manager - INFO - Prepared order for market 663895 with spread 0.0120
2025-11-04 05:10:16,629 - order_manager - INFO - Added order to pending queue: 663895
2025-11-04 05:10:16,630 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 05:10:16,630 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:16,631 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:17,762 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:17,763 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:18,550 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:18,552 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:19,774 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:19,775 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:21,108 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:21,110 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:21,188 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 05:10:22,522 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:22,523 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:22,551 - market_scanner_v2 - INFO - âœ… Fetched 112 markets from API
2025-11-04 05:10:22,554 - market_scanner_v2 - INFO - âœ… Got 112 markets from API
2025-11-04 05:10:22,555 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 108/112 markets passed
2025-11-04 05:10:22,555 - market_scanner_v2 - INFO -    - 4 rejected: competition > 2
2025-11-04 05:10:22,555 - market_scanner_v2 - INFO - âœ… Found 108 qualifying markets (from 112 total)
2025-11-04 05:10:22,556 - market_selector - INFO - Selected 7 markets from 108 candidates
2025-11-04 05:10:23,031 - order_manager - INFO - Prepared order for market 663864 with spread 0.0120
2025-11-04 05:10:23,032 - order_manager - INFO - Added order to pending queue: 663864
2025-11-04 05:10:23,032 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 05:10:23,331 - order_manager - INFO - Prepared order for market 663860 with spread 0.0120
2025-11-04 05:10:23,331 - order_manager - INFO - Added order to pending queue: 663860
2025-11-04 05:10:23,332 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 05:10:23,673 - order_manager - INFO - Prepared order for market 663862 with spread 0.0132
2025-11-04 05:10:23,674 - order_manager - INFO - Added order to pending queue: 663862
2025-11-04 05:10:23,674 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 05:10:23,956 - order_manager - INFO - Prepared order for market 663911 with spread 0.0132
2025-11-04 05:10:23,957 - order_manager - INFO - Added order to pending queue: 663911
2025-11-04 05:10:23,957 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 05:10:24,279 - order_manager - INFO - Prepared order for market 663891 with spread 0.0120
2025-11-04 05:10:24,280 - order_manager - INFO - Added order to pending queue: 663891
2025-11-04 05:10:24,280 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 05:10:24,558 - order_manager - INFO - Prepared order for market 663908 with spread 0.0132
2025-11-04 05:10:24,559 - order_manager - INFO - Added order to pending queue: 663908
2025-11-04 05:10:24,559 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 05:10:24,824 - order_manager - INFO - Prepared order for market 663895 with spread 0.0120
2025-11-04 05:10:24,826 - order_manager - INFO - Added order to pending queue: 663895
2025-11-04 05:10:24,826 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 05:10:24,826 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:24,827 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:26,085 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:26,087 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:26,629 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:29,159 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 05:10:29,714 - market_scanner_v2 - INFO - âœ… Fetched 112 markets from API
2025-11-04 05:10:29,716 - market_scanner_v2 - INFO - âœ… Got 112 markets from API
2025-11-04 05:10:29,717 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 108/112 markets passed
2025-11-04 05:10:29,717 - market_scanner_v2 - INFO -    - 4 rejected: competition > 2
2025-11-04 05:10:29,717 - market_scanner_v2 - INFO - âœ… Found 108 qualifying markets (from 112 total)
2025-11-04 05:10:29,719 - market_selector - INFO - Selected 7 markets from 108 candidates
2025-11-04 05:10:29,997 - order_manager - INFO - Prepared order for market 663864 with spread 0.0120
2025-11-04 05:10:29,998 - order_manager - INFO - Added order to pending queue: 663864
2025-11-04 05:10:29,998 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 05:10:30,293 - order_manager - INFO - Prepared order for market 663860 with spread 0.0120
2025-11-04 05:10:30,294 - order_manager - INFO - Added order to pending queue: 663860
2025-11-04 05:10:30,294 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 05:10:30,593 - order_manager - INFO - Prepared order for market 663862 with spread 0.0132
2025-11-04 05:10:30,594 - order_manager - INFO - Added order to pending queue: 663862
2025-11-04 05:10:30,594 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 05:10:30,872 - order_manager - INFO - Prepared order for market 663911 with spread 0.0132
2025-11-04 05:10:30,873 - order_manager - INFO - Added order to pending queue: 663911
2025-11-04 05:10:30,873 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 05:10:31,167 - order_manager - INFO - Prepared order for market 663891 with spread 0.0120
2025-11-04 05:10:31,168 - order_manager - INFO - Added order to pending queue: 663891
2025-11-04 05:10:31,168 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 05:10:31,447 - order_manager - INFO - Prepared order for market 663908 with spread 0.0132
2025-11-04 05:10:31,447 - order_manager - INFO - Added order to pending queue: 663908
2025-11-04 05:10:31,447 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 05:10:31,736 - order_manager - INFO - Prepared order for market 663895 with spread 0.0120
2025-11-04 05:10:31,736 - order_manager - INFO - Added order to pending queue: 663895
2025-11-04 05:10:31,736 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 05:10:31,737 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:32,490 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:32,491 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:33,669 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:33,671 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:34,532 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:34,534 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:35,440 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:35,441 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:36,081 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 05:10:36,430 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:36,431 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:36,644 - market_scanner_v2 - INFO - âœ… Fetched 112 markets from API
2025-11-04 05:10:36,646 - market_scanner_v2 - INFO - âœ… Got 112 markets from API
2025-11-04 05:10:36,647 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 108/112 markets passed
2025-11-04 05:10:36,647 - market_scanner_v2 - INFO -    - 4 rejected: competition > 2
2025-11-04 05:10:36,647 - market_scanner_v2 - INFO - âœ… Found 108 qualifying markets (from 112 total)
2025-11-04 05:10:36,649 - market_selector - INFO - Selected 7 markets from 108 candidates
2025-11-04 05:10:36,926 - order_manager - INFO - Prepared order for market 663864 with spread 0.0120
2025-11-04 05:10:36,926 - order_manager - INFO - Added order to pending queue: 663864
2025-11-04 05:10:36,927 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 05:10:37,227 - order_manager - INFO - Prepared order for market 663860 with spread 0.0120
2025-11-04 05:10:37,229 - order_manager - INFO - Added order to pending queue: 663860
2025-11-04 05:10:37,229 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 05:10:37,527 - order_manager - INFO - Prepared order for market 663862 with spread 0.0132
2025-11-04 05:10:37,528 - order_manager - INFO - Added order to pending queue: 663862
2025-11-04 05:10:37,528 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 05:10:37,811 - order_manager - INFO - Prepared order for market 663911 with spread 0.0132
2025-11-04 05:10:37,812 - order_manager - INFO - Added order to pending queue: 663911
2025-11-04 05:10:37,812 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 05:10:38,092 - order_manager - INFO - Prepared order for market 663891 with spread 0.0120
2025-11-04 05:10:38,093 - order_manager - INFO - Added order to pending queue: 663891
2025-11-04 05:10:38,093 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 05:10:38,392 - order_manager - INFO - Prepared order for market 663908 with spread 0.0132
2025-11-04 05:10:38,394 - order_manager - INFO - Added order to pending queue: 663908
2025-11-04 05:10:38,394 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 05:10:38,687 - order_manager - INFO - Prepared order for market 663895 with spread 0.0120
2025-11-04 05:10:38,688 - order_manager - INFO - Added order to pending queue: 663895
2025-11-04 05:10:38,689 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 05:10:38,689 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:38,691 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:39,555 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:39,557 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:40,337 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:40,338 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:41,441 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:41,442 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:41,952 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:41,953 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:42,570 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:42,571 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:43,306 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:43,307 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:43,717 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 05:10:44,299 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:44,301 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:44,427 - market_scanner_v2 - INFO - âœ… Fetched 112 markets from API
2025-11-04 05:10:44,431 - market_scanner_v2 - INFO - âœ… Got 112 markets from API
2025-11-04 05:10:44,432 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 108/112 markets passed
2025-11-04 05:10:44,432 - market_scanner_v2 - INFO -    - 4 rejected: competition > 2
2025-11-04 05:10:44,432 - market_scanner_v2 - INFO - âœ… Found 108 qualifying markets (from 112 total)
2025-11-04 05:10:44,435 - market_selector - INFO - Selected 7 markets from 108 candidates
2025-11-04 05:10:44,733 - order_manager - INFO - Prepared order for market 663864 with spread 0.0120
2025-11-04 05:10:44,733 - order_manager - INFO - Added order to pending queue: 663864
2025-11-04 05:10:44,733 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 05:10:45,010 - order_manager - INFO - Prepared order for market 663860 with spread 0.0120
2025-11-04 05:10:45,011 - order_manager - INFO - Added order to pending queue: 663860
2025-11-04 05:10:45,012 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 05:10:45,302 - order_manager - INFO - Prepared order for market 663862 with spread 0.0132
2025-11-04 05:10:45,302 - order_manager - INFO - Added order to pending queue: 663862
2025-11-04 05:10:45,302 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 05:10:45,604 - order_manager - INFO - Prepared order for market 663911 with spread 0.0132
2025-11-04 05:10:45,605 - order_manager - INFO - Added order to pending queue: 663911
2025-11-04 05:10:45,606 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 05:10:45,887 - order_manager - INFO - Prepared order for market 663891 with spread 0.0120
2025-11-04 05:10:45,888 - order_manager - INFO - Added order to pending queue: 663891
2025-11-04 05:10:45,888 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 05:10:46,192 - order_manager - INFO - Prepared order for market 663908 with spread 0.0132
2025-11-04 05:10:46,193 - order_manager - INFO - Added order to pending queue: 663908
2025-11-04 05:10:46,193 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 05:10:46,518 - order_manager - INFO - Prepared order for market 663895 with spread 0.0120
2025-11-04 05:10:46,519 - order_manager - INFO - Added order to pending queue: 663895
2025-11-04 05:10:46,519 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 05:10:46,520 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:46,521 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:47,795 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:47,796 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:48,957 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:48,958 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:49,736 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:49,737 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:50,318 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:50,319 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:50,737 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 05:10:50,983 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:50,984 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:51,453 - market_scanner_v2 - INFO - âœ… Fetched 112 markets from API
2025-11-04 05:10:51,455 - market_scanner_v2 - INFO - âœ… Got 112 markets from API
2025-11-04 05:10:51,456 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 108/112 markets passed
2025-11-04 05:10:51,456 - market_scanner_v2 - INFO -    - 4 rejected: competition > 2
2025-11-04 05:10:51,456 - market_scanner_v2 - INFO - âœ… Found 108 qualifying markets (from 112 total)
2025-11-04 05:10:51,458 - market_selector - INFO - Selected 7 markets from 108 candidates
2025-11-04 05:10:51,743 - order_manager - INFO - Prepared order for market 663864 with spread 0.0120
2025-11-04 05:10:51,744 - order_manager - INFO - Added order to pending queue: 663864
2025-11-04 05:10:51,744 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 05:10:52,032 - order_manager - INFO - Prepared order for market 663860 with spread 0.0120
2025-11-04 05:10:52,033 - order_manager - INFO - Added order to pending queue: 663860
2025-11-04 05:10:52,033 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 05:10:52,314 - order_manager - INFO - Prepared order for market 663862 with spread 0.0132
2025-11-04 05:10:52,316 - order_manager - INFO - Added order to pending queue: 663862
2025-11-04 05:10:52,316 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 05:10:52,630 - order_manager - INFO - Prepared order for market 663911 with spread 0.0132
2025-11-04 05:10:52,631 - order_manager - INFO - Added order to pending queue: 663911
2025-11-04 05:10:52,631 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 05:10:52,910 - order_manager - INFO - Prepared order for market 663891 with spread 0.0120
2025-11-04 05:10:52,910 - order_manager - INFO - Added order to pending queue: 663891
2025-11-04 05:10:52,911 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 05:10:53,197 - order_manager - INFO - Prepared order for market 663908 with spread 0.0132
2025-11-04 05:10:53,197 - order_manager - INFO - Added order to pending queue: 663908
2025-11-04 05:10:53,198 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 05:10:53,486 - order_manager - INFO - Prepared order for market 663895 with spread 0.0120
2025-11-04 05:10:53,487 - order_manager - INFO - Added order to pending queue: 663895
2025-11-04 05:10:53,487 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 05:10:53,487 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:53,488 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:54,328 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:54,329 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:55,708 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:55,709 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:56,247 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:56,248 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:57,331 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:57,332 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:58,742 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:58,743 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:59,317 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:59,318 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:59,410 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 05:10:59,975 - market_scanner_v2 - INFO - âœ… Fetched 112 markets from API
2025-11-04 05:10:59,976 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:59,977 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:10:59,979 - market_scanner_v2 - INFO - âœ… Got 112 markets from API
2025-11-04 05:10:59,980 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 108/112 markets passed
2025-11-04 05:10:59,980 - market_scanner_v2 - INFO -    - 4 rejected: competition > 2
2025-11-04 05:10:59,980 - market_scanner_v2 - INFO - âœ… Found 108 qualifying markets (from 112 total)
2025-11-04 05:10:59,982 - market_selector - INFO - Selected 7 markets from 108 candidates
2025-11-04 05:11:00,275 - order_manager - INFO - Prepared order for market 663864 with spread 0.0120
2025-11-04 05:11:00,275 - order_manager - INFO - Added order to pending queue: 663864
2025-11-04 05:11:00,275 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 05:11:00,581 - order_manager - INFO - Prepared order for market 663860 with spread 0.0120
2025-11-04 05:11:00,582 - order_manager - INFO - Added order to pending queue: 663860
2025-11-04 05:11:00,582 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 05:11:00,879 - order_manager - INFO - Prepared order for market 663862 with spread 0.0132
2025-11-04 05:11:00,880 - order_manager - INFO - Added order to pending queue: 663862
2025-11-04 05:11:00,880 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 05:11:01,170 - order_manager - INFO - Prepared order for market 663911 with spread 0.0132
2025-11-04 05:11:01,171 - order_manager - INFO - Added order to pending queue: 663911
2025-11-04 05:11:01,171 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 05:11:01,465 - order_manager - INFO - Prepared order for market 663891 with spread 0.0120
2025-11-04 05:11:01,470 - order_manager - INFO - Added order to pending queue: 663891
2025-11-04 05:11:01,471 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 05:11:01,770 - order_manager - INFO - Prepared order for market 663908 with spread 0.0132
2025-11-04 05:11:01,770 - order_manager - INFO - Added order to pending queue: 663908
2025-11-04 05:11:01,770 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 05:11:02,049 - order_manager - INFO - Prepared order for market 663895 with spread 0.0120
2025-11-04 05:11:02,050 - order_manager - INFO - Added order to pending queue: 663895
2025-11-04 05:11:02,051 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 05:11:02,051 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:11:02,052 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:11:02,835 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:11:02,836 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:11:03,341 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:11:03,343 - order_manager - ERROR - Error placing single order: 
2025-11-04 05:11:04,734 - order_manager - ERROR - Error placing single order: 
