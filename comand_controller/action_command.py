from abc import abstractmethod, ABCMeta

from entity.student import Student
from repo.student_repo import add_student
from service.student_service import remove_student, retrieve_students, output_student_info, \
    filter_students_by_mark_and_subjects


class Command:
    def __init__(self):
        pass

    @abstractmethod
    def execute(self, args):
        "The required execute method that all command objects will use"


class AddCommand(Command):
    def execute(self, args):
        student = Student(0, args.name, args.surname, args.specialty, args.average_mark)
        add_student(student)
        continue_functioning = True
        print "student was added"
        return continue_functioning

    def __init__(self):
        Command.__init__(self)


class DeleteCommand(Command):
    def execute(self, args):
        remove_student(args)
        continue_functioning = True
        print "student with id: " + str(args) + " was deleted"
        return continue_functioning

    def __init__(self):
        Command.__init__(self)


class ReviewCommand(Command):
    def execute(self, args):
        students = retrieve_students()
        for student in students:
            output_student_info(student)
        continue_functioning = True
        return continue_functioning

    def __init__(self):
        Command.__init__(self)


class FilterCommand(Command):
    def execute(self, args):
        average_mark = args.average_mark
        subject = args.subject
        filter_students_by_mark_and_subjects(average_mark, subject)
        continue_functioning = True
        print "file with filtered students was saved for following parameters: \n" + "mark - "\
              + str(average_mark) + ", subject - " + subject
        return continue_functioning

    def __init__(self):
        Command.__init__(self)


class ExitCommand(Command):
    def execute(self, args):
        continue_functioning = False
        print "Exit"
        return continue_functioning

    def __init__(self):
        Command.__init__(self)
