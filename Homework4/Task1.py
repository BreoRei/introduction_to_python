# Вычислить число ПИ c заданной точностью d
# Пример:- при d = 0.001, π = 3.141
from math import pi


def value_input() -> int:
    while True:
        try:
            accuracy_pi: str = input('Введите точность для числа ПИ, пример(0.01, 0.001 и т.д.): ')
            float(accuracy_pi)
            accuracy_pi: int = len(accuracy_pi)-2
            return accuracy_pi
        except ValueError:
            print(f'Это не число.')


def decorator(func):

    def wrapper(*args):
        print(f'Начало решения!\n{"-"*45}')
        func(*args)
        print(f'{"-"*45}\nОкончание решения!')
    return wrapper


@decorator
def text_printing(num_pi: float):
    print(f'Число ПИ с заданной точностью: {num_pi}')


def generation_of_pi_number_precision(acc_pi: int) -> float:
    num_pi: float = round(pi, acc_pi)
    return num_pi


text_printing(generation_of_pi_number_precision(value_input()))











