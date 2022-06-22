def display_set_with_field_name(set_of_values, field_name):
    print(f"available {field_name} are: {output_set_as_string(set_of_values)} \n")


def output_set_as_string(values_set):
    set_string = ""
    for value in values_set:
        set_string += str(value) + ", "
    set_string = set_string[:len(set_string) - 2]
    return set_string
