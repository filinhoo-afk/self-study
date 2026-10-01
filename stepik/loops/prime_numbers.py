# На вход программе подаются два натуральных числа a и b (a < b). Написать программу, которая находит все простые числа от a до b включительно.

a,b = int(input()), int(input())

for x in range(a, b + 1):
    count = 0
    for i in range(1, x + 1):
        if x % i == 0:
            count += 1
    if count == 2:
        print(x)