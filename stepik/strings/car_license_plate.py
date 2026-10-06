# На вход программе подаётся одна строка – сгенерированный ИИ автомобильный номер.
# Программа должна вывести 'YES' или 'NO' взависимости от того корректно ли написан номер.

# Поступает переменная с автомобильным номером от ИИ
s = input()
letters = 'АВЕКМНОРСТУХ'

if len(s) == 9 or len(s) == 10:
    first_letter, two_letter, three_letter = s[0], s[4], s[5]
    first_number, two_number, three_number = s[1], s[2], s[3]
    underscore, region = s[6], s[7:]

    # Проверяем, что в нужном месте, где должна быть буква, стоит буква из набора,
    # а где должна быть цифра, стоит цифра
    if first_letter in letters and two_letter in letters and three_letter in letters:
        if first_number.isdigit() == True and two_number.isdigit() == True and three_number.isdigit() == True:
            if underscore == '_' and region.isdigit() == True:
                print('YES')
            else:
                print('NO')
        else:
            print('NO')
    else:
        print('NO')
else:
    print('NO')