# Задача: написать функцию draw_triangle(fill, base), которая печатает
# "треугольник" из символов fill: строки растут от 1 до середины
# и затем уменьшаются до 1. Параметр base нечётный.
# Например, для base = 5 получается: 1, 2, 3, 2, 1 символов в строках.

# объявление функции
def draw_triangle(fill, base):
    middle = (base + 1) // 2        # длина самой длинной (средней) строки

    # растущая часть: от 1 до middle
    for i in range(1, middle + 1):
        print(fill * i)

    # убывающая часть: от middle - 1 до 1
    for i in range(middle - 1, 0, -1):
        print(fill * i)

# считываем данные
fill = input()
base = int(input())

# вызываем функцию
draw_triangle(fill, base)