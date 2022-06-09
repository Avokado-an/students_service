class Student:
    def __init__(self, student_id, name, surname, specialty, average_mark):
        self.student_id = student_id
        self.name = name
        self.surname = surname
        self.specialty = specialty
        self.average_mark = average_mark

    def retrieve_specialty_subjects(self):
        return self.specialty
