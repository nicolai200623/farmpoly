2025-11-04 03:59:47,871 - __main__ - INFO - âœ… Using MarketScannerV2 (Playwright + Gamma API)
2025-11-04 03:59:54,797 - __main__ - INFO - âœ… Telegram alerts configured (Chat ID: -1003157421030)
2025-11-04 03:59:54,798 - __main__ - INFO - âœ… Webhook alerts configured
2025-11-04 03:59:54,798 - circuit_breaker - INFO - âœ… Circuit Breaker 'gamma_api' initialized (threshold=5, timeout=60s)
2025-11-04 03:59:54,798 - circuit_breaker - INFO - âœ… Circuit Breaker 'playwright_scraper' initialized (threshold=3, timeout=120s)
2025-11-04 03:59:54,798 - order_manager - INFO - CLOB client initialized successfully (read-only mode)
2025-11-04 03:59:54,812 - wallet_manager - INFO - Loading REAL wallets from .env
2025-11-04 03:59:54,824 - wallet_manager - INFO - âœ… Loaded wallet 1: 0x18F261DC...Ae4FfD96
2025-11-04 03:59:54,824 - wallet_manager - INFO - âœ… Successfully loaded 1 real wallets
2025-11-04 03:59:54,845 - ml_predictor - INFO - No pre-trained model found, using new model
2025-11-04 03:59:54,845 - monitoring_system - INFO - âœ… Monitoring System initialized
2025-11-04 03:59:54,845 - __main__ - INFO - âœ… Monitoring System enabled
2025-11-04 03:59:54,845 - __main__ - INFO - â­ï¸  Reward Manager disabled in config
2025-11-04 03:59:54,846 - __main__ - INFO - All modules initialized successfully
2025-11-04 03:59:54,846 - __main__ - INFO - ðŸš€ Starting Polymarket Trading Bot...
2025-11-04 03:59:55,609 - ml_predictor - INFO - Alert sent: ðŸš€ <b>Polymarket Bot Started</b>
â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”
â° Time: 2025-11-04 03:59:54
ðŸ’¼ Wallets: 1
ðŸ“Š Status: Running
â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”
Bot is now scanning markets and placing orders.
2025-11-04 03:59:55,610 - __main__ - INFO - âœ… Startup alert sent
2025-11-04 03:59:55,610 - __main__ - INFO - ðŸ” Checking USDC approval for wallets...
2025-11-04 03:59:55,756 - usdc_approver - INFO - âœ… Connected to Polygon RPC: https://polygon-mainnet.g.alchemy.com/v2/FQJnJWsEQ...
2025-11-04 03:59:55,756 - __main__ - INFO -    Checking wallet: 0x18F261DC...Ae4FfD96
2025-11-04 03:59:55,890 - __main__ - INFO -    Raw allowance: 100000000 (base units)
2025-11-04 03:59:55,890 - __main__ - INFO -    Allowance in USDC: 100.00 USDC
2025-11-04 03:59:55,891 - __main__ - INFO -    Required minimum: 100 USDC (test mode)
2025-11-04 03:59:55,891 - __main__ - INFO - âœ… USDC approval OK (100 USDC)
2025-11-04 03:59:55,891 - __main__ - WARNING -    âš ï¸  Running in TEST MODE with 100 USDC
2025-11-04 03:59:55,891 - __main__ - WARNING -    For production, approve at least 1,000 USDC
2025-11-04 03:59:55,891 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 03:59:55,892 - ml_predictor - INFO - Insufficient training data: 0 samples
2025-11-04 03:59:55,892 - __main__ - INFO - ML model updated successfully
2025-11-04 03:59:57,640 - market_scanner_v2 - INFO - âœ… Fetched 134 markets from API
2025-11-04 03:59:57,643 - market_scanner_v2 - INFO - âœ… Got 134 markets from API
2025-11-04 03:59:57,644 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 134/134 markets passed
2025-11-04 03:59:57,644 - market_scanner_v2 - INFO - âœ… Found 134 qualifying markets (from 134 total)
2025-11-04 03:59:57,646 - market_selector - INFO - Selected 3 markets from 134 candidates
2025-11-04 03:59:57,925 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 03:59:57,925 - order_manager - WARNING - Could not fetch data for market 663822
2025-11-04 03:59:57,925 - __main__ - INFO - Added market 663822 to pending orders
2025-11-04 03:59:58,252 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 03:59:58,252 - order_manager - WARNING - Could not fetch data for market 663840
2025-11-04 03:59:58,252 - __main__ - INFO - Added market 663840 to pending orders
2025-11-04 03:59:58,530 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 03:59:58,531 - order_manager - WARNING - Could not fetch data for market 663834
2025-11-04 03:59:58,531 - __main__ - INFO - Added market 663834 to pending orders
2025-11-04 04:00:01,752 - ml_predictor - INFO - Alert sent: âœ… <b>Hourly Report</b>
â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”
â° Time: 2025-11-04 04:00:01

ðŸ“Š <b>Performance (Last 60 min)</b>
   â€¢ Scans: 1
   â€¢ Markets found: 134 (134.0/scan)
   â€¢ Orders placed: 0
   â€¢ Orders filled: 0 (0.0%)
   â€¢ Profit: $0.00
   â€¢ Errors: 0 (0.0%)

ðŸ’» <b>System Health</b>
   â€¢ CPU: 61.0%
   â€¢ RAM: 55.7%
   â€¢ Bot RAM: 558 MB
        
â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”
2025-11-04 04:00:01,753 - monitoring_system - INFO - âœ… Hourly report sent
2025-11-04 04:00:04,204 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 04:00:04,982 - market_scanner_v2 - INFO - âœ… Fetched 134 markets from API
2025-11-04 04:00:04,992 - market_scanner_v2 - INFO - âœ… Got 134 markets from API
2025-11-04 04:00:04,993 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 134/134 markets passed
2025-11-04 04:00:04,997 - market_scanner_v2 - INFO - âœ… Found 134 qualifying markets (from 134 total)
2025-11-04 04:00:05,000 - market_selector - INFO - Selected 7 markets from 134 candidates
2025-11-04 04:00:05,471 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:00:05,472 - order_manager - WARNING - Could not fetch data for market 663864
2025-11-04 04:00:05,472 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 04:00:06,091 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:00:06,091 - order_manager - WARNING - Could not fetch data for market 663860
2025-11-04 04:00:06,095 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 04:00:06,578 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:00:06,579 - order_manager - WARNING - Could not fetch data for market 663862
2025-11-04 04:00:06,579 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 04:00:07,069 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:00:07,072 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 04:00:07,072 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 04:00:07,580 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:00:07,580 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 04:00:07,581 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 04:00:08,039 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:00:08,040 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 04:00:08,040 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 04:00:08,515 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:00:08,519 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 04:00:08,519 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 04:00:13,835 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 04:00:14,640 - market_scanner_v2 - INFO - âœ… Fetched 134 markets from API
2025-11-04 04:00:14,649 - market_scanner_v2 - INFO - âœ… Got 134 markets from API
2025-11-04 04:00:14,650 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 134/134 markets passed
2025-11-04 04:00:14,650 - market_scanner_v2 - INFO - âœ… Found 134 qualifying markets (from 134 total)
2025-11-04 04:00:14,660 - market_selector - INFO - Selected 7 markets from 134 candidates
2025-11-04 04:00:15,112 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:00:15,116 - order_manager - WARNING - Could not fetch data for market 663864
2025-11-04 04:00:15,116 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 04:00:15,552 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:00:15,552 - order_manager - WARNING - Could not fetch data for market 663860
2025-11-04 04:00:15,552 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 04:00:15,996 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:00:15,996 - order_manager - WARNING - Could not fetch data for market 663862
2025-11-04 04:00:15,996 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 04:00:16,412 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:00:16,418 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 04:00:16,419 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 04:00:16,955 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:00:16,956 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 04:00:16,956 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 04:00:17,457 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:00:17,467 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 04:00:17,467 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 04:00:17,935 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:00:17,936 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 04:00:17,936 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 04:00:22,819 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 04:00:23,541 - market_scanner_v2 - INFO - âœ… Fetched 134 markets from API
2025-11-04 04:00:23,544 - market_scanner_v2 - INFO - âœ… Got 134 markets from API
2025-11-04 04:00:23,545 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 134/134 markets passed
2025-11-04 04:00:23,545 - market_scanner_v2 - INFO - âœ… Found 134 qualifying markets (from 134 total)
2025-11-04 04:00:23,551 - market_selector - INFO - Selected 7 markets from 134 candidates
2025-11-04 04:00:23,845 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:00:23,845 - order_manager - WARNING - Could not fetch data for market 663864
2025-11-04 04:00:23,845 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 04:00:24,142 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:00:24,143 - order_manager - WARNING - Could not fetch data for market 663860
2025-11-04 04:00:24,143 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 04:00:24,433 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:00:24,438 - order_manager - WARNING - Could not fetch data for market 663862
2025-11-04 04:00:24,438 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 04:00:24,745 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:00:24,746 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 04:00:24,746 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 04:00:25,195 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:00:25,195 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 04:00:25,195 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 04:00:25,476 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:00:25,477 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 04:00:25,477 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 04:00:25,796 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:00:25,797 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 04:00:25,797 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 04:00:31,434 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 04:00:32,179 - market_scanner_v2 - INFO - âœ… Fetched 134 markets from API
2025-11-04 04:00:32,183 - market_scanner_v2 - INFO - âœ… Got 134 markets from API
2025-11-04 04:00:32,184 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 134/134 markets passed
2025-11-04 04:00:32,184 - market_scanner_v2 - INFO - âœ… Found 134 qualifying markets (from 134 total)
2025-11-04 04:00:32,187 - market_selector - INFO - Selected 7 markets from 134 candidates
2025-11-04 04:00:32,493 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:00:32,493 - order_manager - WARNING - Could not fetch data for market 663864
2025-11-04 04:00:32,493 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 04:00:32,760 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:00:32,761 - order_manager - WARNING - Could not fetch data for market 663860
2025-11-04 04:00:32,761 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 04:00:33,059 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:00:33,060 - order_manager - WARNING - Could not fetch data for market 663862
2025-11-04 04:00:33,061 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 04:00:33,353 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:00:33,354 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 04:00:33,354 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 04:00:33,634 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:00:33,635 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 04:00:33,635 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 04:00:33,958 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:00:33,959 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 04:00:33,959 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 04:00:34,251 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:00:34,251 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 04:00:34,251 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 04:00:40,116 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 04:00:40,900 - market_scanner_v2 - INFO - âœ… Fetched 134 markets from API
2025-11-04 04:00:40,903 - market_scanner_v2 - INFO - âœ… Got 134 markets from API
2025-11-04 04:00:40,904 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 134/134 markets passed
2025-11-04 04:00:40,904 - market_scanner_v2 - INFO - âœ… Found 134 qualifying markets (from 134 total)
2025-11-04 04:00:40,906 - market_selector - INFO - Selected 7 markets from 134 candidates
2025-11-04 04:00:41,233 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:00:41,233 - order_manager - WARNING - Could not fetch data for market 663864
2025-11-04 04:00:41,233 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 04:00:41,511 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:00:41,511 - order_manager - WARNING - Could not fetch data for market 663860
2025-11-04 04:00:41,511 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 04:00:41,820 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:00:41,820 - order_manager - WARNING - Could not fetch data for market 663862
2025-11-04 04:00:41,820 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 04:00:42,089 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:00:42,090 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 04:00:42,090 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 04:00:42,365 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:00:42,365 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 04:00:42,365 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 04:00:42,646 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:00:42,646 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 04:00:42,646 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 04:00:42,948 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:00:42,949 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 04:00:42,949 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 04:00:47,653 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 04:00:48,385 - market_scanner_v2 - INFO - âœ… Fetched 134 markets from API
2025-11-04 04:00:48,390 - market_scanner_v2 - INFO - âœ… Got 134 markets from API
2025-11-04 04:00:48,392 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 134/134 markets passed
2025-11-04 04:00:48,392 - market_scanner_v2 - INFO - âœ… Found 134 qualifying markets (from 134 total)
2025-11-04 04:00:48,402 - market_selector - INFO - Selected 7 markets from 134 candidates
2025-11-04 04:00:48,690 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:00:48,690 - order_manager - WARNING - Could not fetch data for market 663864
2025-11-04 04:00:48,690 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 04:00:48,982 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:00:48,984 - order_manager - WARNING - Could not fetch data for market 663860
2025-11-04 04:00:48,984 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 04:00:49,297 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:00:49,298 - order_manager - WARNING - Could not fetch data for market 663862
2025-11-04 04:00:49,298 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 04:00:49,593 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:00:49,594 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 04:00:49,594 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 04:00:49,893 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:00:49,899 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 04:00:49,899 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 04:00:50,230 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:00:50,231 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 04:00:50,231 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 04:00:50,530 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:00:50,531 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 04:00:50,531 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 04:00:55,743 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 04:00:56,546 - market_scanner_v2 - INFO - âœ… Fetched 134 markets from API
2025-11-04 04:00:56,548 - market_scanner_v2 - INFO - âœ… Got 134 markets from API
2025-11-04 04:00:56,550 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 134/134 markets passed
2025-11-04 04:00:56,550 - market_scanner_v2 - INFO - âœ… Found 134 qualifying markets (from 134 total)
2025-11-04 04:00:56,553 - market_selector - INFO - Selected 7 markets from 134 candidates
2025-11-04 04:00:56,858 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:00:56,858 - order_manager - WARNING - Could not fetch data for market 663864
2025-11-04 04:00:56,858 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 04:00:57,175 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:00:57,175 - order_manager - WARNING - Could not fetch data for market 663860
2025-11-04 04:00:57,175 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 04:00:57,473 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:00:57,475 - order_manager - WARNING - Could not fetch data for market 663862
2025-11-04 04:00:57,475 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 04:00:57,799 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:00:57,801 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 04:00:57,801 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 04:00:58,117 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:00:58,118 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 04:00:58,118 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 04:00:58,413 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:00:58,414 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 04:00:58,414 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 04:00:58,712 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:00:58,713 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 04:00:58,713 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 04:01:03,089 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 04:01:03,561 - market_scanner_v2 - INFO - âœ… Fetched 140 markets from API
2025-11-04 04:01:03,564 - market_scanner_v2 - INFO - âœ… Got 140 markets from API
2025-11-04 04:01:03,567 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 140/140 markets passed
2025-11-04 04:01:03,567 - market_scanner_v2 - INFO - âœ… Found 140 qualifying markets (from 140 total)
2025-11-04 04:01:03,570 - market_selector - INFO - Selected 7 markets from 140 candidates
2025-11-04 04:01:03,900 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:01:03,900 - order_manager - WARNING - Could not fetch data for market 663864
2025-11-04 04:01:03,900 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 04:01:04,301 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:01:04,303 - order_manager - WARNING - Could not fetch data for market 663860
2025-11-04 04:01:04,304 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 04:01:04,620 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:01:04,621 - order_manager - WARNING - Could not fetch data for market 663862
2025-11-04 04:01:04,622 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 04:01:04,947 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:01:04,948 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 04:01:04,948 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 04:01:05,294 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:01:05,294 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 04:01:05,295 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 04:01:05,609 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:01:05,609 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 04:01:05,610 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 04:01:05,919 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:01:05,919 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 04:01:05,919 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 04:01:11,341 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 04:01:12,097 - market_scanner_v2 - INFO - âœ… Fetched 138 markets from API
2025-11-04 04:01:12,100 - market_scanner_v2 - INFO - âœ… Got 138 markets from API
2025-11-04 04:01:12,102 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 138/138 markets passed
2025-11-04 04:01:12,102 - market_scanner_v2 - INFO - âœ… Found 138 qualifying markets (from 138 total)
2025-11-04 04:01:12,112 - market_selector - INFO - Selected 7 markets from 138 candidates
2025-11-04 04:01:12,492 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:01:12,493 - order_manager - WARNING - Could not fetch data for market 663864
2025-11-04 04:01:12,493 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 04:01:12,887 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:01:12,888 - order_manager - WARNING - Could not fetch data for market 663860
2025-11-04 04:01:12,888 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 04:01:13,356 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:01:13,357 - order_manager - WARNING - Could not fetch data for market 663862
2025-11-04 04:01:13,357 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 04:01:13,761 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:01:13,761 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 04:01:13,763 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 04:01:14,136 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:01:14,136 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 04:01:14,136 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 04:01:14,532 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:01:14,538 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 04:01:14,538 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 04:01:14,921 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:01:14,921 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 04:01:14,921 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 04:01:20,399 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 04:01:21,154 - market_scanner_v2 - INFO - âœ… Fetched 138 markets from API
2025-11-04 04:01:21,156 - market_scanner_v2 - INFO - âœ… Got 138 markets from API
2025-11-04 04:01:21,160 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 138/138 markets passed
2025-11-04 04:01:21,160 - market_scanner_v2 - INFO - âœ… Found 138 qualifying markets (from 138 total)
2025-11-04 04:01:21,166 - market_selector - INFO - Selected 7 markets from 138 candidates
2025-11-04 04:01:21,621 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:01:21,624 - order_manager - WARNING - Could not fetch data for market 663864
2025-11-04 04:01:21,624 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 04:01:22,029 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:01:22,031 - order_manager - WARNING - Could not fetch data for market 663860
2025-11-04 04:01:22,031 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 04:01:22,413 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:01:22,414 - order_manager - WARNING - Could not fetch data for market 663862
2025-11-04 04:01:22,414 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 04:01:22,705 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:01:22,705 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 04:01:22,705 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 04:01:22,973 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:01:22,974 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 04:01:22,974 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 04:01:23,270 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:01:23,271 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 04:01:23,271 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 04:01:23,548 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:01:23,548 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 04:01:23,548 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 04:01:29,480 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 04:01:30,748 - market_scanner_v2 - INFO - âœ… Fetched 138 markets from API
2025-11-04 04:01:30,750 - market_scanner_v2 - INFO - âœ… Got 138 markets from API
2025-11-04 04:01:30,752 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 138/138 markets passed
2025-11-04 04:01:30,752 - market_scanner_v2 - INFO - âœ… Found 138 qualifying markets (from 138 total)
2025-11-04 04:01:30,754 - market_selector - INFO - Selected 7 markets from 138 candidates
2025-11-04 04:01:31,037 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:01:31,037 - order_manager - WARNING - Could not fetch data for market 663864
2025-11-04 04:01:31,037 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 04:01:31,342 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:01:31,342 - order_manager - WARNING - Could not fetch data for market 663860
2025-11-04 04:01:31,342 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 04:01:31,789 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:01:31,790 - order_manager - WARNING - Could not fetch data for market 663862
2025-11-04 04:01:31,791 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 04:01:32,093 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:01:32,094 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 04:01:32,094 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 04:01:32,386 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:01:32,387 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 04:01:32,387 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 04:01:32,666 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:01:32,667 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 04:01:32,667 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 04:01:32,960 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:01:32,961 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 04:01:32,961 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 04:01:38,748 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 04:01:39,556 - market_scanner_v2 - INFO - âœ… Fetched 138 markets from API
2025-11-04 04:01:39,559 - market_scanner_v2 - INFO - âœ… Got 138 markets from API
2025-11-04 04:01:39,560 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 138/138 markets passed
2025-11-04 04:01:39,560 - market_scanner_v2 - INFO - âœ… Found 138 qualifying markets (from 138 total)
2025-11-04 04:01:39,562 - market_selector - INFO - Selected 7 markets from 138 candidates
2025-11-04 04:01:39,862 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:01:39,862 - order_manager - WARNING - Could not fetch data for market 663864
2025-11-04 04:01:39,862 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 04:01:40,202 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:01:40,204 - order_manager - WARNING - Could not fetch data for market 663860
2025-11-04 04:01:40,204 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 04:01:40,529 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:01:40,529 - order_manager - WARNING - Could not fetch data for market 663862
2025-11-04 04:01:40,530 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 04:01:40,828 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:01:40,829 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 04:01:40,829 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 04:01:41,132 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:01:41,134 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 04:01:41,134 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 04:01:41,442 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:01:41,442 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 04:01:41,443 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 04:01:41,735 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:01:41,736 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 04:01:41,736 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 04:01:46,039 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 04:01:46,778 - market_scanner_v2 - INFO - âœ… Fetched 138 markets from API
2025-11-04 04:01:46,780 - market_scanner_v2 - INFO - âœ… Got 138 markets from API
2025-11-04 04:01:46,782 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 138/138 markets passed
2025-11-04 04:01:46,782 - market_scanner_v2 - INFO - âœ… Found 138 qualifying markets (from 138 total)
2025-11-04 04:01:46,784 - market_selector - INFO - Selected 7 markets from 138 candidates
2025-11-04 04:01:47,112 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:01:47,113 - order_manager - WARNING - Could not fetch data for market 663864
2025-11-04 04:01:47,113 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 04:01:47,464 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:01:47,466 - order_manager - WARNING - Could not fetch data for market 663860
2025-11-04 04:01:47,466 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 04:01:47,776 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:01:47,777 - order_manager - WARNING - Could not fetch data for market 663862
2025-11-04 04:01:47,777 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 04:01:48,052 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:01:48,054 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 04:01:48,055 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 04:01:48,332 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:01:48,334 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 04:01:48,334 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 04:01:48,610 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:01:48,611 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 04:01:48,611 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 04:01:48,904 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:01:48,908 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 04:01:48,908 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 04:01:54,458 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 04:01:55,230 - market_scanner_v2 - INFO - âœ… Fetched 138 markets from API
2025-11-04 04:01:55,233 - market_scanner_v2 - INFO - âœ… Got 138 markets from API
2025-11-04 04:01:55,234 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 138/138 markets passed
2025-11-04 04:01:55,234 - market_scanner_v2 - INFO - âœ… Found 138 qualifying markets (from 138 total)
2025-11-04 04:01:55,237 - market_selector - INFO - Selected 7 markets from 138 candidates
2025-11-04 04:01:55,517 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:01:55,519 - order_manager - WARNING - Could not fetch data for market 663864
2025-11-04 04:01:55,520 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 04:01:55,797 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:01:55,797 - order_manager - WARNING - Could not fetch data for market 663860
2025-11-04 04:01:55,797 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 04:01:56,068 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:01:56,069 - order_manager - WARNING - Could not fetch data for market 663862
2025-11-04 04:01:56,069 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 04:01:56,361 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:01:56,362 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 04:01:56,362 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 04:01:56,670 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:01:56,671 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 04:01:56,671 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 04:01:56,971 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:01:56,972 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 04:01:56,972 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 04:01:57,266 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:01:57,267 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 04:01:57,267 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 04:02:02,596 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 04:02:03,346 - market_scanner_v2 - INFO - âœ… Fetched 138 markets from API
2025-11-04 04:02:03,350 - market_scanner_v2 - INFO - âœ… Got 138 markets from API
2025-11-04 04:02:03,351 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 138/138 markets passed
2025-11-04 04:02:03,351 - market_scanner_v2 - INFO - âœ… Found 138 qualifying markets (from 138 total)
2025-11-04 04:02:03,354 - market_selector - INFO - Selected 7 markets from 138 candidates
2025-11-04 04:02:03,651 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:02:03,652 - order_manager - WARNING - Could not fetch data for market 663864
2025-11-04 04:02:03,652 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 04:02:03,939 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:02:03,940 - order_manager - WARNING - Could not fetch data for market 663860
2025-11-04 04:02:03,940 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 04:02:04,214 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:02:04,215 - order_manager - WARNING - Could not fetch data for market 663862
2025-11-04 04:02:04,215 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 04:02:04,509 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:02:04,510 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 04:02:04,510 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 04:02:04,792 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:02:04,793 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 04:02:04,793 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 04:02:05,079 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:02:05,080 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 04:02:05,080 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 04:02:05,378 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:02:05,379 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 04:02:05,379 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 04:02:09,621 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 04:02:10,346 - market_scanner_v2 - INFO - âœ… Fetched 138 markets from API
2025-11-04 04:02:10,349 - market_scanner_v2 - INFO - âœ… Got 138 markets from API
2025-11-04 04:02:10,350 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 138/138 markets passed
2025-11-04 04:02:10,350 - market_scanner_v2 - INFO - âœ… Found 138 qualifying markets (from 138 total)
2025-11-04 04:02:10,352 - market_selector - INFO - Selected 7 markets from 138 candidates
2025-11-04 04:02:10,632 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:02:10,634 - order_manager - WARNING - Could not fetch data for market 663864
2025-11-04 04:02:10,635 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 04:02:10,912 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:02:10,912 - order_manager - WARNING - Could not fetch data for market 663860
2025-11-04 04:02:10,912 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 04:02:11,197 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:02:11,204 - order_manager - WARNING - Could not fetch data for market 663862
2025-11-04 04:02:11,204 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 04:02:11,485 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:02:11,486 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 04:02:11,486 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 04:02:11,784 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:02:11,784 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 04:02:11,784 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 04:02:12,117 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:02:12,122 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 04:02:12,122 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 04:02:12,414 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:02:12,415 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 04:02:12,415 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 04:02:18,336 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 04:02:19,048 - market_scanner_v2 - INFO - âœ… Fetched 126 markets from API
2025-11-04 04:02:19,050 - market_scanner_v2 - INFO - âœ… Got 126 markets from API
2025-11-04 04:02:19,051 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 126/126 markets passed
2025-11-04 04:02:19,052 - market_scanner_v2 - INFO - âœ… Found 126 qualifying markets (from 126 total)
2025-11-04 04:02:19,054 - market_selector - INFO - Selected 7 markets from 126 candidates
2025-11-04 04:02:19,335 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:02:19,335 - order_manager - WARNING - Could not fetch data for market 663864
2025-11-04 04:02:19,335 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 04:02:19,630 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:02:19,631 - order_manager - WARNING - Could not fetch data for market 663860
2025-11-04 04:02:19,631 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 04:02:19,943 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:02:19,944 - order_manager - WARNING - Could not fetch data for market 663862
2025-11-04 04:02:19,944 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 04:02:20,240 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:02:20,241 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 04:02:20,241 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 04:02:20,533 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:02:20,534 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 04:02:20,534 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 04:02:20,800 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:02:20,801 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 04:02:20,801 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 04:02:21,084 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:02:21,086 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 04:02:21,086 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 04:02:26,105 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 04:02:26,844 - market_scanner_v2 - INFO - âœ… Fetched 126 markets from API
2025-11-04 04:02:26,846 - market_scanner_v2 - INFO - âœ… Got 126 markets from API
2025-11-04 04:02:26,847 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 126/126 markets passed
2025-11-04 04:02:26,847 - market_scanner_v2 - INFO - âœ… Found 126 qualifying markets (from 126 total)
2025-11-04 04:02:26,850 - market_selector - INFO - Selected 7 markets from 126 candidates
2025-11-04 04:02:27,160 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:02:27,161 - order_manager - WARNING - Could not fetch data for market 663864
2025-11-04 04:02:27,161 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 04:02:27,444 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:02:27,444 - order_manager - WARNING - Could not fetch data for market 663860
2025-11-04 04:02:27,444 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 04:02:27,723 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:02:27,724 - order_manager - WARNING - Could not fetch data for market 663862
2025-11-04 04:02:27,724 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 04:02:28,015 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:02:28,016 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 04:02:28,016 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 04:02:28,307 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:02:28,307 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 04:02:28,307 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 04:02:28,602 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:02:28,603 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 04:02:28,603 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 04:02:28,892 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:02:28,892 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 04:02:28,892 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 04:02:34,574 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 04:02:35,337 - market_scanner_v2 - INFO - âœ… Fetched 126 markets from API
2025-11-04 04:02:35,339 - market_scanner_v2 - INFO - âœ… Got 126 markets from API
2025-11-04 04:02:35,340 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 126/126 markets passed
2025-11-04 04:02:35,341 - market_scanner_v2 - INFO - âœ… Found 126 qualifying markets (from 126 total)
2025-11-04 04:02:35,343 - market_selector - INFO - Selected 7 markets from 126 candidates
2025-11-04 04:02:35,637 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:02:35,638 - order_manager - WARNING - Could not fetch data for market 663864
2025-11-04 04:02:35,638 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 04:02:35,942 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:02:35,942 - order_manager - WARNING - Could not fetch data for market 663860
2025-11-04 04:02:35,942 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 04:02:36,234 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:02:36,236 - order_manager - WARNING - Could not fetch data for market 663862
2025-11-04 04:02:36,236 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 04:02:36,516 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:02:36,518 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 04:02:36,518 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 04:02:36,825 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:02:36,826 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 04:02:36,826 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 04:02:37,150 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:02:37,152 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 04:02:37,152 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 04:02:37,442 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:02:37,443 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 04:02:37,444 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 04:02:41,588 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 04:02:42,341 - market_scanner_v2 - INFO - âœ… Fetched 126 markets from API
2025-11-04 04:02:42,358 - market_scanner_v2 - INFO - âœ… Got 126 markets from API
2025-11-04 04:02:42,359 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 126/126 markets passed
2025-11-04 04:02:42,360 - market_scanner_v2 - INFO - âœ… Found 126 qualifying markets (from 126 total)
2025-11-04 04:02:42,370 - market_selector - INFO - Selected 7 markets from 126 candidates
2025-11-04 04:02:42,840 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:02:42,841 - order_manager - WARNING - Could not fetch data for market 663864
2025-11-04 04:02:42,841 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 04:02:43,133 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:02:43,134 - order_manager - WARNING - Could not fetch data for market 663860
2025-11-04 04:02:43,135 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 04:02:43,436 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:02:43,438 - order_manager - WARNING - Could not fetch data for market 663862
2025-11-04 04:02:43,438 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 04:02:43,722 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:02:43,723 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 04:02:43,723 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 04:02:44,205 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:02:44,205 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 04:02:44,206 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 04:02:44,526 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:02:44,527 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 04:02:44,527 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 04:02:44,813 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:02:44,814 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 04:02:44,814 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 04:02:49,162 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 04:02:49,939 - market_scanner_v2 - INFO - âœ… Fetched 126 markets from API
2025-11-04 04:02:49,942 - market_scanner_v2 - INFO - âœ… Got 126 markets from API
2025-11-04 04:02:49,944 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 126/126 markets passed
2025-11-04 04:02:49,944 - market_scanner_v2 - INFO - âœ… Found 126 qualifying markets (from 126 total)
2025-11-04 04:02:49,947 - market_selector - INFO - Selected 7 markets from 126 candidates
2025-11-04 04:02:50,229 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:02:50,229 - order_manager - WARNING - Could not fetch data for market 663864
2025-11-04 04:02:50,229 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 04:02:50,515 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:02:50,516 - order_manager - WARNING - Could not fetch data for market 663860
2025-11-04 04:02:50,516 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 04:02:50,830 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:02:50,832 - order_manager - WARNING - Could not fetch data for market 663862
2025-11-04 04:02:50,832 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 04:02:51,152 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:02:51,153 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 04:02:51,153 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 04:02:51,456 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:02:51,458 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 04:02:51,458 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 04:02:51,768 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:02:51,771 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 04:02:51,771 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 04:02:52,093 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:02:52,094 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 04:02:52,095 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 04:02:56,922 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 04:02:57,682 - market_scanner_v2 - INFO - âœ… Fetched 126 markets from API
2025-11-04 04:02:57,685 - market_scanner_v2 - INFO - âœ… Got 126 markets from API
2025-11-04 04:02:57,686 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 126/126 markets passed
2025-11-04 04:02:57,686 - market_scanner_v2 - INFO - âœ… Found 126 qualifying markets (from 126 total)
2025-11-04 04:02:57,688 - market_selector - INFO - Selected 7 markets from 126 candidates
2025-11-04 04:02:58,001 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:02:58,002 - order_manager - WARNING - Could not fetch data for market 663864
2025-11-04 04:02:58,002 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 04:02:58,285 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:02:58,285 - order_manager - WARNING - Could not fetch data for market 663860
2025-11-04 04:02:58,285 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 04:02:58,572 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:02:58,572 - order_manager - WARNING - Could not fetch data for market 663862
2025-11-04 04:02:58,572 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 04:02:58,852 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:02:58,853 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 04:02:58,853 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 04:02:59,152 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:02:59,153 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 04:02:59,153 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 04:02:59,449 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:02:59,449 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 04:02:59,450 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 04:02:59,730 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:02:59,732 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 04:02:59,732 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 04:03:03,888 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 04:03:04,641 - market_scanner_v2 - INFO - âœ… Fetched 126 markets from API
2025-11-04 04:03:04,643 - market_scanner_v2 - INFO - âœ… Got 126 markets from API
2025-11-04 04:03:04,644 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 126/126 markets passed
2025-11-04 04:03:04,644 - market_scanner_v2 - INFO - âœ… Found 126 qualifying markets (from 126 total)
2025-11-04 04:03:04,647 - market_selector - INFO - Selected 7 markets from 126 candidates
2025-11-04 04:03:04,920 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:03:04,920 - order_manager - WARNING - Could not fetch data for market 663864
2025-11-04 04:03:04,920 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 04:03:05,230 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:03:05,231 - order_manager - WARNING - Could not fetch data for market 663860
2025-11-04 04:03:05,231 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 04:03:05,525 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:03:05,526 - order_manager - WARNING - Could not fetch data for market 663862
2025-11-04 04:03:05,526 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 04:03:05,809 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:03:05,810 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 04:03:05,810 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 04:03:06,108 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:03:06,110 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 04:03:06,110 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 04:03:06,390 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:03:06,391 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 04:03:06,391 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 04:03:06,684 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:03:06,685 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 04:03:06,685 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 04:03:11,529 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 04:03:12,252 - market_scanner_v2 - INFO - âœ… Fetched 126 markets from API
2025-11-04 04:03:12,255 - market_scanner_v2 - INFO - âœ… Got 126 markets from API
2025-11-04 04:03:12,256 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 126/126 markets passed
2025-11-04 04:03:12,256 - market_scanner_v2 - INFO - âœ… Found 126 qualifying markets (from 126 total)
2025-11-04 04:03:12,258 - market_selector - INFO - Selected 7 markets from 126 candidates
2025-11-04 04:03:12,541 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:03:12,542 - order_manager - WARNING - Could not fetch data for market 663864
2025-11-04 04:03:12,543 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 04:03:12,834 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:03:12,835 - order_manager - WARNING - Could not fetch data for market 663860
2025-11-04 04:03:12,835 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 04:03:13,136 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:03:13,136 - order_manager - WARNING - Could not fetch data for market 663862
2025-11-04 04:03:13,137 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 04:03:13,416 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:03:13,416 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 04:03:13,416 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 04:03:13,699 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:03:13,700 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 04:03:13,700 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 04:03:13,973 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:03:13,974 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 04:03:13,974 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 04:03:14,265 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:03:14,266 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 04:03:14,266 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 04:03:18,838 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 04:03:19,579 - market_scanner_v2 - INFO - âœ… Fetched 126 markets from API
2025-11-04 04:03:19,583 - market_scanner_v2 - INFO - âœ… Got 126 markets from API
2025-11-04 04:03:19,584 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 126/126 markets passed
2025-11-04 04:03:19,584 - market_scanner_v2 - INFO - âœ… Found 126 qualifying markets (from 126 total)
2025-11-04 04:03:19,586 - market_selector - INFO - Selected 7 markets from 126 candidates
2025-11-04 04:03:19,890 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:03:19,891 - order_manager - WARNING - Could not fetch data for market 663864
2025-11-04 04:03:19,891 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 04:03:20,182 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:03:20,183 - order_manager - WARNING - Could not fetch data for market 663860
2025-11-04 04:03:20,183 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 04:03:20,463 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:03:20,464 - order_manager - WARNING - Could not fetch data for market 663862
2025-11-04 04:03:20,464 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 04:03:20,739 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:03:20,739 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 04:03:20,739 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 04:03:21,026 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:03:21,026 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 04:03:21,026 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 04:03:21,314 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:03:21,315 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 04:03:21,315 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 04:03:21,608 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:03:21,609 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 04:03:21,609 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 04:03:27,280 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 04:03:28,060 - market_scanner_v2 - INFO - âœ… Fetched 126 markets from API
2025-11-04 04:03:28,062 - market_scanner_v2 - INFO - âœ… Got 126 markets from API
2025-11-04 04:03:28,063 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 126/126 markets passed
2025-11-04 04:03:28,064 - market_scanner_v2 - INFO - âœ… Found 126 qualifying markets (from 126 total)
2025-11-04 04:03:28,066 - market_selector - INFO - Selected 7 markets from 126 candidates
2025-11-04 04:03:28,365 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:03:28,365 - order_manager - WARNING - Could not fetch data for market 663864
2025-11-04 04:03:28,365 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 04:03:28,675 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:03:28,676 - order_manager - WARNING - Could not fetch data for market 663860
2025-11-04 04:03:28,676 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 04:03:28,976 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:03:28,977 - order_manager - WARNING - Could not fetch data for market 663862
2025-11-04 04:03:28,977 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 04:03:29,255 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:03:29,256 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 04:03:29,256 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 04:03:29,538 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:03:29,539 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 04:03:29,539 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 04:03:29,828 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:03:29,829 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 04:03:29,830 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 04:03:30,129 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:03:30,130 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 04:03:30,131 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 04:03:34,734 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 04:03:35,481 - market_scanner_v2 - INFO - âœ… Fetched 126 markets from API
2025-11-04 04:03:35,484 - market_scanner_v2 - INFO - âœ… Got 126 markets from API
2025-11-04 04:03:35,485 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 126/126 markets passed
2025-11-04 04:03:35,486 - market_scanner_v2 - INFO - âœ… Found 126 qualifying markets (from 126 total)
2025-11-04 04:03:35,488 - market_selector - INFO - Selected 7 markets from 126 candidates
2025-11-04 04:03:35,758 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:03:35,759 - order_manager - WARNING - Could not fetch data for market 663864
2025-11-04 04:03:35,759 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 04:03:36,138 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:03:36,138 - order_manager - WARNING - Could not fetch data for market 663860
2025-11-04 04:03:36,138 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 04:03:36,403 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:03:36,404 - order_manager - WARNING - Could not fetch data for market 663862
2025-11-04 04:03:36,404 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 04:03:36,694 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:03:36,695 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 04:03:36,695 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 04:03:36,979 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:03:36,979 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 04:03:36,979 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 04:03:37,258 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:03:37,259 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 04:03:37,259 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 04:03:37,521 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:03:37,522 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 04:03:37,522 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 04:03:43,008 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 04:03:43,747 - market_scanner_v2 - INFO - âœ… Fetched 126 markets from API
2025-11-04 04:03:43,749 - market_scanner_v2 - INFO - âœ… Got 126 markets from API
2025-11-04 04:03:43,750 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 126/126 markets passed
2025-11-04 04:03:43,750 - market_scanner_v2 - INFO - âœ… Found 126 qualifying markets (from 126 total)
2025-11-04 04:03:43,752 - market_selector - INFO - Selected 7 markets from 126 candidates
2025-11-04 04:03:44,035 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:03:44,037 - order_manager - WARNING - Could not fetch data for market 663864
2025-11-04 04:03:44,037 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 04:03:44,323 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:03:44,324 - order_manager - WARNING - Could not fetch data for market 663860
2025-11-04 04:03:44,324 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 04:03:44,600 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:03:44,601 - order_manager - WARNING - Could not fetch data for market 663862
2025-11-04 04:03:44,601 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 04:03:44,893 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:03:44,893 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 04:03:44,894 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 04:03:45,164 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:03:45,165 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 04:03:45,165 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 04:03:45,444 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:03:45,444 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 04:03:45,444 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 04:03:45,747 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:03:45,748 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 04:03:45,748 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 04:03:49,973 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 04:03:50,678 - market_scanner_v2 - INFO - âœ… Fetched 126 markets from API
2025-11-04 04:03:50,680 - market_scanner_v2 - INFO - âœ… Got 126 markets from API
2025-11-04 04:03:50,681 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 126/126 markets passed
2025-11-04 04:03:50,682 - market_scanner_v2 - INFO - âœ… Found 126 qualifying markets (from 126 total)
2025-11-04 04:03:50,684 - market_selector - INFO - Selected 7 markets from 126 candidates
2025-11-04 04:03:50,959 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:03:50,960 - order_manager - WARNING - Could not fetch data for market 663864
2025-11-04 04:03:50,960 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 04:03:51,232 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:03:51,233 - order_manager - WARNING - Could not fetch data for market 663860
2025-11-04 04:03:51,233 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 04:03:51,511 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:03:51,512 - order_manager - WARNING - Could not fetch data for market 663862
2025-11-04 04:03:51,512 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 04:03:51,823 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:03:51,823 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 04:03:51,823 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 04:03:52,130 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:03:52,131 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 04:03:52,131 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 04:03:52,425 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:03:52,426 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 04:03:52,427 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 04:03:52,713 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:03:52,714 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 04:03:52,714 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 04:03:57,300 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 04:03:58,009 - market_scanner_v2 - INFO - âœ… Fetched 126 markets from API
2025-11-04 04:03:58,011 - market_scanner_v2 - INFO - âœ… Got 126 markets from API
2025-11-04 04:03:58,012 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 126/126 markets passed
2025-11-04 04:03:58,012 - market_scanner_v2 - INFO - âœ… Found 126 qualifying markets (from 126 total)
2025-11-04 04:03:58,015 - market_selector - INFO - Selected 7 markets from 126 candidates
2025-11-04 04:03:58,299 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:03:58,299 - order_manager - WARNING - Could not fetch data for market 663864
2025-11-04 04:03:58,300 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 04:03:58,594 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:03:58,595 - order_manager - WARNING - Could not fetch data for market 663860
2025-11-04 04:03:58,595 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 04:03:58,908 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:03:58,909 - order_manager - WARNING - Could not fetch data for market 663862
2025-11-04 04:03:58,909 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 04:03:59,188 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:03:59,188 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 04:03:59,189 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 04:03:59,469 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:03:59,470 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 04:03:59,470 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 04:03:59,742 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:03:59,743 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 04:03:59,743 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 04:04:00,022 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:04:00,023 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 04:04:00,023 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 04:04:05,737 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 04:04:06,439 - market_scanner_v2 - INFO - âœ… Fetched 126 markets from API
2025-11-04 04:04:06,441 - market_scanner_v2 - INFO - âœ… Got 126 markets from API
2025-11-04 04:04:06,443 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 126/126 markets passed
2025-11-04 04:04:06,443 - market_scanner_v2 - INFO - âœ… Found 126 qualifying markets (from 126 total)
2025-11-04 04:04:06,444 - market_selector - INFO - Selected 7 markets from 126 candidates
2025-11-04 04:04:06,705 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:04:06,705 - order_manager - WARNING - Could not fetch data for market 663864
2025-11-04 04:04:06,705 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 04:04:07,033 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:04:07,034 - order_manager - WARNING - Could not fetch data for market 663860
2025-11-04 04:04:07,035 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 04:04:07,308 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:04:07,309 - order_manager - WARNING - Could not fetch data for market 663862
2025-11-04 04:04:07,309 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 04:04:07,598 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:04:07,600 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 04:04:07,600 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 04:04:07,898 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:04:07,900 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 04:04:07,900 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 04:04:08,186 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:04:08,187 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 04:04:08,187 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 04:04:08,517 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:04:08,519 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 04:04:08,519 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 04:04:14,426 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 04:04:15,129 - market_scanner_v2 - INFO - âœ… Fetched 126 markets from API
2025-11-04 04:04:15,132 - market_scanner_v2 - INFO - âœ… Got 126 markets from API
2025-11-04 04:04:15,133 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 126/126 markets passed
2025-11-04 04:04:15,133 - market_scanner_v2 - INFO - âœ… Found 126 qualifying markets (from 126 total)
2025-11-04 04:04:15,135 - market_selector - INFO - Selected 7 markets from 126 candidates
2025-11-04 04:04:15,404 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:04:15,405 - order_manager - WARNING - Could not fetch data for market 663864
2025-11-04 04:04:15,405 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 04:04:15,692 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:04:15,692 - order_manager - WARNING - Could not fetch data for market 663860
2025-11-04 04:04:15,692 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 04:04:15,984 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:04:15,985 - order_manager - WARNING - Could not fetch data for market 663862
2025-11-04 04:04:15,985 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 04:04:16,289 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:04:16,290 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 04:04:16,290 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 04:04:16,692 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:04:16,693 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 04:04:16,693 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 04:04:17,026 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:04:17,027 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 04:04:17,027 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 04:04:17,329 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:04:17,331 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 04:04:17,331 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 04:04:22,708 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 04:04:23,418 - market_scanner_v2 - INFO - âœ… Fetched 126 markets from API
2025-11-04 04:04:23,424 - market_scanner_v2 - INFO - âœ… Got 126 markets from API
2025-11-04 04:04:23,425 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 126/126 markets passed
2025-11-04 04:04:23,425 - market_scanner_v2 - INFO - âœ… Found 126 qualifying markets (from 126 total)
2025-11-04 04:04:23,427 - market_selector - INFO - Selected 7 markets from 126 candidates
2025-11-04 04:04:23,741 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:04:23,742 - order_manager - WARNING - Could not fetch data for market 663864
2025-11-04 04:04:23,742 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 04:04:24,042 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:04:24,043 - order_manager - WARNING - Could not fetch data for market 663860
2025-11-04 04:04:24,043 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 04:04:24,315 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:04:24,316 - order_manager - WARNING - Could not fetch data for market 663862
2025-11-04 04:04:24,316 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 04:04:24,587 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:04:24,587 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 04:04:24,587 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 04:04:24,862 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:04:24,862 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 04:04:24,862 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 04:04:25,153 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:04:25,153 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 04:04:25,153 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 04:04:25,449 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:04:25,450 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 04:04:25,450 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 04:04:30,368 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 04:04:31,083 - market_scanner_v2 - INFO - âœ… Fetched 126 markets from API
2025-11-04 04:04:31,086 - market_scanner_v2 - INFO - âœ… Got 126 markets from API
2025-11-04 04:04:31,087 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 126/126 markets passed
2025-11-04 04:04:31,087 - market_scanner_v2 - INFO - âœ… Found 126 qualifying markets (from 126 total)
2025-11-04 04:04:31,089 - market_selector - INFO - Selected 7 markets from 126 candidates
2025-11-04 04:04:31,398 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:04:31,398 - order_manager - WARNING - Could not fetch data for market 663864
2025-11-04 04:04:31,399 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 04:04:31,738 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:04:31,738 - order_manager - WARNING - Could not fetch data for market 663860
2025-11-04 04:04:31,739 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 04:04:32,012 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:04:32,012 - order_manager - WARNING - Could not fetch data for market 663862
2025-11-04 04:04:32,013 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 04:04:32,312 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:04:32,312 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 04:04:32,312 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 04:04:32,607 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:04:32,607 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 04:04:32,607 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 04:04:32,885 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:04:32,886 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 04:04:32,886 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 04:04:33,180 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:04:33,181 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 04:04:33,181 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 04:04:38,429 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 04:04:39,149 - market_scanner_v2 - INFO - âœ… Fetched 126 markets from API
2025-11-04 04:04:39,153 - market_scanner_v2 - INFO - âœ… Got 126 markets from API
2025-11-04 04:04:39,153 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 126/126 markets passed
2025-11-04 04:04:39,154 - market_scanner_v2 - INFO - âœ… Found 126 qualifying markets (from 126 total)
2025-11-04 04:04:39,155 - market_selector - INFO - Selected 7 markets from 126 candidates
2025-11-04 04:04:39,461 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:04:39,461 - order_manager - WARNING - Could not fetch data for market 663864
2025-11-04 04:04:39,462 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 04:04:39,725 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:04:39,726 - order_manager - WARNING - Could not fetch data for market 663860
2025-11-04 04:04:39,726 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 04:04:40,002 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:04:40,002 - order_manager - WARNING - Could not fetch data for market 663862
2025-11-04 04:04:40,002 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 04:04:40,284 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:04:40,285 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 04:04:40,285 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 04:04:40,564 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:04:40,565 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 04:04:40,566 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 04:04:40,851 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:04:40,852 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 04:04:40,852 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 04:04:41,120 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:04:41,121 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 04:04:41,121 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 04:04:45,401 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 04:04:46,108 - market_scanner_v2 - INFO - âœ… Fetched 126 markets from API
2025-11-04 04:04:46,111 - market_scanner_v2 - INFO - âœ… Got 126 markets from API
2025-11-04 04:04:46,112 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 126/126 markets passed
2025-11-04 04:04:46,112 - market_scanner_v2 - INFO - âœ… Found 126 qualifying markets (from 126 total)
2025-11-04 04:04:46,116 - market_selector - INFO - Selected 7 markets from 126 candidates
2025-11-04 04:04:46,402 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:04:46,403 - order_manager - WARNING - Could not fetch data for market 663864
2025-11-04 04:04:46,403 - __main__ - INFO - Added market 663864 to pending orders
2025-11-04 04:04:46,678 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:04:46,679 - order_manager - WARNING - Could not fetch data for market 663860
2025-11-04 04:04:46,679 - __main__ - INFO - Added market 663860 to pending orders
2025-11-04 04:04:46,960 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:04:46,961 - order_manager - WARNING - Could not fetch data for market 663862
2025-11-04 04:04:46,961 - __main__ - INFO - Added market 663862 to pending orders
2025-11-04 04:04:47,269 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:04:47,270 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 04:04:47,270 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 04:04:47,549 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:04:47,549 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 04:04:47,549 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 04:04:47,858 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:04:47,858 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 04:04:47,858 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 04:04:48,162 - order_manager - ERROR - Error fetching market data: 'OrderBookSummary' object is not subscriptable
2025-11-04 04:04:48,164 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 04:04:48,164 - __main__ - INFO - Added market 663895 to pending orders
