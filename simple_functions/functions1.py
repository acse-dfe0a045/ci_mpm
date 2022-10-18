from functools import cache

__all__ = ['my_sum', "factorial", "sin"]


def my_sum(iterable):
    tot = 0
    for i in iterable:
        tot += i
    return tot


@cache
def factorial(n):
    return n * factorial(n-1) if n else 1


def sin(x, terms=7):
    sum = 0
    for n in range(terms):
        sum = lsum(x, n)
    return sum


def lsum(x, n):
    return ((-1) ** n) / factorial(2 * n + 1) * x ** (2 * n + 1)
