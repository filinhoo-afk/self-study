# Дано натуральное n. Найти все моменты времени hh:mm (часы 0–23, минуты 0–59),
# для которых h в степени n равно m. Вывести их по возрастанию в формате hh:mm.

n = int(input())

for h in range(24):
    for m in range(60):
        if h ** n == m:
            if h < 10:
                hh = '0' + str(h)
            else:
                hh = str(h)
            if m < 10:
                mm = '0' + str(m)
            else:
                mm = str(m)
            print(hh + ':' + mm)