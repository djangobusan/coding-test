def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
def tail_fibonacci(n, a = 0, b = 1):
    if n == 0:
        return a
    if n == 1:
        return b
    return tail_fibonacci(n - 1, b, a + b);

__fibo_cache__ = {}
def memoization_fibonacci(n):
    if n in __fibo_cache__:
        return __fibo_cache__[n]
    else:
        __fibo_cache__[n] = n if n < 2 else memoization_fibonacci(n-2) + memoization_fibonacci(n-1)
        return __fibo_cache__[n]