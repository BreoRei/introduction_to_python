from prettytable import PrettyTable


def get_string(value) -> str:
    if value == 'first_name':
        return input(f'Введите имя -> ')
    elif value == 'last_name':
        return input(f'Введите фамилию -> ')


def get_telephone() -> int:
    while True:
        try:
            telephone = int(input(f'Введите телефон без пробелов -> '))
            return telephone
        except ValueError:
            print('Ошибка ввода. Не номер.')


def contact_added() -> None:
    print('Запись добавлена в справочник.')


def printing(pretty_table) -> None:
    print(pretty_table)


def interface() -> str:
    while True:
        print('Работа со справочником!\n'
              'Для записи контакта "1"\n'
              'Для поиска контакта "2"\n'
              'Для правки контакта "3"\n'
              'Вывести все записи  "4"')
        num: str = input('Введите цифру меню -> ')
        if num in ("1", "2", "3", "4"):
            return num
        else:
            print('Ошибка. Такого номера в меню нет.')


def directory_printing(inner_list: list[list[str]]) -> PrettyTable:
    directory = PrettyTable()
    directory.field_names = ["Имя", "Фамилия", "Номер телефона"]
    directory.add_rows(inner_list)
    return directory

