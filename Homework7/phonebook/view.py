def get_string(value):
    if value == 'first_name':
        return input(f'Введите имя -> ')
    elif value == 'last_name':
        return input(f'Введите фамилию -> ')


def get_telephone():
    while True:
        try:
            telephone = int(input(f'Введите телефон без пробелов -> '))
            return telephone
        except ValueError:
            print('Ошибка ввода. Не номер.')


def contact_added():
    print('Запись добавлена в справочник.')


def printing(text):
    [print(i) for i in text]  # [[print(j) for j in i.items()] for i in text]


def interface() -> str:
    while True:
        print('Работа со справочником!\n'
              'Для записи контакта "1"\n'
              'Для поиска контакта "2"\n'
              'Для правки контакта "3"\n'
              'Вывести все записи  "4"')
        num = input('Введите цифру меню -> ')
        if num in ("1", "2", "3", "4"):
            return num

