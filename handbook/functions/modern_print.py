# Задача: функция modern_print(text) печатает переданную строку, только если
# она ещё не выводилась ранее. Все уникальные строки должны запоминаться.

unique_strings = []


def modern_print(text):
    
    if text not in unique_strings:
        unique_strings.append(text)
        print(text)