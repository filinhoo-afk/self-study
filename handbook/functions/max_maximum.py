# Напишите функцию max2D(matrix), которая принимает список списков целых чисел
# (таблицу) и возвращает максимальный элемент.
# В решении не должно быть вызовов требуемых функций.

def max2D(matrix):
    result = matrix[0][0]
    for row in matrix:
        for number in row:
            if number > result:
                result = number
    return result
