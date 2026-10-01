# Дано n. Напечатать треугольник высотой n:
# 1
# 121
# 12321
# 1234321 ...
# (в строке i: числа от 1 до i, затем обратно до 1, без пробелов)

n = int(input())

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end='')
    for j in range(i - 1, 0, -1):
        print(j, end='')
    print()