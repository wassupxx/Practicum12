def nod(a, b):
    """
    Рекурсивно вычисляет наибольший общий делитель двух натуральных чисел a и b.
    """
    if b == 0:
        return a
    return nod(b, a % b)


a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
print(nod(a, b))
