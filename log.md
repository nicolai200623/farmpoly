2025-11-06 15:00:13,883 - market_scanner_v2 - INFO - âœ… Found 81 qualifying markets (from 2840 total)
2025-11-06 15:00:13,888 - market_selector - INFO - Selected 2 markets from 81 candidates
2025-11-06 15:00:17,362 - order_manager - WARNING - âŒ Calculated prices exceed max spread (96.20% > 3.50%)
2025-11-06 15:00:17,363 - order_manager - WARNING -    This indicates orderbook is too thin or position 2-3 is too far from midpoint
2025-11-06 15:00:17,363 - order_manager - WARNING -    REJECTING market to avoid placing order at position #1 (best bid/ask)
2025-11-06 15:00:17,363 - order_manager - WARNING -    Reason: Adjusting to max spread would place order too close to best bid/ask
2025-11-06 15:00:17,363 - order_manager - WARNING -    â†’ High risk of being filled immediately!
2025-11-06 15:00:17,363 - order_manager - WARNING - Could not calculate valid prices for market 657210
2025-11-06 15:00:17,363 - __main__ - INFO - Added market 657210 to pending orders
2025-11-06 15:00:17,709 - order_manager - WARNING - âŒ Calculated prices exceed max spread (96.20% > 3.50%)
2025-11-06 15:00:17,710 - order_manager - WARNING -    This indicates orderbook is too thin or position 2-3 is too far from midpoint
2025-11-06 15:00:17,710 - order_manager - WARNING -    REJECTING market to avoid placing order at position #1 (best bid/ask)
2025-11-06 15:00:17,710 - order_manager - WARNING -    Reason: Adjusting to max spread would place order too close to best bid/ask
2025-11-06 15:00:17,710 - order_manager - WARNING -    â†’ High risk of being filled immediately!
2025-11-06 15:00:17,710 - order_manager - WARNING - Could not calculate valid prices for market 666798
2025-11-06 15:00:17,710 - __main__ - INFO - Added market 666798 to pending orders
2025-11-06 15:01:01,212 - profit_taking_manager - INFO - ðŸ” Checking positions for wallet: 0x18F261DC...Ae4FfD96
2025-11-06 15:01:01,562 - profit_taking_manager - INFO - ðŸ“Š Found 4 active positions
2025-11-06 15:01:01,562 - profit_taking_manager - INFO - 
ðŸ“ˆ Position: Charlotte 49ers vs. East Carolina
2025-11-06 15:01:01,562 - profit_taking_manager - INFO -    Shares: 259.00 @ $0.1494
2025-11-06 15:01:01,562 - profit_taking_manager - INFO -    Current: $0.0385
2025-11-06 15:01:01,562 - profit_taking_manager - INFO -    P&L: $-28.73 (-74.23%)
2025-11-06 15:01:01,562 - profit_taking_manager - INFO -    â¸ï¸  Losing position - NOT closing (manual decision required)
2025-11-06 15:01:01,563 - profit_taking_manager - INFO - 
ðŸ“ˆ Position: Will Google Gemini 3 score at least 70% on the Fro
2025-11-06 15:01:01,563 - profit_taking_manager - INFO -    Shares: 68.00 @ $0.3900
2025-11-06 15:01:01,563 - profit_taking_manager - INFO -    Current: $0.0800
2025-11-06 15:01:01,563 - profit_taking_manager - INFO -    P&L: $-21.08 (-79.49%)
2025-11-06 15:01:01,563 - profit_taking_manager - INFO -    â¸ï¸  Losing position - NOT closing (manual decision required)
2025-11-06 15:01:01,563 - profit_taking_manager - INFO - 
ðŸ“ˆ Position: Syracuse vs. Miami
2025-11-06 15:01:01,563 - profit_taking_manager - INFO -    Shares: 66.00 @ $0.4900
2025-11-06 15:01:01,563 - profit_taking_manager - INFO -    Current: $0.0475
2025-11-06 15:01:01,563 - profit_taking_manager - INFO -    P&L: $-29.20 (-90.31%)
2025-11-06 15:01:01,563 - profit_taking_manager - INFO -    â¸ï¸  Losing position - NOT closing (manual decision required)
2025-11-06 15:01:01,563 - profit_taking_manager - INFO - 
ðŸ“ˆ Position: Will Netflix dip to $1050 in November?
2025-11-06 15:01:01,563 - profit_taking_manager - INFO -    Shares: 50.00 @ $0.3400
2025-11-06 15:01:01,563 - profit_taking_manager - INFO -    Current: $0.7700
2025-11-06 15:01:01,563 - profit_taking_manager - INFO -    P&L: $21.50 (+126.47%)
2025-11-06 15:01:01,563 - profit_taking_manager - INFO -    ðŸŽ¯ CLOSING: target_profit_reached (126.47% >= 10%)
2025-11-06 15:01:01,563 - profit_taking_manager - INFO - 
ðŸ”„ Placing SELL order for Will Netflix dip to $1050 in November?
2025-11-06 15:01:01,563 - profit_taking_manager - INFO -    Token ID: 109176985745730388398013053205590535560490868817001794547246190093921488790462
2025-11-06 15:01:01,563 - profit_taking_manager - INFO -    Shares: 50.00
2025-11-06 15:01:01,563 - profit_taking_manager - INFO -    Price: $0.7700
2025-11-06 15:01:02,654 - profit_taking_manager - ERROR - âŒ Error closing position: PolyApiException[status_code=400, error_message={'error': 'invalid signature'}]
2025-11-06 15:01:02,656 - __main__ - INFO - â³ Next profit check in 300s
2025-11-06 15:01:15,388 - market_scanner_v2 - INFO - ðŸŒ Scraping markets from /rewards page using Playwright...
2025-11-06 15:01:15,388 - playwright_rewards_scraper - INFO - ðŸŒ Fetching markets from /rewards API...
2025-11-06 15:01:15,388 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 1 (cursor: MA==)...
2025-11-06 15:01:16,055 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 1
2025-11-06 15:01:16,056 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 2 (cursor: MTAw)...
2025-11-06 15:01:16,493 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 2
2025-11-06 15:01:16,494 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 3 (cursor: MjAw)...
2025-11-06 15:01:17,903 - __main__ - WARNING - âš ï¸ Health check failed: 2 issues
2025-11-06 15:01:17,903 - __main__ - WARNING -    - ðŸ”´ KhÃ´ng quÃ©t markets trong 63s!
2025-11-06 15:01:17,903 - __main__ - WARNING -    - âš ï¸ API cháº­m: 38.9s trung bÃ¬nh
2025-11-06 15:01:17,908 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 3
2025-11-06 15:01:17,908 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 4 (cursor: MzAw)...
2025-11-06 15:01:18,562 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 4
2025-11-06 15:01:18,562 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 5 (cursor: NDAw)...
2025-11-06 15:01:19,204 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 5
2025-11-06 15:01:19,205 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 6 (cursor: NTAw)...
2025-11-06 15:01:19,876 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 6
2025-11-06 15:01:19,877 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 7 (cursor: NjAw)...
2025-11-06 15:01:20,346 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 7
2025-11-06 15:01:20,347 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 8 (cursor: NzAw)...
2025-11-06 15:01:20,986 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 8
2025-11-06 15:01:20,987 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 9 (cursor: ODAw)...
2025-11-06 15:01:21,675 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 9
2025-11-06 15:01:21,675 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 10 (cursor: OTAw)...
2025-11-06 15:01:22,135 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 10
2025-11-06 15:01:22,136 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 11 (cursor: MTAwMA==)...
2025-11-06 15:01:22,703 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 11
2025-11-06 15:01:22,704 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 12 (cursor: MTEwMA==)...
2025-11-06 15:01:23,337 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 12
2025-11-06 15:01:23,337 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 13 (cursor: MTIwMA==)...
2025-11-06 15:01:24,000 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 13
2025-11-06 15:01:24,000 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 14 (cursor: MTMwMA==)...
2025-11-06 15:01:24,683 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 14
2025-11-06 15:01:24,683 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 15 (cursor: MTQwMA==)...
2025-11-06 15:01:25,097 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 15
2025-11-06 15:01:25,097 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 16 (cursor: MTUwMA==)...
2025-11-06 15:01:25,783 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 16
2025-11-06 15:01:25,783 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 17 (cursor: MTYwMA==)...
2025-11-06 15:01:26,456 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 17
2025-11-06 15:01:26,456 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 18 (cursor: MTcwMA==)...
2025-11-06 15:01:27,108 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 18
2025-11-06 15:01:27,109 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 19 (cursor: MTgwMA==)...
2025-11-06 15:01:27,822 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 19
2025-11-06 15:01:27,822 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 20 (cursor: MTkwMA==)...
2025-11-06 15:01:28,457 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 20
2025-11-06 15:01:28,457 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 21 (cursor: MjAwMA==)...
2025-11-06 15:01:29,091 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 21
2025-11-06 15:01:29,091 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 22 (cursor: MjEwMA==)...
2025-11-06 15:01:29,509 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 22
2025-11-06 15:01:29,509 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 23 (cursor: MjIwMA==)...
2025-11-06 15:01:29,961 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 23
2025-11-06 15:01:29,961 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 24 (cursor: MjMwMA==)...
2025-11-06 15:01:30,427 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 24
2025-11-06 15:01:30,428 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 25 (cursor: MjQwMA==)...
2025-11-06 15:01:31,138 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 25
2025-11-06 15:01:31,138 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 26 (cursor: MjUwMA==)...
2025-11-06 15:01:31,561 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 26
2025-11-06 15:01:31,562 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 27 (cursor: MjYwMA==)...
2025-11-06 15:01:31,980 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 27
2025-11-06 15:01:31,981 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 28 (cursor: MjcwMA==)...
2025-11-06 15:01:32,420 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 28
2025-11-06 15:01:32,421 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 29 (cursor: MjgwMA==)...
2025-11-06 15:01:32,901 - playwright_rewards_scraper - INFO - âœ… Got 43 markets on page 29
2025-11-06 15:01:32,901 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 30 (cursor: LTE=)...
2025-11-06 15:01:33,232 - playwright_rewards_scraper - INFO - âœ… No more markets on page 30
2025-11-06 15:01:33,232 - playwright_rewards_scraper - INFO - âœ… Fetched 2840 total unique markets from /rewards API
2025-11-06 15:01:33,281 - market_scanner_v2 - INFO - âœ… Got 2840 markets from /rewards page
2025-11-06 15:01:33,282 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Zohran Mamdani win by >9%?
2025-11-06 15:01:33,282 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:01:33,282 - market_scanner_v2 - INFO -    - Estimated Reward: $40 (based on volume=$19063)
2025-11-06 15:01:33,282 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,282 - market_scanner_v2 - INFO -    - Competition: 1.027245 bars, Score: -80.82
2025-11-06 15:01:33,282 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,282 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will any Google Gemini 3 model score at least 1600 on LMAren
2025-11-06 15:01:33,282 - market_scanner_v2 - INFO -    - Category: science
2025-11-06 15:01:33,282 - market_scanner_v2 - INFO -    - Estimated Reward: $50 (based on volume=$9)
2025-11-06 15:01:33,282 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,282 - market_scanner_v2 - INFO -    - Competition: 1.05668 bars, Score: -80.67
2025-11-06 15:01:33,282 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,282 - market_scanner_v2 - INFO - âœ… ACCEPTED: Trump announces new drug boat strike by November 14?
2025-11-06 15:01:33,282 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:01:33,282 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$776)
2025-11-06 15:01:33,282 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,282 - market_scanner_v2 - INFO -    - Competition: 0.243897 bars, Score: -19.31
2025-11-06 15:01:33,282 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,283 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will â€œThe Witcher: Season 4â€ be the top global Netflix show 
2025-11-06 15:01:33,283 - market_scanner_v2 - INFO -    - Category: entertainment
2025-11-06 15:01:33,283 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$3167)
2025-11-06 15:01:33,283 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,283 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.32
2025-11-06 15:01:33,283 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,283 - market_scanner_v2 - INFO - âœ… ACCEPTED: Airbnb (ABNB) Up or Down on November 6?
2025-11-06 15:01:33,283 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:01:33,283 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$7056)
2025-11-06 15:01:33,283 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,283 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.71
2025-11-06 15:01:33,283 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,283 - market_scanner_v2 - INFO - âœ… ACCEPTED: Rocket Lab (RKLB) Up or Down on November 6?
2025-11-06 15:01:33,283 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:01:33,283 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$4439)
2025-11-06 15:01:33,283 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,283 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.44
2025-11-06 15:01:33,283 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,283 - market_scanner_v2 - INFO - âœ… ACCEPTED: Opendoor (OPEN) Up or Down on November 6?
2025-11-06 15:01:33,283 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:01:33,283 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$4345)
2025-11-06 15:01:33,283 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,283 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.43
2025-11-06 15:01:33,283 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,284 - market_scanner_v2 - INFO - âœ… ACCEPTED: Palantir (PLTR) Up or Down on November 6?
2025-11-06 15:01:33,284 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:01:33,284 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$3118)
2025-11-06 15:01:33,284 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,284 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.31
2025-11-06 15:01:33,284 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,284 - market_scanner_v2 - INFO - âœ… ACCEPTED: NYA (NYA) Up or Down on November 6?
2025-11-06 15:01:33,284 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:01:33,284 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$4776)
2025-11-06 15:01:33,284 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,284 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.48
2025-11-06 15:01:33,284 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,284 - market_scanner_v2 - INFO - âœ… ACCEPTED: Netflix (NFLX) Up or Down on November 6?
2025-11-06 15:01:33,284 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:01:33,284 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$1972)
2025-11-06 15:01:33,284 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,284 - market_scanner_v2 - INFO -    - Competition: 0.136 bars, Score: -3.40
2025-11-06 15:01:33,284 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,284 - market_scanner_v2 - INFO - âœ… ACCEPTED: Russell 2000 (RUT) Up or Down on November 6?
2025-11-06 15:01:33,284 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:01:33,284 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2856)
2025-11-06 15:01:33,284 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,284 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.29
2025-11-06 15:01:33,284 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,284 - market_scanner_v2 - INFO - âœ… ACCEPTED: NVIDIA (NVDA) Up or Down on November 6?
2025-11-06 15:01:33,284 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:01:33,284 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2086)
2025-11-06 15:01:33,284 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,284 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.21
2025-11-06 15:01:33,284 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,285 - market_scanner_v2 - INFO - âœ… ACCEPTED: Hang Seng (HSI) Up or Down on November 6?
2025-11-06 15:01:33,285 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:01:33,285 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2965)
2025-11-06 15:01:33,285 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,285 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.30
2025-11-06 15:01:33,285 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,285 - market_scanner_v2 - INFO - âœ… ACCEPTED: Tesla (TSLA) Up or Down on November 6?
2025-11-06 15:01:33,285 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:01:33,285 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2431)
2025-11-06 15:01:33,285 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,285 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.24
2025-11-06 15:01:33,285 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,285 - market_scanner_v2 - INFO - âœ… ACCEPTED: DAX (DAX) Up or Down on November 6?
2025-11-06 15:01:33,285 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:01:33,285 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2020)
2025-11-06 15:01:33,285 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,285 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.20
2025-11-06 15:01:33,285 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,285 - market_scanner_v2 - INFO - âœ… ACCEPTED: Meta (META) Up or Down on November 6?
2025-11-06 15:01:33,285 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:01:33,285 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2728)
2025-11-06 15:01:33,285 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,285 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.27
2025-11-06 15:01:33,285 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,285 - market_scanner_v2 - INFO - âœ… ACCEPTED: FTSE 100 (UKX) Up or Down on November 6?
2025-11-06 15:01:33,285 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:01:33,285 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$4234)
2025-11-06 15:01:33,285 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,286 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.42
2025-11-06 15:01:33,286 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,286 - market_scanner_v2 - INFO - âœ… ACCEPTED: Google (GOOGL) Up or Down on November 6?
2025-11-06 15:01:33,286 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:01:33,286 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$908)
2025-11-06 15:01:33,286 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,286 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.09
2025-11-06 15:01:33,286 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,286 - market_scanner_v2 - INFO - âœ… ACCEPTED: Dow Jones (DJI) Up or Down on November 6?
2025-11-06 15:01:33,286 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:01:33,286 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$4720)
2025-11-06 15:01:33,286 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,286 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.47
2025-11-06 15:01:33,286 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,286 - market_scanner_v2 - INFO - âœ… ACCEPTED: NYMEX Crude Oil Futures (WTI) (CL=F) Up or Down on November 
2025-11-06 15:01:33,286 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:01:33,286 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$920)
2025-11-06 15:01:33,286 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,286 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.09
2025-11-06 15:01:33,286 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,286 - market_scanner_v2 - INFO - âœ… ACCEPTED: Amazon (AMZN) Up or Down on November 6?
2025-11-06 15:01:33,286 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:01:33,286 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$5350)
2025-11-06 15:01:33,286 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,286 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.53
2025-11-06 15:01:33,286 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,286 - market_scanner_v2 - INFO - âœ… ACCEPTED: Nasdaq 100 (NDX) Up or Down on November 6?
2025-11-06 15:01:33,287 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:01:33,287 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$5109)
2025-11-06 15:01:33,287 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,287 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.51
2025-11-06 15:01:33,287 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,287 - market_scanner_v2 - INFO - âœ… ACCEPTED: COMEX Silver Futures (SI=F) Up or Down on November 6?
2025-11-06 15:01:33,287 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:01:33,287 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$702)
2025-11-06 15:01:33,287 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,287 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.07
2025-11-06 15:01:33,287 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,287 - market_scanner_v2 - INFO - âœ… ACCEPTED: Microsoft (MSFT) Up or Down on November 6?
2025-11-06 15:01:33,287 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:01:33,287 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2377)
2025-11-06 15:01:33,287 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,288 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.24
2025-11-06 15:01:33,288 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,288 - market_scanner_v2 - INFO - âœ… ACCEPTED: Nikkei 225 (NIK) Up or Down on November 6?
2025-11-06 15:01:33,288 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:01:33,288 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2526)
2025-11-06 15:01:33,288 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,288 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.25
2025-11-06 15:01:33,288 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,288 - market_scanner_v2 - INFO - âœ… ACCEPTED: COMEX Gold Futures (GC=F) Up or Down on November 6?
2025-11-06 15:01:33,288 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:01:33,288 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$792)
2025-11-06 15:01:33,288 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,288 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.08
2025-11-06 15:01:33,288 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,288 - market_scanner_v2 - INFO - âœ… ACCEPTED: S&P 500 (SPX) Up or Down on November 6?
2025-11-06 15:01:33,289 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:01:33,289 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$4717)
2025-11-06 15:01:33,289 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,289 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.47
2025-11-06 15:01:33,289 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,289 - market_scanner_v2 - INFO - âœ… ACCEPTED: Apple (AAPL) Up or Down on November 6?
2025-11-06 15:01:33,289 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:01:33,289 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2700)
2025-11-06 15:01:33,289 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,289 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.27
2025-11-06 15:01:33,289 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,289 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump establish a Gaza â€œBoard of Peaceâ€ by March 31?
2025-11-06 15:01:33,289 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:01:33,289 - market_scanner_v2 - INFO -    - Estimated Reward: $40 (based on volume=$563)
2025-11-06 15:01:33,289 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,289 - market_scanner_v2 - INFO -    - Competition: 0.26175 bars, Score: -6.12
2025-11-06 15:01:33,289 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,289 - market_scanner_v2 - INFO - âœ… ACCEPTED: U.S. Closes Airspace due to Government Shutdown?
2025-11-06 15:01:33,289 - market_scanner_v2 - INFO -    - Category: science
2025-11-06 15:01:33,289 - market_scanner_v2 - INFO -    - Estimated Reward: $50 (based on volume=$12049)
2025-11-06 15:01:33,289 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,290 - market_scanner_v2 - INFO -    - Competition: 0.2222 bars, Score: 3.98
2025-11-06 15:01:33,290 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,290 - market_scanner_v2 - INFO - âœ… ACCEPTED: NYMEX Crude Oil Futures (WTI) (CL=F) Up or Down on November 
2025-11-06 15:01:33,290 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:01:33,290 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$307)
2025-11-06 15:01:33,290 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,290 - market_scanner_v2 - INFO -    - Competition: 0.225 bars, Score: -12.47
2025-11-06 15:01:33,290 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,290 - market_scanner_v2 - INFO - âœ… ACCEPTED: COMEX Silver Futures (SI=F) Up or Down on November 5?
2025-11-06 15:01:33,290 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:01:33,290 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2845)
2025-11-06 15:01:33,290 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,290 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.28
2025-11-06 15:01:33,290 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,290 - market_scanner_v2 - INFO - âœ… ACCEPTED: COMEX Gold Futures (GC=F) Up or Down on November 5?
2025-11-06 15:01:33,290 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:01:33,290 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$416)
2025-11-06 15:01:33,290 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,290 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.04
2025-11-06 15:01:33,290 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,290 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Nancy Pelosi announce her retirement by November 30?
2025-11-06 15:01:33,290 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:01:33,290 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$3188)
2025-11-06 15:01:33,290 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,290 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.32
2025-11-06 15:01:33,291 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,291 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Nancy Pelosi announce her retirement by June 30, 2026?
2025-11-06 15:01:33,291 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:01:33,291 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$5093)
2025-11-06 15:01:33,291 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,291 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.51
2025-11-06 15:01:33,291 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,291 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Asia" or "Asian" 8+ times during C5+1 Summit
2025-11-06 15:01:33,291 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:01:33,291 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$2996)
2025-11-06 15:01:33,291 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,291 - market_scanner_v2 - INFO -    - Competition: 1.23278 bars, Score: -117.98
2025-11-06 15:01:33,291 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,291 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Thank you" 8+ times during C5+1 Summit on No
2025-11-06 15:01:33,291 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:01:33,291 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$2347)
2025-11-06 15:01:33,291 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,291 - market_scanner_v2 - INFO -    - Competition: 0.686307 bars, Score: -63.40
2025-11-06 15:01:33,291 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,291 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Nuclear" 2+ times during C5+1 Summit on Nove
2025-11-06 15:01:33,291 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:01:33,291 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$1111)
2025-11-06 15:01:33,291 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,291 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.11
2025-11-06 15:01:33,291 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,291 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Soviet" during C5+1 Summit on November 6?
2025-11-06 15:01:33,292 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:01:33,292 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$923)
2025-11-06 15:01:33,292 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,292 - market_scanner_v2 - INFO -    - Competition: 1.473458 bars, Score: -142.25
2025-11-06 15:01:33,292 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,292 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Best Equipment" during C5+1 Summit on Novemb
2025-11-06 15:01:33,292 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:01:33,292 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$163)
2025-11-06 15:01:33,292 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,292 - market_scanner_v2 - INFO -    - Competition: 0.764207 bars, Score: -71.40
2025-11-06 15:01:33,292 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,292 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Investment" during C5+1 Summit on November 6
2025-11-06 15:01:33,292 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:01:33,292 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$1056)
2025-11-06 15:01:33,292 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,292 - market_scanner_v2 - INFO -    - Competition: 0.711047 bars, Score: -66.00
2025-11-06 15:01:33,292 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,292 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Middle East" during C5+1 Summit on November 
2025-11-06 15:01:33,292 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:01:33,292 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$235)
2025-11-06 15:01:33,292 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,292 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.02
2025-11-06 15:01:33,292 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,292 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Azerbaijan" during C5+1 Summit on November 6
2025-11-06 15:01:33,292 - market_scanner_v2 - INFO -    - Category: science
2025-11-06 15:01:33,292 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$3218)
2025-11-06 15:01:33,292 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,292 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.32
2025-11-06 15:01:33,292 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,293 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Afghanistan" during C5+1 Summit on November 
2025-11-06 15:01:33,293 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:01:33,293 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$335)
2025-11-06 15:01:33,293 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,293 - market_scanner_v2 - INFO -    - Competition: 1.259886 bars, Score: -120.96
2025-11-06 15:01:33,293 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,293 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Eight wars" during C5+1 Summit on November 6
2025-11-06 15:01:33,293 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:01:33,293 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$1260)
2025-11-06 15:01:33,293 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,293 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.13
2025-11-06 15:01:33,293 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,293 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Dead Country" during C5+1 Summit on November
2025-11-06 15:01:33,293 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:01:33,293 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$1372)
2025-11-06 15:01:33,293 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,293 - market_scanner_v2 - INFO -    - Competition: 1.126607 bars, Score: -107.52
2025-11-06 15:01:33,293 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,294 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trumpâ€™s approval rating be less than 42.5 on November 7
2025-11-06 15:01:33,294 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:01:33,294 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$1937)
2025-11-06 15:01:33,294 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,294 - market_scanner_v2 - INFO -    - Competition: 0.988 bars, Score: -93.61
2025-11-06 15:01:33,294 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,294 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike 1 country in November 2025?
2025-11-06 15:01:33,294 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:01:33,294 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$2000)
2025-11-06 15:01:33,294 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,294 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.20
2025-11-06 15:01:33,294 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,295 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike 2 countries in November 2025?
2025-11-06 15:01:33,295 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:01:33,295 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$205)
2025-11-06 15:01:33,295 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,295 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.02
2025-11-06 15:01:33,295 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,295 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Netflix reach $1155 in November?
2025-11-06 15:01:33,295 - market_scanner_v2 - INFO -    - Category: entertainment
2025-11-06 15:01:33,295 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$118)
2025-11-06 15:01:33,295 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,295 - market_scanner_v2 - INFO -    - Competition: 2.477698 bars, Score: -237.76
2025-11-06 15:01:33,295 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,295 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Netflix dip to $1050 in November?
2025-11-06 15:01:33,295 - market_scanner_v2 - INFO -    - Category: entertainment
2025-11-06 15:01:33,295 - market_scanner_v2 - INFO -    - Estimated Reward: $30 (based on volume=$165)
2025-11-06 15:01:33,295 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,295 - market_scanner_v2 - INFO -    - Competition: 0.027444 bars, Score: 12.27
2025-11-06 15:01:33,295 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,296 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Lebanon on November 7?
2025-11-06 15:01:33,296 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:01:33,296 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$1850)
2025-11-06 15:01:33,296 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,296 - market_scanner_v2 - INFO -    - Competition: 0.801783 bars, Score: -69.99
2025-11-06 15:01:33,296 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,296 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Lebanon on November 8?
2025-11-06 15:01:33,296 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:01:33,296 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$365)
2025-11-06 15:01:33,296 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,296 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.04
2025-11-06 15:01:33,296 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,296 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Lebanon on November 9?
2025-11-06 15:01:33,296 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:01:33,296 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$282)
2025-11-06 15:01:33,296 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,296 - market_scanner_v2 - INFO -    - Competition: 0.301766 bars, Score: -20.15
2025-11-06 15:01:33,296 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,296 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Lebanon on November 10?
2025-11-06 15:01:33,296 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:01:33,296 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$76)
2025-11-06 15:01:33,296 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,296 - market_scanner_v2 - INFO -    - Competition: 0.026445 bars, Score: 7.36
2025-11-06 15:01:33,297 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,297 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Lebanon on November 11?
2025-11-06 15:01:33,297 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:01:33,297 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$820)
2025-11-06 15:01:33,297 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,297 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.08
2025-11-06 15:01:33,297 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,297 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Lebanon on November 12?
2025-11-06 15:01:33,297 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:01:33,297 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$94)
2025-11-06 15:01:33,297 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,297 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-06 15:01:33,297 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,297 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Lebanon on November 13?
2025-11-06 15:01:33,297 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:01:33,297 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$20)
2025-11-06 15:01:33,297 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,297 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.00
2025-11-06 15:01:33,297 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,297 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Lebanon on November 14?
2025-11-06 15:01:33,297 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:01:33,297 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$486)
2025-11-06 15:01:33,297 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,297 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.05
2025-11-06 15:01:33,297 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,297 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Gaza on November 7?
2025-11-06 15:01:33,297 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:01:33,297 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$458)
2025-11-06 15:01:33,297 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,297 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.05
2025-11-06 15:01:33,298 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,298 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Gaza on November 8?
2025-11-06 15:01:33,298 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:01:33,298 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$143)
2025-11-06 15:01:33,298 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,298 - market_scanner_v2 - INFO -    - Competition: 0.728054 bars, Score: -62.79
2025-11-06 15:01:33,298 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,298 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Gaza on November 9?
2025-11-06 15:01:33,298 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:01:33,298 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$264)
2025-11-06 15:01:33,298 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,298 - market_scanner_v2 - INFO -    - Competition: 0.01976 bars, Score: 8.05
2025-11-06 15:01:33,298 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,298 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Gaza on November 11?
2025-11-06 15:01:33,298 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:01:33,298 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$173)
2025-11-06 15:01:33,298 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,298 - market_scanner_v2 - INFO -    - Competition: 1.456084 bars, Score: -135.59
2025-11-06 15:01:33,298 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,298 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Gaza on November 12?
2025-11-06 15:01:33,298 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:01:33,298 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$186)
2025-11-06 15:01:33,298 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,298 - market_scanner_v2 - INFO -    - Competition: 2.885517 bars, Score: -278.53
2025-11-06 15:01:33,298 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,298 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel launch a major ground offensive in Lebanon by De
2025-11-06 15:01:33,298 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:01:33,298 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$1547)
2025-11-06 15:01:33,299 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,299 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.15
2025-11-06 15:01:33,299 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,299 - market_scanner_v2 - INFO - âœ… ACCEPTED: Park Sung-jae in jail by November 30?
2025-11-06 15:01:33,299 - market_scanner_v2 - INFO -    - Category: science
2025-11-06 15:01:33,299 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$2915)
2025-11-06 15:01:33,299 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,299 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.29
2025-11-06 15:01:33,299 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,299 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Elon Musk post 160-179 tweets from October 31 to Novemb
2025-11-06 15:01:33,299 - market_scanner_v2 - INFO -    - Category: entertainment
2025-11-06 15:01:33,299 - market_scanner_v2 - INFO -    - Estimated Reward: $130 (based on volume=$92649)
2025-11-06 15:01:33,299 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,299 - market_scanner_v2 - INFO -    - Competition: 1.967677 bars, Score: -122.50
2025-11-06 15:01:33,299 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,299 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Elon Muskâ€™s $1T Tesla pay deal pass?
2025-11-06 15:01:33,299 - market_scanner_v2 - INFO -    - Category: entertainment
2025-11-06 15:01:33,299 - market_scanner_v2 - INFO -    - Estimated Reward: $50 (based on volume=$89521)
2025-11-06 15:01:33,299 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,299 - market_scanner_v2 - INFO -    - Competition: 0.79 bars, Score: -45.05
2025-11-06 15:01:33,299 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,300 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Stable launch a token in 2025?
2025-11-06 15:01:33,300 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:01:33,300 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$78233)
2025-11-06 15:01:33,300 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,300 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 12.82
2025-11-06 15:01:33,300 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,301 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump establish a Gaza â€œBoard of Peaceâ€ in 2025?
2025-11-06 15:01:33,301 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:01:33,301 - market_scanner_v2 - INFO -    - Estimated Reward: $30 (based on volume=$9651)
2025-11-06 15:01:33,301 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,301 - market_scanner_v2 - INFO -    - Competition: 1.144407 bars, Score: -98.48
2025-11-06 15:01:33,301 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,301 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will the Government shutdown end November 8-11?
2025-11-06 15:01:33,301 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:01:33,301 - market_scanner_v2 - INFO -    - Estimated Reward: $200 (based on volume=$192333)
2025-11-06 15:01:33,301 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,301 - market_scanner_v2 - INFO -    - Competition: 2.414525 bars, Score: -122.22
2025-11-06 15:01:33,302 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,302 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will the Government shutdown end November 12-15?
2025-11-06 15:01:33,302 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:01:33,302 - market_scanner_v2 - INFO -    - Estimated Reward: $200 (based on volume=$106409)
2025-11-06 15:01:33,302 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,302 - market_scanner_v2 - INFO -    - Competition: 1.442593 bars, Score: -33.62
2025-11-06 15:01:33,302 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,303 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will MetaMask launch a token by September 30, 2026?
2025-11-06 15:01:33,303 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:01:33,303 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$191)
2025-11-06 15:01:33,303 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,303 - market_scanner_v2 - INFO -    - Competition: 0.818883 bars, Score: -71.87
2025-11-06 15:01:33,303 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,303 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Matt Van Epps win TN-7 Special Election?
2025-11-06 15:01:33,303 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:01:33,303 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$1695)
2025-11-06 15:01:33,303 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,303 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.17
2025-11-06 15:01:33,303 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,303 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Russia capture all of Pokrovsk by November 14?
2025-11-06 15:01:33,303 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:01:33,303 - market_scanner_v2 - INFO -    - Estimated Reward: $30 (based on volume=$13354)
2025-11-06 15:01:33,303 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,303 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 16.34
2025-11-06 15:01:33,303 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,304 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump meet with Putin by November 30?
2025-11-06 15:01:33,304 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:01:33,304 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$13675)
2025-11-06 15:01:33,304 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,304 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 6.37
2025-11-06 15:01:33,304 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,304 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Gemini 3.0 be released by November 15?
2025-11-06 15:01:33,304 - market_scanner_v2 - INFO -    - Category: science
2025-11-06 15:01:33,304 - market_scanner_v2 - INFO -    - Estimated Reward: $200 (based on volume=$495622)
2025-11-06 15:01:33,304 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,304 - market_scanner_v2 - INFO -    - Competition: 0.4896 bars, Score: 100.60
2025-11-06 15:01:33,304 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,304 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Gemini 3.0 be released by November 22?
2025-11-06 15:01:33,304 - market_scanner_v2 - INFO -    - Category: science
2025-11-06 15:01:33,304 - market_scanner_v2 - INFO -    - Estimated Reward: $50 (based on volume=$14533)
2025-11-06 15:01:33,304 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,304 - market_scanner_v2 - INFO -    - Competition: 0.243152 bars, Score: 2.14
2025-11-06 15:01:33,304 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,304 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Russia capture Myrnohrad by November 7?
2025-11-06 15:01:33,305 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:01:33,305 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$7500)
2025-11-06 15:01:33,305 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,305 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.75
2025-11-06 15:01:33,305 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,305 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Oscar Piastri finish second in the 2025 Drivers Champio
2025-11-06 15:01:33,305 - market_scanner_v2 - INFO -    - Category: entertainment
2025-11-06 15:01:33,305 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$119)
2025-11-06 15:01:33,305 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:01:33,305 - market_scanner_v2 - INFO -    - Competition: 2.00974 bars, Score: -195.96
2025-11-06 15:01:33,305 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:01:33,306 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 80/2840 markets passed
2025-11-06 15:01:33,306 - market_scanner_v2 - INFO -    - 2521 rejected: reward < $10
2025-11-06 15:01:33,306 - market_scanner_v2 - INFO -    - 204 rejected: competition > 3
2025-11-06 15:01:33,306 - market_scanner_v2 - INFO -    - 32 rejected: category not in ['crypto', 'sports', 'politics', 'science', 'entertainment']
2025-11-06 15:01:33,306 - market_scanner_v2 - INFO -    - 3 rejected: volume = 0 (no liquidity)
2025-11-06 15:01:33,306 - market_scanner_v2 - INFO - ðŸ” Verifying orderbook for top 50 markets...
2025-11-06 15:01:50,576 - market_scanner_v2 - INFO - âœ… Found 80 qualifying markets (from 2840 total)
2025-11-06 15:01:50,580 - market_selector - INFO - Selected 2 markets from 80 candidates
2025-11-06 15:01:52,982 - order_manager - WARNING - âŒ Calculated prices exceed max spread (96.20% > 3.50%)
2025-11-06 15:01:52,982 - order_manager - WARNING -    This indicates orderbook is too thin or position 2-3 is too far from midpoint
2025-11-06 15:01:52,982 - order_manager - WARNING -    REJECTING market to avoid placing order at position #1 (best bid/ask)
2025-11-06 15:01:52,983 - order_manager - WARNING -    Reason: Adjusting to max spread would place order too close to best bid/ask
2025-11-06 15:01:52,983 - order_manager - WARNING -    â†’ High risk of being filled immediately!
2025-11-06 15:01:52,983 - order_manager - WARNING - Could not calculate valid prices for market 657210
2025-11-06 15:01:52,983 - __main__ - INFO - Added market 657210 to pending orders
2025-11-06 15:01:53,328 - order_manager - WARNING - âŒ Calculated prices exceed max spread (88.20% > 3.50%)
2025-11-06 15:01:53,328 - order_manager - WARNING -    This indicates orderbook is too thin or position 2-3 is too far from midpoint
2025-11-06 15:01:53,328 - order_manager - WARNING -    REJECTING market to avoid placing order at position #1 (best bid/ask)
2025-11-06 15:01:53,328 - order_manager - WARNING -    Reason: Adjusting to max spread would place order too close to best bid/ask
2025-11-06 15:01:53,328 - order_manager - WARNING -    â†’ High risk of being filled immediately!
2025-11-06 15:01:53,328 - order_manager - WARNING - Could not calculate valid prices for market 666798
2025-11-06 15:01:53,329 - __main__ - INFO - Added market 666798 to pending orders
2025-11-06 15:02:54,612 - ml_predictor - INFO - Alert sent: ðŸš¨ <b>MONITORING ALERT</b>

ðŸ”´ KhÃ´ng quÃ©t markets trong 62s!
2025-11-06 15:02:54,612 - monitoring_system - INFO - Alert sent: no_scan
2025-11-06 15:02:54,612 - __main__ - WARNING - âš ï¸ Health check failed: 2 issues
2025-11-06 15:02:54,612 - __main__ - WARNING -    - ðŸ”´ KhÃ´ng quÃ©t markets trong 62s!
2025-11-06 15:02:54,612 - __main__ - WARNING -    - âš ï¸ API cháº­m: 39.0s trung bÃ¬nh
2025-11-06 15:03:01,862 - market_scanner_v2 - INFO - ðŸŒ Scraping markets from /rewards page using Playwright...
2025-11-06 15:03:01,862 - playwright_rewards_scraper - INFO - ðŸŒ Fetching markets from /rewards API...
2025-11-06 15:03:01,862 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 1 (cursor: MA==)...
2025-11-06 15:03:02,310 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 1
2025-11-06 15:03:02,311 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 2 (cursor: MTAw)...
2025-11-06 15:03:02,774 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 2
2025-11-06 15:03:02,775 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 3 (cursor: MjAw)...
2025-11-06 15:03:03,214 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 3
2025-11-06 15:03:03,214 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 4 (cursor: MzAw)...
2025-11-06 15:03:03,957 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 4
2025-11-06 15:03:03,957 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 5 (cursor: NDAw)...
2025-11-06 15:03:04,581 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 5
2025-11-06 15:03:04,582 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 6 (cursor: NTAw)...
2025-11-06 15:03:05,234 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 6
2025-11-06 15:03:05,234 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 7 (cursor: NjAw)...
2025-11-06 15:03:05,891 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 7
2025-11-06 15:03:05,892 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 8 (cursor: NzAw)...
2025-11-06 15:03:06,329 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 8
2025-11-06 15:03:06,330 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 9 (cursor: ODAw)...
2025-11-06 15:03:06,961 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 9
2025-11-06 15:03:06,961 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 10 (cursor: OTAw)...
2025-11-06 15:03:07,615 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 10
2025-11-06 15:03:07,616 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 11 (cursor: MTAwMA==)...
2025-11-06 15:03:08,290 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 11
2025-11-06 15:03:08,290 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 12 (cursor: MTEwMA==)...
2025-11-06 15:03:08,952 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 12
2025-11-06 15:03:08,953 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 13 (cursor: MTIwMA==)...
2025-11-06 15:03:09,640 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 13
2025-11-06 15:03:09,641 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 14 (cursor: MTMwMA==)...
2025-11-06 15:03:10,303 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 14
2025-11-06 15:03:10,304 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 15 (cursor: MTQwMA==)...
2025-11-06 15:03:10,956 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 15
2025-11-06 15:03:10,957 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 16 (cursor: MTUwMA==)...
2025-11-06 15:03:11,607 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 16
2025-11-06 15:03:11,608 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 17 (cursor: MTYwMA==)...
2025-11-06 15:03:12,025 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 17
2025-11-06 15:03:12,025 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 18 (cursor: MTcwMA==)...
2025-11-06 15:03:12,500 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 18
2025-11-06 15:03:12,500 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 19 (cursor: MTgwMA==)...
2025-11-06 15:03:13,177 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 19
2025-11-06 15:03:13,178 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 20 (cursor: MTkwMA==)...
2025-11-06 15:03:13,803 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 20
2025-11-06 15:03:13,803 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 21 (cursor: MjAwMA==)...
2025-11-06 15:03:14,491 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 21
2025-11-06 15:03:14,491 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 22 (cursor: MjEwMA==)...
2025-11-06 15:03:15,130 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 22
2025-11-06 15:03:15,131 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 23 (cursor: MjIwMA==)...
2025-11-06 15:03:15,770 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 23
2025-11-06 15:03:15,771 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 24 (cursor: MjMwMA==)...
2025-11-06 15:03:16,429 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 24
2025-11-06 15:03:16,430 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 25 (cursor: MjQwMA==)...
2025-11-06 15:03:17,092 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 25
2025-11-06 15:03:17,093 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 26 (cursor: MjUwMA==)...
2025-11-06 15:03:17,742 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 26
2025-11-06 15:03:17,743 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 27 (cursor: MjYwMA==)...
2025-11-06 15:03:18,380 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 27
2025-11-06 15:03:18,381 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 28 (cursor: MjcwMA==)...
2025-11-06 15:03:19,069 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 28
2025-11-06 15:03:19,070 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 29 (cursor: MjgwMA==)...
2025-11-06 15:03:19,726 - playwright_rewards_scraper - INFO - âœ… Got 42 markets on page 29
2025-11-06 15:03:19,726 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 30 (cursor: LTE=)...
2025-11-06 15:03:20,027 - playwright_rewards_scraper - INFO - âœ… No more markets on page 30
2025-11-06 15:03:20,028 - playwright_rewards_scraper - INFO - âœ… Fetched 2839 total unique markets from /rewards API
2025-11-06 15:03:20,078 - market_scanner_v2 - INFO - âœ… Got 2839 markets from /rewards page
2025-11-06 15:03:20,078 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Zohran Mamdani win by >9%?
2025-11-06 15:03:20,078 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:03:20,078 - market_scanner_v2 - INFO -    - Estimated Reward: $40 (based on volume=$19063)
2025-11-06 15:03:20,078 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,078 - market_scanner_v2 - INFO -    - Competition: 0.390917 bars, Score: -17.19
2025-11-06 15:03:20,078 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,078 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will any Google Gemini 3 model score at least 1600 on LMAren
2025-11-06 15:03:20,078 - market_scanner_v2 - INFO -    - Category: science
2025-11-06 15:03:20,078 - market_scanner_v2 - INFO -    - Estimated Reward: $50 (based on volume=$9)
2025-11-06 15:03:20,078 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,078 - market_scanner_v2 - INFO -    - Competition: 1.05668 bars, Score: -80.67
2025-11-06 15:03:20,078 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,079 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will â€œThe Witcher: Season 4â€ be the top global Netflix show 
2025-11-06 15:03:20,079 - market_scanner_v2 - INFO -    - Category: entertainment
2025-11-06 15:03:20,079 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$3167)
2025-11-06 15:03:20,079 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,079 - market_scanner_v2 - INFO -    - Competition: 0.329167 bars, Score: -27.60
2025-11-06 15:03:20,079 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,079 - market_scanner_v2 - INFO - âœ… ACCEPTED: Airbnb (ABNB) Up or Down on November 6?
2025-11-06 15:03:20,079 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:03:20,079 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$7056)
2025-11-06 15:03:20,079 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,079 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.71
2025-11-06 15:03:20,079 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,079 - market_scanner_v2 - INFO - âœ… ACCEPTED: Rocket Lab (RKLB) Up or Down on November 6?
2025-11-06 15:03:20,079 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:03:20,079 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$4439)
2025-11-06 15:03:20,079 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,079 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.44
2025-11-06 15:03:20,079 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,079 - market_scanner_v2 - INFO - âœ… ACCEPTED: Opendoor (OPEN) Up or Down on November 6?
2025-11-06 15:03:20,079 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:03:20,079 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$4345)
2025-11-06 15:03:20,079 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,080 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.43
2025-11-06 15:03:20,080 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,080 - market_scanner_v2 - INFO - âœ… ACCEPTED: Palantir (PLTR) Up or Down on November 6?
2025-11-06 15:03:20,080 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:03:20,080 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$3118)
2025-11-06 15:03:20,080 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,080 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.31
2025-11-06 15:03:20,080 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,080 - market_scanner_v2 - INFO - âœ… ACCEPTED: NYA (NYA) Up or Down on November 6?
2025-11-06 15:03:20,080 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:03:20,080 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$4776)
2025-11-06 15:03:20,080 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,080 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.48
2025-11-06 15:03:20,080 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,080 - market_scanner_v2 - INFO - âœ… ACCEPTED: Netflix (NFLX) Up or Down on November 6?
2025-11-06 15:03:20,080 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:03:20,080 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$1972)
2025-11-06 15:03:20,080 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,080 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.20
2025-11-06 15:03:20,080 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,080 - market_scanner_v2 - INFO - âœ… ACCEPTED: Russell 2000 (RUT) Up or Down on November 6?
2025-11-06 15:03:20,080 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:03:20,080 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2856)
2025-11-06 15:03:20,080 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,080 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.29
2025-11-06 15:03:20,080 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,080 - market_scanner_v2 - INFO - âœ… ACCEPTED: NVIDIA (NVDA) Up or Down on November 6?
2025-11-06 15:03:20,080 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:03:20,081 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2086)
2025-11-06 15:03:20,081 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,081 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.21
2025-11-06 15:03:20,081 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,081 - market_scanner_v2 - INFO - âœ… ACCEPTED: Hang Seng (HSI) Up or Down on November 6?
2025-11-06 15:03:20,081 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:03:20,081 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2965)
2025-11-06 15:03:20,081 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,081 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.30
2025-11-06 15:03:20,081 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,081 - market_scanner_v2 - INFO - âœ… ACCEPTED: Tesla (TSLA) Up or Down on November 6?
2025-11-06 15:03:20,081 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:03:20,081 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2431)
2025-11-06 15:03:20,081 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,081 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.24
2025-11-06 15:03:20,081 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,081 - market_scanner_v2 - INFO - âœ… ACCEPTED: DAX (DAX) Up or Down on November 6?
2025-11-06 15:03:20,081 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:03:20,081 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2020)
2025-11-06 15:03:20,081 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,081 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.20
2025-11-06 15:03:20,081 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,081 - market_scanner_v2 - INFO - âœ… ACCEPTED: Meta (META) Up or Down on November 6?
2025-11-06 15:03:20,081 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:03:20,081 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2728)
2025-11-06 15:03:20,081 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,081 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.27
2025-11-06 15:03:20,081 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,082 - market_scanner_v2 - INFO - âœ… ACCEPTED: FTSE 100 (UKX) Up or Down on November 6?
2025-11-06 15:03:20,082 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:03:20,082 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$4234)
2025-11-06 15:03:20,082 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,082 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.42
2025-11-06 15:03:20,082 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,082 - market_scanner_v2 - INFO - âœ… ACCEPTED: Google (GOOGL) Up or Down on November 6?
2025-11-06 15:03:20,082 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:03:20,082 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$908)
2025-11-06 15:03:20,082 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,082 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.09
2025-11-06 15:03:20,082 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,082 - market_scanner_v2 - INFO - âœ… ACCEPTED: Dow Jones (DJI) Up or Down on November 6?
2025-11-06 15:03:20,082 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:03:20,082 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$4720)
2025-11-06 15:03:20,082 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,082 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.47
2025-11-06 15:03:20,082 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,082 - market_scanner_v2 - INFO - âœ… ACCEPTED: NYMEX Crude Oil Futures (WTI) (CL=F) Up or Down on November 
2025-11-06 15:03:20,082 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:03:20,082 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$920)
2025-11-06 15:03:20,082 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,082 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.09
2025-11-06 15:03:20,082 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,082 - market_scanner_v2 - INFO - âœ… ACCEPTED: Amazon (AMZN) Up or Down on November 6?
2025-11-06 15:03:20,082 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:03:20,082 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$5350)
2025-11-06 15:03:20,082 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,082 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.53
2025-11-06 15:03:20,083 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,083 - market_scanner_v2 - INFO - âœ… ACCEPTED: Nasdaq 100 (NDX) Up or Down on November 6?
2025-11-06 15:03:20,083 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:03:20,083 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$5109)
2025-11-06 15:03:20,083 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,083 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.51
2025-11-06 15:03:20,083 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,083 - market_scanner_v2 - INFO - âœ… ACCEPTED: COMEX Silver Futures (SI=F) Up or Down on November 6?
2025-11-06 15:03:20,083 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:03:20,083 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$702)
2025-11-06 15:03:20,083 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,083 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.07
2025-11-06 15:03:20,083 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,083 - market_scanner_v2 - INFO - âœ… ACCEPTED: Microsoft (MSFT) Up or Down on November 6?
2025-11-06 15:03:20,083 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:03:20,083 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2377)
2025-11-06 15:03:20,083 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,083 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.24
2025-11-06 15:03:20,083 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,083 - market_scanner_v2 - INFO - âœ… ACCEPTED: Nikkei 225 (NIK) Up or Down on November 6?
2025-11-06 15:03:20,083 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:03:20,083 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2526)
2025-11-06 15:03:20,083 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,083 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.25
2025-11-06 15:03:20,083 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,083 - market_scanner_v2 - INFO - âœ… ACCEPTED: COMEX Gold Futures (GC=F) Up or Down on November 6?
2025-11-06 15:03:20,083 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:03:20,083 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$792)
2025-11-06 15:03:20,084 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,084 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.08
2025-11-06 15:03:20,084 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,084 - market_scanner_v2 - INFO - âœ… ACCEPTED: S&P 500 (SPX) Up or Down on November 6?
2025-11-06 15:03:20,084 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:03:20,084 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$4717)
2025-11-06 15:03:20,084 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,084 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.47
2025-11-06 15:03:20,084 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,084 - market_scanner_v2 - INFO - âœ… ACCEPTED: Apple (AAPL) Up or Down on November 6?
2025-11-06 15:03:20,084 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:03:20,084 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2700)
2025-11-06 15:03:20,084 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,084 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.27
2025-11-06 15:03:20,084 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,084 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump establish a Gaza â€œBoard of Peaceâ€ by March 31?
2025-11-06 15:03:20,084 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:03:20,084 - market_scanner_v2 - INFO -    - Estimated Reward: $40 (based on volume=$563)
2025-11-06 15:03:20,084 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,084 - market_scanner_v2 - INFO -    - Competition: 0.183595 bars, Score: 1.70
2025-11-06 15:03:20,084 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,084 - market_scanner_v2 - INFO - âœ… ACCEPTED: U.S. Closes Airspace due to Government Shutdown?
2025-11-06 15:03:20,084 - market_scanner_v2 - INFO -    - Category: science
2025-11-06 15:03:20,084 - market_scanner_v2 - INFO -    - Estimated Reward: $50 (based on volume=$12049)
2025-11-06 15:03:20,084 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,084 - market_scanner_v2 - INFO -    - Competition: 0.2222 bars, Score: 3.98
2025-11-06 15:03:20,085 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,085 - market_scanner_v2 - INFO - âœ… ACCEPTED: NYMEX Crude Oil Futures (WTI) (CL=F) Up or Down on November 
2025-11-06 15:03:20,085 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:03:20,085 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$307)
2025-11-06 15:03:20,085 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,085 - market_scanner_v2 - INFO -    - Competition: 0.225 bars, Score: -12.47
2025-11-06 15:03:20,085 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,085 - market_scanner_v2 - INFO - âœ… ACCEPTED: COMEX Silver Futures (SI=F) Up or Down on November 5?
2025-11-06 15:03:20,085 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:03:20,085 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2845)
2025-11-06 15:03:20,085 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,085 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.28
2025-11-06 15:03:20,085 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,085 - market_scanner_v2 - INFO - âœ… ACCEPTED: COMEX Gold Futures (GC=F) Up or Down on November 5?
2025-11-06 15:03:20,085 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:03:20,085 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$416)
2025-11-06 15:03:20,085 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,085 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.04
2025-11-06 15:03:20,085 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,085 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Nancy Pelosi announce her retirement by November 30?
2025-11-06 15:03:20,085 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:03:20,085 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$3188)
2025-11-06 15:03:20,085 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,085 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.32
2025-11-06 15:03:20,086 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,086 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Nancy Pelosi announce her retirement by June 30, 2026?
2025-11-06 15:03:20,086 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:03:20,086 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$5093)
2025-11-06 15:03:20,086 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,086 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.51
2025-11-06 15:03:20,086 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,086 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Asia" or "Asian" 8+ times during C5+1 Summit
2025-11-06 15:03:20,086 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:03:20,086 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$2996)
2025-11-06 15:03:20,086 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,086 - market_scanner_v2 - INFO -    - Competition: 0.799607 bars, Score: -74.66
2025-11-06 15:03:20,086 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,086 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Thank you" 8+ times during C5+1 Summit on No
2025-11-06 15:03:20,086 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:03:20,086 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$2347)
2025-11-06 15:03:20,086 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,086 - market_scanner_v2 - INFO -    - Competition: 0.686307 bars, Score: -63.40
2025-11-06 15:03:20,086 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,086 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Russia" or "China" 4+ times during C5+1 Summ
2025-11-06 15:03:20,086 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:03:20,086 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$2268)
2025-11-06 15:03:20,086 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,086 - market_scanner_v2 - INFO -    - Competition: 2.469406 bars, Score: -241.71
2025-11-06 15:03:20,086 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,086 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Nuclear" 2+ times during C5+1 Summit on Nove
2025-11-06 15:03:20,087 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:03:20,087 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$1111)
2025-11-06 15:03:20,087 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,087 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.11
2025-11-06 15:03:20,087 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,087 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Rare Earth" or "Critical Mineral" during C5+
2025-11-06 15:03:20,087 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:03:20,087 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$1486)
2025-11-06 15:03:20,087 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,087 - market_scanner_v2 - INFO -    - Competition: 2.847725 bars, Score: -279.62
2025-11-06 15:03:20,087 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,087 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Drug" during C5+1 Summit on November 6?
2025-11-06 15:03:20,087 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:03:20,087 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$1165)
2025-11-06 15:03:20,087 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,087 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.12
2025-11-06 15:03:20,087 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,087 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Soviet" during C5+1 Summit on November 6?
2025-11-06 15:03:20,087 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:03:20,087 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$923)
2025-11-06 15:03:20,087 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,087 - market_scanner_v2 - INFO -    - Competition: 1.473458 bars, Score: -142.25
2025-11-06 15:03:20,087 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,087 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Best Equipment" during C5+1 Summit on Novemb
2025-11-06 15:03:20,087 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:03:20,087 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$163)
2025-11-06 15:03:20,087 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,088 - market_scanner_v2 - INFO -    - Competition: 0.764207 bars, Score: -71.40
2025-11-06 15:03:20,088 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,088 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Investment" during C5+1 Summit on November 6
2025-11-06 15:03:20,088 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:03:20,088 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$1056)
2025-11-06 15:03:20,088 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,088 - market_scanner_v2 - INFO -    - Competition: 0.711047 bars, Score: -66.00
2025-11-06 15:03:20,088 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,088 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Middle East" during C5+1 Summit on November 
2025-11-06 15:03:20,088 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:03:20,088 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$235)
2025-11-06 15:03:20,088 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,088 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.02
2025-11-06 15:03:20,088 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,088 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Azerbaijan" during C5+1 Summit on November 6
2025-11-06 15:03:20,088 - market_scanner_v2 - INFO -    - Category: science
2025-11-06 15:03:20,088 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$3218)
2025-11-06 15:03:20,088 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,088 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.32
2025-11-06 15:03:20,088 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,088 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Afghanistan" during C5+1 Summit on November 
2025-11-06 15:03:20,088 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:03:20,088 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$335)
2025-11-06 15:03:20,088 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,088 - market_scanner_v2 - INFO -    - Competition: 1.259886 bars, Score: -120.96
2025-11-06 15:03:20,088 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,088 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Eight wars" during C5+1 Summit on November 6
2025-11-06 15:03:20,089 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:03:20,089 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$1260)
2025-11-06 15:03:20,089 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,089 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.13
2025-11-06 15:03:20,089 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,089 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Dead Country" during C5+1 Summit on November
2025-11-06 15:03:20,089 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:03:20,089 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$1372)
2025-11-06 15:03:20,089 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,089 - market_scanner_v2 - INFO -    - Competition: 1.33234 bars, Score: -128.10
2025-11-06 15:03:20,089 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,090 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trumpâ€™s approval rating be less than 42.5 on November 7
2025-11-06 15:03:20,090 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:03:20,090 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$1937)
2025-11-06 15:03:20,090 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,090 - market_scanner_v2 - INFO -    - Competition: 0.988 bars, Score: -93.61
2025-11-06 15:03:20,090 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,090 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike 1 country in November 2025?
2025-11-06 15:03:20,090 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:03:20,090 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$2000)
2025-11-06 15:03:20,090 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,090 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.20
2025-11-06 15:03:20,090 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,090 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike 2 countries in November 2025?
2025-11-06 15:03:20,090 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:03:20,090 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$205)
2025-11-06 15:03:20,091 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,091 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.02
2025-11-06 15:03:20,091 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,091 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Airbnb reach $128 in November?
2025-11-06 15:03:20,091 - market_scanner_v2 - INFO -    - Category: science
2025-11-06 15:03:20,091 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$35)
2025-11-06 15:03:20,091 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,091 - market_scanner_v2 - INFO -    - Competition: 2.582093 bars, Score: -248.21
2025-11-06 15:03:20,091 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,091 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Netflix reach $1155 in November?
2025-11-06 15:03:20,091 - market_scanner_v2 - INFO -    - Category: entertainment
2025-11-06 15:03:20,091 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$118)
2025-11-06 15:03:20,091 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,091 - market_scanner_v2 - INFO -    - Competition: 2.477698 bars, Score: -237.76
2025-11-06 15:03:20,091 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,091 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Netflix dip to $1050 in November?
2025-11-06 15:03:20,091 - market_scanner_v2 - INFO -    - Category: entertainment
2025-11-06 15:03:20,091 - market_scanner_v2 - INFO -    - Estimated Reward: $30 (based on volume=$165)
2025-11-06 15:03:20,091 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,091 - market_scanner_v2 - INFO -    - Competition: 0.027444 bars, Score: 12.27
2025-11-06 15:03:20,091 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,092 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Lebanon on November 7?
2025-11-06 15:03:20,092 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:03:20,092 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$1850)
2025-11-06 15:03:20,092 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,092 - market_scanner_v2 - INFO -    - Competition: 0.801783 bars, Score: -69.99
2025-11-06 15:03:20,092 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,092 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Lebanon on November 8?
2025-11-06 15:03:20,092 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:03:20,092 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$365)
2025-11-06 15:03:20,092 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,092 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.04
2025-11-06 15:03:20,092 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,092 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Lebanon on November 9?
2025-11-06 15:03:20,092 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:03:20,092 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$282)
2025-11-06 15:03:20,093 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,093 - market_scanner_v2 - INFO -    - Competition: 0.301766 bars, Score: -20.15
2025-11-06 15:03:20,093 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,093 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Lebanon on November 11?
2025-11-06 15:03:20,093 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:03:20,093 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$820)
2025-11-06 15:03:20,093 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,093 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.08
2025-11-06 15:03:20,093 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,093 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Lebanon on November 12?
2025-11-06 15:03:20,093 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:03:20,093 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$94)
2025-11-06 15:03:20,093 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,093 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-06 15:03:20,093 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,093 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Lebanon on November 13?
2025-11-06 15:03:20,093 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:03:20,093 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$20)
2025-11-06 15:03:20,093 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,093 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.00
2025-11-06 15:03:20,093 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,093 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Lebanon on November 14?
2025-11-06 15:03:20,093 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:03:20,093 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$486)
2025-11-06 15:03:20,093 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,093 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.05
2025-11-06 15:03:20,093 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,094 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Gaza on November 7?
2025-11-06 15:03:20,094 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:03:20,094 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$458)
2025-11-06 15:03:20,094 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,094 - market_scanner_v2 - INFO -    - Competition: 0.038697 bars, Score: 6.18
2025-11-06 15:03:20,094 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,094 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Gaza on November 8?
2025-11-06 15:03:20,094 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:03:20,094 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$143)
2025-11-06 15:03:20,094 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,094 - market_scanner_v2 - INFO -    - Competition: 0.728054 bars, Score: -62.79
2025-11-06 15:03:20,094 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,094 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Gaza on November 9?
2025-11-06 15:03:20,094 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:03:20,094 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$264)
2025-11-06 15:03:20,094 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,094 - market_scanner_v2 - INFO -    - Competition: 0.00902 bars, Score: 9.12
2025-11-06 15:03:20,094 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,094 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Gaza on November 11?
2025-11-06 15:03:20,094 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:03:20,094 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$173)
2025-11-06 15:03:20,094 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,094 - market_scanner_v2 - INFO -    - Competition: 1.456084 bars, Score: -135.59
2025-11-06 15:03:20,094 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,094 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Gaza on November 12?
2025-11-06 15:03:20,094 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:03:20,095 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$186)
2025-11-06 15:03:20,095 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,095 - market_scanner_v2 - INFO -    - Competition: 2.885517 bars, Score: -278.53
2025-11-06 15:03:20,095 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,095 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel launch a major ground offensive in Lebanon by De
2025-11-06 15:03:20,095 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:03:20,095 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$1547)
2025-11-06 15:03:20,095 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,095 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.15
2025-11-06 15:03:20,095 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,095 - market_scanner_v2 - INFO - âœ… ACCEPTED: Park Sung-jae in jail by November 30?
2025-11-06 15:03:20,095 - market_scanner_v2 - INFO -    - Category: science
2025-11-06 15:03:20,095 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$2915)
2025-11-06 15:03:20,095 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,095 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.29
2025-11-06 15:03:20,095 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,095 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Elon Musk post 160-179 tweets from October 31 to Novemb
2025-11-06 15:03:20,095 - market_scanner_v2 - INFO -    - Category: entertainment
2025-11-06 15:03:20,095 - market_scanner_v2 - INFO -    - Estimated Reward: $130 (based on volume=$92649)
2025-11-06 15:03:20,095 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,095 - market_scanner_v2 - INFO -    - Competition: 1.41758 bars, Score: -67.49
2025-11-06 15:03:20,095 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,096 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Elon Muskâ€™s $1T Tesla pay deal pass?
2025-11-06 15:03:20,096 - market_scanner_v2 - INFO -    - Category: entertainment
2025-11-06 15:03:20,096 - market_scanner_v2 - INFO -    - Estimated Reward: $50 (based on volume=$89521)
2025-11-06 15:03:20,096 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,096 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 33.95
2025-11-06 15:03:20,096 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,096 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Stable launch a token in 2025?
2025-11-06 15:03:20,097 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:03:20,097 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$78233)
2025-11-06 15:03:20,097 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,097 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 12.82
2025-11-06 15:03:20,097 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,098 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump establish a Gaza â€œBoard of Peaceâ€ in 2025?
2025-11-06 15:03:20,098 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:03:20,098 - market_scanner_v2 - INFO -    - Estimated Reward: $30 (based on volume=$9651)
2025-11-06 15:03:20,098 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,098 - market_scanner_v2 - INFO -    - Competition: 0.396333 bars, Score: -23.67
2025-11-06 15:03:20,098 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,098 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will the Government shutdown end November 8-11?
2025-11-06 15:03:20,098 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:03:20,098 - market_scanner_v2 - INFO -    - Estimated Reward: $200 (based on volume=$192333)
2025-11-06 15:03:20,098 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,098 - market_scanner_v2 - INFO -    - Competition: 1.353272 bars, Score: -16.09
2025-11-06 15:03:20,098 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,098 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will the Government shutdown end November 12-15?
2025-11-06 15:03:20,098 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:03:20,098 - market_scanner_v2 - INFO -    - Estimated Reward: $200 (based on volume=$106409)
2025-11-06 15:03:20,098 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,098 - market_scanner_v2 - INFO -    - Competition: 1.442593 bars, Score: -33.62
2025-11-06 15:03:20,098 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,099 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will MetaMask launch a token by September 30, 2026?
2025-11-06 15:03:20,099 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:03:20,099 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$191)
2025-11-06 15:03:20,099 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,099 - market_scanner_v2 - INFO -    - Competition: 0.818883 bars, Score: -71.87
2025-11-06 15:03:20,099 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,100 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Matt Van Epps win TN-7 Special Election?
2025-11-06 15:03:20,100 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:03:20,100 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$1695)
2025-11-06 15:03:20,100 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,100 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.17
2025-11-06 15:03:20,100 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,100 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Russia capture all of Pokrovsk by November 14?
2025-11-06 15:03:20,100 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:03:20,100 - market_scanner_v2 - INFO -    - Estimated Reward: $30 (based on volume=$13354)
2025-11-06 15:03:20,100 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,100 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 16.34
2025-11-06 15:03:20,100 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,100 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump meet with Putin by November 30?
2025-11-06 15:03:20,100 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:03:20,100 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$13675)
2025-11-06 15:03:20,100 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,100 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 6.37
2025-11-06 15:03:20,100 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,101 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Gemini 3.0 be released by November 15?
2025-11-06 15:03:20,101 - market_scanner_v2 - INFO -    - Category: science
2025-11-06 15:03:20,101 - market_scanner_v2 - INFO -    - Estimated Reward: $200 (based on volume=$495622)
2025-11-06 15:03:20,101 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,101 - market_scanner_v2 - INFO -    - Competition: 0.4896 bars, Score: 100.60
2025-11-06 15:03:20,101 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,101 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Gemini 3.0 be released by November 22?
2025-11-06 15:03:20,101 - market_scanner_v2 - INFO -    - Category: science
2025-11-06 15:03:20,101 - market_scanner_v2 - INFO -    - Estimated Reward: $50 (based on volume=$14533)
2025-11-06 15:03:20,101 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,101 - market_scanner_v2 - INFO -    - Competition: 0.243152 bars, Score: 2.14
2025-11-06 15:03:20,101 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,101 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Russia capture Myrnohrad by November 7?
2025-11-06 15:03:20,101 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:03:20,101 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$7500)
2025-11-06 15:03:20,101 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,101 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.75
2025-11-06 15:03:20,101 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,102 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Oscar Piastri finish second in the 2025 Drivers Champio
2025-11-06 15:03:20,102 - market_scanner_v2 - INFO -    - Category: entertainment
2025-11-06 15:03:20,102 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$119)
2025-11-06 15:03:20,102 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,102 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.01
2025-11-06 15:03:20,102 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,102 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump pardon Diddy in 2025?
2025-11-06 15:03:20,102 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:03:20,103 - market_scanner_v2 - INFO -    - Estimated Reward: $30 (based on volume=$8435)
2025-11-06 15:03:20,103 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,103 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 15.84
2025-11-06 15:03:20,103 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,103 - market_scanner_v2 - INFO - âœ… ACCEPTED: TikTok sale announced in 2025?
2025-11-06 15:03:20,103 - market_scanner_v2 - INFO -    - Category: entertainment
2025-11-06 15:03:20,103 - market_scanner_v2 - INFO -    - Estimated Reward: $30 (based on volume=$6818)
2025-11-06 15:03:20,103 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,103 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 15.68
2025-11-06 15:03:20,103 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,103 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Oscar Piastri be the 2025 Drivers Champion?
2025-11-06 15:03:20,103 - market_scanner_v2 - INFO -    - Category: entertainment
2025-11-06 15:03:20,103 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$25940)
2025-11-06 15:03:20,103 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:03:20,103 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 7.59
2025-11-06 15:03:20,103 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:03:20,104 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 85/2839 markets passed
2025-11-06 15:03:20,104 - market_scanner_v2 - INFO -    - 2520 rejected: reward < $10
2025-11-06 15:03:20,104 - market_scanner_v2 - INFO -    - 194 rejected: competition > 3
2025-11-06 15:03:20,104 - market_scanner_v2 - INFO -    - 37 rejected: category not in ['crypto', 'sports', 'politics', 'science', 'entertainment']
2025-11-06 15:03:20,104 - market_scanner_v2 - INFO -    - 3 rejected: volume = 0 (no liquidity)
2025-11-06 15:03:20,104 - market_scanner_v2 - INFO - ðŸ” Verifying orderbook for top 50 markets...
2025-11-06 15:03:37,462 - market_scanner_v2 - INFO - âœ… Found 85 qualifying markets (from 2839 total)
2025-11-06 15:03:37,466 - market_selector - INFO - Selected 2 markets from 85 candidates
2025-11-06 15:03:40,237 - order_manager - WARNING - âŒ Calculated prices exceed max spread (99.40% > 3.50%)
2025-11-06 15:03:40,238 - order_manager - WARNING -    This indicates orderbook is too thin or position 2-3 is too far from midpoint
2025-11-06 15:03:40,238 - order_manager - WARNING -    REJECTING market to avoid placing order at position #1 (best bid/ask)
2025-11-06 15:03:40,238 - order_manager - WARNING -    Reason: Adjusting to max spread would place order too close to best bid/ask
2025-11-06 15:03:40,238 - order_manager - WARNING -    â†’ High risk of being filled immediately!
2025-11-06 15:03:40,238 - order_manager - WARNING - Could not calculate valid prices for market 644988
2025-11-06 15:03:40,238 - __main__ - INFO - Added market 644988 to pending orders
2025-11-06 15:03:40,630 - order_manager - WARNING - âŒ Calculated prices exceed max spread (94.20% > 3.50%)
2025-11-06 15:03:40,631 - order_manager - WARNING -    This indicates orderbook is too thin or position 2-3 is too far from midpoint
2025-11-06 15:03:40,631 - order_manager - WARNING -    REJECTING market to avoid placing order at position #1 (best bid/ask)
2025-11-06 15:03:40,631 - order_manager - WARNING -    Reason: Adjusting to max spread would place order too close to best bid/ask
2025-11-06 15:03:40,631 - order_manager - WARNING -    â†’ High risk of being filled immediately!
2025-11-06 15:03:40,631 - order_manager - WARNING - Could not calculate valid prices for market 657210
2025-11-06 15:03:40,631 - __main__ - INFO - Added market 657210 to pending orders
2025-11-06 15:04:40,478 - __main__ - WARNING - âš ï¸ Health check failed: 2 issues
2025-11-06 15:04:40,479 - __main__ - WARNING -    - ðŸ”´ KhÃ´ng quÃ©t markets trong 62s!
2025-11-06 15:04:40,479 - __main__ - WARNING -    - âš ï¸ API cháº­m: 39.0s trung bÃ¬nh
2025-11-06 15:04:47,066 - market_scanner_v2 - INFO - ðŸŒ Scraping markets from /rewards page using Playwright...
2025-11-06 15:04:47,066 - playwright_rewards_scraper - INFO - ðŸŒ Fetching markets from /rewards API...
2025-11-06 15:04:47,066 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 1 (cursor: MA==)...
2025-11-06 15:04:47,760 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 1
2025-11-06 15:04:47,761 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 2 (cursor: MTAw)...
2025-11-06 15:04:48,221 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 2
2025-11-06 15:04:48,221 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 3 (cursor: MjAw)...
2025-11-06 15:04:48,898 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 3
2025-11-06 15:04:48,899 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 4 (cursor: MzAw)...
2025-11-06 15:04:49,608 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 4
2025-11-06 15:04:49,608 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 5 (cursor: NDAw)...
2025-11-06 15:04:50,476 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 5
2025-11-06 15:04:50,477 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 6 (cursor: NTAw)...
2025-11-06 15:04:51,130 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 6
2025-11-06 15:04:51,131 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 7 (cursor: NjAw)...
2025-11-06 15:04:51,936 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 7
2025-11-06 15:04:51,936 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 8 (cursor: NzAw)...
2025-11-06 15:04:52,682 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 8
2025-11-06 15:04:52,683 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 9 (cursor: ODAw)...
2025-11-06 15:04:53,335 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 9
2025-11-06 15:04:53,335 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 10 (cursor: OTAw)...
2025-11-06 15:04:53,989 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 10
2025-11-06 15:04:53,990 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 11 (cursor: MTAwMA==)...
2025-11-06 15:04:54,676 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 11
2025-11-06 15:04:54,676 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 12 (cursor: MTEwMA==)...
2025-11-06 15:04:55,141 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 12
2025-11-06 15:04:55,142 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 13 (cursor: MTIwMA==)...
2025-11-06 15:04:55,691 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 13
2025-11-06 15:04:55,692 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 14 (cursor: MTMwMA==)...
2025-11-06 15:04:56,359 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 14
2025-11-06 15:04:56,359 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 15 (cursor: MTQwMA==)...
2025-11-06 15:04:57,006 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 15
2025-11-06 15:04:57,007 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 16 (cursor: MTUwMA==)...
2025-11-06 15:04:57,556 - __main__ - INFO - Shutdown signal received
2025-11-06 15:04:57,655 - __main__ - INFO - Shutting down bot...
2025-11-06 15:04:57,655 - order_manager - INFO - Cancelled 0 orders
2025-11-06 15:04:57,655 - __main__ - INFO - Bot shutdown complete
2025-11-06 15:04:57,659 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 16
2025-11-06 15:04:57,659 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 17 (cursor: MTYwMA==)...
2025-11-06 15:04:58,338 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 17
2025-11-06 15:04:58,339 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 18 (cursor: MTcwMA==)...
2025-11-06 15:04:58,998 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 18
2025-11-06 15:04:58,999 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 19 (cursor: MTgwMA==)...
2025-11-06 15:04:59,709 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 19
2025-11-06 15:04:59,710 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 20 (cursor: MTkwMA==)...
2025-11-06 15:05:00,359 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 20
2025-11-06 15:05:00,359 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 21 (cursor: MjAwMA==)...
2025-11-06 15:05:01,007 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 21
2025-11-06 15:05:01,008 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 22 (cursor: MjEwMA==)...
2025-11-06 15:05:01,775 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 22
2025-11-06 15:05:01,776 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 23 (cursor: MjIwMA==)...
2025-11-06 15:05:02,584 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 23
2025-11-06 15:05:02,585 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 24 (cursor: MjMwMA==)...
2025-11-06 15:05:03,298 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 24
2025-11-06 15:05:03,298 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 25 (cursor: MjQwMA==)...
2025-11-06 15:05:03,954 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 25
2025-11-06 15:05:03,955 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 26 (cursor: MjUwMA==)...
2025-11-06 15:05:04,612 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 26
2025-11-06 15:05:04,613 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 27 (cursor: MjYwMA==)...
2025-11-06 15:05:05,108 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 27
2025-11-06 15:05:05,109 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 28 (cursor: MjcwMA==)...
2025-11-06 15:05:05,605 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 28
2025-11-06 15:05:05,606 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 29 (cursor: MjgwMA==)...
2025-11-06 15:05:06,281 - playwright_rewards_scraper - INFO - âœ… Got 42 markets on page 29
2025-11-06 15:05:06,282 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 30 (cursor: LTE=)...
2025-11-06 15:05:06,576 - playwright_rewards_scraper - INFO - âœ… No more markets on page 30
2025-11-06 15:05:06,577 - playwright_rewards_scraper - INFO - âœ… Fetched 2840 total unique markets from /rewards API
2025-11-06 15:05:06,627 - market_scanner_v2 - INFO - âœ… Got 2840 markets from /rewards page
2025-11-06 15:05:06,627 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Zohran Mamdani win by >9%?
2025-11-06 15:05:06,627 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:05:06,627 - market_scanner_v2 - INFO -    - Estimated Reward: $40 (based on volume=$19063)
2025-11-06 15:05:06,627 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,627 - market_scanner_v2 - INFO -    - Competition: 0.102917 bars, Score: 11.61
2025-11-06 15:05:06,627 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,627 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will any Google Gemini 3 model score at least 1600 on LMAren
2025-11-06 15:05:06,627 - market_scanner_v2 - INFO -    - Category: science
2025-11-06 15:05:06,627 - market_scanner_v2 - INFO -    - Estimated Reward: $50 (based on volume=$9)
2025-11-06 15:05:06,627 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,627 - market_scanner_v2 - INFO -    - Competition: 1.509968 bars, Score: -126.00
2025-11-06 15:05:06,627 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,628 - market_scanner_v2 - INFO - âœ… ACCEPTED: Airbnb (ABNB) Up or Down on November 6?
2025-11-06 15:05:06,628 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:05:06,628 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$7056)
2025-11-06 15:05:06,628 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,628 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.71
2025-11-06 15:05:06,628 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,628 - market_scanner_v2 - INFO - âœ… ACCEPTED: Rocket Lab (RKLB) Up or Down on November 6?
2025-11-06 15:05:06,628 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:05:06,628 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$4439)
2025-11-06 15:05:06,628 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,628 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.44
2025-11-06 15:05:06,628 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,628 - market_scanner_v2 - INFO - âœ… ACCEPTED: Opendoor (OPEN) Up or Down on November 6?
2025-11-06 15:05:06,628 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:05:06,628 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$4345)
2025-11-06 15:05:06,628 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,628 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.43
2025-11-06 15:05:06,628 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,628 - market_scanner_v2 - INFO - âœ… ACCEPTED: Palantir (PLTR) Up or Down on November 6?
2025-11-06 15:05:06,628 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:05:06,628 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$3118)
2025-11-06 15:05:06,628 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,628 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.31
2025-11-06 15:05:06,628 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,628 - market_scanner_v2 - INFO - âœ… ACCEPTED: NYA (NYA) Up or Down on November 6?
2025-11-06 15:05:06,628 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:05:06,629 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$4776)
2025-11-06 15:05:06,629 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,629 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.48
2025-11-06 15:05:06,629 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,629 - market_scanner_v2 - INFO - âœ… ACCEPTED: Netflix (NFLX) Up or Down on November 6?
2025-11-06 15:05:06,629 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:05:06,629 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$1972)
2025-11-06 15:05:06,629 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,629 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.20
2025-11-06 15:05:06,629 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,629 - market_scanner_v2 - INFO - âœ… ACCEPTED: Russell 2000 (RUT) Up or Down on November 6?
2025-11-06 15:05:06,629 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:05:06,629 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2856)
2025-11-06 15:05:06,629 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,629 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.29
2025-11-06 15:05:06,629 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,629 - market_scanner_v2 - INFO - âœ… ACCEPTED: NVIDIA (NVDA) Up or Down on November 6?
2025-11-06 15:05:06,629 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:05:06,629 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2086)
2025-11-06 15:05:06,629 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,629 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.21
2025-11-06 15:05:06,629 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,629 - market_scanner_v2 - INFO - âœ… ACCEPTED: Hang Seng (HSI) Up or Down on November 6?
2025-11-06 15:05:06,629 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:05:06,629 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2965)
2025-11-06 15:05:06,629 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,629 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.30
2025-11-06 15:05:06,629 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,629 - market_scanner_v2 - INFO - âœ… ACCEPTED: Tesla (TSLA) Up or Down on November 6?
2025-11-06 15:05:06,629 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:05:06,630 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2431)
2025-11-06 15:05:06,630 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,630 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.24
2025-11-06 15:05:06,630 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,630 - market_scanner_v2 - INFO - âœ… ACCEPTED: DAX (DAX) Up or Down on November 6?
2025-11-06 15:05:06,630 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:05:06,630 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2020)
2025-11-06 15:05:06,630 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,630 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.20
2025-11-06 15:05:06,630 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,630 - market_scanner_v2 - INFO - âœ… ACCEPTED: Meta (META) Up or Down on November 6?
2025-11-06 15:05:06,630 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:05:06,630 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2728)
2025-11-06 15:05:06,630 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,630 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.27
2025-11-06 15:05:06,630 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,630 - market_scanner_v2 - INFO - âœ… ACCEPTED: FTSE 100 (UKX) Up or Down on November 6?
2025-11-06 15:05:06,630 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:05:06,630 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$4234)
2025-11-06 15:05:06,630 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,630 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.42
2025-11-06 15:05:06,630 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,630 - market_scanner_v2 - INFO - âœ… ACCEPTED: Google (GOOGL) Up or Down on November 6?
2025-11-06 15:05:06,630 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:05:06,630 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$908)
2025-11-06 15:05:06,630 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,630 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.09
2025-11-06 15:05:06,630 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,630 - market_scanner_v2 - INFO - âœ… ACCEPTED: Dow Jones (DJI) Up or Down on November 6?
2025-11-06 15:05:06,630 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:05:06,631 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$4720)
2025-11-06 15:05:06,631 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,631 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.47
2025-11-06 15:05:06,631 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,631 - market_scanner_v2 - INFO - âœ… ACCEPTED: NYMEX Crude Oil Futures (WTI) (CL=F) Up or Down on November 
2025-11-06 15:05:06,631 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:05:06,631 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$920)
2025-11-06 15:05:06,631 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,631 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.09
2025-11-06 15:05:06,631 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,631 - market_scanner_v2 - INFO - âœ… ACCEPTED: Amazon (AMZN) Up or Down on November 6?
2025-11-06 15:05:06,631 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:05:06,631 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$5350)
2025-11-06 15:05:06,631 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,631 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.53
2025-11-06 15:05:06,631 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,631 - market_scanner_v2 - INFO - âœ… ACCEPTED: Nasdaq 100 (NDX) Up or Down on November 6?
2025-11-06 15:05:06,631 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:05:06,631 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$5109)
2025-11-06 15:05:06,631 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,631 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.51
2025-11-06 15:05:06,631 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,631 - market_scanner_v2 - INFO - âœ… ACCEPTED: COMEX Silver Futures (SI=F) Up or Down on November 6?
2025-11-06 15:05:06,631 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:05:06,631 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$702)
2025-11-06 15:05:06,631 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,631 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.07
2025-11-06 15:05:06,631 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,631 - market_scanner_v2 - INFO - âœ… ACCEPTED: Microsoft (MSFT) Up or Down on November 6?
2025-11-06 15:05:06,632 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:05:06,632 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2377)
2025-11-06 15:05:06,632 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,632 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.24
2025-11-06 15:05:06,632 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,632 - market_scanner_v2 - INFO - âœ… ACCEPTED: Nikkei 225 (NIK) Up or Down on November 6?
2025-11-06 15:05:06,632 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:05:06,632 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2526)
2025-11-06 15:05:06,632 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,632 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.25
2025-11-06 15:05:06,632 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,632 - market_scanner_v2 - INFO - âœ… ACCEPTED: COMEX Gold Futures (GC=F) Up or Down on November 6?
2025-11-06 15:05:06,632 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:05:06,632 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$792)
2025-11-06 15:05:06,632 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,632 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.08
2025-11-06 15:05:06,632 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,632 - market_scanner_v2 - INFO - âœ… ACCEPTED: S&P 500 (SPX) Up or Down on November 6?
2025-11-06 15:05:06,632 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:05:06,632 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$4717)
2025-11-06 15:05:06,632 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,632 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.47
2025-11-06 15:05:06,632 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,632 - market_scanner_v2 - INFO - âœ… ACCEPTED: Apple (AAPL) Up or Down on November 6?
2025-11-06 15:05:06,632 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:05:06,632 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2700)
2025-11-06 15:05:06,632 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,632 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.27
2025-11-06 15:05:06,632 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,633 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump establish a Gaza â€œBoard of Peaceâ€ by March 31?
2025-11-06 15:05:06,633 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:05:06,633 - market_scanner_v2 - INFO -    - Estimated Reward: $40 (based on volume=$563)
2025-11-06 15:05:06,633 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,633 - market_scanner_v2 - INFO -    - Competition: 0.772267 bars, Score: -57.17
2025-11-06 15:05:06,633 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,633 - market_scanner_v2 - INFO - âœ… ACCEPTED: U.S. Closes Airspace due to Government Shutdown?
2025-11-06 15:05:06,633 - market_scanner_v2 - INFO -    - Category: science
2025-11-06 15:05:06,633 - market_scanner_v2 - INFO -    - Estimated Reward: $50 (based on volume=$12049)
2025-11-06 15:05:06,633 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,633 - market_scanner_v2 - INFO -    - Competition: 0.131733 bars, Score: 13.03
2025-11-06 15:05:06,633 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,633 - market_scanner_v2 - INFO - âœ… ACCEPTED: NYMEX Crude Oil Futures (WTI) (CL=F) Up or Down on November 
2025-11-06 15:05:06,633 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:05:06,633 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$307)
2025-11-06 15:05:06,633 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,633 - market_scanner_v2 - INFO -    - Competition: 0.225 bars, Score: -12.47
2025-11-06 15:05:06,633 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,633 - market_scanner_v2 - INFO - âœ… ACCEPTED: COMEX Silver Futures (SI=F) Up or Down on November 5?
2025-11-06 15:05:06,633 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:05:06,633 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2845)
2025-11-06 15:05:06,633 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,633 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.28
2025-11-06 15:05:06,633 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,633 - market_scanner_v2 - INFO - âœ… ACCEPTED: COMEX Gold Futures (GC=F) Up or Down on November 5?
2025-11-06 15:05:06,634 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:05:06,634 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$416)
2025-11-06 15:05:06,634 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,634 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.04
2025-11-06 15:05:06,634 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,634 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Nancy Pelosi announce her retirement by November 30?
2025-11-06 15:05:06,634 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:05:06,634 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$3188)
2025-11-06 15:05:06,634 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,634 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.32
2025-11-06 15:05:06,634 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,634 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Nancy Pelosi announce her retirement by June 30, 2026?
2025-11-06 15:05:06,634 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:05:06,634 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$5093)
2025-11-06 15:05:06,634 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,634 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.51
2025-11-06 15:05:06,634 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,634 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Asia" or "Asian" 8+ times during C5+1 Summit
2025-11-06 15:05:06,634 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:05:06,634 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$2996)
2025-11-06 15:05:06,634 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,634 - market_scanner_v2 - INFO -    - Competition: 1.00337 bars, Score: -95.04
2025-11-06 15:05:06,634 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,634 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Thank you" 8+ times during C5+1 Summit on No
2025-11-06 15:05:06,634 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:05:06,634 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$2347)
2025-11-06 15:05:06,634 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,634 - market_scanner_v2 - INFO -    - Competition: 0.608537 bars, Score: -55.62
2025-11-06 15:05:06,635 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,635 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Nuclear" 2+ times during C5+1 Summit on Nove
2025-11-06 15:05:06,635 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:05:06,635 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$1111)
2025-11-06 15:05:06,635 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,635 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.11
2025-11-06 15:05:06,635 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,635 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Rare Earth" or "Critical Mineral" during C5+
2025-11-06 15:05:06,635 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:05:06,635 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$1486)
2025-11-06 15:05:06,635 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,635 - market_scanner_v2 - INFO -    - Competition: 2.847725 bars, Score: -279.62
2025-11-06 15:05:06,635 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,635 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Drug" during C5+1 Summit on November 6?
2025-11-06 15:05:06,635 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:05:06,635 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$1165)
2025-11-06 15:05:06,635 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,635 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.12
2025-11-06 15:05:06,635 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,635 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Soviet" during C5+1 Summit on November 6?
2025-11-06 15:05:06,635 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:05:06,635 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$923)
2025-11-06 15:05:06,635 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,635 - market_scanner_v2 - INFO -    - Competition: 1.473458 bars, Score: -142.25
2025-11-06 15:05:06,635 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,635 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Best Equipment" during C5+1 Summit on Novemb
2025-11-06 15:05:06,635 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:05:06,635 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$163)
2025-11-06 15:05:06,636 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,636 - market_scanner_v2 - INFO -    - Competition: 0.764207 bars, Score: -71.40
2025-11-06 15:05:06,636 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,636 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Investment" during C5+1 Summit on November 6
2025-11-06 15:05:06,636 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:05:06,636 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$1056)
2025-11-06 15:05:06,636 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,636 - market_scanner_v2 - INFO -    - Competition: 0.711047 bars, Score: -66.00
2025-11-06 15:05:06,636 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,636 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Middle East" during C5+1 Summit on November 
2025-11-06 15:05:06,636 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:05:06,636 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$235)
2025-11-06 15:05:06,636 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,636 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.02
2025-11-06 15:05:06,636 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,636 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Azerbaijan" during C5+1 Summit on November 6
2025-11-06 15:05:06,636 - market_scanner_v2 - INFO -    - Category: science
2025-11-06 15:05:06,636 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$3218)
2025-11-06 15:05:06,636 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,636 - market_scanner_v2 - INFO -    - Competition: 0.148313 bars, Score: -9.51
2025-11-06 15:05:06,636 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,636 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Afghanistan" during C5+1 Summit on November 
2025-11-06 15:05:06,636 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:05:06,636 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$335)
2025-11-06 15:05:06,636 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,636 - market_scanner_v2 - INFO -    - Competition: 0.771046 bars, Score: -72.07
2025-11-06 15:05:06,636 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,637 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Eight wars" during C5+1 Summit on November 6
2025-11-06 15:05:06,637 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:05:06,637 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$1260)
2025-11-06 15:05:06,637 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,637 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.13
2025-11-06 15:05:06,637 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,637 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Dead Country" during C5+1 Summit on November
2025-11-06 15:05:06,637 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:05:06,637 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$1372)
2025-11-06 15:05:06,637 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,637 - market_scanner_v2 - INFO -    - Competition: 0.453193 bars, Score: -40.18
2025-11-06 15:05:06,637 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,637 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Mamdani make NYC buses free by March 31?
2025-11-06 15:05:06,637 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:05:06,637 - market_scanner_v2 - INFO -    - Estimated Reward: $100 (based on volume=$7076)
2025-11-06 15:05:06,637 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,637 - market_scanner_v2 - INFO -    - Competition: 2.868921 bars, Score: -236.18
2025-11-06 15:05:06,637 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,638 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trumpâ€™s approval rating be less than 42.5 on November 7
2025-11-06 15:05:06,638 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:05:06,638 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$1937)
2025-11-06 15:05:06,638 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,638 - market_scanner_v2 - INFO -    - Competition: 0.988 bars, Score: -93.61
2025-11-06 15:05:06,638 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,638 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike 1 country in November 2025?
2025-11-06 15:05:06,638 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:05:06,638 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$2000)
2025-11-06 15:05:06,638 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,638 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.20
2025-11-06 15:05:06,639 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,639 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike 2 countries in November 2025?
2025-11-06 15:05:06,639 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:05:06,639 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$205)
2025-11-06 15:05:06,639 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,639 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.02
2025-11-06 15:05:06,639 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,639 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Airbnb reach $128 in November?
2025-11-06 15:05:06,639 - market_scanner_v2 - INFO -    - Category: science
2025-11-06 15:05:06,639 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$35)
2025-11-06 15:05:06,639 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,639 - market_scanner_v2 - INFO -    - Competition: 0.173507 bars, Score: -7.35
2025-11-06 15:05:06,639 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,639 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Netflix reach $1155 in November?
2025-11-06 15:05:06,639 - market_scanner_v2 - INFO -    - Category: entertainment
2025-11-06 15:05:06,639 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$118)
2025-11-06 15:05:06,639 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,639 - market_scanner_v2 - INFO -    - Competition: 2.477698 bars, Score: -237.76
2025-11-06 15:05:06,639 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,639 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Netflix dip to $1050 in November?
2025-11-06 15:05:06,639 - market_scanner_v2 - INFO -    - Category: entertainment
2025-11-06 15:05:06,639 - market_scanner_v2 - INFO -    - Estimated Reward: $30 (based on volume=$165)
2025-11-06 15:05:06,639 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,639 - market_scanner_v2 - INFO -    - Competition: 0.027444 bars, Score: 12.27
2025-11-06 15:05:06,640 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,640 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Lebanon on November 7?
2025-11-06 15:05:06,640 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:05:06,640 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$1850)
2025-11-06 15:05:06,640 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,640 - market_scanner_v2 - INFO -    - Competition: 0.98695 bars, Score: -88.51
2025-11-06 15:05:06,640 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,640 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Lebanon on November 8?
2025-11-06 15:05:06,640 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:05:06,640 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$365)
2025-11-06 15:05:06,640 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,640 - market_scanner_v2 - INFO -    - Competition: 1.333333 bars, Score: -123.30
2025-11-06 15:05:06,640 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,640 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Lebanon on November 9?
2025-11-06 15:05:06,640 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:05:06,640 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$282)
2025-11-06 15:05:06,640 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,641 - market_scanner_v2 - INFO -    - Competition: 0.301766 bars, Score: -20.15
2025-11-06 15:05:06,641 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,641 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Lebanon on November 11?
2025-11-06 15:05:06,641 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:05:06,641 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$820)
2025-11-06 15:05:06,641 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,641 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.08
2025-11-06 15:05:06,641 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,641 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Lebanon on November 12?
2025-11-06 15:05:06,641 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:05:06,641 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$94)
2025-11-06 15:05:06,641 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,641 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-06 15:05:06,641 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,641 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Lebanon on November 13?
2025-11-06 15:05:06,641 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:05:06,641 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$20)
2025-11-06 15:05:06,641 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,641 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.00
2025-11-06 15:05:06,641 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,641 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Lebanon on November 14?
2025-11-06 15:05:06,641 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:05:06,641 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$486)
2025-11-06 15:05:06,641 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,641 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.05
2025-11-06 15:05:06,641 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,641 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Gaza on November 7?
2025-11-06 15:05:06,641 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:05:06,641 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$458)
2025-11-06 15:05:06,642 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,642 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.05
2025-11-06 15:05:06,642 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,642 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Gaza on November 8?
2025-11-06 15:05:06,642 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:05:06,642 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$143)
2025-11-06 15:05:06,642 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,642 - market_scanner_v2 - INFO -    - Competition: 0.959392 bars, Score: -85.92
2025-11-06 15:05:06,642 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,642 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Gaza on November 9?
2025-11-06 15:05:06,642 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:05:06,642 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$264)
2025-11-06 15:05:06,642 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,642 - market_scanner_v2 - INFO -    - Competition: 0.005125 bars, Score: 9.51
2025-11-06 15:05:06,642 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,642 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Gaza on November 11?
2025-11-06 15:05:06,642 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:05:06,642 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$173)
2025-11-06 15:05:06,642 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,642 - market_scanner_v2 - INFO -    - Competition: 1.456084 bars, Score: -135.59
2025-11-06 15:05:06,642 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,642 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Gaza on November 12?
2025-11-06 15:05:06,642 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:05:06,642 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$186)
2025-11-06 15:05:06,642 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,642 - market_scanner_v2 - INFO -    - Competition: 2.885517 bars, Score: -278.53
2025-11-06 15:05:06,642 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,642 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel launch a major ground offensive in Lebanon by De
2025-11-06 15:05:06,643 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:05:06,643 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$1547)
2025-11-06 15:05:06,643 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,643 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.15
2025-11-06 15:05:06,643 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,643 - market_scanner_v2 - INFO - âœ… ACCEPTED: Park Sung-jae in jail by November 30?
2025-11-06 15:05:06,643 - market_scanner_v2 - INFO -    - Category: science
2025-11-06 15:05:06,643 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$2915)
2025-11-06 15:05:06,643 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,643 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.29
2025-11-06 15:05:06,643 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,643 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Elon Musk post 160-179 tweets from October 31 to Novemb
2025-11-06 15:05:06,643 - market_scanner_v2 - INFO -    - Category: entertainment
2025-11-06 15:05:06,643 - market_scanner_v2 - INFO -    - Estimated Reward: $130 (based on volume=$92649)
2025-11-06 15:05:06,643 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,643 - market_scanner_v2 - INFO -    - Competition: 1.721481 bars, Score: -97.88
2025-11-06 15:05:06,643 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,643 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Elon Musk post 180-199 tweets from October 31 to Novemb
2025-11-06 15:05:06,643 - market_scanner_v2 - INFO -    - Category: entertainment
2025-11-06 15:05:06,643 - market_scanner_v2 - INFO -    - Estimated Reward: $30 (based on volume=$92908)
2025-11-06 15:05:06,643 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,643 - market_scanner_v2 - INFO -    - Competition: 1.8311 bars, Score: -158.82
2025-11-06 15:05:06,643 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,643 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Elon Musk post 200-219 tweets from October 31 to Novemb
2025-11-06 15:05:06,643 - market_scanner_v2 - INFO -    - Category: entertainment
2025-11-06 15:05:06,643 - market_scanner_v2 - INFO -    - Estimated Reward: $40 (based on volume=$74081)
2025-11-06 15:05:06,644 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,644 - market_scanner_v2 - INFO -    - Competition: 0.49375 bars, Score: -21.97
2025-11-06 15:05:06,644 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,644 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Elon Muskâ€™s $1T Tesla pay deal pass?
2025-11-06 15:05:06,644 - market_scanner_v2 - INFO -    - Category: entertainment
2025-11-06 15:05:06,644 - market_scanner_v2 - INFO -    - Estimated Reward: $50 (based on volume=$89521)
2025-11-06 15:05:06,644 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,644 - market_scanner_v2 - INFO -    - Competition: 1.2344 bars, Score: -89.49
2025-11-06 15:05:06,644 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,645 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Stable launch a token in 2025?
2025-11-06 15:05:06,645 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:05:06,645 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$78233)
2025-11-06 15:05:06,645 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,645 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 12.82
2025-11-06 15:05:06,645 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,646 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump establish a Gaza â€œBoard of Peaceâ€ in 2025?
2025-11-06 15:05:06,646 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:05:06,646 - market_scanner_v2 - INFO -    - Estimated Reward: $30 (based on volume=$9651)
2025-11-06 15:05:06,646 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,646 - market_scanner_v2 - INFO -    - Competition: 0.396333 bars, Score: -23.67
2025-11-06 15:05:06,646 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,646 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will the Government shutdown end November 8-11?
2025-11-06 15:05:06,646 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:05:06,646 - market_scanner_v2 - INFO -    - Estimated Reward: $200 (based on volume=$192333)
2025-11-06 15:05:06,646 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,646 - market_scanner_v2 - INFO -    - Competition: 2.448538 bars, Score: -125.62
2025-11-06 15:05:06,646 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,646 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will the Government shutdown end November 12-15?
2025-11-06 15:05:06,646 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:05:06,646 - market_scanner_v2 - INFO -    - Estimated Reward: $200 (based on volume=$106409)
2025-11-06 15:05:06,646 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,646 - market_scanner_v2 - INFO -    - Competition: 2.667073 bars, Score: -156.07
2025-11-06 15:05:06,646 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,647 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will MetaMask launch a token by September 30, 2026?
2025-11-06 15:05:06,647 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:05:06,647 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$191)
2025-11-06 15:05:06,647 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,647 - market_scanner_v2 - INFO -    - Competition: 0.769923 bars, Score: -66.97
2025-11-06 15:05:06,647 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,648 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Matt Van Epps win TN-7 Special Election?
2025-11-06 15:05:06,648 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:05:06,648 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$1695)
2025-11-06 15:05:06,648 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,648 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.17
2025-11-06 15:05:06,648 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,648 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Russia capture all of Pokrovsk by November 14?
2025-11-06 15:05:06,648 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:05:06,648 - market_scanner_v2 - INFO -    - Estimated Reward: $30 (based on volume=$13354)
2025-11-06 15:05:06,648 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,648 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 16.34
2025-11-06 15:05:06,648 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,648 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Gemini 3.0 be released by November 15?
2025-11-06 15:05:06,648 - market_scanner_v2 - INFO -    - Category: science
2025-11-06 15:05:06,648 - market_scanner_v2 - INFO -    - Estimated Reward: $200 (based on volume=$495622)
2025-11-06 15:05:06,648 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,648 - market_scanner_v2 - INFO -    - Competition: 1.3876 bars, Score: 10.80
2025-11-06 15:05:06,648 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,649 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Gemini 3.0 be released by November 22?
2025-11-06 15:05:06,649 - market_scanner_v2 - INFO -    - Category: science
2025-11-06 15:05:06,649 - market_scanner_v2 - INFO -    - Estimated Reward: $50 (based on volume=$14533)
2025-11-06 15:05:06,649 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,649 - market_scanner_v2 - INFO -    - Competition: 0.243152 bars, Score: 2.14
2025-11-06 15:05:06,649 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,649 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Russia capture Myrnohrad by November 7?
2025-11-06 15:05:06,649 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:05:06,649 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$7500)
2025-11-06 15:05:06,649 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,649 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.75
2025-11-06 15:05:06,649 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,650 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Oscar Piastri finish second in the 2025 Drivers Champio
2025-11-06 15:05:06,650 - market_scanner_v2 - INFO -    - Category: entertainment
2025-11-06 15:05:06,650 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$119)
2025-11-06 15:05:06,650 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:05:06,650 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.01
2025-11-06 15:05:06,650 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:05:06,650 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 82/2840 markets passed
2025-11-06 15:05:06,651 - market_scanner_v2 - INFO -    - 2522 rejected: reward < $10
2025-11-06 15:05:06,651 - market_scanner_v2 - INFO -    - 202 rejected: competition > 3
2025-11-06 15:05:06,651 - market_scanner_v2 - INFO -    - 31 rejected: category not in ['crypto', 'sports', 'politics', 'science', 'entertainment']
2025-11-06 15:05:06,651 - market_scanner_v2 - INFO -    - 3 rejected: volume = 0 (no liquidity)
2025-11-06 15:05:06,651 - market_scanner_v2 - INFO - ðŸ” Verifying orderbook for top 50 markets...
2025-11-06 15:05:24,064 - market_scanner_v2 - INFO - âœ… Found 82 qualifying markets (from 2840 total)
2025-11-06 15:05:24,068 - market_selector - INFO - Selected 2 markets from 82 candidates
2025-11-06 15:05:25,416 - order_manager - WARNING - âŒ Calculated prices exceed max spread (96.20% > 3.50%)
2025-11-06 15:05:25,417 - order_manager - WARNING -    This indicates orderbook is too thin or position 2-3 is too far from midpoint
2025-11-06 15:05:25,417 - order_manager - WARNING -    REJECTING market to avoid placing order at position #1 (best bid/ask)
2025-11-06 15:05:25,417 - order_manager - WARNING -    Reason: Adjusting to max spread would place order too close to best bid/ask
2025-11-06 15:05:25,417 - order_manager - WARNING -    â†’ High risk of being filled immediately!
2025-11-06 15:05:25,417 - order_manager - WARNING - Could not calculate valid prices for market 657210
2025-11-06 15:05:25,417 - __main__ - INFO - Added market 657210 to pending orders
2025-11-06 15:05:25,749 - order_manager - WARNING - âŒ Calculated prices exceed max spread (94.20% > 3.50%)
2025-11-06 15:05:25,749 - order_manager - WARNING -    This indicates orderbook is too thin or position 2-3 is too far from midpoint
2025-11-06 15:05:25,749 - order_manager - WARNING -    REJECTING market to avoid placing order at position #1 (best bid/ask)
2025-11-06 15:05:25,749 - order_manager - WARNING -    Reason: Adjusting to max spread would place order too close to best bid/ask
2025-11-06 15:05:25,749 - order_manager - WARNING -    â†’ High risk of being filled immediately!
2025-11-06 15:05:25,749 - order_manager - WARNING - Could not calculate valid prices for market 539029
2025-11-06 15:05:25,749 - __main__ - INFO - Added market 539029 to pending orders
2025-11-06 15:06:28,716 - __main__ - INFO - âœ… Using MarketScannerV2 (Playwright + Gamma API)
2025-11-06 15:06:31,663 - __main__ - INFO - ðŸ“‚ Loading config from: config.yaml
2025-11-06 15:06:31,691 - __main__ - INFO - âœ… Config loaded successfully
2025-11-06 15:06:31,691 - __main__ - INFO -    - min_reward: 10
2025-11-06 15:06:31,691 - __main__ - INFO -    - max_competition_bars: 3
2025-11-06 15:06:31,691 - __main__ - INFO -    - interval: 60s
2025-11-06 15:06:31,691 - __main__ - INFO - âœ… Telegram alerts configured (Chat ID: -1003157421030)
2025-11-06 15:06:31,691 - __main__ - INFO - âœ… Webhook alerts configured
2025-11-06 15:06:31,691 - telegram_notifier - INFO - âœ… Telegram Notifier initialized (Chat ID: -1003157421030)
2025-11-06 15:06:31,691 - __main__ - INFO - âœ… Telegram Notifier initialized
2025-11-06 15:06:31,691 - market_scanner_v2 - INFO - ðŸ“Š Market Scanner initialized with min_reward=$10, max_competition=3
2025-11-06 15:06:31,691 - market_scanner_v2 - INFO - ðŸŽ¯ Target categories: crypto, sports, politics, science, entertainment
2025-11-06 15:06:31,691 - circuit_breaker - INFO - âœ… Circuit Breaker 'playwright_scraper' initialized (threshold=3, timeout=60s)
2025-11-06 15:06:31,691 - circuit_breaker - INFO - âœ… Circuit Breaker 'playwright_scraper' initialized (threshold=3, timeout=120s)
2025-11-06 15:06:31,691 - order_manager - INFO - CLOB client initialized successfully (read-only mode)
2025-11-06 15:06:31,700 - wallet_manager - INFO - Loading REAL wallets from .env
2025-11-06 15:06:31,706 - wallet_manager - INFO - âœ… Loaded wallet 1: 0x18F261DC...Ae4FfD96
2025-11-06 15:06:31,706 - wallet_manager - INFO - âœ… Successfully loaded 1 real wallets
2025-11-06 15:06:31,722 - ml_predictor - INFO - No pre-trained model found, using new model
2025-11-06 15:06:31,722 - monitoring_system - INFO - âœ… Monitoring System initialized
2025-11-06 15:06:31,722 - __main__ - INFO - âœ… Monitoring System enabled
2025-11-06 15:06:31,722 - __main__ - INFO - â­ï¸  Reward Manager disabled in config
2025-11-06 15:06:32,452 - profit_taking_manager - INFO - âœ… CLOB client initialized with API credentials
2025-11-06 15:06:32,453 - profit_taking_manager - INFO - âœ… Profit Taking Manager initialized
2025-11-06 15:06:32,453 - profit_taking_manager - INFO -    - Min profit: 5%
2025-11-06 15:06:32,453 - profit_taking_manager - INFO -    - Target profit: 10%
2025-11-06 15:06:32,453 - profit_taking_manager - INFO -    - Max profit: 150%
2025-11-06 15:06:32,453 - profit_taking_manager - INFO -    - Check interval: 300s
2025-11-06 15:06:32,453 - __main__ - INFO - âœ… Profit Taking Manager enabled
2025-11-06 15:06:32,453 - __main__ - INFO - All modules initialized successfully
2025-11-06 15:06:32,453 - __main__ - INFO - ðŸš€ Starting Polymarket Trading Bot...
2025-11-06 15:06:33,477 - __main__ - INFO - âœ… Startup alert sent via TelegramNotifier
2025-11-06 15:06:33,478 - __main__ - INFO - ðŸ” Checking USDC approval for wallets...
2025-11-06 15:06:33,704 - usdc_approver - INFO - âœ… Connected to Polygon RPC: https://polygon-mainnet.g.alchemy.com/v2/FQJnJWsEQ...
2025-11-06 15:06:33,704 - __main__ - INFO -    Checking wallet: 0x18F261DC...Ae4FfD96
2025-11-06 15:06:34,085 - __main__ - INFO -    Raw allowance: 16000000 (base units)
2025-11-06 15:06:34,085 - __main__ - INFO -    Allowance in USDC: 16.00 USDC
2025-11-06 15:06:34,085 - __main__ - INFO -    Required minimum: 100 USDC (test mode)
2025-11-06 15:06:34,085 - __main__ - WARNING - âš ï¸  USDC approval needed!
2025-11-06 15:06:34,085 - __main__ - WARNING -    Current: 16.00 USDC
2025-11-06 15:06:34,085 - __main__ - WARNING -    Required: 100 USDC (test mode)
2025-11-06 15:06:34,086 - __main__ - WARNING -    Run: python scripts/approve_wallets.py
2025-11-06 15:06:34,086 - __main__ - WARNING -    Or the bot may fail to place orders
2025-11-06 15:06:34,086 - __main__ - WARNING - 
2025-11-06 15:06:34,086 - __main__ - WARNING -    âš ï¸  NOTE: 100 USDC is for TESTING only!
2025-11-06 15:06:34,086 - __main__ - WARNING -    For production, approve at least 1,000 USDC
2025-11-06 15:06:34,086 - __main__ - INFO - ðŸ” Starting market scanning loop
2025-11-06 15:06:34,086 - market_scanner_v2 - INFO - ðŸŒ Scraping markets from /rewards page using Playwright...
2025-11-06 15:06:34,086 - playwright_rewards_scraper - INFO - ðŸŒ Fetching markets from /rewards API...
2025-11-06 15:06:34,086 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 1 (cursor: MA==)...
2025-11-06 15:06:34,087 - __main__ - INFO - ðŸ“¦ Starting order management loop
2025-11-06 15:06:34,087 - __main__ - INFO - ðŸ‘ï¸  Starting position monitoring loop
2025-11-06 15:06:34,087 - __main__ - INFO - ðŸ›¡ï¸  Starting risk management loop
2025-11-06 15:06:34,087 - __main__ - INFO - ðŸ¤– Starting ML training loop
2025-11-06 15:06:34,087 - ml_predictor - INFO - Insufficient training data: 0 samples
2025-11-06 15:06:34,087 - __main__ - INFO - ML model updated successfully
2025-11-06 15:06:34,087 - __main__ - INFO - ðŸ“Š Starting daily optimization loop
2025-11-06 15:06:34,087 - __main__ - INFO - ðŸ¥ Starting health monitoring loop
2025-11-06 15:06:35,089 - __main__ - INFO - ðŸ“ˆ Starting hourly report loop
2025-11-06 15:06:35,090 - __main__ - INFO - ðŸ’° Starting automated profit taking loop
2025-11-06 15:06:35,090 - profit_taking_manager - INFO - ðŸ” Checking positions for wallet: 0x18F261DC...Ae4FfD96
2025-11-06 15:06:35,430 - profit_taking_manager - INFO - ðŸ“Š Found 4 active positions
2025-11-06 15:06:35,430 - profit_taking_manager - INFO - 
ðŸ“ˆ Position: Charlotte 49ers vs. East Carolina
2025-11-06 15:06:35,430 - profit_taking_manager - INFO -    Shares: 259.00 @ $0.1494
2025-11-06 15:06:35,430 - profit_taking_manager - INFO -    Current: $0.0385
2025-11-06 15:06:35,430 - profit_taking_manager - INFO -    P&L: $-28.73 (-74.23%)
2025-11-06 15:06:35,430 - profit_taking_manager - INFO -    â¸ï¸  Losing position - NOT closing (manual decision required)
2025-11-06 15:06:35,430 - profit_taking_manager - INFO - 
ðŸ“ˆ Position: Will Google Gemini 3 score at least 70% on the Fro
2025-11-06 15:06:35,430 - profit_taking_manager - INFO -    Shares: 68.00 @ $0.3900
2025-11-06 15:06:35,430 - profit_taking_manager - INFO -    Current: $0.0800
2025-11-06 15:06:35,431 - profit_taking_manager - INFO -    P&L: $-21.08 (-79.49%)
2025-11-06 15:06:35,431 - profit_taking_manager - INFO -    â¸ï¸  Losing position - NOT closing (manual decision required)
2025-11-06 15:06:35,431 - profit_taking_manager - INFO - 
ðŸ“ˆ Position: Syracuse vs. Miami
2025-11-06 15:06:35,431 - profit_taking_manager - INFO -    Shares: 66.00 @ $0.4900
2025-11-06 15:06:35,431 - profit_taking_manager - INFO -    Current: $0.0475
2025-11-06 15:06:35,431 - profit_taking_manager - INFO -    P&L: $-29.20 (-90.31%)
2025-11-06 15:06:35,431 - profit_taking_manager - INFO -    â¸ï¸  Losing position - NOT closing (manual decision required)
2025-11-06 15:06:35,431 - profit_taking_manager - INFO - 
ðŸ“ˆ Position: Will Netflix dip to $1050 in November?
2025-11-06 15:06:35,431 - profit_taking_manager - INFO -    Shares: 50.00 @ $0.3400
2025-11-06 15:06:35,431 - profit_taking_manager - INFO -    Current: $0.7700
2025-11-06 15:06:35,431 - profit_taking_manager - INFO -    P&L: $21.50 (+126.47%)
2025-11-06 15:06:35,431 - profit_taking_manager - INFO -    ðŸŽ¯ CLOSING: target_profit_reached (126.47% >= 10%)
2025-11-06 15:06:35,431 - profit_taking_manager - INFO - 
ðŸ”„ Placing SELL order for Will Netflix dip to $1050 in November?
2025-11-06 15:06:35,431 - profit_taking_manager - INFO -    Token ID: 109176985745730388398013053205590535560490868817001794547246190093921488790462
2025-11-06 15:06:35,431 - profit_taking_manager - INFO -    Shares: 50.00
2025-11-06 15:06:35,431 - profit_taking_manager - INFO -    Price: $0.7700
2025-11-06 15:06:37,571 - profit_taking_manager - ERROR - âŒ Error closing position: PolyApiException[status_code=400, error_message={'error': 'invalid signature'}]
2025-11-06 15:06:37,573 - __main__ - INFO - â³ Next profit check in 300s
2025-11-06 15:06:38,253 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 1
2025-11-06 15:06:38,253 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 2 (cursor: MTAw)...
2025-11-06 15:06:38,959 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 2
2025-11-06 15:06:38,960 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 3 (cursor: MjAw)...
2025-11-06 15:06:39,638 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 3
2025-11-06 15:06:39,639 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 4 (cursor: MzAw)...
2025-11-06 15:06:40,326 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 4
2025-11-06 15:06:40,327 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 5 (cursor: NDAw)...
2025-11-06 15:06:40,774 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 5
2025-11-06 15:06:40,775 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 6 (cursor: NTAw)...
2025-11-06 15:06:41,219 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 6
2025-11-06 15:06:41,219 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 7 (cursor: NjAw)...
2025-11-06 15:06:41,768 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 7
2025-11-06 15:06:41,769 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 8 (cursor: NzAw)...
2025-11-06 15:06:42,274 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 8
2025-11-06 15:06:42,275 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 9 (cursor: ODAw)...
2025-11-06 15:06:42,926 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 9
2025-11-06 15:06:42,926 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 10 (cursor: OTAw)...
2025-11-06 15:06:43,585 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 10
2025-11-06 15:06:43,586 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 11 (cursor: MTAwMA==)...
2025-11-06 15:06:44,240 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 11
2025-11-06 15:06:44,241 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 12 (cursor: MTEwMA==)...
2025-11-06 15:06:44,701 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 12
2025-11-06 15:06:44,702 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 13 (cursor: MTIwMA==)...
2025-11-06 15:06:45,396 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 13
2025-11-06 15:06:45,397 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 14 (cursor: MTMwMA==)...
2025-11-06 15:06:46,093 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 14
2025-11-06 15:06:46,094 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 15 (cursor: MTQwMA==)...
2025-11-06 15:06:46,775 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 15
2025-11-06 15:06:46,776 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 16 (cursor: MTUwMA==)...
2025-11-06 15:06:47,452 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 16
2025-11-06 15:06:47,453 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 17 (cursor: MTYwMA==)...
2025-11-06 15:06:48,135 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 17
2025-11-06 15:06:48,136 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 18 (cursor: MTcwMA==)...
2025-11-06 15:06:48,657 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 18
2025-11-06 15:06:48,657 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 19 (cursor: MTgwMA==)...
2025-11-06 15:06:49,303 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 19
2025-11-06 15:06:49,304 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 20 (cursor: MTkwMA==)...
2025-11-06 15:06:49,989 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 20
2025-11-06 15:06:49,990 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 21 (cursor: MjAwMA==)...
2025-11-06 15:06:50,687 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 21
2025-11-06 15:06:50,688 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 22 (cursor: MjEwMA==)...
2025-11-06 15:06:51,484 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 22
2025-11-06 15:06:51,484 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 23 (cursor: MjIwMA==)...
2025-11-06 15:06:52,158 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 23
2025-11-06 15:06:52,158 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 24 (cursor: MjMwMA==)...
2025-11-06 15:06:52,879 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 24
2025-11-06 15:06:52,880 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 25 (cursor: MjQwMA==)...
2025-11-06 15:06:53,571 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 25
2025-11-06 15:06:53,572 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 26 (cursor: MjUwMA==)...
2025-11-06 15:06:54,259 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 26
2025-11-06 15:06:54,260 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 27 (cursor: MjYwMA==)...
2025-11-06 15:06:54,963 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 27
2025-11-06 15:06:54,964 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 28 (cursor: MjcwMA==)...
2025-11-06 15:06:55,643 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 28
2025-11-06 15:06:55,643 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 29 (cursor: MjgwMA==)...
2025-11-06 15:06:56,281 - playwright_rewards_scraper - INFO - âœ… Got 41 markets on page 29
2025-11-06 15:06:56,281 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 30 (cursor: LTE=)...
2025-11-06 15:06:56,536 - playwright_rewards_scraper - INFO - âœ… No more markets on page 30
2025-11-06 15:06:56,536 - playwright_rewards_scraper - INFO - âœ… Fetched 2837 total unique markets from /rewards API
2025-11-06 15:06:56,586 - market_scanner_v2 - INFO - âœ… Got 2837 markets from /rewards page
2025-11-06 15:06:56,587 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Zohran Mamdani win by >9%?
2025-11-06 15:06:56,587 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:06:56,587 - market_scanner_v2 - INFO -    - Estimated Reward: $40 (based on volume=$19063)
2025-11-06 15:06:56,587 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,587 - market_scanner_v2 - INFO -    - Competition: 1.077278 bars, Score: -85.82
2025-11-06 15:06:56,587 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,587 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will any Google Gemini 3 model score at least 1600 on LMAren
2025-11-06 15:06:56,587 - market_scanner_v2 - INFO -    - Category: science
2025-11-06 15:06:56,587 - market_scanner_v2 - INFO -    - Estimated Reward: $50 (based on volume=$9)
2025-11-06 15:06:56,587 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,587 - market_scanner_v2 - INFO -    - Competition: 1.509968 bars, Score: -126.00
2025-11-06 15:06:56,587 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,587 - market_scanner_v2 - INFO - âœ… ACCEPTED: Trump announces new drug boat strike by November 14?
2025-11-06 15:06:56,587 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:06:56,588 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$776)
2025-11-06 15:06:56,588 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,588 - market_scanner_v2 - INFO -    - Competition: 0.91143 bars, Score: -86.07
2025-11-06 15:06:56,588 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,588 - market_scanner_v2 - INFO - âœ… ACCEPTED: Airbnb (ABNB) Up or Down on November 6?
2025-11-06 15:06:56,588 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:06:56,588 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$7056)
2025-11-06 15:06:56,588 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,588 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.71
2025-11-06 15:06:56,588 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,588 - market_scanner_v2 - INFO - âœ… ACCEPTED: Rocket Lab (RKLB) Up or Down on November 6?
2025-11-06 15:06:56,588 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:06:56,588 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$4439)
2025-11-06 15:06:56,588 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,588 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.44
2025-11-06 15:06:56,588 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,588 - market_scanner_v2 - INFO - âœ… ACCEPTED: Opendoor (OPEN) Up or Down on November 6?
2025-11-06 15:06:56,588 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:06:56,588 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$4345)
2025-11-06 15:06:56,588 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,589 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.43
2025-11-06 15:06:56,589 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,589 - market_scanner_v2 - INFO - âœ… ACCEPTED: Palantir (PLTR) Up or Down on November 6?
2025-11-06 15:06:56,589 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:06:56,589 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$3118)
2025-11-06 15:06:56,589 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,589 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.31
2025-11-06 15:06:56,589 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,589 - market_scanner_v2 - INFO - âœ… ACCEPTED: NYA (NYA) Up or Down on November 6?
2025-11-06 15:06:56,589 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:06:56,589 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$4776)
2025-11-06 15:06:56,589 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,589 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.48
2025-11-06 15:06:56,589 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,589 - market_scanner_v2 - INFO - âœ… ACCEPTED: Netflix (NFLX) Up or Down on November 6?
2025-11-06 15:06:56,589 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:06:56,589 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$1972)
2025-11-06 15:06:56,589 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,589 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.20
2025-11-06 15:06:56,589 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,589 - market_scanner_v2 - INFO - âœ… ACCEPTED: Russell 2000 (RUT) Up or Down on November 6?
2025-11-06 15:06:56,589 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:06:56,589 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2856)
2025-11-06 15:06:56,589 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,589 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.29
2025-11-06 15:06:56,589 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,590 - market_scanner_v2 - INFO - âœ… ACCEPTED: NVIDIA (NVDA) Up or Down on November 6?
2025-11-06 15:06:56,590 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:06:56,590 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2086)
2025-11-06 15:06:56,590 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,590 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.21
2025-11-06 15:06:56,590 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,590 - market_scanner_v2 - INFO - âœ… ACCEPTED: Hang Seng (HSI) Up or Down on November 6?
2025-11-06 15:06:56,590 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:06:56,590 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2965)
2025-11-06 15:06:56,590 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,590 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.30
2025-11-06 15:06:56,590 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,590 - market_scanner_v2 - INFO - âœ… ACCEPTED: Tesla (TSLA) Up or Down on November 6?
2025-11-06 15:06:56,590 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:06:56,590 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2431)
2025-11-06 15:06:56,590 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,590 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.24
2025-11-06 15:06:56,590 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,590 - market_scanner_v2 - INFO - âœ… ACCEPTED: DAX (DAX) Up or Down on November 6?
2025-11-06 15:06:56,590 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:06:56,590 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2020)
2025-11-06 15:06:56,590 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,590 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.20
2025-11-06 15:06:56,590 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,590 - market_scanner_v2 - INFO - âœ… ACCEPTED: Meta (META) Up or Down on November 6?
2025-11-06 15:06:56,590 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:06:56,590 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2728)
2025-11-06 15:06:56,591 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,591 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.27
2025-11-06 15:06:56,591 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,591 - market_scanner_v2 - INFO - âœ… ACCEPTED: FTSE 100 (UKX) Up or Down on November 6?
2025-11-06 15:06:56,591 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:06:56,591 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$4234)
2025-11-06 15:06:56,591 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,591 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.42
2025-11-06 15:06:56,591 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,591 - market_scanner_v2 - INFO - âœ… ACCEPTED: Google (GOOGL) Up or Down on November 6?
2025-11-06 15:06:56,591 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:06:56,591 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$908)
2025-11-06 15:06:56,591 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,591 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.09
2025-11-06 15:06:56,591 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,591 - market_scanner_v2 - INFO - âœ… ACCEPTED: Dow Jones (DJI) Up or Down on November 6?
2025-11-06 15:06:56,591 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:06:56,591 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$4720)
2025-11-06 15:06:56,591 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,591 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.47
2025-11-06 15:06:56,591 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,591 - market_scanner_v2 - INFO - âœ… ACCEPTED: NYMEX Crude Oil Futures (WTI) (CL=F) Up or Down on November 
2025-11-06 15:06:56,591 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:06:56,591 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$920)
2025-11-06 15:06:56,592 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,592 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.09
2025-11-06 15:06:56,592 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,592 - market_scanner_v2 - INFO - âœ… ACCEPTED: Amazon (AMZN) Up or Down on November 6?
2025-11-06 15:06:56,592 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:06:56,592 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$5350)
2025-11-06 15:06:56,592 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,592 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.53
2025-11-06 15:06:56,592 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,592 - market_scanner_v2 - INFO - âœ… ACCEPTED: Nasdaq 100 (NDX) Up or Down on November 6?
2025-11-06 15:06:56,592 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:06:56,592 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$5109)
2025-11-06 15:06:56,592 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,592 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.51
2025-11-06 15:06:56,592 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,592 - market_scanner_v2 - INFO - âœ… ACCEPTED: COMEX Silver Futures (SI=F) Up or Down on November 6?
2025-11-06 15:06:56,592 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:06:56,592 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$702)
2025-11-06 15:06:56,592 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,592 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.07
2025-11-06 15:06:56,592 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,592 - market_scanner_v2 - INFO - âœ… ACCEPTED: Microsoft (MSFT) Up or Down on November 6?
2025-11-06 15:06:56,592 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:06:56,592 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2377)
2025-11-06 15:06:56,592 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,593 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.24
2025-11-06 15:06:56,593 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,593 - market_scanner_v2 - INFO - âœ… ACCEPTED: Nikkei 225 (NIK) Up or Down on November 6?
2025-11-06 15:06:56,593 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:06:56,593 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2526)
2025-11-06 15:06:56,593 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,593 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.25
2025-11-06 15:06:56,593 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,593 - market_scanner_v2 - INFO - âœ… ACCEPTED: COMEX Gold Futures (GC=F) Up or Down on November 6?
2025-11-06 15:06:56,593 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:06:56,593 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$792)
2025-11-06 15:06:56,593 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,593 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.08
2025-11-06 15:06:56,593 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,593 - market_scanner_v2 - INFO - âœ… ACCEPTED: S&P 500 (SPX) Up or Down on November 6?
2025-11-06 15:06:56,593 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:06:56,593 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$4717)
2025-11-06 15:06:56,593 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,593 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.47
2025-11-06 15:06:56,593 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,593 - market_scanner_v2 - INFO - âœ… ACCEPTED: Apple (AAPL) Up or Down on November 6?
2025-11-06 15:06:56,593 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:06:56,593 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2700)
2025-11-06 15:06:56,593 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,593 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.27
2025-11-06 15:06:56,593 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,594 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump establish a Gaza â€œBoard of Peaceâ€ by March 31?
2025-11-06 15:06:56,594 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:06:56,594 - market_scanner_v2 - INFO -    - Estimated Reward: $40 (based on volume=$563)
2025-11-06 15:06:56,594 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,594 - market_scanner_v2 - INFO -    - Competition: 0.920455 bars, Score: -71.99
2025-11-06 15:06:56,594 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,594 - market_scanner_v2 - INFO - âœ… ACCEPTED: U.S. Closes Airspace due to Government Shutdown?
2025-11-06 15:06:56,594 - market_scanner_v2 - INFO -    - Category: science
2025-11-06 15:06:56,594 - market_scanner_v2 - INFO -    - Estimated Reward: $50 (based on volume=$12049)
2025-11-06 15:06:56,594 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,594 - market_scanner_v2 - INFO -    - Competition: 0.2222 bars, Score: 3.98
2025-11-06 15:06:56,594 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,594 - market_scanner_v2 - INFO - âœ… ACCEPTED: NYMEX Crude Oil Futures (WTI) (CL=F) Up or Down on November 
2025-11-06 15:06:56,594 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:06:56,594 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$307)
2025-11-06 15:06:56,594 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,594 - market_scanner_v2 - INFO -    - Competition: 0.225 bars, Score: -12.47
2025-11-06 15:06:56,594 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,594 - market_scanner_v2 - INFO - âœ… ACCEPTED: COMEX Silver Futures (SI=F) Up or Down on November 5?
2025-11-06 15:06:56,594 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:06:56,594 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2845)
2025-11-06 15:06:56,594 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,595 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.28
2025-11-06 15:06:56,595 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,595 - market_scanner_v2 - INFO - âœ… ACCEPTED: COMEX Gold Futures (GC=F) Up or Down on November 5?
2025-11-06 15:06:56,595 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:06:56,595 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$416)
2025-11-06 15:06:56,595 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,595 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.04
2025-11-06 15:06:56,595 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,595 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Nancy Pelosi announce her retirement by November 30?
2025-11-06 15:06:56,595 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:06:56,595 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$3188)
2025-11-06 15:06:56,595 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,595 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.32
2025-11-06 15:06:56,595 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,595 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Nancy Pelosi announce her retirement by June 30, 2026?
2025-11-06 15:06:56,595 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:06:56,595 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$5093)
2025-11-06 15:06:56,595 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,595 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.51
2025-11-06 15:06:56,595 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,595 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Asia" or "Asian" 8+ times during C5+1 Summit
2025-11-06 15:06:56,595 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:06:56,595 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$2996)
2025-11-06 15:06:56,595 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,595 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.30
2025-11-06 15:06:56,596 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,596 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Thank you" 8+ times during C5+1 Summit on No
2025-11-06 15:06:56,596 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:06:56,596 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$2347)
2025-11-06 15:06:56,596 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,596 - market_scanner_v2 - INFO -    - Competition: 1.25662 bars, Score: -120.43
2025-11-06 15:06:56,596 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,596 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Nuclear" 2+ times during C5+1 Summit on Nove
2025-11-06 15:06:56,596 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:06:56,596 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$1111)
2025-11-06 15:06:56,596 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,596 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.11
2025-11-06 15:06:56,596 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,596 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Rare Earth" or "Critical Mineral" during C5+
2025-11-06 15:06:56,596 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:06:56,596 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$1486)
2025-11-06 15:06:56,596 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,596 - market_scanner_v2 - INFO -    - Competition: 2.847725 bars, Score: -279.62
2025-11-06 15:06:56,596 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,596 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Drug" during C5+1 Summit on November 6?
2025-11-06 15:06:56,596 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:06:56,596 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$1165)
2025-11-06 15:06:56,596 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,596 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.12
2025-11-06 15:06:56,597 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,597 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Soviet" during C5+1 Summit on November 6?
2025-11-06 15:06:56,597 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:06:56,597 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$923)
2025-11-06 15:06:56,597 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,597 - market_scanner_v2 - INFO -    - Competition: 1.473458 bars, Score: -142.25
2025-11-06 15:06:56,597 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,597 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Best Equipment" during C5+1 Summit on Novemb
2025-11-06 15:06:56,597 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:06:56,597 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$163)
2025-11-06 15:06:56,597 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,597 - market_scanner_v2 - INFO -    - Competition: 0.764207 bars, Score: -71.40
2025-11-06 15:06:56,597 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,597 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Investment" during C5+1 Summit on November 6
2025-11-06 15:06:56,597 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:06:56,597 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$1056)
2025-11-06 15:06:56,597 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,597 - market_scanner_v2 - INFO -    - Competition: 0.829607 bars, Score: -77.86
2025-11-06 15:06:56,597 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,597 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Middle East" during C5+1 Summit on November 
2025-11-06 15:06:56,597 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:06:56,597 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$235)
2025-11-06 15:06:56,597 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,597 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.02
2025-11-06 15:06:56,597 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,597 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Azerbaijan" during C5+1 Summit on November 6
2025-11-06 15:06:56,598 - market_scanner_v2 - INFO -    - Category: science
2025-11-06 15:06:56,598 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$3218)
2025-11-06 15:06:56,598 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,598 - market_scanner_v2 - INFO -    - Competition: 0.0164 bars, Score: 3.68
2025-11-06 15:06:56,598 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,598 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Afghanistan" during C5+1 Summit on November 
2025-11-06 15:06:56,598 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:06:56,598 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$335)
2025-11-06 15:06:56,598 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,598 - market_scanner_v2 - INFO -    - Competition: 0.771046 bars, Score: -72.07
2025-11-06 15:06:56,598 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,598 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Eight wars" during C5+1 Summit on November 6
2025-11-06 15:06:56,598 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:06:56,598 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$1260)
2025-11-06 15:06:56,598 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,598 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.13
2025-11-06 15:06:56,598 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,598 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Dead Country" during C5+1 Summit on November
2025-11-06 15:06:56,598 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:06:56,598 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$1372)
2025-11-06 15:06:56,598 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,598 - market_scanner_v2 - INFO -    - Competition: 0.444993 bars, Score: -39.36
2025-11-06 15:06:56,598 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,599 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trumpâ€™s approval rating be less than 42.5 on November 7
2025-11-06 15:06:56,599 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:06:56,599 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$1937)
2025-11-06 15:06:56,599 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,599 - market_scanner_v2 - INFO -    - Competition: 0.988 bars, Score: -93.61
2025-11-06 15:06:56,600 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,600 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike 1 country in November 2025?
2025-11-06 15:06:56,600 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:06:56,600 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$2000)
2025-11-06 15:06:56,600 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,600 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.20
2025-11-06 15:06:56,600 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,600 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike 2 countries in November 2025?
2025-11-06 15:06:56,600 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:06:56,600 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$205)
2025-11-06 15:06:56,600 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,600 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.02
2025-11-06 15:06:56,600 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,600 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Netflix reach $1155 in November?
2025-11-06 15:06:56,600 - market_scanner_v2 - INFO -    - Category: entertainment
2025-11-06 15:06:56,600 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$118)
2025-11-06 15:06:56,600 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,600 - market_scanner_v2 - INFO -    - Competition: 1.243298 bars, Score: -114.32
2025-11-06 15:06:56,600 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,600 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Netflix dip to $1050 in November?
2025-11-06 15:06:56,600 - market_scanner_v2 - INFO -    - Category: entertainment
2025-11-06 15:06:56,601 - market_scanner_v2 - INFO -    - Estimated Reward: $30 (based on volume=$165)
2025-11-06 15:06:56,601 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,601 - market_scanner_v2 - INFO -    - Competition: 0.027444 bars, Score: 12.27
2025-11-06 15:06:56,601 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,601 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Lebanon on November 7?
2025-11-06 15:06:56,601 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:06:56,601 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$1850)
2025-11-06 15:06:56,601 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,601 - market_scanner_v2 - INFO -    - Competition: 0.98695 bars, Score: -88.51
2025-11-06 15:06:56,601 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,601 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Lebanon on November 8?
2025-11-06 15:06:56,601 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:06:56,601 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$365)
2025-11-06 15:06:56,601 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,601 - market_scanner_v2 - INFO -    - Competition: 1.333333 bars, Score: -123.30
2025-11-06 15:06:56,602 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,602 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Lebanon on November 9?
2025-11-06 15:06:56,602 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:06:56,602 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$282)
2025-11-06 15:06:56,602 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,602 - market_scanner_v2 - INFO -    - Competition: 1.532958 bars, Score: -143.27
2025-11-06 15:06:56,602 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,602 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Lebanon on November 11?
2025-11-06 15:06:56,602 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:06:56,602 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$820)
2025-11-06 15:06:56,602 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,602 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.08
2025-11-06 15:06:56,602 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,602 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Lebanon on November 12?
2025-11-06 15:06:56,602 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:06:56,602 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$94)
2025-11-06 15:06:56,602 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,602 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-06 15:06:56,602 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,602 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Lebanon on November 13?
2025-11-06 15:06:56,602 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:06:56,602 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$20)
2025-11-06 15:06:56,602 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,602 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.00
2025-11-06 15:06:56,602 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,603 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Lebanon on November 14?
2025-11-06 15:06:56,603 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:06:56,603 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$486)
2025-11-06 15:06:56,603 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,603 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.05
2025-11-06 15:06:56,603 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,603 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Gaza on November 7?
2025-11-06 15:06:56,603 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:06:56,603 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$458)
2025-11-06 15:06:56,603 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,603 - market_scanner_v2 - INFO -    - Competition: 1.2366 bars, Score: -113.61
2025-11-06 15:06:56,603 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,603 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Gaza on November 8?
2025-11-06 15:06:56,603 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:06:56,603 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$143)
2025-11-06 15:06:56,603 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,603 - market_scanner_v2 - INFO -    - Competition: 0.959392 bars, Score: -85.92
2025-11-06 15:06:56,603 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,603 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Gaza on November 9?
2025-11-06 15:06:56,603 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:06:56,603 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$264)
2025-11-06 15:06:56,603 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,603 - market_scanner_v2 - INFO -    - Competition: 0.005125 bars, Score: 9.51
2025-11-06 15:06:56,603 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,603 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Gaza on November 11?
2025-11-06 15:06:56,604 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:06:56,604 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$173)
2025-11-06 15:06:56,604 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,604 - market_scanner_v2 - INFO -    - Competition: 1.456084 bars, Score: -135.59
2025-11-06 15:06:56,604 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,604 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Gaza on November 12?
2025-11-06 15:06:56,604 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:06:56,604 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$186)
2025-11-06 15:06:56,604 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,604 - market_scanner_v2 - INFO -    - Competition: 2.885517 bars, Score: -278.53
2025-11-06 15:06:56,604 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,604 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel launch a major ground offensive in Lebanon by De
2025-11-06 15:06:56,604 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:06:56,604 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$1547)
2025-11-06 15:06:56,604 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,604 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.15
2025-11-06 15:06:56,604 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,604 - market_scanner_v2 - INFO - âœ… ACCEPTED: Park Sung-jae in jail by November 30?
2025-11-06 15:06:56,604 - market_scanner_v2 - INFO -    - Category: science
2025-11-06 15:06:56,604 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$2915)
2025-11-06 15:06:56,604 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,604 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.29
2025-11-06 15:06:56,605 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,605 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Elon Musk post 160-179 tweets from October 31 to Novemb
2025-11-06 15:06:56,605 - market_scanner_v2 - INFO -    - Category: entertainment
2025-11-06 15:06:56,605 - market_scanner_v2 - INFO -    - Estimated Reward: $130 (based on volume=$92649)
2025-11-06 15:06:56,605 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,605 - market_scanner_v2 - INFO -    - Competition: 1.315445 bars, Score: -57.28
2025-11-06 15:06:56,605 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,605 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Elon Musk post 180-199 tweets from October 31 to Novemb
2025-11-06 15:06:56,605 - market_scanner_v2 - INFO -    - Category: entertainment
2025-11-06 15:06:56,605 - market_scanner_v2 - INFO -    - Estimated Reward: $30 (based on volume=$92908)
2025-11-06 15:06:56,605 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,605 - market_scanner_v2 - INFO -    - Competition: 0.658333 bars, Score: -41.54
2025-11-06 15:06:56,605 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,605 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Elon Musk post 200-219 tweets from October 31 to Novemb
2025-11-06 15:06:56,605 - market_scanner_v2 - INFO -    - Category: entertainment
2025-11-06 15:06:56,605 - market_scanner_v2 - INFO -    - Estimated Reward: $40 (based on volume=$74081)
2025-11-06 15:06:56,605 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,605 - market_scanner_v2 - INFO -    - Competition: 0.49375 bars, Score: -21.97
2025-11-06 15:06:56,605 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,605 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Elon Muskâ€™s $1T Tesla pay deal pass?
2025-11-06 15:06:56,605 - market_scanner_v2 - INFO -    - Category: entertainment
2025-11-06 15:06:56,606 - market_scanner_v2 - INFO -    - Estimated Reward: $50 (based on volume=$89521)
2025-11-06 15:06:56,606 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,606 - market_scanner_v2 - INFO -    - Competition: 1.2344 bars, Score: -89.49
2025-11-06 15:06:56,606 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,606 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Stable launch a token in 2025?
2025-11-06 15:06:56,606 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:06:56,606 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$78233)
2025-11-06 15:06:56,606 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,606 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 12.82
2025-11-06 15:06:56,606 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,607 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump establish a Gaza â€œBoard of Peaceâ€ in 2025?
2025-11-06 15:06:56,607 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:06:56,607 - market_scanner_v2 - INFO -    - Estimated Reward: $30 (based on volume=$9651)
2025-11-06 15:06:56,608 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,608 - market_scanner_v2 - INFO -    - Competition: 0.396333 bars, Score: -23.67
2025-11-06 15:06:56,608 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,608 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will the Government shutdown end November 8-11?
2025-11-06 15:06:56,608 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:06:56,608 - market_scanner_v2 - INFO -    - Estimated Reward: $200 (based on volume=$192333)
2025-11-06 15:06:56,608 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,608 - market_scanner_v2 - INFO -    - Competition: 1.353272 bars, Score: -16.09
2025-11-06 15:06:56,608 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,608 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will the Government shutdown end November 12-15?
2025-11-06 15:06:56,608 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:06:56,608 - market_scanner_v2 - INFO -    - Estimated Reward: $200 (based on volume=$106409)
2025-11-06 15:06:56,608 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,608 - market_scanner_v2 - INFO -    - Competition: 1.442593 bars, Score: -33.62
2025-11-06 15:06:56,608 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,609 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will MetaMask launch a token by September 30, 2026?
2025-11-06 15:06:56,609 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:06:56,609 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$191)
2025-11-06 15:06:56,609 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,609 - market_scanner_v2 - INFO -    - Competition: 0.769923 bars, Score: -66.97
2025-11-06 15:06:56,609 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,609 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Matt Van Epps win TN-7 Special Election?
2025-11-06 15:06:56,609 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:06:56,609 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$1695)
2025-11-06 15:06:56,610 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,610 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.17
2025-11-06 15:06:56,610 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,610 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Russia capture all of Pokrovsk by November 14?
2025-11-06 15:06:56,610 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:06:56,610 - market_scanner_v2 - INFO -    - Estimated Reward: $30 (based on volume=$13354)
2025-11-06 15:06:56,610 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,610 - market_scanner_v2 - INFO -    - Competition: 0.272272 bars, Score: -10.89
2025-11-06 15:06:56,610 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,610 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Russia capture Siversk by December 31?
2025-11-06 15:06:56,610 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:06:56,610 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$3536)
2025-11-06 15:06:56,610 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,610 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.35
2025-11-06 15:06:56,610 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,610 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Gemini 3.0 be released by November 15?
2025-11-06 15:06:56,610 - market_scanner_v2 - INFO -    - Category: science
2025-11-06 15:06:56,610 - market_scanner_v2 - INFO -    - Estimated Reward: $200 (based on volume=$495622)
2025-11-06 15:06:56,611 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,611 - market_scanner_v2 - INFO -    - Competition: 1.3876 bars, Score: 10.80
2025-11-06 15:06:56,611 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,611 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Gemini 3.0 be released by November 22?
2025-11-06 15:06:56,611 - market_scanner_v2 - INFO -    - Category: science
2025-11-06 15:06:56,611 - market_scanner_v2 - INFO -    - Estimated Reward: $50 (based on volume=$14533)
2025-11-06 15:06:56,611 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,611 - market_scanner_v2 - INFO -    - Competition: 0.243152 bars, Score: 2.14
2025-11-06 15:06:56,611 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,611 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Russia capture Myrnohrad by November 7?
2025-11-06 15:06:56,611 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:06:56,611 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$7500)
2025-11-06 15:06:56,611 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,611 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.75
2025-11-06 15:06:56,611 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,612 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Oscar Piastri finish second in the 2025 Drivers Champio
2025-11-06 15:06:56,612 - market_scanner_v2 - INFO -    - Category: entertainment
2025-11-06 15:06:56,612 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$119)
2025-11-06 15:06:56,612 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,612 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.01
2025-11-06 15:06:56,612 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,612 - market_scanner_v2 - INFO - âœ… ACCEPTED: TikTok sale announced in 2025?
2025-11-06 15:06:56,612 - market_scanner_v2 - INFO -    - Category: entertainment
2025-11-06 15:06:56,612 - market_scanner_v2 - INFO -    - Estimated Reward: $30 (based on volume=$6818)
2025-11-06 15:06:56,612 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:06:56,613 - market_scanner_v2 - INFO -    - Competition: 1.080166 bars, Score: -92.33
2025-11-06 15:06:56,613 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:06:56,613 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 83/2837 markets passed
2025-11-06 15:06:56,613 - market_scanner_v2 - INFO -    - 2519 rejected: reward < $10
2025-11-06 15:06:56,613 - market_scanner_v2 - INFO -    - 201 rejected: competition > 3
2025-11-06 15:06:56,613 - market_scanner_v2 - INFO -    - 31 rejected: category not in ['crypto', 'sports', 'politics', 'science', 'entertainment']
2025-11-06 15:06:56,613 - market_scanner_v2 - INFO -    - 3 rejected: volume = 0 (no liquidity)
2025-11-06 15:06:56,613 - market_scanner_v2 - INFO - ðŸ” Verifying orderbook for top 50 markets...
2025-11-06 15:07:13,963 - market_scanner_v2 - INFO - âœ… Found 83 qualifying markets (from 2837 total)
2025-11-06 15:07:13,967 - market_selector - INFO - Selected 2 markets from 83 candidates
2025-11-06 15:07:16,426 - order_manager - WARNING - âŒ Calculated prices exceed max spread (96.20% > 3.50%)
2025-11-06 15:07:16,427 - order_manager - WARNING -    This indicates orderbook is too thin or position 2-3 is too far from midpoint
2025-11-06 15:07:16,427 - order_manager - WARNING -    REJECTING market to avoid placing order at position #1 (best bid/ask)
2025-11-06 15:07:16,427 - order_manager - WARNING -    Reason: Adjusting to max spread would place order too close to best bid/ask
2025-11-06 15:07:16,427 - order_manager - WARNING -    â†’ High risk of being filled immediately!
2025-11-06 15:07:16,427 - order_manager - WARNING - Could not calculate valid prices for market 657210
2025-11-06 15:07:16,427 - __main__ - WARNING - âš ï¸  Skipped market 657210 - could not prepare valid order (spread too high or orderbook too thin)
2025-11-06 15:07:16,766 - order_manager - WARNING - âŒ Calculated prices exceed max spread (94.20% > 3.50%)
2025-11-06 15:07:16,766 - order_manager - WARNING -    This indicates orderbook is too thin or position 2-3 is too far from midpoint
2025-11-06 15:07:16,766 - order_manager - WARNING -    REJECTING market to avoid placing order at position #1 (best bid/ask)
2025-11-06 15:07:16,766 - order_manager - WARNING -    Reason: Adjusting to max spread would place order too close to best bid/ask
2025-11-06 15:07:16,766 - order_manager - WARNING -    â†’ High risk of being filled immediately!
2025-11-06 15:07:16,766 - order_manager - WARNING - Could not calculate valid prices for market 539029
2025-11-06 15:07:16,766 - __main__ - WARNING - âš ï¸  Skipped market 539029 - could not prepare valid order (spread too high or orderbook too thin)
2025-11-06 15:08:12,949 - market_scanner_v2 - INFO - ðŸŒ Scraping markets from /rewards page using Playwright...
2025-11-06 15:08:12,950 - playwright_rewards_scraper - INFO - ðŸŒ Fetching markets from /rewards API...
2025-11-06 15:08:12,950 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 1 (cursor: MA==)...
2025-11-06 15:08:13,612 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 1
2025-11-06 15:08:13,613 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 2 (cursor: MTAw)...
2025-11-06 15:08:14,315 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 2
2025-11-06 15:08:14,316 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 3 (cursor: MjAw)...
2025-11-06 15:08:15,017 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 3
2025-11-06 15:08:15,018 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 4 (cursor: MzAw)...
2025-11-06 15:08:15,498 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 4
2025-11-06 15:08:15,498 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 5 (cursor: NDAw)...
2025-11-06 15:08:16,985 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 5
2025-11-06 15:08:16,985 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 6 (cursor: NTAw)...
2025-11-06 15:08:17,647 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 6
2025-11-06 15:08:17,648 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 7 (cursor: NjAw)...
2025-11-06 15:08:18,036 - ml_predictor - INFO - Alert sent: ðŸš¨ <b>MONITORING ALERT</b>

ðŸ”´ KhÃ´ng quÃ©t markets trong 62s!
2025-11-06 15:08:18,036 - monitoring_system - INFO - Alert sent: no_scan
2025-11-06 15:08:18,036 - __main__ - WARNING - âš ï¸ Health check failed: 2 issues
2025-11-06 15:08:18,036 - __main__ - WARNING -    - ðŸ”´ KhÃ´ng quÃ©t markets trong 62s!
2025-11-06 15:08:18,036 - __main__ - WARNING -    - âš ï¸ API cháº­m: 42.7s trung bÃ¬nh
2025-11-06 15:08:18,122 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 7
2025-11-06 15:08:18,122 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 8 (cursor: NzAw)...
2025-11-06 15:08:18,780 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 8
2025-11-06 15:08:18,780 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 9 (cursor: ODAw)...
2025-11-06 15:08:19,425 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 9
2025-11-06 15:08:19,426 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 10 (cursor: OTAw)...
2025-11-06 15:08:20,072 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 10
2025-11-06 15:08:20,073 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 11 (cursor: MTAwMA==)...
2025-11-06 15:08:20,770 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 11
2025-11-06 15:08:20,771 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 12 (cursor: MTEwMA==)...
2025-11-06 15:08:21,434 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 12
2025-11-06 15:08:21,435 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 13 (cursor: MTIwMA==)...
2025-11-06 15:08:22,084 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 13
2025-11-06 15:08:22,084 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 14 (cursor: MTMwMA==)...
2025-11-06 15:08:22,534 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 14
2025-11-06 15:08:22,534 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 15 (cursor: MTQwMA==)...
2025-11-06 15:08:22,973 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 15
2025-11-06 15:08:22,974 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 16 (cursor: MTUwMA==)...
2025-11-06 15:08:23,452 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 16
2025-11-06 15:08:23,453 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 17 (cursor: MTYwMA==)...
2025-11-06 15:08:24,245 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 17
2025-11-06 15:08:24,246 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 18 (cursor: MTcwMA==)...
2025-11-06 15:08:24,695 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 18
2025-11-06 15:08:24,695 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 19 (cursor: MTgwMA==)...
2025-11-06 15:08:25,127 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 19
2025-11-06 15:08:25,128 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 20 (cursor: MTkwMA==)...
2025-11-06 15:08:25,785 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 20
2025-11-06 15:08:25,786 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 21 (cursor: MjAwMA==)...
2025-11-06 15:08:26,441 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 21
2025-11-06 15:08:26,442 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 22 (cursor: MjEwMA==)...
2025-11-06 15:08:26,869 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 22
2025-11-06 15:08:26,870 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 23 (cursor: MjIwMA==)...
2025-11-06 15:08:27,540 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 23
2025-11-06 15:08:27,541 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 24 (cursor: MjMwMA==)...
2025-11-06 15:08:28,202 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 24
2025-11-06 15:08:28,202 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 25 (cursor: MjQwMA==)...
2025-11-06 15:08:28,944 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 25
2025-11-06 15:08:28,944 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 26 (cursor: MjUwMA==)...
2025-11-06 15:08:29,584 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 26
2025-11-06 15:08:29,584 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 27 (cursor: MjYwMA==)...
2025-11-06 15:08:30,227 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 27
2025-11-06 15:08:30,227 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 28 (cursor: MjcwMA==)...
2025-11-06 15:08:30,899 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 28
2025-11-06 15:08:30,900 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 29 (cursor: MjgwMA==)...
2025-11-06 15:08:31,320 - playwright_rewards_scraper - INFO - âœ… Got 40 markets on page 29
2025-11-06 15:08:31,321 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 30 (cursor: LTE=)...
2025-11-06 15:08:31,578 - playwright_rewards_scraper - INFO - âœ… No more markets on page 30
2025-11-06 15:08:31,579 - playwright_rewards_scraper - INFO - âœ… Fetched 2836 total unique markets from /rewards API
2025-11-06 15:08:31,629 - market_scanner_v2 - INFO - âœ… Got 2836 markets from /rewards page
2025-11-06 15:08:31,629 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Zohran Mamdani win by >9%?
2025-11-06 15:08:31,629 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:08:31,629 - market_scanner_v2 - INFO -    - Estimated Reward: $40 (based on volume=$19063)
2025-11-06 15:08:31,629 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,629 - market_scanner_v2 - INFO -    - Competition: 0.144083 bars, Score: 7.50
2025-11-06 15:08:31,629 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,630 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will any Google Gemini 3 model score at least 1600 on LMAren
2025-11-06 15:08:31,630 - market_scanner_v2 - INFO -    - Category: science
2025-11-06 15:08:31,630 - market_scanner_v2 - INFO -    - Estimated Reward: $50 (based on volume=$9)
2025-11-06 15:08:31,630 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,630 - market_scanner_v2 - INFO -    - Competition: 1.352048 bars, Score: -110.20
2025-11-06 15:08:31,630 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,630 - market_scanner_v2 - INFO - âœ… ACCEPTED: Airbnb (ABNB) Up or Down on November 6?
2025-11-06 15:08:31,630 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:08:31,630 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$7056)
2025-11-06 15:08:31,630 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,630 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.71
2025-11-06 15:08:31,630 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,630 - market_scanner_v2 - INFO - âœ… ACCEPTED: Rocket Lab (RKLB) Up or Down on November 6?
2025-11-06 15:08:31,630 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:08:31,630 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$4439)
2025-11-06 15:08:31,630 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,630 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.44
2025-11-06 15:08:31,630 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,630 - market_scanner_v2 - INFO - âœ… ACCEPTED: Opendoor (OPEN) Up or Down on November 6?
2025-11-06 15:08:31,630 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:08:31,631 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$4345)
2025-11-06 15:08:31,631 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,631 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.43
2025-11-06 15:08:31,631 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,631 - market_scanner_v2 - INFO - âœ… ACCEPTED: Palantir (PLTR) Up or Down on November 6?
2025-11-06 15:08:31,631 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:08:31,631 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$3118)
2025-11-06 15:08:31,631 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,631 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.31
2025-11-06 15:08:31,631 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,631 - market_scanner_v2 - INFO - âœ… ACCEPTED: NYA (NYA) Up or Down on November 6?
2025-11-06 15:08:31,631 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:08:31,631 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$4776)
2025-11-06 15:08:31,631 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,631 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.48
2025-11-06 15:08:31,631 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,631 - market_scanner_v2 - INFO - âœ… ACCEPTED: Netflix (NFLX) Up or Down on November 6?
2025-11-06 15:08:31,631 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:08:31,631 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$1972)
2025-11-06 15:08:31,631 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,631 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.20
2025-11-06 15:08:31,631 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,631 - market_scanner_v2 - INFO - âœ… ACCEPTED: Russell 2000 (RUT) Up or Down on November 6?
2025-11-06 15:08:31,631 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:08:31,631 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2856)
2025-11-06 15:08:31,631 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,632 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.29
2025-11-06 15:08:31,632 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,632 - market_scanner_v2 - INFO - âœ… ACCEPTED: NVIDIA (NVDA) Up or Down on November 6?
2025-11-06 15:08:31,632 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:08:31,632 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2086)
2025-11-06 15:08:31,632 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,632 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.21
2025-11-06 15:08:31,632 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,632 - market_scanner_v2 - INFO - âœ… ACCEPTED: Hang Seng (HSI) Up or Down on November 6?
2025-11-06 15:08:31,632 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:08:31,632 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2965)
2025-11-06 15:08:31,632 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,632 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.30
2025-11-06 15:08:31,632 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,632 - market_scanner_v2 - INFO - âœ… ACCEPTED: Tesla (TSLA) Up or Down on November 6?
2025-11-06 15:08:31,632 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:08:31,632 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2431)
2025-11-06 15:08:31,632 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,632 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.24
2025-11-06 15:08:31,632 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,632 - market_scanner_v2 - INFO - âœ… ACCEPTED: DAX (DAX) Up or Down on November 6?
2025-11-06 15:08:31,632 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:08:31,632 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2020)
2025-11-06 15:08:31,632 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,632 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.20
2025-11-06 15:08:31,633 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,633 - market_scanner_v2 - INFO - âœ… ACCEPTED: Meta (META) Up or Down on November 6?
2025-11-06 15:08:31,633 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:08:31,633 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2728)
2025-11-06 15:08:31,633 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,633 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.27
2025-11-06 15:08:31,633 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,633 - market_scanner_v2 - INFO - âœ… ACCEPTED: FTSE 100 (UKX) Up or Down on November 6?
2025-11-06 15:08:31,633 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:08:31,633 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$4234)
2025-11-06 15:08:31,633 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,633 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.42
2025-11-06 15:08:31,633 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,633 - market_scanner_v2 - INFO - âœ… ACCEPTED: Google (GOOGL) Up or Down on November 6?
2025-11-06 15:08:31,633 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:08:31,633 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$908)
2025-11-06 15:08:31,633 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,633 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.09
2025-11-06 15:08:31,633 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,633 - market_scanner_v2 - INFO - âœ… ACCEPTED: Dow Jones (DJI) Up or Down on November 6?
2025-11-06 15:08:31,633 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:08:31,633 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$4720)
2025-11-06 15:08:31,633 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,633 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.47
2025-11-06 15:08:31,633 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,633 - market_scanner_v2 - INFO - âœ… ACCEPTED: NYMEX Crude Oil Futures (WTI) (CL=F) Up or Down on November 
2025-11-06 15:08:31,634 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:08:31,634 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$920)
2025-11-06 15:08:31,634 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,634 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.09
2025-11-06 15:08:31,634 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,634 - market_scanner_v2 - INFO - âœ… ACCEPTED: Amazon (AMZN) Up or Down on November 6?
2025-11-06 15:08:31,634 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:08:31,634 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$5350)
2025-11-06 15:08:31,634 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,634 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.53
2025-11-06 15:08:31,634 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,634 - market_scanner_v2 - INFO - âœ… ACCEPTED: Nasdaq 100 (NDX) Up or Down on November 6?
2025-11-06 15:08:31,634 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:08:31,634 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$5109)
2025-11-06 15:08:31,634 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,634 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.51
2025-11-06 15:08:31,634 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,634 - market_scanner_v2 - INFO - âœ… ACCEPTED: COMEX Silver Futures (SI=F) Up or Down on November 6?
2025-11-06 15:08:31,634 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:08:31,634 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$702)
2025-11-06 15:08:31,634 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,634 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.07
2025-11-06 15:08:31,634 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,634 - market_scanner_v2 - INFO - âœ… ACCEPTED: Microsoft (MSFT) Up or Down on November 6?
2025-11-06 15:08:31,634 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:08:31,634 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2377)
2025-11-06 15:08:31,634 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,634 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.24
2025-11-06 15:08:31,634 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,635 - market_scanner_v2 - INFO - âœ… ACCEPTED: Nikkei 225 (NIK) Up or Down on November 6?
2025-11-06 15:08:31,635 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:08:31,635 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2526)
2025-11-06 15:08:31,635 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,635 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.25
2025-11-06 15:08:31,635 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,635 - market_scanner_v2 - INFO - âœ… ACCEPTED: COMEX Gold Futures (GC=F) Up or Down on November 6?
2025-11-06 15:08:31,635 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:08:31,635 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$792)
2025-11-06 15:08:31,635 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,635 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.08
2025-11-06 15:08:31,635 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,635 - market_scanner_v2 - INFO - âœ… ACCEPTED: S&P 500 (SPX) Up or Down on November 6?
2025-11-06 15:08:31,635 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:08:31,635 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$4717)
2025-11-06 15:08:31,635 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,635 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.47
2025-11-06 15:08:31,635 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,635 - market_scanner_v2 - INFO - âœ… ACCEPTED: Apple (AAPL) Up or Down on November 6?
2025-11-06 15:08:31,635 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:08:31,635 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2700)
2025-11-06 15:08:31,635 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,635 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.27
2025-11-06 15:08:31,635 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,635 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump establish a Gaza â€œBoard of Peaceâ€ by March 31?
2025-11-06 15:08:31,635 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:08:31,636 - market_scanner_v2 - INFO -    - Estimated Reward: $40 (based on volume=$563)
2025-11-06 15:08:31,636 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,636 - market_scanner_v2 - INFO -    - Competition: 0.836505 bars, Score: -63.59
2025-11-06 15:08:31,636 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,636 - market_scanner_v2 - INFO - âœ… ACCEPTED: U.S. Closes Airspace due to Government Shutdown?
2025-11-06 15:08:31,636 - market_scanner_v2 - INFO -    - Category: science
2025-11-06 15:08:31,636 - market_scanner_v2 - INFO -    - Estimated Reward: $50 (based on volume=$12049)
2025-11-06 15:08:31,636 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,636 - market_scanner_v2 - INFO -    - Competition: 0.082267 bars, Score: 17.98
2025-11-06 15:08:31,636 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,636 - market_scanner_v2 - INFO - âœ… ACCEPTED: NYMEX Crude Oil Futures (WTI) (CL=F) Up or Down on November 
2025-11-06 15:08:31,636 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:08:31,636 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$307)
2025-11-06 15:08:31,636 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,636 - market_scanner_v2 - INFO -    - Competition: 0.225 bars, Score: -12.47
2025-11-06 15:08:31,636 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,636 - market_scanner_v2 - INFO - âœ… ACCEPTED: COMEX Silver Futures (SI=F) Up or Down on November 5?
2025-11-06 15:08:31,636 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:08:31,636 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$2845)
2025-11-06 15:08:31,636 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,636 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.28
2025-11-06 15:08:31,636 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,636 - market_scanner_v2 - INFO - âœ… ACCEPTED: COMEX Gold Futures (GC=F) Up or Down on November 5?
2025-11-06 15:08:31,637 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:08:31,637 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$416)
2025-11-06 15:08:31,637 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,637 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.04
2025-11-06 15:08:31,637 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,637 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Nancy Pelosi announce her retirement by November 30?
2025-11-06 15:08:31,637 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:08:31,637 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$3188)
2025-11-06 15:08:31,637 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,637 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.32
2025-11-06 15:08:31,637 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,637 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Nancy Pelosi announce her retirement by June 30, 2026?
2025-11-06 15:08:31,637 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:08:31,637 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$5093)
2025-11-06 15:08:31,637 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,637 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.51
2025-11-06 15:08:31,637 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,637 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Asia" or "Asian" 8+ times during C5+1 Summit
2025-11-06 15:08:31,637 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:08:31,637 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$2996)
2025-11-06 15:08:31,637 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,637 - market_scanner_v2 - INFO -    - Competition: 0.998247 bars, Score: -94.53
2025-11-06 15:08:31,637 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,637 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Thank you" 8+ times during C5+1 Summit on No
2025-11-06 15:08:31,637 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:08:31,638 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$2347)
2025-11-06 15:08:31,638 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,638 - market_scanner_v2 - INFO -    - Competition: 1.25662 bars, Score: -120.43
2025-11-06 15:08:31,638 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,638 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Nuclear" 2+ times during C5+1 Summit on Nove
2025-11-06 15:08:31,638 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:08:31,638 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$1111)
2025-11-06 15:08:31,638 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,638 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.11
2025-11-06 15:08:31,638 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,638 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Rare Earth" or "Critical Mineral" during C5+
2025-11-06 15:08:31,638 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:08:31,638 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$1486)
2025-11-06 15:08:31,638 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,638 - market_scanner_v2 - INFO -    - Competition: 2.847725 bars, Score: -279.62
2025-11-06 15:08:31,638 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,638 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Drug" during C5+1 Summit on November 6?
2025-11-06 15:08:31,638 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:08:31,638 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$1165)
2025-11-06 15:08:31,638 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,638 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.12
2025-11-06 15:08:31,638 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,638 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Soviet" during C5+1 Summit on November 6?
2025-11-06 15:08:31,639 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:08:31,639 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$923)
2025-11-06 15:08:31,639 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,639 - market_scanner_v2 - INFO -    - Competition: 1.473458 bars, Score: -142.25
2025-11-06 15:08:31,639 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,639 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Best Equipment" during C5+1 Summit on Novemb
2025-11-06 15:08:31,639 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:08:31,639 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$163)
2025-11-06 15:08:31,639 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,639 - market_scanner_v2 - INFO -    - Competition: 0.764207 bars, Score: -71.40
2025-11-06 15:08:31,639 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,639 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Investment" during C5+1 Summit on November 6
2025-11-06 15:08:31,639 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:08:31,639 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$1056)
2025-11-06 15:08:31,639 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,639 - market_scanner_v2 - INFO -    - Competition: 0.829607 bars, Score: -77.86
2025-11-06 15:08:31,639 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,639 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Middle East" during C5+1 Summit on November 
2025-11-06 15:08:31,639 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:08:31,639 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$235)
2025-11-06 15:08:31,639 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,639 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.02
2025-11-06 15:08:31,639 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,640 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Azerbaijan" during C5+1 Summit on November 6
2025-11-06 15:08:31,640 - market_scanner_v2 - INFO -    - Category: science
2025-11-06 15:08:31,640 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$3218)
2025-11-06 15:08:31,640 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,640 - market_scanner_v2 - INFO -    - Competition: 0.092583 bars, Score: -3.94
2025-11-06 15:08:31,640 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,640 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Afghanistan" during C5+1 Summit on November 
2025-11-06 15:08:31,640 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:08:31,640 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$335)
2025-11-06 15:08:31,640 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,640 - market_scanner_v2 - INFO -    - Competition: 0.771046 bars, Score: -72.07
2025-11-06 15:08:31,640 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,640 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Eight wars" during C5+1 Summit on November 6
2025-11-06 15:08:31,640 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:08:31,640 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$1260)
2025-11-06 15:08:31,640 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,640 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.13
2025-11-06 15:08:31,640 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,640 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump say "Dead Country" during C5+1 Summit on November
2025-11-06 15:08:31,640 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:08:31,640 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$1372)
2025-11-06 15:08:31,640 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,640 - market_scanner_v2 - INFO -    - Competition: 0.444993 bars, Score: -39.36
2025-11-06 15:08:31,640 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,641 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trumpâ€™s approval rating be less than 42.5 on November 7
2025-11-06 15:08:31,641 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:08:31,642 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$1937)
2025-11-06 15:08:31,642 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,642 - market_scanner_v2 - INFO -    - Competition: 0.988 bars, Score: -93.61
2025-11-06 15:08:31,642 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,642 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike 1 country in November 2025?
2025-11-06 15:08:31,642 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:08:31,642 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$2000)
2025-11-06 15:08:31,642 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,642 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.20
2025-11-06 15:08:31,642 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,642 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike 2 countries in November 2025?
2025-11-06 15:08:31,642 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:08:31,642 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$205)
2025-11-06 15:08:31,642 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,642 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.02
2025-11-06 15:08:31,642 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,642 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Netflix reach $1155 in November?
2025-11-06 15:08:31,642 - market_scanner_v2 - INFO -    - Category: entertainment
2025-11-06 15:08:31,643 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$118)
2025-11-06 15:08:31,643 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,643 - market_scanner_v2 - INFO -    - Competition: 1.243298 bars, Score: -114.32
2025-11-06 15:08:31,643 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,643 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Netflix dip to $1050 in November?
2025-11-06 15:08:31,643 - market_scanner_v2 - INFO -    - Category: entertainment
2025-11-06 15:08:31,643 - market_scanner_v2 - INFO -    - Estimated Reward: $30 (based on volume=$165)
2025-11-06 15:08:31,643 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,643 - market_scanner_v2 - INFO -    - Competition: 0.0205 bars, Score: 12.97
2025-11-06 15:08:31,643 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,643 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Lebanon on November 7?
2025-11-06 15:08:31,643 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:08:31,643 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$1850)
2025-11-06 15:08:31,643 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,643 - market_scanner_v2 - INFO -    - Competition: 0.186114 bars, Score: -8.43
2025-11-06 15:08:31,644 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,644 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Lebanon on November 8?
2025-11-06 15:08:31,644 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:08:31,644 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$365)
2025-11-06 15:08:31,644 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,644 - market_scanner_v2 - INFO -    - Competition: 0.074067 bars, Score: 2.63
2025-11-06 15:08:31,644 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,644 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Lebanon on November 9?
2025-11-06 15:08:31,644 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:08:31,644 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$282)
2025-11-06 15:08:31,644 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,644 - market_scanner_v2 - INFO -    - Competition: 1.977358 bars, Score: -187.71
2025-11-06 15:08:31,644 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,644 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Lebanon on November 11?
2025-11-06 15:08:31,644 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:08:31,644 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$820)
2025-11-06 15:08:31,644 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,644 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.08
2025-11-06 15:08:31,644 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,644 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Lebanon on November 12?
2025-11-06 15:08:31,644 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:08:31,644 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$94)
2025-11-06 15:08:31,644 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,644 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.01
2025-11-06 15:08:31,644 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,644 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Lebanon on November 13?
2025-11-06 15:08:31,645 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:08:31,645 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$20)
2025-11-06 15:08:31,645 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,645 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 10.00
2025-11-06 15:08:31,645 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,645 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Lebanon on November 14?
2025-11-06 15:08:31,645 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:08:31,645 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$486)
2025-11-06 15:08:31,645 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,645 - market_scanner_v2 - INFO -    - Competition: 0.263367 bars, Score: -16.29
2025-11-06 15:08:31,645 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,645 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Gaza on November 7?
2025-11-06 15:08:31,645 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:08:31,645 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$458)
2025-11-06 15:08:31,645 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,645 - market_scanner_v2 - INFO -    - Competition: 0.26335 bars, Score: -16.29
2025-11-06 15:08:31,645 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,645 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Gaza on November 8?
2025-11-06 15:08:31,645 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:08:31,645 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$143)
2025-11-06 15:08:31,645 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,646 - market_scanner_v2 - INFO -    - Competition: 0.888295 bars, Score: -78.82
2025-11-06 15:08:31,646 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,646 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Gaza on November 9?
2025-11-06 15:08:31,646 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:08:31,646 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$264)
2025-11-06 15:08:31,646 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,646 - market_scanner_v2 - INFO -    - Competition: 0.005125 bars, Score: 9.51
2025-11-06 15:08:31,646 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,646 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel strike Gaza on November 11?
2025-11-06 15:08:31,646 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:08:31,646 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$173)
2025-11-06 15:08:31,646 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,646 - market_scanner_v2 - INFO -    - Competition: 2.485664 bars, Score: -238.55
2025-11-06 15:08:31,646 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,646 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Israel launch a major ground offensive in Lebanon by De
2025-11-06 15:08:31,646 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:08:31,647 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$1547)
2025-11-06 15:08:31,647 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,647 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.15
2025-11-06 15:08:31,647 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,647 - market_scanner_v2 - INFO - âœ… ACCEPTED: Park Sung-jae in jail by November 30?
2025-11-06 15:08:31,647 - market_scanner_v2 - INFO -    - Category: science
2025-11-06 15:08:31,647 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$2915)
2025-11-06 15:08:31,647 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,647 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.29
2025-11-06 15:08:31,647 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,647 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Elon Musk post 160-179 tweets from October 31 to Novemb
2025-11-06 15:08:31,647 - market_scanner_v2 - INFO -    - Category: entertainment
2025-11-06 15:08:31,647 - market_scanner_v2 - INFO -    - Estimated Reward: $130 (based on volume=$92649)
2025-11-06 15:08:31,647 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,647 - market_scanner_v2 - INFO -    - Competition: 0.807555 bars, Score: -6.49
2025-11-06 15:08:31,647 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,647 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Elon Musk post 200-219 tweets from October 31 to Novemb
2025-11-06 15:08:31,647 - market_scanner_v2 - INFO -    - Category: entertainment
2025-11-06 15:08:31,647 - market_scanner_v2 - INFO -    - Estimated Reward: $40 (based on volume=$74081)
2025-11-06 15:08:31,647 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,648 - market_scanner_v2 - INFO -    - Competition: 0.4 bars, Score: -12.59
2025-11-06 15:08:31,648 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,648 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Elon Muskâ€™s $1T Tesla pay deal pass?
2025-11-06 15:08:31,648 - market_scanner_v2 - INFO -    - Category: entertainment
2025-11-06 15:08:31,648 - market_scanner_v2 - INFO -    - Estimated Reward: $50 (based on volume=$89521)
2025-11-06 15:08:31,648 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,648 - market_scanner_v2 - INFO -    - Competition: 1.2344 bars, Score: -89.49
2025-11-06 15:08:31,648 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,649 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Stable launch a token in 2025?
2025-11-06 15:08:31,649 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:08:31,649 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$78233)
2025-11-06 15:08:31,649 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,649 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 12.82
2025-11-06 15:08:31,649 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,650 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Trump establish a Gaza â€œBoard of Peaceâ€ in 2025?
2025-11-06 15:08:31,650 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:08:31,650 - market_scanner_v2 - INFO -    - Estimated Reward: $30 (based on volume=$9651)
2025-11-06 15:08:31,650 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,650 - market_scanner_v2 - INFO -    - Competition: 0.396333 bars, Score: -23.67
2025-11-06 15:08:31,650 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,650 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will the Government shutdown end November 8-11?
2025-11-06 15:08:31,650 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:08:31,650 - market_scanner_v2 - INFO -    - Estimated Reward: $200 (based on volume=$192333)
2025-11-06 15:08:31,650 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,650 - market_scanner_v2 - INFO -    - Competition: 1.49344 bars, Score: -30.11
2025-11-06 15:08:31,650 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,650 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will the Government shutdown end November 12-15?
2025-11-06 15:08:31,650 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:08:31,650 - market_scanner_v2 - INFO -    - Estimated Reward: $200 (based on volume=$106409)
2025-11-06 15:08:31,650 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,650 - market_scanner_v2 - INFO -    - Competition: 1.44465 bars, Score: -33.82
2025-11-06 15:08:31,650 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,651 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will MetaMask launch a token by September 30, 2026?
2025-11-06 15:08:31,651 - market_scanner_v2 - INFO -    - Category: crypto
2025-11-06 15:08:31,651 - market_scanner_v2 - INFO -    - Estimated Reward: $20 (based on volume=$191)
2025-11-06 15:08:31,651 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,651 - market_scanner_v2 - INFO -    - Competition: 0.769923 bars, Score: -66.97
2025-11-06 15:08:31,651 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,652 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Matt Van Epps win TN-7 Special Election?
2025-11-06 15:08:31,652 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:08:31,652 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$1695)
2025-11-06 15:08:31,652 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,652 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.17
2025-11-06 15:08:31,652 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,652 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Russia capture all of Pokrovsk by November 14?
2025-11-06 15:08:31,652 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:08:31,652 - market_scanner_v2 - INFO -    - Estimated Reward: $30 (based on volume=$13354)
2025-11-06 15:08:31,652 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,652 - market_scanner_v2 - INFO -    - Competition: 0.272272 bars, Score: -10.89
2025-11-06 15:08:31,652 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,652 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Russia capture Siversk by November 30?
2025-11-06 15:08:31,652 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:08:31,652 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$3748)
2025-11-06 15:08:31,652 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,652 - market_scanner_v2 - INFO -    - Competition: 1.821149 bars, Score: -176.74
2025-11-06 15:08:31,653 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,653 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Russia capture Siversk by December 31?
2025-11-06 15:08:31,653 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:08:31,653 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$3536)
2025-11-06 15:08:31,653 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,653 - market_scanner_v2 - INFO -    - Competition: 2.075986 bars, Score: -202.25
2025-11-06 15:08:31,653 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,653 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Gemini 3.0 be released by November 15?
2025-11-06 15:08:31,653 - market_scanner_v2 - INFO -    - Category: science
2025-11-06 15:08:31,653 - market_scanner_v2 - INFO -    - Estimated Reward: $200 (based on volume=$495622)
2025-11-06 15:08:31,653 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,653 - market_scanner_v2 - INFO -    - Competition: 1.3876 bars, Score: 10.80
2025-11-06 15:08:31,653 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,653 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Gemini 3.0 be released by November 22?
2025-11-06 15:08:31,653 - market_scanner_v2 - INFO -    - Category: science
2025-11-06 15:08:31,653 - market_scanner_v2 - INFO -    - Estimated Reward: $50 (based on volume=$14533)
2025-11-06 15:08:31,653 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,653 - market_scanner_v2 - INFO -    - Competition: 0.243152 bars, Score: 2.14
2025-11-06 15:08:31,653 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,654 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Russia capture Myrnohrad by November 7?
2025-11-06 15:08:31,654 - market_scanner_v2 - INFO -    - Category: politics
2025-11-06 15:08:31,654 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$7500)
2025-11-06 15:08:31,654 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,654 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.75
2025-11-06 15:08:31,654 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,654 - market_scanner_v2 - INFO - âœ… ACCEPTED: Will Oscar Piastri finish second in the 2025 Drivers Champio
2025-11-06 15:08:31,655 - market_scanner_v2 - INFO -    - Category: entertainment
2025-11-06 15:08:31,655 - market_scanner_v2 - INFO -    - Estimated Reward: $10 (based on volume=$119)
2025-11-06 15:08:31,655 - market_scanner_v2 - INFO -    - Rewards Config: minSize=0, maxSpread=0
2025-11-06 15:08:31,655 - market_scanner_v2 - INFO -    - Competition: 0 bars, Score: 5.01
2025-11-06 15:08:31,655 - market_scanner_v2 - INFO -    - Source: playwright_api_direct
2025-11-06 15:08:31,656 - market_scanner_v2 - INFO - ðŸ“Š Filter results: 80/2836 markets passed
2025-11-06 15:08:31,656 - market_scanner_v2 - INFO -    - 2518 rejected: reward < $10
2025-11-06 15:08:31,656 - market_scanner_v2 - INFO -    - 205 rejected: competition > 3
2025-11-06 15:08:31,656 - market_scanner_v2 - INFO -    - 30 rejected: category not in ['crypto', 'sports', 'politics', 'science', 'entertainment']
2025-11-06 15:08:31,656 - market_scanner_v2 - INFO -    - 3 rejected: volume = 0 (no liquidity)
2025-11-06 15:08:31,656 - market_scanner_v2 - INFO - ðŸ” Verifying orderbook for top 50 markets...
2025-11-06 15:08:49,047 - market_scanner_v2 - INFO - âœ… Found 80 qualifying markets (from 2836 total)
2025-11-06 15:08:49,051 - market_selector - INFO - Selected 2 markets from 80 candidates
2025-11-06 15:08:51,435 - order_manager - WARNING - âŒ Calculated prices exceed max spread (94.20% > 3.50%)
2025-11-06 15:08:51,435 - order_manager - WARNING -    This indicates orderbook is too thin or position 2-3 is too far from midpoint
2025-11-06 15:08:51,435 - order_manager - WARNING -    REJECTING market to avoid placing order at position #1 (best bid/ask)
2025-11-06 15:08:51,435 - order_manager - WARNING -    Reason: Adjusting to max spread would place order too close to best bid/ask
2025-11-06 15:08:51,435 - order_manager - WARNING -    â†’ High risk of being filled immediately!
2025-11-06 15:08:51,435 - order_manager - WARNING - Could not calculate valid prices for market 657210
2025-11-06 15:08:51,435 - __main__ - WARNING - âš ï¸  Skipped market 657210 - could not prepare valid order (spread too high or orderbook too thin)
2025-11-06 15:08:51,776 - order_manager - WARNING - âŒ Calculated prices exceed max spread (94.20% > 3.50%)
2025-11-06 15:08:51,777 - order_manager - WARNING -    This indicates orderbook is too thin or position 2-3 is too far from midpoint
2025-11-06 15:08:51,777 - order_manager - WARNING -    REJECTING market to avoid placing order at position #1 (best bid/ask)
2025-11-06 15:08:51,777 - order_manager - WARNING -    Reason: Adjusting to max spread would place order too close to best bid/ask
2025-11-06 15:08:51,777 - order_manager - WARNING -    â†’ High risk of being filled immediately!
2025-11-06 15:08:51,777 - order_manager - WARNING - Could not calculate valid prices for market 539029
2025-11-06 15:08:51,777 - __main__ - WARNING - âš ï¸  Skipped market 539029 - could not prepare valid order (spread too high or orderbook too thin)
2025-11-06 15:09:52,064 - __main__ - WARNING - âš ï¸ Health check failed: 2 issues
2025-11-06 15:09:52,064 - __main__ - WARNING -    - ðŸ”´ KhÃ´ng quÃ©t markets trong 62s!
2025-11-06 15:09:52,064 - __main__ - WARNING -    - âš ï¸ API cháº­m: 40.8s trung bÃ¬nh
2025-11-06 15:09:58,907 - market_scanner_v2 - INFO - ðŸŒ Scraping markets from /rewards page using Playwright...
2025-11-06 15:09:58,907 - playwright_rewards_scraper - INFO - ðŸŒ Fetching markets from /rewards API...
2025-11-06 15:09:58,908 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 1 (cursor: MA==)...
2025-11-06 15:09:59,582 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 1
2025-11-06 15:09:59,583 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 2 (cursor: MTAw)...
2025-11-06 15:10:00,280 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 2
2025-11-06 15:10:00,280 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 3 (cursor: MjAw)...
2025-11-06 15:10:00,964 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 3
2025-11-06 15:10:00,965 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 4 (cursor: MzAw)...
2025-11-06 15:10:01,652 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 4
2025-11-06 15:10:01,653 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 5 (cursor: NDAw)...
2025-11-06 15:10:02,325 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 5
2025-11-06 15:10:02,325 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 6 (cursor: NTAw)...
2025-11-06 15:10:03,020 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 6
2025-11-06 15:10:03,021 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 7 (cursor: NjAw)...
2025-11-06 15:10:03,694 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 7
2025-11-06 15:10:03,695 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 8 (cursor: NzAw)...
2025-11-06 15:10:04,348 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 8
2025-11-06 15:10:04,349 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 9 (cursor: ODAw)...
2025-11-06 15:10:05,053 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 9
2025-11-06 15:10:05,054 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 10 (cursor: OTAw)...
2025-11-06 15:10:05,717 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 10
2025-11-06 15:10:05,717 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 11 (cursor: MTAwMA==)...
2025-11-06 15:10:06,406 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 11
2025-11-06 15:10:06,407 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 12 (cursor: MTEwMA==)...
2025-11-06 15:10:07,043 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 12
2025-11-06 15:10:07,043 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 13 (cursor: MTIwMA==)...
2025-11-06 15:10:07,707 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 13
2025-11-06 15:10:07,708 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 14 (cursor: MTMwMA==)...
2025-11-06 15:10:08,418 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 14
2025-11-06 15:10:08,418 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 15 (cursor: MTQwMA==)...
2025-11-06 15:10:08,896 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 15
2025-11-06 15:10:08,897 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 16 (cursor: MTUwMA==)...
2025-11-06 15:10:09,360 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 16
2025-11-06 15:10:09,361 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 17 (cursor: MTYwMA==)...
2025-11-06 15:10:09,816 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 17
2025-11-06 15:10:09,817 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 18 (cursor: MTcwMA==)...
2025-11-06 15:10:10,496 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 18
2025-11-06 15:10:10,497 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 19 (cursor: MTgwMA==)...
2025-11-06 15:10:11,188 - playwright_rewards_scraper - INFO - âœ… Got 100 markets on page 19
2025-11-06 15:10:11,189 - playwright_rewards_scraper - INFO - ðŸ“„ Fetching page 20 (cursor: MTkwMA==)...
