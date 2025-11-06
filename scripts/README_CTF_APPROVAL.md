# CTF Approval Guide

## 🎯 Tại sao cần CTF Approval?

Khi trade trên Polymarket, bạn cần approve **2 loại contract**:

### 1. USDC Approval (đã có)
- **Mục đích:** Cho phép Exchange lấy USDC từ ví bạn để **MUA** outcome tokens
- **Script:** `scripts/approve_wallets.py`
- **Trạng thái:** ✅ Đã có sẵn trong bot

### 2. CTF Approval (MỚI - cần thiết!)
- **Mục đích:** Cho phép Exchange lấy outcome tokens từ ví bạn để **BÁN** chúng
- **Script:** `scripts/approve_ctf.py` (mới tạo)
- **Trạng thái:** ⚠️ Cần chạy ngay!

## ❌ Lỗi khi thiếu CTF Approval

```
❌ Error closing position: PolyApiException[status_code=400, 
   error_message={'error': 'not enough balance / allowance'}]
```

**Nguyên nhân:**
- Bot có outcome tokens trong ví
- Bot có signature hợp lệ
- Nhưng Exchange **KHÔNG có quyền** lấy outcome tokens từ ví bạn
- → Không thể đóng vị thế!

## 🔧 Cách sử dụng

### Bước 1: Kiểm tra trạng thái hiện tại

```bash
python scripts/check_ctf_approval.py
```

**Output mẫu:**
```
🔍 CTF Approval Status Checker
======================================================================

Wallet 1/1: 0x1234567...89abcdef
  ❌ NOT APPROVED - CTF Exchange
  ❌ NOT APPROVED - Neg Risk CTF Exchange
  ❌ NOT APPROVED - Neg Risk Adapter
  ❌ Not approved (0/3)

======================================================================
📈 SUMMARY
======================================================================

✅ Fully approved: 0/1
⚠️  Partially approved: 0/1
❌ Not approved: 1/1

❌ No wallets are approved!
   You MUST run: python scripts/approve_ctf.py
```

### Bước 2: Approve CTF contracts

```bash
python scripts/approve_ctf.py
```

**Script sẽ:**
1. Load tất cả wallets từ `.env`
2. Kiểm tra MATIC balance (cần ~0.03 MATIC/wallet cho gas)
3. Approve 3 operators cho mỗi wallet:
   - **CTF Exchange** - cho normal markets
   - **Neg Risk CTF Exchange** - cho negative risk markets
   - **Neg Risk Adapter** - cho negative risk markets

**Output mẫu:**
```
🔐 CTF Approval Tool for Polymarket Trading
======================================================================

📝 What is CTF approval?
   CTF (Conditional Token Framework) approval allows Polymarket
   exchanges to transfer your outcome tokens when you SELL them.

⚠️  This is REQUIRED to:
   - Close positions (sell outcome tokens)
   - Take profits
   - Exit markets

💡 You only need to run this ONCE per wallet.
======================================================================

✅ Loaded 1 wallets

⚠️  You are about to approve CTF for 1 wallets
   This will approve 3 operators per wallet:
   - CTF Exchange (for normal markets)
   - Neg Risk CTF Exchange (for negative risk markets)
   - Neg Risk Adapter (for negative risk markets)

   Total transactions: 3
   Gas cost: ~0.01 MATIC per transaction (~0.03 MATIC per wallet)

Continue? (yes/no): yes

🚀 Starting CTF approval process...
======================================================================

======================================================================
Wallet 1/1: 0x1234567...89abcdef
======================================================================

🔄 Approving CTF Exchange...
📤 Approval transaction sent: 0xabc123...
   Operator: CTF Exchange
⏳ Waiting for confirmation...
✅ Approval confirmed! Gas used: 46234

🔄 Approving Neg Risk CTF Exchange...
✅ Already approved for Neg Risk CTF Exchange

🔄 Approving Neg Risk Adapter...
✅ Already approved for Neg Risk Adapter

✅ Wallet 1 fully approved (3/3)

======================================================================
📊 FINAL RESULTS
======================================================================

✅ FULL - 0x1234567...89abcdef

======================================================================
Total: 1/1 wallets fully approved
======================================================================

✅ All wallets approved! You can now:
   - Close positions
   - Take profits
   - Sell outcome tokens

   Run: python main.py
```

### Bước 3: Restart bot

```bash
python main.py
```

Bot sẽ tự động đóng vị thế Netflix trong vòng 5 phút! 🎉

## 📊 Chi tiết kỹ thuật

### CTF Contract Addresses (Polygon Mainnet)

```python
CTF_ADDRESS = '0x4D97DCd97eC945f40cF65F87097ACe5EA0476045'
CLOB_EXCHANGE_ADDRESS = '0x4bFb41d5B3570DeFd03C39a9A4D8dE6Bd8B8982E'
NEG_RISK_CTF_EXCHANGE = '0xC5d563A36AE78145C45a50134d48A1215220f80a'
NEG_RISK_ADAPTER = '0xd91E80cF2E7be2e162c6513ceD06f1dD0dA35296'
```

### Function được gọi

```solidity
function setApprovalForAll(address operator, bool approved) external;
```

**Parameters:**
- `operator`: Địa chỉ Exchange contract
- `approved`: `true` để approve, `false` để revoke

### Gas Cost

- **Mỗi approval:** ~46,000 gas (~0.01 MATIC)
- **Mỗi wallet:** 3 approvals = ~0.03 MATIC
- **Chỉ cần approve 1 lần**, dùng mãi mãi!

## 🔒 Bảo mật

### Có an toàn không?

✅ **HOÀN TOÀN AN TOÀN!**

**Lý do:**
1. Chỉ approve cho **official Polymarket contracts** (đã audit)
2. Chỉ approve **outcome tokens** (ERC1155), KHÔNG phải USDC
3. Không thể rút USDC từ ví bạn
4. Chỉ cho phép Exchange **chuyển outcome tokens khi bạn đặt lệnh SELL**

### Tương tự như:

- Approve USDC cho Uniswap để swap
- Approve NFT cho OpenSea để bán
- Approve tokens cho DEX để trade

### Có thể revoke không?

✅ **CÓ!** Chạy lại script với `approved=False`:

```python
# Revoke approval
ctf_contract.functions.setApprovalForAll(operator, False)
```

Nhưng sau khi revoke, bạn sẽ **KHÔNG thể đóng vị thế** nữa!

## ❓ FAQ

### Q: Tại sao cần approve 3 operators?

**A:** Polymarket có 3 loại markets:
- **Normal markets** → CTF Exchange
- **Negative risk markets** → Neg Risk CTF Exchange + Adapter
- Approve cả 3 để bot hoạt động với mọi loại market

### Q: Có cần approve lại không?

**A:** KHÔNG! Approve 1 lần, dùng mãi mãi (trừ khi bạn revoke).

### Q: Nếu thiếu MATIC thì sao?

**A:** Script sẽ báo lỗi. Bạn cần nạp thêm MATIC vào ví (recommend 0.1 MATIC).

### Q: Có thể approve từng phần không?

**A:** CÓ! Script sẽ skip các operators đã approved. Nếu approve fail, chạy lại script là được.

### Q: Tại sao không tích hợp vào approve_wallets.py?

**A:** 
- Tách riêng để dễ debug
- USDC approval cho BUY, CTF approval cho SELL
- Có thể chạy độc lập khi cần

## 🎉 Kết quả mong đợi

Sau khi approve CTF:

1. ✅ Vị thế Netflix (120% profit) sẽ tự động đóng
2. ✅ Nhận ~$20.50 profit
3. ✅ Nhận Telegram notification
4. ✅ Bot có thể tự động chốt lời cho tất cả vị thế
5. ✅ Bot hoạt động đầy đủ chức năng!

## 📚 Tham khảo

- [Official Polymarket CTF Approval Script](https://gist.github.com/poly-rodr/44313920481de58d5a3f6d1f8226bd5e)
- [Gnosis Conditional Token Framework](https://docs.gnosis.io/conditionaltokens/)
- [Polymarket CLOB API Docs](https://docs.polymarket.com/)

