def record_processing(inner_list: [str]) -> list[dict[str, str]]:
    item: int = 0
    list_data: list[dict[str, str]] = []
    while True:
        if len(inner_list[0 + item:3 + item])-1 != 0:
            one_entry: str = inner_list[0 + item:3 + item]
            final_record: dict[str, str] = {'first_name': one_entry[0], 'last_name': one_entry[1], 'telephon': one_entry[2]}
            list_data.append(final_record)
            item += 3
        else:
            break
    return list_data
