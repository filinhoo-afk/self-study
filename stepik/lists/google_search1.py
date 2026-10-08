# На вход программе подаются натуральное число n, затем n строк, затем ещё одна строка – поисковый запрос.
# Написать программу, которая выводит все введённые строки, в которых встречается поисковый запрос.

n = int(input())
x = []
y = []

for _ in range(n):
    x.append(input())

search = input()
for i in range(len(x)):
    if search.lower() in x[i].lower():
        y.append(x[i])
print(*y, sep='\n')
