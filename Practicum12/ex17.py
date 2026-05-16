def function1(x):
    """
    Определяет, является ли натуральное число x простым.
    Возвращает 1, если число простое, иначе — 0.
    """
    if x < 2:
        return 0
    if x == 2:
        return 1
    if x % 2 == 0:
        return 0
    return 1 if _is_prime_recursive(x, 3) else 0


def _is_prime_recursive(n, divider):
    """
    Вспомогательная рекурсивная функция для проверки простоты числа.
    Проверяет, делится ли n на какой‑либо нечётный делитель, начиная с divisor.
    """
    # Если divider² > n, значит, делителей нет — число простое
    if divider * divider > n:
        return True
    if n % divider == 0:
        return False
    return _is_prime_recursive(n, divider + 2)
