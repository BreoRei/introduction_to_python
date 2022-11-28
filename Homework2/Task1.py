# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример: 0,56 -> 11

real_number = input('Введите вещественное число--> ')
split_by_comma = real_number.split(sep=",")
sum = 0

for item in split_by_comma:
    for i in item:
        sum += int(i)
print(f'Сумма цифр вещественного числа {real_number} = {sum}')

