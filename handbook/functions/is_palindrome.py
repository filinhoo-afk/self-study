# Создайте функцию is_palindrome(x), которая принимает одно значение
# (число, строку, кортеж или список) и возвращает True, если передан палиндром, и False — в противном случае.


def is_palindrome(x):
    result = False
    if isinstance(x, int) == True:
        if str(x) == str(x)[::-1]:
            result = True
    else:
        if x == x[::-1]: 
            result = True
    return result

print(is_palindrome(-121))