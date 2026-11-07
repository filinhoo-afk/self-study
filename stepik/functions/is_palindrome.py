# Написать функцию is_palindrome(text), которая принимает в качестве аргумента строку text и возвращает значение True, если указанный текст является палиндромом, или False в противном случае.


def is_palindrome(text):
    cleaned = ''
    for c in text.lower():
        if c not in ' ,.!?-':
            cleaned += c
    return cleaned == cleaned[::-1]

txt = input()
print(is_palindrome(txt))