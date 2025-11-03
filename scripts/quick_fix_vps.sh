#!/bin/bash
# Quick fix script - chỉ cài psutil
# Chạy trên VPS: bash scripts/quick_fix_vps.sh

echo "🔧 Quick Fix: Installing psutil on VPS"
echo "========================================"

# Install psutil
echo "📦 Installing psutil..."
pip3 install psutil --user

# Verify
echo ""
echo "🔍 Verifying installation..."
python3 -c "import psutil; print(f'✅ psutil version: {psutil.__version__}')"

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ SUCCESS! psutil installed."
    echo ""
    echo "🚀 Next steps:"
    echo "   1. Restart bot: python3 main.py"
    echo "   2. Check logs: tail -f log.md"
else
    echo ""
    echo "❌ FAILED! Try:"
    echo "   pip3 install --upgrade pip"
    echo "   pip3 install psutil"
fi

