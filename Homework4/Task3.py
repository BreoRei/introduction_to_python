# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся
# элементов исходной последовательности.
# Ввод: [1, 1, 2, 3, 4, 4, 4]
# Вывод: [2, 3]

from collections import Counter


def value_input() -> list[int]:
    while True:
        try:
            value: list[int] = list(map(int, (input('Введите последовательность чисел через пробел: ').split())))
            return value
        except ValueError:
            print(f'Это не число.')


def decorator(func):

    def wrapper(*args):
        print(f'Начало решения!\n{"-"*45}')
        func(*args)
        print(f'{"-"*45}\nОкончание решения!')
    return wrapper


@decorator
def text_printing(inner_list: list[int]):
    print(f'Список неповторяющихся элементов исходной последовательности: {inner_list}')


def search_for_non_repeating_elements(inner_list: list[int]) -> list[int]:
    number_of_identical_elements: dict[int, int] = Counter(inner_list)
    elements_that_occur_once: list[int] = []
    for key, value in number_of_identical_elements.items():
        if value == 1:
            elements_that_occur_once.append(key)
    return elements_that_occur_once


text_printing(search_for_non_repeating_elements(value_input()))

