
# 📦 `decorators.py` — Version avec `loguru`

```
from functools import wraps
from loguru import logger
import time
import inspect

# ⏱️ Decorator: Benchmark
def benchmark(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        duration = end - start
        logger.info(f"[Benchmark] {func.__name__} exécutée en {duration:.6f} s")
        return result
    return wrapper

# ✅ Decorator: Checker de types
def checker(expected_args: dict):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            sig = inspect.signature(func)
            bound = sig.bind(*args, **kwargs)
            bound.apply_defaults()

            for name, expected_type in expected_args.items():
                if name not in bound.arguments:
                    logger.error(f"[Checker] Argument manquant : {name}")
                    raise ValueError(f"Argument manquant : {name}")
                if not isinstance(bound.arguments[name], expected_type):
                    logger.error(
                        f"[Checker] Mauvais type pour '{name}': attendu {expected_type.__name__}, reçu {type(bound.arguments[name]).__name__}"
                    )
                    raise TypeError(
                        f"Mauvais type pour '{name}': attendu {expected_type.__name__}, reçu {type(bound.arguments[name]).__name__}"
                    )
            return func(*args, **kwargs)
        return wrapper
    return decorator

# 🔁 Decorator: Retry
def retry(max_attempts=3, delay=1, exceptions=(Exception,)):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(1, max_attempts + 1):
                try:
                    logger.debug(f"[Retry] Tentative {attempt} pour {func.__name__}")
                    return func(*args, **kwargs)
                except exceptions as e:
                    logger.warning(f"[Retry] Tentative {attempt} échouée : {e}")
                    last_exception = e
                    if attempt < max_attempts:
                        time.sleep(delay)
            logger.error(f"[Retry] Échec après {max_attempts} tentatives : {last_exception}")
            raise last_exception
        return wrapper
    return decorator
```

---

## 🔧 Exemple d’utilisation dans ton script

```
from decorators import benchmark, checker, retry
from random import random

@benchmark
@retry(max_attempts=4, delay=0.5)
@checker(expected_args={"x": int})
def traitement(x):
    if x < 3:
        raise ValueError("x trop petit")
    return x * 10

# traitement(5)
```

---

## 📁 Bonus : Configuration Loguru (dans ton script principal)

```
from loguru import logger

logger.add("app.log", rotation="1 MB", retention="7 days", level="DEBUG")
```

