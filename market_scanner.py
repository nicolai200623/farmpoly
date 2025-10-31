"""
Market Scanner Module
Scrapes Polymarket rewards page for opportunities
"""

import asyncio
import aiohttp
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
from typing import List, Dict, Optional
import json
import time

logger = logging.getLogger(__name__)


class MarketScanner:
    """Scans Polymarket for trading opportunities"""
    
    def __init__(self, config: dict):
        self.config = config
        self.base_url = "https://polymarket.com"
        self.rewards_url = f"{self.base_url}/rewards"
        self.driver = None
        self.session = None
        self._setup_driver()
    
    def _setup_driver(self):
        """Setup Selenium driver for dynamic content"""
        try:
            options = Options()
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--disable-gpu')
            options.add_argument('--window-size=1920,1080')
            options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')
            
            self.driver = webdriver.Chrome(options=options)
            logger.info("Selenium driver initialized")
        except Exception as e:
            logger.error(f"Failed to setup driver: {e}")
    
    async def scan_rewards_page(self) -> List[Dict]:
        """Scan rewards page for opportunities"""
        markets = []
        
        try:
            # Use Selenium for dynamic content
            markets_data = await self._scrape_with_selenium()
            
            # Filter based on criteria
            filtered_markets = self._filter_markets(markets_data)
            
            logger.info(f"Found {len(filtered_markets)} qualifying markets")
            return filtered_markets
            
        except Exception as e:
            logger.error(f"Scanning error: {e}")
            return markets
    
    async def _scrape_with_selenium(self) -> List[Dict]:
        """Scrape using Selenium for JavaScript-rendered content"""
        markets = []
        
        try:
            # Load page
            self.driver.get(self.rewards_url)
            
            # Wait for content to load
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, "market-card")))
            
            # Allow dynamic content to render
            await asyncio.sleep(2)
            
            # Parse page source
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            
            # Extract market cards
            market_cards = soup.find_all('div', class_='market-card')
            
            for card in market_cards:
                market = self._extract_market_data(card)
                if market:
                    markets.append(market)
            
            # Also check API endpoint
            api_markets = await self._fetch_api_markets()
            markets.extend(api_markets)
            
            return markets
            
        except Exception as e:
            logger.error(f"Selenium scraping error: {e}")
            return markets
    
    async def _fetch_api_markets(self) -> List[Dict]:
        """Fetch markets from API endpoints"""
        markets = []
        
        try:
            if not self.session:
                self.session = aiohttp.ClientSession()
            
            # Multiple API endpoints to check
            endpoints = [
                "/api/markets?rewards=true",
                "/api/rewards/eligible",
                "/api/markets?sort=reward&order=desc"
            ]
            
            for endpoint in endpoints:
                url = f"{self.base_url}{endpoint}"
                
                async with self.session.get(url) as response:
                    if response.status == 200:
                        data = await response.json()
                        
                        # Parse market data
                        for market_data in data.get('markets', []):
                            market = self._parse_api_market(market_data)
                            if market:
                                markets.append(market)
            
            return markets
            
        except Exception as e:
            logger.error(f"API fetch error: {e}")
            return markets
    
    def _extract_market_data(self, card_element) -> Optional[Dict]:
        """Extract market data from HTML card"""
        try:
            market = {
                'id': card_element.get('data-market-id', ''),
                'title': '',
                'reward': 0,
                'competition_bars': 0,
                'min_shares': 0,
                'volume': 0,
                'liquidity': 0,
                'end_date': '',
                'category': '',
                'yes_price': 0,
                'no_price': 0
            }
            
            # Extract title
            title_elem = card_element.find('h3', class_='market-title')
            if title_elem:
                market['title'] = title_elem.text.strip()
            
            # Extract reward amount
            reward_elem = card_element.find('span', class_='reward-amount')
            if reward_elem:
                reward_text = reward_elem.text.strip().replace('$', '').replace(',', '')
                try:
                    market['reward'] = float(reward_text)
                except:
                    market['reward'] = 0
            
            # Extract competition level (bars)
            comp_elem = card_element.find('div', class_='competition-indicator')
            if comp_elem:
                bars = len(comp_elem.find_all('div', class_='bar-filled'))
                market['competition_bars'] = bars
            
            # Extract minimum shares
            min_shares_elem = card_element.find('span', class_='min-shares')
            if min_shares_elem:
                shares_text = min_shares_elem.text.strip().replace(',', '')
                try:
                    market['min_shares'] = int(shares_text)
                except:
                    market['min_shares'] = 0
            
            # Extract volume
            volume_elem = card_element.find('span', class_='volume')
            if volume_elem:
                volume_text = volume_elem.text.strip().replace('$', '').replace('k', '000').replace('m', '000000')
                try:
                    market['volume'] = float(volume_text)
                except:
                    market['volume'] = 0
            
            # Extract prices
            yes_elem = card_element.find('span', class_='yes-price')
            no_elem = card_element.find('span', class_='no-price')
            
            if yes_elem:
                try:
                    market['yes_price'] = float(yes_elem.text.strip().replace('¢', '')) / 100
                except:
                    market['yes_price'] = 0
            
            if no_elem:
                try:
                    market['no_price'] = float(no_elem.text.strip().replace('¢', '')) / 100
                except:
                    market['no_price'] = 0
            
            # Extract category
            category_elem = card_element.find('span', class_='market-category')
            if category_elem:
                market['category'] = category_elem.text.strip().lower()
            
            return market if market['id'] else None
            
        except Exception as e:
            logger.error(f"Error extracting market data: {e}")
            return None
    
    def _parse_api_market(self, data: dict) -> Optional[Dict]:
        """Parse market data from API response"""
        try:
            market = {
                'id': data.get('id', ''),
                'title': data.get('question', ''),
                'reward': float(data.get('reward', {}).get('amount', 0)),
                'competition_bars': self._calculate_competition(data),
                'min_shares': int(data.get('reward', {}).get('minShares', 0)),
                'volume': float(data.get('volume', 0)),
                'liquidity': float(data.get('liquidity', 0)),
                'end_date': data.get('endDate', ''),
                'category': data.get('category', '').lower(),
                'yes_price': float(data.get('lastPrice', {}).get('yes', 0)),
                'no_price': float(data.get('lastPrice', {}).get('no', 0))
            }
            
            return market if market['id'] else None
            
        except Exception as e:
            logger.error(f"Error parsing API market: {e}")
            return None
    
    def _calculate_competition(self, market_data: dict) -> int:
        """Calculate competition level (0-5 bars)"""
        # Based on number of active traders
        active_traders = market_data.get('activeTraders', 0)
        
        if active_traders < 10:
            return 1
        elif active_traders < 50:
            return 2
        elif active_traders < 100:
            return 3
        elif active_traders < 500:
            return 4
        else:
            return 5
    
    def _filter_markets(self, markets: List[Dict]) -> List[Dict]:
        """Filter markets based on configured criteria"""
        filtered = []
        
        for market in markets:
            # Check reward threshold
            if market['reward'] < self.config['min_reward']:
                continue
            
            # Check competition level
            if market['competition_bars'] > self.config['max_competition_bars']:
                continue
            
            # Check minimum shares requirement
            if market['min_shares'] > self.config['min_shares']:
                continue
            
            # Additional filters for sports/illiquid markets
            if market['category'] in ['sports', 'entertainment', 'crypto']:
                filtered.append(market)
            elif market['liquidity'] < 10000:  # Illiquid markets
                filtered.append(market)
        
        return filtered
    
    async def get_market_details(self, market_id: str) -> Optional[Dict]:
        """Get detailed information about a specific market"""
        try:
            url = f"{self.base_url}/api/markets/{market_id}"
            
            if not self.session:
                self.session = aiohttp.ClientSession()
            
            async with self.session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    return self._parse_api_market(data)
            
            return None
            
        except Exception as e:
            logger.error(f"Error fetching market details: {e}")
            return None
    
    async def close(self):
        """Cleanup resources"""
        if self.driver:
            self.driver.quit()
        
        if self.session:
            await self.session.close()