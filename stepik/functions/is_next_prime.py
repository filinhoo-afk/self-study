# Написать функцию get_next_prime(num), которая принимает в качестве аргумента натуральное число num и возвращает первое простое число, большее числа num.


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def get_next_prime(num):
    num += 1
    while not is_prime(num):
        num += 1
    return num

n = int(input())
print(get_next_prime(n))