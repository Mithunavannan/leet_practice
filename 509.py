n = 2

def fib(n):
    if n is None:
        return 0
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        return fib(n - 1) + fib(n - 2)