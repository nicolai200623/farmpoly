2025-11-04 02:50:27,596 - __main__ - INFO - âœ… Using MarketScannerV2 (Playwright + Gamma API)
2025-11-04 02:50:34,030 - __main__ - ERROR - Failed to load config: while parsing a block mapping
  in "config.yaml", line 50, column 3
expected <block end>, but found '<block mapping start>'
  in "config.yaml", line 54, column 4
2025-11-04 02:50:34,031 - circuit_breaker - INFO - âœ… Circuit Breaker 'gamma_api' initialized (threshold=5, timeout=60s)
2025-11-04 02:50:34,031 - circuit_breaker - INFO - âœ… Circuit Breaker 'playwright_scraper' initialized (threshold=3, timeout=120s)
2025-11-04 02:50:34,031 - order_manager - INFO - CLOB client initialized successfully (read-only mode)
2025-11-04 02:50:34,045 - wallet_manager - INFO - Loading REAL wallets from .env
2025-11-04 02:50:34,053 - wallet_manager - INFO - âœ… Loaded wallet 1: 0x18F261DC...Ae4FfD96
2025-11-04 02:50:34,053 - wallet_manager - INFO - âœ… Successfully loaded 1 real wallets
2025-11-04 02:50:34,073 - ml_predictor - INFO - No pre-trained model found, using new model
2025-11-04 02:50:34,073 - monitoring_system - INFO - âœ… Monitoring System initialized
2025-11-04 02:50:34,073 - __main__ - INFO - âœ… Monitoring System enabled
2025-11-04 02:50:34,087 - reward_manager - INFO - âœ… Reward Manager initialized
2025-11-04 02:50:34,087 - reward_manager - INFO -    Check interval: 3600s (1.0h)
2025-11-04 02:50:34,087 - reward_manager - INFO -    Min withdrawal threshold: $10.00
2025-11-04 02:50:34,087 - reward_manager - WARNING - âš ï¸  No withdrawal wallet configured!
2025-11-04 02:50:34,087 - __main__ - INFO - âœ… Reward Manager enabled
2025-11-04 02:50:34,087 - __main__ - INFO - All modules initialized successfully
2025-11-04 02:50:34,087 - __main__ - INFO - ðŸš€ Starting Polymarket Trading Bot...
2025-11-04 02:50:34,087 - ml_predictor - INFO - Alert sent: ðŸš€ <b>Polymarket Bot Started</b>
â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”
â° Time: 2025-11-04 02:50:34
ðŸ’¼ Wallets: 1
ðŸ“Š Status: Running
â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”
Bot is now scanning markets and placing orders.
2025-11-04 02:50:34,087 - __main__ - INFO - âœ… Startup alert sent
2025-11-04 02:50:34,087 - __main__ - INFO - ðŸ” Checking USDC approval for wallets...
2025-11-04 02:50:34,245 - usdc_approver - INFO - âœ… Connected to Polygon RPC: https://polygon-mainnet.g.alchemy.com/v2/FQJnJWsEQ...
2025-11-04 02:50:34,245 - __main__ - INFO -    Checking wallet: 0x18F261DC...Ae4FfD96
2025-11-04 02:50:34,390 - __main__ - INFO -    Raw allowance: 100000000 (base units)
2025-11-04 02:50:34,390 - __main__ - INFO -    Allowance in USDC: 100.00 USDC
2025-11-04 02:50:34,390 - __main__ - INFO -    Required minimum: 100 USDC (test mode)
2025-11-04 02:50:34,390 - __main__ - INFO - âœ… USDC approval OK (100 USDC)
2025-11-04 02:50:34,390 - __main__ - WARNING -    âš ï¸  Running in TEST MODE with 100 USDC
2025-11-04 02:50:34,390 - __main__ - WARNING -    For production, approve at least 1,000 USDC
2025-11-04 02:50:34,391 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:50:34,391 - ml_predictor - INFO - Insufficient training data: 0 samples
2025-11-04 02:50:34,391 - __main__ - INFO - ML model updated successfully
2025-11-04 02:50:35,521 - reward_manager - INFO - âœ… Reward Manager async resources initialized
2025-11-04 02:50:35,521 - __main__ - INFO - ðŸŽ Starting automated reward management loop
2025-11-04 02:50:35,521 - reward_manager - INFO - ðŸ”„ Starting automatic reward withdrawal loop
2025-11-04 02:50:35,521 - reward_manager - INFO - ðŸ” Checking rewards...
2025-11-04 02:50:36,027 - reward_manager - WARNING - âš ï¸  Could not fetch rewards from any API endpoint for 0x18F261DC...
2025-11-04 02:50:36,027 - reward_manager - WARNING -    This is normal if Polymarket doesn't have a public rewards API
2025-11-04 02:50:36,027 - reward_manager - WARNING -    Rewards will be set to $0 (will NOT withdraw wallet balance)
2025-11-04 02:50:36,027 - reward_manager - INFO - ðŸ’° Total ACTUAL rewards across 1 wallets: $0.00 USDC
2025-11-04 02:50:36,027 - reward_manager - INFO - ðŸ“Š Reward Manager Statistics:
2025-11-04 02:50:36,028 - reward_manager - INFO -    Total checks: 1
2025-11-04 02:50:36,028 - reward_manager - INFO -    Total withdrawals: 0
2025-11-04 02:50:36,028 - reward_manager - INFO -    Total withdrawn: $0.00 USDC
2025-11-04 02:50:36,028 - reward_manager - INFO -    Failed withdrawals: 0
2025-11-04 02:50:36,028 - reward_manager - INFO -    Check errors: 0
2025-11-04 02:50:36,028 - reward_manager - INFO - â° Next reward check in 3600s (1.0h)
2025-11-04 02:50:36,229 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:50:36,231 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:50:36,231 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:50:36,231 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:50:36,231 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:50:36,232 - market_selector - INFO - Selected 0 markets from 36 candidates
2025-11-04 02:50:41,014 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:50:41,976 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:50:41,978 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:50:41,979 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:50:41,979 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:50:41,979 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:50:41,980 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:50:42,263 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:50:42,266 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:50:42,267 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:50:42,565 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:50:42,568 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:50:42,569 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:50:42,857 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:50:42,860 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:50:42,862 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:50:43,144 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:50:43,148 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:50:43,148 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:50:48,303 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:50:49,064 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:50:49,066 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:50:49,067 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:50:49,067 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:50:49,067 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:50:49,067 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:50:49,447 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:50:49,449 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:50:49,449 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:50:49,719 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:50:49,721 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:50:49,722 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:50:49,995 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:50:49,996 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:50:49,997 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:50:50,285 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:50:50,287 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:50:50,287 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:50:54,306 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:50:55,052 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:50:55,056 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:50:55,057 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:50:55,057 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:50:55,057 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:50:55,058 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:50:55,340 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:50:55,342 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:50:55,342 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:50:55,637 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:50:55,639 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:50:55,639 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:50:55,923 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:50:55,925 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:50:55,926 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:50:56,214 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:50:56,216 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:50:56,216 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:51:00,826 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:51:01,529 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:51:01,531 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:51:01,532 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:51:01,532 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:51:01,532 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:51:01,533 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:51:01,823 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:51:01,824 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:51:01,825 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:51:02,097 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:51:02,099 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:51:02,099 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:51:02,401 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:51:02,404 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:51:02,406 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:51:02,700 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:51:02,703 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:51:02,703 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:51:06,787 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:51:07,580 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:51:07,582 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:51:07,583 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:51:07,583 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:51:07,583 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:51:07,584 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:51:07,883 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:51:07,887 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:51:07,887 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:51:08,167 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:51:08,171 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:51:08,172 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:51:08,464 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:51:08,467 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:51:08,467 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:51:08,778 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:51:08,782 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:51:08,782 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:51:13,536 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:51:14,320 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:51:14,323 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:51:14,324 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:51:14,324 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:51:14,324 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:51:14,325 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:51:14,601 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:51:14,604 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:51:14,604 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:51:14,869 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:51:14,871 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:51:14,872 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:51:15,176 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:51:15,179 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:51:15,179 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:51:15,467 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:51:15,469 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:51:15,469 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:51:21,162 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:51:21,909 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:51:21,912 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:51:21,913 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:51:21,913 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:51:21,913 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:51:21,914 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:51:22,198 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:51:22,201 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:51:22,202 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:51:22,510 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:51:22,514 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:51:22,514 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:51:22,816 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:51:22,819 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:51:22,819 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:51:23,131 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:51:23,133 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:51:23,134 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:51:28,578 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:51:29,365 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:51:29,368 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:51:29,369 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:51:29,369 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:51:29,369 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:51:29,370 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:51:29,665 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:51:29,668 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:51:29,668 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:51:29,958 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:51:29,960 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:51:29,961 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:51:30,262 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:51:30,264 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:51:30,264 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:51:30,545 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:51:30,547 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:51:30,547 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:51:35,123 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:51:35,868 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:51:35,871 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:51:35,872 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:51:35,873 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:51:35,873 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:51:35,874 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:51:36,164 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:51:36,167 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:51:36,168 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:51:36,441 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:51:36,445 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:51:36,448 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:51:36,721 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:51:36,723 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:51:36,724 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:51:37,010 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:51:37,012 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:51:37,012 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:51:42,336 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:51:43,031 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:51:43,033 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:51:43,034 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:51:43,034 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:51:43,034 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:51:43,035 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:51:43,323 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:51:43,325 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:51:43,325 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:51:43,620 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:51:43,622 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:51:43,622 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:51:43,893 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:51:43,895 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:51:43,896 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:51:44,177 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:51:44,179 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:51:44,180 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:51:49,780 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:51:50,492 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:51:50,495 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:51:50,496 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:51:50,496 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:51:50,496 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:51:50,497 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:51:50,792 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:51:50,794 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:51:50,794 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:51:51,108 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:51:51,111 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:51:51,111 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:51:51,379 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:51:51,381 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:51:51,382 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:51:51,663 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:51:51,666 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:51:51,667 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:51:55,716 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:51:56,423 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:51:56,425 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:51:56,426 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:51:56,426 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:51:56,426 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:51:56,427 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:51:56,712 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:51:56,714 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:51:56,715 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:51:56,981 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:51:56,983 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:51:56,984 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:51:57,255 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:51:57,257 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:51:57,258 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:51:57,571 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:51:57,573 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:51:57,574 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:52:02,488 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:52:03,196 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:52:03,200 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:52:03,201 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:52:03,201 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:52:03,201 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:52:03,202 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:52:03,488 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:52:03,491 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:52:03,492 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:52:03,795 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:52:03,797 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:52:03,798 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:52:04,090 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:52:04,093 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:52:04,094 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:52:04,375 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:52:04,384 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:52:04,385 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:52:09,020 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:52:09,763 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:52:09,765 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:52:09,766 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:52:09,766 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:52:09,766 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:52:09,767 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:52:10,035 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:52:10,037 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:52:10,038 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:52:10,348 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:52:10,351 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:52:10,351 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:52:10,631 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:52:10,633 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:52:10,634 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:52:10,924 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:52:10,927 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:52:10,927 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:52:15,849 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:52:16,630 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:52:16,634 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:52:16,635 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:52:16,635 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:52:16,635 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:52:16,636 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:52:16,916 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:52:16,920 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:52:16,921 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:52:17,231 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:52:17,234 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:52:17,234 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:52:17,526 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:52:17,529 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:52:17,530 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:52:17,841 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:52:17,844 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:52:17,844 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:52:22,055 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:52:22,822 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:52:22,825 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:52:22,826 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:52:22,826 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:52:22,826 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:52:22,827 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:52:23,105 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:52:23,109 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:52:23,109 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:52:23,391 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:52:23,394 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:52:23,395 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:52:23,670 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:52:23,672 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:52:23,673 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:52:23,956 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:52:23,958 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:52:23,958 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:52:29,503 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:52:30,265 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:52:30,268 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:52:30,270 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:52:30,270 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:52:30,270 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:52:30,271 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:52:30,570 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:52:30,572 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:52:30,573 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:52:30,848 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:52:30,850 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:52:30,850 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:52:31,128 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:52:31,130 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:52:31,131 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:52:31,437 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:52:31,439 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:52:31,440 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:52:35,565 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:52:36,292 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:52:36,295 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:52:36,296 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:52:36,296 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:52:36,296 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:52:36,296 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:52:36,569 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:52:36,571 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:52:36,572 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:52:36,850 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:52:36,852 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:52:36,853 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:52:37,132 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:52:37,134 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:52:37,135 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:52:37,435 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:52:37,437 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:52:37,439 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:52:42,905 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:52:43,660 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:52:43,663 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:52:43,664 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:52:43,665 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:52:43,665 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:52:43,666 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:52:43,958 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:52:43,960 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:52:43,960 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:52:44,242 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:52:44,245 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:52:44,245 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:52:44,531 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:52:44,538 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:52:44,539 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:52:44,852 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:52:44,854 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:52:44,854 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:52:49,253 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:52:49,970 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:52:49,973 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:52:49,975 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:52:49,975 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:52:49,975 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:52:49,976 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:52:50,279 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:52:50,282 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:52:50,282 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:52:50,551 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:52:50,553 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:52:50,554 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:52:50,842 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:52:50,844 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:52:50,845 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:52:51,124 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:52:51,127 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:52:51,128 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:52:56,093 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:52:56,901 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:52:56,904 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:52:56,905 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:52:56,905 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:52:56,905 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:52:56,907 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:52:57,194 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:52:57,197 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:52:57,197 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:52:57,465 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:52:57,468 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:52:57,469 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:52:57,750 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:52:57,752 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:52:57,753 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:52:58,204 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:52:58,206 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:52:58,207 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:53:02,604 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:53:03,314 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:53:03,316 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:53:03,316 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:53:03,317 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:53:03,317 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:53:03,317 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:53:03,630 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:53:03,632 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:53:03,632 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:53:03,907 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:53:03,909 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:53:03,910 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:53:04,210 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:53:04,212 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:53:04,212 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:53:04,493 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:53:04,495 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:53:04,495 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:53:09,335 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:53:11,046 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:53:11,048 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:53:11,049 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:53:11,049 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:53:11,049 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:53:11,049 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:53:11,322 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:53:11,324 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:53:11,324 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:53:11,620 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:53:11,622 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:53:11,623 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:53:11,904 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:53:11,906 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:53:11,907 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:53:12,196 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:53:12,199 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:53:12,199 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:53:16,724 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:53:17,453 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:53:17,456 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:53:17,457 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:53:17,457 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:53:17,457 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:53:17,458 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:53:17,771 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:53:17,773 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:53:17,774 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:53:18,073 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:53:18,075 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:53:18,076 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:53:18,357 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:53:18,359 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:53:18,360 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:53:18,647 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:53:18,649 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:53:18,649 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:53:24,397 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:53:25,182 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:53:25,185 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:53:25,186 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:53:25,186 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:53:25,186 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:53:25,187 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:53:25,473 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:53:25,475 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:53:25,475 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:53:25,746 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:53:25,748 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:53:25,749 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:53:26,043 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:53:26,044 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:53:26,045 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:53:26,342 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:53:26,344 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:53:26,345 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:53:31,561 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:53:32,291 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:53:32,293 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:53:32,294 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:53:32,294 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:53:32,294 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:53:32,295 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:53:32,566 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:53:32,569 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:53:32,570 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:53:32,855 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:53:32,857 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:53:32,858 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:53:33,123 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:53:33,125 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:53:33,125 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:53:33,400 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:53:33,403 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:53:33,403 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:53:39,220 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:53:39,941 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:53:39,943 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:53:39,944 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:53:39,944 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:53:39,944 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:53:39,945 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:53:40,206 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:53:40,208 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:53:40,208 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:53:40,482 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:53:40,483 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:53:40,484 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:53:40,770 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:53:40,772 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:53:40,773 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:53:41,052 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:53:41,054 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:53:41,055 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:53:46,009 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:53:46,765 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:53:46,770 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:53:46,771 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:53:46,771 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:53:46,771 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:53:46,772 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:53:47,060 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:53:47,063 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:53:47,064 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:53:47,343 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:53:47,345 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:53:47,346 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:53:47,623 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:53:47,626 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:53:47,627 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:53:47,956 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:53:47,960 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:53:47,961 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:53:53,091 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:53:54,054 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:53:54,056 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:53:54,057 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:53:54,058 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:53:54,058 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:53:54,058 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:53:54,399 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:53:54,401 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:53:54,402 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:53:54,692 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:53:54,695 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:53:54,696 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:53:54,999 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:53:55,002 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:53:55,004 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:53:55,294 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:53:55,296 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:53:55,297 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:53:59,565 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:54:00,259 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:54:00,261 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:54:00,262 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:54:00,262 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:54:00,262 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:54:00,263 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:54:00,533 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:54:00,535 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:54:00,536 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:54:00,804 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:54:00,806 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:54:00,806 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:54:01,096 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:54:01,097 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:54:01,098 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:54:01,393 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:54:01,395 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:54:01,396 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:54:06,875 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:54:07,626 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:54:07,628 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:54:07,629 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:54:07,629 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:54:07,629 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:54:07,630 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:54:07,915 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:54:07,917 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:54:07,918 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:54:08,216 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:54:08,219 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:54:08,220 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:54:08,494 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:54:08,496 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:54:08,497 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:54:08,780 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:54:08,783 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:54:08,784 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:54:13,060 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:54:13,808 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:54:13,811 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:54:13,812 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:54:13,812 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:54:13,812 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:54:13,818 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:54:14,110 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:54:14,113 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:54:14,113 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:54:14,516 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:54:14,518 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:54:14,519 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:54:14,815 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:54:14,817 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:54:14,818 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:54:15,093 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:54:15,095 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:54:15,096 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:54:20,789 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:54:21,582 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:54:21,584 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:54:21,584 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:54:21,584 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:54:21,585 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:54:21,585 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:54:21,869 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:54:21,871 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:54:21,871 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:54:22,213 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:54:22,215 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:54:22,215 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:54:22,494 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:54:22,496 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:54:22,497 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:54:22,948 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:54:22,955 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:54:22,955 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:54:27,611 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:54:28,415 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:54:28,418 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:54:28,419 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:54:28,419 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:54:28,419 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:54:28,420 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:54:28,712 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:54:28,715 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:54:28,715 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:54:28,991 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:54:28,995 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:54:28,995 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:54:29,299 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:54:29,302 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:54:29,303 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:54:29,585 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:54:29,588 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:54:29,589 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:54:35,334 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:54:36,149 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:54:36,151 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:54:36,152 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:54:36,152 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:54:36,152 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:54:36,153 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:54:36,439 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:54:36,442 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:54:36,442 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:54:36,718 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:54:36,720 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:54:36,721 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:54:36,996 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:54:36,999 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:54:37,001 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:54:37,272 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:54:37,275 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:54:37,275 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:54:42,526 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:54:44,088 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:54:44,091 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:54:44,092 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:54:44,092 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:54:44,092 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:54:44,093 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:54:44,393 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:54:44,396 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:54:44,396 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:54:44,673 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:54:44,675 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:54:44,676 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:54:44,973 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:54:44,976 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:54:44,977 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:54:45,254 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:54:45,256 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:54:45,257 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:54:49,667 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:54:50,383 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:54:50,387 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:54:50,389 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:54:50,389 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:54:50,389 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:54:50,390 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:54:50,701 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:54:50,704 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:54:50,705 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:54:50,995 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:54:50,998 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:54:50,999 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:54:51,303 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:54:51,306 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:54:51,307 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:54:51,590 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:54:51,593 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:54:51,593 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:54:56,853 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:54:57,608 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:54:57,612 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:54:57,613 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:54:57,616 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:54:57,616 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:54:57,617 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:54:57,899 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:54:57,901 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:54:57,901 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:54:58,201 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:54:58,203 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:54:58,203 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:54:58,478 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:54:58,480 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:54:58,481 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:54:58,769 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:54:58,771 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:54:58,772 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:55:04,601 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:55:05,340 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:55:05,342 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:55:05,342 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:55:05,342 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:55:05,343 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:55:05,343 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:55:05,636 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:55:05,638 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:55:05,639 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:55:05,943 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:55:05,947 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:55:05,948 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:55:06,241 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:55:06,244 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:55:06,245 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:55:06,536 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:55:06,539 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:55:06,540 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:55:11,282 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:55:12,013 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:55:12,017 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:55:12,018 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:55:12,018 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:55:12,018 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:55:12,019 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:55:12,308 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:55:12,311 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:55:12,311 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:55:12,595 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:55:12,598 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:55:12,599 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:55:12,898 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:55:12,901 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:55:12,901 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:55:13,178 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:55:13,180 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:55:13,181 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:55:18,394 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:55:19,143 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:55:19,146 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:55:19,147 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:55:19,147 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:55:19,147 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:55:19,147 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:55:19,441 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:55:19,443 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:55:19,444 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:55:19,715 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:55:19,717 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:55:19,718 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:55:19,998 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:55:20,000 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:55:20,001 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:55:20,303 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:55:20,305 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:55:20,305 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:55:24,443 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:55:25,130 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:55:25,133 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:55:25,133 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:55:25,134 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:55:25,134 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:55:25,134 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:55:25,421 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:55:25,423 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:55:25,423 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:55:25,697 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:55:25,699 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:55:25,700 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:55:25,978 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:55:25,981 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:55:25,981 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:55:26,261 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:55:26,263 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:55:26,264 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:55:32,178 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:55:32,879 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:55:32,882 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:55:32,882 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:55:32,882 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:55:32,883 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:55:32,883 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:55:33,166 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:55:33,168 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:55:33,169 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:55:33,435 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:55:33,438 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:55:33,439 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:55:33,717 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:55:33,720 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:55:33,721 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:55:33,999 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:55:34,002 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:55:34,003 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:55:38,426 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:55:39,185 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:55:39,189 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:55:39,190 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:55:39,190 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:55:39,190 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:55:39,191 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:55:39,475 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:55:39,478 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:55:39,478 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:55:39,742 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:55:39,745 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:55:39,746 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:55:40,021 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:55:40,023 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:55:40,024 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:55:40,288 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:55:40,289 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:55:40,290 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:55:44,704 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:55:46,112 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:55:46,115 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:55:46,116 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:55:46,116 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:55:46,116 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:55:46,117 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:55:46,385 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:55:46,388 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:55:46,388 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:55:46,727 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:55:46,730 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:55:46,731 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:55:47,014 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:55:47,017 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:55:47,018 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:55:47,315 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:55:47,318 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:55:47,318 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:55:51,612 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:55:52,355 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:55:52,357 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:55:52,358 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:55:52,358 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:55:52,358 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:55:52,359 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:55:52,639 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:55:52,641 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:55:52,641 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:55:52,920 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:55:52,922 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:55:52,923 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:55:53,213 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:55:53,215 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:55:53,215 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:55:53,515 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:55:53,517 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:55:53,517 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:55:58,561 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:55:59,256 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:55:59,258 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:55:59,259 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:55:59,259 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:55:59,259 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:55:59,260 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:55:59,554 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:55:59,557 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:55:59,557 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:55:59,846 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:55:59,848 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:55:59,849 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:56:00,121 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:56:00,123 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:56:00,124 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:56:00,394 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:56:00,397 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:56:00,399 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:56:04,476 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:56:05,199 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:56:05,201 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:56:05,202 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:56:05,202 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:56:05,203 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:56:05,204 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:56:05,469 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:56:05,471 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:56:05,471 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:56:05,745 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:56:05,747 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:56:05,747 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:56:06,030 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:56:06,033 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:56:06,033 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:56:06,317 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:56:06,320 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:56:06,320 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:56:10,930 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:56:11,695 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:56:11,697 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:56:11,698 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:56:11,699 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:56:11,699 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:56:11,700 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:56:12,007 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:56:12,009 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:56:12,010 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:56:12,287 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:56:12,290 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:56:12,291 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:56:12,563 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:56:12,565 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:56:12,565 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:56:12,853 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:56:12,855 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:56:12,856 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:56:17,171 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:56:17,893 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:56:17,896 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:56:17,897 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:56:17,897 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:56:17,897 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:56:17,898 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:56:18,177 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:56:18,180 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:56:18,180 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:56:18,475 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:56:18,477 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:56:18,478 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:56:18,766 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:56:18,769 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:56:18,770 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:56:19,199 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:56:19,201 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:56:19,202 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:56:24,467 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:56:25,178 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:56:25,180 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:56:25,181 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:56:25,181 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:56:25,181 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:56:25,182 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:56:25,460 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:56:25,463 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:56:25,463 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:56:25,752 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:56:25,754 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:56:25,755 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:56:26,043 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:56:26,046 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:56:26,047 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:56:26,343 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:56:26,347 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:56:26,348 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:56:31,833 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:56:32,541 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:56:32,545 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:56:32,546 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:56:32,546 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:56:32,546 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:56:32,547 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:56:32,848 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:56:32,851 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:56:32,852 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:56:33,139 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:56:33,147 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:56:33,148 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:56:33,426 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:56:33,429 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:56:33,429 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:56:33,706 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:56:33,708 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:56:33,709 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:56:38,657 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:56:39,370 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:56:39,373 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:56:39,375 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:56:39,375 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:56:39,375 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:56:39,377 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:56:39,679 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:56:39,694 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:56:39,694 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:56:40,119 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:56:40,121 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:56:40,122 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:56:40,404 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:56:40,406 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:56:40,407 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:56:40,682 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:56:40,685 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:56:40,688 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:56:45,238 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:56:45,955 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:56:45,957 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:56:45,958 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:56:45,958 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:56:45,958 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:56:45,959 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:56:46,230 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:56:46,232 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:56:46,233 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:56:46,512 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:56:46,515 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:56:46,515 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:56:46,804 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:56:46,806 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:56:46,807 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:56:47,089 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:56:47,091 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:56:47,091 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:56:52,968 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:56:53,676 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:56:53,678 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:56:53,679 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:56:53,679 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:56:53,679 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:56:53,680 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:56:53,957 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:56:53,958 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:56:53,959 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:56:54,243 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:56:54,245 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:56:54,246 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:56:54,523 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:56:54,525 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:56:54,525 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:56:54,820 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:56:54,822 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:56:54,822 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:57:00,457 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:57:01,163 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:57:01,165 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:57:01,166 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:57:01,166 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:57:01,166 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:57:01,167 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:57:01,447 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:57:01,450 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:57:01,450 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:57:01,736 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:57:01,739 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:57:01,739 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:57:02,028 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:57:02,030 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:57:02,031 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:57:02,315 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:57:02,317 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:57:02,317 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:57:07,576 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:57:08,307 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:57:08,313 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:57:08,314 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:57:08,315 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:57:08,315 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:57:08,315 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:57:08,596 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:57:08,599 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:57:08,600 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:57:08,901 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:57:08,904 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:57:08,905 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:57:09,190 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:57:09,193 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:57:09,194 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:57:09,499 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:57:09,502 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:57:09,503 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:57:14,616 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:57:15,324 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:57:15,331 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:57:15,332 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:57:15,332 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:57:15,332 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:57:15,333 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:57:15,614 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:57:15,615 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:57:15,618 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:57:15,910 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:57:15,912 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:57:15,913 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:57:16,366 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:57:16,368 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:57:16,368 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:57:16,653 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:57:16,655 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:57:16,656 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:57:21,090 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:57:21,832 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:57:21,834 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:57:21,835 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:57:21,835 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:57:21,835 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:57:21,836 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:57:22,121 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:57:22,124 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:57:22,124 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:57:22,414 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:57:22,417 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:57:22,417 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:57:22,704 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:57:22,707 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:57:22,707 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:57:22,985 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:57:22,987 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:57:22,987 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:57:27,667 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:57:28,381 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:57:28,383 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:57:28,383 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:57:28,383 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:57:28,384 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:57:28,384 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:57:28,669 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:57:28,671 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:57:28,671 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:57:28,949 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:57:28,951 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:57:28,952 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:57:29,244 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:57:29,247 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:57:29,247 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:57:29,536 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:57:29,538 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:57:29,539 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:57:34,403 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:57:35,149 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:57:35,153 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:57:35,154 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:57:35,154 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:57:35,154 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:57:35,155 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:57:35,456 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:57:35,459 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:57:35,459 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:57:35,760 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:57:35,763 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:57:35,764 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:57:36,039 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:57:36,041 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:57:36,042 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:57:36,329 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:57:36,333 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:57:36,333 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:57:40,441 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:57:41,169 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:57:41,172 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:57:41,173 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:57:41,173 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:57:41,173 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:57:41,174 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:57:41,451 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:57:41,454 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:57:41,454 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:57:41,727 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:57:41,729 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:57:41,729 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:57:42,009 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:57:42,011 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:57:42,011 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:57:42,292 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:57:42,294 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:57:42,294 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:57:47,741 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:57:48,476 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:57:48,478 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:57:48,479 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:57:48,479 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:57:48,479 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:57:48,480 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:57:48,758 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:57:48,761 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:57:48,762 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:57:49,049 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:57:49,052 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:57:49,052 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:57:49,350 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:57:49,353 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:57:49,354 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:57:49,638 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:57:49,640 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:57:49,640 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:57:55,473 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:57:56,182 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:57:56,185 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:57:56,186 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:57:56,186 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:57:56,186 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:57:56,187 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:57:56,461 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:57:56,463 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:57:56,464 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:57:56,752 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:57:56,754 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:57:56,755 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:57:57,205 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:57:57,207 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:57:57,207 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:57:57,488 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:57:57,491 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:57:57,492 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:58:02,668 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:58:03,433 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:58:03,437 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:58:03,438 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:58:03,438 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:58:03,438 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:58:03,439 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:58:03,729 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:58:03,732 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:58:03,732 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:58:04,026 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:58:04,028 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:58:04,028 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:58:04,312 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:58:04,314 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:58:04,315 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:58:04,582 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:58:04,584 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:58:04,584 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:58:09,551 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:58:10,307 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:58:10,309 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:58:10,310 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:58:10,310 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:58:10,310 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:58:10,311 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:58:10,596 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:58:10,598 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:58:10,599 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:58:10,893 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:58:10,895 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:58:10,896 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:58:11,172 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:58:11,174 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:58:11,175 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:58:11,474 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:58:11,476 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:58:11,477 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:58:17,327 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:58:18,036 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:58:18,039 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:58:18,040 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:58:18,040 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:58:18,040 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:58:18,040 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:58:18,340 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:58:18,342 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:58:18,343 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:58:18,628 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:58:18,631 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:58:18,633 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:58:18,911 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:58:18,914 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:58:18,915 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:58:19,200 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:58:19,203 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:58:19,204 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:58:24,009 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:58:24,747 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:58:24,749 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:58:24,750 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:58:24,750 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:58:24,750 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:58:24,751 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:58:25,233 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:58:25,236 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:58:25,237 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:58:25,528 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:58:25,530 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:58:25,531 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:58:25,816 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:58:25,818 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:58:25,818 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:58:26,091 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:58:26,094 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:58:26,095 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:58:32,010 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:58:32,715 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:58:32,718 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:58:32,719 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:58:32,719 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:58:32,719 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:58:32,720 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:58:33,008 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:58:33,011 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:58:33,012 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:58:33,318 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:58:33,320 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:58:33,321 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:58:33,603 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:58:33,606 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:58:33,607 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:58:33,880 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:58:33,883 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:58:33,884 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:58:38,806 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:58:39,595 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:58:39,598 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:58:39,599 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:58:39,599 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:58:39,599 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:58:39,600 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:58:39,878 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:58:39,880 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:58:39,881 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:58:40,198 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:58:40,201 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:58:40,202 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:58:40,471 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:58:40,474 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:58:40,475 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:58:40,756 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:58:40,759 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:58:40,760 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:58:46,374 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:58:47,160 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:58:47,162 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:58:47,163 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:58:47,163 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:58:47,163 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:58:47,164 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:58:47,448 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:58:47,449 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:58:47,450 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:58:47,748 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:58:47,750 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:58:47,751 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:58:48,086 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:58:48,088 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:58:48,089 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:58:48,376 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:58:48,378 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:58:48,379 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:58:53,597 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:58:54,309 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:58:54,313 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:58:54,313 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:58:54,314 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:58:54,314 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:58:54,315 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:58:54,595 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:58:54,597 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:58:54,597 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:58:54,871 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:58:54,873 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:58:54,874 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:58:55,154 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:58:55,156 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:58:55,157 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:58:55,438 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:58:55,440 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:58:55,441 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:59:00,440 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:59:01,173 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:59:01,175 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:59:01,177 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:59:01,177 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:59:01,177 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:59:01,178 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:59:01,492 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:59:01,494 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:59:01,495 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:59:01,777 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:59:01,780 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:59:01,780 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:59:02,091 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:59:02,093 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:59:02,093 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:59:02,375 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:59:02,378 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:59:02,380 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:59:07,345 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:59:08,070 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:59:08,073 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:59:08,073 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:59:08,074 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:59:08,074 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:59:08,074 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:59:08,356 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:59:08,359 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:59:08,360 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:59:08,660 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:59:08,663 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:59:08,663 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:59:08,958 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:59:08,960 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:59:08,960 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:59:09,249 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:59:09,251 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:59:09,252 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:59:14,780 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:59:15,493 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:59:15,496 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:59:15,497 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:59:15,497 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:59:15,497 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:59:15,497 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:59:15,774 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:59:15,776 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:59:15,777 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:59:16,088 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:59:16,090 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:59:16,091 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:59:16,382 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:59:16,384 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:59:16,384 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:59:16,658 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:59:16,660 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:59:16,661 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:59:22,621 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:59:23,686 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:59:23,689 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:59:23,690 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:59:23,690 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:59:23,690 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:59:23,691 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:59:24,000 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:59:24,003 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:59:24,005 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:59:24,317 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:59:24,323 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:59:24,324 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:59:24,609 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:59:24,611 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:59:24,612 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:59:24,904 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:59:24,906 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:59:24,906 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:59:29,589 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:59:30,312 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:59:30,315 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:59:30,316 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:59:30,316 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:59:30,316 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:59:30,317 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:59:30,598 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:59:30,600 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:59:30,601 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:59:30,919 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:59:30,923 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:59:30,924 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:59:31,208 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:59:31,210 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:59:31,211 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:59:31,492 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:59:31,495 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:59:31,496 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:59:36,584 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:59:37,305 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:59:37,309 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:59:37,311 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:59:37,311 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:59:37,311 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:59:37,312 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:59:37,587 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:59:37,589 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:59:37,590 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:59:37,869 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:59:37,872 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:59:37,873 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:59:38,154 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:59:38,160 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:59:38,166 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:59:38,478 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:59:38,480 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:59:38,481 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:59:43,448 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:59:44,192 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:59:44,195 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:59:44,196 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:59:44,196 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:59:44,196 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:59:44,197 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:59:44,650 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:59:44,653 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:59:44,654 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:59:44,946 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:59:44,949 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:59:44,950 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:59:45,254 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:59:45,256 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:59:45,257 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:59:45,558 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:59:45,560 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:59:45,561 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:59:51,090 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:59:51,795 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:59:51,797 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:59:51,798 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:59:51,798 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:59:51,798 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:59:51,799 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:59:52,084 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:59:52,086 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:59:52,087 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:59:52,393 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:59:52,395 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:59:52,395 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 02:59:52,689 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:59:52,691 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 02:59:52,692 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 02:59:52,967 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:59:52,970 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 02:59:52,971 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 02:59:58,515 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 02:59:59,226 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 02:59:59,229 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 02:59:59,230 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 02:59:59,231 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 02:59:59,231 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 02:59:59,232 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 02:59:59,515 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:59:59,519 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 02:59:59,519 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 02:59:59,816 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 02:59:59,819 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 02:59:59,821 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 03:00:00,120 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 03:00:00,126 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 03:00:00,127 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 03:00:00,698 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 03:00:00,700 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 03:00:00,701 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 03:00:01,704 - ml_predictor - INFO - Alert sent: âœ… <b>Hourly Report</b>
â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”
â° Time: 2025-11-04 03:00:01

ðŸ“Š <b>Performance (Last 60 min)</b>
   â€¢ Scans: 82
   â€¢ Markets found: 2952 (36.0/scan)
   â€¢ Orders placed: 0
   â€¢ Orders filled: 0 (0.0%)
   â€¢ Profit: $0.00
   â€¢ Errors: 0 (0.0%)

ðŸ’» <b>System Health</b>
   â€¢ CPU: 7.0%
   â€¢ RAM: 66.1%
   â€¢ Bot RAM: 563 MB
        
â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”
2025-11-04 03:00:01,704 - monitoring_system - INFO - âœ… Hourly report sent
2025-11-04 03:00:06,657 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 03:00:07,454 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 03:00:07,457 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 03:00:07,466 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 03:00:07,466 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 03:00:07,466 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 03:00:07,467 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 03:00:07,909 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 03:00:07,911 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 03:00:07,911 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 03:00:08,368 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 03:00:08,370 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 03:00:08,371 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 03:00:08,861 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 03:00:08,863 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 03:00:08,863 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 03:00:09,314 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 03:00:09,316 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 03:00:09,316 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 03:00:14,350 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 03:00:15,116 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 03:00:15,123 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 03:00:15,124 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 03:00:15,124 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 03:00:15,124 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 03:00:15,125 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 03:00:15,591 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 03:00:15,593 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 03:00:15,593 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 03:00:16,079 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 03:00:16,081 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 03:00:16,081 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 03:00:16,516 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 03:00:16,518 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 03:00:16,519 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 03:00:16,967 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 03:00:16,969 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 03:00:16,974 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 03:00:22,078 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 03:00:22,856 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 03:00:22,859 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 03:00:22,859 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 03:00:22,859 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 03:00:22,859 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 03:00:22,860 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 03:00:23,146 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 03:00:23,149 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 03:00:23,150 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 03:00:23,429 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 03:00:23,432 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 03:00:23,432 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 03:00:23,715 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 03:00:23,718 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 03:00:23,719 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 03:00:24,016 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 03:00:24,018 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 03:00:24,019 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 03:00:29,018 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 03:00:29,730 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 03:00:29,733 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 03:00:29,734 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 03:00:29,734 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 03:00:29,734 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 03:00:29,735 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 03:00:30,048 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 03:00:30,051 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 03:00:30,051 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 03:00:30,356 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 03:00:30,359 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 03:00:30,360 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 03:00:30,645 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 03:00:30,648 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 03:00:30,650 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 03:00:30,953 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 03:00:30,956 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 03:00:30,957 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 03:00:36,290 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 03:00:37,000 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 03:00:37,009 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 03:00:37,010 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 03:00:37,010 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 03:00:37,010 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 03:00:37,011 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 03:00:37,315 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 03:00:37,318 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 03:00:37,318 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 03:00:37,616 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 03:00:37,618 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 03:00:37,619 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 03:00:37,890 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 03:00:37,892 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 03:00:37,893 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 03:00:38,178 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 03:00:38,180 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 03:00:38,180 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 03:00:44,039 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 03:00:44,797 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 03:00:44,800 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 03:00:44,801 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 03:00:44,801 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 03:00:44,801 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 03:00:44,802 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 03:00:45,079 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 03:00:45,082 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 03:00:45,082 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 03:00:45,351 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 03:00:45,353 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 03:00:45,355 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 03:00:45,659 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 03:00:45,662 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 03:00:45,663 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 03:00:45,953 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 03:00:45,956 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 03:00:45,957 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 03:00:50,360 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 03:00:51,072 - market_scanner_v2 - INFO - âœ… Fetched 142 markets from API
2025-11-04 03:00:51,074 - market_scanner_v2 - INFO - âœ… Got 142 markets from API
2025-11-04 03:00:51,074 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 36/142 markets passed
2025-11-04 03:00:51,074 - market_scanner_v2 - INFO -    - 106 rejected: reward < $300
2025-11-04 03:00:51,074 - market_scanner_v2 - INFO - âœ… Found 36 qualifying markets (from 142 total)
2025-11-04 03:00:51,075 - market_selector - INFO - Selected 4 markets from 36 candidates
2025-11-04 03:00:51,389 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 03:00:51,391 - order_manager - WARNING - Could not fetch data for market 663911
2025-11-04 03:00:51,392 - __main__ - INFO - Added market 663911 to pending orders
2025-11-04 03:00:51,660 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 03:00:51,662 - order_manager - WARNING - Could not fetch data for market 663891
2025-11-04 03:00:51,663 - __main__ - INFO - Added market 663891 to pending orders
2025-11-04 03:00:51,954 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 03:00:51,956 - order_manager - WARNING - Could not fetch data for market 663908
2025-11-04 03:00:51,957 - __main__ - INFO - Added market 663908 to pending orders
2025-11-04 03:00:52,234 - order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, error_message={'error': 'No orderbook exists for the requested token id'}]
2025-11-04 03:00:52,236 - order_manager - WARNING - Could not fetch data for market 663895
2025-11-04 03:00:52,237 - __main__ - INFO - Added market 663895 to pending orders
2025-11-04 03:00:57,966 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
