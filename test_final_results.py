"""
Test final results - show selected markets
"""

import asyncio
import logging
import yaml
from market_scanner_v2 import MarketScannerV2
from market_selector import MarketSelectorAI

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def test_final():
    """Test final results"""
    
    # Load config
    with open('config.yaml', 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    
    scanner_config = config['market_scanner']
    
    # Create scanner
    scanner = MarketScannerV2(scanner_config)
    
    # Scan markets
    markets = await scanner.scan_rewards_page()
    
    print(f"\n{'='*80}")
    print(f"SCAN RESULTS")
    print(f"{'='*80}\n")
    print(f"Total markets fetched: {len(markets)}")

    # Filter markets
    filtered = scanner._filter_markets(markets)

    print(f"Markets after filtering: {len(filtered)}")

    # Select markets
    selector = MarketSelectorAI(scanner_config)
    selected = await selector.select_markets(filtered)

    print(f"Markets selected: {len(selected)}")

    # Show selected markets
    print(f"\n{'='*80}")
    print(f"SELECTED MARKETS")
    print(f"{'='*80}\n")

    for i, market in enumerate(selected, 1):
        print(f"{i}. {market['question'][:70]}")
        print(f"   Reward: ${market['reward']}")
        print(f"   Competition: {market['competition_bars']} bars")
        print(f"   Category: {market.get('category', 'unknown')}")
        print(f"   Volume 24h: ${market['volume_24hr']:.0f}")
        print(f"   ID: {market['market_id']}")
        print()


if __name__ == "__main__":
    asyncio.run(test_final())

