# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных индексах. Индексы вводятся одной строкой, через пробел.
# n = 3
# [-3, -2, -1, 0, 1, 2, 3]
# --> 0 2 3
# -3 * -1 * 0 = 0
# Вывод: 0

def get_number():
    while True:
        entered_number = input('Введите целое положительное число: ')
        if entered_number.isdigit():
            return int(entered_number)
        print('Ошибка! Вы ввели не число!')


def get_index(number):
    while True:
        entered_index_list = input('Введите ндексы одной строкой, через пробел: ').split()
        index_list = list(map(int, entered_index_list))
        if number*number+1 > max(index_list):
            return index_list
        print('Ошибка! Вы ввели не верный индекс!')


def get_index_multiplication(number, index_list):
    new_list = [i for i in range(-number, number+1)]
    value = 1
    for item in index_list:
        value *= new_list[item]
    return new_list, value


number = get_number()
index_list = get_index(number)
new_list, multiplication = get_index_multiplication(number, index_list)
print(f'\nПроизведение индексов {index_list} в списке index_list {new_list}\nВывод: {multiplication}')

