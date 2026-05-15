def count(a, b):
    """
    Возвращает количество квадратов, которые можно отсечь от прямоугольника a×b.
    """

    if a == b:
        return 1

    if a % b == 0:
        return a // b

    return a // b + count(a % b, b)


a = int(input())
b = int(input())

print(count(a, b))
