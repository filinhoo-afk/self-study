# Задача: консольный трекер задач с меню (добавить, показать, удалить, выход).
# Выход из программы делает цикл, а не функция, потому что break работает только внутри цикла.

# Список задач, который будет пополняться человеком
list_tracker = []

# Меню: показывает пункты и ВОЗВРАЩАЕТ номер, который выбрал человек
def menu():
    print('1. Добавить')
    print('2. Показать всё')
    print('3. Удалить')
    print('4. Выход')
    choose = int(input('Выбери раздел: '))
    return choose

# Раздел "Добавить"
def add_list():
    list_tracker.append(input('Что ты хочешь добавить в список дел? '))

# Раздел "Показать все"
def show_everything():
    print(list_tracker)

# Раздел "Удалить"
def delete_list():
    print('Вот ваш список на данный момент: ')
    print(list_tracker)
    choose_delate = int(input('Выбери номер пункта , который ты хочешь удалить: '))
    del list_tracker[choose_delate - 1]
    
# Главный цикл: он решает, что делать с выбранным пунктом
while True:
    choice = menu()
    if choice == 1:
        add_list()
    elif choice == 2:
        show_everything()
    elif choice == 3:
        delete_list()
    elif choice == 4:
        print('До свидания!')
        break
    else:
        print('Выбери пункт от 1 до 4')