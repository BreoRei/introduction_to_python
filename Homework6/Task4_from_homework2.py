# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных индексах. Индексы вводятся одной строкой, через пробел.
# n = 3
# [-3, -2, -1, 0, 1, 2, 3]
# --> 0 2 3
# -3 * -1 * 0 = 0
# Вывод: 0
from functools import reduce


def get_number() -> list[int]:
    while True:
        entered_number: str = input('Введите целое положительное число: ')
        if entered_number.isdigit():
            return [i for i in range(-int(entered_number), int(entered_number)+1)]
        print('Ошибка! Вы ввели не число!')


def get_index():
    while True:
        list_iterable: list[int] = get_number()
        index_list: list[int] = list(map(int, input('Введите индексы одной строкой, через пробел: ').split()))
        if len(list_iterable)-1 >= max(index_list):
            return list_iterable, index_list
        print('Ошибка! Вы ввели не верный индекс!')


def get_index_multiplication():
    list_iterable, index_list = get_index()
    value = reduce(lambda x, y: x * y, [list_iterable[i] for i in range(len(list_iterable)) if i in index_list])
    return index_list, list_iterable, value


finish_list = get_index_multiplication()
print(f'\nПроизведение индексов {finish_list[0]} в списке {finish_list[1]}\nВывод: {finish_list[2]}')
