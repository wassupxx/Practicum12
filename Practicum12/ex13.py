def odd_list(a, n):
    """
    Рекурсивно из списка, содержащего n целочисленных элементов, возвращает список четных значений.
    """
    if n == 0:
        return []
    first = a[0]
    rest_elements = odd_list(a[1:], n - 1)
    if first % 2 == 0:
        return [first] + rest_elements
    else:
        return rest_elements


a = list(map(int, input().split()))
n = int(input("Enter a number: "))
print(odd_list(a, n))
