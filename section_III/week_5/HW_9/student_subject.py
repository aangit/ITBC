class StudentSubject:
    subject_name: str
    grade: float

    def __init__(self, subject_name: str, grade: float) -> None:
        self.subject_name = subject_name
        self.grade = grade

    def __str__(self):
        result = f"NAME: {self.subject_name} GRADE: {self.grade}"
        return result
       
    def __repr__(self):
        result = f"NAME: {self.subject_name} GRADE: {self.grade}"
        return result 