from view import get_string, get_telephone, printing, interface, contact_added, directory_printing
from data_base import write_data, read_data, write_csv
from funcs import record_processing


def click() -> None:
    value: str = interface()
    if '1' == value:
        first_name: str = get_string('first_name')
        last_name: str = get_string('last_name')
        telephone: int = get_telephone()
        write_csv(first_name, last_name, telephone)
        contact_added()
    elif '2' == value:
        pass
    elif '3' == value:
        pass
    elif '4' == value:
        printing(directory_printing(read_data()))















