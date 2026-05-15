def maxlist(a):
    """
    Рекурсивно вычисляет максимальный элемент списка целочисленных элементов.
    """
    if len(a) == 1:
        return a[0]
    else:
        max_rest = maxlist(a[1:])
        return a[0] if a[0] > max_rest else max_rest


a = list(map(int, input().split()))
print(maxlist(a))
