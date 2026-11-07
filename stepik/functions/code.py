# Написать функцию code_format(text), которая принимает строку текста text, оборачивает её в теги <code></code> и возвращает результат.


def code_format(text):
    return f'<code>{text}</code>'

text = input()
print(code_format(text))