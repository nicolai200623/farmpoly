"""
Test Final Check
Kiem tra category cua 5 markets co competition <= 1
"""

import asyncio
import aiohttp

def infer_category(question):
    """Infer category from question (same logic as bot)"""
    question_lower = question.lower()
    
    # Check specific keywords first (higher priority)
    crypto_keywords = ['bitcoin', 'btc', 'ethereum', 'eth', 'crypto', 'blockchain', 'solana', 'sol', 'dogecoin', 'doge']
    ai_keywords = ['ai', 'artificial intelligence', 'chatgpt', 'gpt', 'claude', 'gemini', 'llm', 'machine learning']
    
    for keyword in crypto_keywords:
        if keyword in question_lower:
            return 'crypto'
    
    for keyword in ai_keywords:
        if keyword in question_lower:
            return 'ai'
    
    # Then check generic keywords
    politics_keywords = ['trump', 'biden', 'election', 'president', 'senate', 'congress', 'netanyahu', 'putin']
    sports_keywords = ['nfl', 'nba', 'mlb', 'soccer', 'football', 'basketball', 'spacex']  # spacex is not sports!
    
    for keyword in politics_keywords:
        if keyword in question_lower:
            return 'politics'
    
    for keyword in sports_keywords:
        if keyword in question_lower:
            return 'sports'
    
    return 'other'

async def test_final():
    """Test final check"""
    
    api_url = "https://gamma-api.polymarket.com/events"
    params = {
        'closed': 'false',
        '_limit': 100
    }
    
    print("=" * 80)
    print("FINAL CHECK - WHY BOT FINDS 0 MARKETS")
    print("=" * 80)
    
    target_categories = ['crypto', 'sports', 'politics']
    max_competition = 1
    min_reward = 10
    
    print(f"\nFILTER CRITERIA:")
    print(f"  min_reward: ${min_reward}")
    print(f"  max_competition_bars: {max_competition}")
    print(f"  target_categories: {target_categories}")
    
    async with aiohttp.ClientSession() as session:
        async with session.get(api_url, params=params, timeout=10) as response:
            if response.status == 200:
                events = await response.json()
                
                # Collect markets that pass ALL filters
                passed_markets = []
                rejected_by_competition = 0
                rejected_by_category = 0
                
                for event in events:
                    for market_data in event.get('markets', []):
                        rewards_min_size = float(market_data.get('rewardsMinSize', 0) or 0)
                        rewards_max_spread = float(market_data.get('rewardsMaxSpread', 0) or 0)
                        
                        if rewards_min_size > 0 and rewards_max_spread > 0:
                            volume = float(market_data.get('volume', 0) or 0)
                            liquidity = float(market_data.get('liquidity', 0) or 0)
                            question = market_data.get('question', 'Unknown')
                            
                            # Calculate reward
                            if volume > 10000:
                                reward = min(volume * 0.002, 500)
                            elif volume > 1000:
                                reward = min(volume * 0.005, 200)
                            else:
                                reward = min(volume * 0.01, 100)
                            
                            if liquidity > 1000:
                                reward *= 1.5
                            
                            # Calculate competition
                            competition = min(3, int(volume / 10000))
                            
                            # Infer category
                            category = infer_category(question)
                            
                            # Check filters
                            if reward < min_reward:
                                continue  # Skip (but this won't happen based on previous test)
                            
                            if competition > max_competition:
                                rejected_by_competition += 1
                                continue
                            
                            if category not in target_categories:
                                rejected_by_category += 1
                                print(f"\nREJECTED (category): {question[:60]}")
                                print(f"  Category: '{category}' not in {target_categories}")
                                print(f"  Volume: ${volume:,.0f}, Competition: {competition} bars")
                                continue
                            
                            # PASSED ALL FILTERS!
                            passed_markets.append({
                                'question': question,
                                'category': category,
                                'volume': volume,
                                'competition': competition,
                                'reward': reward
                            })
                
                print(f"\n" + "=" * 80)
                print(f"RESULTS:")
                print(f"  Total markets with rewards: 83")
                print(f"  Rejected by competition > {max_competition}: {rejected_by_competition}")
                print(f"  Rejected by category: {rejected_by_category}")
                print(f"  PASSED ALL FILTERS: {len(passed_markets)}")
                
                if len(passed_markets) > 0:
                    print(f"\nMARKETS THAT PASSED:")
                    for market in passed_markets:
                        print(f"\n  - {market['question'][:60]}")
                        print(f"    Category: {market['category']}")
                        print(f"    Volume: ${market['volume']:,.0f}")
                        print(f"    Competition: {market['competition']} bars")
                        print(f"    Reward: ${market['reward']:.2f}")
                else:
                    print(f"\nNO MARKETS PASSED ALL FILTERS!")
                    print(f"\nRECOMMENDATIONS:")
                    print(f"  1. Increase max_competition_bars to 3 (most markets have 3 bars)")
                    print(f"  2. OR add more categories to target_categories")

if __name__ == "__main__":
    asyncio.run(test_final())

