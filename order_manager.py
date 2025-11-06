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

    def __init__(self, config: dict, telegram_notifier=None):
        self.config = config
        self.pending_orders = []
        self.active_orders = {}
        self.filled_orders = []
        self.clob_client = None
        self.telegram = telegram_notifier  # Telegram notifier
        
        # Read CLOB settings from config
        clob_config = self.config.get('clob', {})
        self.clob_host = clob_config.get('host', 'https://clob.polymarket.com')
        self.chain_id = clob_config.get('chain_id', 137)
        
        self._initialize_clob()
    
    def _initialize_clob(self):
        """Initialize CLOB client (read-only mode)"""
        try:
            # Initialize CLOB client in read-only mode (no key required for market data)
            self.clob_client = ClobClient(
                host=self.clob_host
            )

            logger.info("CLOB client initialized successfully (read-only mode)")

        except Exception as e:
            logger.error(f"Failed to initialize CLOB: {e}")
    
    async def prepare_market_order(self, market: Dict) -> Dict:
        """Prepare order with position-based pricing (2nd or 3rd position in order book)"""
        try:
            # Get market ID (CLOB API uses 'market_id' or 'condition_id', Gamma API uses 'id')
            market_id = market.get('market_id') or market.get('condition_id') or market.get('id', 'unknown')

            # Get token_id from market data (first token for YES outcome)
            token_id = None
            if market.get('clob_token_ids') and len(market['clob_token_ids']) > 0:
                token_id = market['clob_token_ids'][0]  # Use first token (YES outcome)
                logger.debug(f"Using token_id: {token_id} for market {market_id}")
            else:
                logger.warning(f"No clob_token_ids found for market {market_id}, will try with market ID")

            # Get current market prices and order book
            market_data = await self._fetch_market_data(market_id, token_id)

            if not market_data:
                logger.warning(f"Could not fetch data for market {market_id}")
                return None

            # Get max spread from market rewards config (if available)
            max_spread_pct = market.get('rewards_max_spread', 3.5)  # Default 3.5%
            max_spread_decimal = max_spread_pct / 100  # Convert to decimal (e.g., 0.035)

            # Calculate order prices at 2nd or 3rd position in order book
            yes_price, no_price, position_info = self._calculate_position_based_prices(
                market_data,
                max_spread_decimal
            )

            if yes_price is None or no_price is None:
                logger.warning(f"Could not calculate valid prices for market {market_id}")
                return None

            # Calculate order sizes with jitter
            yes_size, no_size = self._calculate_order_sizes()

            # Prepare both sides
            order = {
                'market_id': market_id,
                'market_title': market.get('question', market.get('title', 'Unknown')),
                'token_ids': market.get('clob_token_ids', []),  # Store token IDs for order placement
                'yes_order': {
                    'side': 'buy',
                    'outcome': 'yes',
                    'price': yes_price,
                    'size': yes_size,
                    'type': 'limit',
                    'time_in_force': 'GTC'  # Good Till Cancelled
                },
                'no_order': {
                    'side': 'buy',
                    'outcome': 'no',
                    'price': no_price,
                    'size': no_size,
                    'type': 'limit',
                    'time_in_force': 'GTC'
                },
                'position_info': position_info,  # Store position details for logging
                'created_at': time.time(),
                'status': 'pending'
            }

            logger.info(f"✅ Prepared order for market {market_id}")
            logger.info(f"   - YES: ${yes_price:.4f} at position {position_info['yes_position']}")
            logger.info(f"   - NO: ${no_price:.4f} at position {position_info['no_position']}")
            logger.info(f"   - Spread from mid: {position_info['spread_from_mid']:.2%} (max: {max_spread_decimal:.2%})")

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
                url = f"{self.clob_host}/book?token_id={lookup_id}"

                async with aiohttp.ClientSession() as session:
                    async with session.get(url) as response:
                        if response.status == 200:
                            return await response.json()

            return None

        except Exception as e:
            logger.error(f"Error getting order book: {e}")
            return None
    
    def _calculate_position_based_prices(self, market_data: Dict, max_spread: float) -> Tuple[Optional[float], Optional[float], Dict]:
        """Calculate order prices to place at 2nd or 3rd position in order book

        Args:
            market_data: Market data including order book
            max_spread: Maximum allowed spread from midpoint (as decimal, e.g., 0.035 for 3.5%)

        Returns:
            Tuple of (yes_price, no_price, position_info)
        """
        try:
            order_book = market_data['order_book']
            mid_price = market_data['mid_price']

            # Extract bids and asks from order book
            if hasattr(order_book, 'bids'):
                bids = order_book.bids if order_book.bids else []
                asks = order_book.asks if order_book.asks else []
            elif isinstance(order_book, dict):
                bids = order_book.get('bids', [])
                asks = order_book.get('asks', [])
            else:
                logger.error(f"Unknown orderbook type: {type(order_book)}")
                return None, None, {}

            # ⚠️ CRITICAL CHECK: Ensure order book has enough depth
            # We need at least 2 orders on each side to place at position 2 or 3
            # This prevents bot from EVER placing at position 1 (best bid/ask)
            logger.debug(f"📊 Orderbook depth: {len(bids)} bids, {len(asks)} asks")

            if len(bids) < 2 or len(asks) < 2:
                logger.warning(f"❌ Order book too thin! Bids: {len(bids)}, Asks: {len(asks)}")
                logger.warning(f"   Bot requires at least 2 orders on EACH side to avoid position 1")
                logger.warning(f"   Rejecting this market to prevent being best bid/ask")
                return None, None, {}

            # Helper function to get price from order (handle both dict and object)
            def get_price(order):
                if isinstance(order, dict):
                    return float(order.get('price', 0))
                else:
                    return float(getattr(order, 'price', 0))

            # Target position: 2nd or 3rd (randomly choose for variety)
            target_position = random.choice([2, 3])

            # Calculate YES order price (buy side - we want to be in the bid book)
            # For YES outcome, we BUY at a price below midpoint
            yes_price = None
            yes_position = 1  # Default to position 1 if not enough orders

            if len(bids) >= target_position:
                # Place at target position (2nd or 3rd)
                target_bid = bids[target_position - 1]
                target_price = get_price(target_bid)

                # Slightly undercut the target position (0.001 = 0.1 cent lower)
                yes_price = target_price - 0.001
                yes_position = target_position
            elif len(bids) > 0:
                # Not enough orders, place behind the last bid
                last_bid = bids[-1]
                yes_price = get_price(last_bid) - 0.001
                yes_position = len(bids) + 1
            else:
                # No bids, place at midpoint - max_spread
                yes_price = mid_price - (max_spread * mid_price)
                yes_position = 1

            # Calculate NO order price (buy side - we want to be in the bid book for NO)
            # For NO outcome, price = 1 - YES_ask_equivalent
            # We need to think in terms of the NO token's order book
            no_price = None
            no_position = 1

            if len(asks) >= target_position:
                # Place at target position (2nd or 3rd)
                target_ask = asks[target_position - 1]
                target_price = get_price(target_ask)

                # For NO: if YES ask is at X, NO bid should be at (1 - X) + small offset
                # We want to be slightly better than the target position
                no_price = 1 - target_price - 0.001
                no_position = target_position
            elif len(asks) > 0:
                # Not enough orders, place behind the last ask
                last_ask = asks[-1]
                no_price = 1 - get_price(last_ask) - 0.001
                no_position = len(asks) + 1
            else:
                # No asks, place at midpoint - max_spread
                no_price = (1 - mid_price) - (max_spread * (1 - mid_price))
                no_position = 1

            # Validate prices are within max spread
            # For YES: spread from mid = (mid - yes_price) / mid
            # For NO: we need to convert NO price to YES equivalent first
            # NO price of X means YES price of (1-X), so spread = (mid - (1-no_price)) / mid
            yes_spread_from_mid = abs(mid_price - yes_price) / mid_price
            no_as_yes_price = 1 - no_price  # Convert NO price to YES equivalent
            no_spread_from_mid = abs(mid_price - no_as_yes_price) / mid_price

            max_spread_from_mid = max(yes_spread_from_mid, no_spread_from_mid)

            # 🔍 DEBUG: Log calculated prices and spreads
            logger.debug(f"💰 Calculated prices:")
            logger.debug(f"   Midpoint: ${mid_price:.4f}")
            logger.debug(f"   YES: ${yes_price:.4f} (position {yes_position}, spread: {yes_spread_from_mid:.2%})")
            logger.debug(f"   NO: ${no_price:.4f} (position {no_position}, spread: {no_spread_from_mid:.2%})")
            logger.debug(f"   Max spread: {max_spread_from_mid:.2%} (allowed: {max_spread:.2%})")

            if max_spread_from_mid > max_spread:
                logger.warning(f"❌ Calculated prices exceed max spread ({max_spread_from_mid:.2%} > {max_spread:.2%})")
                logger.warning(f"   This indicates orderbook is too thin or position 2-3 is too far from midpoint")
                logger.warning(f"   REJECTING market to avoid placing order at position #1 (best bid/ask)")
                logger.warning(f"   Reason: Adjusting to max spread would place order too close to best bid/ask")
                logger.warning(f"   → High risk of being filled immediately!")

                # 🚨 CRITICAL FIX: REJECT market instead of adjusting
                # Adjusting to max spread often places order at or very close to position #1
                # This causes immediate fills and losses
                return None, None, {}

            # Ensure prices are valid (between 0 and 1)
            yes_price = max(0.01, min(0.99, yes_price))
            no_price = max(0.01, min(0.99, no_price))

            position_info = {
                'yes_position': yes_position,
                'no_position': no_position,
                'spread_from_mid': max_spread_from_mid,
                'max_spread_allowed': max_spread,
                'midpoint': mid_price,
                'num_bids': len(bids),
                'num_asks': len(asks)
            }

            return yes_price, no_price, position_info

        except Exception as e:
            logger.error(f"Error calculating position-based prices: {e}")
            import traceback
            traceback.print_exc()
            return None, None, {}
    
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

                # Send Telegram notification
                if self.telegram:
                    try:
                        # Get market details for notification
                        market = {
                            'question': order.get('market_title', 'Unknown'),
                            'id': order['market_id']
                        }
                        await self.telegram.notify_order_placed(order, market)
                    except Exception as e:
                        logger.debug(f"Failed to send order placed notification: {e}")

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
                host=self.clob_host,
                key=wallet['private_key'],  # Add private key for signing
                chain_id=self.chain_id  # From config
            )

            # Set API credentials (required for L2 auth to post orders)
            logger.debug("Setting API credentials...")
            signing_client.set_api_creds(signing_client.create_or_derive_api_creds())

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
    
    async def cancel_order(self, order_id: str, reason: str = "Unknown") -> bool:
        """Cancel an order"""
        try:
            if not self.clob_client:
                return False

            # Cancel via CLOB API
            response = self.clob_client.cancel_order(order_id)

            if response and response.get('success'):
                logger.info(f"Cancelled order {order_id} - Reason: {reason}")

                # Send Telegram notification
                if self.telegram:
                    try:
                        # Find market name from active orders
                        market_name = "Unknown"
                        for market_id, order in self.active_orders.items():
                            if order.get('order_ids', {}).get('yes') == order_id or \
                               order.get('order_ids', {}).get('no') == order_id:
                                market_name = order.get('market_title', 'Unknown')
                                break

                        await self.telegram.notify_order_cancelled(order_id, market_name, reason)
                    except Exception as e:
                        logger.debug(f"Failed to send cancel notification: {e}")

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
                    fill_data = {
                        'market_id': market_id,
                        'side': side,
                        'order_id': order_id,
                        'fill_price': order_status.get('fillPrice'),
                        'fill_size': order_status.get('fillSize'),
                        'timestamp': time.time()
                    }
                    fills.append(fill_data)

                    # Move to filled orders
                    self.filled_orders.append(order_status)

                    # Send Telegram notification (IMPORTANT!)
                    if self.telegram:
                        try:
                            market = {
                                'question': order.get('market_title', 'Unknown'),
                                'id': market_id
                            }
                            # TODO: Calculate P&L if possible
                            await self.telegram.notify_order_filled(fill_data, market, pnl=None)
                        except Exception as e:
                            logger.debug(f"Failed to send fill notification: {e}")
        
        return fills
    
    def get_order_stats(self) -> Dict:
        """Get order statistics"""
        return {
            'pending_orders': len(self.pending_orders),
            'active_orders': len(self.active_orders),
            'filled_orders': len(self.filled_orders),
            'total_processed': len(self.filled_orders) + len(self.active_orders)
        }