"""
Enhanced Telegram Notification System
Gửi thông báo chi tiết về hoạt động của bot qua Telegram
"""

import asyncio
import aiohttp
import logging
from datetime import datetime, timedelta
from typing import Dict, List, Optional
from collections import defaultdict

logger = logging.getLogger(__name__)


class TelegramNotifier:
    """Hệ thống thông báo Telegram nâng cao"""
    
    def __init__(self, config: dict):
        """
        Initialize Telegram notifier
        
        Args:
            config: Bot configuration với alerts settings
        """
        self.config = config
        alerts_config = config.get('alerts', {})
        
        # Telegram credentials
        self.bot_token = alerts_config.get('telegram_bot_token', '')
        self.chat_id = alerts_config.get('telegram_chat_id', '')
        self.enabled = alerts_config.get('telegram_enabled', False)
        
        # Notification settings từ config
        self.notifications = alerts_config.get('notifications', {})
        
        # Cooldown để tránh spam
        self.last_notification_time = defaultdict(lambda: datetime.min)
        self.notification_cooldowns = {
            'order_placed': 0,  # Không cooldown cho order placed
            'order_cancelled': 30,  # 30s cooldown
            'order_filled': 0,  # Không cooldown cho fills (quan trọng!)
            'market_found': 60,  # 1 phút cooldown
            'market_removed': 60,  # 1 phút cooldown
            'error': 30,  # 30s cooldown
            'circuit_breaker': 300,  # 5 phút cooldown
            'risk_alert': 300,  # 5 phút cooldown
        }
        
        # Batch notifications (nhóm các thông báo tương tự)
        self.pending_batches = defaultdict(list)
        self.batch_intervals = {
            'market_found': 60,  # Gửi batch mỗi 60s
            'market_removed': 60,
        }
        
        if self.enabled and self.bot_token and self.chat_id:
            logger.info(f"✅ Telegram Notifier initialized (Chat ID: {self.chat_id})")
        else:
            logger.warning("⚠️  Telegram Notifier disabled or not configured")
    
    async def send_message(self, message: str, parse_mode: str = 'HTML') -> bool:
        """
        Gửi message qua Telegram
        
        Args:
            message: Nội dung message
            parse_mode: HTML hoặc Markdown
            
        Returns:
            True nếu gửi thành công
        """
        if not self.enabled or not self.bot_token or not self.chat_id:
            return False
        
        try:
            url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"
            
            data = {
                'chat_id': self.chat_id,
                'text': message,
                'parse_mode': parse_mode
            }
            
            async with aiohttp.ClientSession() as session:
                async with session.post(url, json=data, timeout=10) as response:
                    if response.status == 200:
                        logger.debug("✅ Telegram message sent")
                        return True
                    else:
                        error_text = await response.text()
                        logger.error(f"❌ Telegram send failed: {response.status} - {error_text}")
                        return False
                        
        except Exception as e:
            logger.error(f"❌ Telegram error: {e}")
            return False
    
    def _check_cooldown(self, notification_type: str) -> bool:
        """
        Kiểm tra cooldown cho notification type
        
        Returns:
            True nếu có thể gửi (không trong cooldown)
        """
        cooldown = self.notification_cooldowns.get(notification_type, 0)
        if cooldown == 0:
            return True
        
        last_time = self.last_notification_time[notification_type]
        elapsed = (datetime.now() - last_time).total_seconds()
        
        return elapsed >= cooldown
    
    def _update_cooldown(self, notification_type: str):
        """Cập nhật thời gian gửi notification cuối cùng"""
        self.last_notification_time[notification_type] = datetime.now()
    
    async def notify_order_placed(self, order: Dict, market: Dict):
        """
        Thông báo khi đặt lệnh mới
        
        Args:
            order: Order details
            market: Market details
        """
        if not self.notifications.get('order_placed', True):
            return
        
        if not self._check_cooldown('order_placed'):
            return
        
        # Extract order details
        market_name = market.get('question', 'Unknown')[:60]
        yes_price = order.get('yes_order', {}).get('price', 0)
        no_price = order.get('no_order', {}).get('price', 0)
        yes_size = order.get('yes_order', {}).get('size', 0)
        no_size = order.get('no_order', {}).get('size', 0)
        spread = order.get('spread', 0)
        
        message = f"""
📝 <b>Order Placed</b>
━━━━━━━━━━━━━━━━━━━━━━
🎯 Market: {market_name}

💰 <b>YES Order</b>
   • Price: ${yes_price:.3f}
   • Size: {yes_size} shares
   
💰 <b>NO Order</b>
   • Price: ${no_price:.3f}
   • Size: {no_size} shares

📊 Spread: {spread*100:.1f}%
⏰ {datetime.now().strftime('%H:%M:%S')}
        """
        
        await self.send_message(message.strip())
        self._update_cooldown('order_placed')
    
    async def notify_order_cancelled(self, order_id: str, market_name: str, reason: str):
        """
        Thông báo khi hủy lệnh
        
        Args:
            order_id: Order ID
            market_name: Tên market
            reason: Lý do hủy
        """
        if not self.notifications.get('order_cancelled', False):
            return
        
        if not self._check_cooldown('order_cancelled'):
            return
        
        message = f"""
🚫 <b>Order Cancelled</b>
━━━━━━━━━━━━━━━━━━━━━━
🎯 Market: {market_name[:60]}
🆔 Order ID: {order_id[:16]}...
📝 Reason: {reason}
⏰ {datetime.now().strftime('%H:%M:%S')}
        """
        
        await self.send_message(message.strip())
        self._update_cooldown('order_cancelled')
    
    async def notify_order_filled(self, fill_data: Dict, market: Dict, pnl: Optional[float] = None):
        """
        Thông báo khi lệnh bị fill (QUAN TRỌNG!)
        
        Args:
            fill_data: Fill details
            market: Market details
            pnl: Profit/Loss nếu có
        """
        if not self.notifications.get('order_filled', True):
            return
        
        # KHÔNG cooldown cho fills - luôn thông báo!
        
        market_name = market.get('question', 'Unknown')[:60]
        side = fill_data.get('side', 'Unknown')
        fill_price = fill_data.get('fill_price', 0)
        fill_size = fill_data.get('fill_size', 0)
        order_id = fill_data.get('order_id', 'Unknown')
        
        # Emoji dựa trên P&L
        pnl_emoji = "💰" if pnl and pnl > 0 else "📉" if pnl and pnl < 0 else "📊"
        
        message = f"""
🚨 <b>ORDER FILLED!</b> 🚨
━━━━━━━━━━━━━━━━━━━━━━
🎯 Market: {market_name}

📊 <b>Fill Details</b>
   • Side: {side.upper()}
   • Price: ${fill_price:.3f}
   • Size: {fill_size} shares
   • Order ID: {order_id[:16]}...
        """
        
        if pnl is not None:
            message += f"\n{pnl_emoji} <b>P&L: ${pnl:+.2f}</b>"
        
        message += f"\n\n⏰ {datetime.now().strftime('%H:%M:%S')}"
        
        await self.send_message(message.strip())
        self._update_cooldown('order_filled')
    
    async def notify_market_found(self, markets: List[Dict]):
        """
        Thông báo khi tìm thấy markets mới (batch)
        
        Args:
            markets: Danh sách markets mới
        """
        if not self.notifications.get('market_found', True):
            return
        
        if not markets:
            return
        
        # Batch notifications
        self.pending_batches['market_found'].extend(markets)
        
        # Chỉ gửi nếu đủ thời gian
        if not self._check_cooldown('market_found'):
            return
        
        pending = self.pending_batches['market_found']
        if not pending:
            return
        
        # Gửi tối đa 5 markets
        markets_to_show = pending[:5]
        total_count = len(pending)
        
        message = f"""
🔍 <b>New Markets Found</b>
━━━━━━━━━━━━━━━━━━━━━━
📊 Total: {total_count} market(s)

"""
        
        for i, market in enumerate(markets_to_show, 1):
            market_name = market.get('question', 'Unknown')[:50]
            reward = market.get('reward', 0)
            competition = market.get('competition_bars', 0)
            
            message += f"{i}. {market_name}\n"
            message += f"   💰 Reward: ${reward:.0f} | 📊 Competition: {competition} bars\n\n"
        
        if total_count > 5:
            message += f"... and {total_count - 5} more\n\n"
        
        message += f"⏰ {datetime.now().strftime('%H:%M:%S')}"
        
        await self.send_message(message.strip())
        self._update_cooldown('market_found')
        
        # Clear batch
        self.pending_batches['market_found'] = []
    
    async def notify_market_removed(self, market_name: str, reason: str):
        """
        Thông báo khi market bị loại bỏ
        
        Args:
            market_name: Tên market
            reason: Lý do loại bỏ
        """
        if not self.notifications.get('market_removed', False):
            return
        
        # Batch notifications
        self.pending_batches['market_removed'].append({
            'name': market_name,
            'reason': reason
        })
        
        if not self._check_cooldown('market_removed'):
            return
        
        pending = self.pending_batches['market_removed']
        if not pending:
            return
        
        message = f"""
⏭️ <b>Markets Removed</b>
━━━━━━━━━━━━━━━━━━━━━━
📊 Total: {len(pending)} market(s)

"""
        
        # Nhóm theo reason
        by_reason = defaultdict(list)
        for item in pending:
            by_reason[item['reason']].append(item['name'])
        
        for reason, names in by_reason.items():
            message += f"<b>{reason}:</b> {len(names)} market(s)\n"
        
        message += f"\n⏰ {datetime.now().strftime('%H:%M:%S')}"
        
        await self.send_message(message.strip())
        self._update_cooldown('market_removed')
        
        # Clear batch
        self.pending_batches['market_removed'] = []

    async def notify_error(self, error_type: str, error_message: str, context: Optional[str] = None):
        """
        Thông báo khi có lỗi

        Args:
            error_type: Loại lỗi
            error_message: Nội dung lỗi
            context: Context bổ sung
        """
        if not self.notifications.get('error', True):
            return

        if not self._check_cooldown('error'):
            return

        message = f"""
❌ <b>Error Occurred</b>
━━━━━━━━━━━━━━━━━━━━━━
🔴 Type: {error_type}
📝 Message: {error_message[:200]}
"""

        if context:
            message += f"📍 Context: {context[:100]}\n"

        message += f"\n⏰ {datetime.now().strftime('%H:%M:%S')}"

        await self.send_message(message.strip())
        self._update_cooldown('error')

    async def notify_circuit_breaker(self, service: str, status: str):
        """
        Thông báo khi circuit breaker được kích hoạt

        Args:
            service: Tên service (gamma_api, playwright_scraper, etc.)
            status: OPEN hoặc CLOSED
        """
        if not self.notifications.get('circuit_breaker', True):
            return

        if not self._check_cooldown('circuit_breaker'):
            return

        emoji = "🔴" if status == "OPEN" else "🟢"

        message = f"""
{emoji} <b>Circuit Breaker {status}</b>
━━━━━━━━━━━━━━━━━━━━━━
⚙️ Service: {service}
📊 Status: {status}
⏰ {datetime.now().strftime('%H:%M:%S')}
        """

        if status == "OPEN":
            message += "\n⚠️ Service temporarily disabled due to repeated failures"
        else:
            message += "\n✅ Service recovered and re-enabled"

        await self.send_message(message.strip())
        self._update_cooldown('circuit_breaker')

    async def notify_risk_alert(self, alert_type: str, details: Dict):
        """
        Thông báo về rủi ro cao

        Args:
            alert_type: Loại alert (high_exposure, position_size, etc.)
            details: Chi tiết về rủi ro
        """
        if not self.notifications.get('risk_alert', True):
            return

        if not self._check_cooldown('risk_alert'):
            return

        message = f"""
⚠️ <b>RISK ALERT</b>
━━━━━━━━━━━━━━━━━━━━━━
🚨 Type: {alert_type}

"""

        # Format details
        for key, value in details.items():
            if isinstance(value, float):
                message += f"   • {key}: {value:.2f}\n"
            else:
                message += f"   • {key}: {value}\n"

        message += f"\n⏰ {datetime.now().strftime('%H:%M:%S')}"

        await self.send_message(message.strip())
        self._update_cooldown('risk_alert')

    async def notify_startup(self, num_wallets: int):
        """
        Thông báo khi bot khởi động

        Args:
            num_wallets: Số lượng wallets
        """
        if not self.config.get('alerts', {}).get('alert_on_startup', True):
            return

        message = f"""
🚀 <b>Polymarket Bot Started</b>
━━━━━━━━━━━━━━━━━━━━━━
⏰ Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
💼 Wallets: {num_wallets}
📊 Status: Running

🔔 <b>Notifications Enabled:</b>
"""

        # List enabled notifications
        enabled = []
        if self.notifications.get('order_placed', True):
            enabled.append("✅ Order Placed")
        if self.notifications.get('order_cancelled', False):
            enabled.append("✅ Order Cancelled")
        if self.notifications.get('order_filled', True):
            enabled.append("✅ Order Filled")
        if self.notifications.get('market_found', True):
            enabled.append("✅ Markets Found")
        if self.notifications.get('error', True):
            enabled.append("✅ Errors")
        if self.notifications.get('risk_alert', True):
            enabled.append("✅ Risk Alerts")

        for item in enabled:
            message += f"   {item}\n"

        message += "\n━━━━━━━━━━━━━━━━━━━━━━\nBot is now scanning markets and placing orders."

        await self.send_message(message.strip())

    async def notify_shutdown(self, reason: str = "Manual shutdown"):
        """
        Thông báo khi bot tắt

        Args:
            reason: Lý do tắt
        """
        if not self.config.get('alerts', {}).get('alert_on_shutdown', True):
            return

        message = f"""
🛑 <b>Polymarket Bot Stopped</b>
━━━━━━━━━━━━━━━━━━━━━━
⏰ Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
📝 Reason: {reason}
📊 Status: Stopped
━━━━━━━━━━━━━━━━━━━━━━
        """

        await self.send_message(message.strip())

    async def notify_daily_report(self, stats: Dict):
        """
        Thông báo báo cáo hàng ngày

        Args:
            stats: Statistics từ optimizer
        """
        if not self.config.get('alerts', {}).get('alert_on_daily_report', True):
            return

        total_pnl = stats.get('total_pnl', 0)
        pnl_emoji = "💰" if total_pnl > 0 else "📉" if total_pnl < 0 else "📊"

        message = f"""
📊 <b>Daily Performance Report</b>
━━━━━━━━━━━━━━━━━━━━━━
📅 Date: {datetime.now().strftime('%Y-%m-%d')}

{pnl_emoji} <b>P&L: ${total_pnl:+.2f}</b>

📈 <b>Trading Stats</b>
   • Orders Placed: {stats.get('orders_placed', 0)}
   • Orders Filled: {stats.get('orders_filled', 0)}
   • Fill Rate: {stats.get('fill_rate', 0):.1%}
   • Markets Traded: {stats.get('markets_traded', 0)}

💰 <b>Rewards</b>
   • Estimated Rewards: ${stats.get('estimated_rewards', 0):.2f}
   • Actual Fills: ${stats.get('fill_pnl', 0):+.2f}

📊 <b>Performance</b>
   • Win Rate: {stats.get('win_rate', 0):.1%}
   • Avg Profit/Trade: ${stats.get('avg_profit', 0):.2f}
   • Best Trade: ${stats.get('best_trade', 0):+.2f}
   • Worst Trade: ${stats.get('worst_trade', 0):+.2f}

━━━━━━━━━━━━━━━━━━━━━━
        """

        await self.send_message(message.strip())

    async def notify_hourly_report(self, stats: Dict, health: Dict):
        """
        Thông báo báo cáo hàng giờ

        Args:
            stats: Statistics từ monitoring
            health: Health status
        """
        status_emoji = "✅" if health.get('healthy', True) else "⚠️"

        message = f"""
{status_emoji} <b>Hourly Report</b>
━━━━━━━━━━━━━━━━━━━━━━
⏰ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

📊 <b>Last 60 Minutes</b>
   • Scans: {stats.get('total_scans', 0)}
   • Markets Found: {stats.get('total_markets_found', 0)}
   • Orders Placed: {stats.get('total_orders_placed', 0)}
   • Orders Filled: {stats.get('total_orders_filled', 0)}
   • Profit: ${stats.get('total_profit', 0):.2f}

💻 <b>System</b>
   • CPU: {health.get('metrics', {}).get('system_cpu_percent', 0):.1f}%
   • RAM: {health.get('metrics', {}).get('system_memory_percent', 0):.1f}%
"""

        # Add issues if any
        issues = health.get('issues', [])
        if issues:
            message += "\n⚠️ <b>Issues:</b>\n"
            for issue in issues[:3]:  # Max 3 issues
                message += f"   • {issue.get('message', 'Unknown')}\n"

        message += "\n━━━━━━━━━━━━━━━━━━━━━━"

        await self.send_message(message.strip())

