# Список задач, который будет пополняться человеком
tasks = []


# Показывает меню и ВОЗВРАЩАЕТ номер, который выбрал человек
def ask_menu_choice():
    print()
    print('1. Добавить')
    print('2. Показать всё')
    print('3. Удалить')
    print('4. Выход')
    try:
        choice = int(input('Выбери раздел: '))
        return choice
    except ValueError:
        pass


# Выводит задачи с номерами
def print_tasks():
    for number, task in enumerate(tasks, 1):
        print(str(number) + '. ' + task)


# Раздел "Добавить"
def add_task():
    tasks.append(input('Что ты хочешь добавить в список дел? '))


# Раздел "Показать всё"
def show_tasks():
    if len(tasks) == 0:
        print('Список пуст')
    else:
        print('Твой список дел:')
        print_tasks()


# Раздел "Удалить"
def delete_task():
    # Если удалять нечего, сразу выходим из функции
    if len(tasks) == 0:
        print('Список пуст, удалять нечего')
        return

    print('Вот ваш список на данный момент: ')
    print_tasks()

    # Спрашиваем номер, пока человек не введёт правильный
    while True:
        try:
            number_to_delete = int(input('Выбери номер пункта, который ты хочешь удалить: '))
            if 1 <= number_to_delete <= len(tasks):
                del tasks[number_to_delete - 1]
                break
            else:
                print('Такого номера нет в списке. Попробуй ещё раз')
        except ValueError:
            print('Нужно ввести номер цифрой, а не букву. Попробуй ещё раз')


# Главный цикл: он решает, что делать с выбранным пунктом
def main():
    while True:
        choice = ask_menu_choice()
        if choice == 1:
            add_task()
        elif choice == 2:
            show_tasks()
        elif choice == 3:
            delete_task()
        elif choice == 4:
            print('До свидания!')
            break
        else:
            print('Выбери пункт от 1 до 4')


if __name__ == '__main__':
    main()