# Условие: на вход подаются натуральное число n, затем n целых чисел.
# Создать из них список, удалить все элементы, стоящие по нечётным индексам
# (индексы 1, 3, 5, ...), и вывести полученный список.


n = int(input())
numbers = []

for _ in range(n):
    numbers.append(int(input()))

result = []
for i in range(0, n, 2):
    result.append(numbers[i])

print(result)
    
