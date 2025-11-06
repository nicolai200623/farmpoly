"""
Detailed analysis of web scraper results
"""

import asyncio
import yaml
from web_rewards_scraper import WebRewardsScraper
from market_scanner_v2 import MarketScannerV2


async def test_detailed():
    # Load config
    with open('config.yaml', 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    
    scanner_config = config.get('market_scanner', {})
    min_reward = scanner_config.get('min_reward', 10)
    max_competition = scanner_config.get('max_competition_bars', 1)
    target_categories = scanner_config.get('target_categories', [])
    
    print("=" * 80)
    print("DETAILED WEB SCRAPER ANALYSIS")
    print("=" * 80)
    print(f"\nFilter Settings:")
    print(f"  Min Reward: ${min_reward}")
    print(f"  Max Competition: {max_competition} bars")
    print(f"  Target Categories: {target_categories}")
    print()
    
    # Fetch markets
    scraper = WebRewardsScraper()
    markets_raw = await scraper.fetch_rewards_markets(limit=100)
    
    # Parse markets
    markets = []
    for market_data in markets_raw:
        parsed = scraper.parse_market(market_data)
        if parsed:
            markets.append(parsed)
    
    print(f"OK Fetched {len(markets)} markets from /rewards page\n")
    
    # Analyze why markets are rejected
    scanner = MarketScannerV2(scanner_config)
    
    # Count rejections
    low_reward = 0
    high_competition = 0
    wrong_category = 0
    passed = 0
    
    print("=" * 80)
    print("ANALYZING EACH MARKET")
    print("=" * 80)
    
    for i, market in enumerate(markets[:20], 1):  # First 20 for analysis
        question = market['question'][:60]
        reward = market['reward']
        competition = market['competition_bars']
        category = scanner._infer_category(market['question'])
        
        # Check filters
        reasons = []
        if reward < min_reward:
            reasons.append(f"reward ${reward:.2f} < ${min_reward}")
            low_reward += 1
        if competition > max_competition:
            reasons.append(f"competition {competition} > {max_competition}")
            high_competition += 1
        if target_categories and category not in target_categories:
            reasons.append(f"category '{category}' not in {target_categories}")
            wrong_category += 1
        
        if not reasons:
            status = "[PASS]"
            passed += 1
        else:
            status = f"[REJECT]: {', '.join(reasons)}"
        
        print(f"\n{i}. {question}")
        print(f"   Reward: ${reward:.2f} | Competition: {competition} | Category: {category}")
        print(f"   {status}")
    
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Total markets: {len(markets)}")
    print(f"  [OK] Passed: {passed}")
    print(f"  [X] Low reward: {low_reward}")
    print(f"  [X] High competition: {high_competition}")
    print(f"  [X] Wrong category: {wrong_category}")
    
    # Show top markets by reward
    print("\n" + "=" * 80)
    print("TOP 10 MARKETS BY ESTIMATED REWARD")
    print("=" * 80)
    
    sorted_markets = sorted(markets, key=lambda m: m['reward'], reverse=True)
    for i, market in enumerate(sorted_markets[:10], 1):
        category = scanner._infer_category(market['question'])
        print(f"\n{i}. {market['question'][:60]}")
        print(f"   Reward: ${market['reward']:.2f}")
        print(f"   Competition: {market['competition_bars']} bars")
        print(f"   Category: {category}")
        print(f"   Volume 24h: ${market['volume']:.2f}")


if __name__ == "__main__":
    asyncio.run(test_detailed())

