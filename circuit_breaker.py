"""
Circuit Breaker Pattern Implementation
Tránh spam API calls khi có lỗi liên tục
"""

import asyncio
import logging
from datetime import datetime, timedelta
from enum import Enum
from typing import Callable, Any, Optional

logger = logging.getLogger(__name__)


class CircuitState(Enum):
    """Trạng thái của circuit breaker"""
    CLOSED = "closed"  # Hoạt động bình thường
    OPEN = "open"  # Ngừng gọi API, trả về lỗi ngay
    HALF_OPEN = "half_open"  # Thử gọi lại để kiểm tra


class CircuitBreaker:
    """
    Circuit Breaker để bảo vệ API calls
    
    Hoạt động:
    1. CLOSED: Cho phép tất cả requests, đếm failures
    2. Khi failures >= threshold → OPEN
    3. OPEN: Reject tất cả requests trong timeout period
    4. Sau timeout → HALF_OPEN
    5. HALF_OPEN: Cho phép 1 request thử
       - Thành công → CLOSED
       - Thất bại → OPEN lại
    """
    
    def __init__(
        self,
        name: str,
        failure_threshold: int = 5,
        timeout_seconds: int = 60,
        success_threshold: int = 2
    ):
        """
        Initialize circuit breaker
        
        Args:
            name: Tên của circuit (để logging)
            failure_threshold: Số lỗi liên tiếp để mở circuit
            timeout_seconds: Thời gian chờ trước khi thử lại (OPEN → HALF_OPEN)
            success_threshold: Số lần thành công liên tiếp để đóng circuit (HALF_OPEN → CLOSED)
        """
        self.name = name
        self.failure_threshold = failure_threshold
        self.timeout_seconds = timeout_seconds
        self.success_threshold = success_threshold
        
        # State
        self.state = CircuitState.CLOSED
        self.failure_count = 0
        self.success_count = 0
        self.last_failure_time: Optional[datetime] = None
        self.last_state_change: datetime = datetime.now()
        
        # Statistics
        self.total_calls = 0
        self.total_failures = 0
        self.total_successes = 0
        self.total_rejected = 0
        
        logger.info(f"✅ Circuit Breaker '{name}' initialized (threshold={failure_threshold}, timeout={timeout_seconds}s)")
    
    async def call(self, func: Callable, *args, **kwargs) -> Any:
        """
        Gọi function với circuit breaker protection
        
        Args:
            func: Async function cần gọi
            *args, **kwargs: Arguments cho function
        
        Returns:
            Kết quả của function
        
        Raises:
            CircuitBreakerOpenError: Nếu circuit đang OPEN
            Exception: Lỗi từ function được gọi
        """
        self.total_calls += 1
        
        # Check state
        if self.state == CircuitState.OPEN:
            # Check if timeout has passed
            if self._should_attempt_reset():
                self._transition_to_half_open()
            else:
                self.total_rejected += 1
                raise CircuitBreakerOpenError(
                    f"Circuit breaker '{self.name}' is OPEN. "
                    f"Will retry in {self._time_until_retry():.0f}s"
                )
        
        # Try to call function
        try:
            result = await func(*args, **kwargs)
            self._on_success()
            return result
            
        except Exception as e:
            self._on_failure()
            raise e
    
    def _on_success(self):
        """Xử lý khi call thành công"""
        self.total_successes += 1
        self.failure_count = 0
        
        if self.state == CircuitState.HALF_OPEN:
            self.success_count += 1
            
            if self.success_count >= self.success_threshold:
                self._transition_to_closed()
    
    def _on_failure(self):
        """Xử lý khi call thất bại"""
        self.total_failures += 1
        self.failure_count += 1
        self.success_count = 0
        self.last_failure_time = datetime.now()
        
        if self.state == CircuitState.HALF_OPEN:
            # Fail ngay trong HALF_OPEN → quay lại OPEN
            self._transition_to_open()
            
        elif self.state == CircuitState.CLOSED:
            if self.failure_count >= self.failure_threshold:
                self._transition_to_open()
    
    def _should_attempt_reset(self) -> bool:
        """Kiểm tra xem đã đến lúc thử reset chưa"""
        if self.last_failure_time is None:
            return False
        
        time_since_failure = (datetime.now() - self.last_failure_time).total_seconds()
        return time_since_failure >= self.timeout_seconds
    
    def _time_until_retry(self) -> float:
        """Tính thời gian còn lại cho đến khi retry"""
        if self.last_failure_time is None:
            return 0
        
        time_since_failure = (datetime.now() - self.last_failure_time).total_seconds()
        return max(0, self.timeout_seconds - time_since_failure)
    
    def _transition_to_open(self):
        """Chuyển sang trạng thái OPEN"""
        if self.state != CircuitState.OPEN:
            logger.warning(
                f"🔴 Circuit breaker '{self.name}' OPENED "
                f"(failures: {self.failure_count}/{self.failure_threshold})"
            )
            self.state = CircuitState.OPEN
            self.last_state_change = datetime.now()
    
    def _transition_to_half_open(self):
        """Chuyển sang trạng thái HALF_OPEN"""
        logger.info(f"🟡 Circuit breaker '{self.name}' HALF_OPEN (attempting reset)")
        self.state = CircuitState.HALF_OPEN
        self.success_count = 0
        self.last_state_change = datetime.now()
    
    def _transition_to_closed(self):
        """Chuyển sang trạng thái CLOSED"""
        logger.info(
            f"🟢 Circuit breaker '{self.name}' CLOSED "
            f"(successes: {self.success_count}/{self.success_threshold})"
        )
        self.state = CircuitState.CLOSED
        self.failure_count = 0
        self.success_count = 0
        self.last_state_change = datetime.now()
    
    def reset(self):
        """Manually reset circuit breaker"""
        logger.info(f"🔄 Circuit breaker '{self.name}' manually reset")
        self.state = CircuitState.CLOSED
        self.failure_count = 0
        self.success_count = 0
        self.last_failure_time = None
    
    def get_stats(self) -> dict:
        """Lấy statistics"""
        uptime = (datetime.now() - self.last_state_change).total_seconds()
        
        return {
            'name': self.name,
            'state': self.state.value,
            'failure_count': self.failure_count,
            'success_count': self.success_count,
            'total_calls': self.total_calls,
            'total_successes': self.total_successes,
            'total_failures': self.total_failures,
            'total_rejected': self.total_rejected,
            'success_rate': self.total_successes / self.total_calls if self.total_calls > 0 else 0,
            'time_in_current_state': uptime,
            'time_until_retry': self._time_until_retry() if self.state == CircuitState.OPEN else 0,
        }


class CircuitBreakerOpenError(Exception):
    """Exception raised when circuit breaker is open"""
    pass


# Decorator để dễ dàng sử dụng circuit breaker
def with_circuit_breaker(breaker: CircuitBreaker):
    """
    Decorator để wrap async function với circuit breaker
    
    Usage:
        breaker = CircuitBreaker("my_api")
        
        @with_circuit_breaker(breaker)
        async def call_api():
            # API call here
            pass
    """
    def decorator(func: Callable):
        async def wrapper(*args, **kwargs):
            return await breaker.call(func, *args, **kwargs)
        return wrapper
    return decorator


# Example usage
async def example():
    """Example usage of circuit breaker"""
    
    # Create circuit breaker
    breaker = CircuitBreaker(
        name="example_api",
        failure_threshold=3,
        timeout_seconds=10,
        success_threshold=2
    )
    
    # Simulate API calls
    async def unreliable_api():
        """Simulated unreliable API"""
        import random
        if random.random() < 0.7:  # 70% failure rate
            raise Exception("API Error")
        return "Success"
    
    # Try calling API
    for i in range(20):
        try:
            result = await breaker.call(unreliable_api)
            print(f"Call {i+1}: {result}")
        except CircuitBreakerOpenError as e:
            print(f"Call {i+1}: Circuit OPEN - {e}")
        except Exception as e:
            print(f"Call {i+1}: Failed - {e}")
        
        await asyncio.sleep(1)
    
    # Print stats
    stats = breaker.get_stats()
    print(f"\nStats: {stats}")


if __name__ == "__main__":
    asyncio.run(example())

