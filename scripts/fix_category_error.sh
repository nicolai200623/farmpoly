#!/bin/bash
# Fix script cho lỗi KeyError: 'category'
# Chạy trên VPS: bash scripts/fix_category_error.sh

echo "================================================================================"
echo "🔧 FIX: KeyError 'category' in market_selector"
echo "================================================================================"

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Get script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

echo -e "\n📁 Project directory: ${GREEN}$PROJECT_DIR${NC}"

# Change to project directory
cd "$PROJECT_DIR" || exit 1

echo -e "\n📝 Vấn đề:"
echo "   - market_selector.py đang expect field 'category' trong market data"
echo "   - API không trả về field này"
echo "   - Gây ra lỗi: Score calculation error: 'category'"
echo "   - Kết quả: Selected 0 markets from 83 candidates"

echo -e "\n✅ Giải pháp:"
echo "   1. Sửa market_selector.py: Dùng market.get('category', 'other')"
echo "   2. Thêm _infer_category() vào market_scanner_v2.py"
echo "   3. Tự động infer category từ question text"

echo -e "\n🔍 Checking files..."

# Check if files exist
if [ ! -f "market_selector.py" ]; then
    echo -e "${YELLOW}⚠️  market_selector.py not found!${NC}"
    exit 1
fi

if [ ! -f "market_scanner_v2.py" ]; then
    echo -e "${YELLOW}⚠️  market_scanner_v2.py not found!${NC}"
    exit 1
fi

echo -e "${GREEN}✅ Files found${NC}"

echo -e "\n📦 Files đã được sửa (trên local):"
echo "   - market_selector.py (3 chỗ)"
echo "   - market_scanner_v2.py (thêm _infer_category method)"

echo -e "\n${YELLOW}⚠️  QUAN TRỌNG:${NC}"
echo "   Bạn cần upload 2 files đã sửa lên VPS:"
echo "   1. market_selector.py"
echo "   2. market_scanner_v2.py"

echo -e "\n📤 Cách upload:"
echo "   ${GREEN}Option 1: Dùng scp${NC}"
echo "   scp market_selector.py user@vps:/home/farmpoly/farmpoly/"
echo "   scp market_scanner_v2.py user@vps:/home/farmpoly/farmpoly/"

echo -e "\n   ${GREEN}Option 2: Dùng git${NC}"
echo "   git add market_selector.py market_scanner_v2.py"
echo "   git commit -m 'Fix KeyError category'"
echo "   git push"
echo "   # Trên VPS:"
echo "   cd /home/farmpoly/farmpoly && git pull"

echo -e "\n   ${GREEN}Option 3: Copy-paste qua SSH${NC}"
echo "   # Mở 2 terminal windows"
echo "   # Terminal 1 (local): cat market_selector.py"
echo "   # Terminal 2 (VPS): nano market_selector.py (paste content)"

echo -e "\n🔄 Sau khi upload, restart bot:"
echo "   ${GREEN}pkill -f main.py${NC}"
echo "   ${GREEN}python3 main.py${NC}"

echo -e "\n✅ Kết quả mong đợi:"
echo "   - Không còn lỗi 'Score calculation error: category'"
echo "   - Markets được chọn thành công"
echo "   - Log hiển thị: 'Selected X markets from 83 candidates' (X > 0)"

echo -e "\n================================================================================"
echo "✅ Script hoàn thành!"
echo "================================================================================"

