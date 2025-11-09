"""
OrderBook WebSocket Module
Real-time order book updates via WebSocket for accurate order placement
"""

import asyncio
import websockets
import json
import logging
from typing import Dict, Optional, Callable
import time
from collections import defaultdict

logger = logging.getLogger(__name__)


class OrderBookWebSocket:
    """Manages WebSocket connection to Polymarket CLOB for real-time orderbook updates"""

    def __init__(self, ws_url: str = "wss://ws-subscriptions-clob.polymarket.com/ws/market"):
        """Initialize WebSocket connection manager

        Args:
            ws_url: WebSocket URL for Polymarket orderbook subscriptions
        """
        self.ws_url = ws_url
        self.ws_connection = None
        self.orderbook_cache = {}  # Cache orderbooks by token_id
        self.subscribed_tokens = set()  # Track subscribed token IDs
        self.callbacks = defaultdict(list)  # Callbacks for orderbook updates
        self.running = False
        self.reconnect_delay = 5  # seconds
        self.last_update_time = {}  # Track last update time per token

    async def connect(self):
        """Connect to WebSocket and start listening"""
        self.running = True

        while self.running:
            try:
                logger.info(f"🔌 Connecting to WebSocket: {self.ws_url}")

                async with websockets.connect(
                    self.ws_url,
                    ping_interval=20,
                    ping_timeout=10
                ) as websocket:
                    self.ws_connection = websocket
                    logger.info("✅ WebSocket connected successfully")

                    # Resubscribe to all tokens after reconnection
                    await self._resubscribe_all()

                    # Listen for messages
                    await self._listen()

            except websockets.exceptions.ConnectionClosed:
                logger.warning(f"⚠️  WebSocket connection closed, reconnecting in {self.reconnect_delay}s...")
                await asyncio.sleep(self.reconnect_delay)
            except Exception as e:
                logger.error(f"❌ WebSocket error: {e}")
                await asyncio.sleep(self.reconnect_delay)

    async def _listen(self):
        """Listen for WebSocket messages"""
        try:
            async for message in self.ws_connection:
                await self._process_message(message)
        except Exception as e:
            logger.error(f"Error listening to WebSocket: {e}")
            raise

    async def _process_message(self, message: str):
        """Process incoming WebSocket message

        Args:
            message: Raw WebSocket message (JSON string)
        """
        try:
            data = json.loads(message)

            # Log raw message for debugging
            logger.debug(f"📨 WebSocket message: {data}")

            # Handle different message types
            msg_type = data.get('type') or data.get('event_type')

            if msg_type == 'book':
                # Orderbook update
                await self._handle_orderbook_update(data)
            elif msg_type == 'last_trade_price':
                # Trade update (can be used to infer orderbook changes)
                logger.debug(f"💱 Trade update: {data}")
            elif msg_type == 'error':
                logger.error(f"❌ WebSocket error message: {data}")
            elif msg_type == 'subscribed':
                logger.info(f"✅ Subscribed to market: {data.get('market', 'unknown')}")
            else:
                logger.debug(f"🔍 Unknown message type: {msg_type}")

        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse WebSocket message: {e}")
        except Exception as e:
            logger.error(f"Error processing WebSocket message: {e}")

    async def _handle_orderbook_update(self, data: Dict):
        """Handle orderbook update message

        Args:
            data: Orderbook update data
        """
        try:
            # Extract token ID (could be 'asset_id', 'token_id', or 'market')
            token_id = data.get('asset_id') or data.get('token_id') or data.get('market')

            if not token_id:
                logger.warning(f"⚠️  Orderbook update missing token_id: {data}")
                return

            # Extract bids and asks
            bids = data.get('bids', [])
            asks = data.get('asks', [])

            # Update cache
            orderbook = {
                'bids': self._parse_orders(bids),
                'asks': self._parse_orders(asks),
                'timestamp': data.get('timestamp', time.time() * 1000),
                'market': token_id
            }

            self.orderbook_cache[token_id] = orderbook
            self.last_update_time[token_id] = time.time()

            logger.debug(f"📊 Updated orderbook for {token_id}:")
            logger.debug(f"   Bids: {len(orderbook['bids'])}, Asks: {len(orderbook['asks'])}")

            if orderbook['bids']:
                best_bid = orderbook['bids'][0]
                logger.debug(f"   Best Bid: ${best_bid['price']:.4f} x {best_bid['size']:.0f}")

            if orderbook['asks']:
                best_ask = orderbook['asks'][0]
                logger.debug(f"   Best Ask: ${best_ask['price']:.4f} x {best_ask['size']:.0f}")

            # Call registered callbacks
            await self._trigger_callbacks(token_id, orderbook)

        except Exception as e:
            logger.error(f"Error handling orderbook update: {e}")

    def _parse_orders(self, orders: list) -> list:
        """Parse order list from WebSocket format to standard format

        Args:
            orders: List of orders from WebSocket (could be [price, size] or {price, size})

        Returns:
            List of orders in standard format [{price, size}, ...]
        """
        parsed = []

        for order in orders:
            if isinstance(order, list) and len(order) >= 2:
                # Format: [price, size]
                parsed.append({
                    'price': float(order[0]),
                    'size': float(order[1])
                })
            elif isinstance(order, dict):
                # Format: {price: ..., size: ...}
                parsed.append({
                    'price': float(order.get('price', 0)),
                    'size': float(order.get('size', 0))
                })

        return parsed

    async def subscribe(self, token_id: str):
        """Subscribe to orderbook updates for a token

        Args:
            token_id: Token ID to subscribe to
        """
        if token_id in self.subscribed_tokens:
            logger.debug(f"Already subscribed to {token_id}")
            return

        if not self.ws_connection:
            logger.warning("WebSocket not connected, cannot subscribe")
            return

        try:
            # Subscribe message format for Polymarket
            subscribe_msg = {
                "type": "subscribe",
                "channel": "book",
                "market": token_id
            }

            await self.ws_connection.send(json.dumps(subscribe_msg))
            self.subscribed_tokens.add(token_id)

            logger.info(f"📡 Subscribed to orderbook for token: {token_id}")

        except Exception as e:
            logger.error(f"Failed to subscribe to {token_id}: {e}")

    async def unsubscribe(self, token_id: str):
        """Unsubscribe from orderbook updates

        Args:
            token_id: Token ID to unsubscribe from
        """
        if token_id not in self.subscribed_tokens:
            return

        if not self.ws_connection:
            return

        try:
            unsubscribe_msg = {
                "type": "unsubscribe",
                "channel": "book",
                "market": token_id
            }

            await self.ws_connection.send(json.dumps(unsubscribe_msg))
            self.subscribed_tokens.remove(token_id)

            # Remove from cache
            if token_id in self.orderbook_cache:
                del self.orderbook_cache[token_id]

            logger.info(f"📴 Unsubscribed from orderbook for token: {token_id}")

        except Exception as e:
            logger.error(f"Failed to unsubscribe from {token_id}: {e}")

    async def _resubscribe_all(self):
        """Resubscribe to all tokens after reconnection"""
        if not self.subscribed_tokens:
            return

        logger.info(f"🔄 Resubscribing to {len(self.subscribed_tokens)} tokens...")

        for token_id in list(self.subscribed_tokens):
            try:
                subscribe_msg = {
                    "type": "subscribe",
                    "channel": "book",
                    "market": token_id
                }
                await self.ws_connection.send(json.dumps(subscribe_msg))
                logger.debug(f"   ✅ Resubscribed to {token_id}")
            except Exception as e:
                logger.error(f"   ❌ Failed to resubscribe to {token_id}: {e}")

    def get_orderbook(self, token_id: str) -> Optional[Dict]:
        """Get cached orderbook for a token

        Args:
            token_id: Token ID

        Returns:
            Orderbook data or None if not available
        """
        orderbook = self.orderbook_cache.get(token_id)

        if orderbook:
            # Check if data is stale (older than 5 seconds)
            age = time.time() - self.last_update_time.get(token_id, 0)
            if age > 5:
                logger.warning(f"⚠️  Orderbook for {token_id} is stale ({age:.1f}s old)")

        return orderbook

    def register_callback(self, token_id: str, callback: Callable):
        """Register a callback for orderbook updates

        Args:
            token_id: Token ID to monitor
            callback: Async function to call on updates (receives orderbook dict)
        """
        self.callbacks[token_id].append(callback)
        logger.debug(f"📞 Registered callback for {token_id}")

    async def _trigger_callbacks(self, token_id: str, orderbook: Dict):
        """Trigger all callbacks for a token

        Args:
            token_id: Token ID
            orderbook: Updated orderbook data
        """
        for callback in self.callbacks[token_id]:
            try:
                await callback(orderbook)
            except Exception as e:
                logger.error(f"Error in callback for {token_id}: {e}")

    def is_connected(self) -> bool:
        """Check if WebSocket is connected"""
        return self.ws_connection is not None and self.ws_connection.open

    async def close(self):
        """Close WebSocket connection"""
        self.running = False

        if self.ws_connection:
            await self.ws_connection.close()
            logger.info("🔌 WebSocket connection closed")

    def get_stats(self) -> Dict:
        """Get WebSocket statistics

        Returns:
            Statistics dictionary
        """
        return {
            'connected': self.is_connected(),
            'subscribed_tokens': len(self.subscribed_tokens),
            'cached_orderbooks': len(self.orderbook_cache),
            'registered_callbacks': sum(len(cbs) for cbs in self.callbacks.values())
        }
