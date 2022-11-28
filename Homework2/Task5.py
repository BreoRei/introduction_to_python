# Реализуйте алгоритм перемешивания списка.

from random import shuffle, choice

# Вариант 1:
# entered_list = input('Введите элементы списка одной строкой, через пробел: ').split()
# shuffle(entered_list)
# print(entered_list)

# --------------------------------------------------

# Вариант 2:
entered_list = input('Введите элементы списка одной строкой, через пробел: ').split()


def get_jumbled_list(entered_list):
    jumbled_list = []
    while True:
        if len(entered_list) > 0:
            value = choice(entered_list)
            jumbled_list.append(entered_list.pop((entered_list.index(value))))
        else:
            return jumbled_list


print(get_jumbled_list(entered_list))

