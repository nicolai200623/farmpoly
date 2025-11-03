"""
Enhanced Monitoring System cho Polymarket Bot
Theo dõi health, performance, và gửi alerts khi có vấn đề
"""

import asyncio
import logging
from datetime import datetime, timedelta
from typing import Dict, List, Optional
from collections import deque
import psutil
import os

logger = logging.getLogger(__name__)


class MonitoringSystem:
    """Hệ thống monitoring nâng cao"""
    
    def __init__(self, config: dict, alert_sender):
        """
        Initialize monitoring system
        
        Args:
            config: Bot configuration
            alert_sender: MLPredictor instance để gửi alerts
        """
        self.config = config
        self.alert_sender = alert_sender
        
        # Monitoring metrics
        self.metrics = {
            'markets_scanned': deque(maxlen=100),  # Last 100 scans
            'markets_found': deque(maxlen=100),
            'orders_placed': deque(maxlen=100),
            'orders_filled': deque(maxlen=100),
            'errors': deque(maxlen=100),
            'api_response_times': deque(maxlen=100),
        }
        
        # Health status
        self.health_status = {
            'last_market_scan': None,
            'last_order_placed': None,
            'last_successful_api_call': None,
            'consecutive_errors': 0,
            'consecutive_zero_markets': 0,
            'system_cpu_percent': 0,
            'system_memory_percent': 0,
            'bot_memory_mb': 0,
        }
        
        # Alert thresholds
        self.thresholds = {
            'max_consecutive_errors': 5,
            'max_consecutive_zero_markets': 10,
            'max_cpu_percent': 80,
            'max_memory_percent': 80,
            'max_api_response_time': 10.0,  # seconds
            'min_scan_interval': 60,  # seconds - alert if no scan in 60s
        }
        
        # Alert cooldowns (để tránh spam)
        self.last_alerts = {}
        self.alert_cooldown = 300  # 5 minutes
        
        logger.info("✅ Monitoring System initialized")
    
    def record_market_scan(self, markets_found: int):
        """Ghi nhận kết quả quét markets"""
        now = datetime.now()
        
        self.metrics['markets_scanned'].append({
            'timestamp': now,
            'count': 1
        })
        
        self.metrics['markets_found'].append({
            'timestamp': now,
            'count': markets_found
        })
        
        self.health_status['last_market_scan'] = now
        
        # Reset hoặc tăng consecutive zero markets
        if markets_found == 0:
            self.health_status['consecutive_zero_markets'] += 1
        else:
            self.health_status['consecutive_zero_markets'] = 0
    
    def record_order_placed(self, order_id: str):
        """Ghi nhận order được đặt"""
        now = datetime.now()
        
        self.metrics['orders_placed'].append({
            'timestamp': now,
            'order_id': order_id
        })
        
        self.health_status['last_order_placed'] = now
    
    def record_order_filled(self, order_id: str, profit: float):
        """Ghi nhận order được fill"""
        now = datetime.now()
        
        self.metrics['orders_filled'].append({
            'timestamp': now,
            'order_id': order_id,
            'profit': profit
        })
    
    def record_error(self, error_type: str, error_message: str):
        """Ghi nhận lỗi"""
        now = datetime.now()
        
        self.metrics['errors'].append({
            'timestamp': now,
            'type': error_type,
            'message': error_message
        })
        
        self.health_status['consecutive_errors'] += 1
    
    def record_api_call(self, response_time: float, success: bool):
        """Ghi nhận API call"""
        now = datetime.now()
        
        self.metrics['api_response_times'].append({
            'timestamp': now,
            'response_time': response_time,
            'success': success
        })
        
        if success:
            self.health_status['last_successful_api_call'] = now
            self.health_status['consecutive_errors'] = 0
    
    def update_system_metrics(self):
        """Cập nhật system metrics (CPU, RAM)"""
        try:
            # System-wide metrics
            self.health_status['system_cpu_percent'] = psutil.cpu_percent(interval=1)
            self.health_status['system_memory_percent'] = psutil.virtual_memory().percent
            
            # Bot process metrics
            process = psutil.Process(os.getpid())
            self.health_status['bot_memory_mb'] = process.memory_info().rss / 1024 / 1024
            
        except Exception as e:
            logger.debug(f"Failed to update system metrics: {e}")
    
    async def check_health(self) -> Dict:
        """
        Kiểm tra health status và gửi alerts nếu cần
        
        Returns:
            Dict với health status và issues
        """
        issues = []
        now = datetime.now()
        
        # Update system metrics
        self.update_system_metrics()
        
        # Check 1: Consecutive errors
        if self.health_status['consecutive_errors'] >= self.thresholds['max_consecutive_errors']:
            issues.append({
                'severity': 'critical',
                'type': 'consecutive_errors',
                'message': f"🔴 {self.health_status['consecutive_errors']} lỗi liên tiếp!"
            })
        
        # Check 2: Consecutive zero markets
        if self.health_status['consecutive_zero_markets'] >= self.thresholds['max_consecutive_zero_markets']:
            issues.append({
                'severity': 'warning',
                'type': 'zero_markets',
                'message': f"⚠️ Không tìm thấy markets trong {self.health_status['consecutive_zero_markets']} lần quét liên tiếp"
            })
        
        # Check 3: No recent market scan
        if self.health_status['last_market_scan']:
            time_since_scan = (now - self.health_status['last_market_scan']).total_seconds()
            if time_since_scan > self.thresholds['min_scan_interval']:
                issues.append({
                    'severity': 'critical',
                    'type': 'no_scan',
                    'message': f"🔴 Không quét markets trong {time_since_scan:.0f}s!"
                })
        
        # Check 4: High CPU usage
        if self.health_status['system_cpu_percent'] > self.thresholds['max_cpu_percent']:
            issues.append({
                'severity': 'warning',
                'type': 'high_cpu',
                'message': f"⚠️ CPU cao: {self.health_status['system_cpu_percent']:.1f}%"
            })
        
        # Check 5: High memory usage
        if self.health_status['system_memory_percent'] > self.thresholds['max_memory_percent']:
            issues.append({
                'severity': 'warning',
                'type': 'high_memory',
                'message': f"⚠️ RAM cao: {self.health_status['system_memory_percent']:.1f}%"
            })
        
        # Check 6: Slow API responses
        if len(self.metrics['api_response_times']) > 0:
            recent_times = [m['response_time'] for m in list(self.metrics['api_response_times'])[-10:]]
            avg_response_time = sum(recent_times) / len(recent_times)
            
            if avg_response_time > self.thresholds['max_api_response_time']:
                issues.append({
                    'severity': 'warning',
                    'type': 'slow_api',
                    'message': f"⚠️ API chậm: {avg_response_time:.1f}s trung bình"
                })
        
        # Send alerts for critical issues
        for issue in issues:
            if issue['severity'] == 'critical':
                await self._send_alert_with_cooldown(issue['type'], issue['message'])
        
        return {
            'healthy': len([i for i in issues if i['severity'] == 'critical']) == 0,
            'issues': issues,
            'metrics': self.health_status
        }
    
    async def _send_alert_with_cooldown(self, alert_type: str, message: str):
        """Gửi alert với cooldown để tránh spam"""
        now = datetime.now()
        
        # Check cooldown
        if alert_type in self.last_alerts:
            time_since_last = (now - self.last_alerts[alert_type]).total_seconds()
            if time_since_last < self.alert_cooldown:
                logger.debug(f"Alert {alert_type} in cooldown ({time_since_last:.0f}s)")
                return
        
        # Send alert
        try:
            await self.alert_sender.send_alert(f"🚨 <b>MONITORING ALERT</b>\n\n{message}")
            self.last_alerts[alert_type] = now
            logger.info(f"Alert sent: {alert_type}")
        except Exception as e:
            logger.error(f"Failed to send alert: {e}")
    
    def get_statistics(self, time_window_minutes: int = 60) -> Dict:
        """
        Lấy thống kê trong khoảng thời gian
        
        Args:
            time_window_minutes: Khoảng thời gian (phút)
        
        Returns:
            Dict với statistics
        """
        now = datetime.now()
        cutoff = now - timedelta(minutes=time_window_minutes)
        
        # Filter metrics trong time window
        recent_scans = [m for m in self.metrics['markets_scanned'] if m['timestamp'] > cutoff]
        recent_found = [m for m in self.metrics['markets_found'] if m['timestamp'] > cutoff]
        recent_orders = [m for m in self.metrics['orders_placed'] if m['timestamp'] > cutoff]
        recent_fills = [m for m in self.metrics['orders_filled'] if m['timestamp'] > cutoff]
        recent_errors = [m for m in self.metrics['errors'] if m['timestamp'] > cutoff]
        
        # Calculate stats
        total_markets_found = sum(m['count'] for m in recent_found)
        total_scans = len(recent_scans)
        avg_markets_per_scan = total_markets_found / total_scans if total_scans > 0 else 0
        
        total_profit = sum(m['profit'] for m in recent_fills)
        fill_rate = len(recent_fills) / len(recent_orders) if len(recent_orders) > 0 else 0
        
        return {
            'time_window_minutes': time_window_minutes,
            'total_scans': total_scans,
            'total_markets_found': total_markets_found,
            'avg_markets_per_scan': avg_markets_per_scan,
            'total_orders_placed': len(recent_orders),
            'total_orders_filled': len(recent_fills),
            'fill_rate': fill_rate,
            'total_profit': total_profit,
            'total_errors': len(recent_errors),
            'error_rate': len(recent_errors) / total_scans if total_scans > 0 else 0,
        }
    
    async def send_hourly_report(self):
        """Gửi báo cáo hàng giờ"""
        stats = self.get_statistics(time_window_minutes=60)
        health = await self.check_health()
        
        # Format report
        status_emoji = "✅" if health['healthy'] else "⚠️"
        
        report = f"""
{status_emoji} <b>Hourly Report</b>
━━━━━━━━━━━━━━━━━━━━━━
⏰ Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

📊 <b>Performance (Last 60 min)</b>
   • Scans: {stats['total_scans']}
   • Markets found: {stats['total_markets_found']} ({stats['avg_markets_per_scan']:.1f}/scan)
   • Orders placed: {stats['total_orders_placed']}
   • Orders filled: {stats['total_orders_filled']} ({stats['fill_rate']:.1%})
   • Profit: ${stats['total_profit']:.2f}
   • Errors: {stats['total_errors']} ({stats['error_rate']:.1%})

💻 <b>System Health</b>
   • CPU: {health['metrics']['system_cpu_percent']:.1f}%
   • RAM: {health['metrics']['system_memory_percent']:.1f}%
   • Bot RAM: {health['metrics']['bot_memory_mb']:.0f} MB
        """
        
        # Add issues if any
        if health['issues']:
            report += "\n\n⚠️ <b>Issues:</b>\n"
            for issue in health['issues']:
                report += f"   • {issue['message']}\n"
        
        report += "\n━━━━━━━━━━━━━━━━━━━━━━"
        
        try:
            await self.alert_sender.send_alert(report.strip())
            logger.info("✅ Hourly report sent")
        except Exception as e:
            logger.error(f"Failed to send hourly report: {e}")

