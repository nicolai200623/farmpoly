"""
Position Monitor Module
Real-time position monitoring with WebSocket
"""

import asyncio
import websockets
import json
import logging
from typing import List, Dict, Optional
import time
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)


class PositionMonitor:
    """Monitor positions and market conditions in real-time"""
    
    def __init__(self, config: dict):
        self.config = config
        self.ws_connection = None
        self.positions = {}
        self.market_conditions = {}
        self.volume_baseline = {}
        self.price_history = {}
        self.ws_url = "wss://clob.polymarket.com/ws"
    
    async def connect_websocket(self):
        """Connect to CLOB WebSocket"""
        try:
            self.ws_connection = await websockets.connect(self.ws_url)
            logger.info("Connected to CLOB WebSocket")
            
            # Subscribe to relevant channels
            await self._subscribe_to_channels()
            
        except Exception as e:
            logger.error(f"WebSocket connection error: {e}")
            await asyncio.sleep(5)
            await self.connect_websocket()  # Retry
    
    async def _subscribe_to_channels(self):
        """Subscribe to market data channels"""
        try:
            # Subscribe to order updates
            subscribe_msg = {
                "type": "subscribe",
                "channels": ["orders", "fills", "market_data"]
            }
            
            await self.ws_connection.send(json.dumps(subscribe_msg))
            logger.info("Subscribed to WebSocket channels")
            
        except Exception as e:
            logger.error(f"Subscription error: {e}")
    
    async def get_open_positions(self) -> List[Dict]:
        """Get all open positions"""
        open_positions = []
        
        for market_id, position in self.positions.items():
            if position['status'] == 'open':
                # Add current market conditions
                position['current_conditions'] = self.market_conditions.get(market_id, {})
                open_positions.append(position)
        
        return open_positions
    
    async def check_cancel_conditions(self, position: Dict) -> bool:
        """Check if position should be cancelled based on conditions"""
        try:
            market_id = position['market_id']
            
            # Check partial fill condition
            if await self._check_partial_fill(position):
                logger.info(f"Partial fill threshold exceeded for {market_id}")
                return True
            
            # Check volume spike
            if await self._check_volume_spike(market_id):
                logger.info(f"Volume spike detected for {market_id}")
                return True
            
            # Check price movement
            if await self._check_price_movement(market_id):
                logger.info(f"Significant price movement for {market_id}")
                return True
            
            # Check time-based conditions
            if self._check_time_conditions(position):
                logger.info(f"Time threshold exceeded for {market_id}")
                return True
            
            return False
            
        except Exception as e:
            logger.error(f"Error checking cancel conditions: {e}")
            return False
    
    async def _check_partial_fill(self, position: Dict) -> bool:
        """Check if partial fill exceeds threshold"""
        if 'fill_percentage' not in position:
            return False
        
        threshold = self.config['partial_fill_threshold']
        fill_pct = position['fill_percentage']
        
        # If partially filled but not enough
        if 0 < fill_pct < 1.0 and fill_pct > threshold:
            return True
        
        return False
    
    async def _check_volume_spike(self, market_id: str) -> bool:
        """Check for volume spike"""
        try:
            current_conditions = self.market_conditions.get(market_id, {})
            current_volume = current_conditions.get('volume', 0)
            
            # Initialize baseline if not exists
            if market_id not in self.volume_baseline:
                self.volume_baseline[market_id] = current_volume
                return False
            
            baseline = self.volume_baseline[market_id]
            if baseline == 0:
                return False
            
            # Check spike multiplier
            spike_ratio = current_volume / baseline
            multiplier = self.config['volume_spike_multiplier']
            
            if spike_ratio > multiplier:
                # Update baseline for next check
                self.volume_baseline[market_id] = current_volume * 0.5 + baseline * 0.5
                return True
            
            # Update baseline (exponential moving average)
            alpha = 0.1
            self.volume_baseline[market_id] = alpha * current_volume + (1 - alpha) * baseline
            
            return False
            
        except Exception as e:
            logger.error(f"Volume spike check error: {e}")
            return False
    
    async def _check_price_movement(self, market_id: str) -> bool:
        """Check for significant price movement"""
        try:
            current_conditions = self.market_conditions.get(market_id, {})
            current_price = current_conditions.get('mid_price', 0)
            
            # Initialize price history if not exists
            if market_id not in self.price_history:
                self.price_history[market_id] = [current_price]
                return False
            
            history = self.price_history[market_id]
            
            # Keep last 10 prices
            history.append(current_price)
            if len(history) > 10:
                history.pop(0)
            
            # Check price movement from entry
            entry_price = history[0]
            if entry_price == 0:
                return False
            
            price_change = abs(current_price - entry_price)
            threshold = self.config['price_move_threshold']
            
            return price_change > threshold
            
        except Exception as e:
            logger.error(f"Price movement check error: {e}")
            return False
    
    def _check_time_conditions(self, position: Dict) -> bool:
        """Check time-based cancel conditions"""
        try:
            # Check if order is too old
            if 'created_at' in position:
                age_seconds = time.time() - position['created_at']
                max_age = 300  # 5 minutes
                
                if age_seconds > max_age:
                    return True
            
            # Check if close to market end
            if 'end_date' in position:
                end_date = datetime.fromisoformat(position['end_date'].replace('Z', '+00:00'))
                time_to_end = (end_date - datetime.utcnow()).total_seconds()
                
                # Cancel if less than 30 minutes to end
                if time_to_end < 1800:
                    return True
            
            return False
            
        except Exception as e:
            logger.error(f"Time condition check error: {e}")
            return False
    
    async def update_position(self, market_id: str, update_data: Dict):
        """Update position data"""
        if market_id not in self.positions:
            self.positions[market_id] = {
                'market_id': market_id,
                'status': 'open',
                'created_at': time.time()
            }
        
        self.positions[market_id].update(update_data)
    
    async def update_market_conditions(self, market_id: str, conditions: Dict):
        """Update market conditions"""
        self.market_conditions[market_id] = conditions
    
    async def listen_to_updates(self):
        """Listen to WebSocket updates"""
        if not self.ws_connection:
            await self.connect_websocket()
        
        try:
            async for message in self.ws_connection:
                data = json.loads(message)
                await self._process_ws_message(data)
                
        except Exception as e:
            logger.error(f"WebSocket listening error: {e}")
            await self.connect_websocket()
    
    async def _process_ws_message(self, data: Dict):
        """Process WebSocket message"""
        try:
            msg_type = data.get('type')
            
            if msg_type == 'order_update':
                await self._handle_order_update(data)
            elif msg_type == 'fill':
                await self._handle_fill(data)
            elif msg_type == 'market_data':
                await self._handle_market_data(data)
            elif msg_type == 'error':
                logger.error(f"WebSocket error: {data}")
                
        except Exception as e:
            logger.error(f"Message processing error: {e}")
    
    async def _handle_order_update(self, data: Dict):
        """Handle order update message"""
        market_id = data.get('marketId')
        order_id = data.get('orderId')
        status = data.get('status')
        
        if market_id and order_id:
            await self.update_position(market_id, {
                'order_id': order_id,
                'status': status,
                'last_update': time.time()
            })
    
    async def _handle_fill(self, data: Dict):
        """Handle fill message"""
        market_id = data.get('marketId')
        order_id = data.get('orderId')
        fill_size = data.get('fillSize', 0)
        total_size = data.get('totalSize', 1)
        
        if market_id:
            fill_percentage = fill_size / total_size if total_size > 0 else 0
            
            await self.update_position(market_id, {
                'fill_percentage': fill_percentage,
                'fill_size': fill_size,
                'last_fill': time.time()
            })
    
    async def _handle_market_data(self, data: Dict):
        """Handle market data update"""
        market_id = data.get('marketId')
        
        if market_id:
            conditions = {
                'mid_price': data.get('midPrice', 0),
                'volume': data.get('volume', 0),
                'spread': data.get('spread', 0),
                'liquidity': data.get('liquidity', 0),
                'timestamp': time.time()
            }
            
            await self.update_market_conditions(market_id, conditions)
    
    def get_monitoring_stats(self) -> Dict:
        """Get monitoring statistics"""
        return {
            'monitored_positions': len(self.positions),
            'active_positions': sum(1 for p in self.positions.values() if p['status'] == 'open'),
            'market_conditions_tracked': len(self.market_conditions),
            'ws_connected': self.ws_connection is not None
        }
    
    async def close(self):
        """Close WebSocket connection"""
        if self.ws_connection:
            await self.ws_connection.close()
            logger.info("WebSocket connection closed")