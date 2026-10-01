# Дано натуральное число n. Написать программу, которая выводит значение суммы 1! + 2! + 3! + … + n!.

n = int(input())
total = 0

for i in range(1, n + 1):
    fact = 1
    for j in range(1, i + 1):
        fact *= j
    total += fact

print(total)