"""
Test API Fetch - Raw
Test truc tiep fetch tu Gamma API va parse
"""

import asyncio
import aiohttp
import yaml

async def test_api_fetch():
    """Test API fetch and parsing"""
    
    # Load config
    with open('config.yaml', 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    
    scanner_config = config['market_scanner']
    
    print("=" * 80)
    print("TESTING API FETCH - RAW")
    print("=" * 80)
    
    print(f"\nCONFIG:")
    print(f"  min_reward: {scanner_config['min_reward']}")
    print(f"  max_competition_bars: {scanner_config['max_competition_bars']}")
    print(f"  target_categories: {scanner_config['target_categories']}")
    
    # Fetch from API
    api_url = "https://gamma-api.polymarket.com/events"
    params = {
        'closed': 'false',
        '_limit': 100
    }
    
    print(f"\nFETCHING FROM API...")
    print(f"  URL: {api_url}")
    print(f"  Params: {params}")
    
    async with aiohttp.ClientSession() as session:
        async with session.get(api_url, params=params, timeout=10) as response:
            if response.status == 200:
                events = await response.json()
                print(f"\n  Status: {response.status}")
                print(f"  Events fetched: {len(events)}")
                
                # Count markets
                total_markets = 0
                markets_with_rewards = 0
                markets_by_category = {}
                markets_by_reward = {}
                
                for event in events:
                    for market_data in event.get('markets', []):
                        total_markets += 1
                        
                        # Check rewards
                        rewards_min_size = float(market_data.get('rewardsMinSize', 0) or 0)
                        rewards_max_spread = float(market_data.get('rewardsMaxSpread', 0) or 0)
                        
                        if rewards_min_size > 0 and rewards_max_spread > 0:
                            markets_with_rewards += 1
                            
                            # Estimate reward (same logic as bot)
                            volume = float(market_data.get('volume', 0) or 0)
                            liquidity = float(market_data.get('liquidity', 0) or 0)
                            
                            # Estimate reward based on volume (rough estimate)
                            if volume > 100000:
                                estimated_reward = 50
                            elif volume > 50000:
                                estimated_reward = 30
                            elif volume > 10000:
                                estimated_reward = 20
                            elif volume > 1000:
                                estimated_reward = 10
                            else:
                                estimated_reward = 5
                            
                            # Count by reward level
                            if estimated_reward >= 10:
                                reward_key = f">= ${estimated_reward}"
                                markets_by_reward[reward_key] = markets_by_reward.get(reward_key, 0) + 1
                            
                            # Infer category (simplified)
                            question = market_data.get('question', '').lower()
                            category = 'other'
                            
                            if any(word in question for word in ['trump', 'biden', 'election', 'president', 'senate', 'congress']):
                                category = 'politics'
                            elif any(word in question for word in ['bitcoin', 'btc', 'eth', 'crypto', 'blockchain']):
                                category = 'crypto'
                            elif any(word in question for word in ['nfl', 'nba', 'mlb', 'soccer', 'football', 'basketball']):
                                category = 'sports'
                            
                            markets_by_category[category] = markets_by_category.get(category, 0) + 1
                
                print(f"\nMARKETS SUMMARY:")
                print(f"  Total markets: {total_markets}")
                print(f"  Markets with rewards: {markets_with_rewards}")
                print(f"  Percentage: {markets_with_rewards/total_markets*100:.1f}%")
                
                print(f"\nMARKETS BY CATEGORY (with rewards):")
                for category, count in sorted(markets_by_category.items(), key=lambda x: x[1], reverse=True):
                    print(f"  {category}: {count}")
                
                print(f"\nMARKETS BY REWARD LEVEL:")
                for reward, count in sorted(markets_by_reward.items(), key=lambda x: x[1], reverse=True):
                    print(f"  {reward}: {count}")
                
                # Check how many would pass filters
                min_reward = scanner_config['min_reward']
                max_competition = scanner_config['max_competition_bars']
                target_categories = scanner_config['target_categories']
                
                print(f"\nFILTER SIMULATION:")
                print(f"  Min reward: ${min_reward}")
                print(f"  Max competition: {max_competition} bars")
                print(f"  Target categories: {target_categories}")
                
                passed = 0
                for category in target_categories:
                    if category in markets_by_category:
                        # Assume all markets in target category have reward >= min_reward
                        # (This is simplified - actual bot checks each market)
                        passed += markets_by_category[category]
                
                print(f"\n  Estimated markets that would pass: {passed}")
                
            else:
                print(f"\n  ERROR: Status {response.status}")

if __name__ == "__main__":
    asyncio.run(test_api_fetch())

