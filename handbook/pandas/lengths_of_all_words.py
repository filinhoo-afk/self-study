# Задача: функция length_stats(text) возвращает Series,
# где индексы — слова текста (в нижнем регистре, без знаков препинания и цифр,
# без повторов, отсортированные по алфавиту), а значения — длины этих слов.

import pandas as pd


def length_stats(text):
    # 1. Переводим весь текст в нижний регистр
    text = text.lower()

    # 2. Оставляем только буквы и пробелы, остальное выбрасываем
    clean = ''
    for char in text:
        if char.isalpha() or char.isspace():
            clean = clean + char

    # 3. Разбиваем на слова по пробелам
    words = clean.split()

    # 4. Убираем повторы и сортируем по алфавиту
    unique_words = sorted(set(words))

    # 5. Считаем длину каждого слова
    lengths = []
    for word in unique_words:
        lengths.append(len(word))

    # 6. Собираем Series: значения — длины, индексы — слова
    return pd.Series(lengths, index=unique_words, dtype='int64')