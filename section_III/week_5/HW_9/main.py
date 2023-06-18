from student import Student
from subject import Subject
from department import Department 
from university import University

def main():
    subject_1 = Subject("Termodinamika_1", "TM1")
    subject_2 = Subject("Termodinamika_2", "TM2")
    subject_3 = Subject("Matematika_1", "M1")
    

    department_1 = Department("Fluidi", "Fizika", [subject_1, subject_2])
    departments = [department_1]

    student_1 = Student("Luka", "12345", department_1, [subject_1, subject_2])
    student_2 = Student("Mihajlo", "766538", department_1, [subject_2, subject_3 ])
    

    student_1.insert_grade(subject_1.name, 10)
    student_1.insert_grade(subject_2.name, 8)

    student_2.add_subject(subject_1)
    student_2.insert_grade(subject_1.name, 7)
    student_2.insert_grade(subject_2.name, 9)
    
    university = University(departments)
    
    print(student_1.get_all_passed_exams())
    print(student_1.average_grade_of_student())
    for student in university.get_student_with_max_average_grade():
        print(student)
    
    for student in university.students_with_least_passed_exams():
        print(student)

    for student in university.students_passed_all_exams():
        print(student)


    print(university.students_grouped_by_department())   

    for student in university.get_students_by_department(department_1.name):
        print(student)

    print(university.failed_subject())
if __name__ == "__main__":
    main()