import csv

file_path = r'phonebook.txt'


def write_csv(first_name, last_name, telephone) -> None:
    with open(file_path, 'a', newline='') as csvfile:
        csv.writer(csvfile).writerow([first_name, last_name, telephone])


def write_data(first_name, last_name, telephone) -> None:
    with open(file_path, 'a') as f:
        instance = f"{first_name}\n{last_name}\n{telephone}\n"
        f.write(instance)


def read_data() -> list[list[str]]:
    with open(file_path, 'r') as f:
        list_string: list[list[str]] = [i.split(',') for i in f.read().split('\n') if i]
        return list_string
