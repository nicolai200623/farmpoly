# FIX: Liquidity Rewards Filtering

## Vấn Đề

Bot đang nhận notifications về các markets có rewards, nhưng khi kiểm tra thủ công trên https://polymarket.com/rewards thì những markets đó KHÔNG CÓ trong danh sách.

### Nguyên nhân:

Polymarket có **nhiều loại rewards khác nhau**:

1. **Liquidity Rewards (Reward Daily)** ✅ Đây là loại chúng ta cần
   - Hiển thị trên https://polymarket.com/rewards
   - Dành cho market makers cung cấp liquidity
   - Có yêu cầu:
     - `rewards_min_size > 0`: Minimum order size
     - `rewards_max_spread > 0`: Maximum spread limit
   - Được trả HÀNG NGÀY khi maintain orders

2. **Các loại rewards khác** ❌ KHÔNG phải liquidity rewards
   - Trading rewards
   - Event-specific rewards
   - Campaign rewards
   - Không có yêu cầu min_size và max_spread
   - Không phải reward hàng ngày cho market making

### Vấn đề trong code cũ:

Bot đang lấy **TẤT CẢ** markets có `rewards_config` từ API `/api/rewards/markets`, không phân biệt loại rewards.

**Files bị ảnh hưởng:**
1. `playwright_rewards_scraper.py` - Scraper chính lấy data từ /api/rewards/markets
2. `polymarket_rewards_api.py` - API wrapper cho rewards endpoint

## Giải Pháp

### Thêm filter để chỉ chấp nhận LIQUIDITY REWARDS:

```python
# ✅ FILTER: Check if this is a LIQUIDITY REWARDS market
rewards_min_size = float(market_data.get('rewards_min_size', 0) or 0)
rewards_max_spread = float(market_data.get('rewards_max_spread', 0) or 0)

# Skip markets without LIQUIDITY REWARDS indicators
# Only accept if BOTH conditions are true:
# 1. rewards_min_size > 0 (requires minimum order size)
# 2. rewards_max_spread > 0 (requires spread limit)
if rewards_min_size == 0 or rewards_max_spread == 0:
    logger.debug(f"⏭️  Skipped (not liquidity rewards): {question[:60]}")
    return None  # Skip this market
```

### Tại sao filter này đúng?

**Liquidity Rewards** có đặc điểm:
- ✅ `rewards_min_size > 0` - Yêu cầu order phải đủ lớn (thường 100-500 USDC)
- ✅ `rewards_max_spread > 0` - Yêu cầu spread phải hẹp (thường < 1.5%)
- ✅ Hiển thị trên /rewards page

**Các rewards khác** (trading, events, etc.):
- ❌ `rewards_min_size = 0` HOẶC `rewards_max_spread = 0`
- ❌ Không yêu cầu maintain orders
- ❌ Không hiển thị trên /rewards page

## Thay Đổi Code

### 1. `playwright_rewards_scraper.py`

**Trước:**
```python
# Extract reward from rewards_config
reward = 0
if 'rewards_config' in market_data and market_data['rewards_config']:
    for config in market_data['rewards_config']:
        reward += float(config.get('rate_per_day', 0))
# ... add market to list without checking
all_markets.append(market)
```

**Sau:**
```python
# ✅ FILTER 1: Check if this is a LIQUIDITY REWARDS market
rewards_min_size = float(market_data.get('rewards_min_size', 0) or 0)
rewards_max_spread = float(market_data.get('rewards_max_spread', 0) or 0)

if rewards_min_size == 0 or rewards_max_spread == 0:
    logger.debug(f"⏭️  Skipped (not liquidity rewards): {question[:60]}")
    continue  # Skip this market

# Extract reward from rewards_config
reward = 0
if 'rewards_config' in market_data and market_data['rewards_config']:
    for config in market_data['rewards_config']:
        reward += float(config.get('rate_per_day', 0))
# ... only add if passed filter
all_markets.append(market)
```

### 2. `polymarket_rewards_api.py`

**Trước:**
```python
def parse_market(self, market_data: dict) -> Optional[Dict]:
    try:
        # Extract reward from rewards_config
        reward = 0
        if 'rewards_config' in market_data and market_data['rewards_config']:
            for config in market_data['rewards_config']:
                reward += float(config.get('rate_per_day', 0))
        # ... return market
        return market
```

**Sau:**
```python
def parse_market(self, market_data: dict) -> Optional[Dict]:
    try:
        # ✅ FILTER: Check if this is a LIQUIDITY REWARDS market
        rewards_min_size = float(market_data.get('rewards_min_size', 0) or 0)
        rewards_max_spread = float(market_data.get('rewards_max_spread', 0) or 0)

        if rewards_min_size == 0 or rewards_max_spread == 0:
            logger.debug(f"⏭️  Skipped (not liquidity rewards): {question[:60]}")
            return None  # Skip this market

        # Extract reward from rewards_config
        reward = 0
        if 'rewards_config' in market_data and market_data['rewards_config']:
            for config in market_data['rewards_config']:
                reward += float(config.get('rate_per_day', 0))
        # ... return market
        return market
```

## Kết Quả Mong Đợi

### Trước fix:

```
🔍 Scanning markets...
✅ Found 250 markets with rewards_config
📊 Filter results: 50/250 markets passed

Markets included:
- Market A: Liquidity rewards ($100/day) ✅ ĐÚNG
- Market B: Trading rewards ($50/day) ❌ SAI - không phải liquidity rewards
- Market C: Event rewards ($200/day) ❌ SAI - không phải liquidity rewards
```

### Sau fix:

```
🔍 Scanning markets...
✅ Found 250 markets with rewards_config
⏭️  Skipped (not liquidity rewards): Market B - minSize=0, maxSpread=0
⏭️  Skipped (not liquidity rewards): Market C - minSize=0, maxSpread=0
📊 Filter results: 20/250 markets passed (only liquidity rewards)

Markets included:
- Market A: Liquidity rewards ($100/day) ✅ ĐÚNG
  - rewards_min_size: 200
  - rewards_max_spread: 0.015 (1.5%)
```

## Lợi Ích

1. **Chính xác hơn**: Chỉ trade markets có liquidity rewards thực sự
2. **Giảm nhiễu**: Không nhận notifications về markets không liên quan
3. **Đúng mục đích**: Bot được thiết kế để farm liquidity rewards, không phải trading rewards
4. **Khớp với /rewards page**: Chỉ lấy markets hiển thị trên https://polymarket.com/rewards

## Testing

Để verify fix hoạt động:

1. Chạy bot và xem logs:
```bash
python main.py
```

2. Kiểm tra xem có messages "Skipped (not liquidity rewards)" không

3. So sánh markets bot chọn với markets trên https://polymarket.com/rewards

4. Đảm bảo tất cả markets bot chọn đều có trên /rewards page

## Tham Khảo

- Polymarket Liquidity Rewards: https://docs.polymarket.com/polymarket-learn/trading/liquidity-rewards
- API endpoint: https://polymarket.com/api/rewards/markets
- Rewards page: https://polymarket.com/rewards
