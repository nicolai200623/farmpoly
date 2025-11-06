"""
Test fetching clob_token_ids from Gamma API with debug logging
"""
import asyncio
import logging

# Enable debug logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

from playwright_rewards_scraper import PlaywrightRewardsScraper

async def test():
    scraper = PlaywrightRewardsScraper()
    
    print("=" * 80)
    print("🔍 Testing clob_token_ids fetch with DEBUG logging")
    print("=" * 80)
    
    # Fetch all markets
    print("\n📥 Fetching markets...")
    markets = await scraper.scrape_rewards_page()
    print(f"✅ Fetched {len(markets)} markets")
    
    # Check how many have clob_token_ids
    markets_with_clob = [m for m in markets if m.get('clob_token_ids') and len(m['clob_token_ids']) > 0]
    print(f"\n📊 Markets with clob_token_ids: {len(markets_with_clob)}/{len(markets)}")
    
    # Show first 5 markets with clob_token_ids
    if markets_with_clob:
        print(f"\n📋 First 5 markets with clob_token_ids:")
        for i, market in enumerate(markets_with_clob[:5]):
            print(f"\n{i+1}. {market['question'][:60]}...")
            print(f"   Reward: ${market['reward']:.0f}")
            print(f"   Competition: {market['competition_bars']}")
            print(f"   Volume: ${market['volume']:,.2f}")
            print(f"   CLOB Token IDs: {market['clob_token_ids']}")
    else:
        print("\n❌ NO markets have clob_token_ids!")
        print("\nChecking first 5 markets:")
        for i, market in enumerate(markets[:5]):
            print(f"\n{i+1}. {market['question'][:60]}...")
            print(f"   Reward: ${market['reward']:.0f}")
            print(f"   Slug: {market.get('slug', 'NO SLUG')}")
            print(f"   CLOB Token IDs: {market.get('clob_token_ids', 'NO FIELD')}")

if __name__ == "__main__":
    asyncio.run(test())

