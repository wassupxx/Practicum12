from functools import lru_cache


@lru_cache(maxsize=None)
def fib(k):
    """
    Рекурсивно вычисляет k-ый член последовательности Фибоначчи
    """
    if k < 3:
        return 1
    return fib(k - 1) + fib(k - 2)


k = int(input("Enter a number: "))
print(fib(k))
