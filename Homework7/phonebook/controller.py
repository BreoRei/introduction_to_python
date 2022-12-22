from view import get_string, get_telephone, printing, interface, contact_added, directory_printing, \
    search_input, request_for_deletion, contact_deleted, delete_all_entries, no_contact, menu_operation
from data_base import is_there_file, read_data, write_csv, rewrite_csv
from funcs import contact_search, deleting_contact


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
        elif '2' == value:
            contact = contact_search(contact_list, search_input())
            if len(contact) == 0:
                no_contact()
            else:
                printing(directory_printing(contact))
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
        elif '4' == value:
            printing(directory_printing(contact_list))
        menu = menu_operation()

