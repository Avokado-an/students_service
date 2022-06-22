from validator.student_validator import isint, isfloat, is_valid_specialty, is_valid_subject, is_valid_mark


def input_specialty():
    specialty = input("specialty - ")
    while not is_valid_specialty(specialty):
        specialty = input("specialty - ")
    return specialty


def input_subject():
    subject = str(input("subject - "))
    while not is_valid_subject(subject):
        subject = input("subject - ")
    return subject


def input_mark():
    mark_string = input_float("average mark")
    if not is_valid_mark(mark_string):
        print("average mark should be positive number smaller than 10")
        return input_mark()
    return float(mark_string)


def input_float(field_name):
    number = input(f"{field_name} - ")
    while not isfloat(number):
        print("input a floating point number")
        number = input(f"{field_name} - ")
    return float(number)


def input_int(field_name):
    number = input(f"{field_name} - ")
    while not isint(number):
        print("input a number")
        number = input(f"{field_name} - ")
    return int(number)
