from view import get_string, get_telephone, printing, interface, contact_added, directory_printing, \
    search_input, request_for_deletion, contact_deleted, delete_all_entries, no_contact, menu_operation
from data_base import is_there_file, read_data, write_csv, rewrite_csv
from funcs import contact_search, deleting_contact
from logger import logger


def click() -> None:
    check = ''
    is_there_file()
    contact_list = read_data()
    menu = 1
    while menu:
        value: str = interface()
        if '1' == value:
            contact: list[list[str]] = [[get_string('first_name'), get_string('last_name'), get_telephone()]]
            if contact not in contact_list:
                write_csv(contact[0])
                contact_added()
                contact_list = read_data()
                logger(value, *contact)
        elif '2' == value:
            search_inp: str = search_input()
            contact = contact_search(contact_list, search_inp)
            if len(contact) == 0:
                no_contact()
            else:
                printing(directory_printing(contact))
            logger(value, [search_inp])
        elif '3' == value:
            contact = contact_search(contact_list, search_input())
            printing(directory_printing(contact))
            if len(contact) == 1:
                check = request_for_deletion()
            elif len(contact) > 1:
                check = delete_all_entries()
            if check == 'y':
                contact_list = deleting_contact(contact_list, contact)
                rewrite_csv(contact_list)
                printing(directory_printing(contact))
                contact_deleted()
                logger(value, *contact)
        elif '4' == value:
            printing(directory_printing(contact_list))
            logger(value, ['справочника'])
        menu = menu_operation()

