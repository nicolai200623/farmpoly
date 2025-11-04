2025-11-04 05:54:01,117 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:54:01,117 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:54:02,092 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:54:02,092 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:54:04,201 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:54:04,201 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:54:05,132 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:54:05,132 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:54:05,772 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 05:54:06,806 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:54:06,807 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:54:07,747 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:54:07,748 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:54:07,773 - market_scanner_v2 - INFO - âœ… Fetched 159 markets from API
2025-11-04 05:54:07,775 - market_scanner_v2 - INFO - âœ… Got 159 markets from API
2025-11-04 05:54:07,776 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 159/159 markets passed
2025-11-04 05:54:07,776 - market_scanner_v2 - INFO - âœ… Found 159 qualifying markets (from 159 total)
2025-11-04 05:54:07,778 - market_selector - INFO - Selected 3 markets from 159 candidates
2025-11-04 05:54:08,066 - order_manager - INFO - Prepared order for market 664311 with spread 0.0120
2025-11-04 05:54:08,066 - order_manager - INFO - Added order to pending queue: 664311
2025-11-04 05:54:08,067 - __main__ - INFO - Added market 664311 to pending orders
2025-11-04 05:54:08,351 - order_manager - INFO - Prepared order for market 664308 with spread 0.0120
2025-11-04 05:54:08,352 - order_manager - INFO - Added order to pending queue: 664308
2025-11-04 05:54:08,352 - __main__ - INFO - Added market 664308 to pending orders
2025-11-04 05:54:08,631 - order_manager - INFO - Prepared order for market 664305 with spread 0.0132
2025-11-04 05:54:08,631 - order_manager - INFO - Added order to pending queue: 664305
2025-11-04 05:54:08,632 - __main__ - INFO - Added market 664305 to pending orders
2025-11-04 05:54:09,777 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:54:09,777 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:54:10,708 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:54:10,709 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:54:12,272 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:54:12,273 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:54:13,186 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:54:13,186 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:54:15,438 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:54:15,439 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:54:16,392 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:54:16,393 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:54:16,393 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 05:54:17,323 - market_scanner_v2 - INFO - âœ… Fetched 159 markets from API
2025-11-04 05:54:17,325 - market_scanner_v2 - INFO - âœ… Got 159 markets from API
2025-11-04 05:54:17,326 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 159/159 markets passed
2025-11-04 05:54:17,326 - market_scanner_v2 - INFO - âœ… Found 159 qualifying markets (from 159 total)
2025-11-04 05:54:17,328 - market_selector - INFO - Selected 3 markets from 159 candidates
2025-11-04 05:54:17,611 - order_manager - INFO - Prepared order for market 664311 with spread 0.0120
2025-11-04 05:54:17,612 - order_manager - INFO - Added order to pending queue: 664311
2025-11-04 05:54:17,613 - __main__ - INFO - Added market 664311 to pending orders
2025-11-04 05:54:17,970 - order_manager - INFO - Prepared order for market 664308 with spread 0.0120
2025-11-04 05:54:17,970 - order_manager - INFO - Added order to pending queue: 664308
2025-11-04 05:54:17,971 - __main__ - INFO - Added market 664308 to pending orders
2025-11-04 05:54:18,254 - order_manager - INFO - Prepared order for market 664305 with spread 0.0132
2025-11-04 05:54:18,255 - order_manager - INFO - Added order to pending queue: 664305
2025-11-04 05:54:18,255 - __main__ - INFO - Added market 664305 to pending orders
2025-11-04 05:54:19,530 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:54:19,531 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:54:20,408 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:54:20,409 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:54:22,792 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:54:22,792 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:54:23,700 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:54:23,700 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:54:23,781 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 05:54:24,724 - market_scanner_v2 - INFO - âœ… Fetched 159 markets from API
2025-11-04 05:54:24,727 - market_scanner_v2 - INFO - âœ… Got 159 markets from API
2025-11-04 05:54:24,729 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 159/159 markets passed
2025-11-04 05:54:24,729 - market_scanner_v2 - INFO - âœ… Found 159 qualifying markets (from 159 total)
2025-11-04 05:54:24,732 - market_selector - INFO - Selected 3 markets from 159 candidates
2025-11-04 05:54:25,018 - order_manager - INFO - Prepared order for market 664311 with spread 0.0120
2025-11-04 05:54:25,019 - order_manager - INFO - Added order to pending queue: 664311
2025-11-04 05:54:25,019 - __main__ - INFO - Added market 664311 to pending orders
2025-11-04 05:54:25,330 - order_manager - INFO - Prepared order for market 664308 with spread 0.0120
2025-11-04 05:54:25,330 - order_manager - INFO - Added order to pending queue: 664308
2025-11-04 05:54:25,331 - __main__ - INFO - Added market 664308 to pending orders
2025-11-04 05:54:25,614 - order_manager - INFO - Prepared order for market 664305 with spread 0.0132
2025-11-04 05:54:25,615 - order_manager - INFO - Added order to pending queue: 664305
2025-11-04 05:54:25,615 - __main__ - INFO - Added market 664305 to pending orders
2025-11-04 05:54:26,559 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:54:26,559 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:54:27,430 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:54:27,430 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:54:29,751 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:54:29,751 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:54:30,693 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:54:30,694 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:54:31,482 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 05:54:32,600 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:54:32,601 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:54:33,474 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:54:33,474 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:54:33,501 - market_scanner_v2 - INFO - âœ… Fetched 159 markets from API
2025-11-04 05:54:33,504 - market_scanner_v2 - INFO - âœ… Got 159 markets from API
2025-11-04 05:54:33,505 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 159/159 markets passed
2025-11-04 05:54:33,505 - market_scanner_v2 - INFO - âœ… Found 159 qualifying markets (from 159 total)
2025-11-04 05:54:33,507 - market_selector - INFO - Selected 3 markets from 159 candidates
2025-11-04 05:54:33,796 - order_manager - INFO - Prepared order for market 664311 with spread 0.0120
2025-11-04 05:54:33,797 - order_manager - INFO - Added order to pending queue: 664311
2025-11-04 05:54:33,797 - __main__ - INFO - Added market 664311 to pending orders
2025-11-04 05:54:34,157 - order_manager - INFO - Prepared order for market 664308 with spread 0.0120
2025-11-04 05:54:34,158 - order_manager - INFO - Added order to pending queue: 664308
2025-11-04 05:54:34,158 - __main__ - INFO - Added market 664308 to pending orders
2025-11-04 05:54:34,511 - order_manager - INFO - Prepared order for market 664305 with spread 0.0120
2025-11-04 05:54:34,512 - order_manager - INFO - Added order to pending queue: 664305
2025-11-04 05:54:34,512 - __main__ - INFO - Added market 664305 to pending orders
2025-11-04 05:54:35,803 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:54:35,803 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:54:36,690 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:54:36,690 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:54:38,654 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:54:38,655 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:54:39,544 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:54:39,544 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:54:40,982 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:54:40,983 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:54:41,874 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:54:41,875 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:54:41,875 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 05:54:43,475 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:54:43,475 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:54:44,322 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:54:44,323 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:54:44,344 - market_scanner_v2 - INFO - âœ… Fetched 159 markets from API
2025-11-04 05:54:45,348 - market_scanner_v2 - INFO - âœ… Got 159 markets from API
2025-11-04 05:54:45,349 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 159/159 markets passed
2025-11-04 05:54:45,349 - market_scanner_v2 - INFO - âœ… Found 159 qualifying markets (from 159 total)
2025-11-04 05:54:45,352 - market_selector - INFO - Selected 3 markets from 159 candidates
2025-11-04 05:54:45,628 - order_manager - INFO - Prepared order for market 664311 with spread 0.0120
2025-11-04 05:54:45,628 - order_manager - INFO - Added order to pending queue: 664311
2025-11-04 05:54:45,628 - __main__ - INFO - Added market 664311 to pending orders
2025-11-04 05:54:45,917 - order_manager - INFO - Prepared order for market 664308 with spread 0.0120
2025-11-04 05:54:45,918 - order_manager - INFO - Added order to pending queue: 664308
2025-11-04 05:54:45,918 - __main__ - INFO - Added market 664308 to pending orders
2025-11-04 05:54:46,741 - order_manager - INFO - Prepared order for market 664305 with spread 0.0120
2025-11-04 05:54:46,742 - order_manager - INFO - Added order to pending queue: 664305
2025-11-04 05:54:46,742 - __main__ - INFO - Added market 664305 to pending orders
2025-11-04 05:54:47,583 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:54:47,584 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:54:48,656 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:54:48,656 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:54:50,204 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:54:50,204 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:54:51,210 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:54:51,211 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:54:51,375 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 05:54:53,194 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:54:53,195 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:54:54,055 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:54:54,055 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:54:54,081 - market_scanner_v2 - INFO - âœ… Fetched 159 markets from API
2025-11-04 05:54:54,084 - market_scanner_v2 - INFO - âœ… Got 159 markets from API
2025-11-04 05:54:54,086 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 159/159 markets passed
2025-11-04 05:54:54,086 - market_scanner_v2 - INFO - âœ… Found 159 qualifying markets (from 159 total)
2025-11-04 05:54:54,088 - market_selector - INFO - Selected 3 markets from 159 candidates
2025-11-04 05:54:54,383 - order_manager - INFO - Prepared order for market 664311 with spread 0.0120
2025-11-04 05:54:54,384 - order_manager - INFO - Added order to pending queue: 664311
2025-11-04 05:54:54,384 - __main__ - INFO - Added market 664311 to pending orders
2025-11-04 05:54:54,660 - order_manager - INFO - Prepared order for market 664308 with spread 0.0120
2025-11-04 05:54:54,660 - order_manager - INFO - Added order to pending queue: 664308
2025-11-04 05:54:54,660 - __main__ - INFO - Added market 664308 to pending orders
2025-11-04 05:54:54,943 - order_manager - INFO - Prepared order for market 664305 with spread 0.0120
2025-11-04 05:54:54,943 - order_manager - INFO - Added order to pending queue: 664305
2025-11-04 05:54:54,943 - __main__ - INFO - Added market 664305 to pending orders
2025-11-04 05:54:56,017 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:54:56,017 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:54:56,893 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:54:56,894 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:54:58,488 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:54:58,488 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:54:59,366 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:54:59,366 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:54:59,366 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 05:55:00,236 - market_scanner_v2 - INFO - âœ… Fetched 159 markets from API
2025-11-04 05:55:00,240 - market_scanner_v2 - INFO - âœ… Got 159 markets from API
2025-11-04 05:55:00,241 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 159/159 markets passed
2025-11-04 05:55:00,242 - market_scanner_v2 - INFO - âœ… Found 159 qualifying markets (from 159 total)
2025-11-04 05:55:00,244 - market_selector - INFO - Selected 3 markets from 159 candidates
2025-11-04 05:55:00,526 - order_manager - INFO - Prepared order for market 664311 with spread 0.0120
2025-11-04 05:55:00,527 - order_manager - INFO - Added order to pending queue: 664311
2025-11-04 05:55:00,527 - __main__ - INFO - Added market 664311 to pending orders
2025-11-04 05:55:00,821 - order_manager - INFO - Prepared order for market 664308 with spread 0.0120
2025-11-04 05:55:00,823 - order_manager - INFO - Added order to pending queue: 664308
2025-11-04 05:55:00,823 - __main__ - INFO - Added market 664308 to pending orders
2025-11-04 05:55:01,130 - order_manager - INFO - Prepared order for market 664305 with spread 0.0120
2025-11-04 05:55:01,130 - order_manager - INFO - Added order to pending queue: 664305
2025-11-04 05:55:01,130 - __main__ - INFO - Added market 664305 to pending orders
2025-11-04 05:55:02,231 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:55:02,231 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:55:03,340 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:55:03,340 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:55:05,400 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:55:05,400 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:55:06,336 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:55:06,337 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:55:06,407 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 05:55:08,854 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:55:08,855 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:55:09,820 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:55:09,821 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:55:09,845 - market_scanner_v2 - INFO - âœ… Fetched 159 markets from API
2025-11-04 05:55:09,849 - market_scanner_v2 - INFO - âœ… Got 159 markets from API
2025-11-04 05:55:09,850 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 159/159 markets passed
2025-11-04 05:55:09,851 - market_scanner_v2 - INFO - âœ… Found 159 qualifying markets (from 159 total)
2025-11-04 05:55:09,854 - market_selector - INFO - Selected 3 markets from 159 candidates
2025-11-04 05:55:10,153 - order_manager - INFO - Prepared order for market 664311 with spread 0.0120
2025-11-04 05:55:10,153 - order_manager - INFO - Added order to pending queue: 664311
2025-11-04 05:55:10,153 - __main__ - INFO - Added market 664311 to pending orders
2025-11-04 05:55:10,470 - order_manager - INFO - Prepared order for market 664308 with spread 0.0120
2025-11-04 05:55:10,471 - order_manager - INFO - Added order to pending queue: 664308
2025-11-04 05:55:10,471 - __main__ - INFO - Added market 664308 to pending orders
2025-11-04 05:55:10,756 - order_manager - INFO - Prepared order for market 664305 with spread 0.0120
2025-11-04 05:55:10,756 - order_manager - INFO - Added order to pending queue: 664305
2025-11-04 05:55:10,756 - __main__ - INFO - Added market 664305 to pending orders
2025-11-04 05:55:12,051 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:55:12,051 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:55:12,925 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:55:12,926 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:55:14,764 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:55:14,764 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:55:16,739 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:55:16,739 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:55:17,742 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 05:55:18,898 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:55:18,899 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:55:19,758 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:55:19,759 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:55:19,787 - market_scanner_v2 - INFO - âœ… Fetched 159 markets from API
2025-11-04 05:55:19,789 - market_scanner_v2 - INFO - âœ… Got 159 markets from API
2025-11-04 05:55:19,790 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 159/159 markets passed
2025-11-04 05:55:19,791 - market_scanner_v2 - INFO - âœ… Found 159 qualifying markets (from 159 total)
2025-11-04 05:55:19,793 - market_selector - INFO - Selected 3 markets from 159 candidates
2025-11-04 05:55:20,075 - order_manager - INFO - Prepared order for market 664311 with spread 0.0120
2025-11-04 05:55:20,076 - order_manager - INFO - Added order to pending queue: 664311
2025-11-04 05:55:20,076 - __main__ - INFO - Added market 664311 to pending orders
2025-11-04 05:55:20,368 - order_manager - INFO - Prepared order for market 664308 with spread 0.0120
2025-11-04 05:55:20,369 - order_manager - INFO - Added order to pending queue: 664308
2025-11-04 05:55:20,369 - __main__ - INFO - Added market 664308 to pending orders
2025-11-04 05:55:20,644 - order_manager - INFO - Prepared order for market 664305 with spread 0.0120
2025-11-04 05:55:20,644 - order_manager - INFO - Added order to pending queue: 664305
2025-11-04 05:55:20,644 - __main__ - INFO - Added market 664305 to pending orders
2025-11-04 05:55:21,525 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:55:21,526 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:55:22,449 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:55:22,450 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:55:24,226 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:55:24,226 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:55:25,114 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:55:25,115 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:55:26,747 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:55:26,747 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:55:27,685 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:55:27,686 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:55:27,686 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 05:55:29,818 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:55:29,818 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:55:30,756 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:55:30,760 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:55:30,795 - market_scanner_v2 - INFO - âœ… Fetched 159 markets from API
2025-11-04 05:55:30,799 - market_scanner_v2 - INFO - âœ… Got 159 markets from API
2025-11-04 05:55:30,801 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 159/159 markets passed
2025-11-04 05:55:30,802 - market_scanner_v2 - INFO - âœ… Found 159 qualifying markets (from 159 total)
2025-11-04 05:55:30,806 - market_selector - INFO - Selected 3 markets from 159 candidates
2025-11-04 05:55:31,148 - order_manager - INFO - Prepared order for market 664311 with spread 0.0120
2025-11-04 05:55:31,149 - order_manager - INFO - Added order to pending queue: 664311
2025-11-04 05:55:31,149 - __main__ - INFO - Added market 664311 to pending orders
2025-11-04 05:55:31,471 - order_manager - INFO - Prepared order for market 664308 with spread 0.0120
2025-11-04 05:55:31,472 - order_manager - INFO - Added order to pending queue: 664308
2025-11-04 05:55:31,473 - __main__ - INFO - Added market 664308 to pending orders
2025-11-04 05:55:31,864 - order_manager - INFO - Prepared order for market 664305 with spread 0.0120
2025-11-04 05:55:31,864 - order_manager - INFO - Added order to pending queue: 664305
2025-11-04 05:55:31,865 - __main__ - INFO - Added market 664305 to pending orders
2025-11-04 05:55:33,199 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:55:33,200 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:55:34,277 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:55:34,278 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:55:36,756 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:55:36,756 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:55:38,010 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:55:38,011 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:55:38,011 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 05:55:39,990 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:55:39,991 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:55:41,297 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:55:41,298 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:55:41,359 - market_scanner_v2 - INFO - âœ… Fetched 159 markets from API
2025-11-04 05:55:41,368 - market_scanner_v2 - INFO - âœ… Got 159 markets from API
2025-11-04 05:55:41,372 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 159/159 markets passed
2025-11-04 05:55:41,372 - market_scanner_v2 - INFO - âœ… Found 159 qualifying markets (from 159 total)
2025-11-04 05:55:41,380 - market_selector - INFO - Selected 3 markets from 159 candidates
2025-11-04 05:55:41,784 - order_manager - INFO - Prepared order for market 664311 with spread 0.0120
2025-11-04 05:55:41,784 - order_manager - INFO - Added order to pending queue: 664311
2025-11-04 05:55:41,785 - __main__ - INFO - Added market 664311 to pending orders
2025-11-04 05:55:42,097 - order_manager - INFO - Prepared order for market 664308 with spread 0.0120
2025-11-04 05:55:42,099 - order_manager - INFO - Added order to pending queue: 664308
2025-11-04 05:55:42,099 - __main__ - INFO - Added market 664308 to pending orders
2025-11-04 05:55:42,508 - order_manager - INFO - Prepared order for market 664305 with spread 0.0120
2025-11-04 05:55:42,509 - order_manager - INFO - Added order to pending queue: 664305
2025-11-04 05:55:42,509 - __main__ - INFO - Added market 664305 to pending orders
2025-11-04 05:55:43,634 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:55:43,634 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:55:44,782 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:55:44,783 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:55:46,278 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:55:46,279 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:55:47,249 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:55:47,249 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:55:47,249 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 05:55:48,777 - market_scanner_v2 - INFO - âœ… Fetched 159 markets from API
2025-11-04 05:55:49,753 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:55:49,754 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:55:50,816 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:55:50,816 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:55:50,818 - market_scanner_v2 - INFO - âœ… Got 159 markets from API
2025-11-04 05:55:50,819 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 159/159 markets passed
2025-11-04 05:55:50,819 - market_scanner_v2 - INFO - âœ… Found 159 qualifying markets (from 159 total)
2025-11-04 05:55:50,821 - market_selector - INFO - Selected 3 markets from 159 candidates
2025-11-04 05:55:51,101 - order_manager - INFO - Prepared order for market 664311 with spread 0.0120
2025-11-04 05:55:51,101 - order_manager - INFO - Added order to pending queue: 664311
2025-11-04 05:55:51,101 - __main__ - INFO - Added market 664311 to pending orders
2025-11-04 05:55:51,378 - order_manager - INFO - Prepared order for market 664308 with spread 0.0120
2025-11-04 05:55:51,379 - order_manager - INFO - Added order to pending queue: 664308
2025-11-04 05:55:51,379 - __main__ - INFO - Added market 664308 to pending orders
2025-11-04 05:55:51,692 - order_manager - INFO - Prepared order for market 664305 with spread 0.0120
2025-11-04 05:55:51,692 - order_manager - INFO - Added order to pending queue: 664305
2025-11-04 05:55:51,692 - __main__ - INFO - Added market 664305 to pending orders
2025-11-04 05:55:53,124 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:55:53,124 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:55:54,314 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:55:54,315 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:55:56,771 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:55:56,772 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:55:58,732 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:55:58,733 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:55:58,733 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 05:55:59,661 - market_scanner_v2 - INFO - âœ… Fetched 159 markets from API
2025-11-04 05:55:59,673 - market_scanner_v2 - INFO - âœ… Got 159 markets from API
2025-11-04 05:55:59,676 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 159/159 markets passed
2025-11-04 05:55:59,676 - market_scanner_v2 - INFO - âœ… Found 159 qualifying markets (from 159 total)
2025-11-04 05:55:59,681 - market_selector - INFO - Selected 3 markets from 159 candidates
2025-11-04 05:56:00,170 - order_manager - INFO - Prepared order for market 664311 with spread 0.0120
2025-11-04 05:56:00,170 - order_manager - INFO - Added order to pending queue: 664311
2025-11-04 05:56:00,170 - __main__ - INFO - Added market 664311 to pending orders
2025-11-04 05:56:00,639 - order_manager - INFO - Prepared order for market 664308 with spread 0.0120
2025-11-04 05:56:00,648 - order_manager - INFO - Added order to pending queue: 664308
2025-11-04 05:56:00,648 - __main__ - INFO - Added market 664308 to pending orders
2025-11-04 05:56:01,147 - order_manager - INFO - Prepared order for market 664305 with spread 0.0120
2025-11-04 05:56:01,147 - order_manager - INFO - Added order to pending queue: 664305
2025-11-04 05:56:01,147 - __main__ - INFO - Added market 664305 to pending orders
2025-11-04 05:56:02,414 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:56:02,418 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:56:04,216 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:56:04,217 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:56:06,363 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:56:06,365 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:56:07,834 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:56:07,834 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:56:07,835 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 05:56:08,436 - market_scanner_v2 - INFO - âœ… Fetched 159 markets from API
2025-11-04 05:56:08,444 - market_scanner_v2 - INFO - âœ… Got 159 markets from API
2025-11-04 05:56:08,445 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 159/159 markets passed
2025-11-04 05:56:08,445 - market_scanner_v2 - INFO - âœ… Found 159 qualifying markets (from 159 total)
2025-11-04 05:56:08,451 - market_selector - INFO - Selected 3 markets from 159 candidates
2025-11-04 05:56:08,917 - order_manager - INFO - Prepared order for market 664311 with spread 0.0120
2025-11-04 05:56:08,917 - order_manager - INFO - Added order to pending queue: 664311
2025-11-04 05:56:08,917 - __main__ - INFO - Added market 664311 to pending orders
2025-11-04 05:56:09,475 - order_manager - INFO - Prepared order for market 664308 with spread 0.0120
2025-11-04 05:56:09,475 - order_manager - INFO - Added order to pending queue: 664308
2025-11-04 05:56:09,476 - __main__ - INFO - Added market 664308 to pending orders
2025-11-04 05:56:09,842 - order_manager - INFO - Prepared order for market 664305 with spread 0.0120
2025-11-04 05:56:09,843 - order_manager - INFO - Added order to pending queue: 664305
2025-11-04 05:56:09,843 - __main__ - INFO - Added market 664305 to pending orders
2025-11-04 05:56:11,110 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:56:11,111 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:56:12,536 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:56:12,536 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:56:15,422 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:56:15,423 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:56:16,372 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:56:16,373 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:56:16,373 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 05:56:17,087 - market_scanner_v2 - INFO - âœ… Fetched 159 markets from API
2025-11-04 05:56:17,090 - market_scanner_v2 - INFO - âœ… Got 159 markets from API
2025-11-04 05:56:17,091 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 159/159 markets passed
2025-11-04 05:56:17,091 - market_scanner_v2 - INFO - âœ… Found 159 qualifying markets (from 159 total)
2025-11-04 05:56:17,094 - market_selector - INFO - Selected 3 markets from 159 candidates
2025-11-04 05:56:17,383 - order_manager - INFO - Prepared order for market 664311 with spread 0.0120
2025-11-04 05:56:17,383 - order_manager - INFO - Added order to pending queue: 664311
2025-11-04 05:56:17,383 - __main__ - INFO - Added market 664311 to pending orders
2025-11-04 05:56:17,735 - order_manager - INFO - Prepared order for market 664308 with spread 0.0120
2025-11-04 05:56:17,735 - order_manager - INFO - Added order to pending queue: 664308
2025-11-04 05:56:17,735 - __main__ - INFO - Added market 664308 to pending orders
2025-11-04 05:56:18,052 - order_manager - INFO - Prepared order for market 664305 with spread 0.0120
2025-11-04 05:56:18,053 - order_manager - INFO - Added order to pending queue: 664305
2025-11-04 05:56:18,053 - __main__ - INFO - Added market 664305 to pending orders
2025-11-04 05:56:19,042 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:56:19,042 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:56:20,003 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:56:20,003 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:56:21,888 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:56:21,888 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:56:22,830 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:56:22,831 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:56:23,395 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 05:56:25,015 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:56:25,016 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:56:26,001 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:56:26,009 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:56:26,059 - market_scanner_v2 - INFO - âœ… Fetched 159 markets from API
2025-11-04 05:56:26,061 - market_scanner_v2 - INFO - âœ… Got 159 markets from API
2025-11-04 05:56:26,063 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 159/159 markets passed
2025-11-04 05:56:26,063 - market_scanner_v2 - INFO - âœ… Found 159 qualifying markets (from 159 total)
2025-11-04 05:56:26,065 - market_selector - INFO - Selected 3 markets from 159 candidates
2025-11-04 05:56:26,416 - order_manager - INFO - Prepared order for market 664311 with spread 0.0120
2025-11-04 05:56:26,416 - order_manager - INFO - Added order to pending queue: 664311
2025-11-04 05:56:26,416 - __main__ - INFO - Added market 664311 to pending orders
2025-11-04 05:56:26,689 - order_manager - INFO - Prepared order for market 664308 with spread 0.0120
2025-11-04 05:56:26,690 - order_manager - INFO - Added order to pending queue: 664308
2025-11-04 05:56:26,690 - __main__ - INFO - Added market 664308 to pending orders
2025-11-04 05:56:26,979 - order_manager - INFO - Prepared order for market 664305 with spread 0.0120
2025-11-04 05:56:26,980 - order_manager - INFO - Added order to pending queue: 664305
2025-11-04 05:56:26,980 - __main__ - INFO - Added market 664305 to pending orders
2025-11-04 05:56:28,098 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:56:28,098 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:56:29,095 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:56:29,095 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:56:30,862 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:56:30,863 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:56:31,856 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:56:31,857 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:56:32,066 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 05:56:32,687 - market_scanner_v2 - INFO - âœ… Fetched 159 markets from API
2025-11-04 05:56:32,691 - market_scanner_v2 - INFO - âœ… Got 159 markets from API
2025-11-04 05:56:32,692 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 159/159 markets passed
2025-11-04 05:56:32,692 - market_scanner_v2 - INFO - âœ… Found 159 qualifying markets (from 159 total)
2025-11-04 05:56:32,695 - market_selector - INFO - Selected 3 markets from 159 candidates
2025-11-04 05:56:32,988 - order_manager - INFO - Prepared order for market 664311 with spread 0.0120
2025-11-04 05:56:32,988 - order_manager - INFO - Added order to pending queue: 664311
2025-11-04 05:56:32,988 - __main__ - INFO - Added market 664311 to pending orders
2025-11-04 05:56:33,289 - order_manager - INFO - Prepared order for market 664308 with spread 0.0120
2025-11-04 05:56:33,290 - order_manager - INFO - Added order to pending queue: 664308
2025-11-04 05:56:33,290 - __main__ - INFO - Added market 664308 to pending orders
2025-11-04 05:56:33,569 - order_manager - INFO - Prepared order for market 664305 with spread 0.0120
2025-11-04 05:56:33,570 - order_manager - INFO - Added order to pending queue: 664305
2025-11-04 05:56:33,570 - __main__ - INFO - Added market 664305 to pending orders
2025-11-04 05:56:34,668 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:56:34,668 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:56:35,534 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:56:35,534 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:56:37,027 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:56:37,028 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:56:37,926 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:56:37,927 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:56:38,560 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 05:56:39,643 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:56:39,643 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:56:40,750 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:56:40,750 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:56:40,778 - market_scanner_v2 - INFO - âœ… Fetched 159 markets from API
2025-11-04 05:56:40,781 - market_scanner_v2 - INFO - âœ… Got 159 markets from API
2025-11-04 05:56:40,782 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 159/159 markets passed
2025-11-04 05:56:40,782 - market_scanner_v2 - INFO - âœ… Found 159 qualifying markets (from 159 total)
2025-11-04 05:56:40,784 - market_selector - INFO - Selected 3 markets from 159 candidates
2025-11-04 05:56:41,097 - order_manager - INFO - Prepared order for market 664311 with spread 0.0120
2025-11-04 05:56:41,098 - order_manager - INFO - Added order to pending queue: 664311
2025-11-04 05:56:41,098 - __main__ - INFO - Added market 664311 to pending orders
2025-11-04 05:56:41,380 - order_manager - INFO - Prepared order for market 664308 with spread 0.0120
2025-11-04 05:56:41,381 - order_manager - INFO - Added order to pending queue: 664308
2025-11-04 05:56:41,381 - __main__ - INFO - Added market 664308 to pending orders
2025-11-04 05:56:41,677 - order_manager - INFO - Prepared order for market 664305 with spread 0.0120
2025-11-04 05:56:41,677 - order_manager - INFO - Added order to pending queue: 664305
2025-11-04 05:56:41,678 - __main__ - INFO - Added market 664305 to pending orders
2025-11-04 05:56:42,716 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:56:42,717 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:56:43,761 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:56:43,762 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:56:45,870 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:56:45,871 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:56:46,859 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:56:46,860 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:56:46,860 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 05:56:48,372 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:56:48,372 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:56:49,252 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:56:49,253 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:56:49,278 - market_scanner_v2 - INFO - âœ… Fetched 159 markets from API
2025-11-04 05:56:49,280 - market_scanner_v2 - INFO - âœ… Got 159 markets from API
2025-11-04 05:56:49,281 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 159/159 markets passed
2025-11-04 05:56:49,281 - market_scanner_v2 - INFO - âœ… Found 159 qualifying markets (from 159 total)
2025-11-04 05:56:49,284 - market_selector - INFO - Selected 3 markets from 159 candidates
2025-11-04 05:56:49,594 - order_manager - INFO - Prepared order for market 664311 with spread 0.0120
2025-11-04 05:56:49,595 - order_manager - INFO - Added order to pending queue: 664311
2025-11-04 05:56:49,595 - __main__ - INFO - Added market 664311 to pending orders
2025-11-04 05:56:49,957 - order_manager - INFO - Prepared order for market 664308 with spread 0.0132
2025-11-04 05:56:49,958 - order_manager - INFO - Added order to pending queue: 664308
2025-11-04 05:56:49,958 - __main__ - INFO - Added market 664308 to pending orders
2025-11-04 05:56:50,253 - order_manager - INFO - Prepared order for market 664305 with spread 0.0120
2025-11-04 05:56:50,255 - order_manager - INFO - Added order to pending queue: 664305
2025-11-04 05:56:50,255 - __main__ - INFO - Added market 664305 to pending orders
2025-11-04 05:56:51,452 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:56:51,452 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:56:52,468 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:56:52,468 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:56:54,470 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:56:54,470 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:56:55,348 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:56:55,348 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:56:55,938 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 05:56:57,406 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:56:57,406 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:56:58,366 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:56:58,367 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:56:58,395 - market_scanner_v2 - INFO - âœ… Fetched 159 markets from API
2025-11-04 05:56:58,400 - market_scanner_v2 - INFO - âœ… Got 159 markets from API
2025-11-04 05:56:58,401 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 159/159 markets passed
2025-11-04 05:56:58,401 - market_scanner_v2 - INFO - âœ… Found 159 qualifying markets (from 159 total)
2025-11-04 05:56:58,404 - market_selector - INFO - Selected 3 markets from 159 candidates
2025-11-04 05:56:58,701 - order_manager - INFO - Prepared order for market 664214 with spread 0.0120
2025-11-04 05:56:58,702 - order_manager - INFO - Added order to pending queue: 664214
2025-11-04 05:56:58,702 - __main__ - INFO - Added market 664214 to pending orders
2025-11-04 05:56:58,982 - order_manager - INFO - Prepared order for market 664311 with spread 0.0120
2025-11-04 05:56:58,983 - order_manager - INFO - Added order to pending queue: 664311
2025-11-04 05:56:58,983 - __main__ - INFO - Added market 664311 to pending orders
2025-11-04 05:56:59,270 - order_manager - INFO - Prepared order for market 664308 with spread 0.0120
2025-11-04 05:56:59,271 - order_manager - INFO - Added order to pending queue: 664308
2025-11-04 05:56:59,271 - __main__ - INFO - Added market 664308 to pending orders
2025-11-04 05:57:00,160 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:57:00,161 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:57:01,014 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:57:01,014 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:57:02,939 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:57:02,940 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:57:05,088 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 05:57:05,660 - market_scanner_v2 - INFO - âœ… Fetched 159 markets from API
2025-11-04 05:57:05,662 - market_scanner_v2 - INFO - âœ… Got 159 markets from API
2025-11-04 05:57:05,663 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 159/159 markets passed
2025-11-04 05:57:05,663 - market_scanner_v2 - INFO - âœ… Found 159 qualifying markets (from 159 total)
2025-11-04 05:57:05,666 - market_selector - INFO - Selected 3 markets from 159 candidates
2025-11-04 05:57:05,947 - order_manager - INFO - Prepared order for market 664214 with spread 0.0120
2025-11-04 05:57:05,947 - order_manager - INFO - Added order to pending queue: 664214
2025-11-04 05:57:05,947 - __main__ - INFO - Added market 664214 to pending orders
2025-11-04 05:57:06,227 - order_manager - INFO - Prepared order for market 664311 with spread 0.0120
2025-11-04 05:57:06,227 - order_manager - INFO - Added order to pending queue: 664311
2025-11-04 05:57:06,227 - __main__ - INFO - Added market 664311 to pending orders
2025-11-04 05:57:06,497 - order_manager - INFO - Prepared order for market 664308 with spread 0.0120
2025-11-04 05:57:06,498 - order_manager - INFO - Added order to pending queue: 664308
2025-11-04 05:57:06,498 - __main__ - INFO - Added market 664308 to pending orders
2025-11-04 05:57:07,870 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:57:07,870 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:57:09,938 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:57:09,938 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:57:10,807 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:57:10,807 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:57:12,514 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:57:12,514 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:57:13,421 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:57:13,422 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:57:13,422 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 05:57:14,505 - market_scanner_v2 - INFO - âœ… Fetched 159 markets from API
2025-11-04 05:57:14,510 - market_scanner_v2 - INFO - âœ… Got 159 markets from API
2025-11-04 05:57:14,511 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 159/159 markets passed
2025-11-04 05:57:14,511 - market_scanner_v2 - INFO - âœ… Found 159 qualifying markets (from 159 total)
2025-11-04 05:57:14,514 - market_selector - INFO - Selected 3 markets from 159 candidates
2025-11-04 05:57:14,804 - order_manager - INFO - Prepared order for market 664214 with spread 0.0120
2025-11-04 05:57:14,804 - order_manager - INFO - Added order to pending queue: 664214
2025-11-04 05:57:14,805 - __main__ - INFO - Added market 664214 to pending orders
2025-11-04 05:57:15,083 - order_manager - INFO - Prepared order for market 664311 with spread 0.0120
2025-11-04 05:57:15,084 - order_manager - INFO - Added order to pending queue: 664311
2025-11-04 05:57:15,084 - __main__ - INFO - Added market 664311 to pending orders
2025-11-04 05:57:15,360 - order_manager - INFO - Prepared order for market 664308 with spread 0.0120
2025-11-04 05:57:15,361 - order_manager - INFO - Added order to pending queue: 664308
2025-11-04 05:57:15,361 - __main__ - INFO - Added market 664308 to pending orders
2025-11-04 05:57:16,251 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:57:16,251 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:57:17,244 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:57:17,244 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:57:19,491 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:57:19,491 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:57:20,399 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:57:20,400 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:57:21,054 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 05:57:22,289 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:57:22,290 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:57:23,162 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:57:23,163 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:57:23,196 - market_scanner_v2 - INFO - âœ… Fetched 159 markets from API
2025-11-04 05:57:23,199 - market_scanner_v2 - INFO - âœ… Got 159 markets from API
2025-11-04 05:57:23,201 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 159/159 markets passed
2025-11-04 05:57:23,201 - market_scanner_v2 - INFO - âœ… Found 159 qualifying markets (from 159 total)
2025-11-04 05:57:23,203 - market_selector - INFO - Selected 3 markets from 159 candidates
2025-11-04 05:57:23,494 - order_manager - INFO - Prepared order for market 664214 with spread 0.0120
2025-11-04 05:57:23,495 - order_manager - INFO - Added order to pending queue: 664214
2025-11-04 05:57:23,495 - __main__ - INFO - Added market 664214 to pending orders
2025-11-04 05:57:23,788 - order_manager - INFO - Prepared order for market 664311 with spread 0.0120
2025-11-04 05:57:23,789 - order_manager - INFO - Added order to pending queue: 664311
2025-11-04 05:57:23,789 - __main__ - INFO - Added market 664311 to pending orders
2025-11-04 05:57:24,096 - order_manager - INFO - Prepared order for market 664308 with spread 0.0120
2025-11-04 05:57:24,096 - order_manager - INFO - Added order to pending queue: 664308
2025-11-04 05:57:24,096 - __main__ - INFO - Added market 664308 to pending orders
2025-11-04 05:57:26,015 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:57:26,015 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:57:26,930 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:57:26,930 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:57:29,226 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:57:29,226 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:57:30,134 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:57:30,135 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:57:30,135 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 05:57:30,890 - market_scanner_v2 - INFO - âœ… Fetched 159 markets from API
2025-11-04 05:57:30,891 - market_scanner_v2 - INFO - âœ… Got 159 markets from API
2025-11-04 05:57:30,893 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 159/159 markets passed
2025-11-04 05:57:30,893 - market_scanner_v2 - INFO - âœ… Found 159 qualifying markets (from 159 total)
2025-11-04 05:57:30,895 - market_selector - INFO - Selected 3 markets from 159 candidates
2025-11-04 05:57:31,250 - order_manager - INFO - Prepared order for market 664214 with spread 0.0120
2025-11-04 05:57:31,250 - order_manager - INFO - Added order to pending queue: 664214
2025-11-04 05:57:31,251 - __main__ - INFO - Added market 664214 to pending orders
2025-11-04 05:57:31,591 - order_manager - INFO - Prepared order for market 664311 with spread 0.0120
2025-11-04 05:57:31,592 - order_manager - INFO - Added order to pending queue: 664311
2025-11-04 05:57:31,592 - __main__ - INFO - Added market 664311 to pending orders
2025-11-04 05:57:31,999 - order_manager - INFO - Prepared order for market 664308 with spread 0.0120
2025-11-04 05:57:32,000 - order_manager - INFO - Added order to pending queue: 664308
2025-11-04 05:57:32,000 - __main__ - INFO - Added market 664308 to pending orders
2025-11-04 05:57:32,858 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:57:32,859 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:57:33,742 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:57:33,742 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:57:35,952 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:57:35,952 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:57:36,900 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:57:36,900 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:57:37,051 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 05:57:38,607 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:57:38,607 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:57:39,486 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:57:39,486 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:57:39,507 - market_scanner_v2 - INFO - âœ… Fetched 159 markets from API
2025-11-04 05:57:39,509 - market_scanner_v2 - INFO - âœ… Got 159 markets from API
2025-11-04 05:57:39,510 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 159/159 markets passed
2025-11-04 05:57:39,510 - market_scanner_v2 - INFO - âœ… Found 159 qualifying markets (from 159 total)
2025-11-04 05:57:39,513 - market_selector - INFO - Selected 3 markets from 159 candidates
2025-11-04 05:57:39,800 - order_manager - INFO - Prepared order for market 664214 with spread 0.0120
2025-11-04 05:57:39,800 - order_manager - INFO - Added order to pending queue: 664214
2025-11-04 05:57:39,800 - __main__ - INFO - Added market 664214 to pending orders
2025-11-04 05:57:40,077 - order_manager - INFO - Prepared order for market 664311 with spread 0.0120
2025-11-04 05:57:40,077 - order_manager - INFO - Added order to pending queue: 664311
2025-11-04 05:57:40,077 - __main__ - INFO - Added market 664311 to pending orders
2025-11-04 05:57:40,374 - order_manager - INFO - Prepared order for market 664308 with spread 0.0120
2025-11-04 05:57:40,375 - order_manager - INFO - Added order to pending queue: 664308
2025-11-04 05:57:40,375 - __main__ - INFO - Added market 664308 to pending orders
2025-11-04 05:57:41,561 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:57:41,562 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:57:42,430 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:57:42,430 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:57:43,910 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:57:43,910 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:57:44,948 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:57:44,949 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:57:44,949 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 05:57:46,854 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:57:46,854 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:57:47,803 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:57:47,804 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:57:47,824 - market_scanner_v2 - INFO - âœ… Fetched 159 markets from API
2025-11-04 05:57:47,826 - market_scanner_v2 - INFO - âœ… Got 159 markets from API
2025-11-04 05:57:47,828 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 159/159 markets passed
2025-11-04 05:57:47,828 - market_scanner_v2 - INFO - âœ… Found 159 qualifying markets (from 159 total)
2025-11-04 05:57:47,830 - market_selector - INFO - Selected 3 markets from 159 candidates
2025-11-04 05:57:48,208 - order_manager - INFO - Prepared order for market 664214 with spread 0.0120
2025-11-04 05:57:48,209 - order_manager - INFO - Added order to pending queue: 664214
2025-11-04 05:57:48,209 - __main__ - INFO - Added market 664214 to pending orders
2025-11-04 05:57:48,493 - order_manager - INFO - Prepared order for market 664311 with spread 0.0120
2025-11-04 05:57:48,494 - order_manager - INFO - Added order to pending queue: 664311
2025-11-04 05:57:48,494 - __main__ - INFO - Added market 664311 to pending orders
2025-11-04 05:57:48,771 - order_manager - INFO - Prepared order for market 664308 with spread 0.0120
2025-11-04 05:57:48,771 - order_manager - INFO - Added order to pending queue: 664308
2025-11-04 05:57:48,771 - __main__ - INFO - Added market 664308 to pending orders
2025-11-04 05:57:49,947 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:57:49,948 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:57:50,842 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:57:50,842 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:57:52,532 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:57:52,532 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:57:53,491 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:57:53,491 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:57:53,801 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 05:57:54,511 - market_scanner_v2 - INFO - âœ… Fetched 159 markets from API
2025-11-04 05:57:54,514 - market_scanner_v2 - INFO - âœ… Got 159 markets from API
2025-11-04 05:57:54,514 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 159/159 markets passed
2025-11-04 05:57:54,515 - market_scanner_v2 - INFO - âœ… Found 159 qualifying markets (from 159 total)
2025-11-04 05:57:54,517 - market_selector - INFO - Selected 3 markets from 159 candidates
2025-11-04 05:57:54,903 - order_manager - INFO - Prepared order for market 664214 with spread 0.0120
2025-11-04 05:57:54,903 - order_manager - INFO - Added order to pending queue: 664214
2025-11-04 05:57:54,903 - __main__ - INFO - Added market 664214 to pending orders
2025-11-04 05:57:55,173 - order_manager - INFO - Prepared order for market 664311 with spread 0.0120
2025-11-04 05:57:55,173 - order_manager - INFO - Added order to pending queue: 664311
2025-11-04 05:57:55,173 - __main__ - INFO - Added market 664311 to pending orders
2025-11-04 05:57:55,452 - order_manager - INFO - Prepared order for market 664308 with spread 0.0120
2025-11-04 05:57:55,455 - order_manager - INFO - Added order to pending queue: 664308
2025-11-04 05:57:55,455 - __main__ - INFO - Added market 664308 to pending orders
2025-11-04 05:57:56,344 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:57:56,344 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:57:57,318 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:57:57,319 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:57:59,679 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:57:59,679 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:58:00,566 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:58:00,566 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:58:00,567 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 05:58:01,275 - market_scanner_v2 - INFO - âœ… Fetched 159 markets from API
2025-11-04 05:58:01,277 - market_scanner_v2 - INFO - âœ… Got 159 markets from API
2025-11-04 05:58:01,278 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 159/159 markets passed
2025-11-04 05:58:01,278 - market_scanner_v2 - INFO - âœ… Found 159 qualifying markets (from 159 total)
2025-11-04 05:58:01,281 - market_selector - INFO - Selected 3 markets from 159 candidates
2025-11-04 05:58:01,594 - order_manager - INFO - Prepared order for market 664214 with spread 0.0120
2025-11-04 05:58:01,594 - order_manager - INFO - Added order to pending queue: 664214
2025-11-04 05:58:01,594 - __main__ - INFO - Added market 664214 to pending orders
2025-11-04 05:58:01,875 - order_manager - INFO - Prepared order for market 664311 with spread 0.0120
2025-11-04 05:58:01,879 - order_manager - INFO - Added order to pending queue: 664311
2025-11-04 05:58:01,880 - __main__ - INFO - Added market 664311 to pending orders
2025-11-04 05:58:02,184 - order_manager - INFO - Prepared order for market 664308 with spread 0.0120
2025-11-04 05:58:02,185 - order_manager - INFO - Added order to pending queue: 664308
2025-11-04 05:58:02,185 - __main__ - INFO - Added market 664308 to pending orders
2025-11-04 05:58:03,085 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:58:03,086 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:58:04,068 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:58:04,069 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:58:05,804 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:58:05,804 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:58:06,684 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:58:06,684 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:58:06,684 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 05:58:07,432 - market_scanner_v2 - INFO - âœ… Fetched 159 markets from API
2025-11-04 05:58:07,438 - market_scanner_v2 - INFO - âœ… Got 159 markets from API
2025-11-04 05:58:07,439 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 159/159 markets passed
2025-11-04 05:58:07,440 - market_scanner_v2 - INFO - âœ… Found 159 qualifying markets (from 159 total)
2025-11-04 05:58:07,446 - market_selector - INFO - Selected 3 markets from 159 candidates
2025-11-04 05:58:07,738 - order_manager - INFO - Prepared order for market 664214 with spread 0.0120
2025-11-04 05:58:07,738 - order_manager - INFO - Added order to pending queue: 664214
2025-11-04 05:58:07,738 - __main__ - INFO - Added market 664214 to pending orders
2025-11-04 05:58:08,017 - order_manager - INFO - Prepared order for market 664311 with spread 0.0120
2025-11-04 05:58:08,017 - order_manager - INFO - Added order to pending queue: 664311
2025-11-04 05:58:08,018 - __main__ - INFO - Added market 664311 to pending orders
2025-11-04 05:58:08,303 - order_manager - INFO - Prepared order for market 664308 with spread 0.0120
2025-11-04 05:58:08,304 - order_manager - INFO - Added order to pending queue: 664308
2025-11-04 05:58:08,304 - __main__ - INFO - Added market 664308 to pending orders
2025-11-04 05:58:09,292 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:58:09,293 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:58:10,244 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:58:10,244 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:58:12,598 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:58:12,598 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:58:13,584 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:58:13,584 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:58:13,584 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 05:58:14,204 - market_scanner_v2 - INFO - âœ… Fetched 159 markets from API
2025-11-04 05:58:14,207 - market_scanner_v2 - INFO - âœ… Got 159 markets from API
2025-11-04 05:58:14,208 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 159/159 markets passed
2025-11-04 05:58:14,208 - market_scanner_v2 - INFO - âœ… Found 159 qualifying markets (from 159 total)
2025-11-04 05:58:14,211 - market_selector - INFO - Selected 3 markets from 159 candidates
2025-11-04 05:58:14,517 - order_manager - INFO - Prepared order for market 664214 with spread 0.0120
2025-11-04 05:58:14,518 - order_manager - INFO - Added order to pending queue: 664214
2025-11-04 05:58:14,518 - __main__ - INFO - Added market 664214 to pending orders
2025-11-04 05:58:14,854 - order_manager - INFO - Prepared order for market 664211 with spread 0.0120
2025-11-04 05:58:14,855 - order_manager - INFO - Added order to pending queue: 664211
2025-11-04 05:58:14,855 - __main__ - INFO - Added market 664211 to pending orders
2025-11-04 05:58:15,130 - order_manager - INFO - Prepared order for market 664311 with spread 0.0120
2025-11-04 05:58:15,131 - order_manager - INFO - Added order to pending queue: 664311
2025-11-04 05:58:15,131 - __main__ - INFO - Added market 664311 to pending orders
2025-11-04 05:58:16,023 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:58:16,023 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:58:16,889 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:58:16,890 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:58:18,833 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:58:18,834 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:58:19,784 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:58:19,785 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:58:21,086 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 05:58:22,088 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:58:22,092 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:58:22,962 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:58:22,963 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:58:23,211 - market_scanner_v2 - INFO - âœ… Fetched 159 markets from API
2025-11-04 05:58:23,219 - market_scanner_v2 - INFO - âœ… Got 159 markets from API
2025-11-04 05:58:23,220 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 159/159 markets passed
2025-11-04 05:58:23,220 - market_scanner_v2 - INFO - âœ… Found 159 qualifying markets (from 159 total)
2025-11-04 05:58:23,225 - market_selector - INFO - Selected 3 markets from 159 candidates
2025-11-04 05:58:23,621 - order_manager - INFO - Prepared order for market 664214 with spread 0.0120
2025-11-04 05:58:23,621 - order_manager - INFO - Added order to pending queue: 664214
2025-11-04 05:58:23,622 - __main__ - INFO - Added market 664214 to pending orders
2025-11-04 05:58:23,927 - order_manager - INFO - Prepared order for market 664211 with spread 0.0120
2025-11-04 05:58:23,928 - order_manager - INFO - Added order to pending queue: 664211
2025-11-04 05:58:23,928 - __main__ - INFO - Added market 664211 to pending orders
2025-11-04 05:58:24,227 - order_manager - INFO - Prepared order for market 664311 with spread 0.0120
2025-11-04 05:58:24,228 - order_manager - INFO - Added order to pending queue: 664311
2025-11-04 05:58:24,228 - __main__ - INFO - Added market 664311 to pending orders
2025-11-04 05:58:25,258 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:58:25,258 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:58:26,203 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:58:26,204 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:58:28,536 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:58:28,536 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:58:29,470 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:58:29,471 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:58:30,473 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 05:58:31,499 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:58:31,499 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:58:32,453 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:58:32,453 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:58:33,905 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:58:33,905 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:58:34,831 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:58:34,831 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:58:34,852 - market_scanner_v2 - INFO - âœ… Fetched 159 markets from API
2025-11-04 05:58:34,855 - market_scanner_v2 - INFO - âœ… Got 159 markets from API
2025-11-04 05:58:34,856 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 159/159 markets passed
2025-11-04 05:58:34,856 - market_scanner_v2 - INFO - âœ… Found 159 qualifying markets (from 159 total)
2025-11-04 05:58:34,859 - market_selector - INFO - Selected 3 markets from 159 candidates
2025-11-04 05:58:35,205 - order_manager - INFO - Prepared order for market 664214 with spread 0.0120
2025-11-04 05:58:35,206 - order_manager - INFO - Added order to pending queue: 664214
2025-11-04 05:58:35,206 - __main__ - INFO - Added market 664214 to pending orders
2025-11-04 05:58:35,489 - order_manager - INFO - Prepared order for market 664211 with spread 0.0120
2025-11-04 05:58:35,490 - order_manager - INFO - Added order to pending queue: 664211
2025-11-04 05:58:35,490 - __main__ - INFO - Added market 664211 to pending orders
2025-11-04 05:58:35,882 - order_manager - INFO - Prepared order for market 664311 with spread 0.0132
2025-11-04 05:58:35,883 - order_manager - INFO - Added order to pending queue: 664311
2025-11-04 05:58:35,884 - __main__ - INFO - Added market 664311 to pending orders
2025-11-04 05:58:36,737 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:58:36,738 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:58:37,725 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:58:37,725 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:58:39,368 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:58:39,369 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:58:40,243 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:58:40,243 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:58:41,958 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:58:41,959 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:58:42,854 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:58:42,855 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:58:42,855 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 05:58:43,433 - market_scanner_v2 - INFO - âœ… Fetched 159 markets from API
2025-11-04 05:58:43,435 - market_scanner_v2 - INFO - âœ… Got 159 markets from API
2025-11-04 05:58:43,436 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 159/159 markets passed
2025-11-04 05:58:43,436 - market_scanner_v2 - INFO - âœ… Found 159 qualifying markets (from 159 total)
2025-11-04 05:58:43,438 - market_selector - INFO - Selected 3 markets from 159 candidates
2025-11-04 05:58:43,724 - order_manager - INFO - Prepared order for market 664214 with spread 0.0120
2025-11-04 05:58:43,725 - order_manager - INFO - Added order to pending queue: 664214
2025-11-04 05:58:43,725 - __main__ - INFO - Added market 664214 to pending orders
2025-11-04 05:58:43,991 - order_manager - INFO - Prepared order for market 664211 with spread 0.0120
2025-11-04 05:58:43,992 - order_manager - INFO - Added order to pending queue: 664211
2025-11-04 05:58:43,992 - __main__ - INFO - Added market 664211 to pending orders
2025-11-04 05:58:44,324 - order_manager - INFO - Prepared order for market 664311 with spread 0.0132
2025-11-04 05:58:44,325 - order_manager - INFO - Added order to pending queue: 664311
2025-11-04 05:58:44,325 - __main__ - INFO - Added market 664311 to pending orders
2025-11-04 05:58:45,209 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:58:45,210 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:58:46,088 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:58:46,089 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:58:47,914 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:58:47,915 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:58:48,828 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:58:48,828 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:58:48,919 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 05:58:50,272 - market_scanner_v2 - INFO - âœ… Fetched 159 markets from API
2025-11-04 05:58:51,227 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:58:51,227 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:58:52,208 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:58:52,208 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:58:52,209 - market_scanner_v2 - INFO - âœ… Got 159 markets from API
2025-11-04 05:58:52,210 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 159/159 markets passed
2025-11-04 05:58:52,211 - market_scanner_v2 - INFO - âœ… Found 159 qualifying markets (from 159 total)
2025-11-04 05:58:52,213 - market_selector - INFO - Selected 3 markets from 159 candidates
2025-11-04 05:58:52,487 - order_manager - INFO - Prepared order for market 664214 with spread 0.0120
2025-11-04 05:58:52,487 - order_manager - INFO - Added order to pending queue: 664214
2025-11-04 05:58:52,487 - __main__ - INFO - Added market 664214 to pending orders
2025-11-04 05:58:52,757 - order_manager - INFO - Prepared order for market 664211 with spread 0.0120
2025-11-04 05:58:52,758 - order_manager - INFO - Added order to pending queue: 664211
2025-11-04 05:58:52,758 - __main__ - INFO - Added market 664211 to pending orders
2025-11-04 05:58:53,038 - order_manager - INFO - Prepared order for market 664311 with spread 0.0132
2025-11-04 05:58:53,039 - order_manager - INFO - Added order to pending queue: 664311
2025-11-04 05:58:53,039 - __main__ - INFO - Added market 664311 to pending orders
2025-11-04 05:58:54,645 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:58:54,646 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:58:55,710 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:58:55,710 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:58:57,323 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:58:57,324 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:58:58,288 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:58:58,288 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:58:58,288 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 05:58:59,067 - market_scanner_v2 - INFO - âœ… Fetched 159 markets from API
2025-11-04 05:58:59,071 - market_scanner_v2 - INFO - âœ… Got 159 markets from API
2025-11-04 05:58:59,072 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 159/159 markets passed
2025-11-04 05:58:59,073 - market_scanner_v2 - INFO - âœ… Found 159 qualifying markets (from 159 total)
2025-11-04 05:58:59,076 - market_selector - INFO - Selected 3 markets from 159 candidates
2025-11-04 05:58:59,396 - order_manager - INFO - Prepared order for market 664214 with spread 0.0120
2025-11-04 05:58:59,396 - order_manager - INFO - Added order to pending queue: 664214
2025-11-04 05:58:59,396 - __main__ - INFO - Added market 664214 to pending orders
2025-11-04 05:58:59,710 - order_manager - INFO - Prepared order for market 664211 with spread 0.0120
2025-11-04 05:58:59,710 - order_manager - INFO - Added order to pending queue: 664211
2025-11-04 05:58:59,711 - __main__ - INFO - Added market 664211 to pending orders
2025-11-04 05:58:59,986 - order_manager - INFO - Prepared order for market 664311 with spread 0.0132
2025-11-04 05:58:59,987 - order_manager - INFO - Added order to pending queue: 664311
2025-11-04 05:58:59,988 - __main__ - INFO - Added market 664311 to pending orders
2025-11-04 05:59:00,880 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:59:00,881 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:59:01,775 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:59:01,775 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:59:04,249 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:59:04,249 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:59:05,239 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:59:05,240 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

2025-11-04 05:59:05,240 - market_scanner_v2 - INFO - ðŸ” Fetching from Gamma API...
2025-11-04 05:59:05,961 - market_scanner_v2 - INFO - âœ… Fetched 159 markets from API
2025-11-04 05:59:05,964 - market_scanner_v2 - INFO - âœ… Got 159 markets from API
2025-11-04 05:59:05,965 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 159/159 markets passed
2025-11-04 05:59:05,965 - market_scanner_v2 - INFO - âœ… Found 159 qualifying markets (from 159 total)
2025-11-04 05:59:05,968 - market_selector - INFO - Selected 3 markets from 159 candidates
2025-11-04 05:59:06,235 - order_manager - INFO - Prepared order for market 664214 with spread 0.0120
2025-11-04 05:59:06,236 - order_manager - INFO - Added order to pending queue: 664214
2025-11-04 05:59:06,236 - __main__ - INFO - Added market 664214 to pending orders
2025-11-04 05:59:06,569 - order_manager - INFO - Prepared order for market 664299 with spread 0.0120
2025-11-04 05:59:06,569 - order_manager - INFO - Added order to pending queue: 664299
2025-11-04 05:59:06,569 - __main__ - INFO - Added market 664299 to pending orders
2025-11-04 05:59:06,857 - order_manager - INFO - Prepared order for market 664211 with spread 0.0120
2025-11-04 05:59:06,858 - order_manager - INFO - Added order to pending queue: 664211
2025-11-04 05:59:06,858 - __main__ - INFO - Added market 664211 to pending orders
2025-11-04 05:59:08,013 - order_manager - ERROR - Error placing single order: PolyException: API Credentials are needed to interact with this endpoint!
2025-11-04 05:59:08,017 - order_manager - ERROR - Full traceback: Traceback (most recent call last):
  File "/home/farmpoly/farmpoly/order_manager.py", line 340, in _place_single_order
    response = signing_client.post_order(signed_order)
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 515, in post_order
    self.assert_level_2_auth()
  File "/home/farmpoly/farmpoly/venv/lib/python3.10/site-packages/py_clob_client/client.py", line 697, in assert_level_2_auth
    raise PolyException(L2_AUTH_UNAVAILABLE)
py_clob_client.exceptions.PolyException: API Credentials are needed to interact with this endpoint!

