# ⚡ Quick Fix VPS - 2 Lỗi Nghiêm Trọng

## 🚨 **Vấn Đề**

Bot tìm thấy 118 markets nhưng **chọn 0 markets** → Không đặt lệnh!

**2 lỗi**:
1. ❌ `KeyError: 'category'` (83 lần)
2. ❌ `Datetime timezone error` (32 lần)

---

## ⚡ **Quick Fix (5 phút)**

### **Bước 1: Upload 2 files**

```bash
# Trên máy local
scp market_selector.py user@vps:/home/farmpoly/farmpoly/
scp market_scanner_v2.py user@vps:/home/farmpoly/farmpoly/
```

### **Bước 2: Restart bot**

```bash
# SSH vào VPS
ssh user@vps
cd /home/farmpoly/farmpoly
pkill -f main.py
python3 main.py &
```

### **Bước 3: Verify**

```bash
tail -f log.md
```

**Kết quả mong đợi**:
```
✅ Selected 5 markets from 118 candidates
✅ Top market: Ethereum Up or Down (score: 0.85)
✅ Placing order for market: ...
```

---

## 📝 **Chi Tiết Sửa**

### **Lỗi 1: Category KeyError**
- **File**: `market_selector.py` (3 chỗ)
- **Fix**: Dùng `market.get('category', 'other')` thay vì `market['category']`

### **Lỗi 2: Datetime Timezone**
- **File**: `market_selector.py` (1 chỗ)
- **Fix**: Dùng `datetime.now(timezone.utc)` thay vì `datetime.utcnow()`

### **Bonus: Category Inference**
- **File**: `market_scanner_v2.py`
- **Thêm**: Method `_infer_category()` để tự động phân loại markets

---

## ✅ **Đã Test**

- ✅ Test local: 5/5 tests passed
- ✅ Category inference: 8/9 correct
- ✅ Datetime calculation: All passed
- ✅ Error handling: All passed

---

## 📖 **Docs**

- **Chi tiết**: `FIX_VPS_ERRORS_COMPLETE.md`
- **Script**: `scripts/fix_vps_complete.sh`
- **Tests**: `scripts/test_category_fix.py`, `scripts/test_datetime_fix.py`

