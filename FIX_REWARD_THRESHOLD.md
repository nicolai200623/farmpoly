# Fix: Bot Rejecting All Markets với "reward < $300"

## 🔍 Vấn đề phát hiện

Bot đang reject TẤT CẢ 57 markets với lý do "reward < $300", mặc dù `config.yaml` đã set `min_reward: 100`.

## 🎯 Nguyên nhân

### 1. **Công thức tính reward SAI**
- API trả về markets với `umaReward = 2` (UMA tokens)
- Bot tính: `reward = umaReward * 100 = 2 * 100 = $200`
- Công thức này **KHÔNG CHÍNH XÁC** - cần research thêm về UMA rewards

### 2. **Default config hardcoded = 300**
- File `main.py` có default config với `min_reward: 300`
- File `market_scanner_v2.py` cũng có default value = 300
- Khi bot không đọc được config.yaml, nó sẽ dùng default này

### 3. **Không có logging để debug**
- Không biết bot đang dùng config nào
- Không biết giá trị min_reward thực tế là bao nhiêu

## ✅ Giải pháp đã áp dụng

### 1. **Sửa default config trong `main.py`**
```python
# BEFORE
'min_reward': 300,

# AFTER  
'min_reward': 100,  # FIXED: match config.yaml
```

### 2. **Sửa logic đọc config trong `market_scanner_v2.py`**
```python
# BEFORE
self.min_reward = scanner_config.get('min_reward', 300)

# AFTER
# Handle both nested and direct config
if 'min_reward' in config:
    self.min_reward = config.get('min_reward', 100)
else:
    scanner_config = config.get('market_scanner', {})
    self.min_reward = scanner_config.get('min_reward', 100)

# Log the actual values
logger.info(f"📊 Market Scanner initialized with min_reward=${self.min_reward}")
```

### 3. **Thêm logging khi load config**
```python
logger.info(f"📂 Loading config from: {path}")
logger.info(f"✅ Config loaded successfully")
logger.info(f"   - min_reward: {scanner_config.get('min_reward')}")
logger.info(f"   - max_competition_bars: {scanner_config.get('max_competition_bars')}")
```

### 4. **Sửa file test `test_bot.py`**
```python
# BEFORE
'min_reward': 300,

# AFTER
'min_reward': 100,  # FIXED: match config.yaml
```

## 📊 Kết quả

### Test trên local:
```
✅ Config loaded successfully!
📊 Market Scanner Config:
   - min_reward: 100
   - max_competition_bars: 2
   
✅ MarketScannerV2 initialized
   - scanner.min_reward: 100
   
✅ ALL TESTS PASSED!
```

### Sau khi deploy lên VPS:
Bot sẽ:
1. Log ra giá trị config khi khởi động
2. Sử dụng `min_reward = 100` thay vì 300
3. Chấp nhận các markets có reward >= $100
4. Với 57 markets có reward = $200, TẤT CẢ sẽ pass filter

## 🚀 Cách deploy

```bash
# 1. Commit changes
git add .
git commit -m "fix: Sửa min_reward default từ 300 xuống 100, thêm logging"

# 2. Push to VPS
git push origin master

# 3. Trên VPS
git pull
sudo systemctl restart farmpoly-bot

# 4. Kiểm tra log
tail -f log.md
```

## 📝 Điều cần lưu ý

### 1. **Về `illiquid_threshold: 10000`**
- Đây là **LIQUIDITY** (thanh khoản), KHÔNG phải volume
- Markets với liquidity < $10k = ít tiền trong order book = dễ kiếm rewards
- Bot ưu tiên markets có liquidity thấp

### 2. **Về UMA Rewards**
- Hiện tại bot tính: `umaReward * 100`
- Công thức này có thể KHÔNG CHÍNH XÁC
- Cần research thêm về:
  - 1 UMA token = bao nhiêu USD?
  - UMA rewards được trả như thế nào?
  - Có nên trade markets chỉ có UMA rewards?

### 3. **Monitoring sau khi deploy**
Kiểm tra log để đảm bảo:
- ✅ Config được load đúng: `min_reward: 100`
- ✅ Scanner initialized với `min_reward=$100`
- ✅ Markets được tìm thấy và pass filter
- ✅ Orders được place thành công

## 🔧 Files đã sửa

1. `main.py` - Sửa default config, thêm logging
2. `market_scanner_v2.py` - Sửa logic đọc config, thêm logging
3. `test_bot.py` - Sửa test config
4. `test_config_loading.py` - Script test mới
5. `test_api.py` - Script debug API

## ⚠️ Vấn đề cần theo dõi

1. **Reward calculation accuracy**: Công thức `umaReward * 100` có thể sai
2. **Market quality**: Markets với reward $200 có đáng trade không?
3. **Fill rate**: Với min_reward thấp hơn, fill rate có tăng không?

## 📚 Tài liệu tham khảo

- Config: `config.yaml` line 15
- Scanner: `market_scanner_v2.py` line 21-42
- Main: `main.py` line 69-114

