# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
from random import randint

candies: int = 2021


def game_selection(cand) -> str:
    while True:
        try:
            players: int = int(input(f"Игра с компьютером ----> 1\n"
                                     "Игра с другом ---------> 2\n"
                                     "Введите 1 или 2--------> "))
            if players == 1 or players == 2:
                print(f'На столе лежит {cand} конфета, каждый игрок берёт от 1 до 28 конфет.\n'
                      f'Забирает все конфеты тот кто сделает последний ход!\n')
                return "pve" if players == 1 else "pvp"
            else:
                print("Для игры нужно выбрать!!!")
        except ValueError:
            print("Нужны цифры 1 или 2!!!")


def lottery(name) -> int:
    one = 'Player 1'
    two = 'Player 2'
    if name == 'pve':
        two = 'Компьютер'
    print(f'Жеребьевка.')
    pl_one = randint(1, 10)
    print(f'{one} выбросил {pl_one}')
    pl_two = randint(1, 10)
    print(f'{two} выбросил {pl_two}')
    return 1 if pl_one > pl_two else 2


def moves(cand: int, player: int, game: str) -> tuple[int, int]:
    if game == "pvp":
        cand -= number_entry(cand)
    else:
        if player == 1:
            cand -= number_entry(cand)
        else:
            cand -= virtual_player(cand)
    print(f'Всего осталось {cand} конфет.')
    player = 2 if player == 1 else 1
    return cand, player


def number_entry(cand: int) -> int:
    while True:
        try:
            num: int = int(input(f'Введите число от 1 до {28 if cand > 28 else cand} --> '))
            if num <= cand:
                if 0 < num < 29:
                    break
                else:
                    print('Число не подходит!')
            else:
                print(f'Конфет осталось {cand}!')
        except ValueError:
            print('Вы ввели не число!')
    return num


def virtual_player(cand: int) -> int:
    max_number: int = 28
    if cand <= max_number:
        num = cand
    elif cand % 28 == 0:
        num = 28 - 1
    elif cand % 28 == 1:
        if (cand // 28) % 2 == 1:
            num = 28 - 1
        else:
            num = 28
    else:
        num = cand % 28 - 1
    print(f'Он взял {num}!')
    return num


def candy_game(game: str, cand: int) -> int:
    player: int = lottery(game)
    if game == "pve" and player == 2:
        print(f'Первым начинает Compi\n')
    else:
        print(f'Первым начинает Player {player}\n')
    while True:
        if cand > 0:
            if game == "pve" and player == 2:
                print('Ходит компьютер!')
                cand, player = moves(cand, player, game)
            else:
                print(f'Ходит Player {player}')
                cand, player = moves(cand, player, game)
        else:
            player = 2 if player == 1 else 1
            print(f'Игра закончилась: '
                  f'{"победил Компьютер" if game == "pve" and player == 2 else f"победил игрок {player}"}!')
            return player


candy_game(game_selection(candies), candies)
