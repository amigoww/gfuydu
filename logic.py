import random
from decouple import config
def game():
    attempts = int(config('ATTEMPTS'))
    diapazone = int(config('NUMBERS_DIAPAZONE'))
    start_capital = int(config('START_CAPITAL'))
    for i in range(attempts):
        attempts -= 1
        print(f'Ваш баланс: {start_capital}')
        bet = int(input('Введите ставку'))
        if bet > start_capital:
            print('Не достаточно средств')
            continue
        elif bet < start_capital:
            print('Не хитри')
            continue
        number = random.randint(1, diapazone)
        guess_number = int(input(f'Угадайте число от одного до {diapazone}'))
        if guess_number > diapazone or guess_number < 1:
            print('Введите нормальное число')
            continue
        elif guess_number == number:
            capital = bet * 2
            start_capital += capital - bet
            print(f'Вы выиграли {capital}, ваш баланс {start_capital}' )
        else:
            start_capital -= bet
            print(f'Вы не угадали, вы потеряли {bet}')
        if start_capital <= 0:
            print('Вы проиграли все')
            break
    print(f'Игра окончена, ваш баланс {start_capital}')