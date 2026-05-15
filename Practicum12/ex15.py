def ten_to_bin(x):
    """
    Переводит натуральное число x из десятичной системы в двоичную.
    """
    if x == 0:
        return 0
    if x == 1:
        return 1
    return str(ten_to_bin(x // 2)) + str(x % 2)


x = int(input())
print((ten_to_bin(x)))
