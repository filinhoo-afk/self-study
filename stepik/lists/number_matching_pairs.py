# На вход программе подаётся строка текста, содержащая целые числа. Из данной строки формируется список чисел.
# Написать программу, которая подсчитывает, сколько в полученном списке пар элементов, равных друг другу. 
# Считается, что любые два элемента, равные друг другу, образуют одну пару, которую необходимо посчитать.

strings = input().split()
numbers = []

for item in strings:
    numbers.append(int(item))

count = 0

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j]:
            count += 1

print(count)
