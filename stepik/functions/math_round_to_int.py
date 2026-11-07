# Написать функцию math_round_to_int(num), которая принимает положительное число с плавающей точкой num, округляет его до целого по математическим правилам, и возвращает результат.


def math_round_to_int(num):
    return int(num + 0.5)

num = float(input())
print(math_round_to_int(num))