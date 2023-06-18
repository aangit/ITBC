from typing import List
from department import Department
from student import Student


class University:

    departments: List[Department]

    def __init__(self, departments: List[Department]) -> None:
        self.departments = departments

    def add_department(self, department: Department) -> None:
        if department not in self.departments:
            self.departments.append(department)

    def get_all_students(self) -> List[Student]:
        students_accross_departments = []
        for department in self.departments:
            students_accross_departments += department.students
        return students_accross_departments

    def get_student_with_max_average_grade(self):
        best_students = []
        best_average_grade = 0
        for student in self.get_all_students():
            average_grade = student.average_grade_of_student()
            if average_grade == best_average_grade:
                best_students.append(student)
            if average_grade > best_average_grade:
                best_students.clear()
                best_students.append(student)
                best_average_grade = average_grade
        return best_students

    def failed_subject(self):
        failed_subjects = []
        passed_subjects = []
        for student in self.get_all_students():
            for subject in student.grades:
                if subject.grade is None:
                    failed_subjects.append(subject)
                else:
                    passed_subjects.append(subject)

        return set(failed_subjects).difference(set(passed_subjects))

    def students_with_least_passed_exams(self) -> List[Student]:
        min_value = 9999
        least_exams = []

        for student in self.get_all_students():
            all_exams = len(student.get_all_passed_exams())
            if all_exams == min_value:
                least_exams.append(student)
            if all_exams < min_value:
                least_exams.clear()
                least_exams.append(student)
                min_value = all_exams
        return least_exams

    def students_passed_all_exams(self) -> List[Student]:
        students = []
        for student in self.get_all_students():
            if student.all_exams_passed():
                students.append(student)
        return students

    def students_grouped_by_department(self) -> dict:
        grouped_by_department = dict()
        for student in self.get_all_students():
            if student.department.name not in grouped_by_department:
                grouped_by_department[student.department.name] = 1
            else:
                grouped_by_department[student.department.name] += 1
        number_of_students = len(self.get_all_students())
        for dep in grouped_by_department:
            grouped_by_department[dep] = grouped_by_department[dep] / \
                number_of_students * 100
        return grouped_by_department


    def get_students_by_department(self, department_name: str) -> List[Student]:
        for department in self.departments:
            if department.name == department_name:
                return department.students
        raise ValueError (f"There is no such department {department_name}")
