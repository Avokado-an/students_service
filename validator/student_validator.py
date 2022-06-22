from entity.specialty import Specialty
from util.output_util import display_set_with_field_name


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


def is_valid_mark(num):
    if isfloat(num):
        return 0 <= float(num) <= 10
    return False


def is_valid_specialty(specialty_name):
    specialties = retrieve_all_specialties()
    specialty_exists = specialty_name in specialties
    if specialty_exists:
        return True
    display_set_with_field_name(specialties, "specialties")
    return False


def is_valid_subject(subject):
    subjects = retrieve_all_subjects()
    subject_exists = subject in subjects
    if subject_exists:
        return True
    display_set_with_field_name(subjects, "subjects")
    return False


def retrieve_all_specialties():
    specialties = []
    for specialty in Specialty:
        specialties.append(specialty.name)
    return set(specialties)


def retrieve_all_subjects():
    subjects = []
    for specialty in Specialty:
        for subject in specialty.value:
            subjects.append(subject)
    return set(subjects)
