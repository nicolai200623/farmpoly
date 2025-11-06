"""
Test if SpaceX markets appear in web scraper results
"""

import asyncio
from web_rewards_scraper import WebRewardsScraper


async def test_spacex():
    scraper = WebRewardsScraper()
    
    print("=" * 80)
    print("CHECKING FOR SPACEX MARKETS IN WEB SCRAPER")
    print("=" * 80)
    
    # Fetch all markets (no limit)
    markets = await scraper.fetch_rewards_markets(limit=None)
    
    print(f"\n✅ Fetched {len(markets)} total markets from /rewards page\n")
    
    # Search for SpaceX
    spacex_markets = []
    for market_data in markets:
        question = market_data.get('question', '')
        if 'SpaceX' in question or 'spacex' in question.lower():
            spacex_markets.append(market_data)
    
    if spacex_markets:
        print(f"❌ FOUND {len(spacex_markets)} SpaceX markets (UNEXPECTED!):\n")
        for market in spacex_markets:
            print(f"  - {market.get('question')}")
            print(f"    Market ID: {market.get('market_id')}")
            print()
    else:
        print("✅ NO SpaceX markets found (CORRECT!)")
        print("   This confirms web scraper only returns markets on /rewards page")
    
    # Show first 10 markets for reference
    print("\n" + "=" * 80)
    print("FIRST 10 MARKETS FROM WEB:")
    print("=" * 80)
    for i, market_data in enumerate(markets[:10], 1):
        parsed = scraper.parse_market(market_data)
        if parsed:
            print(f"{i}. {parsed['question'][:70]}")


if __name__ == "__main__":
    asyncio.run(test_spacex())

