def search(a, x):
    """
    Рекурсивно определяет, имеется ли среди целочисленных значений списка a, число x.
    """
    if len(a) == 0:
        return 0
    if (a[0]) == x:
        return 1
    return search(a[1:], x)


a = list(map(int, input().split()))
x = int(input("Enter a number: "))
print(search(a, x))
