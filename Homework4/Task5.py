# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл,
# содержащий сумму многочленов (складываются числа, у которых "х" в одинаковых степенях).

file_path_one = r'polynomial_formula_one.txt'
file_path_two = r'polynomial_formula_two.txt'
file_path_three = r'general_formula_of_two_files.txt'


def data_formatting(inner_list: list[str]) -> dict[str, int]:
    inner_list = list(map(lambda x: x.strip(), inner_list[:-2:2]))
    inner_list = [item.split('*') for item in inner_list]
    inner_tuple: dict[str, int] = {}
    for item in inner_list:
        if len(item) == 2:
            inner_tuple[item[1]] = int(item[0])
        else:
            try:
                if int(item[0]):
                    inner_tuple['0'] = int(item[0])
            except ValueError:
                inner_tuple[item[0]] = 0
    return inner_tuple


def summing_the_same_key_values(tuple_one: dict[str, int], tuple_two: dict[str, int]) -> str:
    if len(tuple_one) >= len(tuple_two):
        big_dict = tuple_one
        small_dict = tuple_two
    else:
        big_dict = tuple_two
        small_dict = tuple_one
    text: str = ''
    for i, j in big_dict.items():
        if small_dict.get(i) is None:
            text += f'{j}*{i} + '
        elif i == '0':
            text += f'{j + small_dict[i]} = 0'
        else:
            text += f'{j + small_dict[i]}*{i} + '
    return text


with open(file_path_three, 'w+') as f3:
    with open(file_path_one, 'r') as f1:
        values_from_file_one: list[str] = f1.read().split()
        file_one: dict[str, int] = data_formatting(values_from_file_one)
    with open(file_path_two, 'r') as f2:
        values_from_file_two: list[str] = f2.read().split()
        file_two: dict[str, int] = data_formatting(values_from_file_two)
    f3.write(summing_the_same_key_values(file_one, file_two))



