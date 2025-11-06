"""
Analyze rejected markets to improve category classification
"""

import asyncio
import yaml
from web_rewards_scraper import WebRewardsScraper
from market_scanner_v2 import MarketScannerV2


async def analyze():
    # Load config
    with open('config.yaml', 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    
    scanner_config = config.get('market_scanner', {})
    min_reward = scanner_config.get('min_reward', 10)
    target_categories = scanner_config.get('target_categories', [])
    
    print("=" * 80)
    print("ANALYZING REJECTED CATEGORIES")
    print("=" * 80)
    print(f"Target categories: {target_categories}")
    print(f"Min reward: ${min_reward}\n")
    
    # Fetch markets
    scraper = WebRewardsScraper()
    markets_raw = await scraper.fetch_rewards_markets(limit=100)
    
    # Parse markets
    markets = []
    for market_data in markets_raw:
        parsed = scraper.parse_market(market_data)
        if parsed:
            markets.append(parsed)
    
    scanner = MarketScannerV2(scanner_config)
    
    # Group by category
    by_category = {}
    rejected_by_category = {}
    
    for market in markets:
        if market['reward'] < min_reward:
            continue  # Skip low reward
        
        category = scanner._infer_category(market['question'])
        
        if category not in by_category:
            by_category[category] = []
        by_category[category].append(market)
        
        # Check if rejected
        if target_categories and category not in target_categories:
            if category not in rejected_by_category:
                rejected_by_category[category] = []
            rejected_by_category[category].append(market)
    
    # Show statistics
    print("CATEGORY DISTRIBUTION (reward >= $10):")
    print("=" * 80)
    for category in sorted(by_category.keys()):
        count = len(by_category[category])
        rejected = len(rejected_by_category.get(category, []))
        status = "[REJECTED]" if rejected > 0 else "[ACCEPTED]"
        print(f"{status} {category:15s}: {count:3d} markets")
    
    # Show rejected markets by category
    print("\n" + "=" * 80)
    print("REJECTED MARKETS BY CATEGORY")
    print("=" * 80)
    
    for category in sorted(rejected_by_category.keys()):
        markets_list = rejected_by_category[category]
        print(f"\n{category.upper()} ({len(markets_list)} markets):")
        print("-" * 80)
        
        for i, market in enumerate(markets_list[:10], 1):  # Show first 10
            print(f"{i}. {market['question'][:70]}")
            print(f"   Reward: ${market['reward']:.2f}")
        
        if len(markets_list) > 10:
            print(f"   ... and {len(markets_list) - 10} more")
    
    # Suggest keywords
    print("\n" + "=" * 80)
    print("SUGGESTED KEYWORDS TO ADD")
    print("=" * 80)
    
    # Analyze "other" category
    if 'other' in rejected_by_category:
        print("\nOTHER category (needs classification):")
        other_markets = rejected_by_category['other']
        
        # Extract common words
        from collections import Counter
        words = []
        for market in other_markets:
            question_lower = market['question'].lower()
            # Extract words
            import re
            market_words = re.findall(r'\b[a-z]{4,}\b', question_lower)
            words.extend(market_words)
        
        # Count frequency
        word_freq = Counter(words)
        print("\nMost common words:")
        for word, count in word_freq.most_common(20):
            if word not in ['will', 'have', 'than', 'more', 'less', 'before', 'after', 'from', 'with', 'that', 'this']:
                print(f"  {word}: {count}")


if __name__ == "__main__":
    asyncio.run(analyze())

