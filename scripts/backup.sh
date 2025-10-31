#!/bin/bash

# Polymarket Bot Backup Script

DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="backups/$DATE"

echo "========================================="
echo "Polymarket Bot - Backup Script"
echo "========================================="
echo ""
echo "Creating backup: $BACKUP_DIR"
echo ""

# Create backup directory
mkdir -p $BACKUP_DIR

# Backup logs
if [ -d "logs" ]; then
    echo "✅ Backing up logs..."
    cp -r logs $BACKUP_DIR/
else
    echo "⚠️  No logs directory found"
fi

# Backup data
if [ -d "data" ]; then
    echo "✅ Backing up data..."
    cp -r data $BACKUP_DIR/
else
    echo "⚠️  No data directory found"
fi

# Backup models
if [ -d "models" ]; then
    echo "✅ Backing up models..."
    cp -r models $BACKUP_DIR/
else
    echo "⚠️  No models directory found"
fi

# Backup config
if [ -f "config.yaml" ]; then
    echo "✅ Backing up config..."
    cp config.yaml $BACKUP_DIR/
else
    echo "⚠️  No config.yaml found"
fi

# Backup .env.example (not .env for security)
if [ -f ".env.example" ]; then
    cp .env.example $BACKUP_DIR/
fi

echo ""
echo "Creating archive..."

# Create archive
tar -czf $BACKUP_DIR.tar.gz $BACKUP_DIR/

# Remove uncompressed backup
rm -rf $BACKUP_DIR

echo ""
echo "✅ Backup completed: $BACKUP_DIR.tar.gz"
echo "   Size: $(du -h $BACKUP_DIR.tar.gz | cut -f1)"

echo ""
echo "Cleaning old backups (keeping last 7)..."

# Keep only last 7 backups
cd backups
ls -t *.tar.gz 2>/dev/null | tail -n +8 | xargs -r rm
cd ..

BACKUP_COUNT=$(ls -1 backups/*.tar.gz 2>/dev/null | wc -l)
echo "   Current backups: $BACKUP_COUNT"

echo ""
echo "========================================="
echo "Backup Complete!"
echo "========================================="

