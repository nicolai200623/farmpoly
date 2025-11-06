"""
Debug script to analyze filter logic and find why 0 markets pass filters
"""
import asyncio
import sys
from playwright_rewards_scraper import PlaywrightRewardsScraper

async def debug_filters():
    """Debug filter logic step by step"""
    
    print("=" * 80)
    print("🔍 DEBUGGING FILTER LOGIC")
    print("=" * 80)
    
    # Initialize scraper
    scraper = PlaywrightRewardsScraper()
    
    # Fetch all markets
    print("\n📥 Fetching all markets from /rewards API...")
    markets = await scraper.scrape_rewards_page()
    print(f"✅ Fetched {len(markets)} total markets")
    
    # Config values
    min_reward = 10
    max_competition = 3
    target_categories = ['crypto', 'sports', 'politics', 'science', 'entertainment']
    
    print(f"\n⚙️  Filter Config:")
    print(f"   - min_reward: ${min_reward}")
    print(f"   - max_competition: {max_competition}")
    print(f"   - target_categories: {target_categories}")
    
    # Step 1: Filter by reward
    print(f"\n" + "=" * 80)
    print(f"STEP 1: Filter by reward >= ${min_reward}")
    print("=" * 80)
    
    markets_with_high_reward = []
    for market in markets:
        reward = market.get('reward', 0) or market.get('umaReward', 0)
        if reward >= min_reward:
            markets_with_high_reward.append(market)
    
    print(f"✅ {len(markets_with_high_reward)}/{len(markets)} markets have reward >= ${min_reward}")
    
    # Show first 5 examples
    print(f"\n📋 First 5 markets with reward >= ${min_reward}:")
    for i, market in enumerate(markets_with_high_reward[:5]):
        reward = market.get('reward', 0) or market.get('umaReward', 0)
        competition = market.get('competition', 0)
        category = market.get('category', 'unknown')
        clob_ids = market.get('clob_token_ids', [])
        volume = market.get('volume', 0) or market.get('volume_24hr', 0)
        
        print(f"\n{i+1}. {market.get('question', 'NO QUESTION')[:60]}...")
        print(f"   ID: {market.get('id')}")
        print(f"   Reward: ${reward}")
        print(f"   Competition: {competition}")
        print(f"   Category: {category}")
        print(f"   CLOB Token IDs: {len(clob_ids)} tokens")
        print(f"   Volume: ${volume:,.2f}")
    
    # Step 2: Filter by competition
    print(f"\n" + "=" * 80)
    print(f"STEP 2: Filter by competition <= {max_competition}")
    print("=" * 80)
    
    markets_with_low_competition = []
    competition_values = []
    for market in markets_with_high_reward:
        competition = market.get('competition', 0)
        competition_values.append(competition)
        if competition <= max_competition:
            markets_with_low_competition.append(market)
    
    print(f"✅ {len(markets_with_low_competition)}/{len(markets_with_high_reward)} markets have competition <= {max_competition}")
    
    # Show competition distribution
    print(f"\n📊 Competition distribution in high-reward markets:")
    from collections import Counter
    comp_counter = Counter(competition_values)
    for comp_level in sorted(comp_counter.keys()):
        count = comp_counter[comp_level]
        bar = "█" * min(50, count)
        print(f"   Competition {comp_level}: {count:4d} markets {bar}")
    
    # Show first 5 examples
    print(f"\n📋 First 5 markets with reward >= ${min_reward} AND competition <= {max_competition}:")
    for i, market in enumerate(markets_with_low_competition[:5]):
        reward = market.get('reward', 0) or market.get('umaReward', 0)
        competition = market.get('competition', 0)
        category = market.get('category', 'unknown')
        clob_ids = market.get('clob_token_ids', [])
        volume = market.get('volume', 0) or market.get('volume_24hr', 0)
        
        print(f"\n{i+1}. {market.get('question', 'NO QUESTION')[:60]}...")
        print(f"   ID: {market.get('id')}")
        print(f"   Reward: ${reward}")
        print(f"   Competition: {competition}")
        print(f"   Category: {category}")
        print(f"   CLOB Token IDs: {len(clob_ids)} tokens")
        print(f"   Volume: ${volume:,.2f}")
    
    # Step 3: Filter by category
    print(f"\n" + "=" * 80)
    print(f"STEP 3: Filter by category in {target_categories}")
    print("=" * 80)
    
    markets_with_target_category = []
    category_values = []
    for market in markets_with_low_competition:
        category = market.get('category', 'other')
        category_values.append(category)
        if category in target_categories:
            markets_with_target_category.append(market)
    
    print(f"✅ {len(markets_with_target_category)}/{len(markets_with_low_competition)} markets have category in {target_categories}")
    
    # Show category distribution
    print(f"\n📊 Category distribution in low-competition markets:")
    cat_counter = Counter(category_values)
    for category in sorted(cat_counter.keys()):
        count = cat_counter[category]
        in_target = "✅" if category in target_categories else "❌"
        print(f"   {in_target} {category}: {count} markets")
    
    # Show first 5 examples
    print(f"\n📋 First 5 markets passing reward + competition + category filters:")
    for i, market in enumerate(markets_with_target_category[:5]):
        reward = market.get('reward', 0) or market.get('umaReward', 0)
        competition = market.get('competition', 0)
        category = market.get('category', 'unknown')
        clob_ids = market.get('clob_token_ids', [])
        volume = market.get('volume', 0) or market.get('volume_24hr', 0)
        
        print(f"\n{i+1}. {market.get('question', 'NO QUESTION')[:60]}...")
        print(f"   ID: {market.get('id')}")
        print(f"   Reward: ${reward}")
        print(f"   Competition: {competition}")
        print(f"   Category: {category}")
        print(f"   CLOB Token IDs: {len(clob_ids)} tokens")
        print(f"   Volume: ${volume:,.2f}")
    
    # Step 4: Filter by clob_token_ids
    print(f"\n" + "=" * 80)
    print(f"STEP 4: Filter by clob_token_ids existence")
    print("=" * 80)
    
    markets_with_clob_ids = []
    for market in markets_with_target_category:
        clob_ids = market.get('clob_token_ids', [])
        if clob_ids and len(clob_ids) > 0:
            markets_with_clob_ids.append(market)
    
    print(f"✅ {len(markets_with_clob_ids)}/{len(markets_with_target_category)} markets have clob_token_ids")
    
    # Show first 5 examples
    print(f"\n📋 First 5 markets passing ALL filters (reward + competition + category + clob_ids):")
    for i, market in enumerate(markets_with_clob_ids[:5]):
        reward = market.get('reward', 0) or market.get('umaReward', 0)
        competition = market.get('competition', 0)
        category = market.get('category', 'unknown')
        clob_ids = market.get('clob_token_ids', [])
        volume = market.get('volume', 0) or market.get('volume_24hr', 0)
        
        print(f"\n{i+1}. {market.get('question', 'NO QUESTION')[:60]}...")
        print(f"   ID: {market.get('id')}")
        print(f"   Reward: ${reward}")
        print(f"   Competition: {competition}")
        print(f"   Category: {category}")
        print(f"   CLOB Token IDs: {clob_ids}")
        print(f"   Volume: ${volume:,.2f}")
    
    # Step 5: Filter by volume
    print(f"\n" + "=" * 80)
    print(f"STEP 5: Filter by volume > 0")
    print("=" * 80)
    
    markets_with_volume = []
    for market in markets_with_clob_ids:
        volume = market.get('volume', 0) or market.get('volume_24hr', 0)
        if volume > 0:
            markets_with_volume.append(market)
    
    print(f"✅ {len(markets_with_volume)}/{len(markets_with_clob_ids)} markets have volume > 0")
    
    # Show first 5 examples
    print(f"\n📋 FINAL: First 5 markets passing ALL filters:")
    for i, market in enumerate(markets_with_volume[:5]):
        reward = market.get('reward', 0) or market.get('umaReward', 0)
        competition = market.get('competition', 0)
        category = market.get('category', 'unknown')
        clob_ids = market.get('clob_token_ids', [])
        volume = market.get('volume', 0) or market.get('volume_24hr', 0)
        
        print(f"\n{i+1}. {market.get('question', 'NO QUESTION')[:60]}...")
        print(f"   ID: {market.get('id')}")
        print(f"   Reward: ${reward}")
        print(f"   Competition: {competition}")
        print(f"   Category: {category}")
        print(f"   CLOB Token IDs: {clob_ids}")
        print(f"   Volume: ${volume:,.2f}")
    
    # Summary
    print(f"\n" + "=" * 80)
    print(f"📊 SUMMARY")
    print("=" * 80)
    print(f"Total markets fetched: {len(markets)}")
    print(f"After reward filter (>= ${min_reward}): {len(markets_with_high_reward)}")
    print(f"After competition filter (<= {max_competition}): {len(markets_with_low_competition)}")
    print(f"After category filter: {len(markets_with_target_category)}")
    print(f"After clob_token_ids filter: {len(markets_with_clob_ids)}")
    print(f"After volume filter (> 0): {len(markets_with_volume)}")
    print(f"\n✅ FINAL: {len(markets_with_volume)} markets pass ALL filters")
    
    # Check if bot's filter logic matches
    print(f"\n" + "=" * 80)
    print(f"🔍 CHECKING BOT'S FILTER LOGIC")
    print("=" * 80)
    
    if len(markets_with_volume) == 0:
        print("❌ NO MARKETS PASS ALL FILTERS!")
        print("\nPossible issues:")
        print("1. Competition field might be using wrong key (check 'competition' vs 'competition_bars')")
        print("2. Volume field might be 0 for all markets")
        print("3. Category field might not match expected values")
        
        # Check field names
        print(f"\n🔍 Checking field names in first market:")
        if markets:
            first_market = markets[0]
            print(f"Available fields: {list(first_market.keys())}")
            print(f"\nField values:")
            for key in ['reward', 'umaReward', 'competition', 'competition_bars', 'category', 'clob_token_ids', 'volume', 'volume_24hr']:
                value = first_market.get(key, 'NOT FOUND')
                print(f"   {key}: {value}")

if __name__ == "__main__":
    asyncio.run(debug_filters())

