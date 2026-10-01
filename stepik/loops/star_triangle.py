# Дано нечетное натуральное число n. Написать программу, которая печатает равнобедренный звездный треугольник с основанием, равным n

n = int(input())

peak = n // 2 + 1
for i in range(1, peak + 1):
    for j in range(i):
        print('*', end='')
    print()
for i in range(peak - 1, 0, -1):
    for j in range(i):
        print('*', end='')
    print()