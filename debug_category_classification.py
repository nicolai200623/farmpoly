"""
Debug category classification
"""

import asyncio
import yaml
from web_rewards_scraper import WebRewardsScraper
from market_scanner_v2 import MarketScannerV2


async def debug():
    # Load config
    with open('config.yaml', 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)

    # Fetch markets
    scraper = WebRewardsScraper()
    markets = await scraper.fetch_rewards_markets(limit=10)

    print(f"\n{'='*80}")
    print(f"FETCHED {len(markets)} MARKETS")
    print(f"{'='*80}\n")

    # Parse markets
    parsed_markets = []
    for market in markets:
        parsed = scraper.parse_market(market)
        if parsed:
            parsed_markets.append(parsed)

    print(f"PARSED {len(parsed_markets)} MARKETS\n")

    # Test category classification
    scanner = MarketScannerV2(config)
    
    for i, market in enumerate(parsed_markets[:5], 1):
        print(f"\n{'-'*80}")
        print(f"MARKET {i}")
        print(f"{'-'*80}")
        print(f"Question: {market.get('question')}")
        print(f"Tags: {market.get('tags')}")
        print(f"Reward: ${market.get('reward'):.0f}")

        # Test category inference
        category = scanner._infer_category(market.get('question'), market)
        print(f"Inferred Category: {category}")


if __name__ == "__main__":
    asyncio.run(debug())

