def comp(a, b, m, n):
    """
        Возвращает длину НОП в строках a и b
    """
    if m == 0 or n == 0:
        return 0
    if a[m - 1] == b[n - 1]:
        return 1 + comp(a, b, m - 1, n - 1)
    return max(comp(a, b, m - 1, n), comp(a, b, m, n - 1))


a = input()
b = input()
m = int(input())
n = int(input())
print(comp(a, b, m, n))
