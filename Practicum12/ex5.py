def mod_number(a, b):
    """
    Рекурсивно находит остаток от деления натурального числа a на натуральное число b.
    """
    if a < b:
        return a
    return mod_number(a - b, b)


a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
print(mod_number(a, b))
