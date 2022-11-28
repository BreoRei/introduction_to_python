# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
# Пример: Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44} Сумма 9.06

def get_number():
    while True:
        is_number = input('Введите целое положительное число: ')
        if is_number.isdigit():
            return is_number
        print('Ошибка! Вы ввели не число!')


list_number = [round((1 + 1/i)**i, 2) for i in range(1, int(get_number()) + 1)]
print(sum(list_number))
