from prettytable import PrettyTable


def get_string(value) -> str:
    if value == 'first_name':
        return input(f'Введите имя -> ').capitalize()
    elif value == 'last_name':
        return input(f'Введите фамилию -> ').capitalize()


def get_telephone() -> int:
    while True:
        try:
            telephone = int(input(f'Введите телефон без пробелов -> '))
            return telephone
        except ValueError:
            print('Ошибка ввода. Не номер.')


def contact_added() -> None:
    print('Контакт добавлен в справочник.')


def contact_deleted() -> None:
    print('Контакт удален из справочника.')


def printing(pretty_table) -> None:
    print(pretty_table)


def interface() -> str:
    while True:
        print('Работа со справочником!\n'
              'Для записи контакта "1"\n'
              'Для поиска контакта "2"\n'
              'Для удаление контакта "3"\n'
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


def search_input() -> str:
    value = input('Введите имя, фамилию или телефон -> ')
    if value.isdigit():
        return value.replace(' ', '')
    else:
        return value.capitalize()


def request_for_deletion() -> str:
    return input('Для удаления записи введите ------> y\n'
                 'Чтобы пропустить нажмите "Enter" -> ').lower()


def delete_all_entries():
    return input('Для удаленпия всех записей --------> y\n'
                 'Для отмены нажмите "Enter" --------> ').lower()


def no_contact() -> None:
    print('Такого контакта нет.')


def menu_operation() -> str:
    return input('Введите любую букву чтобы продолжить работу! \n'
                 'Нажмите "Enter" для выхода из программы ---> ')
