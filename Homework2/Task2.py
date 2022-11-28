# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def get_number():
    while True:
        is_number = input('Введите целое положительное число: ')
        if is_number.isdigit():
            return is_number
        print('Ошибка! Вы ввели не число!')


def product_of_numbers(item):
    multiplication = 1
    for i in range(1, item + 1):
        multiplication *= i
    return multiplication


list_number = [product_of_numbers(i) for i in range(1, int(get_number()) + 1)]
print(f'Набор произведений чисел от 1 до {len(list_number)}: \n{list_number}')
