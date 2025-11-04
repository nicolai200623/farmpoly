#!/bin/bash
# Deploy bot code to VPS
# Usage: ./scripts/deploy_to_vps.sh [commit_message]

set -e  # Exit on error

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo "========================================================================"
echo "🚀 DEPLOY POLYMARKET BOT TO VPS"
echo "========================================================================"
echo ""

# Step 1: Check if there are changes
echo "📋 Step 1: Checking for changes..."
if [[ -z $(git status -s) ]]; then
    echo -e "${YELLOW}⚠️  No changes to commit${NC}"
    echo ""
    read -p "Continue with deployment anyway? (y/n): " continue_deploy
    if [[ "$continue_deploy" != "y" ]]; then
        echo "Deployment cancelled."
        exit 0
    fi
else
    echo -e "${GREEN}✅ Changes detected${NC}"
    git status -s
    echo ""
fi

# Step 2: Commit changes (if any)
if [[ -n $(git status -s) ]]; then
    echo "📝 Step 2: Committing changes..."
    
    # Get commit message from argument or prompt
    if [[ -n "$1" ]]; then
        COMMIT_MSG="$1"
    else
        read -p "Enter commit message: " COMMIT_MSG
        if [[ -z "$COMMIT_MSG" ]]; then
            COMMIT_MSG="Update bot code"
        fi
    fi
    
    git add -A
    git commit -m "$COMMIT_MSG"
    echo -e "${GREEN}✅ Changes committed${NC}"
    echo ""
else
    echo "📝 Step 2: No changes to commit"
    echo ""
fi

# Step 3: Push to GitHub
echo "📤 Step 3: Pushing to GitHub..."
git push origin master
echo -e "${GREEN}✅ Pushed to GitHub${NC}"
echo ""

# Step 4: Deploy to VPS
echo "🌐 Step 4: Deploying to VPS..."
echo ""

# VPS connection details (CHANGE THESE!)
VPS_USER="root"
VPS_HOST="your-vps-ip"  # ← CHANGE THIS!
VPS_PATH="~/projects/farmpoly"

echo "VPS: $VPS_USER@$VPS_HOST"
echo "Path: $VPS_PATH"
echo ""

# SSH command to deploy
ssh $VPS_USER@$VPS_HOST << 'ENDSSH'
    echo "========================================================================"
    echo "🔧 VPS DEPLOYMENT"
    echo "========================================================================"
    echo ""
    
    # Navigate to project
    cd ~/projects/farmpoly
    
    # Stop bot
    echo "⏸️  Stopping bot..."
    sudo systemctl stop farmpoly-bot
    echo "✅ Bot stopped"
    echo ""
    
    # Pull latest code
    echo "📥 Pulling latest code..."
    git pull origin master
    echo "✅ Code updated"
    echo ""
    
    # Verify key files
    echo "🔍 Verifying fixes..."
    
    # Check Fix #11 (min_reward)
    if grep -q "scanner_config = config.get('market_scanner', {})" market_scanner_v2.py; then
        echo "✅ Fix #11 (min_reward) verified"
    else
        echo "❌ Fix #11 (min_reward) NOT found!"
    fi
    
    # Check Fix #10 (max_concurrent_markets)
    if grep -q "market_selection_config = self.config.get('market_selection', {})" market_selector.py; then
        echo "✅ Fix #10 (max_concurrent_markets) verified"
    else
        echo "❌ Fix #10 (max_concurrent_markets) NOT found!"
    fi
    
    # Check Fix #12 (max_position_age)
    if grep -q "max_age = self.config.get('max_position_age'" position_monitor.py; then
        echo "✅ Fix #12 (max_position_age) verified"
    else
        echo "❌ Fix #12 (max_position_age) NOT found!"
    fi
    
    echo ""
    
    # Restart bot
    echo "🔄 Restarting bot..."
    sudo systemctl restart farmpoly-bot
    echo "✅ Bot restarted"
    echo ""
    
    # Check status
    echo "📊 Bot status:"
    sudo systemctl status farmpoly-bot --no-pager | head -n 10
    echo ""
    
    # Show recent logs
    echo "📋 Recent logs (last 20 lines):"
    tail -n 20 logs/polymarket_bot.log
    echo ""
    
    echo "========================================================================"
    echo "✅ DEPLOYMENT COMPLETE!"
    echo "========================================================================"
    echo ""
    echo "Monitor logs with:"
    echo "  tail -f ~/projects/farmpoly/logs/polymarket_bot.log"
    echo ""
ENDSSH

echo ""
echo "========================================================================"
echo "✅ DEPLOYMENT SUCCESSFUL!"
echo "========================================================================"
echo ""
echo "Next steps:"
echo "  1. Monitor logs: ssh $VPS_USER@$VPS_HOST 'tail -f $VPS_PATH/logs/polymarket_bot.log'"
echo "  2. Check for 'reward < \$100' instead of 'reward < \$300'"
echo "  3. Verify bot selects 1 market instead of 3"
echo ""

