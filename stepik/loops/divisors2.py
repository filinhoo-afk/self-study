# Даны a и b (a < b). Найти число из отрезка [a; b] с максимальной суммой делителей.
# Если таких чисел несколько — взять наибольшее.
# Вывести через пробел: само число и сумму его делителей.

a, b = int(input()), int(input())
best_num = 0
best_sum = 0

for x in range(a, b + 1):
    total = 0
    for i in range(1, x + 1):
        if x % i == 0:
            total += i
    if total >= best_sum:
        best_sum = total
        best_num = x

print(best_num, best_sum)