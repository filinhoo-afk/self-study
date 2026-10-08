# На вход программе подаются натуральное число n, затем n строк.
# Напишите программу, которая для каждого введённого числа x выводит значение функции: 
# f(x) = x**2 + 2x + 1

n = int(input())
s = []
num = []

for _ in range(n):
    x = int(input())
    num.append(x)
    x = x ** 2 + 2 * x + 1
    s.append(x)

print(*num, sep='\n')    
print()    
print(*s, sep='\n')