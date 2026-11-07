# Написать функцию is_password_good(password), которая принимает в качестве аргумента строковое значение пароля password и возвращает значение True, если пароль является надёжным, или False в противном случае.


def is_password_good(password):
    has_upper = has_lower = has_digit = False
    for c in password:
        if c.isupper():
            has_upper = True
        elif c.islower():
            has_lower = True
        elif c.isdigit():
            has_digit = True
    return len(password) >= 8 and has_upper and has_lower and has_digit

txt = input()
print(is_password_good(txt))