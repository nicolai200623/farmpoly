"""
Market Selector AI Module
Intelligent market selection using scoring algorithms
"""

import numpy as np
import pandas as pd
from typing import List, Dict, Tuple
import logging
from datetime import datetime, timedelta
import asyncio

logger = logging.getLogger(__name__)


class MarketSelectorAI:
    """AI-powered market selection and scoring"""
    
    def __init__(self, config: dict):
        self.config = config
        self.historical_data = []
        self.volume_baselines = {}
        self.market_performance = {}
        self.selection_threshold = 0.7  # Minimum score to select
    
    async def select_markets(self, markets: List[Dict]) -> List[Dict]:
        """Select best markets using AI scoring"""
        try:
            # Calculate scores for all markets
            scored_markets = []
            
            for market in markets:
                score = await self._calculate_market_score(market)
                market['ai_score'] = score
                
                if score >= self.selection_threshold:
                    scored_markets.append(market)
            
            # Sort by score (highest first)
            scored_markets.sort(key=lambda x: x['ai_score'], reverse=True)
            
            # Apply portfolio limits
            selected = self._apply_portfolio_constraints(scored_markets)
            
            logger.info(f"Selected {len(selected)} markets from {len(markets)} candidates")
            
            return selected
            
        except Exception as e:
            logger.error(f"Market selection error: {e}")
            return []
    
    async def _calculate_market_score(self, market: Dict) -> float:
        """Calculate comprehensive market score"""
        try:
            # Base score components
            reward_score = self._score_reward(market['reward'])
            competition_score = self._score_competition(market['competition_bars'])
            volume_spike_score = await self._score_volume_spike(market)
            liquidity_score = self._score_liquidity(market.get('liquidity', 0))
            category_score = self._score_category(market.get('category', 'other'))  # Default to 'other' if missing
            price_score = self._score_price_efficiency(market)
            timing_score = self._score_timing(market)
            
            # Weighted combination
            weights = {
                'reward': 0.25,
                'competition': 0.20,
                'volume_spike': 0.15,
                'liquidity': 0.10,
                'category': 0.10,
                'price': 0.10,
                'timing': 0.10
            }
            
            total_score = (
                weights['reward'] * reward_score +
                weights['competition'] * competition_score +
                weights['volume_spike'] * volume_spike_score +
                weights['liquidity'] * liquidity_score +
                weights['category'] * category_score +
                weights['price'] * price_score +
                weights['timing'] * timing_score
            )
            
            # Apply special conditions
            if market.get('category') == 'sports':
                total_score *= 1.2  # 20% boost for sports
            
            if market.get('liquidity', 0) < 5000:
                total_score *= 1.15  # 15% boost for illiquid markets
            
            return min(total_score, 1.0)  # Cap at 1.0
            
        except Exception as e:
            logger.error(f"Score calculation error: {e}")
            return 0.0
    
    def _score_reward(self, reward: float) -> float:
        """Score based on reward amount"""
        if reward >= 1000:
            return 1.0
        elif reward >= 500:
            return 0.8
        elif reward >= 300:
            return 0.6
        else:
            return 0.3
    
    def _score_competition(self, bars: int) -> float:
        """Score based on competition level (inverse)"""
        competition_scores = {
            1: 1.0,   # Very low competition
            2: 0.8,   # Low competition
            3: 0.5,   # Medium competition
            4: 0.2,   # High competition
            5: 0.1    # Very high competition
        }
        return competition_scores.get(bars, 0.1)
    
    async def _score_volume_spike(self, market: Dict) -> float:
        """Score based on volume spike detection"""
        try:
            market_id = market['id']
            current_volume = market['volume']
            
            # Get baseline volume
            if market_id not in self.volume_baselines:
                # Initialize with current volume
                self.volume_baselines[market_id] = current_volume
                return 0.5  # Neutral score for new markets
            
            baseline = self.volume_baselines[market_id]
            
            if baseline == 0:
                return 0.5
            
            # Calculate spike ratio
            spike_ratio = current_volume / baseline
            
            # Update baseline (exponential moving average)
            alpha = 0.1
            self.volume_baselines[market_id] = alpha * current_volume + (1 - alpha) * baseline
            
            # Score based on spike
            if spike_ratio > 3:
                return 0.2  # Too much spike - likely already discovered
            elif spike_ratio > 2:
                return 0.4  # High spike - be cautious
            elif spike_ratio > 1.5:
                return 0.6  # Moderate spike
            elif spike_ratio > 1.2:
                return 0.8  # Small spike - good opportunity
            else:
                return 1.0  # No spike - best opportunity
                
        except Exception as e:
            logger.error(f"Volume spike scoring error: {e}")
            return 0.5
    
    def _score_liquidity(self, liquidity: float) -> float:
        """Score based on liquidity (prefer illiquid)"""
        if liquidity < 1000:
            return 1.0  # Very illiquid - best
        elif liquidity < 5000:
            return 0.8  # Illiquid - good
        elif liquidity < 10000:
            return 0.6  # Semi-liquid
        elif liquidity < 50000:
            return 0.4  # Liquid
        else:
            return 0.2  # Very liquid - worst for our strategy
    
    def _score_category(self, category: str) -> float:
        """Score based on market category"""
        category_scores = {
            'sports': 1.0,        # Best - predictable patterns
            'entertainment': 0.9,  # Very good
            'crypto': 0.8,        # Good volatility
            'politics': 0.6,      # Medium
            'economics': 0.5,     # Okay
            'science': 0.4,       # Lower priority
            'other': 0.3          # Lowest priority
        }
        return category_scores.get(category.lower(), 0.3)
    
    def _score_price_efficiency(self, market: Dict) -> float:
        """Score based on price efficiency (distance from 50/50)"""
        yes_price = market.get('yes_price', 0)
        no_price = market.get('no_price', 0)
        
        if yes_price == 0 or no_price == 0:
            return 0.5
        
        # Calculate price sum (should be close to 1.0 for efficient markets)
        price_sum = yes_price + no_price
        
        # Distance from perfect efficiency
        efficiency_distance = abs(1.0 - price_sum)
        
        # Prefer slightly inefficient markets
        if efficiency_distance < 0.02:
            return 0.3  # Too efficient
        elif efficiency_distance < 0.05:
            return 0.7  # Good inefficiency
        elif efficiency_distance < 0.10:
            return 1.0  # Best - exploitable inefficiency
        else:
            return 0.5  # Too inefficient - might be broken
    
    def _score_timing(self, market: Dict) -> float:
        """Score based on market timing (time to expiry)"""
        try:
            if not market.get('end_date'):
                return 0.5
            
            # Parse end date
            end_date = datetime.fromisoformat(market['end_date'].replace('Z', '+00:00'))
            now = datetime.utcnow()
            
            # Calculate days to expiry
            days_to_expiry = (end_date - now).days
            
            # Score based on time remaining
            if days_to_expiry < 1:
                return 0.2  # Too close to expiry
            elif days_to_expiry < 3:
                return 0.8  # Good - quick resolution
            elif days_to_expiry < 7:
                return 1.0  # Best - optimal timeframe
            elif days_to_expiry < 30:
                return 0.7  # Good
            else:
                return 0.4  # Too far out
                
        except Exception as e:
            logger.error(f"Timing score error: {e}")
            return 0.5
    
    def _apply_portfolio_constraints(self, markets: List[Dict]) -> List[Dict]:
        """Apply portfolio-level constraints"""
        selected = []
        category_counts = {}
        max_per_category = 3
        max_total = 10
        
        for market in markets:
            # Check total limit
            if len(selected) >= max_total:
                break
            
            # Check category limit
            category = market.get('category', 'other')
            if category_counts.get(category, 0) >= max_per_category:
                continue

            # Check correlation with existing selections
            if self._is_correlated(market, selected):
                continue

            selected.append(market)
            category_counts[category] = category_counts.get(category, 0) + 1
        
        return selected
    
    def _is_correlated(self, market: Dict, selected: List[Dict]) -> bool:
        """Check if market is correlated with already selected markets"""
        for selected_market in selected:
            # Check title similarity
            if self._similarity_score(market['title'], selected_market['title']) > 0.7:
                return True
            
            # Check if same event/topic
            if market.get('event_id') and market.get('event_id') == selected_market.get('event_id'):
                return True
        
        return False
    
    def _similarity_score(self, text1: str, text2: str) -> float:
        """Calculate text similarity score"""
        # Simple word overlap for now
        words1 = set(text1.lower().split())
        words2 = set(text2.lower().split())
        
        if not words1 or not words2:
            return 0.0
        
        intersection = words1.intersection(words2)
        union = words1.union(words2)
        
        return len(intersection) / len(union)
    
    def update_performance(self, market_id: str, performance: Dict):
        """Update market performance history for learning"""
        self.market_performance[market_id] = performance
        
        # Store for future model training
        self.historical_data.append({
            'market_id': market_id,
            'timestamp': datetime.utcnow(),
            'performance': performance
        })
    
    def get_selection_stats(self) -> Dict:
        """Get statistics about market selection"""
        return {
            'total_markets_analyzed': len(self.historical_data),
            'average_score_threshold': self.selection_threshold,
            'category_preferences': self._get_category_stats(),
            'volume_baselines': len(self.volume_baselines)
        }
    
    def _get_category_stats(self) -> Dict:
        """Get category-wise statistics"""
        stats = {}
        for data in self.historical_data:
            category = data.get('category', 'unknown')
            if category not in stats:
                stats[category] = {'count': 0, 'avg_performance': 0}
            stats[category]['count'] += 1
        
        return stats