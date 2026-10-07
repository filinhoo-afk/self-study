# Условие: на вход подаётся натуральное число n.
# Создать список из всех делителей числа n в порядке возрастания и вывести его.

n = int(input())
result = []

for i in range(1, n+1):
    if n % i == 0:
        result.append(i)
print(result)