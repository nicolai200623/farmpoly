2025-11-04 04:35:17,074 - __main__ - INFO - âœ… Using MarketScannerV2 (Playwright + Gamma API)
2025-11-04 04:35:22,275 - __main__ - INFO - âœ… Telegram alerts configured (Chat ID: -1003157421030)
2025-11-04 04:35:22,275 - __main__ - INFO - âœ… Webhook alerts configured
2025-11-04 04:35:22,275 - circuit_breaker - INFO - âœ… Circuit Breaker 'gamma_api' initialized (threshold=5, timeout=60s)
2025-11-04 04:35:22,275 - circuit_breaker - INFO - âœ… Circuit Breaker 'playwright_scraper' initialized (threshold=3, timeout=120s)
2025-11-04 04:35:22,275 - order_manager - INFO - CLOB client initialized successfully (read-only mode)
2025-11-04 04:35:22,284 - wallet_manager - INFO - Loading REAL wallets from .env
2025-11-04 04:35:22,291 - wallet_manager - INFO - âœ… Loaded wallet 1: 0x18F261DC...Ae4FfD96
2025-11-04 04:35:22,292 - wallet_manager - INFO - âœ… Successfully loaded 1 real wallets
2025-11-04 04:35:22,302 - ml_predictor - INFO - No pre-trained model found, using new model
2025-11-04 04:35:22,302 - monitoring_system - INFO - âœ… Monitoring System initialized
2025-11-04 04:35:22,302 - __main__ - INFO - âœ… Monitoring System enabled
2025-11-04 04:35:22,302 - __main__ - INFO - â­ï¸  Reward Manager disabled in config
2025-11-04 04:35:22,302 - __main__ - INFO - All modules initialized successfully
2025-11-04 04:35:22,302 - __main__ - INFO - ðŸš€ Starting Polymarket Trading Bot...
2025-11-04 04:35:23,052 - ml_predictor - INFO - Alert sent: ðŸš€ <b>Polymarket Bot Started</b>
â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”
â° Time: 2025-11-04 04:35:22
ðŸ’¼ Wallets: 1
ðŸ“Š Status: Running
â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”
Bot is now scanning markets and placing orders.
2025-11-04 04:35:23,053 - __main__ - INFO - âœ… Startup alert sent
2025-11-04 04:35:23,053 - __main__ - INFO - ðŸ” Checking USDC approval for wallets...
2025-11-04 04:35:23,223 - usdc_approver - INFO - âœ… Connected to Polygon RPC: https://polygon-mainnet.g.alchemy.com/v2/FQJnJWsEQ...
2025-11-04 04:35:23,223 - __main__ - INFO -    Checking wallet: 0x18F261DC...Ae4FfD96
2025-11-04 04:35:23,342 - __main__ - INFO -    Raw allowance: 100000000 (base units)
2025-11-04 04:35:23,342 - __main__ - INFO -    Allowance in USDC: 100.00 USDC
2025-11-04 04:35:23,342 - __main__ - INFO -    Required minimum: 100 USDC (test mode)
2025-11-04 04:35:23,342 - __main__ - INFO - âœ… USDC approval OK (100 USDC)
2025-11-04 04:35:23,343 - __main__ - WARNING -    âš ï¸  Running in TEST MODE with 100 USDC
2025-11-04 04:35:23,343 - __main__ - WARNING -    For production, approve at least 1,000 USDC
2025-11-04 04:35:23,343 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 04:35:23,344 - ml_predictor - INFO - Insufficient training data: 0 samples
2025-11-04 04:35:23,344 - __main__ - INFO - ML model updated successfully
2025-11-04 04:35:25,054 - market_scanner_v2 - INFO - âœ… Fetched 126 markets from API
2025-11-04 04:35:25,057 - market_scanner_v2 - INFO - âœ… Got 126 markets from API
2025-11-04 04:35:25,057 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 126/126 markets passed
2025-11-04 04:35:25,058 - market_scanner_v2 - INFO - âœ… Found 126 qualifying markets (from 126 total)
2025-11-04 04:35:25,059 - market_selector - INFO - Selected 3 markets from 126 candidates
2025-11-04 04:35:25,358 - order_manager - INFO - Prepared order for market 663822 with spread 0.0120
2025-11-04 04:35:25,359 - order_manager - INFO - Added order to pending queue: 663822
2025-11-04 04:35:25,359 - __main__ - INFO - Added market 663822 to pending orders
2025-11-04 04:35:25,634 - order_manager - INFO - Prepared order for market 663824 with spread 0.0120
2025-11-04 04:35:25,635 - order_manager - INFO - Added order to pending queue: 663824
2025-11-04 04:35:25,635 - __main__ - INFO - Added market 663824 to pending orders
2025-11-04 04:35:25,929 - order_manager - INFO - Prepared order for market 663840 with spread 0.0120
2025-11-04 04:35:25,930 - order_manager - INFO - Added order to pending queue: 663840
2025-11-04 04:35:25,930 - __main__ - INFO - Added market 663840 to pending orders
2025-11-04 04:35:28,651 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:35:29,682 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:35:29,683 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:35:30,783 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:35:30,784 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:35:31,501 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 04:35:31,772 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:35:32,248 - market_scanner_v2 - INFO - âœ… Fetched 126 markets from API
2025-11-04 04:35:32,250 - market_scanner_v2 - INFO - âœ… Got 126 markets from API
2025-11-04 04:35:32,251 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 126/126 markets passed
2025-11-04 04:35:32,251 - market_scanner_v2 - INFO - âœ… Found 126 qualifying markets (from 126 total)
2025-11-04 04:35:32,253 - market_selector - INFO - Selected 7 markets from 126 candidates
2025-11-04 04:35:32,532 - order_manager - INFO - Prepared order for market 663864 with spread 0.0120
2025-11-04 04:35:32,534 - order_manager - INFO - Added order to pending queue: 663864
2025-11-04 04:35:32,534 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 04:35:32,815 - order_manager - INFO - Prepared order for market 663860 with spread 0.0120
2025-11-04 04:35:32,816 - order_manager - INFO - Added order to pending queue: 663860
2025-11-04 04:35:32,816 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 04:35:33,112 - order_manager - INFO - Prepared order for market 663862 with spread 0.0132
2025-11-04 04:35:33,113 - order_manager - INFO - Added order to pending queue: 663862
2025-11-04 04:35:33,113 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 04:35:33,448 - order_manager - INFO - Prepared order for market 663911 with spread 0.0132
2025-11-04 04:35:33,449 - order_manager - INFO - Added order to pending queue: 663911
2025-11-04 04:35:33,449 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 04:35:33,723 - order_manager - INFO - Prepared order for market 663891 with spread 0.0120
2025-11-04 04:35:33,723 - order_manager - INFO - Added order to pending queue: 663891
2025-11-04 04:35:33,723 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 04:35:34,000 - order_manager - INFO - Prepared order for market 663908 with spread 0.0132
2025-11-04 04:35:34,001 - order_manager - INFO - Added order to pending queue: 663908
2025-11-04 04:35:34,001 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 04:35:34,279 - order_manager - INFO - Prepared order for market 663895 with spread 0.0120
2025-11-04 04:35:34,280 - order_manager - INFO - Added order to pending queue: 663895
2025-11-04 04:35:34,280 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 04:35:38,089 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:35:39,089 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 04:35:39,544 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:35:39,545 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:35:40,009 - market_scanner_v2 - INFO - âœ… Fetched 126 markets from API
2025-11-04 04:35:40,011 - market_scanner_v2 - INFO - âœ… Got 126 markets from API
2025-11-04 04:35:40,012 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 126/126 markets passed
2025-11-04 04:35:40,012 - market_scanner_v2 - INFO - âœ… Found 126 qualifying markets (from 126 total)
2025-11-04 04:35:40,014 - market_selector - INFO - Selected 7 markets from 126 candidates
2025-11-04 04:35:40,312 - order_manager - INFO - Prepared order for market 663864 with spread 0.0120
2025-11-04 04:35:40,313 - order_manager - INFO - Added order to pending queue: 663864
2025-11-04 04:35:40,313 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 04:35:40,609 - order_manager - INFO - Prepared order for market 663860 with spread 0.0120
2025-11-04 04:35:40,611 - order_manager - INFO - Added order to pending queue: 663860
2025-11-04 04:35:40,611 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 04:35:40,884 - order_manager - INFO - Prepared order for market 663862 with spread 0.0132
2025-11-04 04:35:40,885 - order_manager - INFO - Added order to pending queue: 663862
2025-11-04 04:35:40,885 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 04:35:41,181 - order_manager - INFO - Prepared order for market 663911 with spread 0.0132
2025-11-04 04:35:41,181 - order_manager - INFO - Added order to pending queue: 663911
2025-11-04 04:35:41,182 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 04:35:41,464 - order_manager - INFO - Prepared order for market 663891 with spread 0.0120
2025-11-04 04:35:41,465 - order_manager - INFO - Added order to pending queue: 663891
2025-11-04 04:35:41,465 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 04:35:41,766 - order_manager - INFO - Prepared order for market 663908 with spread 0.0132
2025-11-04 04:35:41,767 - order_manager - INFO - Added order to pending queue: 663908
2025-11-04 04:35:41,767 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 04:35:42,081 - order_manager - INFO - Prepared order for market 663895 with spread 0.0120
2025-11-04 04:35:42,082 - order_manager - INFO - Added order to pending queue: 663895
2025-11-04 04:35:42,082 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 04:35:42,083 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:35:42,083 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:35:43,056 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:35:43,058 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:35:43,832 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:35:43,839 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:35:44,461 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:35:44,462 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:35:45,387 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:35:45,388 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:35:46,470 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:35:46,471 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:35:47,566 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 04:35:47,707 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:35:47,708 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:35:48,353 - market_scanner_v2 - INFO - âœ… Fetched 126 markets from API
2025-11-04 04:35:48,357 - market_scanner_v2 - INFO - âœ… Got 126 markets from API
2025-11-04 04:35:48,358 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 126/126 markets passed
2025-11-04 04:35:48,358 - market_scanner_v2 - INFO - âœ… Found 126 qualifying markets (from 126 total)
2025-11-04 04:35:48,360 - market_selector - INFO - Selected 7 markets from 126 candidates
2025-11-04 04:35:48,841 - order_manager - INFO - Prepared order for market 663864 with spread 0.0120
2025-11-04 04:35:48,842 - order_manager - INFO - Added order to pending queue: 663864
2025-11-04 04:35:48,842 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 04:35:49,144 - order_manager - INFO - Prepared order for market 663860 with spread 0.0120
2025-11-04 04:35:49,145 - order_manager - INFO - Added order to pending queue: 663860
2025-11-04 04:35:49,145 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 04:35:49,453 - order_manager - INFO - Prepared order for market 663862 with spread 0.0132
2025-11-04 04:35:49,454 - order_manager - INFO - Added order to pending queue: 663862
2025-11-04 04:35:49,454 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 04:35:49,729 - order_manager - INFO - Prepared order for market 663911 with spread 0.0132
2025-11-04 04:35:49,730 - order_manager - INFO - Added order to pending queue: 663911
2025-11-04 04:35:49,730 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 04:35:50,023 - order_manager - INFO - Prepared order for market 663891 with spread 0.0120
2025-11-04 04:35:50,024 - order_manager - INFO - Added order to pending queue: 663891
2025-11-04 04:35:50,025 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 04:35:50,323 - order_manager - INFO - Prepared order for market 663908 with spread 0.0132
2025-11-04 04:35:50,324 - order_manager - INFO - Added order to pending queue: 663908
2025-11-04 04:35:50,324 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 04:35:50,618 - order_manager - INFO - Prepared order for market 663895 with spread 0.0120
2025-11-04 04:35:50,619 - order_manager - INFO - Added order to pending queue: 663895
2025-11-04 04:35:50,619 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 04:35:50,619 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:35:50,620 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:35:52,073 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:35:56,210 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:35:56,359 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 04:35:57,098 - market_scanner_v2 - INFO - âœ… Fetched 126 markets from API
2025-11-04 04:35:57,102 - market_scanner_v2 - INFO - âœ… Got 126 markets from API
2025-11-04 04:35:57,103 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 126/126 markets passed
2025-11-04 04:35:57,103 - market_scanner_v2 - INFO - âœ… Found 126 qualifying markets (from 126 total)
2025-11-04 04:35:57,106 - market_selector - INFO - Selected 7 markets from 126 candidates
2025-11-04 04:35:57,399 - order_manager - INFO - Prepared order for market 663864 with spread 0.0120
2025-11-04 04:35:57,400 - order_manager - INFO - Added order to pending queue: 663864
2025-11-04 04:35:57,400 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 04:35:57,681 - order_manager - INFO - Prepared order for market 663860 with spread 0.0120
2025-11-04 04:35:57,682 - order_manager - INFO - Added order to pending queue: 663860
2025-11-04 04:35:57,682 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 04:35:57,985 - order_manager - INFO - Prepared order for market 663862 with spread 0.0132
2025-11-04 04:35:57,986 - order_manager - INFO - Added order to pending queue: 663862
2025-11-04 04:35:57,986 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 04:35:58,296 - order_manager - INFO - Prepared order for market 663911 with spread 0.0132
2025-11-04 04:35:58,297 - order_manager - INFO - Added order to pending queue: 663911
2025-11-04 04:35:58,298 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 04:35:58,612 - order_manager - INFO - Prepared order for market 663891 with spread 0.0120
2025-11-04 04:35:58,614 - order_manager - INFO - Added order to pending queue: 663891
2025-11-04 04:35:58,614 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 04:35:58,890 - order_manager - INFO - Prepared order for market 663908 with spread 0.0132
2025-11-04 04:35:58,891 - order_manager - INFO - Added order to pending queue: 663908
2025-11-04 04:35:58,891 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 04:35:59,283 - order_manager - INFO - Prepared order for market 663895 with spread 0.0120
2025-11-04 04:35:59,284 - order_manager - INFO - Added order to pending queue: 663895
2025-11-04 04:35:59,284 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 04:35:59,284 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:35:59,286 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:00,614 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:00,615 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:01,142 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:01,143 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:02,333 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:02,334 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:03,795 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:03,796 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:04,193 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 04:36:04,939 - market_scanner_v2 - INFO - âœ… Fetched 126 markets from API
2025-11-04 04:36:04,941 - market_scanner_v2 - INFO - âœ… Got 126 markets from API
2025-11-04 04:36:04,942 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 126/126 markets passed
2025-11-04 04:36:04,943 - market_scanner_v2 - INFO - âœ… Found 126 qualifying markets (from 126 total)
2025-11-04 04:36:04,945 - market_selector - INFO - Selected 7 markets from 126 candidates
2025-11-04 04:36:05,221 - order_manager - INFO - Prepared order for market 663864 with spread 0.0120
2025-11-04 04:36:05,221 - order_manager - INFO - Added order to pending queue: 663864
2025-11-04 04:36:05,221 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 04:36:05,516 - order_manager - INFO - Prepared order for market 663860 with spread 0.0120
2025-11-04 04:36:05,517 - order_manager - INFO - Added order to pending queue: 663860
2025-11-04 04:36:05,517 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 04:36:05,798 - order_manager - INFO - Prepared order for market 663862 with spread 0.0132
2025-11-04 04:36:05,799 - order_manager - INFO - Added order to pending queue: 663862
2025-11-04 04:36:05,799 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 04:36:06,440 - order_manager - INFO - Prepared order for market 663911 with spread 0.0132
2025-11-04 04:36:06,442 - order_manager - INFO - Added order to pending queue: 663911
2025-11-04 04:36:06,442 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 04:36:06,727 - order_manager - INFO - Prepared order for market 663891 with spread 0.0120
2025-11-04 04:36:06,728 - order_manager - INFO - Added order to pending queue: 663891
2025-11-04 04:36:06,728 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 04:36:07,031 - order_manager - INFO - Prepared order for market 663908 with spread 0.0132
2025-11-04 04:36:07,032 - order_manager - INFO - Added order to pending queue: 663908
2025-11-04 04:36:07,033 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 04:36:07,308 - order_manager - INFO - Prepared order for market 663895 with spread 0.0120
2025-11-04 04:36:07,309 - order_manager - INFO - Added order to pending queue: 663895
2025-11-04 04:36:07,309 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 04:36:07,314 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:07,320 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:08,347 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:08,349 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:09,821 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:09,822 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:10,373 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:10,374 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:11,794 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:11,795 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:12,360 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 04:36:12,767 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:12,768 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:13,108 - market_scanner_v2 - INFO - âœ… Fetched 126 markets from API
2025-11-04 04:36:13,111 - market_scanner_v2 - INFO - âœ… Got 126 markets from API
2025-11-04 04:36:13,112 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 126/126 markets passed
2025-11-04 04:36:13,112 - market_scanner_v2 - INFO - âœ… Found 126 qualifying markets (from 126 total)
2025-11-04 04:36:13,114 - market_selector - INFO - Selected 7 markets from 126 candidates
2025-11-04 04:36:13,403 - order_manager - INFO - Prepared order for market 663864 with spread 0.0120
2025-11-04 04:36:13,403 - order_manager - INFO - Added order to pending queue: 663864
2025-11-04 04:36:13,403 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 04:36:13,689 - order_manager - INFO - Prepared order for market 663860 with spread 0.0120
2025-11-04 04:36:13,690 - order_manager - INFO - Added order to pending queue: 663860
2025-11-04 04:36:13,690 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 04:36:13,994 - order_manager - INFO - Prepared order for market 663862 with spread 0.0132
2025-11-04 04:36:13,994 - order_manager - INFO - Added order to pending queue: 663862
2025-11-04 04:36:13,994 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 04:36:14,269 - order_manager - INFO - Prepared order for market 663911 with spread 0.0132
2025-11-04 04:36:14,270 - order_manager - INFO - Added order to pending queue: 663911
2025-11-04 04:36:14,270 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 04:36:14,579 - order_manager - INFO - Prepared order for market 663891 with spread 0.0120
2025-11-04 04:36:14,580 - order_manager - INFO - Added order to pending queue: 663891
2025-11-04 04:36:14,580 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 04:36:14,867 - order_manager - INFO - Prepared order for market 663908 with spread 0.0132
2025-11-04 04:36:14,868 - order_manager - INFO - Added order to pending queue: 663908
2025-11-04 04:36:14,868 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 04:36:15,157 - order_manager - INFO - Prepared order for market 663895 with spread 0.0120
2025-11-04 04:36:15,158 - order_manager - INFO - Added order to pending queue: 663895
2025-11-04 04:36:15,158 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 04:36:15,158 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:15,159 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:16,127 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:16,128 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:16,773 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:16,774 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:18,274 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:18,276 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:19,048 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:19,049 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:20,260 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:20,261 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:20,900 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 04:36:21,450 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:21,451 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:21,624 - market_scanner_v2 - INFO - âœ… Fetched 126 markets from API
2025-11-04 04:36:21,627 - market_scanner_v2 - INFO - âœ… Got 126 markets from API
2025-11-04 04:36:21,628 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 126/126 markets passed
2025-11-04 04:36:21,629 - market_scanner_v2 - INFO - âœ… Found 126 qualifying markets (from 126 total)
2025-11-04 04:36:21,631 - market_selector - INFO - Selected 7 markets from 126 candidates
2025-11-04 04:36:21,909 - order_manager - INFO - Prepared order for market 663864 with spread 0.0120
2025-11-04 04:36:21,910 - order_manager - INFO - Added order to pending queue: 663864
2025-11-04 04:36:21,910 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 04:36:22,206 - order_manager - INFO - Prepared order for market 663860 with spread 0.0120
2025-11-04 04:36:22,208 - order_manager - INFO - Added order to pending queue: 663860
2025-11-04 04:36:22,208 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 04:36:22,508 - order_manager - INFO - Prepared order for market 663862 with spread 0.0132
2025-11-04 04:36:22,509 - order_manager - INFO - Added order to pending queue: 663862
2025-11-04 04:36:22,509 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 04:36:22,789 - order_manager - INFO - Prepared order for market 663911 with spread 0.0132
2025-11-04 04:36:22,789 - order_manager - INFO - Added order to pending queue: 663911
2025-11-04 04:36:22,790 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 04:36:23,070 - order_manager - INFO - Prepared order for market 663891 with spread 0.0120
2025-11-04 04:36:23,071 - order_manager - INFO - Added order to pending queue: 663891
2025-11-04 04:36:23,071 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 04:36:23,456 - order_manager - INFO - Prepared order for market 663908 with spread 0.0132
2025-11-04 04:36:23,457 - order_manager - INFO - Added order to pending queue: 663908
2025-11-04 04:36:23,457 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 04:36:23,735 - order_manager - INFO - Prepared order for market 663895 with spread 0.0120
2025-11-04 04:36:23,735 - order_manager - INFO - Added order to pending queue: 663895
2025-11-04 04:36:23,736 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 04:36:23,736 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:23,738 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:24,897 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:24,899 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:26,352 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:26,353 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:27,053 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:27,054 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:28,281 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:28,282 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:29,135 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 04:36:29,697 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:29,875 - market_scanner_v2 - INFO - âœ… Fetched 126 markets from API
2025-11-04 04:36:29,878 - market_scanner_v2 - INFO - âœ… Got 126 markets from API
2025-11-04 04:36:29,879 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 126/126 markets passed
2025-11-04 04:36:29,879 - market_scanner_v2 - INFO - âœ… Found 126 qualifying markets (from 126 total)
2025-11-04 04:36:29,881 - market_selector - INFO - Selected 7 markets from 126 candidates
2025-11-04 04:36:30,168 - order_manager - INFO - Prepared order for market 663864 with spread 0.0120
2025-11-04 04:36:30,168 - order_manager - INFO - Added order to pending queue: 663864
2025-11-04 04:36:30,168 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 04:36:30,456 - order_manager - INFO - Prepared order for market 663860 with spread 0.0120
2025-11-04 04:36:30,458 - order_manager - INFO - Added order to pending queue: 663860
2025-11-04 04:36:30,458 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 04:36:30,759 - order_manager - INFO - Prepared order for market 663862 with spread 0.0132
2025-11-04 04:36:30,760 - order_manager - INFO - Added order to pending queue: 663862
2025-11-04 04:36:30,760 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 04:36:31,189 - order_manager - INFO - Prepared order for market 663911 with spread 0.0132
2025-11-04 04:36:31,190 - order_manager - INFO - Added order to pending queue: 663911
2025-11-04 04:36:31,191 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 04:36:31,492 - order_manager - INFO - Prepared order for market 663891 with spread 0.0120
2025-11-04 04:36:31,493 - order_manager - INFO - Added order to pending queue: 663891
2025-11-04 04:36:31,493 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 04:36:31,777 - order_manager - INFO - Prepared order for market 663908 with spread 0.0132
2025-11-04 04:36:31,778 - order_manager - INFO - Added order to pending queue: 663908
2025-11-04 04:36:31,779 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 04:36:32,070 - order_manager - INFO - Prepared order for market 663895 with spread 0.0120
2025-11-04 04:36:32,071 - order_manager - INFO - Added order to pending queue: 663895
2025-11-04 04:36:32,071 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 04:36:33,676 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:34,473 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:34,474 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:35,886 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:35,887 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:36,924 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 04:36:37,352 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:37,354 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:37,634 - market_scanner_v2 - INFO - âœ… Fetched 126 markets from API
2025-11-04 04:36:37,636 - market_scanner_v2 - INFO - âœ… Got 126 markets from API
2025-11-04 04:36:37,637 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 126/126 markets passed
2025-11-04 04:36:37,637 - market_scanner_v2 - INFO - âœ… Found 126 qualifying markets (from 126 total)
2025-11-04 04:36:37,639 - market_selector - INFO - Selected 7 markets from 126 candidates
2025-11-04 04:36:37,923 - order_manager - INFO - Prepared order for market 663864 with spread 0.0120
2025-11-04 04:36:37,924 - order_manager - INFO - Added order to pending queue: 663864
2025-11-04 04:36:37,924 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 04:36:38,229 - order_manager - INFO - Prepared order for market 663860 with spread 0.0120
2025-11-04 04:36:38,230 - order_manager - INFO - Added order to pending queue: 663860
2025-11-04 04:36:38,230 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 04:36:38,513 - order_manager - INFO - Prepared order for market 663862 with spread 0.0132
2025-11-04 04:36:38,514 - order_manager - INFO - Added order to pending queue: 663862
2025-11-04 04:36:38,514 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 04:36:38,810 - order_manager - INFO - Prepared order for market 663911 with spread 0.0132
2025-11-04 04:36:38,811 - order_manager - INFO - Added order to pending queue: 663911
2025-11-04 04:36:38,811 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 04:36:39,097 - order_manager - INFO - Prepared order for market 663891 with spread 0.0120
2025-11-04 04:36:39,098 - order_manager - INFO - Added order to pending queue: 663891
2025-11-04 04:36:39,098 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 04:36:39,380 - order_manager - INFO - Prepared order for market 663908 with spread 0.0132
2025-11-04 04:36:39,381 - order_manager - INFO - Added order to pending queue: 663908
2025-11-04 04:36:39,381 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 04:36:39,693 - order_manager - INFO - Prepared order for market 663895 with spread 0.0120
2025-11-04 04:36:39,694 - order_manager - INFO - Added order to pending queue: 663895
2025-11-04 04:36:39,694 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 04:36:39,695 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:39,696 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:40,734 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:40,735 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:41,705 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:41,706 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:42,993 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:42,994 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:44,260 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:44,262 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:44,488 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 04:36:45,222 - market_scanner_v2 - INFO - âœ… Fetched 126 markets from API
2025-11-04 04:36:45,224 - market_scanner_v2 - INFO - âœ… Got 126 markets from API
2025-11-04 04:36:45,225 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 126/126 markets passed
2025-11-04 04:36:45,226 - market_scanner_v2 - INFO - âœ… Found 126 qualifying markets (from 126 total)
2025-11-04 04:36:45,227 - market_selector - INFO - Selected 7 markets from 126 candidates
2025-11-04 04:36:45,514 - order_manager - INFO - Prepared order for market 663864 with spread 0.0120
2025-11-04 04:36:45,514 - order_manager - INFO - Added order to pending queue: 663864
2025-11-04 04:36:45,514 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 04:36:45,797 - order_manager - INFO - Prepared order for market 663860 with spread 0.0120
2025-11-04 04:36:45,798 - order_manager - INFO - Added order to pending queue: 663860
2025-11-04 04:36:45,798 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 04:36:46,099 - order_manager - INFO - Prepared order for market 663862 with spread 0.0132
2025-11-04 04:36:46,100 - order_manager - INFO - Added order to pending queue: 663862
2025-11-04 04:36:46,100 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 04:36:46,388 - order_manager - INFO - Prepared order for market 663911 with spread 0.0132
2025-11-04 04:36:46,388 - order_manager - INFO - Added order to pending queue: 663911
2025-11-04 04:36:46,388 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 04:36:46,693 - order_manager - INFO - Prepared order for market 663891 with spread 0.0120
2025-11-04 04:36:46,696 - order_manager - INFO - Added order to pending queue: 663891
2025-11-04 04:36:46,696 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 04:36:46,991 - order_manager - INFO - Prepared order for market 663908 with spread 0.0132
2025-11-04 04:36:46,992 - order_manager - INFO - Added order to pending queue: 663908
2025-11-04 04:36:46,992 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 04:36:47,270 - order_manager - INFO - Prepared order for market 663895 with spread 0.0120
2025-11-04 04:36:47,270 - order_manager - INFO - Added order to pending queue: 663895
2025-11-04 04:36:47,271 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 04:36:47,271 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:47,272 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:48,227 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:48,228 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:49,597 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:49,598 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:51,078 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:51,079 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:51,610 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 04:36:51,951 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:51,952 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:52,331 - market_scanner_v2 - INFO - âœ… Fetched 126 markets from API
2025-11-04 04:36:52,334 - market_scanner_v2 - INFO - âœ… Got 126 markets from API
2025-11-04 04:36:52,335 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 126/126 markets passed
2025-11-04 04:36:52,335 - market_scanner_v2 - INFO - âœ… Found 126 qualifying markets (from 126 total)
2025-11-04 04:36:52,338 - market_selector - INFO - Selected 7 markets from 126 candidates
2025-11-04 04:36:52,639 - order_manager - INFO - Prepared order for market 663864 with spread 0.0120
2025-11-04 04:36:52,639 - order_manager - INFO - Added order to pending queue: 663864
2025-11-04 04:36:52,639 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 04:36:52,906 - order_manager - INFO - Prepared order for market 663860 with spread 0.0120
2025-11-04 04:36:52,907 - order_manager - INFO - Added order to pending queue: 663860
2025-11-04 04:36:52,907 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 04:36:53,187 - order_manager - INFO - Prepared order for market 663862 with spread 0.0132
2025-11-04 04:36:53,188 - order_manager - INFO - Added order to pending queue: 663862
2025-11-04 04:36:53,188 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 04:36:53,471 - order_manager - INFO - Prepared order for market 663911 with spread 0.0132
2025-11-04 04:36:53,472 - order_manager - INFO - Added order to pending queue: 663911
2025-11-04 04:36:53,472 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 04:36:53,792 - order_manager - INFO - Prepared order for market 663891 with spread 0.0120
2025-11-04 04:36:53,793 - order_manager - INFO - Added order to pending queue: 663891
2025-11-04 04:36:53,793 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 04:36:54,101 - order_manager - INFO - Prepared order for market 663908 with spread 0.0132
2025-11-04 04:36:54,101 - order_manager - INFO - Added order to pending queue: 663908
2025-11-04 04:36:54,101 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 04:36:54,368 - order_manager - INFO - Prepared order for market 663895 with spread 0.0120
2025-11-04 04:36:54,369 - order_manager - INFO - Added order to pending queue: 663895
2025-11-04 04:36:54,370 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 04:36:54,370 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:54,371 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:55,839 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:55,840 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:57,354 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:57,355 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:57,992 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:57,993 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:58,707 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:58,708 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:58,879 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 04:36:59,492 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:59,493 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:36:59,636 - market_scanner_v2 - INFO - âœ… Fetched 126 markets from API
2025-11-04 04:36:59,638 - market_scanner_v2 - INFO - âœ… Got 126 markets from API
2025-11-04 04:36:59,639 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 126/126 markets passed
2025-11-04 04:36:59,640 - market_scanner_v2 - INFO - âœ… Found 126 qualifying markets (from 126 total)
2025-11-04 04:36:59,642 - market_selector - INFO - Selected 7 markets from 126 candidates
2025-11-04 04:36:59,938 - order_manager - INFO - Prepared order for market 663864 with spread 0.0120
2025-11-04 04:36:59,939 - order_manager - INFO - Added order to pending queue: 663864
2025-11-04 04:36:59,939 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 04:37:00,221 - order_manager - INFO - Prepared order for market 663860 with spread 0.0120
2025-11-04 04:37:00,222 - order_manager - INFO - Added order to pending queue: 663860
2025-11-04 04:37:00,222 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 04:37:00,514 - order_manager - INFO - Prepared order for market 663862 with spread 0.0132
2025-11-04 04:37:00,515 - order_manager - INFO - Added order to pending queue: 663862
2025-11-04 04:37:00,515 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 04:37:00,913 - order_manager - INFO - Prepared order for market 663911 with spread 0.0132
2025-11-04 04:37:00,913 - order_manager - INFO - Added order to pending queue: 663911
2025-11-04 04:37:00,914 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 04:37:01,193 - order_manager - INFO - Prepared order for market 663891 with spread 0.0120
2025-11-04 04:37:01,194 - order_manager - INFO - Added order to pending queue: 663891
2025-11-04 04:37:01,194 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 04:37:01,511 - order_manager - INFO - Prepared order for market 663908 with spread 0.0132
2025-11-04 04:37:01,513 - order_manager - INFO - Added order to pending queue: 663908
2025-11-04 04:37:01,513 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 04:37:01,844 - order_manager - INFO - Prepared order for market 663895 with spread 0.0120
2025-11-04 04:37:01,845 - order_manager - INFO - Added order to pending queue: 663895
2025-11-04 04:37:01,845 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 04:37:01,845 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:37:01,846 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:37:03,283 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:37:03,285 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:37:04,539 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:37:04,541 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:37:05,400 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:37:05,402 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:37:06,439 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 04:37:06,762 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:37:06,763 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:37:07,178 - market_scanner_v2 - INFO - âœ… Fetched 126 markets from API
2025-11-04 04:37:07,180 - market_scanner_v2 - INFO - âœ… Got 126 markets from API
2025-11-04 04:37:07,181 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 126/126 markets passed
2025-11-04 04:37:07,181 - market_scanner_v2 - INFO - âœ… Found 126 qualifying markets (from 126 total)
2025-11-04 04:37:07,183 - market_selector - INFO - Selected 7 markets from 126 candidates
2025-11-04 04:37:07,462 - order_manager - INFO - Prepared order for market 663864 with spread 0.0120
2025-11-04 04:37:07,462 - order_manager - INFO - Added order to pending queue: 663864
2025-11-04 04:37:07,462 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 04:37:07,752 - order_manager - INFO - Prepared order for market 663860 with spread 0.0120
2025-11-04 04:37:07,753 - order_manager - INFO - Added order to pending queue: 663860
2025-11-04 04:37:07,753 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 04:37:08,030 - order_manager - INFO - Prepared order for market 663862 with spread 0.0132
2025-11-04 04:37:08,031 - order_manager - INFO - Added order to pending queue: 663862
2025-11-04 04:37:08,031 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 04:37:08,332 - order_manager - INFO - Prepared order for market 663911 with spread 0.0132
2025-11-04 04:37:08,333 - order_manager - INFO - Added order to pending queue: 663911
2025-11-04 04:37:08,333 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 04:37:08,615 - order_manager - INFO - Prepared order for market 663891 with spread 0.0120
2025-11-04 04:37:08,616 - order_manager - INFO - Added order to pending queue: 663891
2025-11-04 04:37:08,616 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 04:37:08,900 - order_manager - INFO - Prepared order for market 663908 with spread 0.0132
2025-11-04 04:37:08,900 - order_manager - INFO - Added order to pending queue: 663908
2025-11-04 04:37:08,900 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 04:37:09,207 - order_manager - INFO - Prepared order for market 663895 with spread 0.0120
2025-11-04 04:37:09,208 - order_manager - INFO - Added order to pending queue: 663895
2025-11-04 04:37:09,208 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 04:37:09,208 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:37:09,209 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:37:10,432 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:37:10,433 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:37:11,289 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:37:11,291 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:37:12,609 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:37:12,610 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:37:13,256 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:37:13,257 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:37:13,325 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 04:37:14,052 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:37:14,054 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:37:14,077 - market_scanner_v2 - INFO - âœ… Fetched 126 markets from API
2025-11-04 04:37:14,079 - market_scanner_v2 - INFO - âœ… Got 126 markets from API
2025-11-04 04:37:14,080 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 126/126 markets passed
2025-11-04 04:37:14,080 - market_scanner_v2 - INFO - âœ… Found 126 qualifying markets (from 126 total)
2025-11-04 04:37:14,082 - market_selector - INFO - Selected 7 markets from 126 candidates
2025-11-04 04:37:14,457 - order_manager - INFO - Prepared order for market 663864 with spread 0.0120
2025-11-04 04:37:14,458 - order_manager - INFO - Added order to pending queue: 663864
2025-11-04 04:37:14,458 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 04:37:14,735 - order_manager - INFO - Prepared order for market 663860 with spread 0.0120
2025-11-04 04:37:14,736 - order_manager - INFO - Added order to pending queue: 663860
2025-11-04 04:37:14,736 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 04:37:15,018 - order_manager - INFO - Prepared order for market 663862 with spread 0.0132
2025-11-04 04:37:15,019 - order_manager - INFO - Added order to pending queue: 663862
2025-11-04 04:37:15,019 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 04:37:15,313 - order_manager - INFO - Prepared order for market 663911 with spread 0.0132
2025-11-04 04:37:15,314 - order_manager - INFO - Added order to pending queue: 663911
2025-11-04 04:37:15,314 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 04:37:15,599 - order_manager - INFO - Prepared order for market 663891 with spread 0.0120
2025-11-04 04:37:15,600 - order_manager - INFO - Added order to pending queue: 663891
2025-11-04 04:37:15,600 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 04:37:15,892 - order_manager - INFO - Prepared order for market 663908 with spread 0.0132
2025-11-04 04:37:15,893 - order_manager - INFO - Added order to pending queue: 663908
2025-11-04 04:37:15,893 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 04:37:16,318 - order_manager - INFO - Prepared order for market 663895 with spread 0.0120
2025-11-04 04:37:16,318 - order_manager - INFO - Added order to pending queue: 663895
2025-11-04 04:37:16,319 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 04:37:16,319 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:37:16,320 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:37:16,940 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:37:16,941 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:37:17,766 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:37:17,768 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:37:18,493 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:37:18,494 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:37:19,960 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:37:19,962 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:37:20,680 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:37:20,681 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:37:20,808 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 04:37:21,558 - market_scanner_v2 - INFO - âœ… Fetched 126 markets from API
2025-11-04 04:37:21,560 - market_scanner_v2 - INFO - âœ… Got 126 markets from API
2025-11-04 04:37:21,561 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 126/126 markets passed
2025-11-04 04:37:21,561 - market_scanner_v2 - INFO - âœ… Found 126 qualifying markets (from 126 total)
2025-11-04 04:37:21,563 - market_selector - INFO - Selected 7 markets from 126 candidates
2025-11-04 04:37:21,838 - order_manager - INFO - Prepared order for market 663864 with spread 0.0120
2025-11-04 04:37:21,838 - order_manager - INFO - Added order to pending queue: 663864
2025-11-04 04:37:21,838 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 04:37:22,105 - order_manager - INFO - Prepared order for market 663860 with spread 0.0120
2025-11-04 04:37:22,105 - order_manager - INFO - Added order to pending queue: 663860
2025-11-04 04:37:22,105 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 04:37:22,396 - order_manager - INFO - Prepared order for market 663862 with spread 0.0132
2025-11-04 04:37:22,396 - order_manager - INFO - Added order to pending queue: 663862
2025-11-04 04:37:22,396 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 04:37:22,654 - order_manager - INFO - Prepared order for market 663911 with spread 0.0132
2025-11-04 04:37:22,655 - order_manager - INFO - Added order to pending queue: 663911
2025-11-04 04:37:22,655 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 04:37:22,936 - order_manager - INFO - Prepared order for market 663891 with spread 0.0120
2025-11-04 04:37:22,936 - order_manager - INFO - Added order to pending queue: 663891
2025-11-04 04:37:22,936 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 04:37:23,209 - order_manager - INFO - Prepared order for market 663908 with spread 0.0132
2025-11-04 04:37:23,210 - order_manager - INFO - Added order to pending queue: 663908
2025-11-04 04:37:23,210 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 04:37:23,493 - order_manager - INFO - Prepared order for market 663895 with spread 0.0120
2025-11-04 04:37:23,495 - order_manager - INFO - Added order to pending queue: 663895
2025-11-04 04:37:23,495 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 04:37:23,495 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:37:23,496 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:37:24,285 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:37:24,286 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:37:25,400 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:37:25,401 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:37:26,578 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:37:26,579 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:37:28,356 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:37:28,357 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:37:28,358 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 04:37:29,064 - market_scanner_v2 - INFO - âœ… Fetched 126 markets from API
2025-11-04 04:37:29,066 - market_scanner_v2 - INFO - âœ… Got 126 markets from API
2025-11-04 04:37:29,067 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 126/126 markets passed
2025-11-04 04:37:29,067 - market_scanner_v2 - INFO - âœ… Found 126 qualifying markets (from 126 total)
2025-11-04 04:37:29,069 - market_selector - INFO - Selected 7 markets from 126 candidates
2025-11-04 04:37:29,340 - order_manager - INFO - Prepared order for market 663864 with spread 0.0120
2025-11-04 04:37:29,340 - order_manager - INFO - Added order to pending queue: 663864
2025-11-04 04:37:29,340 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 04:37:29,637 - order_manager - INFO - Prepared order for market 663860 with spread 0.0120
2025-11-04 04:37:29,638 - order_manager - INFO - Added order to pending queue: 663860
2025-11-04 04:37:29,638 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 04:37:29,906 - order_manager - INFO - Prepared order for market 663862 with spread 0.0132
2025-11-04 04:37:29,906 - order_manager - INFO - Added order to pending queue: 663862
2025-11-04 04:37:29,906 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 04:37:30,192 - order_manager - INFO - Prepared order for market 663911 with spread 0.0132
2025-11-04 04:37:30,193 - order_manager - INFO - Added order to pending queue: 663911
2025-11-04 04:37:30,193 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 04:37:30,475 - order_manager - INFO - Prepared order for market 663891 with spread 0.0120
2025-11-04 04:37:30,477 - order_manager - INFO - Added order to pending queue: 663891
2025-11-04 04:37:30,477 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 04:37:30,755 - order_manager - INFO - Prepared order for market 663908 with spread 0.0132
2025-11-04 04:37:30,756 - order_manager - INFO - Added order to pending queue: 663908
2025-11-04 04:37:30,756 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 04:37:31,032 - order_manager - INFO - Prepared order for market 663895 with spread 0.0120
2025-11-04 04:37:31,033 - order_manager - INFO - Added order to pending queue: 663895
2025-11-04 04:37:31,033 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 04:37:31,033 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:37:31,034 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:37:32,445 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:37:32,446 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:37:33,295 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:37:33,296 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:37:34,186 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:37:34,187 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:37:35,246 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 04:37:35,336 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:37:35,337 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:37:35,952 - market_scanner_v2 - INFO - âœ… Fetched 126 markets from API
2025-11-04 04:37:35,955 - market_scanner_v2 - INFO - âœ… Got 126 markets from API
2025-11-04 04:37:35,956 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 126/126 markets passed
2025-11-04 04:37:35,956 - market_scanner_v2 - INFO - âœ… Found 126 qualifying markets (from 126 total)
2025-11-04 04:37:35,958 - market_selector - INFO - Selected 7 markets from 126 candidates
2025-11-04 04:37:36,241 - order_manager - INFO - Prepared order for market 663864 with spread 0.0120
2025-11-04 04:37:36,241 - order_manager - INFO - Added order to pending queue: 663864
2025-11-04 04:37:36,241 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 04:37:36,566 - order_manager - INFO - Prepared order for market 663860 with spread 0.0120
2025-11-04 04:37:36,567 - order_manager - INFO - Added order to pending queue: 663860
2025-11-04 04:37:36,567 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 04:37:36,856 - order_manager - INFO - Prepared order for market 663862 with spread 0.0132
2025-11-04 04:37:36,857 - order_manager - INFO - Added order to pending queue: 663862
2025-11-04 04:37:36,857 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 04:37:37,144 - order_manager - INFO - Prepared order for market 663911 with spread 0.0132
2025-11-04 04:37:37,146 - order_manager - INFO - Added order to pending queue: 663911
2025-11-04 04:37:37,146 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 04:37:37,439 - order_manager - INFO - Prepared order for market 663891 with spread 0.0120
2025-11-04 04:37:37,440 - order_manager - INFO - Added order to pending queue: 663891
2025-11-04 04:37:37,440 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 04:37:37,761 - order_manager - INFO - Prepared order for market 663908 with spread 0.0132
2025-11-04 04:37:37,762 - order_manager - INFO - Added order to pending queue: 663908
2025-11-04 04:37:37,762 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 04:37:38,048 - order_manager - INFO - Prepared order for market 663895 with spread 0.0120
2025-11-04 04:37:38,053 - order_manager - INFO - Added order to pending queue: 663895
2025-11-04 04:37:38,054 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 04:37:38,054 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:37:38,055 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:37:39,126 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:37:39,127 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:37:39,938 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
2025-11-04 04:37:39,939 - order_manager - ERROR - Error placing single order: ClobClient.create_order() got an unexpected keyword argument 'token_id'
