"""
Test bot with new web scraper
Verify it finds markets from /rewards page and NOT SpaceX markets
"""

import asyncio
import yaml
import logging
from market_scanner_v2 import MarketScannerV2

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)


async def test_bot():
    # Load config
    with open('config.yaml', 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    
    scanner_config = config.get('market_scanner', {})
    
    print("=" * 80)
    print("TESTING BOT WITH WEB SCRAPER")
    print("=" * 80)
    print(f"\nConfig:")
    print(f"  Min Reward: ${scanner_config.get('min_reward', 10)}")
    print(f"  Max Competition: {scanner_config.get('max_competition_bars', 1)} bars")
    print(f"  Target Categories: {scanner_config.get('target_categories', [])}")
    print()
    
    # Create scanner
    scanner = MarketScannerV2(scanner_config)
    
    # Scan markets
    print("Scanning markets...\n")
    markets = await scanner.scan_rewards_page()

    print("\n" + "=" * 80)
    print(f"RESULTS: Found {len(markets)} qualifying markets")
    print("=" * 80)

    if markets:
        # Check for SpaceX
        spacex_count = sum(1 for m in markets if 'spacex' in m['question'].lower())

        if spacex_count > 0:
            print(f"\n[ERROR] Found {spacex_count} SpaceX markets (should be 0!)")
            for m in markets:
                if 'spacex' in m['question'].lower():
                    print(f"  - {m['question']}")
        else:
            print(f"\n[OK] CORRECT: No SpaceX markets found")

        # Show first 10 markets
        print(f"\nFirst 10 qualifying markets:")
        for i, market in enumerate(markets[:10], 1):
            print(f"\n{i}. {market['question'][:70]}")
            print(f"   Category: {market.get('category', 'N/A')}")
            print(f"   Reward: ${market['reward']:.2f}")
            print(f"   Competition: {market['competition_bars']} bars")
            print(f"   Volume 24h: ${market['volume']:.2f}")
            print(f"   Source: {market.get('source', 'N/A')}")
    else:
        print("\n[WARNING] No markets found")
        print("   Check config settings (min_reward, max_competition_bars, target_categories)")


if __name__ == "__main__":
    asyncio.run(test_bot())

