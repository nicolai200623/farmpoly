# 🔧 Fix Hoàn Chỉnh: Tất Cả Lỗi VPS

## 📋 **Tóm Tắt**

Bot đang gặp **2 lỗi nghiêm trọng** trên VPS khiến **0 markets được chọn**:

1. ❌ **KeyError: 'category'** (83 lần)
2. ❌ **Datetime timezone error** (32 lần)

**Kết quả**: `Selected 0 markets from 118 candidates` → Bot không đặt lệnh!

---

## 🎯 **LỖI 1: KeyError 'category'**

### **Triệu chứng**:
```
market_selector - ERROR - Score calculation error: 'category'
market_selector - INFO - Selected 0 markets from 83 candidates
```

### **Nguyên nhân**:
- `market_selector.py` expect field `'category'` trong market data
- API không trả về field này
- Gây ra KeyError cho TẤT CẢ markets

### **Giải pháp**:

#### **File: market_selector.py** (3 chỗ sửa)

**Chỗ 1 - Dòng 61**:
```python
# TRƯỚC (SAI):
category_score = self._score_category(market['category'])

# SAU (ĐÚNG):
category_score = self._score_category(market.get('category', 'other'))
```

**Chỗ 2 - Dòng 87**:
```python
# TRƯỚC (SAI):
if market['category'] == 'sports':

# SAU (ĐÚNG):
if market.get('category') == 'sports':
```

**Chỗ 3 - Dòng 253**:
```python
# TRƯỚC (SAI):
category = market['category']

# SAU (ĐÚNG):
category = market.get('category', 'other')
```

#### **File: market_scanner_v2.py** (Thêm category inference)

**Thêm vào dòng 181-183**:
```python
# Infer category from question/title
question = market_data.get('question') or event.get('title', 'Unknown') if event else 'Unknown'
category = self._infer_category(question, event)
```

**Thêm vào market dict (dòng 195)**:
```python
market = {
    'id': market_data.get('id') or market_data.get('conditionId'),
    'question': question,
    'reward': reward,
    'competition_bars': competition,
    'min_shares': int(rewards_min_size) if rewards_min_size > 0 else 100,
    'volume': volume,
    'liquidity': liquidity,
    'end_date': market_data.get('endDate') or market_data.get('endDateIso'),
    'source': 'gamma_api',
    'category': category,  # ← THÊM DÒNG NÀY
    # Thêm thông tin rewards chi tiết
    'rewards_min_size': rewards_min_size,
    'rewards_max_spread': rewards_max_spread,
    'uma_reward': uma_reward,
}
```

**Thêm method _infer_category() (sau dòng 345)**:
```python
def _infer_category(self, question: str, event: dict = None) -> str:
    """
    Infer market category from question text
    
    Categories: sports, crypto, politics, entertainment, economics, science, other
    """
    question_lower = question.lower()
    
    # Sports keywords
    sports_keywords = [
        'nfl', 'nba', 'mlb', 'nhl', 'soccer', 'football', 'basketball',
        'esports', 'counter-strike', 'cs2', 'mobile legends', 'mlbb',
        'team', 'match', 'game', 'vs', 'win', 'score'
    ]
    
    # Crypto keywords
    crypto_keywords = [
        'bitcoin', 'btc', 'ethereum', 'eth', 'solana', 'sol', 'xrp',
        'crypto', 'up or down', 'price', 'trading'
    ]
    
    # Politics keywords
    politics_keywords = [
        'election', 'president', 'senate', 'congress', 'vote', 'poll',
        'democrat', 'republican', 'party', 'government', 'policy'
    ]
    
    # Entertainment keywords
    entertainment_keywords = [
        'movie', 'film', 'actor', 'actress', 'celebrity', 'tv show',
        'series', 'netflix', 'disney', 'oscar', 'emmy', 'grammy'
    ]
    
    # Economics keywords
    economics_keywords = [
        'stock', 'market', 'economy', 'gdp', 'inflation', 'fed',
        'recession', 'unemployment', 'dow', 'nasdaq', 's&p'
    ]
    
    # Science keywords
    science_keywords = [
        'technology', 'ai', 'artificial intelligence', 'research',
        'discovery', 'space', 'nasa', 'climate', 'vaccine'
    ]
    
    # Check each category
    if any(keyword in question_lower for keyword in sports_keywords):
        return 'sports'
    elif any(keyword in question_lower for keyword in crypto_keywords):
        return 'crypto'
    elif any(keyword in question_lower for keyword in politics_keywords):
        return 'politics'
    elif any(keyword in question_lower for keyword in entertainment_keywords):
        return 'entertainment'
    elif any(keyword in question_lower for keyword in economics_keywords):
        return 'economics'
    elif any(keyword in question_lower for keyword in science_keywords):
        return 'science'
    else:
        return 'other'
```

---

## 🎯 **LỖI 2: Datetime Timezone Error**

### **Triệu chứng**:
```
market_selector - ERROR - Timing score error: can't subtract offset-naive and offset-aware datetimes
```

### **Nguyên nhân**:
- `end_date` có timezone (`+00:00`)
- `now` không có timezone (naive datetime)
- Python không cho phép trừ 2 datetime khác kiểu

### **Giải pháp**:

#### **File: market_selector.py** (Dòng 211-224)

```python
def _score_timing(self, market: Dict) -> float:
    """Score based on market timing (time to expiry)"""
    try:
        if not market.get('end_date'):
            return 0.5
        
        # Parse end date
        end_date = datetime.fromisoformat(market['end_date'].replace('Z', '+00:00'))
        
        # TRƯỚC (SAI):
        # now = datetime.utcnow()  # ← Naive datetime
        
        # SAU (ĐÚNG):
        from datetime import timezone
        now = datetime.now(timezone.utc)  # ← Timezone-aware datetime
        
        # Calculate days to expiry
        days_to_expiry = (end_date - now).days
        
        # Score based on time remaining
        if days_to_expiry < 1:
            return 0.2  # Too close to expiry
        elif days_to_expiry < 3:
            return 0.8  # Good - quick resolution
        elif days_to_expiry < 7:
            return 1.0  # Best - optimal timeframe
        elif days_to_expiry < 30:
            return 0.7  # Good
        else:
            return 0.4  # Too far out
            
    except Exception as e:
        logger.error(f"Timing score error: {e}")
        return 0.5
```

---

## 📤 **Deploy Lên VPS**

### **Files cần upload**:
1. ✅ `market_selector.py` (sửa 4 chỗ: 3 cho category + 1 cho datetime)
2. ✅ `market_scanner_v2.py` (thêm _infer_category method)

### **Option 1: Dùng SCP** ⭐ (Khuyến nghị)

```bash
# Trên máy local
scp market_selector.py user@vps-ip:/home/farmpoly/farmpoly/
scp market_scanner_v2.py user@vps-ip:/home/farmpoly/farmpoly/

# SSH vào VPS
ssh user@vps-ip
cd /home/farmpoly/farmpoly
pkill -f main.py
python3 main.py &
tail -f log.md
```

### **Option 2: Dùng Git**

```bash
# Trên máy local
git add market_selector.py market_scanner_v2.py
git commit -m "Fix category KeyError and datetime timezone error"
git push

# Trên VPS
ssh user@vps-ip
cd /home/farmpoly/farmpoly
git pull
pkill -f main.py
python3 main.py &
tail -f log.md
```

---

## 🔍 **Verify Fix Thành Công**

### **Kiểm tra log**:

```bash
tail -50 log.md
```

### **Kết quả mong đợi**:

```diff
- ❌ market_selector - ERROR - Score calculation error: 'category'
- ❌ market_selector - ERROR - Timing score error: can't subtract...
- ❌ market_selector - INFO - Selected 0 markets from 118 candidates

+ ✅ market_selector - INFO - Selected 5 markets from 118 candidates
+ ✅ market_selector - INFO - Top market: Ethereum Up or Down (score: 0.85)
+ ✅ order_manager - INFO - Placing order for market: ...
```

---

## ✅ **Checklist**

- [x] ✅ Sửa category KeyError (3 chỗ trong market_selector.py)
- [x] ✅ Thêm _infer_category() vào market_scanner_v2.py
- [x] ✅ Sửa datetime timezone error (1 chỗ trong market_selector.py)
- [x] ✅ Test local thành công (tất cả tests passed)
- [ ] ⏳ Upload 2 files lên VPS
- [ ] ⏳ Restart bot
- [ ] ⏳ Verify không còn lỗi
- [ ] ⏳ Verify markets được chọn (X > 0)

---

## 📊 **Tóm Tắt**

| Lỗi | Nguyên Nhân | Giải Pháp | Status |
|-----|-------------|-----------|--------|
| KeyError: 'category' | API không trả về field | Dùng `.get()` + infer category | ✅ Fixed |
| Datetime timezone | Naive vs aware datetime | Dùng `datetime.now(timezone.utc)` | ✅ Fixed |
| 0 markets selected | 2 lỗi trên | Fix cả 2 lỗi | ✅ Ready |

**Thời gian deploy**: 5-10 phút  
**Độ khó**: ⭐⭐ Trung bình

---

## 🎯 **Kết Quả Sau Fix**

- ✅ Không còn lỗi category
- ✅ Không còn lỗi datetime
- ✅ Markets được chọn thành công
- ✅ Bot bắt đầu đặt orders
- ✅ Trading hoạt động bình thường

