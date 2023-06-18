import typing
from subject import Subject
from student_subject import StudentSubject


class Student:
    grades: typing.List[StudentSubject]

    def __init__(self, name: str, student_id: str, department, subjects: typing.List[Subject]) -> None:
        self.__name = name
        self.student_id = student_id
        self.department = department
        self.department.add_student(self)
        self.subjects = subjects
        self.grades = []
        for subject in self.subjects:
            new_grade = StudentSubject(subject.name, None)
            self.grades.append(new_grade)
        self.all_students.append(self)

    def __str__(self):
        result = f"NAME: {self.__name} STUDENT ID: {self.student_id}\nSubjects\n"
        for subject in self.subjects:
            result += subject.name + "\n"
        return result

    def __repr__(self):
        result = f"NAME: {self.__name} STUDENT ID: {self.student_id}\nSubjects\n"
        for subject in self.subjects:
            result += subject.name + "\n"
        return result

    def add_subject(self, subject_to_add: Subject) -> None:
        if subject_to_add not in self.subjects:
            self.subjects.append(subject_to_add)
            new_grade = StudentSubject(subject_to_add.name, None)
            self.grades.append(new_grade)

    def insert_grade(self, exam_name: str, grade: float) -> None:
        for subject in self.grades:
            if subject.subject_name == exam_name:
                subject.grade = grade
                return
        raise ValueError(
            f"Student does not have this exam {exam_name} assigned")

    def get_name(self):
        return self.__name

    def get_all_passed_exams(self) -> typing.List[StudentSubject]:
        list_of_passed_exams = []
        for grade in self.grades:
            if grade.grade is not None:
                list_of_passed_exams.append(grade)
        return list_of_passed_exams

    def average_grade_of_student(self) -> float:
        passed_exams = self.get_all_passed_exams()
        sum_of_grades = 0
        number_of_passed_exams = len(passed_exams)
        if number_of_passed_exams == 0:
            return 0
        for passed_exam in passed_exams:
            sum_of_grades += passed_exam.grade
        return sum_of_grades / number_of_passed_exams

    #to be fixed!
    def get_subject_with_highest_average(self):
        counter = 0
        sum_of_grades = 0
        dict_with_top_passed_subject = {}
        for name in self.grades:
            if self.grades[name] == name:
                counter += 1
                sum_of_grades += self.grades[name]
        dict_with_top_passed_subject[name] = sum_of_grades / counter

        max_value = 0
        top_passed_subject = " "
        for subject in dict_with_top_passed_subject:
            if dict_with_top_passed_subject[subject] > max_value:
                max_value = dict_with_top_passed_subject[subject]
                top_passed_subject = subject
        return top_passed_subject

    def all_exams_passed(self) -> bool:
        for grade in self.grades:
            if grade.grade is None:
                return False
        return True