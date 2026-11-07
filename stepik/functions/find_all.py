# Написать функцию с именем find_all(target, symbol), которая принимает два аргумента: строку target и символ symbol и возвращает список, содержащий все местоположения этого символа в строке.


def find_all(target, symbol):
    return [i for i in range(len(target)) if target[i] == symbol]

s = input()
char = input()
print(find_all(s, char))