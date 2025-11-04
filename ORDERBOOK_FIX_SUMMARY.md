# 🔧 ORDERBOOK 404 ERROR - ĐÃ SỬA

## 📋 TÓM TẮT VẤN ĐỀ

### **Lỗi trước khi sửa:**
```
order_manager - ERROR - Error getting order book: PolyApiException[status_code=404, 
error_message={'error': 'No orderbook exists for the requested token id'}]
```

**Tần suất:** ~400 lỗi trong 10 phút (4 markets × ~100 lần/market)

**Nguyên nhân:**
- Bot sử dụng `market['id']` (condition ID) để fetch orderbook
- CLOB API yêu cầu `token_id` (contract address), không phải condition ID
- Gamma API trả về `clobTokenIds` nhưng bot không sử dụng

**Hậu quả:**
- ✅ Market selection hoạt động (4 markets selected)
- ❌ Không fetch được orderbook
- ❌ Không tính được giá để đặt lệnh
- ❌ **0 orders placed**

---

## ✅ GIẢI PHÁP ĐÃ TRIỂN KHAI

### **1. Sửa config.yaml (Lỗi cú pháp)**

**File:** `config.yaml` dòng 54-55

**Trước:**
```yaml
# Position size range (number of shares)
 size_min: 50   # ← Thừa 1 space
 size_max: 100  # ← Thừa 1 space
```

**Sau:**
```yaml
# Position size range (number of shares)
  size_min: 50   # ✅ Đúng indentation
  size_max: 100  # ✅ Đúng indentation
```

---

### **2. Sửa market_scanner_v2.py (Lấy token IDs)**

**File:** `market_scanner_v2.py` dòng 185-214

**Thêm code parse `clobTokenIds`:**
```python
# Parse clobTokenIds (JSON string array)
clob_token_ids = []
try:
    import json
    clob_token_ids_str = market_data.get('clobTokenIds', '[]')
    if isinstance(clob_token_ids_str, str):
        clob_token_ids = json.loads(clob_token_ids_str)
    elif isinstance(clob_token_ids_str, list):
        clob_token_ids = clob_token_ids_str
except Exception as e:
    logger.debug(f"Could not parse clobTokenIds: {e}")

market = {
    'id': market_data.get('id') or market_data.get('conditionId'),
    'condition_id': market_data.get('conditionId'),  # ✅ Store condition ID
    'clob_token_ids': clob_token_ids,  # ✅ Store CLOB token IDs
    'question': question,
    # ... rest of fields
}
```

**Kết quả:**
- Mỗi market giờ có `clob_token_ids` array
- Ví dụ: `["5634754...", "20238019..."]` (YES token, NO token)

---

### **3. Sửa order_manager.py (Sử dụng token IDs)**

#### **3.1. Hàm `_get_order_book()` - Dòng 127-155**

**Trước:**
```python
async def _get_order_book(self, market_id: str) -> Optional[Dict]:
    book = self.clob_client.get_order_book(market_id)  # ❌ Dùng market_id
```

**Sau:**
```python
async def _get_order_book(self, market_id: str, token_id: str = None) -> Optional[Dict]:
    lookup_id = token_id if token_id else market_id
    book = self.clob_client.get_order_book(lookup_id)  # ✅ Dùng token_id
```

#### **3.2. Hàm `_fetch_market_data()` - Dòng 92-104**

**Trước:**
```python
async def _fetch_market_data(self, market_id: str) -> Optional[Dict]:
    order_book = await self._get_order_book(market_id)  # ❌ Không truyền token_id
```

**Sau:**
```python
async def _fetch_market_data(self, market_id: str, token_id: str = None) -> Optional[Dict]:
    order_book = await self._get_order_book(market_id, token_id)  # ✅ Truyền token_id
```

#### **3.3. Hàm `prepare_market_order()` - Dòng 43-99**

**Thêm logic lấy token_id:**
```python
async def prepare_market_order(self, market: Dict) -> Dict:
    # ✅ Get token_id from market data
    token_id = None
    if market.get('clob_token_ids') and len(market['clob_token_ids']) > 0:
        token_id = market['clob_token_ids'][0]  # Use first token (YES)
        logger.debug(f"Using token_id: {token_id} for market {market['id']}")
    
    # ✅ Pass token_id to fetch market data
    market_data = await self._fetch_market_data(market['id'], token_id)
    
    # ✅ Store token_ids in order for later use
    order = {
        'market_id': market['id'],
        'token_ids': market.get('clob_token_ids', []),  # Store for order placement
        # ... rest of order
    }
```

#### **3.4. Hàm `place_order()` - Dòng 225-279**

**Trước:**
```python
async def place_order(self, order: Dict, wallet: Dict) -> Optional[Dict]:
    # Place YES side
    yes_order_id = await self._place_single_order(
        order['yes_order'],
        order['market_id'],  # ❌ Dùng market_id cho cả YES và NO
        wallet
    )
```

**Sau:**
```python
async def place_order(self, order: Dict, wallet: Dict) -> Optional[Dict]:
    # ✅ Get token IDs for YES and NO outcomes
    token_ids = order.get('token_ids', [])
    yes_token_id = token_ids[0]  # First token is YES
    no_token_id = token_ids[1]   # Second token is NO
    
    # Place YES side
    yes_order_id = await self._place_single_order(
        order['yes_order'],
        yes_token_id,  # ✅ Dùng YES token ID
        wallet
    )
    
    # Place NO side
    no_order_id = await self._place_single_order(
        order['no_order'],
        no_token_id,  # ✅ Dùng NO token ID
        wallet
    )
```

---

## 🔍 CÁCH HOẠT ĐỘNG

### **Flow mới:**

1. **Market Scanner** fetch từ Gamma API
   - Parse `clobTokenIds` từ response
   - Lưu vào `market['clob_token_ids']`

2. **Market Selector** chọn markets
   - Markets đã có `clob_token_ids` sẵn

3. **Order Manager** prepare order
   - Lấy `token_id` từ `market['clob_token_ids'][0]`
   - Fetch orderbook bằng `token_id` (không phải market_id)
   - Tính giá thành công ✅

4. **Order Manager** place order
   - Dùng `token_ids[0]` cho YES order
   - Dùng `token_ids[1]` cho NO order
   - Đặt lệnh thành công ✅

---

## 📊 KẾT QUẢ MONG ĐỢI

### **Trước khi sửa:**
```
✅ Markets scanned: 142
✅ Markets selected: 4
❌ Orderbook fetch: FAILED (404 error × 400)
❌ Orders placed: 0
❌ Profit: $0.00
```

### **Sau khi sửa:**
```
✅ Markets scanned: 142
✅ Markets selected: 4
✅ Orderbook fetch: SUCCESS (using token_id)
✅ Orders placed: 8 (4 markets × 2 sides)
💰 Profit: TBD (bot sẽ bắt đầu trade)
```

---

## 🚀 HÀNH ĐỘNG TIẾP THEO

### **1. Khởi động lại bot trên VPS**
```bash
# Dừng bot hiện tại
Ctrl+C

# Pull code mới từ repo (nếu đã push)
git pull

# Hoặc copy files đã sửa lên VPS

# Chạy lại bot
python main.py
```

### **2. Monitor log trong 5-10 phút đầu**

**Kiểm tra:**
- ✅ Không còn lỗi 404 orderbook
- ✅ Log hiển thị: `Using token_id: ... for market ...`
- ✅ Log hiển thị: `Prepared order for market ... with spread ...`
- ✅ Log hiển thị: `Placed orders for market ...: {'yes': '...', 'no': '...'}`

**Lệnh xem log:**
```bash
# Xem log realtime
tail -f nohup.out

# Hoặc search cho "token_id"
grep "token_id" nohup.out

# Search cho "Placed orders"
grep "Placed orders" nohup.out
```

### **3. Kiểm tra sau 1 giờ**

**Xem hourly report:**
- Orders placed > 0 ✅
- Orders filled > 0 (nếu có cơ hội tốt)
- Profit (có thể âm/dương tùy market)

---

## ⚠️ LƯU Ý

1. **Bot vẫn ở TEST MODE** (100 USDC approved)
   - Để thoát warning, approve ≥1,000 USDC
   - Nhưng bot VẪN ĐẶT LỆNH THẬT với $100

2. **Vốn nhỏ ($100) = Ít cơ hội**
   - Bot chỉ đặt lệnh khi spread đủ lớn
   - Có thể mất vài giờ mới có order đầu tiên
   - Bình thường, không phải lỗi

3. **Monitor MATIC balance**
   - Mỗi order tốn ~0.01-0.05 MATIC gas
   - Đảm bảo có ≥0.5 MATIC trong wallet

4. **Nếu vẫn gặp lỗi:**
   - Check log chi tiết
   - Verify `clob_token_ids` có trong market data
   - Test với 1 market cụ thể

---

## 📝 FILES ĐÃ SỬA

1. ✅ `config.yaml` - Sửa indentation lỗi
2. ✅ `market_scanner_v2.py` - Parse và lưu `clobTokenIds`
3. ✅ `order_manager.py` - Sử dụng token_id thay vì market_id

**Tổng số dòng code thay đổi:** ~80 dòng

---

## 🎯 SUMMARY

**Vấn đề:** Bot không fetch được orderbook vì dùng sai ID type

**Giải pháp:** Parse `clobTokenIds` từ Gamma API và dùng đúng token_id

**Kết quả:** Bot giờ có thể fetch orderbook và đặt lệnh thành công

**Next step:** Restart bot và monitor logs để confirm fix hoạt động

---

**Ngày sửa:** 2025-11-04  
**Người sửa:** AI Assistant  
**Status:** ✅ READY TO TEST

