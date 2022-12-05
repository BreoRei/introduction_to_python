# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# - k=4 => 8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0 или 8*(x**4) + 5*x + 4 = 0 и т.д.
from random import randint

file_path_one = r'polynomial_formula_one.txt'
file_path_two = r'polynomial_formula_two.txt'


def value_input() -> int:
    while True:
        try:
            value: int = int(input('Введите степень многочлена: '))
            return value
        except ValueError:
            print(f'Это не число.')


def write_the_formula_for_the_degree_polynomial(polynomial_degree: int) -> str:
    text: str = ''
    for i in range(polynomial_degree):
        number: int = randint(0, 100)
        if polynomial_degree - i == 1:
            if number > 1:
                text += f'{number}*x + '
            else:
                text = f'x + '
        elif number > 1:
            text += f'{number}*x^{polynomial_degree-i} + '
        else:
            text += f'x^{polynomial_degree-i} + '
    num: int = randint(0, 100)
    if num > 0:
        text += f'{num} '
    else:
        text = text[:-2]
    text += '= 0'
    return text


with open(file_path_one, 'w+') as f1:
    f1.writelines(write_the_formula_for_the_degree_polynomial(value_input()))

with open(file_path_two, 'w+') as f2:
    f2.writelines(write_the_formula_for_the_degree_polynomial(value_input()))
