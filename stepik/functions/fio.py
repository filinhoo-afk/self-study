# Напишите функцию print_fio(name, surname, patronymic), которая принимает три параметра:
# name, surname, patronymic , а затем выводит на печать ФИО человека


# объявление функции
def print_fio(name, surname, patronymic):
    fio = surname[0].upper() + name[0].upper() + patronymic[0].upper()
    print(fio)

# считываем данные
name, surname, patronymic = input(), input(), input()

# вызываем функцию
print_fio(name, surname, patronymic)



