"""
Test fetching clob_token_ids from Gamma API
"""
import asyncio
from playwright_rewards_scraper import PlaywrightRewardsScraper

async def test():
    scraper = PlaywrightRewardsScraper()
    
    print("=" * 80)
    print("🔍 Testing clob_token_ids fetch")
    print("=" * 80)
    
    # Fetch all markets
    print("\n📥 Fetching markets...")
    markets = await scraper.scrape_rewards_page()
    print(f"✅ Fetched {len(markets)} markets")
    
    # Check how many have clob_token_ids
    markets_with_clob = [m for m in markets if m.get('clob_token_ids') and len(m['clob_token_ids']) > 0]
    print(f"\n📊 Markets with clob_token_ids: {len(markets_with_clob)}/{len(markets)}")
    
    # Show first 5 markets with clob_token_ids
    print(f"\n📋 First 5 markets with clob_token_ids:")
    for i, market in enumerate(markets_with_clob[:5]):
        print(f"\n{i+1}. {market['question'][:60]}...")
        print(f"   Reward: ${market['reward']:.0f}")
        print(f"   Competition: {market['competition_bars']}")
        print(f"   Volume: ${market['volume']:,.2f}")
        print(f"   CLOB Token IDs: {market['clob_token_ids']}")
    
    # Check markets with reward >= 10
    high_reward_markets = [m for m in markets if m['reward'] >= 10]
    high_reward_with_clob = [m for m in high_reward_markets if m.get('clob_token_ids') and len(m['clob_token_ids']) > 0]
    
    print(f"\n📊 High-reward markets (>= $10):")
    print(f"   Total: {len(high_reward_markets)}")
    print(f"   With clob_token_ids: {len(high_reward_with_clob)}")
    print(f"   Without clob_token_ids: {len(high_reward_markets) - len(high_reward_with_clob)}")

if __name__ == "__main__":
    asyncio.run(test())

