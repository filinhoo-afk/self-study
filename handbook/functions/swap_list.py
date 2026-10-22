# Задача: функция swap принимает два списка и меняет их содержимое
# местами. Сами объекты-списки остаются теми же, поэтому результат
# должен быть виден во всех переменных, которые на них ссылаются.

def swap(a, b):
    temp = []
    for item in a:
        temp.append(item)

    a.clear()
    for item in b:
        a.append(item)

    b.clear()
    for item in temp:
        b.append(item)