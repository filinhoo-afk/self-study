# Создайте функцию split_numbers(text), которая принимает строку целых чисел,
# разделённых пробелами, и возвращает кортеж этих чисел.
# В решении должны быть только функции, без вызовов требуемых функций.

def split_numbers(text):
    parts = text.split()
    numbers = []
    for part in parts:
        numbers.append(int(part))
    return tuple(numbers)