# 🛠️ Utility Scripts

Thư mục này chứa các script tiện ích để quản lý và vận hành Polymarket Bot.

## 📋 Danh Sách Scripts

### 1. check_wallets.py
Kiểm tra số dư MATIC và USDC của tất cả ví.

**Sử dụng:**
```bash
python scripts/check_wallets.py
```

**Output:**
- Địa chỉ mỗi ví
- Số dư MATIC
- Số dư USDC
- Cảnh báo nếu số dư thấp
- Tổng số dư tất cả ví

**Yêu cầu:**
- File `.env` đã cấu hình với `WALLET_PRIVATE_KEYS`
- Kết nối internet

### 2. generate_wallets.py
Tạo ví Ethereum mới cho bot.

**Sử dụng:**
```bash
python scripts/generate_wallets.py
```

**Tính năng:**
- Tạo số lượng ví tùy chọn
- Hiển thị address và private key
- Export format cho `.env`
- Tùy chọn lưu vào file

**Lưu ý bảo mật:**
- ⚠️ Private keys rất nhạy cảm
- Không share với ai
- Backup an toàn
- Xóa file sau khi backup

### 3. backup.sh (Sẽ tạo)
Backup dữ liệu bot.

**Sử dụng:**
```bash
./scripts/backup.sh
```

**Backup:**
- Logs
- Data
- Models
- Config files

## 🔧 Tạo Scripts Mới

### backup.sh

```bash
cat > scripts/backup.sh << 'EOF'
#!/bin/bash

# Polymarket Bot Backup Script

DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="backups/$DATE"

echo "Creating backup: $BACKUP_DIR"

# Create backup directory
mkdir -p $BACKUP_DIR

# Backup logs
if [ -d "logs" ]; then
    echo "Backing up logs..."
    cp -r logs $BACKUP_DIR/
fi

# Backup data
if [ -d "data" ]; then
    echo "Backing up data..."
    cp -r data $BACKUP_DIR/
fi

# Backup models
if [ -d "models" ]; then
    echo "Backing up models..."
    cp -r models $BACKUP_DIR/
fi

# Backup config
if [ -f "config.yaml" ]; then
    echo "Backing up config..."
    cp config.yaml $BACKUP_DIR/
fi

# Create archive
echo "Creating archive..."
tar -czf $BACKUP_DIR.tar.gz $BACKUP_DIR/

# Remove uncompressed backup
rm -rf $BACKUP_DIR

echo "Backup completed: $BACKUP_DIR.tar.gz"
echo "Size: $(du -h $BACKUP_DIR.tar.gz | cut -f1)"

# Keep only last 7 backups
echo "Cleaning old backups..."
ls -t backups/*.tar.gz | tail -n +8 | xargs -r rm

echo "Done!"
EOF

chmod +x scripts/backup.sh
```

### monitor.sh

```bash
cat > scripts/monitor.sh << 'EOF'
#!/bin/bash

# Polymarket Bot Monitor Script

echo "=== Polymarket Bot Monitor ==="
echo ""

# Check if bot is running
if pgrep -f "python main.py" > /dev/null; then
    echo "✅ Bot is running"
    PID=$(pgrep -f "python main.py")
    echo "   PID: $PID"
    
    # Show resource usage
    echo ""
    echo "Resource Usage:"
    ps aux | grep $PID | grep -v grep | awk '{print "   CPU: "$3"% | Memory: "$4"%"}'
else
    echo "❌ Bot is not running"
fi

echo ""

# Check log file
if [ -f "logs/polymarket_bot.log" ]; then
    echo "Recent Log Entries:"
    tail -5 logs/polymarket_bot.log | sed 's/^/   /'
    
    echo ""
    echo "Error Count (last 100 lines):"
    ERROR_COUNT=$(tail -100 logs/polymarket_bot.log | grep -c ERROR)
    echo "   $ERROR_COUNT errors"
else
    echo "⚠️  Log file not found"
fi

echo ""

# Check disk space
echo "Disk Space:"
df -h . | tail -1 | awk '{print "   Used: "$3" / "$2" ("$5")"}'

echo ""
echo "=== End Monitor ==="
EOF

chmod +x scripts/monitor.sh
```

### restart.sh

```bash
cat > scripts/restart.sh << 'EOF'
#!/bin/bash

# Polymarket Bot Restart Script

echo "Restarting Polymarket Bot..."

# Stop bot
echo "Stopping bot..."
pkill -TERM -f "python main.py"

# Wait for graceful shutdown
sleep 5

# Force kill if still running
if pgrep -f "python main.py" > /dev/null; then
    echo "Force stopping..."
    pkill -9 -f "python main.py"
fi

# Wait a bit
sleep 2

# Start bot
echo "Starting bot..."
source venv/bin/activate
nohup python main.py > logs/nohup.log 2>&1 &

# Check if started
sleep 3
if pgrep -f "python main.py" > /dev/null; then
    echo "✅ Bot restarted successfully"
    PID=$(pgrep -f "python main.py")
    echo "   PID: $PID"
else
    echo "❌ Failed to restart bot"
    exit 1
fi
EOF

chmod +x scripts/restart.sh
```

### analyze_performance.py

```bash
cat > scripts/analyze_performance.py << 'EOF'
#!/usr/bin/env python3
"""
Analyze bot performance from logs
"""

import re
from datetime import datetime
from collections import defaultdict

def parse_log_file(filename='logs/polymarket_bot.log'):
    """Parse log file and extract metrics"""
    
    metrics = {
        'fills': [],
        'cancels': [],
        'errors': [],
        'pnl': []
    }
    
    try:
        with open(filename, 'r') as f:
            for line in f:
                # Extract fills
                if 'filled' in line.lower():
                    metrics['fills'].append(line)
                
                # Extract cancels
                if 'cancel' in line.lower():
                    metrics['cancels'].append(line)
                
                # Extract errors
                if 'ERROR' in line:
                    metrics['errors'].append(line)
                
                # Extract P&L
                if 'P&L' in line or 'profit' in line.lower():
                    metrics['pnl'].append(line)
    
    except FileNotFoundError:
        print(f"❌ Log file not found: {filename}")
        return None
    
    return metrics

def main():
    """Main function"""
    print("=" * 60)
    print("Polymarket Bot - Performance Analysis")
    print("=" * 60)
    print()
    
    metrics = parse_log_file()
    
    if not metrics:
        return
    
    print(f"Total Fills:    {len(metrics['fills'])}")
    print(f"Total Cancels:  {len(metrics['cancels'])}")
    print(f"Total Errors:   {len(metrics['errors'])}")
    print()
    
    if metrics['fills']:
        print("Recent Fills:")
        for fill in metrics['fills'][-5:]:
            print(f"  {fill.strip()}")
    
    print()
    
    if metrics['errors']:
        print("Recent Errors:")
        for error in metrics['errors'][-5:]:
            print(f"  {error.strip()}")
    
    print()
    print("=" * 60)

if __name__ == "__main__":
    main()
EOF

chmod +x scripts/analyze_performance.py
```

## 📝 Sử Dụng Scripts

### Kiểm tra ví hàng ngày
```bash
# Chạy mỗi sáng
python scripts/check_wallets.py
```

### Backup định kỳ
```bash
# Thêm vào crontab
crontab -e

# Backup mỗi ngày lúc 00:00
0 0 * * * /path/to/polymarket-bot/scripts/backup.sh
```

### Monitor bot
```bash
# Kiểm tra status
./scripts/monitor.sh

# Hoặc watch mode
watch -n 10 ./scripts/monitor.sh
```

### Restart bot
```bash
# Restart khi cần
./scripts/restart.sh
```

### Phân tích performance
```bash
# Xem metrics
python scripts/analyze_performance.py
```

## 🔐 Bảo Mật

**Lưu ý quan trọng:**
- Scripts có thể chứa hoặc truy cập sensitive data
- Không share scripts đã chạy (có thể chứa logs)
- Kiểm tra permissions: `chmod 700 scripts/*.sh`
- Không commit output files

## 📞 Hỗ Trợ

Nếu gặp vấn đề với scripts:
1. Kiểm tra permissions: `ls -la scripts/`
2. Kiểm tra dependencies
3. Xem logs
4. Mở issue trên GitHub

---

**Tip**: Tạo alias cho các scripts thường dùng:

```bash
# Thêm vào ~/.bashrc hoặc ~/.zshrc
alias bot-check='python scripts/check_wallets.py'
alias bot-monitor='./scripts/monitor.sh'
alias bot-restart='./scripts/restart.sh'
alias bot-backup='./scripts/backup.sh'
```

