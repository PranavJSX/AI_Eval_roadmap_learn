import time
import functools

def time_and_log(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        start = time.perf_counter()
        result = func(*args,**kwargs)
        end = time.perf_counter()
        duration = end-start
        print(f"[LOG] Ran {func.__name__} in {duration:.4f}s Reuslt = {result}")
        return result
    return wrapper

