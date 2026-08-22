import time
import functools

def retry_on_failure( retires=3, delay=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, retires+ 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print("Attempt failed retrying again")
                    if attempt == retires:
                        raise e
                    time.sleep(delay)
        return wrapper
    return decorator



def log_eval_run(func):
    @functools.wraps(func)
    def wrapper_log_eval_run(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time-start_time
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k} = {repr(v)}" for k,v in kwargs.items()]
        print(f"function Name: {func.__name__}")
        print(f"function Positional Arguments are : {args_repr}")
        print(f"function Keyword Arguments are : {kwargs_repr}")
        print(f"function output is : {value}")
        print(f"functions execution time is : {total_time}")
        return value
    return wrapper_log_eval_run
        