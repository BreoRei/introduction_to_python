# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
# Пример: -[1.1, 1.2, 3.1, 10.01] #=> 0.19


while True:
    try:
        entered_list: list[float] = list(map(float, input('Введите дробные числа через пробел: ').split()))
        break
    except ValueError:
        print(f'Это не число.')


def decorator(func):

    def wrapper(*args):
        print(f'Начало решения!\n{"-"*45}')
        func(*args)
        print(f'{"-"*45}\nОкончание решения!')

    return wrapper


def difference_in_max_and_min_denominators(arg_list: list[float]) -> (float, float, float):
    for index in range(len(arg_list)):
        numerator, denominator = str(arg_list[index]).split(sep='.')
        arg_list[index] = float('.'.join(('0', denominator)))
        float_max: float = max(arg_list)
        float_min: float = min(arg_list)
    total: float = max(arg_list) - min(arg_list)
    return float_min, float_max, total


@decorator
def prints_text(func):
    print(f'Разница между |max->{func[1]}|-|min->{func[0]}| = {func[2]}')


prints_text(difference_in_max_and_min_denominators(entered_list))
