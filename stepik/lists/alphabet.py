# Условие: ввода нет. Вывести список вида ['a', 'bb', 'ccc', 'dddd', ...],
# где i-я буква английского алфавита повторяется i раз.
# Последний элемент состоит из 26 символов 'z'.

result = list()

for i in range(26):
    letter = chr(97 + i)                 
    result.append(letter * (i + 1))      

print(result)


