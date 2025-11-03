#!/bin/bash
# Complete fix script cho tất cả lỗi VPS
# Chạy trên VPS: bash scripts/fix_vps_complete.sh

echo "================================================================================"
echo "🔧 COMPLETE FIX: Category KeyError + Datetime Timezone Error"
echo "================================================================================"

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Get script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

echo -e "\n📁 Project directory: ${GREEN}$PROJECT_DIR${NC}"

# Change to project directory
cd "$PROJECT_DIR" || exit 1

echo -e "\n📝 Vấn đề hiện tại:"
echo "   ❌ Lỗi 1: KeyError 'category' (83 lần)"
echo "   ❌ Lỗi 2: Datetime timezone error (32 lần)"
echo "   ❌ Kết quả: Selected 0 markets from 118 candidates"
echo "   ❌ Bot không đặt lệnh!"

echo -e "\n✅ Giải pháp:"
echo "   1. Fix category KeyError: Dùng .get('category', 'other')"
echo "   2. Fix datetime error: Dùng datetime.now(timezone.utc)"
echo "   3. Thêm _infer_category() để tự động phân loại markets"

echo -e "\n🔍 Checking files..."

# Check if files exist
if [ ! -f "market_selector.py" ]; then
    echo -e "${RED}❌ market_selector.py not found!${NC}"
    exit 1
fi

if [ ! -f "market_scanner_v2.py" ]; then
    echo -e "${RED}❌ market_scanner_v2.py not found!${NC}"
    exit 1
fi

echo -e "${GREEN}✅ Files found${NC}"

echo -e "\n📦 Files đã được sửa (trên local):"
echo "   - market_selector.py (4 chỗ: 3 category + 1 datetime)"
echo "   - market_scanner_v2.py (thêm _infer_category method)"

echo -e "\n${YELLOW}⚠️  QUAN TRỌNG:${NC}"
echo "   Bạn cần upload 2 files đã sửa lên VPS"

echo -e "\n📤 Cách upload:"
echo ""
echo -e "${GREEN}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}Option 1: Dùng SCP (Khuyến nghị)${NC}"
echo -e "${GREEN}═══════════════════════════════════════════════════════════════${NC}"
echo ""
echo "# Trên máy local:"
echo "scp market_selector.py user@vps-ip:/home/farmpoly/farmpoly/"
echo "scp market_scanner_v2.py user@vps-ip:/home/farmpoly/farmpoly/"
echo ""
echo "# SSH vào VPS:"
echo "ssh user@vps-ip"
echo "cd /home/farmpoly/farmpoly"
echo "pkill -f main.py"
echo "python3 main.py &"
echo "tail -f log.md"
echo ""
echo -e "${GREEN}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}Option 2: Dùng Git${NC}"
echo -e "${GREEN}═══════════════════════════════════════════════════════════════${NC}"
echo ""
echo "# Trên máy local:"
echo "git add market_selector.py market_scanner_v2.py"
echo "git commit -m 'Fix category KeyError and datetime timezone error'"
echo "git push"
echo ""
echo "# Trên VPS:"
echo "ssh user@vps-ip"
echo "cd /home/farmpoly/farmpoly"
echo "git pull"
echo "pkill -f main.py"
echo "python3 main.py &"
echo "tail -f log.md"
echo ""
echo -e "${GREEN}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}Option 3: Copy-Paste Manual${NC}"
echo -e "${GREEN}═══════════════════════════════════════════════════════════════${NC}"
echo ""
echo "# SSH vào VPS:"
echo "ssh user@vps-ip"
echo "cd /home/farmpoly/farmpoly"
echo ""
echo "# Backup files cũ:"
echo "cp market_selector.py market_selector.py.backup"
echo "cp market_scanner_v2.py market_scanner_v2.py.backup"
echo ""
echo "# Edit files (paste content từ local):"
echo "nano market_selector.py"
echo "nano market_scanner_v2.py"
echo ""
echo "# Restart bot:"
echo "pkill -f main.py"
echo "python3 main.py &"
echo "tail -f log.md"
echo ""

echo -e "\n✅ Kết quả mong đợi sau khi fix:"
echo ""
echo -e "${GREEN}TRƯỚC (LỖI):${NC}"
echo "  ❌ market_selector - ERROR - Score calculation error: 'category'"
echo "  ❌ market_selector - ERROR - Timing score error: can't subtract..."
echo "  ❌ market_selector - INFO - Selected 0 markets from 118 candidates"
echo ""
echo -e "${GREEN}SAU (ĐÚNG):${NC}"
echo "  ✅ market_selector - INFO - Selected 5 markets from 118 candidates"
echo "  ✅ market_selector - INFO - Top market: Ethereum Up or Down (score: 0.85)"
echo "  ✅ order_manager - INFO - Placing order for market: ..."
echo ""

echo -e "\n📊 Checklist:"
echo "  [x] Sửa category KeyError (3 chỗ)"
echo "  [x] Thêm _infer_category() method"
echo "  [x] Sửa datetime timezone error (1 chỗ)"
echo "  [x] Test local thành công"
echo "  [ ] Upload files lên VPS"
echo "  [ ] Restart bot"
echo "  [ ] Verify không còn lỗi"
echo "  [ ] Verify markets được chọn"

echo -e "\n================================================================================"
echo "✅ Script hoàn thành!"
echo "================================================================================"
echo ""
echo -e "${YELLOW}📖 Xem hướng dẫn chi tiết:${NC} FIX_VPS_ERRORS_COMPLETE.md"
echo ""

