"""
Risk Manager Module
Portfolio risk management and hedging
"""

import logging
from typing import List, Dict, Optional, Tuple
import asyncio
from decimal import Decimal
import numpy as np

logger = logging.getLogger(__name__)


class RiskManager:
    """Manages portfolio risk and capital allocation"""
    
    def __init__(self, config: dict):
        self.config = config
        self.total_capital = 10000  # Default capital
        self.allocated_capital = {}
        self.market_exposures = {}
        self.hedging_positions = {}
        self.risk_metrics = {
            'var_95': 0,  # Value at Risk 95%
            'max_drawdown': 0,
            'sharpe_ratio': 0,
            'total_exposure': 0
        }
    
    async def check_market_limit(self, market: Dict) -> bool:
        """Check if market fits within risk limits"""
        try:
            # Get market ID (CLOB API uses 'market_id' or 'condition_id', Gamma API uses 'id')
            market_id = market.get('market_id') or market.get('condition_id') or market.get('id', 'unknown')
            required_capital = self._calculate_required_capital(market)
            
            # Check max capital per market
            max_per_market = self.total_capital * self.config['max_capital_per_market']
            
            if required_capital > max_per_market:
                logger.warning(f"Market {market_id} exceeds capital limit: {required_capital} > {max_per_market}")
                return False
            
            # Check total allocation
            total_allocated = sum(self.allocated_capital.values())
            remaining_capital = self.total_capital - total_allocated
            
            if required_capital > remaining_capital:
                logger.warning(f"Insufficient capital for market {market_id}: {required_capital} > {remaining_capital}")
                return False
            
            # Check correlation limits
            if not self._check_correlation_limits(market):
                logger.warning(f"Market {market_id} exceeds correlation limits")
                return False
            
            return True
            
        except Exception as e:
            logger.error(f"Risk limit check error: {e}")
            return False
    
    def _calculate_required_capital(self, market: Dict) -> float:
        """Calculate capital required for market"""
        # Base on expected order size and price
        avg_price = 0.5  # Assume 50 cents average
        avg_size = (self.config.get('order_management', {}).get('size_min', 200) + 
                   self.config.get('order_management', {}).get('size_max', 500)) / 2
        
        # Both sides (YES and NO)
        required = avg_price * avg_size * 2
        
        # Add buffer for volatility
        volatility_buffer = 1.2
        
        return required * volatility_buffer
    
    def _check_correlation_limits(self, market: Dict) -> bool:
        """Check if market is too correlated with existing positions"""
        category = market.get('category', '')
        
        # Count positions in same category
        category_count = sum(
            1 for m_id, details in self.market_exposures.items()
            if details.get('category') == category
        )
        
        # Max 3 markets per category
        if category_count >= 3:
            return False
        
        # Check title similarity for same event
        market_title = market.get('title', '').lower()
        for m_id, details in self.market_exposures.items():
            existing_title = details.get('title', '').lower()
            
            # Simple similarity check
            common_words = set(market_title.split()) & set(existing_title.split())
            if len(common_words) > 3:  # Too similar
                return False
        
        return True
    
    async def calculate_portfolio_risk(self) -> Dict:
        """Calculate overall portfolio risk metrics"""
        try:
            positions = []
            total_exposure = 0
            
            for market_id, exposure in self.market_exposures.items():
                positions.append(exposure)
                total_exposure += abs(exposure.get('net_exposure', 0))
            
            self.risk_metrics['total_exposure'] = total_exposure
            
            # Calculate Value at Risk (simplified)
            if positions:
                exposures = [p.get('net_exposure', 0) for p in positions]
                if exposures:
                    self.risk_metrics['var_95'] = self._calculate_var(exposures)
            
            # Check if hedging needed
            needs_hedging = self._check_hedging_needed()
            
            return {
                'needs_hedging': needs_hedging,
                'positions': positions,
                'metrics': self.risk_metrics.copy(),
                'total_exposure': total_exposure,
                'exposure_ratio': total_exposure / self.total_capital if self.total_capital > 0 else 0
            }
            
        except Exception as e:
            logger.error(f"Portfolio risk calculation error: {e}")
            return {'needs_hedging': False, 'positions': [], 'metrics': {}}
    
    def _calculate_var(self, exposures: List[float], confidence: float = 0.95) -> float:
        """Calculate Value at Risk"""
        if not exposures:
            return 0
        
        # Simplified VaR calculation
        exposures_array = np.array(exposures)
        
        # Assume normal distribution with historical volatility
        volatility = 0.02  # 2% daily volatility
        mean_exposure = np.mean(exposures_array)
        std_exposure = np.std(exposures_array) if len(exposures) > 1 else mean_exposure * volatility
        
        # Calculate VaR at confidence level
        from scipy import stats
        z_score = stats.norm.ppf(1 - confidence)
        var = mean_exposure + z_score * std_exposure
        
        return abs(var)
    
    def _check_hedging_needed(self) -> bool:
        """Check if portfolio needs hedging"""
        # Check total exposure ratio
        total_exposure = self.risk_metrics.get('total_exposure', 0)
        exposure_ratio = total_exposure / self.total_capital if self.total_capital > 0 else 0
        
        # Need hedging if exposure > 70%
        if exposure_ratio > 0.7:
            return True
        
        # Check for unbalanced positions
        for market_id, exposure in self.market_exposures.items():
            yes_exposure = exposure.get('yes_exposure', 0)
            no_exposure = exposure.get('no_exposure', 0)
            
            imbalance = abs(yes_exposure - no_exposure)
            total = yes_exposure + no_exposure
            
            if total > 0 and imbalance / total > 0.6:  # 60% imbalance
                return True
        
        return False
    
    async def apply_hedging(self, positions: List[Dict]):
        """Apply hedging strategies"""
        try:
            for position in positions:
                market_id = position.get('market_id')
                
                if not market_id:
                    continue
                
                # Check if already hedged
                if market_id in self.hedging_positions:
                    continue
                
                # Calculate hedge requirements
                hedge_params = self._calculate_hedge_params(position)
                
                if hedge_params:
                    # Apply hedge (simplified - would place actual orders)
                    await self._execute_hedge(market_id, hedge_params)
                    
                    self.hedging_positions[market_id] = {
                        'hedge_params': hedge_params,
                        'timestamp': asyncio.get_event_loop().time()
                    }
                    
                    logger.info(f"Applied hedging for market {market_id}")
            
        except Exception as e:
            logger.error(f"Hedging error: {e}")
    
    def _calculate_hedge_params(self, position: Dict) -> Optional[Dict]:
        """Calculate hedging parameters"""
        yes_exposure = position.get('yes_exposure', 0)
        no_exposure = position.get('no_exposure', 0)
        
        # Calculate imbalance
        net_exposure = yes_exposure - no_exposure
        
        if abs(net_exposure) < 100:  # Too small to hedge
            return None
        
        # Determine hedge side and size
        if net_exposure > 0:  # Long YES, need to hedge with NO
            hedge_side = 'no'
            hedge_size = abs(net_exposure) * 0.5  # Partial hedge
        else:  # Long NO, need to hedge with YES
            hedge_side = 'yes'
            hedge_size = abs(net_exposure) * 0.5
        
        return {
            'side': hedge_side,
            'size': hedge_size,
            'type': 'market',  # Use market order for immediate hedge
            'urgency': 'high' if abs(net_exposure) > 500 else 'normal'
        }
    
    async def _execute_hedge(self, market_id: str, hedge_params: Dict):
        """Execute hedging order (simplified)"""
        # This would interact with order_manager to place actual hedge
        logger.info(f"Executing hedge for {market_id}: {hedge_params}")
        
        # Update exposure after hedge
        if market_id in self.market_exposures:
            exposure = self.market_exposures[market_id]
            
            if hedge_params['side'] == 'yes':
                exposure['yes_exposure'] += hedge_params['size']
            else:
                exposure['no_exposure'] += hedge_params['size']
            
            exposure['net_exposure'] = exposure['yes_exposure'] - exposure['no_exposure']
    
    async def rebalance_capital(self):
        """Rebalance capital allocation across markets"""
        try:
            # Calculate current allocations
            total_allocated = sum(self.allocated_capital.values())
            
            if total_allocated > self.total_capital * 0.9:  # Over 90% allocated
                # Need to reduce positions
                await self._reduce_positions()
            
            # Rebalance between markets
            market_count = len(self.allocated_capital)
            if market_count > 0:
                target_per_market = (self.total_capital * 0.8) / market_count
                
                for market_id in list(self.allocated_capital.keys()):
                    current = self.allocated_capital[market_id]
                    
                    if current > target_per_market * 1.5:  # Too concentrated
                        # Reduce position
                        self.allocated_capital[market_id] = target_per_market
                        logger.info(f"Reduced allocation for {market_id}: {current} -> {target_per_market}")
            
        except Exception as e:
            logger.error(f"Rebalancing error: {e}")
    
    async def _reduce_positions(self):
        """Reduce positions when over-allocated"""
        # Sort by performance (would need actual P&L data)
        # For now, reduce oldest positions
        
        if not self.allocated_capital:
            return
        
        # Reduce each position by 20%
        for market_id in self.allocated_capital:
            self.allocated_capital[market_id] *= 0.8
        
        logger.info("Reduced all positions by 20% due to over-allocation")
    
    def update_market_exposure(self, market_id: str, exposure_data: Dict):
        """Update market exposure tracking"""
        self.market_exposures[market_id] = exposure_data
        
        # Update allocated capital
        total_exposure = abs(exposure_data.get('net_exposure', 0))
        self.allocated_capital[market_id] = total_exposure
    
    def get_risk_report(self) -> Dict:
        """Generate risk report"""
        return {
            'total_capital': self.total_capital,
            'allocated_capital': sum(self.allocated_capital.values()),
            'free_capital': self.total_capital - sum(self.allocated_capital.values()),
            'market_count': len(self.market_exposures),
            'hedged_markets': len(self.hedging_positions),
            'risk_metrics': self.risk_metrics.copy(),
            'exposure_summary': self._get_exposure_summary()
        }
    
    def _get_exposure_summary(self) -> Dict:
        """Get summary of exposures by category"""
        summary = {}
        
        for market_id, exposure in self.market_exposures.items():
            category = exposure.get('category', 'other')
            
            if category not in summary:
                summary[category] = {
                    'count': 0,
                    'total_exposure': 0,
                    'net_exposure': 0
                }
            
            summary[category]['count'] += 1
            summary[category]['total_exposure'] += abs(exposure.get('net_exposure', 0))
            summary[category]['net_exposure'] += exposure.get('net_exposure', 0)
        
        return summary
    
    def set_total_capital(self, capital: float):
        """Set total available capital"""
        self.total_capital = capital
        logger.info(f"Total capital set to: ${capital}")