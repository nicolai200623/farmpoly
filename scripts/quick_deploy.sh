#!/bin/bash
# Farmpoly Bot - Quick Deploy Script
# One-command deployment for VPS

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}"
cat << "EOF"
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║        🚀 FARMPOLY BOT - QUICK DEPLOY SCRIPT 🚀          ║
║                                                           ║
║              Automated VPS Deployment                     ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
EOF
echo -e "${NC}"

# Configuration
PROJECT_DIR="$HOME/projects/farmpoly"
SERVICE_NAME="farmpoly-bot"
SERVICE_FILE="/etc/systemd/system/${SERVICE_NAME}.service"

# Functions
print_step() {
    echo -e "\n${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${YELLOW}▶ $1${NC}"
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}\n"
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

# Check if running as correct user
if [ "$EUID" -eq 0 ]; then 
    print_error "Please do not run as root"
    exit 1
fi

# Step 1: Check prerequisites
print_step "Step 1/7: Checking prerequisites"

if ! command -v python3 &> /dev/null; then
    print_error "Python3 not found. Please run vps_setup.sh first"
    exit 1
fi
print_success "Python3 found: $(python3 --version)"

if ! command -v git &> /dev/null; then
    print_error "Git not found. Please run vps_setup.sh first"
    exit 1
fi
print_success "Git found"

# Step 2: Navigate to project
print_step "Step 2/7: Navigating to project directory"

if [ ! -d "$PROJECT_DIR" ]; then
    print_error "Project directory not found at $PROJECT_DIR"
    print_warning "Please clone the repository first:"
    echo "  cd ~/projects"
    echo "  git clone https://github.com/nicolai200623/farmpoly.git"
    exit 1
fi

cd "$PROJECT_DIR"
print_success "Project directory: $PROJECT_DIR"

# Step 3: Setup virtual environment
print_step "Step 3/7: Setting up virtual environment"

if [ ! -d "venv" ]; then
    print_warning "Virtual environment not found. Creating..."
    python3 -m venv venv
fi

source venv/bin/activate
print_success "Virtual environment activated"

# Upgrade pip
pip install --upgrade pip -q
print_success "Pip upgraded"

# Step 4: Install dependencies
print_step "Step 4/7: Installing dependencies"

if [ -f "requirements.txt" ]; then
    print_warning "This may take 5-10 minutes..."
    pip install -r requirements.txt -q
    print_success "Python packages installed"
else
    print_error "requirements.txt not found"
    exit 1
fi

# Install Playwright browsers
if command -v playwright &> /dev/null; then
    playwright install chromium
    print_success "Playwright browsers installed"
fi

# Step 5: Check configuration
print_step "Step 5/7: Checking configuration"

if [ ! -f ".env" ]; then
    print_warning ".env file not found"
    if [ -f ".env.example" ]; then
        cp .env.example .env
        print_success "Created .env from .env.example"
        print_warning "⚠️  IMPORTANT: Edit .env and add your private keys!"
        echo ""
        echo "Run: nano .env"
        echo ""
        read -p "Press Enter after you've configured .env..."
    else
        print_error ".env.example not found"
        exit 1
    fi
fi

# Secure .env
chmod 600 .env
print_success ".env secured (permissions: 600)"

if [ ! -f "config.yaml" ]; then
    print_error "config.yaml not found"
    exit 1
fi
print_success "config.yaml found"

# Create necessary directories
mkdir -p logs data models backups
print_success "Directories created"

# Step 6: Run tests
print_step "Step 6/7: Running tests"

if [ -f "tests/run_tests.py" ]; then
    print_warning "Running unit tests..."
    if python tests/run_tests.py; then
        print_success "All tests passed!"
    else
        print_error "Some tests failed"
        read -p "Continue anyway? (y/n) " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            exit 1
        fi
    fi
else
    print_warning "Test file not found, skipping tests"
fi

deactivate

# Step 7: Setup systemd service
print_step "Step 7/7: Setting up systemd service"

# Create service file content
SERVICE_CONTENT="[Unit]
Description=Farmpoly Polymarket Trading Bot
After=network.target

[Service]
Type=simple
User=$USER
WorkingDirectory=$PROJECT_DIR
Environment=\"PATH=$PROJECT_DIR/venv/bin\"
ExecStart=$PROJECT_DIR/venv/bin/python main.py
Restart=always
RestartSec=10
StandardOutput=append:$PROJECT_DIR/logs/systemd.log
StandardError=append:$PROJECT_DIR/logs/systemd-error.log

# Security settings
NoNewPrivileges=true
PrivateTmp=true

[Install]
WantedBy=multi-user.target"

# Check if service already exists
if [ -f "$SERVICE_FILE" ]; then
    print_warning "Service file already exists"
    read -p "Overwrite? (y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        print_warning "Skipping service creation"
    else
        echo "$SERVICE_CONTENT" | sudo tee "$SERVICE_FILE" > /dev/null
        print_success "Service file updated"
    fi
else
    echo "$SERVICE_CONTENT" | sudo tee "$SERVICE_FILE" > /dev/null
    print_success "Service file created"
fi

# Reload systemd
sudo systemctl daemon-reload
print_success "Systemd reloaded"

# Enable service
sudo systemctl enable "$SERVICE_NAME"
print_success "Service enabled (auto-start on boot)"

# Ask to start service
echo ""
read -p "Start the bot now? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    sudo systemctl start "$SERVICE_NAME"
    sleep 2
    
    if systemctl is-active --quiet "$SERVICE_NAME"; then
        print_success "Bot started successfully!"
    else
        print_error "Failed to start bot"
        echo ""
        echo "Check logs with:"
        echo "  sudo journalctl -u $SERVICE_NAME -n 50"
        exit 1
    fi
fi

# Final summary
echo ""
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}           ✅ DEPLOYMENT COMPLETED SUCCESSFULLY!${NC}"
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
echo -e "${BLUE}📋 Useful Commands:${NC}"
echo ""
echo "  Check status:"
echo "    sudo systemctl status $SERVICE_NAME"
echo ""
echo "  View logs:"
echo "    tail -f $PROJECT_DIR/logs/polymarket_bot.log"
echo "    sudo journalctl -u $SERVICE_NAME -f"
echo ""
echo "  Control bot:"
echo "    sudo systemctl start $SERVICE_NAME"
echo "    sudo systemctl stop $SERVICE_NAME"
echo "    sudo systemctl restart $SERVICE_NAME"
echo ""
echo "  Monitor bot:"
echo "    bash $PROJECT_DIR/scripts/monitor.sh"
echo ""
echo "  Check wallets:"
echo "    cd $PROJECT_DIR && source venv/bin/activate"
echo "    python scripts/check_wallets.py"
echo ""
echo -e "${YELLOW}⚠️  IMPORTANT REMINDERS:${NC}"
echo ""
echo "  1. Make sure .env has your private keys"
echo "  2. Fund your wallets with USDC + MATIC"
echo "  3. Approve USDC: python scripts/approve_wallets.py"
echo "  4. Monitor logs for the first hour"
echo "  5. Start with small capital (\$50-100)"
echo ""
echo -e "${GREEN}Good luck! 🚀${NC}"
echo ""

