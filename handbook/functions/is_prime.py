# Задача: функция is_prime(n) принимает натуральное число и возвращает True,
# если число простое (делится только на 1 и на себя), иначе False.
def is_prime(n):
    if n < 2:  # 1 не простое число
        return False

    result = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            result = False
            break
    return result