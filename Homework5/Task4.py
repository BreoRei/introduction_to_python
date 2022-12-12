# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.


def repetition_coding(string: str) -> str:
    char: str = string[0]
    count: int | str = 1
    final_string: str = ''
    for i in range(1, len(string)):
        if string[i] == char:
            count += 1
        else:
            if char != string[i]:
                if (count == 1 and len(final_string) > 0) and (
                        not final_string[len(final_string) - 2:-1].isdigit()
                        or final_string[len(final_string) - 2:-1] == '1'):
                    count = ''
            final_string += str(count) + char
            count = 1
            char = string[i]
    final_string += str(count) + char
    return final_string


def recovery(string: str) -> str:
    count: int = 1
    final_string: str = ''
    for char in string:
        if char.isdigit():
            count = int(char)
        else:
            final_string += (char * count)
    return final_string


file_path = r'text.txt'

try:
    with open(file_path, 'r') as f:
        text = f.read()
        if text[0].isdigit():
            text = recovery(text)
            with open(file_path, 'w') as file:
                file.write(text)
        else:
            text = repetition_coding(text)
            with open(file_path, 'w') as file:
                file.write(text)
except FileNotFoundError:
    with open(file_path, 'w') as f:
        f.write(input('Введите строку для шифровки или дешифровки -> '))
