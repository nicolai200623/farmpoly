#!/bin/bash
# Script để cài đặt dependencies trên VPS
# Chạy script này trên VPS sau khi upload code

echo "================================================================================"
echo "🔧 VPS DEPENDENCY INSTALLATION SCRIPT"
echo "================================================================================"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if running on Linux
if [[ "$OSTYPE" != "linux-gnu"* ]]; then
    echo -e "${YELLOW}⚠️  Warning: This script is designed for Linux VPS${NC}"
fi

# Get script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

echo -e "\n📁 Project directory: ${GREEN}$PROJECT_DIR${NC}"

# Change to project directory
cd "$PROJECT_DIR" || exit 1

# Check Python version
echo -e "\n🐍 Checking Python version..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version)
    echo -e "${GREEN}✅ $PYTHON_VERSION${NC}"
else
    echo -e "${RED}❌ Python3 not found!${NC}"
    exit 1
fi

# Check pip
echo -e "\n📦 Checking pip..."
if command -v pip3 &> /dev/null; then
    PIP_VERSION=$(pip3 --version)
    echo -e "${GREEN}✅ $PIP_VERSION${NC}"
else
    echo -e "${RED}❌ pip3 not found!${NC}"
    echo -e "${YELLOW}Installing pip...${NC}"
    sudo apt-get update
    sudo apt-get install -y python3-pip
fi

# Upgrade pip
echo -e "\n⬆️  Upgrading pip..."
pip3 install --upgrade pip --user

# Check if requirements.txt exists
if [ ! -f "requirements.txt" ]; then
    echo -e "${RED}❌ requirements.txt not found!${NC}"
    exit 1
fi

echo -e "\n📋 Found requirements.txt"

# Install psutil first (critical for monitoring)
echo -e "\n🔧 Installing psutil (critical dependency)..."
pip3 install psutil --user
if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ psutil installed successfully${NC}"
else
    echo -e "${RED}❌ Failed to install psutil${NC}"
    exit 1
fi

# Verify psutil
echo -e "\n🔍 Verifying psutil installation..."
python3 -c "import psutil; print(f'✅ psutil version: {psutil.__version__}')"
if [ $? -ne 0 ]; then
    echo -e "${RED}❌ psutil verification failed${NC}"
    exit 1
fi

# Install all dependencies from requirements.txt
echo -e "\n📦 Installing all dependencies from requirements.txt..."
echo -e "${YELLOW}This may take several minutes...${NC}"

pip3 install -r requirements.txt --user

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ All dependencies installed${NC}"
else
    echo -e "${YELLOW}⚠️  Some dependencies may have failed${NC}"
    echo -e "${YELLOW}Continuing with verification...${NC}"
fi

# Run dependency check script
echo -e "\n🔍 Running dependency verification..."
if [ -f "scripts/check_dependencies.py" ]; then
    python3 scripts/check_dependencies.py
    CHECK_RESULT=$?
else
    echo -e "${YELLOW}⚠️  check_dependencies.py not found, skipping verification${NC}"
    CHECK_RESULT=0
fi

# Install Playwright browsers (if needed)
echo -e "\n🌐 Installing Playwright browsers..."
python3 -m playwright install chromium
if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ Playwright browsers installed${NC}"
else
    echo -e "${YELLOW}⚠️  Playwright browser installation failed (may need system dependencies)${NC}"
    echo -e "${YELLOW}Run: sudo apt-get install -y libnss3 libatk-bridge2.0-0 libdrm2 libxkbcommon0 libgbm1${NC}"
fi

# Summary
echo -e "\n================================================================================"
echo -e "📊 INSTALLATION SUMMARY"
echo -e "================================================================================"

# Check critical modules
echo -e "\n🔍 Checking critical modules:"

CRITICAL_MODULES=("psutil" "aiohttp" "yaml" "torch" "web3")
ALL_OK=true

for module in "${CRITICAL_MODULES[@]}"; do
    if python3 -c "import $module" 2>/dev/null; then
        echo -e "   ${GREEN}✅${NC} $module"
    else
        echo -e "   ${RED}❌${NC} $module"
        ALL_OK=false
    fi
done

echo -e "\n================================================================================"

if [ "$ALL_OK" = true ] && [ $CHECK_RESULT -eq 0 ]; then
    echo -e "${GREEN}🎉 ALL DEPENDENCIES INSTALLED SUCCESSFULLY!${NC}"
    echo -e "\n✅ Next steps:"
    echo -e "   1. Check configuration: ${YELLOW}cat config.yaml${NC}"
    echo -e "   2. Check .env file: ${YELLOW}cat .env${NC}"
    echo -e "   3. Run bot: ${YELLOW}python3 main.py${NC}"
    echo -e "   4. Monitor logs: ${YELLOW}tail -f log.md${NC}"
    exit 0
else
    echo -e "${YELLOW}⚠️  SOME DEPENDENCIES MAY BE MISSING${NC}"
    echo -e "\n📝 Troubleshooting:"
    echo -e "   1. Check Python version: ${YELLOW}python3 --version${NC}"
    echo -e "   2. Check pip: ${YELLOW}pip3 --version${NC}"
    echo -e "   3. Try manual install: ${YELLOW}pip3 install <module-name> --user${NC}"
    echo -e "   4. Check system dependencies: ${YELLOW}sudo apt-get install python3-dev${NC}"
    exit 1
fi

