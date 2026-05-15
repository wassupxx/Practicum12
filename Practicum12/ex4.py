def sum_progress(a1, r, n):
    """
        Рекурсивно вычисляет сумму n членов арифмитеческой прогрессии
    """
    if n == 1:
        return a1
    return a1 + sum_progress(a1 + r, r, n - 1)


a1 = int(input("Enter a number: "))
r = int(input("Enter a number: "))
n = int(input("Enter a number: "))
print(sum_progress(a1, r, n))
