# Условие: даны 4 слова (по одному на строке).
# Берём самую "маленькую" и самую "большую" строки (по сравнению строк),
# перемножаем Unicode-коды их последних символов и возводим результат в квадрат.

words = [input() for _ in range(4)]

smallest = min(words)
largest = max(words)

result = (ord(smallest[-1]) * ord(largest[-1])) ** 2
print(result)