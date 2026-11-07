# Написать функцию is_valid_password(password), которая принимает в качестве аргумента строковое значение пароля password и возвращает значение True, если пароль является действительным паролем BEEGEEK банка, или False в противном случае.


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def is_valid_password(password):
    parts = password.split(':')
    if len(parts) != 3:
        return False
    a, b, c = parts
    if not (a.isdigit() and b.isdigit() and c.isdigit()):
        return False
    return a == a[::-1] and is_prime(int(b)) and int(c) % 2 == 0

psw = input()
print(is_valid_password(psw))