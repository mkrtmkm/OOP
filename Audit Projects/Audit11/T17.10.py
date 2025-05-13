from random import randint

def cashed_decoratior(func):
    cashed_res = {}
    def wrapper(*args, **kwargs):
        nonlocal cashed_res
        try:
            return cashed_res[args]
        except KeyError:
            res = func(*args, **kwargs)
            cashed_res[args] = res
            return res
    return wrapper

@cashed_decorator
def is_prine

def Monte_Carlo(n, m):
    c = 0
    for i in range(m):
        k = randint(1, n)
        if is_prine(k):
            c += 1
        return c/m

