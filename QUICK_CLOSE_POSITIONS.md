# ⚡ HƯỚNG DẪN NHANH - ĐÓNG VỊ THẾ THỦ CÔNG

## 🚀 Chạy ngay

```bash
python close_positions_manual.py
```

## 📋 Menu chính

```
1. Đóng vị thế cụ thể (nhập số thứ tự)
2. Đóng TẤT CẢ vị thế
3. Đóng chỉ vị thế ĐANG LÃI
4. Đóng chỉ vị thế ĐANG LỖ
5. Làm mới danh sách vị thế
0. Thoát
```

## 💡 Ví dụ nhanh

### Đóng vị thế số 1, 3, 5:
```
Nhập lựa chọn: 1
Nhập số thứ tự: 1,3,5
Gõ 'YES' để xác nhận: YES
```

### Đóng tất cả vị thế lãi:
```
Nhập lựa chọn: 3
Gõ 'YES' để xác nhận: YES
```

### Đóng tất cả:
```
Nhập lựa chọn: 2
Gõ 'YES' để xác nhận: YES
```

## ⚠️ Lưu ý

- ✅ Script đặt giá bán = giá hiện tại × 0.99 (giảm 1% để khớp nhanh)
- ✅ Cần có đủ MATIC để trả gas (~0.01-0.05 MATIC/lệnh)
- ✅ Lệnh thường khớp trong vài giây đến vài phút
- ✅ Kiểm tra kết quả trên https://polymarket.com/portfolio

## 🔧 Khắc phục lỗi

### "WALLET_1_PK không tìm thấy"
```bash
# Kiểm tra .env
cat .env | grep WALLET
```

### "Không có vị thế"
- Kiểm tra trên Polymarket.com
- Vị thế có thể đã đóng tự động

### "Failed to place order"
- Kiểm tra MATIC balance
- Làm mới danh sách (option 5)

## 📖 Hướng dẫn chi tiết

Xem file: `HUONG_DAN_DONG_VI_THE_THU_CONG.md`

---

**Chúc bạn trading thành công! 🚀**

