# Даны n и m. Найти все целые a, b, c от 1 до n (не включая n),
# для которых a + 3*b + 2*c = m, и вывести их в виде "a + 3×b + 2×c = m".
# Если решений нет — вывести "При заданных n и m решений не существует."

n = int(input())
m = int(input())
found = False

for a in range(1, n):
    for b in range(1, n):
        for c in range(1, n):
            if a + 3 * b + 2 * c == m:
                print(a, ' + 3×', b, ' + 2×', c, ' = ', m, sep='')
                found = True

if not found:
    print('При заданных n и m решений не существует.')