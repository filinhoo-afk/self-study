# Условие: на вход подаются 2 строки. Сравнить их посимвольно, не учитывая регистр
# и игнорируя все небуквенные символы. Вывести YES, если строки равны
# в результате такой проверки, иначе NO.

first = input()
second = input()


first_letters = ''
for ch in first:
    if ch.isalpha():                 
        first_letters += ch.lower()  


second_letters = ''
for ch in second:
    if ch.isalpha():
        second_letters += ch.lower()


if first_letters == second_letters:
    print('YES')
else:
    print('NO')