import csv

file_path = r'phonebook.txt'


def write_csv(contact_list: list[str]) -> None:
    with open(file_path, 'a', newline='') as csvfile:
        csv.writer(csvfile).writerow([contact_list[0], contact_list[1], contact_list[2]])


def is_there_file():
    try:
        with open(file_path, 'a'):
            pass
    except FileNotFoundError:
        with open(file_path, 'w') as csvfile:
            csv.writer(csvfile)


def rewrite_csv(contact_list: list[list[str]]) -> None:
    with open(file_path, 'w'):
        for contact in contact_list:
            write_csv(contact)


def read_data() -> list[list[str]]:
    with open(file_path, 'r') as f:
        list_string: list[list[str]] = [i.split(',') for i in f.read().split('\n') if i]
        return list_string
