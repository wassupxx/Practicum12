def combin(n, k):
    """
    Рекурсивно вычисляет комбинаторное сочетание
    """
    if k == 0 or n == k:
        return 1
    if k > n:
        return 0
    return combin(n - 1, k - 1) + combin(n - 1, k)



n = int(input("Enter a number: "))
k = int(input("Enter a number: "))
print(combin(n, k))
