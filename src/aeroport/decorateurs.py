import logging
import time
from functools import wraps


def benchmark(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        duration = end - start
        logging.info(f"[Benchmark] {func.__name__} exécutée en {duration:.6f} s")
        return result
    return wrapper