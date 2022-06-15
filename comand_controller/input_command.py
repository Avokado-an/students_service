from abc import ABCMeta, abstractmethod

from entity.filter import StudentFilter
from entity.specialty import Specialty
from entity.student import Student


class Command:
    def __init__(self):
        pass

    @abstractmethod
    def input(self):
        "The required execute method that all command objects will use"


class AddCommandInput(Command):
    def input(self):
        name = input("name - ")
        surname = input("surname - ")
        specialty = input_specialty()
        average_mark = input_mark()
        return Student(0, name, surname, specialty, average_mark)

    def __init__(self):
        Command.__init__(self)


class DeleteCommandInput(Command):
    def input(self):
        student_id = input_int("student id")
        return student_id

    def __init__(self):
        Command.__init__(self)


class ReviewCommandInput(Command):
    def input(self):
        pass

    def __init__(self):
        Command.__init__(self)


class FilterCommandInput(Command):
    def input(self):
        subject = input_subject()
        average_mark = input_mark()
        return StudentFilter(average_mark, subject)

    def __init__(self):
        Command.__init__(self)


def input_subject():
    subject = str(input("subject - "))
    subjects = retrieve_all_subjects()
    while subject not in subjects:
        print(f"available subjects are: {output_set_as_string(subjects)}\n")
        subject = input("subject - ")
    return subject


def input_specialty():
    specialty = str(input("specialty - "))
    specialties = retrieve_all_specialties()
    while specialty not in specialties:
        print(f"available specialties are: {output_set_as_string(specialties)} \n")
        specialty = str(input("specialty - "))
    return specialty


def output_set_as_string(values_set):
    set_string = ""
    for value in values_set:
        set_string += str(value) + ", "
    set_string = set_string[:len(set_string) - 2]
    return set_string


def retrieve_all_subjects():
    subjects = []
    for specialty in Specialty:
        for subject in specialty.value:
            subjects.append(subject)
    return set(subjects)


def retrieve_all_specialties():
    specialties = []
    for specialty in Specialty:
        specialties.append(specialty.name)
    return set(specialties)


def input_mark():
    mark_string = input_float("average mark")
    if not 10. > float(mark_string) > 0.:
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


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def isint(num):
    try:
        int(num)
        return True
    except ValueError:
        return False
