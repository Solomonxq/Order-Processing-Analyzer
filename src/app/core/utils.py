from collections.abc import Callable
from functools import wraps
from typing import TypeVar

from ..logs.loger import logger

F = TypeVar("F", bound=Callable[..., object])


def log_execution(func: F) -> F:
    @wraps(func)
    def wrapper(*args, **kwargs) -> object:
        import time

        start: float = time.time()
        result: object = func(*args, **kwargs)
        end: float = time.time()
        logger.info(
            f"Назва функції: {func.__name__} | Час виконання {end - start:.2f}s"
        )
        return result

    return wrapper


def retry(times: int = 3) -> Callable[[F], F]:
    def decor(func: F) -> F:
        @wraps(func)
        def wrapper(*args, **kwargs) -> object | None | None:
            last_exc: Exception | None = None
            for i in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as excp:
                    logger.warning(
                        f"Помилка у {func.__name__} (спроба {i + 1}/{times}): {excp}"
                    )
                    last_exc = excp
            if last_exc:
                raise last_exc
            return None

        return wrapper

    return decor