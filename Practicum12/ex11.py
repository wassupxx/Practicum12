def ind_maxlist(a):
    """
    Рекурсивно выисляет индекс максимального элемента списка целочисленных элементов.
    """
    if len(a) == 1:
        return 0
    else:
        indmax_rest = ind_maxlist(a[1:])
        if a[0] > a[indmax_rest + 1]:
            return 0
        return indmax_rest + 1


a = list(map(int, input().split()))
print(ind_maxlist(a))
