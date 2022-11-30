# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


def decorator(func):

    def wrapper(*args):
        print(f'Начало решения!\n{"-"*45}')
        func(*args)
        print(f'{"-"*45}\nОкончание решения!')

    return wrapper


while True:
    try:
        num: int = int(input('Введите число: '))
        break
    except ValueError:
        print(f'Это не число.')


def convert_to_binary(number: int) -> int:
    binary: str = ''
    while True:
        if number > 1:
            binary = str(number % 2) + binary
            number = int(number/2)
        if number == 1:
            binary = str(number) + binary
            return int(binary)


@decorator
def prints_text(n, func):
    print(f'Число в десятичной системе счисления: \t{n}\nЧисло в двоичной системе счисления: \t{func}')


prints_text(num, convert_to_binary(num))
