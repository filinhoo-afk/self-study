# Написать функцию get_last_index(data, value), которая принимает на вход список data и некоторое значение value 
# И возвращает индекс последнего вхождения данного значения в список или текст «ERROR!» (без кавычек), если искомое значение отсутствует в списке.


def get_last_index(data, value):
    for i in range(len(data) - 1, -1, -1):
        if data[i] == value:
            return i
    return 'ERROR!'

data = eval(input())
value = eval(input())
print(get_last_index(data, value))