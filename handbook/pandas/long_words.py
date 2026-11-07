# Задача: функция get_long(data, min_length=5) получает Series
# (индексы — слова, значения — их длины) и возвращает только те элементы,
# у которых длина слова не меньше min_length.

import pandas as pd


def get_long(data, min_length=5):
    # Оставляем только элементы, где значение >= min_length
    return data[data >= min_length]