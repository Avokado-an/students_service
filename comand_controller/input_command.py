from abc import abstractmethod

from entity.filter import StudentFilter
from entity.student import Student
from util.input_util import input_mark, input_subject, input_int, input_specialty


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
