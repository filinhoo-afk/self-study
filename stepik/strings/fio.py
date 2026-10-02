# На вход программе подаются три строки: имя, фамилия и отчество (именно в таком порядке). Написать программу, которая выводит инициалы человека.

name, lastname, patronymic = input(), input(), input()
print(lastname[0], name[0], patronymic[0], sep='')