def pownum(a, n):
    """
        Рекурсивно вычисляет степень n вещественного числа a.
    """
    if n == 1:
        return a
    return a * pownum(a, n - 1)


a = int(input("Enter a number: "))
n = int(input("Enter a number: "))
print(pownum(a, n))
