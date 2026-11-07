# Задача: написать функцию print_perm_time_call(msc_time), которая принимает
# московское время "hh:mm" и печатает пермское время (на 2 часа больше)
# в формате "Созвон будет в HH:MM."

# объявление функции
def print_perm_time_call(msc_time):
    parts = msc_time.split(':')      # делим "08:30" на ['08', '30']
    hours = int(parts[0])            # часы как число: 8
    minutes = parts[1]               # минуты оставляем строкой: '30'

    hours = hours + 2                # Пермь опережает Москву на 2 часа

    hours_text = str(hours)
    # если час однозначный (например, 9), добавляем ведущий ноль: '09'
    if hours < 10:
        hours_text = '0' + hours_text

    print('Созвон будет в ' + hours_text + ':' + minutes + '.')

# считываем данные
msc_time = input()

# вызываем функцию
print_perm_time_call(msc_time)