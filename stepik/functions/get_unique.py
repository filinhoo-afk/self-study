# Написать функцию get_unique(numbers), которая принимает список целых чисел numbers и возвращает новый список без повторяющихся значений, при этом сохраняя порядок появления чисел в исходном списке.


def get_unique(numbers):
    result = []
    for num in numbers:
        if num not in result:
            result.append(num)
    return result

numbers = eval(input())
print(get_unique(numbers))