# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

def value_input() -> int:
    while True:
        try:
            num: int = int(input('Введите число: '))
            return num
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

    print(f'Список простых множителей числа: {inner_list}')


def search_for_simple_plurals(num: int) -> list[int]:
    list_of_prime_factors: list[int] = []
    i: int = 2
    while num > 1:
        if num % i == 0:
            list_of_prime_factors.append(i)
            num //= i
        else:
            i += 1

    return list_of_prime_factors


text_printing(search_for_simple_plurals(value_input()))


