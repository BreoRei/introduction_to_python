file_path = r'phonebook.txt'


def write_data(first_name, last_name, telephone) -> None:
    with open(file_path, 'a') as f:
        instance = f"{first_name}\n{last_name}\n{telephone}\n"
        f.write(instance)


def read_data() -> list[str]:
    with open(file_path, 'r') as f:
        list_string: list[str] = f.read().split('\n')
        return list_string
