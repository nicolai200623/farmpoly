2025-11-04 04:23:53,046 - __main__ - INFO - âœ… Using MarketScannerV2 (Playwright + Gamma API)
2025-11-04 04:24:00,138 - __main__ - INFO - âœ… Telegram alerts configured (Chat ID: -1003157421030)
2025-11-04 04:24:00,138 - __main__ - INFO - âœ… Webhook alerts configured
2025-11-04 04:24:00,139 - circuit_breaker - INFO - âœ… Circuit Breaker 'gamma_api' initialized (threshold=5, timeout=60s)
2025-11-04 04:24:00,139 - circuit_breaker - INFO - âœ… Circuit Breaker 'playwright_scraper' initialized (threshold=3, timeout=120s)
2025-11-04 04:24:00,139 - order_manager - INFO - CLOB client initialized successfully (read-only mode)
2025-11-04 04:24:00,152 - wallet_manager - INFO - Loading REAL wallets from .env
2025-11-04 04:24:00,162 - wallet_manager - INFO - âœ… Loaded wallet 1: 0x18F261DC...Ae4FfD96
2025-11-04 04:24:00,162 - wallet_manager - INFO - âœ… Successfully loaded 1 real wallets
2025-11-04 04:24:00,167 - ml_predictor - INFO - No pre-trained model found, using new model
2025-11-04 04:24:00,167 - monitoring_system - INFO - âœ… Monitoring System initialized
2025-11-04 04:24:00,167 - __main__ - INFO - âœ… Monitoring System enabled
2025-11-04 04:24:00,167 - __main__ - INFO - â­ï¸  Reward Manager disabled in config
2025-11-04 04:24:00,167 - __main__ - INFO - All modules initialized successfully
2025-11-04 04:24:00,167 - __main__ - INFO - ðŸš€ Starting Polymarket Trading Bot...
2025-11-04 04:24:00,935 - ml_predictor - INFO - Alert sent: ðŸš€ <b>Polymarket Bot Started</b>
â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”
â° Time: 2025-11-04 04:24:00
ðŸ’¼ Wallets: 1
ðŸ“Š Status: Running
â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”
Bot is now scanning markets and placing orders.
2025-11-04 04:24:00,935 - __main__ - INFO - âœ… Startup alert sent
2025-11-04 04:24:00,935 - __main__ - INFO - ðŸ” Checking USDC approval for wallets...
2025-11-04 04:24:01,098 - usdc_approver - INFO - âœ… Connected to Polygon RPC: https://polygon-mainnet.g.alchemy.com/v2/FQJnJWsEQ...
2025-11-04 04:24:01,098 - __main__ - INFO -    Checking wallet: 0x18F261DC...Ae4FfD96
2025-11-04 04:24:01,292 - __main__ - INFO -    Raw allowance: 100000000 (base units)
2025-11-04 04:24:01,293 - __main__ - INFO -    Allowance in USDC: 100.00 USDC
2025-11-04 04:24:01,293 - __main__ - INFO -    Required minimum: 100 USDC (test mode)
2025-11-04 04:24:01,293 - __main__ - INFO - âœ… USDC approval OK (100 USDC)
2025-11-04 04:24:01,293 - __main__ - WARNING -    âš ï¸  Running in TEST MODE with 100 USDC
2025-11-04 04:24:01,293 - __main__ - WARNING -    For production, approve at least 1,000 USDC
2025-11-04 04:24:01,293 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 04:24:01,294 - ml_predictor - INFO - Insufficient training data: 0 samples
2025-11-04 04:24:01,294 - __main__ - INFO - ML model updated successfully
2025-11-04 04:24:03,016 - market_scanner_v2 - INFO - âœ… Fetched 126 markets from API
2025-11-04 04:24:03,018 - market_scanner_v2 - INFO - âœ… Got 126 markets from API
2025-11-04 04:24:03,019 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 126/126 markets passed
2025-11-04 04:24:03,019 - market_scanner_v2 - INFO - âœ… Found 126 qualifying markets (from 126 total)
2025-11-04 04:24:03,021 - market_selector - INFO - Selected 3 markets from 126 candidates
2025-11-04 04:24:03,306 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:24:03,306 - order_manager - WARNING - Could not fetch data for market 663822
2025-11-04 04:24:03,307 - __main__ - INFO - Added market 663822 to pending orders
2025-11-04 04:24:03,628 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:24:03,629 - order_manager - WARNING - Could not fetch data for market 663840
2025-11-04 04:24:03,629 - __main__ - INFO - Added market 663840 to pending orders
2025-11-04 04:24:03,904 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:24:03,905 - order_manager - WARNING - Could not fetch data for market 663824
2025-11-04 04:24:03,905 - __main__ - INFO - Added market 663824 to pending orders
2025-11-04 04:24:08,883 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 04:24:09,660 - market_scanner_v2 - INFO - âœ… Fetched 126 markets from API
2025-11-04 04:24:09,663 - market_scanner_v2 - INFO - âœ… Got 126 markets from API
2025-11-04 04:24:09,664 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 126/126 markets passed
2025-11-04 04:24:09,664 - market_scanner_v2 - INFO - âœ… Found 126 qualifying markets (from 126 total)
2025-11-04 04:24:09,666 - market_selector - INFO - Selected 7 markets from 126 candidates
2025-11-04 04:24:09,972 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:24:09,972 - order_manager - WARNING - Could not fetch data for market 663864
2025-11-04 04:24:09,973 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 04:24:10,283 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:24:10,283 - order_manager - WARNING - Could not fetch data for market 663862
2025-11-04 04:24:10,283 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 04:24:10,573 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:24:10,574 - order_manager - WARNING - Could not fetch data for market 663860
2025-11-04 04:24:10,574 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 04:24:10,868 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:24:10,869 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 04:24:10,869 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 04:24:11,189 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:24:11,190 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 04:24:11,190 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 04:24:11,476 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:24:11,477 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 04:24:11,477 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 04:24:11,809 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:24:11,810 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 04:24:11,810 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 04:24:16,969 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 04:24:17,687 - market_scanner_v2 - INFO - âœ… Fetched 126 markets from API
2025-11-04 04:24:17,690 - market_scanner_v2 - INFO - âœ… Got 126 markets from API
2025-11-04 04:24:17,691 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 126/126 markets passed
2025-11-04 04:24:17,691 - market_scanner_v2 - INFO - âœ… Found 126 qualifying markets (from 126 total)
2025-11-04 04:24:17,693 - market_selector - INFO - Selected 7 markets from 126 candidates
2025-11-04 04:24:17,987 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:24:17,988 - order_manager - WARNING - Could not fetch data for market 663864
2025-11-04 04:24:17,988 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 04:24:18,271 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:24:18,272 - order_manager - WARNING - Could not fetch data for market 663862
2025-11-04 04:24:18,272 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 04:24:18,544 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:24:18,545 - order_manager - WARNING - Could not fetch data for market 663860
2025-11-04 04:24:18,545 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 04:24:18,841 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:24:18,842 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 04:24:18,842 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 04:24:19,144 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:24:19,145 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 04:24:19,145 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 04:24:19,419 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:24:19,421 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 04:24:19,421 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 04:24:19,712 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:24:19,712 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 04:24:19,712 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 04:24:24,883 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 04:24:25,287 - market_scanner_v2 - INFO - âœ… Fetched 126 markets from API
2025-11-04 04:24:25,289 - market_scanner_v2 - INFO - âœ… Got 126 markets from API
2025-11-04 04:24:25,290 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 126/126 markets passed
2025-11-04 04:24:25,290 - market_scanner_v2 - INFO - âœ… Found 126 qualifying markets (from 126 total)
2025-11-04 04:24:25,293 - market_selector - INFO - Selected 7 markets from 126 candidates
2025-11-04 04:24:25,579 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:24:25,580 - order_manager - WARNING - Could not fetch data for market 663864
2025-11-04 04:24:25,580 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 04:24:25,854 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:24:25,855 - order_manager - WARNING - Could not fetch data for market 663862
2025-11-04 04:24:25,855 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 04:24:26,137 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:24:26,138 - order_manager - WARNING - Could not fetch data for market 663860
2025-11-04 04:24:26,138 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 04:24:26,445 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:24:26,446 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 04:24:26,446 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 04:24:26,736 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:24:26,737 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 04:24:26,737 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 04:24:27,036 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:24:27,037 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 04:24:27,037 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 04:24:27,345 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:24:27,346 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 04:24:27,346 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 04:24:31,398 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 04:24:32,189 - market_scanner_v2 - INFO - âœ… Fetched 126 markets from API
2025-11-04 04:24:32,191 - market_scanner_v2 - INFO - âœ… Got 126 markets from API
2025-11-04 04:24:32,192 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 126/126 markets passed
2025-11-04 04:24:32,193 - market_scanner_v2 - INFO - âœ… Found 126 qualifying markets (from 126 total)
2025-11-04 04:24:32,195 - market_selector - INFO - Selected 7 markets from 126 candidates
2025-11-04 04:24:32,495 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:24:32,495 - order_manager - WARNING - Could not fetch data for market 663864
2025-11-04 04:24:32,495 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 04:24:32,795 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:24:32,796 - order_manager - WARNING - Could not fetch data for market 663862
2025-11-04 04:24:32,796 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 04:24:33,092 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:24:33,093 - order_manager - WARNING - Could not fetch data for market 663860
2025-11-04 04:24:33,093 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 04:24:33,384 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:24:33,385 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 04:24:33,385 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 04:24:33,660 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:24:33,661 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 04:24:33,661 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 04:24:33,964 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:24:33,965 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 04:24:33,965 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 04:24:34,267 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:24:34,267 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 04:24:34,267 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 04:24:40,048 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 04:24:40,764 - market_scanner_v2 - INFO - âœ… Fetched 126 markets from API
2025-11-04 04:24:40,767 - market_scanner_v2 - INFO - âœ… Got 126 markets from API
2025-11-04 04:24:40,768 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 126/126 markets passed
2025-11-04 04:24:40,768 - market_scanner_v2 - INFO - âœ… Found 126 qualifying markets (from 126 total)
2025-11-04 04:24:40,771 - market_selector - INFO - Selected 7 markets from 126 candidates
2025-11-04 04:24:41,065 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:24:41,066 - order_manager - WARNING - Could not fetch data for market 663864
2025-11-04 04:24:41,066 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 04:24:41,347 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:24:41,348 - order_manager - WARNING - Could not fetch data for market 663862
2025-11-04 04:24:41,348 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 04:24:41,647 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:24:41,648 - order_manager - WARNING - Could not fetch data for market 663860
2025-11-04 04:24:41,649 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 04:24:41,929 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:24:41,930 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 04:24:41,930 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 04:24:42,252 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:24:42,252 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 04:24:42,252 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 04:24:42,532 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:24:42,534 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 04:24:42,534 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 04:24:42,833 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:24:42,834 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 04:24:42,834 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 04:24:47,212 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 04:24:47,990 - market_scanner_v2 - INFO - âœ… Fetched 126 markets from API
2025-11-04 04:24:47,994 - market_scanner_v2 - INFO - âœ… Got 126 markets from API
2025-11-04 04:24:47,995 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 126/126 markets passed
2025-11-04 04:24:47,996 - market_scanner_v2 - INFO - âœ… Found 126 qualifying markets (from 126 total)
2025-11-04 04:24:47,998 - market_selector - INFO - Selected 7 markets from 126 candidates
2025-11-04 04:24:48,297 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:24:48,297 - order_manager - WARNING - Could not fetch data for market 663864
2025-11-04 04:24:48,297 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 04:24:48,595 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:24:48,596 - order_manager - WARNING - Could not fetch data for market 663862
2025-11-04 04:24:48,596 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 04:24:48,866 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:24:48,867 - order_manager - WARNING - Could not fetch data for market 663860
2025-11-04 04:24:48,867 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 04:24:49,140 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:24:49,140 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 04:24:49,140 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 04:24:49,433 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:24:49,433 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 04:24:49,433 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 04:24:49,718 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:24:49,719 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 04:24:49,719 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 04:24:50,018 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:24:50,018 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 04:24:50,019 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 04:24:54,057 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 04:24:54,774 - market_scanner_v2 - INFO - âœ… Fetched 126 markets from API
2025-11-04 04:24:54,776 - market_scanner_v2 - INFO - âœ… Got 126 markets from API
2025-11-04 04:24:54,778 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 126/126 markets passed
2025-11-04 04:24:54,778 - market_scanner_v2 - INFO - âœ… Found 126 qualifying markets (from 126 total)
2025-11-04 04:24:54,780 - market_selector - INFO - Selected 7 markets from 126 candidates
2025-11-04 04:24:55,056 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:24:55,056 - order_manager - WARNING - Could not fetch data for market 663864
2025-11-04 04:24:55,056 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 04:24:55,336 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:24:55,338 - order_manager - WARNING - Could not fetch data for market 663862
2025-11-04 04:24:55,338 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 04:24:55,659 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:24:55,660 - order_manager - WARNING - Could not fetch data for market 663860
2025-11-04 04:24:55,660 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 04:24:55,954 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:24:55,954 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 04:24:55,954 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 04:24:56,278 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:24:56,278 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 04:24:56,279 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 04:24:56,558 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:24:56,559 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 04:24:56,559 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 04:24:56,842 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:24:56,843 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 04:24:56,843 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 04:25:01,150 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 04:25:01,906 - market_scanner_v2 - INFO - âœ… Fetched 126 markets from API
2025-11-04 04:25:01,913 - market_scanner_v2 - INFO - âœ… Got 126 markets from API
2025-11-04 04:25:01,914 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 126/126 markets passed
2025-11-04 04:25:01,915 - market_scanner_v2 - INFO - âœ… Found 126 qualifying markets (from 126 total)
2025-11-04 04:25:01,917 - market_selector - INFO - Selected 7 markets from 126 candidates
2025-11-04 04:25:02,259 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:25:02,260 - order_manager - WARNING - Could not fetch data for market 663864
2025-11-04 04:25:02,260 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 04:25:02,605 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:25:02,607 - order_manager - WARNING - Could not fetch data for market 663862
2025-11-04 04:25:02,607 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 04:25:02,907 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:25:02,907 - order_manager - WARNING - Could not fetch data for market 663860
2025-11-04 04:25:02,907 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 04:25:03,225 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:25:03,226 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 04:25:03,226 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 04:25:03,527 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:25:03,528 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 04:25:03,529 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 04:25:03,826 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:25:03,827 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 04:25:03,827 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 04:25:04,110 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:25:04,111 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 04:25:04,111 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 04:25:09,535 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 04:25:10,389 - market_scanner_v2 - INFO - âœ… Fetched 126 markets from API
2025-11-04 04:25:10,391 - market_scanner_v2 - INFO - âœ… Got 126 markets from API
2025-11-04 04:25:10,392 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 126/126 markets passed
2025-11-04 04:25:10,393 - market_scanner_v2 - INFO - âœ… Found 126 qualifying markets (from 126 total)
2025-11-04 04:25:10,395 - market_selector - INFO - Selected 7 markets from 126 candidates
2025-11-04 04:25:10,682 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:25:10,683 - order_manager - WARNING - Could not fetch data for market 663864
2025-11-04 04:25:10,683 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 04:25:11,012 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:25:11,013 - order_manager - WARNING - Could not fetch data for market 663862
2025-11-04 04:25:11,013 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 04:25:11,308 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:25:11,309 - order_manager - WARNING - Could not fetch data for market 663860
2025-11-04 04:25:11,309 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 04:25:11,634 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:25:11,635 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 04:25:11,635 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 04:25:11,935 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:25:11,936 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 04:25:11,936 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 04:25:12,250 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:25:12,252 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 04:25:12,252 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 04:25:12,570 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:25:12,571 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 04:25:12,571 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 04:25:17,466 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 04:25:18,188 - market_scanner_v2 - INFO - âœ… Fetched 126 markets from API
2025-11-04 04:25:18,191 - market_scanner_v2 - INFO - âœ… Got 126 markets from API
2025-11-04 04:25:18,192 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 126/126 markets passed
2025-11-04 04:25:18,193 - market_scanner_v2 - INFO - âœ… Found 126 qualifying markets (from 126 total)
2025-11-04 04:25:18,195 - market_selector - INFO - Selected 7 markets from 126 candidates
2025-11-04 04:25:18,469 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:25:18,470 - order_manager - WARNING - Could not fetch data for market 663864
2025-11-04 04:25:18,470 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 04:25:18,768 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:25:18,769 - order_manager - WARNING - Could not fetch data for market 663862
2025-11-04 04:25:18,769 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 04:25:19,051 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:25:19,052 - order_manager - WARNING - Could not fetch data for market 663860
2025-11-04 04:25:19,052 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 04:25:19,347 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:25:19,348 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 04:25:19,348 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 04:25:19,637 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:25:19,637 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 04:25:19,637 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 04:25:19,911 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:25:19,912 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 04:25:19,912 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 04:25:20,200 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:25:20,201 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 04:25:20,201 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 04:25:26,071 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 04:25:27,039 - market_scanner_v2 - INFO - âœ… Fetched 126 markets from API
2025-11-04 04:25:27,042 - market_scanner_v2 - INFO - âœ… Got 126 markets from API
2025-11-04 04:25:27,043 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 126/126 markets passed
2025-11-04 04:25:27,044 - market_scanner_v2 - INFO - âœ… Found 126 qualifying markets (from 126 total)
2025-11-04 04:25:27,046 - market_selector - INFO - Selected 7 markets from 126 candidates
2025-11-04 04:25:27,360 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:25:27,361 - order_manager - WARNING - Could not fetch data for market 663864
2025-11-04 04:25:27,361 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 04:25:27,645 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:25:27,646 - order_manager - WARNING - Could not fetch data for market 663862
2025-11-04 04:25:27,646 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 04:25:27,941 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:25:27,942 - order_manager - WARNING - Could not fetch data for market 663860
2025-11-04 04:25:27,942 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 04:25:28,233 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:25:28,234 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 04:25:28,234 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 04:25:28,518 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:25:28,518 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 04:25:28,519 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 04:25:28,793 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:25:28,795 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 04:25:28,795 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 04:25:29,167 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:25:29,168 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 04:25:29,168 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 04:25:35,122 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 04:25:35,871 - market_scanner_v2 - INFO - âœ… Fetched 126 markets from API
2025-11-04 04:25:35,874 - market_scanner_v2 - INFO - âœ… Got 126 markets from API
2025-11-04 04:25:35,875 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 126/126 markets passed
2025-11-04 04:25:35,875 - market_scanner_v2 - INFO - âœ… Found 126 qualifying markets (from 126 total)
2025-11-04 04:25:35,877 - market_selector - INFO - Selected 7 markets from 126 candidates
2025-11-04 04:25:36,340 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:25:36,341 - order_manager - WARNING - Could not fetch data for market 663864
2025-11-04 04:25:36,341 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 04:25:36,632 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:25:36,633 - order_manager - WARNING - Could not fetch data for market 663862
2025-11-04 04:25:36,633 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 04:25:36,914 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:25:36,915 - order_manager - WARNING - Could not fetch data for market 663860
2025-11-04 04:25:36,915 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 04:25:37,201 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:25:37,201 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 04:25:37,201 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 04:25:37,492 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:25:37,493 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 04:25:37,493 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 04:25:37,786 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:25:37,787 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 04:25:37,787 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 04:25:38,081 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:25:38,081 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 04:25:38,081 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 04:25:43,149 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 04:25:43,869 - market_scanner_v2 - INFO - âœ… Fetched 126 markets from API
2025-11-04 04:25:43,872 - market_scanner_v2 - INFO - âœ… Got 126 markets from API
2025-11-04 04:25:43,873 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 126/126 markets passed
2025-11-04 04:25:43,873 - market_scanner_v2 - INFO - âœ… Found 126 qualifying markets (from 126 total)
2025-11-04 04:25:43,876 - market_selector - INFO - Selected 7 markets from 126 candidates
2025-11-04 04:25:44,144 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:25:44,144 - order_manager - WARNING - Could not fetch data for market 663864
2025-11-04 04:25:44,144 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 04:25:44,464 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:25:44,465 - order_manager - WARNING - Could not fetch data for market 663862
2025-11-04 04:25:44,465 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 04:25:44,757 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:25:44,758 - order_manager - WARNING - Could not fetch data for market 663860
2025-11-04 04:25:44,758 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 04:25:45,073 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:25:45,074 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 04:25:45,074 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 04:25:45,409 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:25:45,414 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 04:25:45,414 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 04:25:45,702 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:25:45,703 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 04:25:45,703 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 04:25:46,011 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:25:46,012 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 04:25:46,012 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 04:25:51,657 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 04:25:52,371 - market_scanner_v2 - INFO - âœ… Fetched 126 markets from API
2025-11-04 04:25:52,373 - market_scanner_v2 - INFO - âœ… Got 126 markets from API
2025-11-04 04:25:52,375 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 126/126 markets passed
2025-11-04 04:25:52,375 - market_scanner_v2 - INFO - âœ… Found 126 qualifying markets (from 126 total)
2025-11-04 04:25:52,377 - market_selector - INFO - Selected 7 markets from 126 candidates
2025-11-04 04:25:52,658 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:25:52,658 - order_manager - WARNING - Could not fetch data for market 663864
2025-11-04 04:25:52,658 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 04:25:52,939 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:25:52,940 - order_manager - WARNING - Could not fetch data for market 663862
2025-11-04 04:25:52,941 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 04:25:53,274 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:25:53,275 - order_manager - WARNING - Could not fetch data for market 663860
2025-11-04 04:25:53,275 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 04:25:53,584 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:25:53,585 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 04:25:53,585 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 04:25:53,868 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:25:53,869 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 04:25:53,869 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 04:25:54,158 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:25:54,160 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 04:25:54,160 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 04:25:54,480 - order_manager - ERROR - Error fetching market data: 'OrderSummary' object is not subscriptable
2025-11-04 04:25:54,481 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 04:25:54,481 - __main__ - INFO - Added market 663895 to pending orders
