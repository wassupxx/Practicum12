def numbers(x):
    """
    Выводит на экран цифры натурального числа x в обратном порядке.
    """
    if x < 10:
        return x
    print(x % 10)
    return numbers(x // 10)
x = int(input())
print(numbers(x))
