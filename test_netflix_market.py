"""
Test script để kiểm tra Netflix market structure
Xác định xem bot có đang lấy categorical market outcomes làm binary markets không
"""

import asyncio
import aiohttp
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def test_rewards_api():
    """Test /rewards API để tìm Netflix market"""

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Referer': 'https://polymarket.com/rewards',
        'Origin': 'https://polymarket.com'
    }

    netflix_markets = []

    async with aiohttp.ClientSession(headers=headers) as session:
        next_cursor = 'MA=='
        page_num = 1

        while page_num <= 10:  # Check first 10 pages
            url = "https://polymarket.com/api/rewards/markets"
            params = {
                'orderBy': 'market',
                'position': 'DESC',
                'query': '',
                'showFavorites': 'false',
                'tagSlug': 'all',
                'nextCursor': next_cursor,
                'requestPath': '/rewards/user/markets',
                'onlyMergeable': 'false',
                'noCompetition': 'false',
                'onlyOpenOrders': 'false',
                'onlyPositions': 'false'
            }

            logger.info(f"📄 Checking page {page_num}...")

            async with session.get(url, params=params) as response:
                if response.status != 200:
                    logger.error(f"❌ Failed: HTTP {response.status}")
                    break

                data = await response.json()

                if isinstance(data, list):
                    markets_data = data
                else:
                    markets_data = data.get('data', [])

                if not markets_data:
                    break

                # Tìm Netflix markets
                for market_data in markets_data:
                    question = market_data.get('question', '')
                    if 'NFLX' in question or 'Netflix' in question:
                        netflix_markets.append(market_data)
                        logger.info(f"✅ Found Netflix market: {question[:80]}")

                # Get next cursor
                prev_cursor = next_cursor
                if isinstance(data, dict):
                    next_cursor = data.get('next_cursor') or data.get('nextCursor')
                else:
                    next_cursor = None

                if not next_cursor or next_cursor == prev_cursor:
                    break

                page_num += 1

    return netflix_markets


async def analyze_market_structure(market_data):
    """Phân tích cấu trúc của market để xem có phải categorical không"""

    print("\n" + "="*80)
    print("📊 MARKET STRUCTURE ANALYSIS")
    print("="*80)

    question = market_data.get('question', '')
    market_id = market_data.get('market_id', '')
    market_slug = market_data.get('market_slug', '')
    event_slug = market_data.get('event_slug', '')

    print(f"\n❓ Question: {question}")
    print(f"🆔 Market ID: {market_id}")
    print(f"📝 Market Slug: {market_slug}")
    print(f"📝 Event Slug: {event_slug}")

    # Kiểm tra tokens
    tokens = market_data.get('tokens', [])
    print(f"\n🎯 Number of tokens: {len(tokens)}")

    for i, token in enumerate(tokens, 1):
        token_id = token.get('token_id', '')
        outcome = token.get('outcome', '')
        print(f"   Token {i}: {outcome} (ID: {token_id})")

    # Extract rewards
    reward = 0
    if 'rewards_config' in market_data and market_data['rewards_config']:
        for config in market_data['rewards_config']:
            reward += float(config.get('rate_per_day', 0))

    competition = market_data.get('market_competitiveness', 0)

    print(f"\n💰 Reward: ${reward}")
    print(f"📊 Competition: {competition} bars")

    # Kiểm tra nếu đây là categorical market
    if len(tokens) > 2:
        print(f"\n⚠️  CATEGORICAL MARKET DETECTED!")
        print(f"   This market has {len(tokens)} outcomes, not binary YES/NO")
        print(f"   Bot should REJECT this market!")
    elif len(tokens) == 2:
        print(f"\n✅ BINARY MARKET")
        print(f"   This market has 2 outcomes (YES/NO)")
    else:
        print(f"\n❌ INVALID MARKET")
        print(f"   This market has only {len(tokens)} token(s)")

    # Kiểm tra xem có phải là một outcome của categorical market không
    # Bằng cách fetch Gamma API với event_slug
    if event_slug:
        print(f"\n🔍 Checking if this is part of a categorical event...")
        await check_gamma_api(event_slug, market_slug)

    return market_data


async def check_gamma_api(event_slug, market_slug):
    """Kiểm tra Gamma API để xem event có bao nhiêu markets"""

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    }

    # Try both event slug and market slug
    for slug_type, slug in [('event', event_slug), ('market', market_slug)]:
        if not slug:
            continue

        try:
            url = f"https://gamma-api.polymarket.com/events?slug={slug}"

            async with aiohttp.ClientSession(headers=headers) as session:
                async with session.get(url, timeout=aiohttp.ClientTimeout(total=10)) as response:
                    if response.status != 200:
                        continue

                    data = await response.json()

                    if isinstance(data, list) and len(data) > 0:
                        event = data[0]
                    elif isinstance(data, dict):
                        event = data
                    else:
                        continue

                    markets = event.get('markets', [])

                    print(f"\n📦 Gamma API ({slug_type} slug: {slug}):")
                    print(f"   Total markets in event: {len(markets)}")

                    if len(markets) > 1:
                        print(f"\n   ⚠️  THIS IS A CATEGORICAL EVENT!")
                        print(f"   Event has {len(markets)} different outcomes:")
                        for i, market in enumerate(markets[:10], 1):  # Show first 10
                            print(f"      {i}. {market.get('question', 'N/A')[:60]}")

                        if len(markets) > 10:
                            print(f"      ... and {len(markets) - 10} more")
                    elif len(markets) == 1:
                        print(f"   ✅ This is a standalone market")
                        # Check tokens in this market
                        market = markets[0]
                        tokens = market.get('tokens', [])
                        print(f"   Tokens: {len(tokens)}")
                        for token in tokens:
                            print(f"      - {token.get('outcome', 'N/A')}")

                    return

        except Exception as e:
            logger.debug(f"Error checking {slug_type} slug: {e}")


async def main():
    """Main test function"""

    print("\n" + "="*80)
    print("🔍 TESTING NETFLIX MARKET STRUCTURE")
    print("="*80)

    # Step 1: Get Netflix markets from /rewards API
    print("\n📡 Step 1: Fetching Netflix markets from /rewards API...")
    netflix_markets = await test_rewards_api()

    if not netflix_markets:
        print("\n❌ No Netflix markets found in /rewards API")
        return

    print(f"\n✅ Found {len(netflix_markets)} Netflix market(s)")

    # Step 2: Analyze each market
    for i, market_data in enumerate(netflix_markets, 1):
        print(f"\n{'='*80}")
        print(f"📊 ANALYZING MARKET {i}/{len(netflix_markets)}")
        await analyze_market_structure(market_data)

    print("\n" + "="*80)
    print("✅ ANALYSIS COMPLETE")
    print("="*80)


if __name__ == "__main__":
    asyncio.run(main())
