# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
while True:
    try:
        entered_list: list[int] = list(map(int, input('Введите числа через пробел: ').split()))
        break
    except ValueError:
        print(f'Это не число.')


def decorator(func):

    def wrapper(*args):
        print(f'Начало решения!\n{"-"*45}')
        func(*args)
        print(f'{"-"*45}\nОкончание решения!')

    return wrapper


def product_of_pairs_of_numbers(search_list: list[int]) -> list[int]:
    arg_list: list[int] = []
    odd: bool = False
    if len(search_list) % 2 == 1:
        odd = True
    for item in range(int(len(search_list)/2)+odd):
        arg_list.append(search_list[item]*search_list[-(1+item)])
    return arg_list


@decorator
def prints_text(inner_list: list[int], func: list[int]):
    print(f'Исходный список: {inner_list}\nИтоговый список: {func}')


prints_text(entered_list, product_of_pairs_of_numbers(entered_list))





