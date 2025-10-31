"""
Market Scanner V2 - Upgraded with Playwright + Gamma API
Replaces fragile Selenium scraper with robust multi-source approach
"""

import asyncio
import aiohttp
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeout
import logging
from typing import List, Dict, Optional
import json
import time

logger = logging.getLogger(__name__)


class MarketScannerV2:
    """Enhanced market scanner with Playwright and API fallback"""
    
    def __init__(self, config: dict):
        self.config = config
        self.rewards_url = "https://gamma.polymarket.com/?show=rewards"
        self.api_url = "https://gamma-api.polymarket.com/markets"
        self.min_reward = config.get('min_reward', 300)
        self.max_competition = config.get('max_competition_bars', 2)
        self.browser = None
        self.context = None
        
    async def initialize(self):
        """Initialize Playwright browser"""
        try:
            playwright = await async_playwright().start()
            self.browser = await playwright.chromium.launch(
                headless=True,
                args=['--disable-blink-features=AutomationControlled']
            )
            self.context = await self.browser.new_context(
                viewport={'width': 1920, 'height': 1080},
                user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            )
            logger.info("✅ Playwright browser initialized")
        except Exception as e:
            logger.error(f"❌ Failed to initialize Playwright: {e}")
    
    async def close(self):
        """Close browser"""
        if self.browser:
            await self.browser.close()
    
    async def scan_rewards_page(self) -> List[Dict]:
        """Scan rewards page using multiple sources"""
        markets = []
        
        try:
            # Method 1: Try Gamma API first (fastest and most reliable)
            logger.info("🔍 Fetching from Gamma API...")
            api_markets = await self._fetch_gamma_api()
            
            if api_markets:
                markets.extend(api_markets)
                logger.info(f"✅ Got {len(api_markets)} markets from API")
            
            # Method 2: Fallback to Playwright scraping if API fails
            if not markets:
                logger.info("🔍 Falling back to Playwright scraping...")
                scraped_markets = await self._scrape_with_playwright()
                markets.extend(scraped_markets)
            
            # Filter based on criteria
            filtered_markets = self._filter_markets(markets)
            
            logger.info(f"✅ Found {len(filtered_markets)} qualifying markets (from {len(markets)} total)")
            return filtered_markets
            
        except Exception as e:
            logger.error(f"❌ Scanning error: {e}")
            return []
    
    async def _fetch_gamma_api(self) -> List[Dict]:
        """Fetch markets from Gamma API"""
        markets = []
        
        try:
            async with aiohttp.ClientSession() as session:
                # Try rewards endpoint
                params = {
                    'reward': 'true',
                    'active': 'true',
                    'limit': 100
                }
                
                async with session.get(self.api_url, params=params, timeout=10) as response:
                    if response.status == 200:
                        data = await response.json()
                        
                        # Parse API response
                        if isinstance(data, list):
                            for item in data:
                                market = self._parse_api_market(item)
                                if market:
                                    markets.append(market)
                        elif isinstance(data, dict) and 'data' in data:
                            for item in data['data']:
                                market = self._parse_api_market(item)
                                if market:
                                    markets.append(market)
                    else:
                        logger.warning(f"⚠️  API returned status {response.status}")
                        
        except Exception as e:
            logger.warning(f"⚠️  API fetch failed: {e}")
        
        return markets
    
    def _parse_api_market(self, item: dict) -> Optional[Dict]:
        """Parse market data from API response"""
        try:
            # Extract reward info
            reward_info = item.get('rewards', {}) or item.get('reward', {})
            
            if not reward_info:
                return None
            
            # Calculate reward amount
            reward = 0
            if isinstance(reward_info, dict):
                reward = float(reward_info.get('amount', 0) or reward_info.get('total', 0))
            elif isinstance(reward_info, (int, float)):
                reward = float(reward_info)
            
            # Get competition level
            competition = item.get('competition_bars', 0) or item.get('competition', 0)
            
            # Get minimum shares
            min_shares = item.get('min_shares', 0) or item.get('minimum_shares', 0)
            
            market = {
                'id': item.get('id') or item.get('market_id'),
                'question': item.get('question') or item.get('title', 'Unknown'),
                'reward': reward,
                'competition_bars': competition,
                'min_shares': min_shares,
                'volume': float(item.get('volume', 0)),
                'liquidity': float(item.get('liquidity', 0)),
                'end_date': item.get('end_date') or item.get('end_time'),
                'source': 'gamma_api'
            }
            
            return market
            
        except Exception as e:
            logger.debug(f"Failed to parse API market: {e}")
            return None
    
    async def _scrape_with_playwright(self) -> List[Dict]:
        """Scrape using Playwright for JavaScript-rendered content"""
        markets = []
        
        if not self.context:
            await self.initialize()
        
        try:
            page = await self.context.new_page()
            
            # Navigate to rewards page
            await page.goto(self.rewards_url, wait_until='networkidle', timeout=30000)
            
            # Wait for market cards to load
            try:
                await page.wait_for_selector('[data-testid="market-card"], .market-card, .reward-card', 
                                            timeout=10000)
            except PlaywrightTimeout:
                logger.warning("⚠️  Timeout waiting for market cards")
            
            # Extract market data using JavaScript
            markets_data = await page.evaluate('''
                () => {
                    const cards = document.querySelectorAll('[data-testid="market-card"], .market-card, .reward-card');
                    return Array.from(cards).map(card => {
                        // Try multiple selectors for reward amount
                        const rewardEl = card.querySelector('.reward-amount, [data-testid="reward"], .reward');
                        const reward = rewardEl ? parseFloat(rewardEl.textContent.replace(/[^0-9.]/g, '')) : 0;
                        
                        // Competition bars
                        const bars = card.querySelectorAll('.bar-filled, .competition-bar.filled, [data-filled="true"]');
                        const competition = bars.length;
                        
                        // Minimum shares
                        const sharesEl = card.querySelector('.min-shares, [data-testid="min-shares"]');
                        const minShares = sharesEl ? parseInt(sharesEl.textContent.replace(/[^0-9]/g, '')) : 0;
                        
                        // Question/title
                        const titleEl = card.querySelector('.market-title, h3, h4, [data-testid="title"]');
                        const question = titleEl ? titleEl.textContent.trim() : 'Unknown';
                        
                        // Market ID (from link or data attribute)
                        const linkEl = card.querySelector('a[href*="/market/"]');
                        const marketId = linkEl ? linkEl.href.split('/market/')[1].split('?')[0] : null;
                        
                        return {
                            id: marketId,
                            question: question,
                            reward: reward,
                            competition_bars: competition,
                            min_shares: minShares
                        };
                    }).filter(m => m.id && m.reward > 0);
                }
            ''')
            
            # Convert to market objects
            for data in markets_data:
                market = {
                    'id': data['id'],
                    'question': data['question'],
                    'reward': data['reward'],
                    'competition_bars': data['competition_bars'],
                    'min_shares': data['min_shares'],
                    'volume': 0,
                    'liquidity': 0,
                    'end_date': None,
                    'source': 'playwright'
                }
                markets.append(market)
            
            await page.close()
            
        except Exception as e:
            logger.error(f"❌ Playwright scraping error: {e}")
        
        return markets
    
    def _filter_markets(self, markets: List[Dict]) -> List[Dict]:
        """Filter markets based on criteria"""
        filtered = []
        
        for market in markets:
            # Check reward threshold
            if market['reward'] < self.min_reward:
                continue
            
            # Check competition level
            if market['competition_bars'] > self.max_competition:
                continue
            
            # Add score for ranking
            market['score'] = self._calculate_score(market)
            
            filtered.append(market)
        
        # Sort by score (highest first)
        filtered.sort(key=lambda x: x['score'], reverse=True)
        
        return filtered
    
    def _calculate_score(self, market: Dict) -> float:
        """Calculate market opportunity score"""
        score = 0.0
        
        # Reward contribution (higher is better)
        score += market['reward'] * 0.5
        
        # Competition penalty (lower is better)
        score -= market['competition_bars'] * 100
        
        # Volume bonus (if available)
        if market.get('volume', 0) > 0:
            score += min(market['volume'] / 10000, 50)
        
        # Liquidity bonus (if available)
        if market.get('liquidity', 0) > 0:
            score += min(market['liquidity'] / 5000, 30)
        
        return score


# Backward compatibility - alias to new scanner
MarketScanner = MarketScannerV2

