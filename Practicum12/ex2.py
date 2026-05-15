def count(n):
    """
        Рекурсивно подсчитывает количество цифр в натуральном числе.
    """
    if n < 10:
        return 1
    return 1 + count(n // 10)


n = int(input("Enter a number: "))
print(count(n))
