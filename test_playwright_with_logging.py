"""
Test Playwright Rewards Scraper with detailed logging
"""
import asyncio
import logging
import sys
sys.path.insert(0, '.')

from playwright_rewards_scraper import PlaywrightRewardsScraper

# Enable detailed logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

async def main():
    scraper = PlaywrightRewardsScraper()
    
    print("Testing Playwright Rewards Scraper with detailed logging...")
    print("This will scrape markets from https://polymarket.com/rewards")
    print("May take 2-3 minutes...\n")
    
    try:
        await scraper.initialize()
        markets = await scraper.scrape_rewards_page()
        
        print(f"\n{'='*80}")
        print(f"FINAL RESULTS")
        print(f"{'='*80}")
        print(f"Total unique markets scraped: {len(markets)}")
        
        if markets:
            # Show reward distribution
            rewards = [m['reward'] for m in markets]
            print(f"\nReward stats:")
            print(f"  Min: ${min(rewards)}")
            print(f"  Max: ${max(rewards)}")
            print(f"  Average: ${sum(rewards)/len(rewards):.2f}")
        
    finally:
        await scraper.close()

if __name__ == "__main__":
    asyncio.run(main())

