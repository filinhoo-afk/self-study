# Задача: функция merge принимает два отсортированных по возрастанию
# кортежа целых чисел и возвращает один отсортированный кортеж
# со всеми числами. Встроенные функции сортировки использовать нельзя.

def merge(x, y):
    result = []
    i = 0
    j = 0

    while i < len(x) and j < len(y):
        if x[i] <= y[j]:
            result.append(x[i])
            i = i + 1
        else:
            result.append(y[j])
            j = j + 1

    while i < len(x):
        result.append(x[i])
        i = i + 1

    while j < len(y):
        result.append(y[j])
        j = j + 1

    return tuple(result)