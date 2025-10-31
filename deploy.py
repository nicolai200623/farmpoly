#!/usr/bin/env python3
"""
Deployment Script for Polymarket Trading Bot
Handles production deployment with monitoring and auto-restart
"""

import os
import sys
import subprocess
import time
import signal
import logging
from datetime import datetime
import psutil
import yaml

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class BotDeployer:
    """Production deployment manager"""
    
    def __init__(self, config_file='config.yaml'):
        self.config_file = config_file
        self.process = None
        self.restart_count = 0
        self.max_restarts = 10
        self.monitoring = True
        
    def deploy(self):
        """Deploy bot with monitoring"""
        print("""
        ╔══════════════════════════════════════════════╗
        ║     POLYMARKET BOT PRODUCTION DEPLOYMENT     ║
        ║     Target: Beat aesparing2 | Top 1%         ║
        ╚══════════════════════════════════════════════╝
        """)
        
        # Pre-deployment checks
        if not self.pre_deployment_checks():
            logger.error("Pre-deployment checks failed")
            return False
        
        # Setup signal handlers
        signal.signal(signal.SIGTERM, self.handle_shutdown)
        signal.signal(signal.SIGINT, self.handle_shutdown)
        
        # Start bot with monitoring
        self.start_bot()
        
        # Monitor loop
        while self.monitoring:
            if self.process and self.process.poll() is not None:
                # Process died
                logger.warning(f"Bot process died with code {self.process.returncode}")
                
                if self.restart_count < self.max_restarts:
                    logger.info(f"Restarting bot (attempt {self.restart_count + 1}/{self.max_restarts})")
                    time.sleep(10)  # Wait before restart
                    self.start_bot()
                    self.restart_count += 1
                else:
                    logger.error("Max restarts reached. Manual intervention required.")
                    self.monitoring = False
            
            # Check system resources
            self.check_system_health()
            
            time.sleep(30)  # Check every 30 seconds
    
    def pre_deployment_checks(self):
        """Run pre-deployment checks"""
        print("\n🔍 Running pre-deployment checks...")
        
        checks = {
            'config_exists': os.path.exists(self.config_file),
            'env_exists': os.path.exists('.env'),
            'dependencies': self.check_dependencies(),
            'wallet_config': self.check_wallet_config(),
            'network': self.check_network(),
            'disk_space': self.check_disk_space()
        }
        
        for check, passed in checks.items():
            status = "✅" if passed else "❌"
            print(f"  {status} {check}")
        
        return all(checks.values())
    
    def check_dependencies(self):
        """Check if all dependencies are installed"""
        try:
            import aiohttp
            import websockets
            import torch
            import selenium
            return True
        except ImportError:
            return False
    
    def check_wallet_config(self):
        """Check wallet configuration"""
        if not os.path.exists('.env'):
            return False
        
        with open('.env', 'r') as f:
            env_content = f.read()
            return 'WALLET_PRIVATE_KEYS' in env_content
    
    def check_network(self):
        """Check network connectivity"""
        try:
            import requests
            response = requests.get('https://polymarket.com', timeout=5)
            return response.status_code == 200
        except:
            return False
    
    def check_disk_space(self):
        """Check available disk space"""
        usage = psutil.disk_usage('/')
        # Need at least 1GB free
        return usage.free > 1024 * 1024 * 1024
    
    def start_bot(self):
        """Start the bot process"""
        try:
            logger.info(f"Starting bot with config: {self.config_file}")
            
            cmd = [
                sys.executable,
                'main.py',
                '--config', self.config_file
            ]
            
            self.process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True
            )
            
            logger.info(f"Bot started with PID: {self.process.pid}")
            
            # Log initial output
            for _ in range(10):
                if self.process.stdout:
                    line = self.process.stdout.readline()
                    if line:
                        logger.info(f"Bot output: {line.strip()}")
            
        except Exception as e:
            logger.error(f"Failed to start bot: {e}")
    
    def check_system_health(self):
        """Monitor system health"""
        try:
            # CPU usage
            cpu_percent = psutil.cpu_percent(interval=1)
            if cpu_percent > 90:
                logger.warning(f"High CPU usage: {cpu_percent}%")
            
            # Memory usage
            memory = psutil.virtual_memory()
            if memory.percent > 90:
                logger.warning(f"High memory usage: {memory.percent}%")
            
            # Check bot process
            if self.process:
                try:
                    proc = psutil.Process(self.process.pid)
                    proc_memory = proc.memory_info().rss / 1024 / 1024  # MB
                    
                    if proc_memory > 1000:  # Over 1GB
                        logger.warning(f"Bot using high memory: {proc_memory:.0f}MB")
                except psutil.NoSuchProcess:
                    logger.error("Bot process not found")
                    
        except Exception as e:
            logger.error(f"Health check error: {e}")
    
    def handle_shutdown(self, signum, frame):
        """Handle shutdown signals"""
        logger.info("Shutdown signal received")
        self.monitoring = False
        
        if self.process:
            logger.info("Stopping bot process...")
            self.process.terminate()
            time.sleep(5)
            
            if self.process.poll() is None:
                logger.warning("Force killing bot process")
                self.process.kill()
        
        logger.info("Deployment manager shutdown complete")
        sys.exit(0)


def setup_systemd_service():
    """Setup systemd service for auto-start"""
    service_content = """[Unit]
Description=Polymarket Trading Bot
After=network.target

[Service]
Type=simple
User={user}
WorkingDirectory={working_dir}
ExecStart={python_path} {script_path}
Restart=always
RestartSec=10
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
""".format(
        user=os.getenv('USER'),
        working_dir=os.getcwd(),
        python_path=sys.executable,
        script_path=os.path.join(os.getcwd(), 'deploy.py')
    )
    
    service_file = '/etc/systemd/system/polymarket-bot.service'
    
    print(f"""
To setup auto-start on system boot:

1. Save this as {service_file}:

{service_content}

2. Run these commands:
   sudo systemctl daemon-reload
   sudo systemctl enable polymarket-bot
   sudo systemctl start polymarket-bot
   
3. Check status:
   sudo systemctl status polymarket-bot
   journalctl -u polymarket-bot -f
""")


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Deploy Polymarket Bot')
    parser.add_argument('--config', default='config.yaml', help='Config file path')
    parser.add_argument('--systemd', action='store_true', help='Show systemd setup')
    
    args = parser.parse_args()
    
    if args.systemd:
        setup_systemd_service()
    else:
        deployer = BotDeployer(args.config)
        deployer.deploy()