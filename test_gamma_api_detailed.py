"""
Test Gamma API Response - Chi tiet
Kiem tra xem Gamma API tra ve gi va tai sao bot khong tim thay markets
"""

import asyncio
import aiohttp
import json

async def test_gamma_api():
    """Test Gamma API response"""
    
    api_url = "https://gamma-api.polymarket.com/events"
    
    print("=" * 80)
    print("TESTING GAMMA API - DETAILED ANALYSIS")
    print("=" * 80)
    
    async with aiohttp.ClientSession() as session:
        # Test 1: Fetch events
        print("\n1. FETCHING EVENTS...")
        params = {
            'closed': 'false',
            '_limit': 10,  # Chi lay 10 events de test
        }
        
        async with session.get(api_url, params=params) as response:
            if response.status == 200:
                events = await response.json()
                print(f"   Status: {response.status}")
                print(f"   Total events: {len(events)}")
                
                # Analyze first event
                if events:
                    event = events[0]
                    print(f"\n2. ANALYZING FIRST EVENT:")
                    print(f"   Event ID: {event.get('id')}")
                    print(f"   Event Slug: {event.get('slug')}")
                    print(f"   Markets count: {len(event.get('markets', []))}")
                    
                    # Analyze markets in this event
                    markets = event.get('markets', [])
                    if markets:
                        print(f"\n3. ANALYZING MARKETS IN THIS EVENT:")
                        
                        for i, market in enumerate(markets[:3]):  # Chi xem 3 markets dau
                            print(f"\n   Market {i+1}:")
                            print(f"   - Question: {market.get('question', 'N/A')[:60]}")
                            print(f"   - Market ID: {market.get('id')}")
                            print(f"   - rewardsMinSize: {market.get('rewardsMinSize')}")
                            print(f"   - rewardsMaxSpread: {market.get('rewardsMaxSpread')}")
                            print(f"   - volume: {market.get('volume')}")
                            print(f"   - liquidity: {market.get('liquidity')}")
                            
                            # Check rewards_config
                            rewards_config = market.get('rewards_config', [])
                            if rewards_config:
                                print(f"   - rewards_config: {rewards_config}")
                            
                            # Check if this market would pass our filter
                            rewards_min_size = float(market.get('rewardsMinSize', 0) or 0)
                            rewards_max_spread = float(market.get('rewardsMaxSpread', 0) or 0)
                            
                            if rewards_min_size > 0 and rewards_max_spread > 0:
                                print(f"   ✅ PASS: Has verified rewards")
                            else:
                                print(f"   ❌ REJECT: No verified rewards (minSize={rewards_min_size}, maxSpread={rewards_max_spread})")
                
                # Count total markets with rewards
                print(f"\n4. COUNTING MARKETS WITH REWARDS ACROSS ALL EVENTS:")
                total_markets = 0
                markets_with_rewards = 0
                
                for event in events:
                    for market in event.get('markets', []):
                        total_markets += 1
                        rewards_min_size = float(market.get('rewardsMinSize', 0) or 0)
                        rewards_max_spread = float(market.get('rewardsMaxSpread', 0) or 0)
                        
                        if rewards_min_size > 0 and rewards_max_spread > 0:
                            markets_with_rewards += 1
                
                print(f"   Total markets: {total_markets}")
                print(f"   Markets with rewards: {markets_with_rewards}")
                print(f"   Percentage: {markets_with_rewards/total_markets*100:.1f}%")
                
            else:
                print(f"   ERROR: Status {response.status}")
                text = await response.text()
                print(f"   Response: {text[:200]}")

if __name__ == "__main__":
    asyncio.run(test_gamma_api())

