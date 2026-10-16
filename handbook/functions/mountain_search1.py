# Задача: функция find_mountains(heights) принимает список высот и
# возвращает кортеж номеров всех "гор" (точек выше обоих соседей).
# Нумерация с 1. Первый и последний элементы не проверяем.

def find_mountains(heights):
    number = list()

    for i in range(1, len(heights) - 1):
        if heights[i] > heights[i - 1] and heights[i] > heights[i + 1]:
            number.append(i + 1)

    return tuple(number)