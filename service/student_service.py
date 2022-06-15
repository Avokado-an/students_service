from repo.student_repo import create_student_filtered_file, add_student, load_initial_students, delete_student


def filter_students_by_mark_and_subjects(min_mark, subjects):
    student_filter = lambda student: subjects in student.specialty.value and student.average_mark >= min_mark
    students = retrieve_students()
    filtered_students = filter(student_filter, students)
    create_student_filtered_file(min_mark, subjects, filtered_students)
    return filtered_students


def output_student_info(student):
    print(f"{str(student.student_id)}: {student.name} {student.surname}: {str(student.average_mark)}"
          f"; subjects: {str(student.specialty.value)}")


def retrieve_students():
    students = load_initial_students()
    return students


def create_student(created_student):
    add_student(created_student)


def remove_student(student_id):
    delete_student(student_id)
