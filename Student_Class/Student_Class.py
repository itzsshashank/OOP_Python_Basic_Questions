class Student:
    student_count = 0
    total_marks = 0

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        Student.student_count += 1
        Student.total_marks += marks

    def get_student_marks(self):
        return self.marks

    @classmethod
    def get_average_marks(cls):
        return cls.total_marks/cls.student_count

    def get_student_info(self):
        return f"Name: {self.name}, Marks: {self.marks}"


student1 = Student("Shahsank", 88)
student2 = Student("Vansh", 70)
student3 = Student("Ravijeet", 92)

print(Student.student_count)  # To get total student count
print(student1.get_student_marks())  # To get marks of a particular student
print(Student.get_average_marks())  # To get Average marks of all the students
print(student3.get_student_info())  # To get student's information
print(student2.get_student_marks())  # To get marks of a particular student
