# Создать две функции для онлайн-кликера:
# click() - увеличивает значение счётчика на 1;
# get_count() - возвращает текущее значение счётчика.
# В решении не должно быть вызовов функций.

count = 0


def click():
    global count
    count = count + 1


def get_count():
    return count