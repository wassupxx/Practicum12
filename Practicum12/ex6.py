def degree5(n):
    """
    Рекурсивно вычисляет, какой степенью числа 5 является натуральное число n.
    """
    if n == 1:
        return 0
    if n < 1:
        return -1
    if n % 5 != 0:
        return -1
    result = degree5(n // 5)
    if result == -1:
        return -1
    return 1 + result


n = int(input("Enter a number: "))
print(degree5(n))
