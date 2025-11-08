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

            # Get token_id from market data
            # For binary markets (YES/NO), fetch both orderbooks
            # This is simpler and more direct than calculating from one orderbook
            token_ids = market.get('clob_token_ids', [])

            logger.info(f"🔍 Market {market_id} has {len(token_ids)} tokens: {token_ids}")

            # CRITICAL CHECK 1: Reject categorical event outcomes
            # If event_slug != market_slug, this is an outcome of a categorical event
            market_slug = market.get('market_slug', '')
            event_slug = market.get('event_slug', '')
            if event_slug and market_slug and event_slug != market_slug:
                logger.warning(f"❌ REJECTED - CATEGORICAL EVENT OUTCOME detected!")
                logger.warning(f"   Event slug: {event_slug}")
                logger.warning(f"   Market slug: {market_slug}")
                logger.warning(f"   This is one outcome of a categorical event, not a standalone binary market")
                logger.warning(f"   Example: 'NFLX above $1070' is one of many outcomes in 'NFLX above on Nov 14'")
                logger.warning(f"   Market: {market.get('question', 'Unknown')[:80]}")
                return None

            # CRITICAL CHECK 2: Only accept BINARY markets (exactly 2 tokens)
            # Categorical markets have >2 tokens and are not suitable for our YES/NO strategy
            if len(token_ids) != 2:
                if len(token_ids) < 2:
                    logger.warning(f"❌ REJECTED - Invalid market: only {len(token_ids)} token(s)")
                    logger.warning(f"   Binary markets must have exactly 2 tokens (YES + NO)")
                else:
                    logger.warning(f"❌ REJECTED - CATEGORICAL MARKET detected: {len(token_ids)} tokens")
                    logger.warning(f"   This is NOT a binary YES/NO market!")
                    logger.warning(f"   Categorical markets have multiple outcomes, not suitable for our strategy")
                    logger.warning(f"   Example: 'Elon tweets 0-19' vs '20-39' vs '40-59' etc.")
                logger.warning(f"   Market: {market.get('question', 'Unknown')[:80]}")
                return None

            logger.info(f"✅ Binary market confirmed: 2 tokens (YES/NO)")

            # AUTO-SELECT CORRECT TOKEN: Try BOTH tokens and pick the one with narrower spread
            # Polymarket token convention may vary - we can't assume token[0] = YES or NO
            # The correct token will have a NARROW spread (e.g., 2-10¢)
            # The wrong token will have a WIDE spread (e.g., 90-98¢)
            token_id_0 = token_ids[0]
            token_id_1 = token_ids[1]

            logger.info(f"🧪 Testing token[0]: {token_id_0}")
            market_data_0 = await self._fetch_market_data(market_id, token_id_0)

            logger.info(f"🧪 Testing token[1]: {token_id_1}")
            market_data_1 = await self._fetch_market_data(market_id, token_id_1)

            if not market_data_0 or not market_data_1:
                logger.warning(f"❌ Could not fetch orderbook for both tokens")
                return None

            # Compare spreads - pick the token with NARROWER spread
            spread_0 = market_data_0.get('current_spread', 1.0)
            spread_1 = market_data_1.get('current_spread', 1.0)

            logger.info(f"📊 Token[0] spread: ${spread_0:.4f} ({spread_0*100:.2f}¢)")
            logger.info(f"📊 Token[1] spread: ${spread_1:.4f} ({spread_1*100:.2f}¢)")

            if spread_0 < spread_1:
                yes_token_id = token_id_0
                no_token_id = token_id_1
                yes_market_data = market_data_0
                no_market_data = market_data_1
                logger.info(f"✅ Using token[0] as YES (narrower spread)")
            else:
                yes_token_id = token_id_1
                no_token_id = token_id_0
                yes_market_data = market_data_1
                no_market_data = market_data_0
                logger.info(f"✅ Using token[1] as YES (narrower spread)")

            # VALIDATION: Verify this is a TRUE binary market (YES + NO ≈ $1.00)
            # Binary market validation - Check if YES + NO bids sum to ~$1.00
            # This helps detect categorical markets misidentified as binary
            yes_best_bid = yes_market_data.get('best_bid', 0)
            no_best_bid = no_market_data.get('best_bid', 0)
            bid_sum = yes_best_bid + no_best_bid

            # ✅ IMPORTANT: Skip validation for LIQUIDITY REWARDS markets
            # Markets with liquidity rewards are INTENTIONALLY illiquid (high spread)
            # That's WHY Polymarket pays rewards - they need market makers!
            #
            # Example ILLIQUID binary market (with rewards):
            # YES: Bid $0.01, Ask $0.95 → Spread 94¢
            # NO:  Bid $0.05, Ask $0.99 → Spread 94¢
            # Sum of bids: $0.06 (very low, but THIS IS NORMAL for illiquid markets!)
            #
            # These markets are GOOD opportunities for farming:
            # - High spread = Low liquidity = High rewards
            # - Bot will CREATE liquidity by placing tight spread orders
            # - Bot earns rewards for improving market efficiency
            has_liquidity_rewards = market.get('rewardsMinSize', 0) > 0 and market.get('rewardsMaxSpread', 0) > 0

            if not has_liquidity_rewards:
                # Only validate binary market for non-rewards markets
                # In true binary market: YES bid + NO bid should be in range [0.3, 1.7]
                if bid_sum < 0.3 or bid_sum > 1.7:
                    logger.warning(f"❌ REJECTED - Invalid binary market detected!")
                    logger.warning(f"   YES best bid: ${yes_best_bid:.4f} ({yes_best_bid*100:.2f}¢)")
                    logger.warning(f"   NO best bid: ${no_best_bid:.4f} ({no_best_bid*100:.2f}¢)")
                    logger.warning(f"   Sum: ${bid_sum:.4f} (expected ~$1.00 for binary markets)")
                    logger.warning(f"   This market does NOT behave like a binary YES/NO market")
                    logger.warning(f"   Likely a categorical market with 2 unrelated outcomes")
                    return None

                logger.info(f"✅ Binary market validation passed:")
                logger.info(f"   YES best bid: ${yes_best_bid:.4f} + NO best bid: ${no_best_bid:.4f} = ${bid_sum:.4f}")
                logger.info(f"   Sum is within valid range [0.3, 1.7] for binary markets")
            else:
                # Skip validation for liquidity rewards markets
                logger.info(f"✅ Skipping binary validation for LIQUIDITY REWARDS market:")
                logger.info(f"   YES best bid: ${yes_best_bid:.4f}, NO best bid: ${no_best_bid:.4f}")
                logger.info(f"   Sum: ${bid_sum:.4f} (low bid sum is NORMAL for illiquid markets with rewards)")
                logger.info(f"   This market has liquidity rewards - illiquidity is expected and desired!")

            # Get max spread from market rewards config (if available)
            # UPDATED: Increased default from 3.5% to 8% for position #3 strategy
            # Position #3 naturally has wider spread than position #1, so we need higher threshold
            max_spread_pct = market.get('rewards_max_spread', 8.0)  # Default 8.0%
            max_spread_decimal = max_spread_pct / 100  # Convert to decimal (e.g., 0.08)

            # Calculate order prices at position #3 in order book
            # Pass both YES and NO orderbook data for direct price lookup
            yes_price, no_price, position_info = self._calculate_position_based_prices(
                yes_market_data,
                no_market_data,
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
            logger.info(f"   - YES bid: ${yes_price:.4f} ({yes_price*100:.2f}¢) at position #{position_info.get('target_position', 3)}")
            logger.info(f"   - NO bid: ${no_price:.4f} ({no_price*100:.2f}¢) at position #{position_info.get('target_position', 3)}")
            logger.info(f"   - Spread: {position_info['spread']:.2%} (max: {max_spread_decimal:.2%})")
            logger.info(f"   - Offset from position #2: ${position_info['offset']:.4f} ({position_info['offset']*100:.2f}¢)")

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

            # 🔍 DEBUG: Log orderbook data
            logger.info(f"📊 Orderbook for market {market_id}:")
            logger.info(f"   Best Bid: ${best_bid:.4f} ({best_bid*100:.2f}¢)")
            logger.info(f"   Best Ask: ${best_ask:.4f} ({best_ask*100:.2f}¢)")
            logger.info(f"   Mid Price: ${mid_price:.4f} ({mid_price*100:.2f}¢)")
            logger.info(f"   Spread: ${(best_ask - best_bid):.4f} ({(best_ask - best_bid)*100:.2f}¢)")
            logger.info(f"   Spread %: {((best_ask - best_bid) / best_bid * 100):.2f}%")

            # Log top 3 bids and asks
            logger.info(f"   Top 3 Bids:")
            for i, bid in enumerate(bids[:3], 1):
                price = get_order_value(bid, 'price')
                size = get_order_value(bid, 'size')
                logger.info(f"      {i}. ${price:.4f} ({price*100:.2f}¢) x {size:.0f}")

            logger.info(f"   Top 3 Asks:")
            for i, ask in enumerate(asks[:3], 1):
                price = get_order_value(ask, 'price')
                size = get_order_value(ask, 'size')
                logger.info(f"      {i}. ${price:.4f} ({price*100:.2f}¢) x {size:.0f}")

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
    
    def _calculate_position_based_prices(self, yes_market_data: Dict, no_market_data: Dict, max_spread: float) -> Tuple[Optional[float], Optional[float], Dict]:
        """Calculate order prices to place at position #3 in orderbook

        STRATEGY (SIMPLIFIED):
        1. Fetch both YES and NO orderbooks
        2. Get bid price from position #2 in YES orderbook
        3. Get bid price from position #2 in NO orderbook
        4. Place our orders slightly below position #2 (0.05-0.15 cents lower)
        5. This ensures our orders are at position #3 → NEVER at position #1
        6. Check if spread between our YES bid and NO bid is within max_spread

        Args:
            yes_market_data: Market data including YES token orderbook
            no_market_data: Market data including NO token orderbook
            max_spread: Maximum allowed spread between our bid and ask (as decimal, e.g., 0.08 for 8%)

        Returns:
            Tuple of (yes_price, no_price, position_info)
        """
        try:
            # Extract YES orderbook
            yes_order_book = yes_market_data['order_book']
            yes_mid_price = yes_market_data['mid_price']

            # Extract NO orderbook
            no_order_book = no_market_data['order_book']
            no_mid_price = no_market_data['mid_price']

            # Helper function to extract bids from orderbook
            def get_bids(order_book):
                if hasattr(order_book, 'bids'):
                    return order_book.bids if order_book.bids else []
                elif isinstance(order_book, dict):
                    return order_book.get('bids', [])
                else:
                    return []

            # Helper function to get price from order (handle both dict and object)
            def get_price(order):
                if isinstance(order, dict):
                    return float(order.get('price', 0))
                else:
                    return float(getattr(order, 'price', 0))

            # Get bids from both orderbooks
            yes_bids = get_bids(yes_order_book)
            no_bids = get_bids(no_order_book)

            # ⚠️ CRITICAL CHECK: Need at least 2 bids on each side
            # We take bid price from position #2, so we need at least 2 bids
            logger.debug(f"📊 Orderbook depth: YES {len(yes_bids)} bids, NO {len(no_bids)} bids")

            if len(yes_bids) < 2 or len(no_bids) < 2:
                logger.warning(f"❌ Order book too thin! YES bids: {len(yes_bids)}, NO bids: {len(no_bids)}")
                logger.warning(f"   Need at least 2 bids on EACH side to place at position #3")
                logger.warning(f"   REJECTING market")
                return None, None, {}

            # Get bid position #1 and #2 from YES orderbook
            yes_best_bid = get_price(yes_bids[0])  # Position #1
            yes_second_bid = get_price(yes_bids[1])  # Position #2

            # Get bid position #1 and #2 from NO orderbook
            no_best_bid = get_price(no_bids[0])  # Position #1
            no_second_bid = get_price(no_bids[1])  # Position #2

            # Random offset between 0.05 and 0.15 cents to add variety
            # This ensures we're at position #3 (below position #2)
            offset = random.uniform(0.0005, 0.0015)  # 0.0005 = 0.05 cent, 0.0015 = 0.15 cent

            # Calculate our order prices at position #3
            # Simply take position #2 bid and subtract offset
            yes_price = yes_second_bid - offset
            no_price = no_second_bid - offset

            # Validate prices are within reasonable bounds
            # Some markets have very low/high prices (e.g., 0.002 or 0.998)
            # Only reject if prices are completely invalid (<0.0001 or >0.9999)
            if yes_price < 0.0001 or yes_price > 0.9999:
                logger.warning(f"❌ Invalid YES price: ${yes_price:.4f} ({yes_price*100:.2f}¢)")
                logger.warning(f"   Position #2 YES bid too extreme: ${yes_second_bid:.4f}")
                logger.warning(f"   REJECTING market")
                return None, None, {}

            if no_price < 0.0001 or no_price > 0.9999:
                logger.warning(f"❌ Invalid NO price: ${no_price:.4f} ({no_price*100:.2f}¢)")
                logger.warning(f"   Position #2 NO bid too extreme: ${no_second_bid:.4f}")
                logger.warning(f"   REJECTING market")
                return None, None, {}

            # Calculate spread between our YES bid and NO bid
            # In binary market: YES price + NO price should ≈ $1.00
            # Our spread = (1 - no_price) - yes_price
            # This represents the gap between our YES bid and the implied YES ask from our NO bid
            our_yes_ask_equivalent = 1 - no_price  # Convert NO bid to YES ask
            spread_dollars = our_yes_ask_equivalent - yes_price

            # Calculate spread percentage relative to mid price
            mid_price = (yes_mid_price + (1 - no_mid_price)) / 2  # Average of both mid prices
            spread_percent = spread_dollars / mid_price if mid_price > 0 else 0

            # 🔍 DEBUG: Log calculated prices and spreads
            logger.info(f"💰 Calculated prices (POSITION #3 STRATEGY - DIRECT FROM ORDERBOOKS):")
            logger.info(f"   YES Position #1 (Best Bid): ${yes_best_bid:.4f} ({yes_best_bid*100:.2f}¢)")
            logger.info(f"   YES Position #2 (Bid): ${yes_second_bid:.4f} ({yes_second_bid*100:.2f}¢)")
            logger.info(f"   NO Position #1 (Best Bid): ${no_best_bid:.4f} ({no_best_bid*100:.2f}¢)")
            logger.info(f"   NO Position #2 (Bid): ${no_second_bid:.4f} ({no_second_bid*100:.2f}¢)")
            logger.info(f"   Offset: ${offset:.4f} ({offset*100:.2f}¢)")
            logger.info(f"   Our YES bid (Position #3): ${yes_price:.4f} ({yes_price*100:.2f}¢)")
            logger.info(f"   Our NO bid (Position #3): ${no_price:.4f} ({no_price*100:.2f}¢)")
            logger.info(f"   Our YES ask (from NO): ${our_yes_ask_equivalent:.4f} ({our_yes_ask_equivalent*100:.2f}¢)")
            logger.info(f"   Spread: ${spread_dollars:.4f} ({spread_dollars*100:.2f}¢) = {spread_percent:.2%}")
            logger.info(f"   Max allowed spread: {max_spread:.2%}")

            # Check if spread exceeds max allowed
            if spread_percent > max_spread:
                logger.warning(f"❌ Spread too high ({spread_percent:.2%} > {max_spread:.2%})")
                logger.warning(f"   This indicates orderbook is too wide")
                logger.warning(f"   REJECTING market")
                return None, None, {}

            position_info = {
                'yes_price': yes_price,
                'no_price': no_price,
                'yes_best_bid': yes_best_bid,
                'yes_second_bid': yes_second_bid,
                'no_best_bid': no_best_bid,
                'no_second_bid': no_second_bid,
                'offset': offset,
                'spread': spread_percent,
                'max_spread_allowed': max_spread,
                'midpoint': mid_price,
                'num_yes_bids': len(yes_bids),
                'num_no_bids': len(no_bids),
                'target_position': 3  # We aim for position #3
            }

            return yes_price, no_price, position_info

        except Exception as e:
            logger.error(f"Error calculating prices: {e}")
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