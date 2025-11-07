#!/usr/bin/env python3
"""
Test script để verify orderbook cho market Elon Musk tweets
URL: https://polymarket.com/event/elon-musk-of-tweets-october-31-november-7/elon-musk-of-tweets-october-31-november-7-140-159
"""

import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from py_clob_client.client import ClobClient
import logging
import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def test_elon_market():
    """Test market Elon Musk tweets để xem orderbook có đúng không"""

    # Market slug từ URL
    slug = "elon-musk-of-tweets-october-31-november-7-140-159"

    logger.info(f"=" * 80)
    logger.info(f"TESTING MARKET: {slug}")
    logger.info(f"=" * 80)

    # Step 1: Fetch market data từ Gamma API
    logger.info("\n📊 Step 1: Fetching market data from Gamma API...")

    gamma_url = f"https://gamma-api.polymarket.com/markets/{slug}"

    response = requests.get(gamma_url)
    if response.status_code != 200:
        logger.error(f"❌ Failed to fetch market: HTTP {response.status_code}")
        return

    market_data = response.json()

    # Log market info
    logger.info(f"\n✅ Market Info:")
    logger.info(f"   Question: {market_data.get('question', 'N/A')}")
    logger.info(f"   Market Type: {market_data.get('market_type', 'N/A')}")
    logger.info(f"   Condition ID: {market_data.get('condition_id', 'N/A')}")

    # Step 2: Get clob_token_ids
    tokens = market_data.get('tokens', [])
    logger.info(f"\n🔍 Step 2: Extracting clob_token_ids...")
    logger.info(f"   Found {len(tokens)} tokens in market")

    if len(tokens) == 0:
        logger.error("❌ No tokens found!")
        return

    for i, token in enumerate(tokens):
        logger.info(f"\n   Token {i}:")
        logger.info(f"      Outcome: {token.get('outcome', 'N/A')}")
        logger.info(f"      Token ID: {token.get('token_id', 'N/A')}")
        logger.info(f"      Winner: {token.get('winner', False)}")

    # Get token IDs
    clob_token_ids = [token.get('token_id') for token in tokens if token.get('token_id')]

    logger.info(f"\n   Extracted {len(clob_token_ids)} token IDs")

    if len(clob_token_ids) < 2:
        logger.warning(f"⚠️  Market has less than 2 tokens!")
        logger.warning(f"   This might be a categorical market, not binary YES/NO")

    # Step 3: Fetch orderbook cho từng token
    logger.info(f"\n📖 Step 3: Fetching orderbook for each token...")

    clob_client = ClobClient(host="https://clob.polymarket.com")

    for i, token_id in enumerate(clob_token_ids[:2], 1):  # Only test first 2 tokens
        logger.info(f"\n{'=' * 80}")
        logger.info(f"TOKEN {i}: {token_id}")
        logger.info(f"{'=' * 80}")

        try:
            # Fetch orderbook
            orderbook = clob_client.get_order_book(token_id)

            # Get bids and asks
            bids = orderbook.bids if orderbook.bids else []
            asks = orderbook.asks if orderbook.asks else []

            logger.info(f"\n📊 Orderbook Summary:")
            logger.info(f"   Total Bids: {len(bids)}")
            logger.info(f"   Total Asks: {len(asks)}")

            if bids:
                best_bid = float(bids[0].price)
                logger.info(f"   Best Bid: ${best_bid:.4f} ({best_bid*100:.2f}¢)")
            else:
                logger.warning(f"   No bids!")

            if asks:
                best_ask = float(asks[0].price)
                logger.info(f"   Best Ask: ${best_ask:.4f} ({best_ask*100:.2f}¢)")
            else:
                logger.warning(f"   No asks!")

            if bids and asks:
                spread = float(asks[0].price) - float(bids[0].price)
                mid_price = (float(bids[0].price) + float(asks[0].price)) / 2
                spread_pct = (spread / mid_price * 100) if mid_price > 0 else 999

                logger.info(f"   Mid Price: ${mid_price:.4f} ({mid_price*100:.2f}¢)")
                logger.info(f"   Spread: ${spread:.4f} ({spread*100:.2f}¢)")
                logger.info(f"   Spread %: {spread_pct:.2f}%")

                # Check if spread is too wide
                if spread_pct > 50:
                    logger.warning(f"⚠️  SPREAD TOO WIDE! {spread_pct:.2f}% > 50%")
                else:
                    logger.info(f"✅ Spread OK: {spread_pct:.2f}% <= 50%")

            # Show top 3 bids and asks
            logger.info(f"\n   Top 3 Bids:")
            for j, bid in enumerate(bids[:3], 1):
                price = float(bid.price)
                size = float(bid.size)
                logger.info(f"      {j}. ${price:.4f} ({price*100:.2f}¢) x {size:.0f}")

            logger.info(f"\n   Top 3 Asks:")
            for j, ask in enumerate(asks[:3], 1):
                price = float(ask.price)
                size = float(ask.size)
                logger.info(f"      {j}. ${price:.4f} ({price*100:.2f}¢) x {size:.0f}")

        except Exception as e:
            logger.error(f"❌ Error fetching orderbook for token {i}: {e}")

    # Step 4: Check if this is a binary or categorical market
    logger.info(f"\n{'=' * 80}")
    logger.info(f"ANALYSIS")
    logger.info(f"{'=' * 80}")

    if len(clob_token_ids) == 2:
        logger.info(f"\n✅ This is a BINARY market (2 tokens)")
        logger.info(f"   Token[0] should be YES")
        logger.info(f"   Token[1] should be NO")
    elif len(clob_token_ids) > 2:
        logger.warning(f"\n⚠️  This is a CATEGORICAL market ({len(clob_token_ids)} tokens)")
        logger.warning(f"   NOT a binary YES/NO market!")
        logger.warning(f"   Bot logic assumes binary markets - this may cause issues!")
    else:
        logger.error(f"\n❌ Invalid market - only {len(clob_token_ids)} token(s)")


if __name__ == "__main__":
    test_elon_market()
