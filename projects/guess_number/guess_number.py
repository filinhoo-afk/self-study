import random


def ask_yes_no(prompt):
    while True:
        answer = input(prompt).strip().lower()

        if answer in ('y', 'n'):
            return answer
        print('Ошибка! Введи Y или N.')


def choose_difficulty():
    print('\nВыбери уровень сложности:')
    print('1 — Лёгкий (0–50, 10 попыток)')
    print('2 — Средний (0–100, 7 попыток)')
    print('3 — Сложный (0–200, 8 попыток)')

    while True:
        choice = input('Твой выбор: ').strip()

        if choice == '1':
            return 50, 10
        elif choice == '2':
            return 100, 7
        elif choice == '3':
            return 200, 8

        print('Ошибка! Выбери 1, 2 или 3.')


def read_guess(max_number):
    while True:
        try:
            guess = int(input(
                f'Введи число от 0 до {max_number}: '
            ))
        except ValueError:
            print('Ошибка! Нужно ввести целое число.')
            continue

        if guess < 0 or guess > max_number:
            print(f'Число должно быть от 0 до {max_number}!')
            continue

        return guess


def show_hint(secret_number, guess, max_number):
    difference = abs(secret_number - guess)

    # Пороги зависят от диапазона сложности
    if difference <= max(1, max_number * 0.03):
        print('ОЧЕНЬ ЖАРКО! 🔥')
    elif difference <= max(2, max_number * 0.07):
        print('Горячо! 🔥')
    elif difference <= max(3, max_number * 0.15):
        print('Тепло! 🌡️')
    else:
        print('Холодно! ❄️')

    if guess < secret_number:
        print('Загаданное число БОЛЬШЕ ↑')
    else:
        print('Загаданное число МЕНЬШЕ ↓')


def play_game(max_number, max_attempts):
    secret_number = random.randint(0, max_number)
    attempts = 0

    print(f'\nЯ загадал число от 0 до {max_number}!')
    print(f'У тебя {max_attempts} попыток.')

    while attempts < max_attempts:
        guess = read_guess(max_number)
        attempts += 1

        if guess == secret_number:
            print(f'\n🎉 Ты угадал число {secret_number}!')
            print(f'Количество попыток: {attempts}')
            return

        show_hint(secret_number, guess, max_number)
        print(f'Осталось попыток: {max_attempts - attempts}')

    print(f'\nПопытки закончились! Число было: {secret_number}')


def main():
    print('Привет! Добро пожаловать в игру «Угадай число»!')

    if ask_yes_no('Хочешь сыграть? Y/N: ') == 'n':
        print('Хорошо! Приходи в другой раз.')
        return

    while True:
        max_number, max_attempts = choose_difficulty()
        play_game(max_number, max_attempts)

        if ask_yes_no('\nХочешь сыграть ещё? Y/N: ') == 'n':
            print('Спасибо за игру! До встречи!')
            break


if __name__ == '__main__':
    main()