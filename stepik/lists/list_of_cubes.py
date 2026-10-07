# Условие: на вход подаются натуральное число n, а затем n целых чисел.
# Создать из этих чисел список их кубов и вывести его.

n = int(input())
result = list()

for _ in range(n):
    result.append(int(input())**3)
    
print(result)


