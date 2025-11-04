"""
Order Manager Module
Handles order placement, updates, and cancellations
"""

import asyncio
import aiohttp
import logging
from typing import List, Dict, Optional, Tuple
from decimal import Decimal, ROUND_DOWN
import json
import time
import random
from py_clob_client.client import ClobClient

logger = logging.getLogger(__name__)


class OrderManager:
    """Manages order lifecycle on Polymarket CLOB"""
    
    def __init__(self, config: dict):
        self.config = config
        self.pending_orders = []
        self.active_orders = {}
        self.filled_orders = []
        self.clob_client = None
        self._initialize_clob()
    
    def _initialize_clob(self):
        """Initialize CLOB client (read-only mode)"""
        try:
            # Initialize CLOB client in read-only mode (no key required for market data)
            self.clob_client = ClobClient(
                host="https://clob.polymarket.com"
            )

            logger.info("CLOB client initialized successfully (read-only mode)")

        except Exception as e:
            logger.error(f"Failed to initialize CLOB: {e}")
    
    async def prepare_market_order(self, market: Dict) -> Dict:
        """Prepare order with dynamic spread calculation"""
        try:
            # Get token_id from market data (first token for YES outcome)
            token_id = None
            if market.get('clob_token_ids') and len(market['clob_token_ids']) > 0:
                token_id = market['clob_token_ids'][0]  # Use first token (YES outcome)
                logger.debug(f"Using token_id: {token_id} for market {market['id']}")
            else:
                logger.warning(f"No clob_token_ids found for market {market['id']}, will try with market ID")

            # Get current market prices
            market_data = await self._fetch_market_data(market['id'], token_id)

            if not market_data:
                logger.warning(f"Could not fetch data for market {market['id']}")
                return None

            # Calculate dynamic spread
            spread = self._calculate_dynamic_spread(market_data)

            # Calculate order sizes with jitter
            yes_size, no_size = self._calculate_order_sizes()

            # Prepare both sides
            order = {
                'market_id': market['id'],
                'market_title': market.get('question', market.get('title', 'Unknown')),
                'token_ids': market.get('clob_token_ids', []),  # Store token IDs for order placement
                'yes_order': {
                    'side': 'buy',
                    'outcome': 'yes',
                    'price': market_data['mid_price'] - spread,
                    'size': yes_size,
                    'type': 'limit',
                    'time_in_force': 'GTC'  # Good Till Cancelled
                },
                'no_order': {
                    'side': 'buy',
                    'outcome': 'no',
                    'price': 1 - (market_data['mid_price'] + spread),
                    'size': no_size,
                    'type': 'limit',
                    'time_in_force': 'GTC'
                },
                'spread': spread,
                'created_at': time.time(),
                'status': 'pending'
            }

            logger.info(f"Prepared order for market {market['id']} with spread {spread:.4f}")

            return order

        except Exception as e:
            logger.error(f"Error preparing order: {e}")
            return None
    
    async def _fetch_market_data(self, market_id: str, token_id: str = None) -> Optional[Dict]:
        """Fetch current market data from CLOB

        Args:
            market_id: Market ID (for logging)
            token_id: CLOB token ID (required for fetching orderbook)
        """
        try:
            # Get order book using token_id
            order_book = await self._get_order_book(market_id, token_id)

            if not order_book:
                return None

            # Convert OrderBookSummary object to dict if needed
            if hasattr(order_book, 'bids'):
                # It's an OrderBookSummary object, access attributes directly
                bids = order_book.bids if order_book.bids else []
                asks = order_book.asks if order_book.asks else []
            elif isinstance(order_book, dict):
                # It's already a dict (from direct API call)
                bids = order_book.get('bids', [])
                asks = order_book.get('asks', [])
            else:
                logger.error(f"Unknown orderbook type: {type(order_book)}")
                return None

            # Helper function to safely get price/size from order (object or dict)
            def get_order_value(order, field):
                if hasattr(order, field):
                    return float(getattr(order, field))
                elif isinstance(order, dict):
                    return float(order.get(field, 0))
                else:
                    return 0.0

            # Calculate mid price
            best_bid = get_order_value(bids[0], 'price') if bids else 0
            best_ask = get_order_value(asks[0], 'price') if asks else 1
            mid_price = (best_bid + best_ask) / 2

            # Calculate spread and depth
            current_spread = best_ask - best_bid

            # Calculate volume at best prices
            bid_volume = sum(get_order_value(bid, 'size') for bid in bids[:5])
            ask_volume = sum(get_order_value(ask, 'size') for ask in asks[:5])

            return {
                'mid_price': mid_price,
                'best_bid': best_bid,
                'best_ask': best_ask,
                'current_spread': current_spread,
                'bid_volume': bid_volume,
                'ask_volume': ask_volume,
                'order_book': order_book
            }

        except Exception as e:
            logger.error(f"Error fetching market data: {e}")
            return None
    
    async def _get_order_book(self, market_id: str, token_id: str = None) -> Optional[Dict]:
        """Get order book from CLOB API

        Args:
            market_id: Market ID (for logging)
            token_id: CLOB token ID (required for fetching orderbook)
        """
        try:
            # Use token_id if provided, otherwise fall back to market_id
            lookup_id = token_id if token_id else market_id

            if self.clob_client:
                # Use py-clob-client with token_id
                book = self.clob_client.get_order_book(lookup_id)
                return book
            else:
                # Fallback to direct API call
                url = f"https://clob.polymarket.com/book?token_id={lookup_id}"

                async with aiohttp.ClientSession() as session:
                    async with session.get(url) as response:
                        if response.status == 200:
                            return await response.json()

            return None

        except Exception as e:
            logger.error(f"Error getting order book: {e}")
            return None
    
    def _calculate_dynamic_spread(self, market_data: Dict) -> float:
        """Calculate dynamic spread based on market conditions"""
        try:
            base_spread = (self.config['spread_min'] + self.config['spread_max']) / 2
            
            # Adjust based on current spread
            current_spread = market_data['current_spread']
            if current_spread > 0.05:  # Wide spread
                spread_multiplier = 1.2
            elif current_spread > 0.02:  # Normal spread
                spread_multiplier = 1.0
            else:  # Tight spread
                spread_multiplier = 0.8
            
            # Adjust based on volume imbalance
            bid_volume = market_data['bid_volume']
            ask_volume = market_data['ask_volume']
            
            if bid_volume > ask_volume * 2:  # Heavy buying pressure
                spread_multiplier *= 1.1
            elif ask_volume > bid_volume * 2:  # Heavy selling pressure
                spread_multiplier *= 1.1
            
            # Calculate final spread
            dynamic_spread = base_spread * spread_multiplier
            
            # Ensure within configured bounds
            dynamic_spread = max(self.config['spread_min'], 
                                min(self.config['spread_max'], dynamic_spread))
            
            return dynamic_spread
            
        except Exception as e:
            logger.error(f"Error calculating spread: {e}")
            return (self.config['spread_min'] + self.config['spread_max']) / 2
    
    def _calculate_order_sizes(self) -> Tuple[int, int]:
        """Calculate order sizes with jitter"""
        base_size = (self.config['size_min'] + self.config['size_max']) / 2
        
        # Add random jitter (±20%)
        jitter_range = 0.2
        yes_jitter = random.uniform(1 - jitter_range, 1 + jitter_range)
        no_jitter = random.uniform(1 - jitter_range, 1 + jitter_range)
        
        yes_size = int(base_size * yes_jitter)
        no_size = int(base_size * no_jitter)
        
        # Ensure within bounds
        yes_size = max(self.config['size_min'], min(self.config['size_max'], yes_size))
        no_size = max(self.config['size_min'], min(self.config['size_max'], no_size))
        
        return yes_size, no_size
    
    async def place_order(self, order: Dict, wallet: Dict) -> Optional[Dict]:
        """Place order on CLOB"""
        try:
            if not self.clob_client:
                logger.error("CLOB client not initialized")
                return None

            # Get token IDs for YES and NO outcomes
            token_ids = order.get('token_ids', [])
            if len(token_ids) < 2:
                logger.error(f"Missing token_ids for market {order['market_id']}")
                return None

            yes_token_id = token_ids[0]  # First token is YES
            no_token_id = token_ids[1]   # Second token is NO

            placed_orders = {}

            # Place YES side
            yes_order_id = await self._place_single_order(
                order['yes_order'],
                yes_token_id,  # Use YES token ID
                wallet
            )
            if yes_order_id:
                placed_orders['yes'] = yes_order_id

            # Add small delay to appear human
            await asyncio.sleep(random.uniform(0.5, 1.5))

            # Place NO side
            no_order_id = await self._place_single_order(
                order['no_order'],
                no_token_id,  # Use NO token ID
                wallet
            )
            if no_order_id:
                placed_orders['no'] = no_order_id

            if placed_orders:
                # Update order status
                order['status'] = 'active'
                order['order_ids'] = placed_orders
                order['placed_at'] = time.time()

                # Add to active orders
                self.active_orders[order['market_id']] = order

                logger.info(f"Placed orders for market {order['market_id']}: {placed_orders}")

            return placed_orders

        except Exception as e:
            logger.error(f"Error placing order: {e}")
            return None
    
    async def _place_single_order(self, order_params: Dict, market_id: str, wallet: Dict) -> Optional[str]:
        """Place a single order on CLOB"""
        try:
            # Create order using ClobClient directly
            from py_clob_client.order_builder.constants import BUY, SELL
            from py_clob_client.clob_types import OrderArgs
            import traceback

            # Determine side constant
            side_constant = BUY if order_params['side'] == 'buy' else SELL

            # Log order details for debugging
            logger.debug(f"Creating order: token_id={market_id}, price={order_params['price']}, size={order_params['size']}, side={order_params['side']}")

            # Create OrderArgs object
            order_args = OrderArgs(
                token_id=market_id,
                price=order_params['price'],
                size=order_params['size'],
                side=side_constant
            )

            # Create a new ClobClient instance with the wallet's private key
            # (The global clob_client is read-only, we need a signing client per wallet)
            signing_client = ClobClient(
                host="https://clob.polymarket.com",
                key=wallet['private_key']  # Add private key for signing
            )

            # Create and sign order
            logger.debug("Signing order...")
            signed_order = signing_client.create_order(order_args)
            logger.debug(f"Order signed: {type(signed_order)}")

            # Submit order
            logger.debug("Submitting order to CLOB...")
            response = signing_client.post_order(signed_order)
            logger.debug(f"CLOB response: {response}")

            if response and 'orderID' in response:
                logger.info(f"Order placed successfully: {response['orderID']}")
                return response['orderID']

            logger.warning(f"Order placement failed: no orderID in response: {response}")
            return None

        except Exception as e:
            # Enhanced error logging with full traceback
            logger.error(f"Error placing single order: {type(e).__name__}: {str(e)}")
            logger.error(f"Full traceback: {traceback.format_exc()}")
            return None
    
    async def cancel_order(self, order_id: str) -> bool:
        """Cancel an order"""
        try:
            if not self.clob_client:
                return False
            
            # Cancel via CLOB API
            response = self.clob_client.cancel_order(order_id)
            
            if response and response.get('success'):
                logger.info(f"Cancelled order {order_id}")
                return True
            
            return False
            
        except Exception as e:
            logger.error(f"Error cancelling order {order_id}: {e}")
            return False
    
    async def cancel_all_orders(self) -> int:
        """Cancel all active orders"""
        cancelled_count = 0
        
        for market_id, order in list(self.active_orders.items()):
            if 'order_ids' in order:
                for side, order_id in order['order_ids'].items():
                    if await self.cancel_order(order_id):
                        cancelled_count += 1
                
                # Remove from active orders
                del self.active_orders[market_id]
        
        logger.info(f"Cancelled {cancelled_count} orders")
        return cancelled_count
    
    async def update_order_price(self, order_id: str, new_price: float, wallet: Dict) -> bool:
        """Update order price (cancel and replace)"""
        try:
            # Get order details
            order_details = await self._get_order_details(order_id)

            if not order_details:
                return False

            # Cancel existing order
            if not await self.cancel_order(order_id):
                return False

            # Place new order with updated price
            new_order_params = order_details.copy()
            new_order_params['price'] = new_price

            # Use provided wallet (from wallet manager)
            new_order_id = await self._place_single_order(
                new_order_params,
                order_details['market_id'],
                wallet
            )

            return new_order_id is not None

        except Exception as e:
            logger.error(f"Error updating order: {e}")
            return False
    
    async def _get_order_details(self, order_id: str) -> Optional[Dict]:
        """Get details of a specific order"""
        try:
            if self.clob_client:
                return self.clob_client.get_order(order_id)
            return None
        except Exception as e:
            logger.error(f"Error getting order details: {e}")
            return None
    
    async def add_pending_order(self, order: Dict):
        """Add order to pending queue"""
        if order:
            self.pending_orders.append(order)
            logger.info(f"Added order to pending queue: {order['market_id']}")
    
    async def get_pending_orders(self) -> List[Dict]:
        """Get all pending orders"""
        return self.pending_orders.copy()
    
    async def check_order_fills(self) -> List[Dict]:
        """Check for filled orders"""
        fills = []
        
        for market_id, order in self.active_orders.items():
            if 'order_ids' not in order:
                continue
            
            for side, order_id in order['order_ids'].items():
                order_status = await self._get_order_details(order_id)
                
                if order_status and order_status.get('status') == 'filled':
                    fills.append({
                        'market_id': market_id,
                        'side': side,
                        'order_id': order_id,
                        'fill_price': order_status.get('fillPrice'),
                        'fill_size': order_status.get('fillSize'),
                        'timestamp': time.time()
                    })
                    
                    # Move to filled orders
                    self.filled_orders.append(order_status)
        
        return fills
    
    def get_order_stats(self) -> Dict:
        """Get order statistics"""
        return {
            'pending_orders': len(self.pending_orders),
            'active_orders': len(self.active_orders),
            'filled_orders': len(self.filled_orders),
            'total_processed': len(self.filled_orders) + len(self.active_orders)
        }