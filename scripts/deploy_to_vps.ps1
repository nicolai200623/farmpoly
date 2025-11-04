# Deploy bot code to VPS (PowerShell version for Windows)
# Usage: .\scripts\deploy_to_vps.ps1 "Your commit message"

param(
    [string]$CommitMessage = "Update bot code"
)

Write-Host "========================================================================" -ForegroundColor Cyan
Write-Host "🚀 DEPLOY POLYMARKET BOT TO VPS" -ForegroundColor Cyan
Write-Host "========================================================================" -ForegroundColor Cyan
Write-Host ""

# Step 1: Check for changes
Write-Host "📋 Step 1: Checking for changes..." -ForegroundColor Yellow
$changes = git status -s
if ($changes.Length -eq 0) {
    Write-Host "⚠️  No changes to commit" -ForegroundColor Yellow
    Write-Host ""
    $continue = Read-Host "Continue with deployment anyway? (y/n)"
    if ($continue -ne "y") {
        Write-Host "Deployment cancelled." -ForegroundColor Red
        exit
    }
} else {
    Write-Host "✅ Changes detected" -ForegroundColor Green
    git status -s
    Write-Host ""
}

# Step 2: Commit changes
if ($changes.Length -gt 0) {
    Write-Host "📝 Step 2: Committing changes..." -ForegroundColor Yellow
    
    git add -A
    git commit -m $CommitMessage
    Write-Host "✅ Changes committed" -ForegroundColor Green
    Write-Host ""
} else {
    Write-Host "📝 Step 2: No changes to commit" -ForegroundColor Yellow
    Write-Host ""
}

# Step 3: Push to GitHub
Write-Host "📤 Step 3: Pushing to GitHub..." -ForegroundColor Yellow
try {
    git push origin master
    Write-Host "✅ Pushed to GitHub" -ForegroundColor Green
    Write-Host ""
} catch {
    Write-Host "❌ Failed to push to GitHub: $_" -ForegroundColor Red
    Write-Host ""
    Write-Host "Troubleshooting:" -ForegroundColor Yellow
    Write-Host "  1. Check your GitHub credentials" -ForegroundColor Yellow
    Write-Host "  2. Make sure you have push access to the repository" -ForegroundColor Yellow
    Write-Host "  3. Try: git push origin master --verbose" -ForegroundColor Yellow
    exit 1
}

# Step 4: Instructions for VPS deployment
Write-Host "🌐 Step 4: Deploy to VPS" -ForegroundColor Yellow
Write-Host ""
Write-Host "⚠️  MANUAL STEP REQUIRED:" -ForegroundColor Yellow
Write-Host ""
Write-Host "SSH into your VPS and run the following commands:" -ForegroundColor Cyan
Write-Host ""
Write-Host "ssh root@your-vps-ip" -ForegroundColor White
Write-Host ""
Write-Host "Then run:" -ForegroundColor Cyan
Write-Host ""
Write-Host @"
cd ~/projects/farmpoly
sudo systemctl stop farmpoly-bot
git pull origin master
sudo systemctl restart farmpoly-bot
tail -f logs/polymarket_bot.log
"@ -ForegroundColor White
Write-Host ""
Write-Host "========================================================================"
Write-Host "✅ LOCAL DEPLOYMENT COMPLETE!" -ForegroundColor Green
Write-Host "========================================================================"
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host "  1. SSH into VPS and pull the latest code" -ForegroundColor Yellow
Write-Host "  2. Restart the bot" -ForegroundColor Yellow
Write-Host "  3. Monitor logs to verify fixes" -ForegroundColor Yellow
Write-Host ""
Write-Host "Or use the automated SSH script (if configured):" -ForegroundColor Cyan
Write-Host "  .\scripts\ssh_deploy.ps1" -ForegroundColor White
Write-Host ""

