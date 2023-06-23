# Write a program that requires the user to enter the number of students, and then to enter information about those students:
# their number index as well as their average grade. 
# After that, the program should print out which of the students has the highest average grade. 
# Take care that the score must be in the range (6.0 - 10.0), otherwise it is necessary to re-enter the data.
# Instead of the average grade, we require the user to enter the student's grades until they enter "end grades"


def get_student_data(num_students):
    students_data = {}
    for i in range(1, num_students + 1):
        while True:
            index = input(f"Enter the index number of student {i}: ")
            grades = []
            while True:
                grade = input("Enter the student's grade (or 'end grades' to finish): ")
                if grade == "end grades":
                    break
                try:
                    grade = float(grade)
                    if grade < 6.00 or grade > 10.00:
                        raise ValueError
                    grades.append(grade)
                except ValueError:
                    print("Invalid grade! Please enter a numeric grade between 6.0 and 10.0.")
            if grades:
                students_data[index] = sum(grades) / len(grades)
                break
            else:
                print("No grades entered for the student. Please enter at least one grade.")
    return students_data

def find_highest_average_grade(students_data):
    highest_grade = 0
    highest_average_student = None

    for index, average_grade in students_data.items():
        if average_grade > highest_grade:
            highest_grade = average_grade
            highest_average_student = index
    return highest_average_student

num_students = int(input("Enter the number of students: "))

student_data = get_student_data(num_students)

highest_grade_student = find_highest_average_grade(student_data)

print("Student", highest_grade_student, "has the highest average grade.")

