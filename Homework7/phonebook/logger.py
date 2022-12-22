import csv
from datetime import datetime

file_path = r'program_logs.txt'

dict_actions = {'1': 'запись', '2': 'поиск', '3': 'удаление', '4': 'печать'}


def logger(action: str, contact: list[str]):
    with open(file_path, 'a', newline='') as csvfile:
        present_time = datetime.now()
        data_time = datetime.strftime(present_time, "%d.%m.%Y %H:%M")
        csv.writer(csvfile).writerow([data_time, dict_actions[action], *contact])
