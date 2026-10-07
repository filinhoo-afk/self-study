# Условие: даны число n и n строк вида
# <фамилия> <инициалы>, «<название книги>».
# Книги должны идти по возрастанию: сначала по фамилии автора,
# а при одинаковых фамилиях по названию (инициалы игнорируются).
# Вывести YES, если книги отсортированы верно, иначе NO.

n = int(input())

is_sorted = True     
prev_surname = ''    
prev_title = ''       

for i in range(n):
    line = input()

    parts = line.split()
    surname = parts[0]

    start = line.find('«')    
    end = line.rfind('»')     
    title = line[start + 1:end]

    if i > 0:
        if surname < prev_surname:
            is_sorted = False
        elif surname == prev_surname and title < prev_title:
            is_sorted = False

    prev_surname = surname
    prev_title = title

if is_sorted:
    print('YES')
else:
    print('NO')
