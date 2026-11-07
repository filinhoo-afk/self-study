# Написать функцию convert_to_miles(km), которая принимает в качестве аргумента расстояние в километрах и возвращает расстояние в милях.

# объявление функции
def convert_to_miles(km):
    ml = km * 0.6214
    return ml


# считываем данные
num = int(input())

# вызываем функцию
print(convert_to_miles(num))


