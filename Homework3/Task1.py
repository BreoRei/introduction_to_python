# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной идексах.
# Пример: [2, 3, 5, 9, 3] #-> на нечётных идексах элементы 3 и 9, ответ: 12

while True:
    try:
        entered_list: list[int] = list(map(int, input('Введите числа через пробел: ').split()))
        break
    except ValueError:
        print('Это не число.')


def decorator(func):

    def wrapper(*args):
        print(f'Начало решения!\n{"-"*45}')
        func(*args)
        print(f'{"-"*45}\nОкончание решения!')

    return wrapper


@decorator
def prints_text(func):
    print(f'Сумма элементов нечётных индексов = {func}')
# ___________________________________________________________
# Вариант 1:


def sum_of_elements_in_odd_positions_1(search_list: list[int]) -> int:
    sum_: int = 0
    for item in range(len(search_list)):
        if item % 2 == 1:
            sum_ += search_list[item]
    return sum_
# ____________________________________________________________
# Вариант 2:


def sum_of_elements_in_odd_positions_2(inner_list: list[int]):
    sum_ = sum(inner_list[1::2])
    return sum_
# ____________________________________________________________


print('Вариант 1:')
prints_text(sum_of_elements_in_odd_positions_1(entered_list))
print('\nВариант 2:')
prints_text(sum_of_elements_in_odd_positions_1(entered_list))
