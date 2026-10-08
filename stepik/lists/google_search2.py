# Задача: на вход подаётся число n, затем n строк, затем число k,
# затем k поисковых запросов. Нужно вывести все введённые строки,
# в которых встречаются одновременно ВСЕ поисковые запросы.
# Поиск не зависит от регистра символов.

n = int(input())
x = []
for _ in range(n):
    x.append(input())

k = int(input())
queries = []
for _ in range(k):
    queries.append(input())

for line in x:
    all_found = True
    for q in queries:
        if q.lower() not in line.lower():
            all_found = False
    if all_found:
        print(line)