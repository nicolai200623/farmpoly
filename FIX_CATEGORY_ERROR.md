# 🔧 Fix: KeyError 'category' trong market_selector

## 📋 **Tóm Tắt Vấn Đề**

### **Lỗi hiện tại**:
```
market_selector - ERROR - Score calculation error: 'category'
market_selector - INFO - Selected 0 markets from 83 candidates
```

### **Nguyên nhân**:
- `market_selector.py` đang cố truy cập `market['category']`
- API **không trả về** field `'category'` trong market data
- Gây ra **KeyError** cho TẤT CẢ 83 markets
- Kết quả: **Không market nào được chọn** → Bot không đặt lệnh

### **Ảnh hưởng**:
- ❌ Bot tìm thấy 83 markets nhưng không chọn được market nào
- ❌ Không có orders được đặt
- ❌ Bot chạy nhưng hoàn toàn idle

---

## ✅ **Giải Pháp**

### **1. Sửa market_selector.py** (3 chỗ)

#### **Chỗ 1: Dòng 61** - Score calculation
```python
# TRƯỚC (SAI):
category_score = self._score_category(market['category'])

# SAU (ĐÚNG):
category_score = self._score_category(market.get('category', 'other'))
```

#### **Chỗ 2: Dòng 87** - Special conditions
```python
# TRƯỚC (SAI):
if market['category'] == 'sports':

# SAU (ĐÚNG):
if market.get('category') == 'sports':
```

#### **Chỗ 3: Dòng 253** - Portfolio constraints
```python
# TRƯỚC (SAI):
category = market['category']

# SAU (ĐÚNG):
category = market.get('category', 'other')
```

### **2. Thêm category vào market_scanner_v2.py**

#### **Thêm vào dòng 181-183**:
```python
# Infer category from question/title
question = market_data.get('question') or event.get('title', 'Unknown') if event else 'Unknown'
category = self._infer_category(question, event)
```

#### **Thêm vào market dict (dòng 195)**:
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
    # ...
}
```

#### **Thêm method _infer_category() (sau dòng 345)**:
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
    
    # ... (xem full code trong market_scanner_v2.py)
    
    # Check each category
    if any(keyword in question_lower for keyword in sports_keywords):
        return 'sports'
    elif any(keyword in question_lower for keyword in crypto_keywords):
        return 'crypto'
    # ... etc
    else:
        return 'other'
```

---

## 📤 **Cách Deploy Lên VPS**

### **Option 1: Dùng SCP** (Khuyến nghị)

```bash
# Trên máy local
scp market_selector.py user@vps-ip:/home/farmpoly/farmpoly/
scp market_scanner_v2.py user@vps-ip:/home/farmpoly/farmpoly/

# SSH vào VPS và restart bot
ssh user@vps-ip
cd /home/farmpoly/farmpoly
pkill -f main.py
python3 main.py
```

### **Option 2: Dùng Git**

```bash
# Trên máy local
git add market_selector.py market_scanner_v2.py
git commit -m "Fix KeyError: category in market_selector"
git push

# Trên VPS
ssh user@vps-ip
cd /home/farmpoly/farmpoly
git pull
pkill -f main.py
python3 main.py
```

### **Option 3: Copy-Paste Manual**

```bash
# SSH vào VPS
ssh user@vps-ip
cd /home/farmpoly/farmpoly

# Backup files cũ
cp market_selector.py market_selector.py.backup
cp market_scanner_v2.py market_scanner_v2.py.backup

# Edit files
nano market_selector.py
# (Paste nội dung từ local)

nano market_scanner_v2.py
# (Paste nội dung từ local)

# Restart bot
pkill -f main.py
python3 main.py
```

---

## 🔍 **Verify Fix Thành Công**

### **Check log sau khi restart**:

```bash
tail -f log.md
```

### **Kết quả mong đợi**:

```
✅ TRƯỚC (LỖI):
market_selector - ERROR - Score calculation error: 'category'
market_selector - ERROR - Score calculation error: 'category'
... (83 lần)
market_selector - INFO - Selected 0 markets from 83 candidates

✅ SAU (ĐÚNG):
market_selector - INFO - Selected 5 markets from 83 candidates
market_selector - INFO - Top market: Ethereum Up or Down (score: 125.3)
order_manager - INFO - Placing order for market: ...
```

### **Không còn lỗi**:
- ❌ `Score calculation error: 'category'`
- ✅ Markets được chọn thành công
- ✅ Orders được đặt

---

## 📊 **Checklist**

- [ ] Sửa `market_selector.py` (3 chỗ)
- [ ] Thêm `_infer_category()` vào `market_scanner_v2.py`
- [ ] Thêm `'category'` vào market dict
- [ ] Upload 2 files lên VPS
- [ ] Restart bot trên VPS
- [ ] Check log verify không còn lỗi
- [ ] Verify markets được chọn (Selected X markets, X > 0)
- [ ] Verify orders được đặt

---

## 🎯 **Tóm Tắt**

| Vấn Đề | Giải Pháp | Files Sửa |
|--------|-----------|-----------|
| KeyError: 'category' | Dùng `.get('category', 'other')` | market_selector.py |
| API không trả về category | Tự động infer từ question text | market_scanner_v2.py |
| 0 markets selected | Fix lỗi → markets được chọn | Cả 2 files |

**Thời gian ước tính**: 5-10 phút

**Độ khó**: ⭐⭐ Trung bình (cần upload files lên VPS)

---

## 💡 **Lưu Ý**

1. **Backup trước khi sửa**: Luôn backup files cũ
2. **Test local trước**: Đã test thành công trên Windows local
3. **Restart bot**: Nhớ restart bot sau khi upload
4. **Monitor logs**: Theo dõi logs để verify fix thành công

---

## 📞 **Nếu Vẫn Gặp Vấn Đề**

Cung cấp:
1. Output của `tail -50 log.md`
2. Output của `python3 -c "import market_selector; print('OK')"`
3. Output của `python3 -c "import market_scanner_v2; print('OK')"`

