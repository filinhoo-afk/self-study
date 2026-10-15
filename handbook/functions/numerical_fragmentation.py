# Напишите функцию fragments(numbers), которая принимает список целых чисел
# и возвращает список вложенных списков, где каждый вложенный список -
# возрастающий отрезок исходной последовательности (каждое следующее число
# больше предыдущего).
# В решении не должно быть вызовов требуемых функций.

def fragments(numbers):
    if len(numbers) == 0:
        return []
    result = []
    current = [numbers[0]]
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            current.append(numbers[i])
        else:
            result.append(current)
            current = [numbers[i]]
    result.append(current)
    return result