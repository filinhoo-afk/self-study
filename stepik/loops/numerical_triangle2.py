# Дано натуральное число n. Напишите программу, которая печатает численный треугольник с высотой, равной n.

n = int(input())
num = 1

for i in range(1, n + 1):
    for j in range(i):
        print(num, end=' ')
        num += 1
    print()