# Написать функцию convert_to_python_case(text), которая принимает в качестве аргумента строку в «верблюжьем регистре» и преобразует его в «змеиный регистр».


def convert_to_python_case(text):
    result = ''
    for i in range(len(text)):
        c = text[i]
        if c.isupper():
            if i != 0:
                result += '_'
            result += c.lower()
        else:
            result += c
    return result

txt = input()
print(convert_to_python_case(txt))