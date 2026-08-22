import functools
import time

def cache_response(func):
    cache = {}

    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        key = (args, tuple(sorted(kwargs.items())))

        if key in cache:
            print(f"[CACHE HIT] Returning cached result for key : {args[1:] if len(args)>1 else args}")
            return cache[key]

        result = func(*args,**kwargs)
        cache[key] = result
        return result
    return wrapper



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