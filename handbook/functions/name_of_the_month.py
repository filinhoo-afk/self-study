# Напишите функцию month(number, language), которая принимает номер месяца
# number (от 1 до 12) и язык интерфейса language ("ru" или "en") и возвращает
# название соответствующего месяца на нужном языке с заглавной буквы.
# В решении должны быть только функции, без вызовов требуемых функций.

def month(number, language):
    months_ru = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
                 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
    months_en = ['January', 'February', 'March', 'April', 'May', 'June',
                 'July', 'August', 'September', 'October', 'November', 'December']
    if language == 'ru':
        return months_ru[number - 1]
    else:
        return months_en[number - 1]
