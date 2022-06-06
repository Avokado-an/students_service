from entity.specialty import Specialty


class StudentFilter:
    average_mark = 0
    subject = Specialty.none

    def __init__(self, average_mark, subject):
        self.average_mark = average_mark
        self.subject = subject
