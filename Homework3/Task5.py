# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:- для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

while True:
    try:
        num: int = int(input('Введите число: '))
        break
    except ValueError:
        print(f'Это не число.')


def decorator(func):

    def wrapper(*args):
        print(f'Начало решения!\n{"-"*60}')
        func(*args)
        print(f'{"-"*60}\nОкончание решения!')

    return wrapper


@decorator
def prints_text(func1: list[int], func2: list[int]):
    print(f'Негафибоначчи & Фибоначчи:\n{func2 + func1[1:]}')


def fibonacci(number: int):
    inner_list: list[int] = []
    for item in range(number+1):
        match item:
            case 0 | 1:
                inner_list.append(item)
            case _:
                inner_list.append(inner_list[item-2]+inner_list[item-1])
    return inner_list


def negafibonacci(number: int):
    inner_list: list[int] = []
    for item in range(number + 1):
        match item:
            case 0 | 1:
                inner_list.insert(0, item)
            case _:
                inner_list.insert(0, (inner_list[1] - inner_list[0]))
    return inner_list


prints_text(fibonacci(num), negafibonacci(num))
