from view import get_string, get_telephone, printing, interface, contact_added
from data_base import write_data, read_data
from funcs import record_processing


def click():
    value = interface()
    if '1' == value:
        first_name = get_string('first_name')
        last_name = get_string('last_name')
        telephone = get_telephone()
        write_data(first_name, last_name, telephone)
        contact_added()
    elif '2' == value:
        pass
    elif '3' == value:
        pass
    elif '4' == value:
        printing(record_processing(read_data()))















