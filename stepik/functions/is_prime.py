# Написать функцию is_prime(num), которая принимает в качестве аргумента натуральное число и возвращает значение True, если число является простым, или False в противном случае.


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input())
print(is_prime(n))