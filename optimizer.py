"""
Daily Optimizer Module
Daily strategy optimization and performance analysis
"""

import logging
import json
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import asyncio

logger = logging.getLogger(__name__)


class DailyOptimizer:
    """Optimizes trading strategy based on daily performance"""
    
    def __init__(self, config: dict):
        self.config = config
        self.performance_history = []
        self.market_statistics = {}
        self.strategy_parameters = config.copy()
        self.optimization_history = []
    
    async def optimize_daily_strategy(self):
        """Run daily optimization routine"""
        try:
            logger.info("Starting daily optimization...")
            
            # Analyze yesterday's performance
            performance = await self._analyze_performance()
            
            # Calculate optimization targets
            optimizations = self._calculate_optimizations(performance)
            
            # Apply optimizations
            await self._apply_optimizations(optimizations)
            
            # Generate and log report
            report = self._generate_optimization_report(performance, optimizations)
            logger.info(f"Optimization complete: {report}")
            
            # Store optimization history
            self.optimization_history.append({
                'date': datetime.utcnow().isoformat(),
                'performance': performance,
                'optimizations': optimizations,
                'report': report
            })
            
            return report
            
        except Exception as e:
            logger.error(f"Daily optimization error: {e}")
            return {}
    
    async def _analyze_performance(self) -> Dict:
        """Analyze previous day's performance"""
        try:
            # Get yesterday's data
            yesterday = datetime.utcnow() - timedelta(days=1)
            
            # Filter performance history
            yesterday_data = [
                p for p in self.performance_history
                if datetime.fromisoformat(p['timestamp']).date() == yesterday.date()
            ]
            
            if not yesterday_data:
                logger.warning("No data available for yesterday")
                return self._default_performance()
            
            # Calculate metrics
            total_orders = len(yesterday_data)
            filled_orders = sum(1 for p in yesterday_data if p['filled'])
            fill_rate = filled_orders / total_orders if total_orders > 0 else 0
            
            # P&L calculation
            total_pnl = sum(p.get('pnl', 0) for p in yesterday_data)
            winning_trades = sum(1 for p in yesterday_data if p.get('pnl', 0) > 0)
            win_rate = winning_trades / filled_orders if filled_orders > 0 else 0
            
            # Market analysis
            market_breakdown = self._analyze_by_market_type(yesterday_data)
            
            # Time analysis
            hourly_performance = self._analyze_by_hour(yesterday_data)
            
            return {
                'date': yesterday.isoformat(),
                'total_orders': total_orders,
                'filled_orders': filled_orders,
                'fill_rate': fill_rate,
                'total_pnl': total_pnl,
                'win_rate': win_rate,
                'market_breakdown': market_breakdown,
                'hourly_performance': hourly_performance,
                'avg_spread': np.mean([p.get('spread', 0.01) for p in yesterday_data]),
                'avg_size': np.mean([p.get('size', 250) for p in yesterday_data])
            }
            
        except Exception as e:
            logger.error(f"Performance analysis error: {e}")
            return self._default_performance()
    
    def _default_performance(self) -> Dict:
        """Return default performance metrics"""
        return {
            'date': datetime.utcnow().isoformat(),
            'total_orders': 0,
            'filled_orders': 0,
            'fill_rate': 0,
            'total_pnl': 0,
            'win_rate': 0,
            'market_breakdown': {},
            'hourly_performance': {},
            'avg_spread': 0.01,
            'avg_size': 250
        }
    
    def _analyze_by_market_type(self, data: List[Dict]) -> Dict:
        """Analyze performance by market category"""
        breakdown = {}
        
        for record in data:
            category = record.get('category', 'unknown')
            
            if category not in breakdown:
                breakdown[category] = {
                    'count': 0,
                    'filled': 0,
                    'pnl': 0,
                    'fill_rate': 0
                }
            
            breakdown[category]['count'] += 1
            if record.get('filled'):
                breakdown[category]['filled'] += 1
            breakdown[category]['pnl'] += record.get('pnl', 0)
        
        # Calculate fill rates
        for category in breakdown:
            if breakdown[category]['count'] > 0:
                breakdown[category]['fill_rate'] = (
                    breakdown[category]['filled'] / breakdown[category]['count']
                )
        
        return breakdown
    
    def _analyze_by_hour(self, data: List[Dict]) -> Dict:
        """Analyze performance by hour of day"""
        hourly = {}
        
        for record in data:
            hour = datetime.fromisoformat(record['timestamp']).hour
            
            if hour not in hourly:
                hourly[hour] = {
                    'orders': 0,
                    'fills': 0,
                    'pnl': 0
                }
            
            hourly[hour]['orders'] += 1
            if record.get('filled'):
                hourly[hour]['fills'] += 1
            hourly[hour]['pnl'] += record.get('pnl', 0)
        
        return hourly
    
    def _calculate_optimizations(self, performance: Dict) -> Dict:
        """Calculate strategy optimizations based on performance"""
        optimizations = {}
        
        # Spread optimization
        if performance['fill_rate'] < 0.3:  # Low fill rate
            # Tighten spreads
            optimizations['spread_adjustment'] = -0.002  # Reduce by 0.2 cents
        elif performance['fill_rate'] > 0.7:  # High fill rate
            # Widen spreads for better profit
            optimizations['spread_adjustment'] = 0.001  # Increase by 0.1 cents
        else:
            optimizations['spread_adjustment'] = 0
        
        # Size optimization
        if performance['win_rate'] > 0.6:  # Good win rate
            # Increase position sizes
            optimizations['size_multiplier'] = 1.1
        elif performance['win_rate'] < 0.4:  # Poor win rate
            # Reduce position sizes
            optimizations['size_multiplier'] = 0.9
        else:
            optimizations['size_multiplier'] = 1.0
        
        # Market selection optimization
        market_scores = {}
        for category, stats in performance['market_breakdown'].items():
            # Score based on fill rate and P&L
            score = stats['fill_rate'] * 0.5 + (stats['pnl'] / 1000) * 0.5
            market_scores[category] = score
        
        # Identify best and worst performing categories
        if market_scores:
            best_category = max(market_scores, key=market_scores.get)
            worst_category = min(market_scores, key=market_scores.get)
            
            optimizations['preferred_categories'] = [best_category]
            optimizations['avoid_categories'] = [worst_category] if market_scores[worst_category] < 0 else []
        
        # Time-based optimization
        best_hours = []
        worst_hours = []
        
        for hour, stats in performance['hourly_performance'].items():
            if stats['orders'] > 5:  # Minimum sample size
                hourly_pnl = stats['pnl'] / stats['orders']
                if hourly_pnl > 10:  # Good hourly P&L
                    best_hours.append(hour)
                elif hourly_pnl < -5:  # Poor hourly P&L
                    worst_hours.append(hour)
        
        optimizations['best_trading_hours'] = best_hours
        optimizations['avoid_hours'] = worst_hours
        
        # Risk management optimization
        if performance['total_pnl'] < -500:  # Significant loss
            optimizations['risk_reduction'] = 0.5  # Reduce risk by 50%
        elif performance['total_pnl'] > 1000:  # Good profit
            optimizations['risk_increase'] = 1.2  # Increase risk by 20%
        else:
            optimizations['risk_adjustment'] = 1.0
        
        return optimizations
    
    async def _apply_optimizations(self, optimizations: Dict):
        """Apply calculated optimizations to strategy"""
        try:
            # Update spread parameters
            if 'spread_adjustment' in optimizations:
                adj = optimizations['spread_adjustment']
                self.strategy_parameters['order_management']['spread_min'] += adj
                self.strategy_parameters['order_management']['spread_max'] += adj
                
                # Keep within bounds
                self.strategy_parameters['order_management']['spread_min'] = max(
                    0.005, self.strategy_parameters['order_management']['spread_min']
                )
                self.strategy_parameters['order_management']['spread_max'] = min(
                    0.02, self.strategy_parameters['order_management']['spread_max']
                )
            
            # Update size parameters
            if 'size_multiplier' in optimizations:
                mult = optimizations['size_multiplier']
                self.strategy_parameters['order_management']['size_min'] = int(
                    self.strategy_parameters['order_management']['size_min'] * mult
                )
                self.strategy_parameters['order_management']['size_max'] = int(
                    self.strategy_parameters['order_management']['size_max'] * mult
                )
            
            # Update market preferences
            if 'preferred_categories' in optimizations:
                self.strategy_parameters['market_preferences'] = optimizations['preferred_categories']
            
            if 'avoid_categories' in optimizations:
                self.strategy_parameters['market_blacklist'] = optimizations['avoid_categories']
            
            # Update trading hours
            if 'best_trading_hours' in optimizations:
                self.strategy_parameters['active_hours'] = optimizations['best_trading_hours']
            
            # Update risk parameters
            if 'risk_reduction' in optimizations:
                self.strategy_parameters['risk_management']['max_capital_per_market'] *= optimizations['risk_reduction']
            elif 'risk_increase' in optimizations:
                self.strategy_parameters['risk_management']['max_capital_per_market'] *= optimizations.get('risk_increase', 1.0)
            
            logger.info(f"Applied optimizations: {optimizations}")
            
        except Exception as e:
            logger.error(f"Error applying optimizations: {e}")
    
    def _generate_optimization_report(self, performance: Dict, optimizations: Dict) -> Dict:
        """Generate optimization report"""
        report = {
            'timestamp': datetime.utcnow().isoformat(),
            'performance_summary': {
                'fill_rate': f"{performance['fill_rate']:.1%}",
                'win_rate': f"{performance['win_rate']:.1%}",
                'total_pnl': f"${performance['total_pnl']:.2f}",
                'orders': performance['total_orders']
            },
            'optimizations_applied': optimizations,
            'new_parameters': {
                'spread_range': f"{self.strategy_parameters['order_management']['spread_min']:.3f} - {self.strategy_parameters['order_management']['spread_max']:.3f}",
                'size_range': f"{self.strategy_parameters['order_management']['size_min']} - {self.strategy_parameters['order_management']['size_max']}",
                'max_capital_per_market': f"{self.strategy_parameters['risk_management']['max_capital_per_market']:.1%}"
            }
        }
        
        return report
    
    async def calculate_daily_pnl(self) -> float:
        """Calculate daily P&L"""
        try:
            today = datetime.utcnow().date()
            
            today_data = [
                p for p in self.performance_history
                if datetime.fromisoformat(p['timestamp']).date() == today
            ]
            
            return sum(p.get('pnl', 0) for p in today_data)
            
        except Exception as e:
            logger.error(f"P&L calculation error: {e}")
            return 0.0
    
    def add_performance_record(self, record: Dict):
        """Add performance record"""
        record['timestamp'] = datetime.utcnow().isoformat()
        self.performance_history.append(record)
        
        # Keep last 30 days
        cutoff = datetime.utcnow() - timedelta(days=30)
        self.performance_history = [
            p for p in self.performance_history
            if datetime.fromisoformat(p['timestamp']) > cutoff
        ]
    
    def get_strategy_parameters(self) -> Dict:
        """Get current strategy parameters"""
        return self.strategy_parameters.copy()
    
    def get_optimization_stats(self) -> Dict:
        """Get optimization statistics"""
        return {
            'total_optimizations': len(self.optimization_history),
            'performance_records': len(self.performance_history),
            'current_parameters': self.strategy_parameters,
            'last_optimization': self.optimization_history[-1] if self.optimization_history else None
        }