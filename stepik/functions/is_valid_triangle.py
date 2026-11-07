# Написать функцию is_valid_triangle(side1, side2, side3), которая принимает в качестве аргументов три натуральных числа, и возвращает значение True
# Если существует невырожденный треугольник со сторонами side1, side2, side3, или False в противном случае.


def is_valid_triangle(side1, side2, side3):
    return side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1

a, b, c = int(input()), int(input()), int(input())
print(is_valid_triangle(a, b, c))