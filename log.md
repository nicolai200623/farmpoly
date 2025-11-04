2025-11-04 08:10:01,133 - __main__ - INFO - âœ… Using MarketScannerV2 (Playwright + Gamma API)
2025-11-04 08:10:07,332 - __main__ - INFO - âœ… Telegram alerts configured (Chat ID: -1003157421030)
2025-11-04 08:10:07,333 - __main__ - INFO - âœ… Webhook alerts configured
2025-11-04 08:10:07,333 - circuit_breaker - INFO - âœ… Circuit Breaker 'gamma_api' initialized (threshold=5, timeout=60s)
2025-11-04 08:10:07,333 - circuit_breaker - INFO - âœ… Circuit Breaker 'playwright_scraper' initialized (threshold=3, timeout=120s)
2025-11-04 08:10:07,333 - order_manager - INFO - CLOB client initialized successfully (read-only mode)
2025-11-04 08:10:07,341 - wallet_manager - INFO - Loading REAL wallets from .env
2025-11-04 08:10:07,347 - wallet_manager - INFO - âœ… Loaded wallet 1: 0x18F261DC...Ae4FfD96
2025-11-04 08:10:07,347 - wallet_manager - INFO - âœ… Successfully loaded 1 real wallets
2025-11-04 08:10:07,374 - ml_predictor - INFO - No pre-trained model found, using new model
2025-11-04 08:10:07,374 - monitoring_system - INFO - âœ… Monitoring System initialized
2025-11-04 08:10:07,374 - __main__ - INFO - âœ… Monitoring System enabled
2025-11-04 08:10:07,374 - __main__ - INFO - â­ï¸  Reward Manager disabled in config
2025-11-04 08:10:07,374 - __main__ - INFO - All modules initialized successfully
2025-11-04 08:10:07,374 - __main__ - INFO - ðŸš€ Starting Polymarket Trading Bot...
2025-11-04 08:10:08,349 - ml_predictor - INFO - Alert sent: ðŸš€ <b>Polymarket Bot Started</b>
â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”
â° Time: 2025-11-04 08:10:07
ðŸ’¼ Wallets: 1
ðŸ“Š Status: Running
â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”
Bot is now scanning markets and placing orders.
2025-11-04 08:10:08,350 - __main__ - INFO - âœ… Startup alert sent
2025-11-04 08:10:08,350 - __main__ - INFO - ðŸ” Checking USDC approval for wallets...
2025-11-04 08:10:08,562 - usdc_approver - INFO - âœ… Connected to Polygon RPC: https://polygon-mainnet.g.alchemy.com/v2/FQJnJWsEQ...
2025-11-04 08:10:08,562 - __main__ - INFO -    Checking wallet: 0x18F261DC...Ae4FfD96
2025-11-04 08:10:08,946 - __main__ - INFO -    Raw allowance: 100000000 (base units)
2025-11-04 08:10:08,946 - __main__ - INFO -    Allowance in USDC: 100.00 USDC
2025-11-04 08:10:08,947 - __main__ - INFO -    Required minimum: 100 USDC (test mode)
2025-11-04 08:10:08,947 - __main__ - INFO - âœ… USDC approval OK (100 USDC)
2025-11-04 08:10:08,947 - __main__ - WARNING -    âš ï¸  Running in TEST MODE with 100 USDC
2025-11-04 08:10:08,947 - __main__ - WARNING -    For production, approve at least 1,000 USDC
2025-11-04 08:10:08,947 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 08:10:08,948 - ml_predictor - INFO - Insufficient training data: 0 samples
2025-11-04 08:10:08,948 - __main__ - INFO - ML model updated successfully
2025-11-04 08:10:10,958 - market_scanner_v2 - INFO - âœ… Fetched 300 markets from API
2025-11-04 08:10:10,960 - market_scanner_v2 - INFO - âœ… Got 300 markets from API
2025-11-04 08:10:10,962 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 300/300 markets passed
2025-11-04 08:10:10,962 - market_scanner_v2 - INFO - âœ… Found 300 qualifying markets (from 300 total)
2025-11-04 08:10:10,964 - market_selector - INFO - Selected 3 markets from 300 candidates
2025-11-04 08:10:11,293 - order_manager - INFO - Prepared order for market 664453 with spread 0.0120
2025-11-04 08:10:11,293 - order_manager - INFO - Added order to pending queue: 664453
2025-11-04 08:10:11,293 - __main__ - INFO - Added market 664453 to pending orders
2025-11-04 08:10:11,642 - order_manager - INFO - Prepared order for market 664438 with spread 0.0120
2025-11-04 08:10:11,642 - order_manager - INFO - Added order to pending queue: 664438
2025-11-04 08:10:11,643 - __main__ - INFO - Added market 664438 to pending orders
2025-11-04 08:10:11,987 - order_manager - INFO - Prepared order for market 664299 with spread 0.0120
2025-11-04 08:10:11,987 - order_manager - INFO - Added order to pending queue: 664299
2025-11-04 08:10:11,988 - __main__ - INFO - Added market 664299 to pending orders
2025-11-04 08:10:14,203 - order_manager - INFO - Order placed successfully: 0x3aade4c80e20e314e8dcdbe370c55ccccc85cfb1ada4270646b9de63e8857f5e
2025-11-04 08:10:17,685 - order_manager - INFO - Order placed successfully: 0x745d87fde2ee23eda7894bd05039a841b35482f5696710356e57fba17fc4c9bd
2025-11-04 08:10:17,685 - order_manager - INFO - Placed orders for market 664453: {'yes': '0x3aade4c80e20e314e8dcdbe370c55ccccc85cfb1ada4270646b9de63e8857f5e', 'no': '0x745d87fde2ee23eda7894bd05039a841b35482f5696710356e57fba17fc4c9bd'}
2025-11-04 08:10:19,748 - order_manager - INFO - Order placed successfully: 0x3f7f49156165bca0e092ac703f74a01ac815f6fbb7ccb29fde37cdca6e497afa
2025-11-04 08:10:19,748 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 08:10:20,787 - market_scanner_v2 - INFO - âœ… Fetched 300 markets from API
2025-11-04 08:10:22,843 - order_manager - INFO - Order placed successfully: 0x8f4f1e08871f4d9d537a3291cac52b6128cd4f29610e7fda32120b0c827e3f60
2025-11-04 08:10:22,843 - order_manager - INFO - Placed orders for market 664438: {'yes': '0x3f7f49156165bca0e092ac703f74a01ac815f6fbb7ccb29fde37cdca6e497afa', 'no': '0x8f4f1e08871f4d9d537a3291cac52b6128cd4f29610e7fda32120b0c827e3f60'}
2025-11-04 08:10:24,997 - order_manager - INFO - Order placed successfully: 0x1a2c65d9e9be4163b44afa1d89f61ee519e1139854308da0cdc0014c34dfbb97
2025-11-04 08:10:24,999 - market_scanner_v2 - INFO - âœ… Got 300 markets from API
2025-11-04 08:10:25,000 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 300/300 markets passed
2025-11-04 08:10:25,000 - market_scanner_v2 - INFO - âœ… Found 300 qualifying markets (from 300 total)
2025-11-04 08:10:25,003 - market_selector - INFO - Selected 3 markets from 300 candidates
2025-11-04 08:10:25,341 - order_manager - INFO - Prepared order for market 664299 with spread 0.0120
2025-11-04 08:10:25,341 - order_manager - INFO - Added order to pending queue: 664299
2025-11-04 08:10:25,341 - __main__ - INFO - Added market 664299 to pending orders
2025-11-04 08:10:25,672 - order_manager - INFO - Prepared order for market 664211 with spread 0.0120
2025-11-04 08:10:25,672 - order_manager - INFO - Added order to pending queue: 664211
2025-11-04 08:10:25,672 - __main__ - INFO - Added market 664211 to pending orders
2025-11-04 08:10:26,021 - order_manager - INFO - Prepared order for market 664214 with spread 0.0120
2025-11-04 08:10:26,022 - order_manager - INFO - Added order to pending queue: 664214
2025-11-04 08:10:26,022 - __main__ - INFO - Added market 664214 to pending orders
2025-11-04 08:10:28,540 - order_manager - INFO - Order placed successfully: 0xa2fe4390472af91b495e6e671e1bfe72129a9c1160744340b9f5176193d9f134
2025-11-04 08:10:28,541 - order_manager - INFO - Placed orders for market 664299: {'yes': '0x1a2c65d9e9be4163b44afa1d89f61ee519e1139854308da0cdc0014c34dfbb97', 'no': '0xa2fe4390472af91b495e6e671e1bfe72129a9c1160744340b9f5176193d9f134'}
2025-11-04 08:10:31,565 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 08:10:34,102 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:10:34,104 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:10:34,136 - market_scanner_v2 - INFO - âœ… Fetched 300 markets from API
2025-11-04 08:10:34,138 - market_scanner_v2 - INFO - âœ… Got 300 markets from API
2025-11-04 08:10:34,139 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 300/300 markets passed
2025-11-04 08:10:34,139 - market_scanner_v2 - INFO - âœ… Found 300 qualifying markets (from 300 total)
2025-11-04 08:10:34,142 - market_selector - INFO - Selected 3 markets from 300 candidates
2025-11-04 08:10:34,492 - order_manager - INFO - Prepared order for market 664299 with spread 0.0120
2025-11-04 08:10:34,492 - order_manager - INFO - Added order to pending queue: 664299
2025-11-04 08:10:34,492 - __main__ - INFO - Added market 664299 to pending orders
2025-11-04 08:10:34,827 - order_manager - INFO - Prepared order for market 664211 with spread 0.0120
2025-11-04 08:10:34,828 - order_manager - INFO - Added order to pending queue: 664211
2025-11-04 08:10:34,828 - __main__ - INFO - Added market 664211 to pending orders
2025-11-04 08:10:35,162 - order_manager - INFO - Prepared order for market 664214 with spread 0.0120
2025-11-04 08:10:35,162 - order_manager - INFO - Added order to pending queue: 664214
2025-11-04 08:10:35,162 - __main__ - INFO - Added market 664214 to pending orders
2025-11-04 08:10:37,393 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:10:37,394 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:10:39,446 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:10:39,447 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:10:43,022 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:10:43,023 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:10:45,158 - order_manager - INFO - Order placed successfully: 0x282f718aa67fde477cffb0fbefff081e502db61d0cc80dbdb220ba2cdff867d2
2025-11-04 08:10:45,159 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 08:10:46,206 - market_scanner_v2 - INFO - âœ… Fetched 300 markets from API
2025-11-04 08:10:46,208 - market_scanner_v2 - INFO - âœ… Got 300 markets from API
2025-11-04 08:10:46,209 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 300/300 markets passed
2025-11-04 08:10:46,210 - market_scanner_v2 - INFO - âœ… Found 300 qualifying markets (from 300 total)
2025-11-04 08:10:46,212 - market_selector - INFO - Selected 3 markets from 300 candidates
2025-11-04 08:10:46,545 - order_manager - INFO - Prepared order for market 664299 with spread 0.0120
2025-11-04 08:10:46,545 - order_manager - INFO - Added order to pending queue: 664299
2025-11-04 08:10:46,545 - __main__ - INFO - Added market 664299 to pending orders
2025-11-04 08:10:46,880 - order_manager - INFO - Prepared order for market 664214 with spread 0.0120
2025-11-04 08:10:46,880 - order_manager - INFO - Added order to pending queue: 664214
2025-11-04 08:10:46,881 - __main__ - INFO - Added market 664214 to pending orders
2025-11-04 08:10:47,217 - order_manager - INFO - Prepared order for market 664211 with spread 0.0120
2025-11-04 08:10:47,217 - order_manager - INFO - Added order to pending queue: 664211
2025-11-04 08:10:47,217 - __main__ - INFO - Added market 664211 to pending orders
2025-11-04 08:10:49,338 - order_manager - INFO - Order placed successfully: 0xee0b891719b8081ea310b601016fce3bae370da90c8eb9448f2857704de834d6
2025-11-04 08:10:49,338 - order_manager - INFO - Placed orders for market 664299: {'yes': '0x282f718aa67fde477cffb0fbefff081e502db61d0cc80dbdb220ba2cdff867d2', 'no': '0xee0b891719b8081ea310b601016fce3bae370da90c8eb9448f2857704de834d6'}
2025-11-04 08:10:51,568 - order_manager - INFO - Order placed successfully: 0x29fda1bb55cf546d074d4c9e3ae8455f3aef983c2511e97094bab98a78559368
2025-11-04 08:10:51,704 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 08:10:52,723 - market_scanner_v2 - INFO - âœ… Fetched 300 markets from API
2025-11-04 08:10:52,725 - market_scanner_v2 - INFO - âœ… Got 300 markets from API
2025-11-04 08:10:52,726 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 300/300 markets passed
2025-11-04 08:10:52,726 - market_scanner_v2 - INFO - âœ… Found 300 qualifying markets (from 300 total)
2025-11-04 08:10:52,729 - market_selector - INFO - Selected 3 markets from 300 candidates
2025-11-04 08:10:53,069 - order_manager - INFO - Prepared order for market 664299 with spread 0.0120
2025-11-04 08:10:53,069 - order_manager - INFO - Added order to pending queue: 664299
2025-11-04 08:10:53,070 - __main__ - INFO - Added market 664299 to pending orders
2025-11-04 08:10:53,408 - order_manager - INFO - Prepared order for market 664214 with spread 0.0120
2025-11-04 08:10:53,408 - order_manager - INFO - Added order to pending queue: 664214
2025-11-04 08:10:53,408 - __main__ - INFO - Added market 664214 to pending orders
2025-11-04 08:10:53,774 - order_manager - INFO - Prepared order for market 664211 with spread 0.0120
2025-11-04 08:10:53,774 - order_manager - INFO - Added order to pending queue: 664211
2025-11-04 08:10:53,774 - __main__ - INFO - Added market 664211 to pending orders
2025-11-04 08:10:55,930 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:10:55,930 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:10:55,932 - order_manager - INFO - Placed orders for market 664299: {'yes': '0x29fda1bb55cf546d074d4c9e3ae8455f3aef983c2511e97094bab98a78559368'}
2025-11-04 08:10:58,035 - order_manager - INFO - Order placed successfully: 0xf8510c361f3e2525e592b40d3dc5a83789b9a48e68b5a08e72e0bba06a2f70a0
2025-11-04 08:10:58,443 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 08:11:01,063 - order_manager - INFO - Order placed successfully: 0x3cb7ca161af02d2e5124c6ebb138bbb1c215a124029aeed23600c1e92311e91d
2025-11-04 08:11:01,064 - order_manager - INFO - Placed orders for market 664211: {'yes': '0xf8510c361f3e2525e592b40d3dc5a83789b9a48e68b5a08e72e0bba06a2f70a0', 'no': '0x3cb7ca161af02d2e5124c6ebb138bbb1c215a124029aeed23600c1e92311e91d'}
2025-11-04 08:11:03,174 - order_manager - INFO - Order placed successfully: 0x71c12562c389978329c08e3dd391234b25c3b628f6efc35e1ea9a73dd9f1b6de
2025-11-04 08:11:03,203 - market_scanner_v2 - INFO - âœ… Fetched 300 markets from API
2025-11-04 08:11:03,205 - market_scanner_v2 - INFO - âœ… Got 300 markets from API
2025-11-04 08:11:03,206 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 300/300 markets passed
2025-11-04 08:11:03,207 - market_scanner_v2 - INFO - âœ… Found 300 qualifying markets (from 300 total)
2025-11-04 08:11:03,209 - market_selector - INFO - Selected 3 markets from 300 candidates
2025-11-04 08:11:03,556 - order_manager - INFO - Prepared order for market 664299 with spread 0.0120
2025-11-04 08:11:03,556 - order_manager - INFO - Added order to pending queue: 664299
2025-11-04 08:11:03,556 - __main__ - INFO - Added market 664299 to pending orders
2025-11-04 08:11:03,903 - order_manager - INFO - Prepared order for market 664214 with spread 0.0120
2025-11-04 08:11:03,904 - order_manager - INFO - Added order to pending queue: 664214
2025-11-04 08:11:03,904 - __main__ - INFO - Added market 664214 to pending orders
2025-11-04 08:11:04,240 - order_manager - INFO - Prepared order for market 664211 with spread 0.0120
2025-11-04 08:11:04,241 - order_manager - INFO - Added order to pending queue: 664211
2025-11-04 08:11:04,241 - __main__ - INFO - Added market 664211 to pending orders
2025-11-04 08:11:06,456 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:11:06,457 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:11:06,458 - order_manager - INFO - Placed orders for market 664214: {'yes': '0x71c12562c389978329c08e3dd391234b25c3b628f6efc35e1ea9a73dd9f1b6de'}
2025-11-04 08:11:08,731 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 08:11:09,768 - market_scanner_v2 - INFO - âœ… Fetched 300 markets from API
2025-11-04 08:11:09,770 - market_scanner_v2 - INFO - âœ… Got 300 markets from API
2025-11-04 08:11:09,771 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 300/300 markets passed
2025-11-04 08:11:09,771 - market_scanner_v2 - INFO - âœ… Found 300 qualifying markets (from 300 total)
2025-11-04 08:11:09,774 - market_selector - INFO - Selected 3 markets from 300 candidates
2025-11-04 08:11:10,118 - order_manager - INFO - Prepared order for market 664299 with spread 0.0120
2025-11-04 08:11:10,118 - order_manager - INFO - Added order to pending queue: 664299
2025-11-04 08:11:10,118 - __main__ - INFO - Added market 664299 to pending orders
2025-11-04 08:11:10,457 - order_manager - INFO - Prepared order for market 664214 with spread 0.0120
2025-11-04 08:11:10,457 - order_manager - INFO - Added order to pending queue: 664214
2025-11-04 08:11:10,457 - __main__ - INFO - Added market 664214 to pending orders
2025-11-04 08:11:10,802 - order_manager - INFO - Prepared order for market 664211 with spread 0.0120
2025-11-04 08:11:10,802 - order_manager - INFO - Added order to pending queue: 664211
2025-11-04 08:11:10,802 - __main__ - INFO - Added market 664211 to pending orders
2025-11-04 08:11:12,844 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:11:12,844 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:11:16,262 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:11:16,262 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:11:18,368 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:11:18,368 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:11:18,369 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 08:11:21,286 - order_manager - INFO - Order placed successfully: 0xdf23cc2c4d31fc9dd23f9a226cd3e1c75caba849687614b0e9b6804cb3494132
2025-11-04 08:11:21,287 - order_manager - INFO - Placed orders for market 664438: {'no': '0xdf23cc2c4d31fc9dd23f9a226cd3e1c75caba849687614b0e9b6804cb3494132'}
2025-11-04 08:11:23,434 - order_manager - INFO - Order placed successfully: 0x113725bc099200a427901735091e84ca6f98059440afffee9b36be3e5fb75151
2025-11-04 08:11:23,457 - market_scanner_v2 - INFO - âœ… Fetched 300 markets from API
2025-11-04 08:11:23,459 - market_scanner_v2 - INFO - âœ… Got 300 markets from API
2025-11-04 08:11:23,460 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 300/300 markets passed
2025-11-04 08:11:23,460 - market_scanner_v2 - INFO - âœ… Found 300 qualifying markets (from 300 total)
2025-11-04 08:11:23,462 - market_selector - INFO - Selected 3 markets from 300 candidates
2025-11-04 08:11:23,781 - order_manager - INFO - Prepared order for market 664299 with spread 0.0120
2025-11-04 08:11:23,782 - order_manager - INFO - Added order to pending queue: 664299
2025-11-04 08:11:23,782 - __main__ - INFO - Added market 664299 to pending orders
2025-11-04 08:11:24,119 - order_manager - INFO - Prepared order for market 664214 with spread 0.0120
2025-11-04 08:11:24,120 - order_manager - INFO - Added order to pending queue: 664214
2025-11-04 08:11:24,120 - __main__ - INFO - Added market 664214 to pending orders
2025-11-04 08:11:24,453 - order_manager - INFO - Prepared order for market 664211 with spread 0.0120
2025-11-04 08:11:24,453 - order_manager - INFO - Added order to pending queue: 664211
2025-11-04 08:11:24,453 - __main__ - INFO - Added market 664211 to pending orders
2025-11-04 08:11:26,551 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:11:26,553 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:11:26,554 - order_manager - INFO - Placed orders for market 664299: {'yes': '0x113725bc099200a427901735091e84ca6f98059440afffee9b36be3e5fb75151'}
2025-11-04 08:11:28,657 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:11:28,657 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:11:29,516 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 08:11:32,143 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:11:32,144 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:11:34,233 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:11:34,233 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:11:34,260 - market_scanner_v2 - INFO - âœ… Fetched 300 markets from API
2025-11-04 08:11:34,262 - market_scanner_v2 - INFO - âœ… Got 300 markets from API
2025-11-04 08:11:34,262 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 300/300 markets passed
2025-11-04 08:11:34,263 - market_scanner_v2 - INFO - âœ… Found 300 qualifying markets (from 300 total)
2025-11-04 08:11:34,265 - market_selector - INFO - Selected 3 markets from 300 candidates
2025-11-04 08:11:34,597 - order_manager - INFO - Prepared order for market 664299 with spread 0.0120
2025-11-04 08:11:34,597 - order_manager - INFO - Added order to pending queue: 664299
2025-11-04 08:11:34,597 - __main__ - INFO - Added market 664299 to pending orders
2025-11-04 08:11:34,931 - order_manager - INFO - Prepared order for market 664214 with spread 0.0120
2025-11-04 08:11:34,932 - order_manager - INFO - Added order to pending queue: 664214
2025-11-04 08:11:34,932 - __main__ - INFO - Added market 664214 to pending orders
2025-11-04 08:11:35,282 - order_manager - INFO - Prepared order for market 664211 with spread 0.0120
2025-11-04 08:11:35,282 - order_manager - INFO - Added order to pending queue: 664211
2025-11-04 08:11:35,282 - __main__ - INFO - Added market 664211 to pending orders
2025-11-04 08:11:37,344 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:11:37,344 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:11:39,380 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:11:39,381 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:11:42,123 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:11:42,123 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:11:44,250 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:11:44,250 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:11:44,252 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 08:11:47,633 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:11:47,633 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:11:49,747 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:11:49,747 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:11:49,775 - market_scanner_v2 - INFO - âœ… Fetched 300 markets from API
2025-11-04 08:11:49,776 - market_scanner_v2 - INFO - âœ… Got 300 markets from API
2025-11-04 08:11:49,777 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 300/300 markets passed
2025-11-04 08:11:49,777 - market_scanner_v2 - INFO - âœ… Found 300 qualifying markets (from 300 total)
2025-11-04 08:11:49,780 - market_selector - INFO - Selected 3 markets from 300 candidates
2025-11-04 08:11:50,111 - order_manager - INFO - Prepared order for market 664299 with spread 0.0120
2025-11-04 08:11:50,111 - order_manager - INFO - Added order to pending queue: 664299
2025-11-04 08:11:50,111 - __main__ - INFO - Added market 664299 to pending orders
2025-11-04 08:11:50,436 - order_manager - INFO - Prepared order for market 664214 with spread 0.0120
2025-11-04 08:11:50,436 - order_manager - INFO - Added order to pending queue: 664214
2025-11-04 08:11:50,436 - __main__ - INFO - Added market 664214 to pending orders
2025-11-04 08:11:50,771 - order_manager - INFO - Prepared order for market 664211 with spread 0.0120
2025-11-04 08:11:50,771 - order_manager - INFO - Added order to pending queue: 664211
2025-11-04 08:11:50,771 - __main__ - INFO - Added market 664211 to pending orders
2025-11-04 08:11:52,840 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:11:52,840 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:11:54,876 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:11:54,876 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:11:54,878 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 08:11:55,901 - market_scanner_v2 - INFO - âœ… Fetched 300 markets from API
2025-11-04 08:11:57,957 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:11:57,958 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:12:00,006 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:12:00,007 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:12:00,009 - market_scanner_v2 - INFO - âœ… Got 300 markets from API
2025-11-04 08:12:00,011 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 300/300 markets passed
2025-11-04 08:12:00,011 - market_scanner_v2 - INFO - âœ… Found 300 qualifying markets (from 300 total)
2025-11-04 08:12:00,013 - market_selector - INFO - Selected 3 markets from 300 candidates
2025-11-04 08:12:00,344 - order_manager - INFO - Prepared order for market 664299 with spread 0.0120
2025-11-04 08:12:00,345 - order_manager - INFO - Added order to pending queue: 664299
2025-11-04 08:12:00,345 - __main__ - INFO - Added market 664299 to pending orders
2025-11-04 08:12:00,677 - order_manager - INFO - Prepared order for market 664214 with spread 0.0120
2025-11-04 08:12:00,678 - order_manager - INFO - Added order to pending queue: 664214
2025-11-04 08:12:00,678 - __main__ - INFO - Added market 664214 to pending orders
2025-11-04 08:12:01,009 - order_manager - INFO - Prepared order for market 664211 with spread 0.0120
2025-11-04 08:12:01,009 - order_manager - INFO - Added order to pending queue: 664211
2025-11-04 08:12:01,010 - __main__ - INFO - Added market 664211 to pending orders
2025-11-04 08:12:03,559 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:12:03,560 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:12:05,581 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:12:05,581 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:12:05,583 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 08:12:06,594 - market_scanner_v2 - INFO - âœ… Fetched 300 markets from API
2025-11-04 08:12:06,595 - market_scanner_v2 - INFO - âœ… Got 300 markets from API
2025-11-04 08:12:06,596 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 300/300 markets passed
2025-11-04 08:12:06,596 - market_scanner_v2 - INFO - âœ… Found 300 qualifying markets (from 300 total)
2025-11-04 08:12:06,599 - market_selector - INFO - Selected 3 markets from 300 candidates
2025-11-04 08:12:06,924 - order_manager - INFO - Prepared order for market 664299 with spread 0.0120
2025-11-04 08:12:06,924 - order_manager - INFO - Added order to pending queue: 664299
2025-11-04 08:12:06,924 - __main__ - INFO - Added market 664299 to pending orders
2025-11-04 08:12:07,241 - order_manager - INFO - Prepared order for market 664214 with spread 0.0120
2025-11-04 08:12:07,241 - order_manager - INFO - Added order to pending queue: 664214
2025-11-04 08:12:07,241 - __main__ - INFO - Added market 664214 to pending orders
2025-11-04 08:12:07,594 - order_manager - INFO - Prepared order for market 664211 with spread 0.0120
2025-11-04 08:12:07,594 - order_manager - INFO - Added order to pending queue: 664211
2025-11-04 08:12:07,594 - __main__ - INFO - Added market 664211 to pending orders
2025-11-04 08:12:09,821 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:12:09,821 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:12:11,941 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:12:11,941 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:12:12,560 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 08:12:15,262 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:12:15,262 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:12:17,324 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:12:17,324 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:12:18,359 - market_scanner_v2 - INFO - âœ… Fetched 300 markets from API
2025-11-04 08:12:18,360 - market_scanner_v2 - INFO - âœ… Got 300 markets from API
2025-11-04 08:12:18,361 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 300/300 markets passed
2025-11-04 08:12:18,361 - market_scanner_v2 - INFO - âœ… Found 300 qualifying markets (from 300 total)
2025-11-04 08:12:18,364 - market_selector - INFO - Selected 3 markets from 300 candidates
2025-11-04 08:12:18,694 - order_manager - INFO - Prepared order for market 664299 with spread 0.0120
2025-11-04 08:12:18,694 - order_manager - INFO - Added order to pending queue: 664299
2025-11-04 08:12:18,694 - __main__ - INFO - Added market 664299 to pending orders
2025-11-04 08:12:19,038 - order_manager - INFO - Prepared order for market 664214 with spread 0.0120
2025-11-04 08:12:19,039 - order_manager - INFO - Added order to pending queue: 664214
2025-11-04 08:12:19,039 - __main__ - INFO - Added market 664214 to pending orders
2025-11-04 08:12:19,381 - order_manager - INFO - Prepared order for market 664211 with spread 0.0120
2025-11-04 08:12:19,381 - order_manager - INFO - Added order to pending queue: 664211
2025-11-04 08:12:19,381 - __main__ - INFO - Added market 664211 to pending orders
2025-11-04 08:12:21,470 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:12:21,471 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:12:23,546 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:12:23,546 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:12:23,621 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 08:12:26,522 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:12:26,523 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:12:28,686 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:12:28,686 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:12:28,712 - market_scanner_v2 - INFO - âœ… Fetched 300 markets from API
2025-11-04 08:12:28,714 - market_scanner_v2 - INFO - âœ… Got 300 markets from API
2025-11-04 08:12:28,715 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 300/300 markets passed
2025-11-04 08:12:28,715 - market_scanner_v2 - INFO - âœ… Found 300 qualifying markets (from 300 total)
2025-11-04 08:12:28,718 - market_selector - INFO - Selected 3 markets from 300 candidates
2025-11-04 08:12:29,083 - order_manager - INFO - Prepared order for market 664299 with spread 0.0120
2025-11-04 08:12:29,083 - order_manager - INFO - Added order to pending queue: 664299
2025-11-04 08:12:29,083 - __main__ - INFO - Added market 664299 to pending orders
2025-11-04 08:12:29,424 - order_manager - INFO - Prepared order for market 664214 with spread 0.0120
2025-11-04 08:12:29,424 - order_manager - INFO - Added order to pending queue: 664214
2025-11-04 08:12:29,424 - __main__ - INFO - Added market 664214 to pending orders
2025-11-04 08:12:29,756 - order_manager - INFO - Prepared order for market 664211 with spread 0.0120
2025-11-04 08:12:29,757 - order_manager - INFO - Added order to pending queue: 664211
2025-11-04 08:12:29,757 - __main__ - INFO - Added market 664211 to pending orders
2025-11-04 08:12:32,268 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:12:32,269 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:12:34,409 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:12:34,409 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:12:34,412 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 08:12:35,472 - market_scanner_v2 - INFO - âœ… Fetched 300 markets from API
2025-11-04 08:12:35,474 - market_scanner_v2 - INFO - âœ… Got 300 markets from API
2025-11-04 08:12:35,475 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 300/300 markets passed
2025-11-04 08:12:35,475 - market_scanner_v2 - INFO - âœ… Found 300 qualifying markets (from 300 total)
2025-11-04 08:12:35,478 - market_selector - INFO - Selected 3 markets from 300 candidates
2025-11-04 08:12:35,814 - order_manager - INFO - Prepared order for market 664299 with spread 0.0120
2025-11-04 08:12:35,815 - order_manager - INFO - Added order to pending queue: 664299
2025-11-04 08:12:35,815 - __main__ - INFO - Added market 664299 to pending orders
2025-11-04 08:12:36,162 - order_manager - INFO - Prepared order for market 664214 with spread 0.0120
2025-11-04 08:12:36,162 - order_manager - INFO - Added order to pending queue: 664214
2025-11-04 08:12:36,162 - __main__ - INFO - Added market 664214 to pending orders
2025-11-04 08:12:36,535 - order_manager - INFO - Prepared order for market 664211 with spread 0.0120
2025-11-04 08:12:36,536 - order_manager - INFO - Added order to pending queue: 664211
2025-11-04 08:12:36,536 - __main__ - INFO - Added market 664211 to pending orders
2025-11-04 08:12:38,610 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:12:38,610 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:12:40,718 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:12:40,719 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:12:40,777 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 08:12:43,370 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:12:43,370 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:12:45,448 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:12:45,448 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:12:45,479 - market_scanner_v2 - INFO - âœ… Fetched 300 markets from API
2025-11-04 08:12:45,481 - market_scanner_v2 - INFO - âœ… Got 300 markets from API
2025-11-04 08:12:45,482 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 300/300 markets passed
2025-11-04 08:12:45,482 - market_scanner_v2 - INFO - âœ… Found 300 qualifying markets (from 300 total)
2025-11-04 08:12:45,484 - market_selector - INFO - Selected 3 markets from 300 candidates
2025-11-04 08:12:45,836 - order_manager - INFO - Prepared order for market 664299 with spread 0.0120
2025-11-04 08:12:45,836 - order_manager - INFO - Added order to pending queue: 664299
2025-11-04 08:12:45,836 - __main__ - INFO - Added market 664299 to pending orders
2025-11-04 08:12:46,178 - order_manager - INFO - Prepared order for market 664214 with spread 0.0120
2025-11-04 08:12:46,179 - order_manager - INFO - Added order to pending queue: 664214
2025-11-04 08:12:46,179 - __main__ - INFO - Added market 664214 to pending orders
2025-11-04 08:12:46,534 - order_manager - INFO - Prepared order for market 664211 with spread 0.0120
2025-11-04 08:12:46,534 - order_manager - INFO - Added order to pending queue: 664211
2025-11-04 08:12:46,534 - __main__ - INFO - Added market 664211 to pending orders
2025-11-04 08:12:48,632 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:12:48,632 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:12:50,721 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:12:50,721 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:12:51,727 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 08:12:54,009 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:12:54,009 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:12:56,044 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:12:56,045 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:12:56,073 - market_scanner_v2 - INFO - âœ… Fetched 300 markets from API
2025-11-04 08:12:56,075 - market_scanner_v2 - INFO - âœ… Got 300 markets from API
2025-11-04 08:12:56,076 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 300/300 markets passed
2025-11-04 08:12:56,076 - market_scanner_v2 - INFO - âœ… Found 300 qualifying markets (from 300 total)
2025-11-04 08:12:56,079 - market_selector - INFO - Selected 3 markets from 300 candidates
2025-11-04 08:12:56,409 - order_manager - INFO - Prepared order for market 664299 with spread 0.0120
2025-11-04 08:12:56,410 - order_manager - INFO - Added order to pending queue: 664299
2025-11-04 08:12:56,410 - __main__ - INFO - Added market 664299 to pending orders
2025-11-04 08:12:56,756 - order_manager - INFO - Prepared order for market 664214 with spread 0.0120
2025-11-04 08:12:56,757 - order_manager - INFO - Added order to pending queue: 664214
2025-11-04 08:12:56,757 - __main__ - INFO - Added market 664214 to pending orders
2025-11-04 08:12:57,098 - order_manager - INFO - Prepared order for market 664211 with spread 0.0120
2025-11-04 08:12:57,099 - order_manager - INFO - Added order to pending queue: 664211
2025-11-04 08:12:57,099 - __main__ - INFO - Added market 664211 to pending orders
2025-11-04 08:12:59,211 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:12:59,212 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:13:01,301 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:13:01,302 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:13:04,369 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:13:04,370 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:13:04,372 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 08:13:05,185 - market_scanner_v2 - INFO - âœ… Fetched 300 markets from API
2025-11-04 08:13:05,187 - market_scanner_v2 - INFO - âœ… Got 300 markets from API
2025-11-04 08:13:05,188 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 300/300 markets passed
2025-11-04 08:13:05,188 - market_scanner_v2 - INFO - âœ… Found 300 qualifying markets (from 300 total)
2025-11-04 08:13:05,191 - market_selector - INFO - Selected 3 markets from 300 candidates
2025-11-04 08:13:05,534 - order_manager - INFO - Prepared order for market 664299 with spread 0.0120
2025-11-04 08:13:05,535 - order_manager - INFO - Added order to pending queue: 664299
2025-11-04 08:13:05,535 - __main__ - INFO - Added market 664299 to pending orders
2025-11-04 08:13:05,871 - order_manager - INFO - Prepared order for market 664214 with spread 0.0120
2025-11-04 08:13:05,871 - order_manager - INFO - Added order to pending queue: 664214
2025-11-04 08:13:05,871 - __main__ - INFO - Added market 664214 to pending orders
2025-11-04 08:13:06,216 - order_manager - INFO - Prepared order for market 664211 with spread 0.0120
2025-11-04 08:13:06,216 - order_manager - INFO - Added order to pending queue: 664211
2025-11-04 08:13:06,216 - __main__ - INFO - Added market 664211 to pending orders
2025-11-04 08:13:10,655 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:13:10,656 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:13:10,927 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 08:13:13,646 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:13:13,646 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:13:15,754 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:13:15,755 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:13:15,787 - market_scanner_v2 - INFO - âœ… Fetched 300 markets from API
2025-11-04 08:13:15,793 - market_scanner_v2 - INFO - âœ… Got 300 markets from API
2025-11-04 08:13:15,794 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 300/300 markets passed
2025-11-04 08:13:15,794 - market_scanner_v2 - INFO - âœ… Found 300 qualifying markets (from 300 total)
2025-11-04 08:13:15,801 - market_selector - INFO - Selected 3 markets from 300 candidates
2025-11-04 08:13:16,130 - order_manager - INFO - Prepared order for market 664299 with spread 0.0120
2025-11-04 08:13:16,131 - order_manager - INFO - Added order to pending queue: 664299
2025-11-04 08:13:16,131 - __main__ - INFO - Added market 664299 to pending orders
2025-11-04 08:13:16,495 - order_manager - INFO - Prepared order for market 664214 with spread 0.0120
2025-11-04 08:13:16,496 - order_manager - INFO - Added order to pending queue: 664214
2025-11-04 08:13:16,496 - __main__ - INFO - Added market 664214 to pending orders
2025-11-04 08:13:16,837 - order_manager - INFO - Prepared order for market 664211 with spread 0.0120
2025-11-04 08:13:16,837 - order_manager - INFO - Added order to pending queue: 664211
2025-11-04 08:13:16,837 - __main__ - INFO - Added market 664211 to pending orders
2025-11-04 08:13:18,924 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:13:18,924 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:13:21,059 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:13:21,060 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:13:24,834 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:13:24,834 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:13:26,938 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:13:26,939 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:13:26,941 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 08:13:29,988 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:13:29,988 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:13:32,090 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:13:32,090 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:13:32,116 - market_scanner_v2 - INFO - âœ… Fetched 300 markets from API
2025-11-04 08:13:32,118 - market_scanner_v2 - INFO - âœ… Got 300 markets from API
2025-11-04 08:13:32,119 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 300/300 markets passed
2025-11-04 08:13:32,119 - market_scanner_v2 - INFO - âœ… Found 300 qualifying markets (from 300 total)
2025-11-04 08:13:32,122 - market_selector - INFO - Selected 3 markets from 300 candidates
2025-11-04 08:13:32,460 - order_manager - INFO - Prepared order for market 664299 with spread 0.0120
2025-11-04 08:13:32,460 - order_manager - INFO - Added order to pending queue: 664299
2025-11-04 08:13:32,460 - __main__ - INFO - Added market 664299 to pending orders
2025-11-04 08:13:32,810 - order_manager - INFO - Prepared order for market 664214 with spread 0.0120
2025-11-04 08:13:32,810 - order_manager - INFO - Added order to pending queue: 664214
2025-11-04 08:13:32,810 - __main__ - INFO - Added market 664214 to pending orders
2025-11-04 08:13:33,150 - order_manager - INFO - Prepared order for market 664211 with spread 0.0120
2025-11-04 08:13:33,151 - order_manager - INFO - Added order to pending queue: 664211
2025-11-04 08:13:33,151 - __main__ - INFO - Added market 664211 to pending orders
2025-11-04 08:13:35,241 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:13:35,241 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:13:37,349 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:13:37,349 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:13:40,114 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:13:40,115 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:13:42,155 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:13:42,155 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:13:42,157 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 08:13:45,204 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:13:45,204 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:13:47,277 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:13:47,278 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:13:47,300 - market_scanner_v2 - INFO - âœ… Fetched 300 markets from API
2025-11-04 08:13:47,302 - market_scanner_v2 - INFO - âœ… Got 300 markets from API
2025-11-04 08:13:47,303 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 300/300 markets passed
2025-11-04 08:13:47,303 - market_scanner_v2 - INFO - âœ… Found 300 qualifying markets (from 300 total)
2025-11-04 08:13:47,305 - market_selector - INFO - Selected 3 markets from 300 candidates
2025-11-04 08:13:47,637 - order_manager - INFO - Prepared order for market 664299 with spread 0.0120
2025-11-04 08:13:47,637 - order_manager - INFO - Added order to pending queue: 664299
2025-11-04 08:13:47,637 - __main__ - INFO - Added market 664299 to pending orders
2025-11-04 08:13:47,978 - order_manager - INFO - Prepared order for market 664214 with spread 0.0120
2025-11-04 08:13:47,978 - order_manager - INFO - Added order to pending queue: 664214
2025-11-04 08:13:47,978 - __main__ - INFO - Added market 664214 to pending orders
2025-11-04 08:13:48,304 - order_manager - INFO - Prepared order for market 664211 with spread 0.0120
2025-11-04 08:13:48,305 - order_manager - INFO - Added order to pending queue: 664211
2025-11-04 08:13:48,305 - __main__ - INFO - Added market 664211 to pending orders
2025-11-04 08:13:50,401 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:13:50,402 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:13:52,487 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:13:52,487 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:13:52,634 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 08:13:55,873 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:13:55,874 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:13:57,910 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:13:57,910 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:13:57,936 - market_scanner_v2 - INFO - âœ… Fetched 300 markets from API
2025-11-04 08:13:57,938 - market_scanner_v2 - INFO - âœ… Got 300 markets from API
2025-11-04 08:13:57,939 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 300/300 markets passed
2025-11-04 08:13:57,940 - market_scanner_v2 - INFO - âœ… Found 300 qualifying markets (from 300 total)
2025-11-04 08:13:57,942 - market_selector - INFO - Selected 3 markets from 300 candidates
2025-11-04 08:13:58,257 - order_manager - INFO - Prepared order for market 664299 with spread 0.0120
2025-11-04 08:13:58,257 - order_manager - INFO - Added order to pending queue: 664299
2025-11-04 08:13:58,258 - __main__ - INFO - Added market 664299 to pending orders
2025-11-04 08:13:58,598 - order_manager - INFO - Prepared order for market 664214 with spread 0.0120
2025-11-04 08:13:58,599 - order_manager - INFO - Added order to pending queue: 664214
2025-11-04 08:13:58,599 - __main__ - INFO - Added market 664214 to pending orders
2025-11-04 08:13:58,946 - order_manager - INFO - Prepared order for market 664211 with spread 0.0120
2025-11-04 08:13:58,947 - order_manager - INFO - Added order to pending queue: 664211
2025-11-04 08:13:58,947 - __main__ - INFO - Added market 664211 to pending orders
2025-11-04 08:14:01,086 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:14:01,087 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:14:03,245 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:14:03,245 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:14:03,649 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 08:14:06,645 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:14:06,645 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:14:08,754 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:14:08,755 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:14:08,782 - market_scanner_v2 - INFO - âœ… Fetched 300 markets from API
2025-11-04 08:14:08,784 - market_scanner_v2 - INFO - âœ… Got 300 markets from API
2025-11-04 08:14:08,785 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 300/300 markets passed
2025-11-04 08:14:08,785 - market_scanner_v2 - INFO - âœ… Found 300 qualifying markets (from 300 total)
2025-11-04 08:14:08,788 - market_selector - INFO - Selected 3 markets from 300 candidates
2025-11-04 08:14:09,133 - order_manager - INFO - Prepared order for market 664299 with spread 0.0120
2025-11-04 08:14:09,134 - order_manager - INFO - Added order to pending queue: 664299
2025-11-04 08:14:09,134 - __main__ - INFO - Added market 664299 to pending orders
2025-11-04 08:14:09,465 - order_manager - INFO - Prepared order for market 664214 with spread 0.0120
2025-11-04 08:14:09,466 - order_manager - INFO - Added order to pending queue: 664214
2025-11-04 08:14:09,466 - __main__ - INFO - Added market 664214 to pending orders
2025-11-04 08:14:09,792 - order_manager - INFO - Prepared order for market 664211 with spread 0.0120
2025-11-04 08:14:09,793 - order_manager - INFO - Added order to pending queue: 664211
2025-11-04 08:14:09,793 - __main__ - INFO - Added market 664211 to pending orders
2025-11-04 08:14:11,871 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:14:11,872 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:14:13,898 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:14:13,898 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:14:14,338 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 08:14:17,140 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:14:17,141 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:14:19,246 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:14:19,247 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:14:19,275 - market_scanner_v2 - INFO - âœ… Fetched 300 markets from API
2025-11-04 08:14:19,277 - market_scanner_v2 - INFO - âœ… Got 300 markets from API
2025-11-04 08:14:19,278 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 300/300 markets passed
2025-11-04 08:14:19,278 - market_scanner_v2 - INFO - âœ… Found 300 qualifying markets (from 300 total)
2025-11-04 08:14:19,281 - market_selector - INFO - Selected 3 markets from 300 candidates
2025-11-04 08:14:19,628 - order_manager - INFO - Prepared order for market 664299 with spread 0.0120
2025-11-04 08:14:19,628 - order_manager - INFO - Added order to pending queue: 664299
2025-11-04 08:14:19,628 - __main__ - INFO - Added market 664299 to pending orders
2025-11-04 08:14:19,971 - order_manager - INFO - Prepared order for market 664214 with spread 0.0120
2025-11-04 08:14:19,972 - order_manager - INFO - Added order to pending queue: 664214
2025-11-04 08:14:19,972 - __main__ - INFO - Added market 664214 to pending orders
2025-11-04 08:14:20,346 - order_manager - INFO - Prepared order for market 664211 with spread 0.0120
2025-11-04 08:14:20,346 - order_manager - INFO - Added order to pending queue: 664211
2025-11-04 08:14:20,346 - __main__ - INFO - Added market 664211 to pending orders
2025-11-04 08:14:22,450 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:14:22,451 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:14:24,497 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:14:24,497 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:14:25,502 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 08:14:27,865 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:14:27,865 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:14:29,923 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:14:29,923 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:14:29,952 - market_scanner_v2 - INFO - âœ… Fetched 300 markets from API
2025-11-04 08:14:29,954 - market_scanner_v2 - INFO - âœ… Got 300 markets from API
2025-11-04 08:14:29,955 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 300/300 markets passed
2025-11-04 08:14:29,956 - market_scanner_v2 - INFO - âœ… Found 300 qualifying markets (from 300 total)
2025-11-04 08:14:29,958 - market_selector - INFO - Selected 3 markets from 300 candidates
2025-11-04 08:14:30,296 - order_manager - INFO - Prepared order for market 664299 with spread 0.0120
2025-11-04 08:14:30,297 - order_manager - INFO - Added order to pending queue: 664299
2025-11-04 08:14:30,297 - __main__ - INFO - Added market 664299 to pending orders
2025-11-04 08:14:30,628 - order_manager - INFO - Prepared order for market 664214 with spread 0.0120
2025-11-04 08:14:30,629 - order_manager - INFO - Added order to pending queue: 664214
2025-11-04 08:14:30,629 - __main__ - INFO - Added market 664214 to pending orders
2025-11-04 08:14:30,968 - order_manager - INFO - Prepared order for market 664211 with spread 0.0120
2025-11-04 08:14:30,969 - order_manager - INFO - Added order to pending queue: 664211
2025-11-04 08:14:30,969 - __main__ - INFO - Added market 664211 to pending orders
2025-11-04 08:14:33,076 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:14:33,077 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:14:35,217 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:14:35,217 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:14:36,226 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 08:14:38,423 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:14:38,424 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:14:40,535 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:14:40,536 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:14:40,576 - market_scanner_v2 - INFO - âœ… Fetched 300 markets from API
2025-11-04 08:14:40,579 - market_scanner_v2 - INFO - âœ… Got 300 markets from API
2025-11-04 08:14:40,580 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 300/300 markets passed
2025-11-04 08:14:40,580 - market_scanner_v2 - INFO - âœ… Found 300 qualifying markets (from 300 total)
2025-11-04 08:14:40,583 - market_selector - INFO - Selected 3 markets from 300 candidates
2025-11-04 08:14:40,930 - order_manager - INFO - Prepared order for market 664299 with spread 0.0120
2025-11-04 08:14:40,930 - order_manager - INFO - Added order to pending queue: 664299
2025-11-04 08:14:40,930 - __main__ - INFO - Added market 664299 to pending orders
2025-11-04 08:14:41,264 - order_manager - INFO - Prepared order for market 664214 with spread 0.0120
2025-11-04 08:14:41,265 - order_manager - INFO - Added order to pending queue: 664214
2025-11-04 08:14:41,265 - __main__ - INFO - Added market 664214 to pending orders
2025-11-04 08:14:41,604 - order_manager - INFO - Prepared order for market 664211 with spread 0.0120
2025-11-04 08:14:41,604 - order_manager - INFO - Added order to pending queue: 664211
2025-11-04 08:14:41,604 - __main__ - INFO - Added market 664211 to pending orders
2025-11-04 08:14:43,744 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:14:43,744 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:14:45,830 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:14:45,830 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:14:46,576 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 08:14:48,977 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:14:48,981 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:14:51,069 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:14:51,070 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:14:51,100 - market_scanner_v2 - INFO - âœ… Fetched 300 markets from API
2025-11-04 08:14:51,103 - market_scanner_v2 - INFO - âœ… Got 300 markets from API
2025-11-04 08:14:51,104 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 300/300 markets passed
2025-11-04 08:14:51,104 - market_scanner_v2 - INFO - âœ… Found 300 qualifying markets (from 300 total)
2025-11-04 08:14:51,107 - market_selector - INFO - Selected 3 markets from 300 candidates
2025-11-04 08:14:51,442 - order_manager - INFO - Prepared order for market 664299 with spread 0.0120
2025-11-04 08:14:51,443 - order_manager - INFO - Added order to pending queue: 664299
2025-11-04 08:14:51,443 - __main__ - INFO - Added market 664299 to pending orders
2025-11-04 08:14:51,779 - order_manager - INFO - Prepared order for market 664214 with spread 0.0120
2025-11-04 08:14:51,780 - order_manager - INFO - Added order to pending queue: 664214
2025-11-04 08:14:51,780 - __main__ - INFO - Added market 664214 to pending orders
2025-11-04 08:14:52,111 - order_manager - INFO - Prepared order for market 664211 with spread 0.0120
2025-11-04 08:14:52,111 - order_manager - INFO - Added order to pending queue: 664211
2025-11-04 08:14:52,112 - __main__ - INFO - Added market 664211 to pending orders
2025-11-04 08:14:54,171 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:14:54,171 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:14:56,221 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:14:56,222 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:14:57,379 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 08:14:59,662 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:14:59,663 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:15:01,820 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:15:01,820 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:15:01,855 - market_scanner_v2 - INFO - âœ… Fetched 300 markets from API
2025-11-04 08:15:01,858 - market_scanner_v2 - INFO - âœ… Got 300 markets from API
2025-11-04 08:15:01,860 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 300/300 markets passed
2025-11-04 08:15:01,860 - market_scanner_v2 - INFO - âœ… Found 300 qualifying markets (from 300 total)
2025-11-04 08:15:01,863 - market_selector - INFO - Selected 3 markets from 300 candidates
2025-11-04 08:15:02,201 - order_manager - INFO - Prepared order for market 664299 with spread 0.0120
2025-11-04 08:15:02,202 - order_manager - INFO - Added order to pending queue: 664299
2025-11-04 08:15:02,202 - __main__ - INFO - Added market 664299 to pending orders
2025-11-04 08:15:02,609 - order_manager - INFO - Prepared order for market 664214 with spread 0.0120
2025-11-04 08:15:02,610 - order_manager - INFO - Added order to pending queue: 664214
2025-11-04 08:15:02,610 - __main__ - INFO - Added market 664214 to pending orders
2025-11-04 08:15:02,959 - order_manager - INFO - Prepared order for market 664211 with spread 0.0120
2025-11-04 08:15:02,959 - order_manager - INFO - Added order to pending queue: 664211
2025-11-04 08:15:02,959 - __main__ - INFO - Added market 664211 to pending orders
2025-11-04 08:15:05,038 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:15:05,039 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:15:07,084 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:15:07,085 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:15:09,973 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:15:09,973 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:15:12,128 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:15:12,129 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:15:12,131 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 08:15:13,161 - market_scanner_v2 - INFO - âœ… Fetched 300 markets from API
2025-11-04 08:15:13,164 - market_scanner_v2 - INFO - âœ… Got 300 markets from API
2025-11-04 08:15:13,165 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 300/300 markets passed
2025-11-04 08:15:13,165 - market_scanner_v2 - INFO - âœ… Found 300 qualifying markets (from 300 total)
2025-11-04 08:15:13,168 - market_selector - INFO - Selected 3 markets from 300 candidates
2025-11-04 08:15:13,545 - order_manager - INFO - Prepared order for market 664299 with spread 0.0120
2025-11-04 08:15:13,546 - order_manager - INFO - Added order to pending queue: 664299
2025-11-04 08:15:13,546 - __main__ - INFO - Added market 664299 to pending orders
2025-11-04 08:15:13,880 - order_manager - INFO - Prepared order for market 664214 with spread 0.0120
2025-11-04 08:15:13,881 - order_manager - INFO - Added order to pending queue: 664214
2025-11-04 08:15:13,881 - __main__ - INFO - Added market 664214 to pending orders
2025-11-04 08:15:14,212 - order_manager - INFO - Prepared order for market 664211 with spread 0.0120
2025-11-04 08:15:14,213 - order_manager - INFO - Added order to pending queue: 664211
2025-11-04 08:15:14,213 - __main__ - INFO - Added market 664211 to pending orders
2025-11-04 08:15:16,245 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:15:16,246 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:15:18,370 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:15:18,371 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:15:18,682 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 08:15:21,594 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:15:21,594 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:15:23,673 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:15:23,674 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:15:23,700 - market_scanner_v2 - INFO - âœ… Fetched 300 markets from API
2025-11-04 08:15:23,702 - market_scanner_v2 - INFO - âœ… Got 300 markets from API
2025-11-04 08:15:23,703 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 300/300 markets passed
2025-11-04 08:15:23,703 - market_scanner_v2 - INFO - âœ… Found 300 qualifying markets (from 300 total)
2025-11-04 08:15:23,706 - market_selector - INFO - Selected 3 markets from 300 candidates
2025-11-04 08:15:24,045 - order_manager - INFO - Prepared order for market 664299 with spread 0.0120
2025-11-04 08:15:24,045 - order_manager - INFO - Added order to pending queue: 664299
2025-11-04 08:15:24,045 - __main__ - INFO - Added market 664299 to pending orders
2025-11-04 08:15:24,378 - order_manager - INFO - Prepared order for market 664214 with spread 0.0120
2025-11-04 08:15:24,378 - order_manager - INFO - Added order to pending queue: 664214
2025-11-04 08:15:24,379 - __main__ - INFO - Added market 664214 to pending orders
2025-11-04 08:15:24,726 - order_manager - INFO - Prepared order for market 664211 with spread 0.0120
2025-11-04 08:15:24,727 - order_manager - INFO - Added order to pending queue: 664211
2025-11-04 08:15:24,727 - __main__ - INFO - Added market 664211 to pending orders
2025-11-04 08:15:26,904 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:15:26,905 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:15:28,965 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:15:28,966 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:15:29,970 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 08:15:32,530 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:15:32,531 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:15:34,595 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:15:34,596 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:15:34,628 - market_scanner_v2 - INFO - âœ… Fetched 300 markets from API
2025-11-04 08:15:34,631 - market_scanner_v2 - INFO - âœ… Got 300 markets from API
2025-11-04 08:15:34,632 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 300/300 markets passed
2025-11-04 08:15:34,632 - market_scanner_v2 - INFO - âœ… Found 300 qualifying markets (from 300 total)
2025-11-04 08:15:34,635 - market_selector - INFO - Selected 3 markets from 300 candidates
2025-11-04 08:15:34,989 - order_manager - INFO - Prepared order for market 664299 with spread 0.0120
2025-11-04 08:15:34,990 - order_manager - INFO - Added order to pending queue: 664299
2025-11-04 08:15:34,990 - __main__ - INFO - Added market 664299 to pending orders
2025-11-04 08:15:35,329 - order_manager - INFO - Prepared order for market 664214 with spread 0.0120
2025-11-04 08:15:35,329 - order_manager - INFO - Added order to pending queue: 664214
2025-11-04 08:15:35,329 - __main__ - INFO - Added market 664214 to pending orders
2025-11-04 08:15:35,673 - order_manager - INFO - Prepared order for market 664211 with spread 0.0120
2025-11-04 08:15:35,673 - order_manager - INFO - Added order to pending queue: 664211
2025-11-04 08:15:35,673 - __main__ - INFO - Added market 664211 to pending orders
2025-11-04 08:15:37,757 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:15:37,758 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:15:39,846 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:15:39,847 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:15:43,236 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:15:43,237 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:15:45,360 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:15:45,361 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:15:45,363 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 08:15:46,385 - market_scanner_v2 - INFO - âœ… Fetched 300 markets from API
2025-11-04 08:15:46,388 - market_scanner_v2 - INFO - âœ… Got 300 markets from API
2025-11-04 08:15:46,390 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 300/300 markets passed
2025-11-04 08:15:46,390 - market_scanner_v2 - INFO - âœ… Found 300 qualifying markets (from 300 total)
2025-11-04 08:15:46,393 - market_selector - INFO - Selected 3 markets from 300 candidates
2025-11-04 08:15:46,737 - order_manager - INFO - Prepared order for market 664299 with spread 0.0120
2025-11-04 08:15:46,737 - order_manager - INFO - Added order to pending queue: 664299
2025-11-04 08:15:46,737 - __main__ - INFO - Added market 664299 to pending orders
2025-11-04 08:15:47,085 - order_manager - INFO - Prepared order for market 664214 with spread 0.0120
2025-11-04 08:15:47,086 - order_manager - INFO - Added order to pending queue: 664214
2025-11-04 08:15:47,086 - __main__ - INFO - Added market 664214 to pending orders
2025-11-04 08:15:47,419 - order_manager - INFO - Prepared order for market 664211 with spread 0.0120
2025-11-04 08:15:47,420 - order_manager - INFO - Added order to pending queue: 664211
2025-11-04 08:15:47,420 - __main__ - INFO - Added market 664211 to pending orders
2025-11-04 08:15:49,485 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:15:49,485 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:15:51,588 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:15:51,589 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:15:54,647 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:15:54,648 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:15:56,756 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:15:56,756 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:15:56,758 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 08:15:59,661 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:15:59,662 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:16:01,808 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:16:01,808 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:16:01,836 - market_scanner_v2 - INFO - âœ… Fetched 300 markets from API
2025-11-04 08:16:04,942 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:16:04,943 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:16:07,044 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:16:07,044 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:16:07,050 - market_scanner_v2 - INFO - âœ… Got 300 markets from API
2025-11-04 08:16:07,052 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 300/300 markets passed
2025-11-04 08:16:07,052 - market_scanner_v2 - INFO - âœ… Found 300 qualifying markets (from 300 total)
2025-11-04 08:16:07,058 - market_selector - INFO - Selected 3 markets from 300 candidates
2025-11-04 08:16:07,406 - order_manager - INFO - Prepared order for market 664299 with spread 0.0120
2025-11-04 08:16:07,406 - order_manager - INFO - Added order to pending queue: 664299
2025-11-04 08:16:07,406 - __main__ - INFO - Added market 664299 to pending orders
2025-11-04 08:16:07,751 - order_manager - INFO - Prepared order for market 664214 with spread 0.0120
2025-11-04 08:16:07,751 - order_manager - INFO - Added order to pending queue: 664214
2025-11-04 08:16:07,752 - __main__ - INFO - Added market 664214 to pending orders
2025-11-04 08:16:08,079 - order_manager - INFO - Prepared order for market 664211 with spread 0.0120
2025-11-04 08:16:08,080 - order_manager - INFO - Added order to pending queue: 664211
2025-11-04 08:16:08,080 - __main__ - INFO - Added market 664211 to pending orders
2025-11-04 08:16:10,389 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:16:10,390 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:16:12,476 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:16:12,476 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:16:12,605 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 08:16:13,630 - market_scanner_v2 - INFO - âœ… Fetched 300 markets from API
2025-11-04 08:16:13,632 - market_scanner_v2 - INFO - âœ… Got 300 markets from API
2025-11-04 08:16:13,633 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 300/300 markets passed
2025-11-04 08:16:13,634 - market_scanner_v2 - INFO - âœ… Found 300 qualifying markets (from 300 total)
2025-11-04 08:16:13,637 - market_selector - INFO - Selected 3 markets from 300 candidates
2025-11-04 08:16:14,028 - order_manager - INFO - Prepared order for market 664299 with spread 0.0120
2025-11-04 08:16:14,028 - order_manager - INFO - Added order to pending queue: 664299
2025-11-04 08:16:14,028 - __main__ - INFO - Added market 664299 to pending orders
2025-11-04 08:16:14,361 - order_manager - INFO - Prepared order for market 664214 with spread 0.0120
2025-11-04 08:16:14,361 - order_manager - INFO - Added order to pending queue: 664214
2025-11-04 08:16:14,361 - __main__ - INFO - Added market 664214 to pending orders
2025-11-04 08:16:14,704 - order_manager - INFO - Prepared order for market 664211 with spread 0.0120
2025-11-04 08:16:14,704 - order_manager - INFO - Added order to pending queue: 664211
2025-11-04 08:16:14,704 - __main__ - INFO - Added market 664211 to pending orders
2025-11-04 08:16:16,769 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:16:16,769 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:16:18,883 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:16:18,883 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:16:19,696 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 08:16:22,266 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:16:22,267 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:16:24,368 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:16:24,368 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:16:24,399 - market_scanner_v2 - INFO - âœ… Fetched 300 markets from API
2025-11-04 08:16:24,401 - market_scanner_v2 - INFO - âœ… Got 300 markets from API
2025-11-04 08:16:24,401 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 300/300 markets passed
2025-11-04 08:16:24,402 - market_scanner_v2 - INFO - âœ… Found 300 qualifying markets (from 300 total)
2025-11-04 08:16:24,404 - market_selector - INFO - Selected 3 markets from 300 candidates
2025-11-04 08:16:24,731 - order_manager - INFO - Prepared order for market 664299 with spread 0.0120
2025-11-04 08:16:24,731 - order_manager - INFO - Added order to pending queue: 664299
2025-11-04 08:16:24,731 - __main__ - INFO - Added market 664299 to pending orders
2025-11-04 08:16:25,084 - order_manager - INFO - Prepared order for market 664214 with spread 0.0120
2025-11-04 08:16:25,085 - order_manager - INFO - Added order to pending queue: 664214
2025-11-04 08:16:25,085 - __main__ - INFO - Added market 664214 to pending orders
2025-11-04 08:16:25,423 - order_manager - INFO - Prepared order for market 664211 with spread 0.0120
2025-11-04 08:16:25,424 - order_manager - INFO - Added order to pending queue: 664211
2025-11-04 08:16:25,424 - __main__ - INFO - Added market 664211 to pending orders
2025-11-04 08:16:27,631 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:16:27,631 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:16:29,705 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:16:29,705 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:16:29,746 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 08:16:30,791 - market_scanner_v2 - INFO - âœ… Fetched 300 markets from API
2025-11-04 08:16:30,793 - market_scanner_v2 - INFO - âœ… Got 300 markets from API
2025-11-04 08:16:30,794 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 300/300 markets passed
2025-11-04 08:16:30,794 - market_scanner_v2 - INFO - âœ… Found 300 qualifying markets (from 300 total)
2025-11-04 08:16:30,797 - market_selector - INFO - Selected 3 markets from 300 candidates
2025-11-04 08:16:31,136 - order_manager - INFO - Prepared order for market 664299 with spread 0.0120
2025-11-04 08:16:31,136 - order_manager - INFO - Added order to pending queue: 664299
2025-11-04 08:16:31,136 - __main__ - INFO - Added market 664299 to pending orders
2025-11-04 08:16:31,497 - order_manager - INFO - Prepared order for market 664214 with spread 0.0120
2025-11-04 08:16:31,498 - order_manager - INFO - Added order to pending queue: 664214
2025-11-04 08:16:31,498 - __main__ - INFO - Added market 664214 to pending orders
2025-11-04 08:16:31,827 - order_manager - INFO - Prepared order for market 664211 with spread 0.0120
2025-11-04 08:16:31,827 - order_manager - INFO - Added order to pending queue: 664211
2025-11-04 08:16:31,828 - __main__ - INFO - Added market 664211 to pending orders
2025-11-04 08:16:33,853 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:16:33,853 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:16:36,001 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:16:36,002 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:16:37,006 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 08:16:39,119 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:16:39,120 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:16:41,217 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:16:41,217 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:16:42,296 - market_scanner_v2 - INFO - âœ… Fetched 300 markets from API
2025-11-04 08:16:42,299 - market_scanner_v2 - INFO - âœ… Got 300 markets from API
2025-11-04 08:16:42,300 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 300/300 markets passed
2025-11-04 08:16:42,300 - market_scanner_v2 - INFO - âœ… Found 300 qualifying markets (from 300 total)
2025-11-04 08:16:42,302 - market_selector - INFO - Selected 3 markets from 300 candidates
2025-11-04 08:16:42,645 - order_manager - INFO - Prepared order for market 664299 with spread 0.0120
2025-11-04 08:16:42,646 - order_manager - INFO - Added order to pending queue: 664299
2025-11-04 08:16:42,646 - __main__ - INFO - Added market 664299 to pending orders
2025-11-04 08:16:42,987 - order_manager - INFO - Prepared order for market 664214 with spread 0.0120
2025-11-04 08:16:42,988 - order_manager - INFO - Added order to pending queue: 664214
2025-11-04 08:16:42,988 - __main__ - INFO - Added market 664214 to pending orders
2025-11-04 08:16:43,331 - order_manager - INFO - Prepared order for market 664211 with spread 0.0120
2025-11-04 08:16:43,331 - order_manager - INFO - Added order to pending queue: 664211
2025-11-04 08:16:43,331 - __main__ - INFO - Added market 664211 to pending orders
2025-11-04 08:16:45,395 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:16:45,395 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:16:47,477 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:16:47,477 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:16:47,479 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 08:16:50,390 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:16:50,390 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:16:52,502 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:16:52,503 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:16:52,530 - market_scanner_v2 - INFO - âœ… Fetched 300 markets from API
2025-11-04 08:16:52,532 - market_scanner_v2 - INFO - âœ… Got 300 markets from API
2025-11-04 08:16:52,533 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 300/300 markets passed
2025-11-04 08:16:52,533 - market_scanner_v2 - INFO - âœ… Found 300 qualifying markets (from 300 total)
2025-11-04 08:16:52,536 - market_selector - INFO - Selected 3 markets from 300 candidates
2025-11-04 08:16:52,866 - order_manager - INFO - Prepared order for market 664299 with spread 0.0120
2025-11-04 08:16:52,866 - order_manager - INFO - Added order to pending queue: 664299
2025-11-04 08:16:52,866 - __main__ - INFO - Added market 664299 to pending orders
2025-11-04 08:16:53,190 - order_manager - INFO - Prepared order for market 664214 with spread 0.0120
2025-11-04 08:16:53,190 - order_manager - INFO - Added order to pending queue: 664214
2025-11-04 08:16:53,191 - __main__ - INFO - Added market 664214 to pending orders
2025-11-04 08:16:53,527 - order_manager - INFO - Prepared order for market 664211 with spread 0.0120
2025-11-04 08:16:53,528 - order_manager - INFO - Added order to pending queue: 664211
2025-11-04 08:16:53,528 - __main__ - INFO - Added market 664211 to pending orders
2025-11-04 08:16:55,572 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:16:55,573 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:16:57,682 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:16:57,683 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:17:00,712 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:17:00,713 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:17:02,809 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:17:02,809 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:17:02,811 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 08:17:03,818 - market_scanner_v2 - INFO - âœ… Fetched 300 markets from API
2025-11-04 08:17:03,820 - market_scanner_v2 - INFO - âœ… Got 300 markets from API
2025-11-04 08:17:03,821 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 300/300 markets passed
2025-11-04 08:17:03,821 - market_scanner_v2 - INFO - âœ… Found 300 qualifying markets (from 300 total)
2025-11-04 08:17:03,824 - market_selector - INFO - Selected 3 markets from 300 candidates
2025-11-04 08:17:04,153 - order_manager - INFO - Prepared order for market 664299 with spread 0.0120
2025-11-04 08:17:04,154 - order_manager - INFO - Added order to pending queue: 664299
2025-11-04 08:17:04,154 - __main__ - INFO - Added market 664299 to pending orders
2025-11-04 08:17:04,489 - order_manager - INFO - Prepared order for market 664214 with spread 0.0120
2025-11-04 08:17:04,489 - order_manager - INFO - Added order to pending queue: 664214
2025-11-04 08:17:04,489 - __main__ - INFO - Added market 664214 to pending orders
2025-11-04 08:17:04,813 - order_manager - INFO - Prepared order for market 664211 with spread 0.0120
2025-11-04 08:17:04,813 - order_manager - INFO - Added order to pending queue: 664211
2025-11-04 08:17:04,813 - __main__ - INFO - Added market 664211 to pending orders
2025-11-04 08:17:06,850 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:17:06,851 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:17:08,987 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:17:08,987 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:17:09,991 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 08:17:12,111 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:17:12,112 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:17:14,185 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:17:14,186 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:17:14,215 - market_scanner_v2 - INFO - âœ… Fetched 300 markets from API
2025-11-04 08:17:14,218 - market_scanner_v2 - INFO - âœ… Got 300 markets from API
2025-11-04 08:17:14,219 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 300/300 markets passed
2025-11-04 08:17:14,219 - market_scanner_v2 - INFO - âœ… Found 300 qualifying markets (from 300 total)
2025-11-04 08:17:14,222 - market_selector - INFO - Selected 3 markets from 300 candidates
2025-11-04 08:17:14,561 - order_manager - INFO - Prepared order for market 664299 with spread 0.0120
2025-11-04 08:17:14,562 - order_manager - INFO - Added order to pending queue: 664299
2025-11-04 08:17:14,562 - __main__ - INFO - Added market 664299 to pending orders
2025-11-04 08:17:14,898 - order_manager - INFO - Prepared order for market 664214 with spread 0.0120
2025-11-04 08:17:14,898 - order_manager - INFO - Added order to pending queue: 664214
2025-11-04 08:17:14,898 - __main__ - INFO - Added market 664214 to pending orders
2025-11-04 08:17:15,231 - order_manager - INFO - Prepared order for market 664211 with spread 0.0120
2025-11-04 08:17:15,232 - order_manager - INFO - Added order to pending queue: 664211
2025-11-04 08:17:15,232 - __main__ - INFO - Added market 664211 to pending orders
2025-11-04 08:17:17,323 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:17:17,324 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:17:19,342 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:17:19,343 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:17:19,345 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 08:17:20,333 - market_scanner_v2 - INFO - âœ… Fetched 276 markets from API
2025-11-04 08:17:20,335 - market_scanner_v2 - INFO - âœ… Got 276 markets from API
2025-11-04 08:17:20,336 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 276/276 markets passed
2025-11-04 08:17:20,336 - market_scanner_v2 - INFO - âœ… Found 276 qualifying markets (from 276 total)
2025-11-04 08:17:20,338 - market_selector - INFO - Selected 3 markets from 276 candidates
2025-11-04 08:17:20,696 - order_manager - INFO - Prepared order for market 664299 with spread 0.0120
2025-11-04 08:17:20,696 - order_manager - INFO - Added order to pending queue: 664299
2025-11-04 08:17:20,696 - __main__ - INFO - Added market 664299 to pending orders
2025-11-04 08:17:21,044 - order_manager - INFO - Prepared order for market 664214 with spread 0.0120
2025-11-04 08:17:21,044 - order_manager - INFO - Added order to pending queue: 664214
2025-11-04 08:17:21,044 - __main__ - INFO - Added market 664214 to pending orders
2025-11-04 08:17:21,382 - order_manager - INFO - Prepared order for market 664211 with spread 0.0120
2025-11-04 08:17:21,383 - order_manager - INFO - Added order to pending queue: 664211
2025-11-04 08:17:21,383 - __main__ - INFO - Added market 664211 to pending orders
2025-11-04 08:17:23,470 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:17:23,471 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:17:25,522 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:17:25,522 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:17:28,158 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:17:28,158 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:17:30,247 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:17:30,247 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:17:30,248 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 08:17:32,881 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:17:32,882 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:17:34,964 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:17:34,964 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:17:34,993 - market_scanner_v2 - INFO - âœ… Fetched 276 markets from API
2025-11-04 08:17:34,995 - market_scanner_v2 - INFO - âœ… Got 276 markets from API
2025-11-04 08:17:34,996 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 276/276 markets passed
2025-11-04 08:17:34,996 - market_scanner_v2 - INFO - âœ… Found 276 qualifying markets (from 276 total)
2025-11-04 08:17:34,999 - market_selector - INFO - Selected 3 markets from 276 candidates
2025-11-04 08:17:35,348 - order_manager - INFO - Prepared order for market 664299 with spread 0.0120
2025-11-04 08:17:35,349 - order_manager - INFO - Added order to pending queue: 664299
2025-11-04 08:17:35,349 - __main__ - INFO - Added market 664299 to pending orders
2025-11-04 08:17:35,686 - order_manager - INFO - Prepared order for market 664214 with spread 0.0120
2025-11-04 08:17:35,687 - order_manager - INFO - Added order to pending queue: 664214
2025-11-04 08:17:35,687 - __main__ - INFO - Added market 664214 to pending orders
2025-11-04 08:17:36,031 - order_manager - INFO - Prepared order for market 664211 with spread 0.0120
2025-11-04 08:17:36,031 - order_manager - INFO - Added order to pending queue: 664211
2025-11-04 08:17:36,031 - __main__ - INFO - Added market 664211 to pending orders
2025-11-04 08:17:38,170 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:17:38,170 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:17:40,293 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:17:40,293 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:17:41,297 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 08:17:43,711 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:17:43,712 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:17:45,779 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:17:45,779 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:17:45,810 - market_scanner_v2 - INFO - âœ… Fetched 276 markets from API
2025-11-04 08:17:45,812 - market_scanner_v2 - INFO - âœ… Got 276 markets from API
2025-11-04 08:17:45,813 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 276/276 markets passed
2025-11-04 08:17:45,813 - market_scanner_v2 - INFO - âœ… Found 276 qualifying markets (from 276 total)
2025-11-04 08:17:45,815 - market_selector - INFO - Selected 3 markets from 276 candidates
2025-11-04 08:17:46,148 - order_manager - INFO - Prepared order for market 664299 with spread 0.0120
2025-11-04 08:17:46,148 - order_manager - INFO - Added order to pending queue: 664299
2025-11-04 08:17:46,148 - __main__ - INFO - Added market 664299 to pending orders
2025-11-04 08:17:46,483 - order_manager - INFO - Prepared order for market 664214 with spread 0.0120
2025-11-04 08:17:46,484 - order_manager - INFO - Added order to pending queue: 664214
2025-11-04 08:17:46,485 - __main__ - INFO - Added market 664214 to pending orders
2025-11-04 08:17:46,855 - order_manager - INFO - Prepared order for market 664211 with spread 0.0120
2025-11-04 08:17:46,855 - order_manager - INFO - Added order to pending queue: 664211
2025-11-04 08:17:46,855 - __main__ - INFO - Added market 664211 to pending orders
2025-11-04 08:17:48,936 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:17:48,937 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:17:51,014 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:17:51,015 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:17:51,131 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 08:17:54,159 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:17:54,159 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:17:56,186 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:17:56,186 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:17:56,210 - market_scanner_v2 - INFO - âœ… Fetched 276 markets from API
2025-11-04 08:17:56,212 - market_scanner_v2 - INFO - âœ… Got 276 markets from API
2025-11-04 08:17:56,213 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 276/276 markets passed
2025-11-04 08:17:56,214 - market_scanner_v2 - INFO - âœ… Found 276 qualifying markets (from 276 total)
2025-11-04 08:17:56,216 - market_selector - INFO - Selected 3 markets from 276 candidates
2025-11-04 08:17:56,552 - order_manager - INFO - Prepared order for market 664299 with spread 0.0120
2025-11-04 08:17:56,553 - order_manager - INFO - Added order to pending queue: 664299
2025-11-04 08:17:56,553 - __main__ - INFO - Added market 664299 to pending orders
2025-11-04 08:17:56,908 - order_manager - INFO - Prepared order for market 664214 with spread 0.0120
2025-11-04 08:17:56,909 - order_manager - INFO - Added order to pending queue: 664214
2025-11-04 08:17:56,909 - __main__ - INFO - Added market 664214 to pending orders
2025-11-04 08:17:57,241 - order_manager - INFO - Prepared order for market 664211 with spread 0.0120
2025-11-04 08:17:57,241 - order_manager - INFO - Added order to pending queue: 664211
2025-11-04 08:17:57,242 - __main__ - INFO - Added market 664211 to pending orders
2025-11-04 08:17:59,588 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:17:59,588 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:18:04,793 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:18:04,794 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:18:04,796 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 08:18:07,922 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:18:07,922 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:18:10,056 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:18:10,057 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

2025-11-04 08:18:10,082 - market_scanner_v2 - INFO - âœ… Fetched 276 markets from API
2025-11-04 08:18:10,085 - market_scanner_v2 - INFO - âœ… Got 276 markets from API
2025-11-04 08:18:10,086 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 276/276 markets passed
2025-11-04 08:18:10,086 - market_scanner_v2 - INFO - âœ… Found 276 qualifying markets (from 276 total)
2025-11-04 08:18:10,088 - market_selector - INFO - Selected 3 markets from 276 candidates
2025-11-04 08:18:10,440 - order_manager - INFO - Prepared order for market 664299 with spread 0.0120
2025-11-04 08:18:10,440 - order_manager - INFO - Added order to pending queue: 664299
2025-11-04 08:18:10,440 - __main__ - INFO - Added market 664299 to pending orders
2025-11-04 08:18:10,783 - order_manager - INFO - Prepared order for market 664214 with spread 0.0120
2025-11-04 08:18:10,783 - order_manager - INFO - Added order to pending queue: 664214
2025-11-04 08:18:10,783 - __main__ - INFO - Added market 664214 to pending orders
2025-11-04 08:18:11,106 - order_manager - INFO - Prepared order for market 664211 with spread 0.0120
2025-11-04 08:18:11,106 - order_manager - INFO - Added order to pending queue: 664211
2025-11-04 08:18:11,106 - __main__ - INFO - Added market 664211 to pending orders
2025-11-04 08:18:14,586 - order_manager - ERROR - Error placing single order: PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]
2025-11-04 08:18:14,586 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 344, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 533, in post_order
    return post("{}{}".format(self.host, POST_ORDER), headers=headers, data=body)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 54, in post
    return request(endpoint, POST, headers, data)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/http_helpers/helpers.py", line 42, in request
    raise PolyApiException(resp)
py_clob_client.exceptions.PolyApiException: PolyApiException[status_code=400, error_message={'error': 'not enough balance / allowance'}]

