

def contact_search(contact_list: list[list[str]], value: str) -> list[list[str]]:
    inner_list: list = []
    for contact in contact_list:
        if value.isdigit():
            if contact[2] == value:
                inner_list.append(contact)
                break
        elif contact[0] == value or contact[1] == value:
            inner_list.append(contact)
    return inner_list


def deleting_contact(contact_list: list[list[str]], cont_del_list: list[list[str]]) -> list[list[str]]:
    for contact in cont_del_list:
        if contact in contact_list:
            contact_list.remove(contact)
    return contact_list




