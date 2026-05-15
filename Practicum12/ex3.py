def progress(a1, r, n):
    """
        Рекурсивно вычисляет n‑й член арифметической прогрессии.
    """
    if n == 1:
        return a1
    return progress(a1 + r, r, n - 1)


a1 = int(input("Enter a number: "))
r = int(input("Enter a number: "))
n = int(input("Enter a number: "))
print(progress(a1, r, n))
