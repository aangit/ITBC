import typing
from subject import Subject
from student import Student


class Department:
    name: str
    module: str
    subjects: typing.List[Subject]
    students: typing.List[Student]

    def __init__(self, name: str, module: str, subjects: typing.List[Subject]) -> None:
        self.name = name
        self.module = module
        self.subjects = subjects
        self.students = []

    def add_student(self, student_to_add: Student) -> None:
        if student_to_add not in self.students:
            self.students.append(student_to_add)

    def add_subject(self, subject_to_add: Subject) -> None:
        if subject_to_add not in self.subjects:
            self.subjects.append(subject_to_add)
