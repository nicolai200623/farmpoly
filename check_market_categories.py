"""
Check what categories the markets belong to
"""

import asyncio
import logging
from polymarket_rewards_api import PolymarketRewardsAPI
from market_scanner_v2 import MarketScannerV2

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def check_categories():
    """Check market categories"""
    api = PolymarketRewardsAPI()
    
    # Fetch markets
    markets = await api.fetch_all_rewards_markets(limit=100)
    
    print(f"\n{'='*80}")
    print(f"📊 CHECKING CATEGORIES FOR {len(markets)} MARKETS")
    print(f"{'='*80}\n")
    
    # Create scanner to use category inference
    config = {
        'min_reward': 3,
        'max_competition_bars': 3,
        'target_categories': ['crypto', 'sports', 'politics', 'science', 'entertainment']
    }
    scanner = MarketScannerV2(config)
    
    # Count categories
    category_counts = {}
    
    for market in markets:
        # Infer category
        category = scanner._infer_category(market['question'], market)
        
        if category not in category_counts:
            category_counts[category] = []
        
        category_counts[category].append(market)
    
    # Print summary
    print(f"📈 CATEGORY DISTRIBUTION:\n")
    for category, markets_list in sorted(category_counts.items(), key=lambda x: len(x[1]), reverse=True):
        print(f"{category}: {len(markets_list)} markets")
    
    # Show sample markets for each category
    print(f"\n{'='*80}")
    print(f"📋 SAMPLE MARKETS BY CATEGORY")
    print(f"{'='*80}\n")
    
    for category, markets_list in sorted(category_counts.items(), key=lambda x: len(x[1]), reverse=True):
        print(f"\n{category.upper()} ({len(markets_list)} markets):")
        print("-" * 80)
        for i, market in enumerate(markets_list[:5], 1):
            print(f"{i}. {market['question'][:70]}")
            print(f"   Reward: ${market['reward']}, Competition: {market['competition_bars']} bars")


if __name__ == "__main__":
    asyncio.run(check_categories())

