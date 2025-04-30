import time
def benchmark(f):
    def wrapper(*args, **kwargs):
        t = time.perf_counter()
        result = f(*args, **kwargs)
        t = time.perf_counter() - t
        print(f"{f.__name__} took {t} seconds")
        return result
    return wrapper

@benchmark
def fibonacci_iter(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b



def fibonacci_rec(n):
    if n <= 1:
        return n
    return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)


@benchmark
def run_fib_rec(n):
    return fibonacci_rec(n)

n = 50
print("Ітеративний варіант:")
print(fibonacci_iter(n))
print("Рекурсивний варіант:")
print(run_fib_rec(n))