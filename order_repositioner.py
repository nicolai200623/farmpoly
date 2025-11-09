"""
Order Repositioner Module
Automatically adjusts orders to maintain position 2-3 in orderbook based on real-time updates
"""

import asyncio
import logging
from typing import Dict, Optional
import time

logger = logging.getLogger(__name__)


class OrderRepositioner:
    """Monitors orderbook changes and repositions orders to maintain target position"""

    def __init__(self, order_manager, orderbook_ws, config: dict):
        """Initialize order repositioner

        Args:
            order_manager: OrderManager instance
            orderbook_ws: OrderBookWebSocket instance
            config: Configuration dict
        """
        self.order_manager = order_manager
        self.orderbook_ws = orderbook_ws
        self.config = config

        # Track order positions
        self.monitored_orders = {}  # market_id -> order details

        # Configuration
        self.check_interval = config.get('reposition_check_interval', 15)  # seconds
        self.min_reposition_gap = config.get('min_reposition_gap', 0.002)  # $0.002 = 0.2 cents
        self.max_repositions_per_hour = config.get('max_repositions_per_hour', 10)
        self.reposition_cooldown = config.get('reposition_cooldown', 60)  # seconds

        # Statistics
        self.repositions_count = 0
        self.last_reposition_time = {}

    async def monitor_and_reposition(self):
        """Main loop to monitor and reposition orders"""
        logger.info("🔄 Starting order repositioning loop")

        while True:
            try:
                # Check all active orders
                active_orders = self.order_manager.active_orders

                for market_id, order in active_orders.items():
                    await self._check_and_reposition_order(market_id, order)

                # Wait before next check
                await asyncio.sleep(self.check_interval)

            except Exception as e:
                logger.error(f"Error in repositioning loop: {e}")
                await asyncio.sleep(30)

    async def _check_and_reposition_order(self, market_id: str, order: Dict):
        """Check if order needs repositioning and reposition if necessary

        Args:
            market_id: Market ID
            order: Order details
        """
        try:
            # Skip if in cooldown
            last_reposition = self.last_reposition_time.get(market_id, 0)
            if time.time() - last_reposition < self.reposition_cooldown:
                logger.debug(f"⏳ Order {market_id} in cooldown, skipping")
                return

            # Get token IDs
            token_ids = order.get('token_ids', [])
            if len(token_ids) < 2:
                return

            yes_token_id = token_ids[0]
            no_token_id = token_ids[1]

            # Get real-time orderbooks from WebSocket
            yes_orderbook = self.orderbook_ws.get_orderbook(yes_token_id)
            no_orderbook = self.orderbook_ws.get_orderbook(no_token_id)

            if not yes_orderbook or not no_orderbook:
                logger.debug(f"⏳ Orderbooks not available yet for {market_id}")
                return

            # Get our current order prices
            our_yes_price = order.get('yes_order', {}).get('price')
            our_no_price = order.get('no_order', {}).get('price')

            if not our_yes_price or not our_no_price:
                return

            # Check if we need to reposition
            needs_reposition, reason = self._check_if_needs_reposition(
                yes_orderbook, no_orderbook,
                our_yes_price, our_no_price
            )

            if needs_reposition:
                logger.info(f"🔄 Repositioning order for {market_id}: {reason}")
                await self._reposition_order(market_id, order, yes_orderbook, no_orderbook)

        except Exception as e:
            logger.error(f"Error checking order {market_id}: {e}")

    def _check_if_needs_reposition(
        self,
        yes_orderbook: Dict,
        no_orderbook: Dict,
        our_yes_price: float,
        our_no_price: float
    ) -> tuple[bool, str]:
        """Check if order needs repositioning

        Args:
            yes_orderbook: YES token orderbook
            no_orderbook: NO token orderbook
            our_yes_price: Our current YES bid price
            our_no_price: Our current NO bid price

        Returns:
            Tuple of (needs_reposition: bool, reason: str)
        """
        try:
            # Get bids from orderbooks
            yes_bids = yes_orderbook.get('bids', [])
            no_bids = no_orderbook.get('bids', [])

            if len(yes_bids) < 3 or len(no_bids) < 3:
                return False, "Not enough bids in orderbook"

            # Find our position in YES orderbook
            yes_position = self._find_our_position(yes_bids, our_yes_price)
            no_position = self._find_our_position(no_bids, our_no_price)

            logger.debug(f"📊 Current positions - YES: #{yes_position}, NO: #{no_position}")

            # ✅ TARGET: Position 2 or 3 (0-indexed: position 1 or 2)
            # If we're at position 1 (best bid), we need to move down
            # If we're at position 4+ or not in top 10, we need to move up

            # Check YES position
            if yes_position == 0:
                return True, f"YES order at position #1 (too aggressive, target #2-3)"
            elif yes_position > 3:
                return True, f"YES order at position #{yes_position + 1} (too passive, target #2-3)"

            # Check NO position
            if no_position == 0:
                return True, f"NO order at position #1 (too aggressive, target #2-3)"
            elif no_position > 3:
                return True, f"NO order at position #{no_position + 1} (too passive, target #2-3)"

            # Check if price gap is too large (market moved significantly)
            yes_second_bid = yes_bids[1]['price']
            no_second_bid = no_bids[1]['price']

            yes_gap = abs(our_yes_price - yes_second_bid)
            no_gap = abs(our_no_price - no_second_bid)

            if yes_gap > self.min_reposition_gap:
                return True, f"YES price gap too large: ${yes_gap:.4f} ({yes_gap*100:.2f}¢)"

            if no_gap > self.min_reposition_gap:
                return True, f"NO price gap too large: ${no_gap:.4f} ({no_gap*100:.2f}¢)"

            return False, "Position OK"

        except Exception as e:
            logger.error(f"Error checking reposition need: {e}")
            return False, f"Error: {e}"

    def _find_our_position(self, bids: list, our_price: float) -> int:
        """Find our order's position in the orderbook

        Args:
            bids: List of bids from orderbook
            our_price: Our bid price

        Returns:
            Position (0-indexed, 0 = best bid)
        """
        for i, bid in enumerate(bids):
            bid_price = bid.get('price', 0)

            # Check if this is our order (within 0.0001 tolerance)
            if abs(bid_price - our_price) < 0.0001:
                return i

        # Not found in top bids
        return 999

    async def _reposition_order(
        self,
        market_id: str,
        order: Dict,
        yes_orderbook: Dict,
        no_orderbook: Dict
    ):
        """Reposition order to target position

        Args:
            market_id: Market ID
            order: Current order details
            yes_orderbook: YES token orderbook
            no_orderbook: NO token orderbook
        """
        try:
            # Get bids
            yes_bids = yes_orderbook.get('bids', [])
            no_bids = no_orderbook.get('bids', [])

            if len(yes_bids) < 3 or len(no_bids) < 3:
                logger.warning(f"⚠️  Not enough bids to reposition {market_id}")
                return

            # Calculate new prices at position #2 (0-indexed: position 1)
            # Add small offset to ensure we're at position #2-3, not #1
            yes_second_bid = yes_bids[1]['price']
            no_second_bid = no_bids[1]['price']

            # Small random offset to avoid exact match with existing orders
            import random
            offset = random.uniform(0.0005, 0.0010)  # 0.05-0.10 cents

            new_yes_price = yes_second_bid - offset
            new_no_price = no_second_bid - offset

            # Validate prices
            if new_yes_price < 0.001 or new_yes_price > 0.999:
                logger.warning(f"⚠️  Invalid YES price: ${new_yes_price:.4f}")
                return

            if new_no_price < 0.001 or new_no_price > 0.999:
                logger.warning(f"⚠️  Invalid NO price: ${new_no_price:.4f}")
                return

            # Get order IDs
            order_ids = order.get('order_ids', {})
            yes_order_id = order_ids.get('yes')
            no_order_id = order_ids.get('no')

            if not yes_order_id or not no_order_id:
                logger.warning(f"⚠️  Missing order IDs for {market_id}")
                return

            # Cancel existing orders
            logger.info(f"🗑️  Cancelling existing orders for {market_id}")
            await self.order_manager.cancel_order(yes_order_id, reason="Repositioning")
            await asyncio.sleep(0.5)
            await self.order_manager.cancel_order(no_order_id, reason="Repositioning")
            await asyncio.sleep(0.5)

            # Create new orders at updated prices
            logger.info(f"📤 Placing new orders at position #2-3")
            logger.info(f"   YES: ${new_yes_price:.4f} ({new_yes_price*100:.2f}¢)")
            logger.info(f"   NO: ${new_no_price:.4f} ({new_no_price*100:.2f}¢)")

            # Update order details
            order['yes_order']['price'] = new_yes_price
            order['no_order']['price'] = new_no_price

            # Get wallet for placing new orders
            from wallet_manager import WalletManager
            wallet_mgr = WalletManager(self.config.get('wallet_management', {}))
            wallet = await wallet_mgr.get_next_wallet()

            # Place new orders
            result = await self.order_manager.place_order(order, wallet)

            if result:
                logger.info(f"✅ Successfully repositioned orders for {market_id}")
                self.repositions_count += 1
                self.last_reposition_time[market_id] = time.time()
            else:
                logger.warning(f"⚠️  Failed to place repositioned orders for {market_id}")

        except Exception as e:
            logger.error(f"Error repositioning order {market_id}: {e}")

    def get_stats(self) -> Dict:
        """Get repositioning statistics

        Returns:
            Statistics dictionary
        """
        return {
            'total_repositions': self.repositions_count,
            'monitored_orders': len(self.monitored_orders),
            'last_reposition': max(self.last_reposition_time.values()) if self.last_reposition_time else 0
        }
