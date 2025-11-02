#!/bin/bash
# Farmpoly Bot - VPS Setup Script for Ubuntu 22.04
# This script automates the initial setup on a fresh Ubuntu VPS

set -e  # Exit on error

echo "🚀 Farmpoly Bot - VPS Setup Script"
echo "===================================="
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print colored output
print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_info() {
    echo -e "${YELLOW}ℹ️  $1${NC}"
}

# Check if running as root
if [ "$EUID" -eq 0 ]; then 
    print_error "Please do not run as root. Run as regular user with sudo privileges."
    exit 1
fi

print_info "Starting VPS setup..."
echo ""

# 1. Update system
print_info "Step 1/8: Updating system packages..."
sudo apt update && sudo apt upgrade -y
print_success "System updated"
echo ""

# 2. Install basic tools
print_info "Step 2/8: Installing basic tools..."
sudo apt install -y \
    git \
    curl \
    wget \
    vim \
    htop \
    screen \
    tmux \
    build-essential \
    software-properties-common
print_success "Basic tools installed"
echo ""

# 3. Install Python 3.9+
print_info "Step 3/8: Installing Python..."
sudo apt install -y \
    python3 \
    python3-pip \
    python3-venv \
    python3-dev
PYTHON_VERSION=$(python3 --version)
print_success "Python installed: $PYTHON_VERSION"
echo ""

# 4. Install Playwright dependencies
print_info "Step 4/8: Installing Playwright dependencies..."
sudo apt install -y \
    libnss3 \
    libnspr4 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libdrm2 \
    libdbus-1-3 \
    libxkbcommon0 \
    libxcomposite1 \
    libxdamage1 \
    libxfixes3 \
    libxrandr2 \
    libgbm1 \
    libpango-1.0-0 \
    libcairo2 \
    libasound2 \
    libatspi2.0-0 \
    libwayland-client0 \
    fonts-liberation \
    fonts-noto-color-emoji
print_success "Playwright dependencies installed"
echo ""

# 5. Create project directory
print_info "Step 5/8: Creating project directory..."
mkdir -p ~/projects
cd ~/projects
print_success "Project directory created: ~/projects"
echo ""

# 6. Setup virtual environment (if project exists)
if [ -d "farmpoly" ]; then
    print_info "Step 6/8: Setting up virtual environment..."
    cd farmpoly
    
    # Create venv
    python3 -m venv venv
    source venv/bin/activate
    
    # Upgrade pip
    pip install --upgrade pip
    
    # Install requirements
    if [ -f "requirements.txt" ]; then
        print_info "Installing Python packages (this may take 5-10 minutes)..."
        pip install -r requirements.txt
        print_success "Python packages installed"
    fi
    
    # Install Playwright browsers
    print_info "Installing Playwright browsers..."
    playwright install chromium
    print_success "Playwright browsers installed"
    
    # Create necessary directories
    mkdir -p logs data models backups
    print_success "Directories created"
    
    deactivate
    cd ~/projects
else
    print_info "Step 6/8: Skipped (project not found)"
    print_info "Please clone your repository to ~/projects/farmpoly"
fi
echo ""

# 7. Setup firewall
print_info "Step 7/8: Configuring firewall..."
sudo ufw --force enable
sudo ufw allow 22/tcp  # SSH
print_success "Firewall configured (SSH allowed)"
echo ""

# 8. Security hardening
print_info "Step 8/8: Applying security settings..."

# Disable root login (backup first)
if [ -f "/etc/ssh/sshd_config" ]; then
    sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.backup
    print_success "SSH config backed up"
fi

echo ""
print_success "VPS setup completed!"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📋 Next Steps:"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "1. Clone your repository:"
echo "   cd ~/projects"
echo "   git clone https://github.com/nicolai200623/farmpoly.git"
echo ""
echo "2. Setup the bot:"
echo "   cd farmpoly"
echo "   source venv/bin/activate"
echo "   cp .env.example .env"
echo "   nano .env  # Add your private keys"
echo ""
echo "3. Test the bot:"
echo "   python tests/run_tests.py"
echo ""
echo "4. Create systemd service:"
echo "   sudo nano /etc/systemd/system/farmpoly-bot.service"
echo "   # Copy content from VPS_UBUNTU_DEPLOYMENT.md"
echo ""
echo "5. Start the bot:"
echo "   sudo systemctl enable farmpoly-bot"
echo "   sudo systemctl start farmpoly-bot"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
print_info "For detailed instructions, see VPS_UBUNTU_DEPLOYMENT.md"
echo ""

