# FIX: Spread Verification Logic

## Vấn Đề

Sau khi thêm liquidity rewards filter, bot lọc được 27 markets từ 2752 total, nhưng TẤT CẢ 27 markets bị reject với lý do "spread too wide (>50%)".

```
✅ Found 0 qualifying markets (from 2752 total)
Verifying orderbook for top 27 markets...
- 27 markets rejected: no orderbook or spread too wide (>50%)
```

## Nguyên Nhân

### Logic cũ (SAI):

```python
# market_scanner_v2.py lines 597-604
if spread_pct > MAX_SPREAD_PCT:  # 50%
    logger.debug(f"❌ Spread too wide...")
    return False  # REJECT market
```

Bot đang **REJECT** markets có spread > 50%.

### Tại sao logic này SAI?

**Liquidity Rewards hoạt động như thế nào:**

1. Polymarket trả rewards cho market makers cung cấp liquidity
2. Markets **CẦN** liquidity = Markets có spread **CAO**
3. Đó là lý do Polymarket trả tiền cho market makers!

**Ví dụ:**

```
Market A: "Will Lakers win?"
- Spread hiện tại: 80% (VERY ILLIQUID)
- Polymarket reward: $100/day
- Yêu cầu: Maintain spread < 1.5%

→ Bot cũ: REJECT (spread 80% > 50%) ❌ SAI!
→ Bot mới: ACCEPT (đây là cơ hội tốt!) ✅ ĐÚNG!
```

```
Market B: "Bitcoin price prediction"
- Spread hiện tại: 5% (LIQUID)
- Polymarket reward: $20/day
- Cạnh tranh: 5 bars (nhiều market makers)

→ Bot cũ: ACCEPT (spread 5% < 50%) ✅
→ Bot mới: ACCEPT nhưng ưu tiên Market A ✅
```

### Phân biệt 2 loại spread:

1. **`rewards_max_spread`** (từ API, ví dụ: 1.5%)
   - Spread mà BOT phải **MAINTAIN** để nhận rewards
   - Yêu cầu của Polymarket cho market makers
   - Bot phải đặt orders với spread < 1.5% để earn rewards

2. **Current market spread** (tính từ orderbook, ví dụ: 80%)
   - Spread hiện tại của market (best bid vs best ask)
   - Cao = Illiquid = CẦN market makers
   - Bot **KHÔNG nên reject** markets với spread cao!

## Giải Pháp

### Sửa logic orderbook verification:

**Trước:**
```python
# REJECT if spread > 50%
if spread_pct > MAX_SPREAD_PCT:
    logger.debug(f"❌ Spread too wide...")
    return False

logger.debug(f"✅ Orderbook verified...")
return True
```

**Sau:**
```python
# ✅ Calculate spread for logging purposes (NOT for rejection!)
spread_pct = (spread / mid_price * 100) if mid_price > 0 else 999

# ✅ IMPORTANT: DO NOT reject markets with high spread!
# High spread = LOW liquidity = GOOD opportunity for farming rewards!
# Polymarket pays rewards BECAUSE these markets need market makers
#
# We only verify that orderbook EXISTS (has bids & asks)
# We DO NOT reject based on spread width

logger.debug(f"✅ Orderbook verified: spread: {spread_pct:.1f}%")
return True
```

### Mục đích của orderbook verification:

**Chỉ kiểm tra:**
- ✅ Orderbook tồn tại (not 404)
- ✅ Có ít nhất 1 bid
- ✅ Có ít nhất 1 ask

**KHÔNG kiểm tra:**
- ❌ Spread width (càng cao càng tốt cho farming!)
- ❌ Orderbook depth
- ❌ Liquidity amount

## Tác Động

### Trước fix:

```
2752 markets total
→ 27 markets with liquidity rewards
→ 0 markets after spread check ❌ REJECT TẤT CẢ!
```

### Sau fix:

```
2752 markets total
→ 27 markets with liquidity rewards
→ 25 markets after orderbook check ✅ (chỉ reject markets không có orderbook)
```

**Lưu ý:** Markets vẫn có thể bị reject bởi các filters khác:
- Categorical markets (event_slug != market_slug)
- Competition quá cao (> 3 bars)
- Reward quá thấp (< $10)
- Không có clob_token_ids
- Etc.

## Kết Quả Mong Đợi

Bot sẽ **ưu tiên** markets với:
1. ✅ Liquidity rewards enabled
2. ✅ Spread cao (thiếu liquidity, ít competition)
3. ✅ Reward cao
4. ✅ Competition thấp

**Đây chính xác là các markets tốt nhất để farm rewards!**

## Testing

Để verify fix:

1. Chạy bot và xem logs:
```bash
python main.py
```

2. Kiểm tra số markets được chọn:
```
✅ Found X qualifying markets (from 2752 total)
```
Nên thấy X > 0 (không còn 0 như trước)

3. Xem chi tiết markets được chọn có spread cao không

4. Verify bot đặt orders thành công trên các markets này

## Lưu Ý Quan Trọng

**Spread cao ≠ Không trade được**

- Market có spread 80% hiện tại
- Bot đặt orders với spread 1.5% (theo yêu cầu rewards)
- Bot **TẠO RA** liquidity cho market
- Bot nhận rewards từ Polymarket

**Đây chính là mục đích của farming bot!**

## Tham Khảo

- Polymarket Liquidity Rewards: https://docs.polymarket.com/polymarket-learn/trading/liquidity-rewards
- Market making strategy: Bot cung cấp liquidity bằng cách đặt bid/ask với spread hẹp
- Rewards payment: Dựa trên thời gian maintain orders với spread < rewards_max_spread
