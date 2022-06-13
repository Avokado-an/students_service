import os
from datetime import datetime

import openpyxl
from openpyxl import Workbook

from entity.specialty import Specialty
from entity.student import Student

students_path = "students.xlsx"
sheet_name = "Sheet1"
filters_path = "saved/filter/"


def load_spreadsheet_sheet(file_path, spread_sheet_name):
    spreadsheet_file = load_spreadsheet_file(file_path)
    return spreadsheet_file[spread_sheet_name]


def load_spreadsheet_file(file_path):
    try:
        return openpyxl.load_workbook(file_path)
    except IOError:
        print "No spreadsheet provided"


def load_initial_students():
    student_sheet = load_spreadsheet_sheet(students_path, sheet_name)
    students = []
    for student_row in range(2, student_sheet.max_row + 1):
        student = fill_student_properties_from_spreadsheet(student_sheet, student_row)
        students.append(student)
    return students


def add_student(created_student):
    wb = load_spreadsheet_file(students_path)
    ws = wb[sheet_name]
    created_student.student_id = define_last_student_id() + 1
    student_dict = {
        1: created_student.student_id,
        2: created_student.name,
        3: created_student.surname,
        4: created_student.specialty,
        5: created_student.average_mark
    }
    ws.append(student_dict)
    wb.save(students_path)


def delete_student(student_id):
    wb = load_spreadsheet_file(students_path)
    ws = wb[sheet_name]
    for student_row in range(2, ws.max_row + 1):
        if ws.cell(student_row, 1).value == student_id:
            ws.delete_rows(student_row)
            wb.save(students_path)


def create_student_filtered_file(minimal_mark, subject, students):
    date = datetime.today().strftime('%Y-%m-%d')
    create_path_if_not_exist()
    filename = "filter_for_" + subject + "_with_mark_above_" + str(minimal_mark) + "_for_" + str(date) + ".xlsx"
    wb = Workbook()
    ws = wb.active
    student_id = 1
    header = {
        1: "id",
        2: "name",
        3: "surname"
    }
    ws.append(header)
    for student in students:
        student_dict = {
            1: student.student_id,
            2: student.name,
            3: student.surname
        }
        ws.append(student_dict)
        student_id += 1
    wb.save(filters_path + filename)


def create_path_if_not_exist():
    if not os.path.exists(filters_path):
        os.makedirs(filters_path)

def define_last_student_id():
    student_sheet = load_spreadsheet_sheet(students_path, sheet_name)
    return student_sheet.cell(student_sheet.max_row, 1).value


def define_last_row():
    student_sheet = load_spreadsheet_sheet(students_path, sheet_name)
    return student_sheet.max_row


def fill_student_properties_from_spreadsheet(sheet, row):
    student = Student(sheet.cell(row, 1).value,
                      sheet.cell(row, 2).value,
                      sheet.cell(row, 3).value,
                      getattr(Specialty, sheet.cell(row, 4).value),
                      sheet.cell(row, 5).value
                      )
    return student
