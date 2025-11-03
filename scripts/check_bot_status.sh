#!/bin/bash

# Farmpoly Bot Status Checker
# Kiểm tra bot có đang farm trên Polymarket không

echo "============================================================"
echo "FARMPOLY BOT STATUS CHECKER"
echo "============================================================"
echo ""

# 1. Check systemd service
echo "1. SYSTEMD SERVICE STATUS:"
echo "-----------------------------------------------------------"
sudo systemctl status farmpoly-bot --no-pager | head -15
echo ""

# 2. Check if bot is running
echo "2. PROCESS CHECK:"
echo "-----------------------------------------------------------"
if pgrep -f "python main.py" > /dev/null; then
    echo "✅ Bot process is running"
    echo "   PID: $(pgrep -f 'python main.py')"
else
    echo "❌ Bot process NOT running!"
fi
echo ""

# 3. Check recent logs for orders
echo "3. RECENT ORDERS (last 50 lines):"
echo "-----------------------------------------------------------"
sudo journalctl -u farmpoly-bot -n 50 | grep -i "order" | tail -10
if [ $? -ne 0 ]; then
    echo "⚠️  No orders found in recent logs"
fi
echo ""

# 4. Check for markets
echo "4. MARKETS FOUND (last 50 lines):"
echo "-----------------------------------------------------------"
sudo journalctl -u farmpoly-bot -n 50 | grep -i "selected.*market" | tail -5
if [ $? -ne 0 ]; then
    echo "⚠️  No market selection found in recent logs"
fi
echo ""

# 5. Check for errors
echo "5. RECENT ERRORS (last 100 lines):"
echo "-----------------------------------------------------------"
sudo journalctl -u farmpoly-bot -n 100 | grep -i "error\|failed\|warning" | tail -10
if [ $? -ne 0 ]; then
    echo "✅ No errors found"
fi
echo ""

# 6. Check USDC approval
echo "6. USDC APPROVAL STATUS:"
echo "-----------------------------------------------------------"
sudo journalctl -u farmpoly-bot -n 100 | grep -i "approval" | tail -5
if [ $? -ne 0 ]; then
    echo "⚠️  No approval info in recent logs"
fi
echo ""

# 7. Check wallet balance (if script exists)
echo "7. WALLET BALANCE:"
echo "-----------------------------------------------------------"
if [ -f "/home/farmpoly/farmpoly/scripts/check_wallets.py" ]; then
    cd /home/farmpoly/farmpoly
    source venv/bin/activate 2>/dev/null
    python scripts/check_wallets.py 2>/dev/null | grep -A 5 "Wallet 1:"
    if [ $? -ne 0 ]; then
        echo "⚠️  Could not check wallet balance"
    fi
else
    echo "⚠️  check_wallets.py not found"
fi
echo ""

# 8. Summary
echo "============================================================"
echo "SUMMARY & RECOMMENDATIONS:"
echo "============================================================"
echo ""

# Check if bot placed any orders
if sudo journalctl -u farmpoly-bot --since "1 hour ago" | grep -q "Order placed successfully"; then
    echo "✅ Bot HAS placed orders in the last hour - FARMING!"
else
    echo "⚠️  Bot has NOT placed orders in the last hour"
    echo ""
    echo "Possible reasons:"
    echo "  1. USDC.e not approved - Run: python scripts/approve_wallets.py"
    echo "  2. No USDC.e in wallet - Check balance and transfer funds"
    echo "  3. No markets with rewards available"
    echo "  4. Bot just started - Wait a few minutes"
fi
echo ""

# Check for withdrawal issue
if sudo journalctl -u farmpoly-bot --since "1 hour ago" | grep -q "Withdrawal successful"; then
    echo "⚠️  WARNING: Bot withdrew funds in the last hour!"
    echo "   Check URGENT_WITHDRAWAL_ISSUE.md for details"
fi
echo ""

echo "To view live logs: sudo journalctl -u farmpoly-bot -f"
echo "To check Polymarket: https://polymarket.com/ (connect wallet)"
echo "To check PolygonScan: https://polygonscan.com/address/0x18F261DC6d7Fc5ef2C96Ca4D56776220Ae4FfD96"
echo ""

