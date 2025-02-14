def remove_duplicates(input_list):
    unique = []
    for item in input_list:
        if item not in unique:
            unique.append(item)
    return unique
