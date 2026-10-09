# На вход программе подаётся строка текста, содержащая различные натуральные числа. Вам необходимо переставить максимальный и минимальный элементы местами и вывести изменённую строку.

numbers = input().split()

min_num = min(numbers, key=int)
max_num = max(numbers, key=int)

min_index = numbers.index(min_num)
max_index = numbers.index(max_num)

numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]

print(*numbers)



