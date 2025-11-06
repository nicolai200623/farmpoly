"""
Test Playwright Rewards Scraper
"""
import asyncio
import sys
sys.path.insert(0, '.')

from playwright_rewards_scraper import PlaywrightRewardsScraper

async def main():
    scraper = PlaywrightRewardsScraper()
    
    print("Testing Playwright Rewards Scraper...")
    print("This will scrape markets from https://polymarket.com/rewards")
    print("May take 1-2 minutes...\n")
    
    try:
        await scraper.initialize()
        markets = await scraper.scrape_rewards_page()
        
        print(f"\n{'='*80}")
        print(f"RESULTS")
        print(f"{'='*80}")
        print(f"Total markets scraped: {len(markets)}")
        
        if markets:
            print(f"\nFirst 10 markets:")
            for i, market in enumerate(markets[:10], 1):
                print(f"\n{i}. {market['question'][:70]}")
                print(f"   Reward: ${market['reward']}")
                print(f"   Competition: {market['competition_bars']} bars")
                print(f"   Volume 24h: ${market['volume_24hr']:.0f}")
            
            # Check if specific markets are in the results
            print(f"\n{'='*80}")
            print(f"CHECKING SPECIFIC MARKETS")
            print(f"{'='*80}\n")
            
            search_terms = [
                "Atlanta Hawks make the NBA Playoffs",
                "Los Angeles Clippers win the 2025",
                "Supreme Court rules in favor of Trump's tariffs",
                "Netflix dip to $1050"
            ]
            
            for term in search_terms:
                found = False
                for market in markets:
                    if term.lower() in market['question'].lower():
                        print(f"❌ FOUND (should NOT be here): {market['question'][:70]}")
                        print(f"   Reward: ${market['reward']}")
                        found = True
                        break
                
                if not found:
                    print(f"✅ NOT FOUND (correct!): {term}")
        
    finally:
        await scraper.close()

if __name__ == "__main__":
    asyncio.run(main())

