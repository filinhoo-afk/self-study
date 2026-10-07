# Условие: на вход подаются натуральное число n и n строк, а затем число k.
# Вывести k-ю букву из каждой из введённых строк на одной строке без пробелов.

n = int(input())
words = []

for _ in range(n):
    words.append(input())

k = int(input())

result = ''
for word in words:
    if len(word) >= k:           
        result += word[k - 1]

print(result)