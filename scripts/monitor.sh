#!/bin/bash
# Farmpoly Bot - Monitoring Script
# Real-time monitoring dashboard for the bot

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
MAGENTA='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Project directory
PROJECT_DIR="$HOME/projects/farmpoly"
LOG_FILE="$PROJECT_DIR/logs/polymarket_bot.log"

# Function to print header
print_header() {
    clear
    echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${CYAN}           🤖 FARMPOLY BOT MONITORING DASHBOARD${NC}"
    echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${YELLOW}Last updated: $(date '+%Y-%m-%d %H:%M:%S')${NC}"
    echo ""
}

# Function to check bot status
check_bot_status() {
    echo -e "${BLUE}📊 Bot Status:${NC}"
    if systemctl is-active --quiet farmpoly-bot; then
        echo -e "   Status: ${GREEN}● RUNNING${NC}"
        UPTIME=$(systemctl show farmpoly-bot --property=ActiveEnterTimestamp --value)
        echo -e "   Uptime: $UPTIME"
    else
        echo -e "   Status: ${RED}● STOPPED${NC}"
    fi
    echo ""
}

# Function to show system resources
show_system_resources() {
    echo -e "${BLUE}💻 System Resources:${NC}"
    
    # CPU usage
    CPU_USAGE=$(top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{print 100 - $1}')
    echo -e "   CPU Usage: ${YELLOW}${CPU_USAGE}%${NC}"
    
    # Memory usage
    MEM_INFO=$(free -h | grep Mem)
    MEM_USED=$(echo $MEM_INFO | awk '{print $3}')
    MEM_TOTAL=$(echo $MEM_INFO | awk '{print $2}')
    echo -e "   Memory: ${YELLOW}${MEM_USED}${NC} / ${MEM_TOTAL}"
    
    # Disk usage
    DISK_USAGE=$(df -h $PROJECT_DIR | tail -1 | awk '{print $5}')
    echo -e "   Disk Usage: ${YELLOW}${DISK_USAGE}${NC}"
    
    echo ""
}

# Function to show recent logs
show_recent_logs() {
    echo -e "${BLUE}📝 Recent Logs (last 10 lines):${NC}"
    if [ -f "$LOG_FILE" ]; then
        tail -n 10 "$LOG_FILE" | while read line; do
            if [[ $line == *"ERROR"* ]]; then
                echo -e "${RED}$line${NC}"
            elif [[ $line == *"WARNING"* ]]; then
                echo -e "${YELLOW}$line${NC}"
            elif [[ $line == *"SUCCESS"* ]] || [[ $line == *"✅"* ]]; then
                echo -e "${GREEN}$line${NC}"
            else
                echo "$line"
            fi
        done
    else
        echo -e "${RED}   Log file not found${NC}"
    fi
    echo ""
}

# Function to show error count
show_error_count() {
    echo -e "${BLUE}⚠️  Error Summary (last 1 hour):${NC}"
    if [ -f "$LOG_FILE" ]; then
        ERROR_COUNT=$(grep -c "ERROR" "$LOG_FILE" 2>/dev/null || echo "0")
        WARNING_COUNT=$(grep -c "WARNING" "$LOG_FILE" 2>/dev/null || echo "0")
        
        if [ "$ERROR_COUNT" -gt 0 ]; then
            echo -e "   Errors: ${RED}${ERROR_COUNT}${NC}"
        else
            echo -e "   Errors: ${GREEN}0${NC}"
        fi
        
        if [ "$WARNING_COUNT" -gt 0 ]; then
            echo -e "   Warnings: ${YELLOW}${WARNING_COUNT}${NC}"
        else
            echo -e "   Warnings: ${GREEN}0${NC}"
        fi
    fi
    echo ""
}

# Function to show trading stats
show_trading_stats() {
    echo -e "${BLUE}💰 Trading Stats (from logs):${NC}"
    if [ -f "$LOG_FILE" ]; then
        # Count orders placed
        ORDERS_PLACED=$(grep -c "Order placed" "$LOG_FILE" 2>/dev/null || echo "0")
        echo -e "   Orders Placed: ${GREEN}${ORDERS_PLACED}${NC}"
        
        # Count fills
        FILLS=$(grep -c "filled" "$LOG_FILE" 2>/dev/null || echo "0")
        echo -e "   Fills: ${GREEN}${FILLS}${NC}"
        
        # Count cancellations
        CANCELS=$(grep -c "cancelled" "$LOG_FILE" 2>/dev/null || echo "0")
        echo -e "   Cancellations: ${YELLOW}${CANCELS}${NC}"
    fi
    echo ""
}

# Function to show quick actions
show_quick_actions() {
    echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${BLUE}⚡ Quick Actions:${NC}"
    echo ""
    echo "  [r] Restart bot"
    echo "  [s] Stop bot"
    echo "  [l] View full logs"
    echo "  [w] Check wallets"
    echo "  [t] Run tests"
    echo "  [q] Quit"
    echo ""
    echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
}

# Main monitoring loop
monitor_loop() {
    while true; do
        print_header
        check_bot_status
        show_system_resources
        show_error_count
        show_trading_stats
        show_recent_logs
        show_quick_actions
        
        # Wait for user input with timeout
        read -t 5 -n 1 action
        
        case $action in
            r|R)
                echo ""
                echo -e "${YELLOW}Restarting bot...${NC}"
                sudo systemctl restart farmpoly-bot
                sleep 2
                ;;
            s|S)
                echo ""
                echo -e "${YELLOW}Stopping bot...${NC}"
                sudo systemctl stop farmpoly-bot
                sleep 2
                ;;
            l|L)
                echo ""
                echo -e "${YELLOW}Opening full logs...${NC}"
                less +F "$LOG_FILE"
                ;;
            w|W)
                echo ""
                cd "$PROJECT_DIR"
                source venv/bin/activate
                python scripts/check_wallets.py
                deactivate
                read -p "Press Enter to continue..."
                ;;
            t|T)
                echo ""
                cd "$PROJECT_DIR"
                source venv/bin/activate
                python tests/run_tests.py
                deactivate
                read -p "Press Enter to continue..."
                ;;
            q|Q)
                echo ""
                echo -e "${GREEN}Exiting monitor...${NC}"
                exit 0
                ;;
        esac
    done
}

# Check if project directory exists
if [ ! -d "$PROJECT_DIR" ]; then
    echo -e "${RED}Error: Project directory not found at $PROJECT_DIR${NC}"
    exit 1
fi

# Start monitoring
monitor_loop

