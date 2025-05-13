def cache_results(max_arg):
    def decorator(func):
        cache = [None] * (max_arg + 1)

        def wrapper(n):
            nonlocal cache
            if n < 0 or n > max_arg:
                raise ValueError(f"Аргумент повинен бути в межах від 0 до {max_arg}")
            if cache[n] is not None:
                return cache[n]
            res = func(n)
            cache[n] = res
            return res
        return wrapper
    return decorator

@cache_results(100)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(30))