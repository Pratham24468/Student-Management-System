#Student Management System

print("|-------------------------|")
print("|Student Management System|")
print("|-------------------------|")

class Student:
    def __init__(self, name, roll_no, Maths_marks, Science_marks, English_marks):
        self.name = name
        self.roll_no = roll_no
        self.Maths_marks = Maths_marks
        self.Science_marks = Science_marks
        self.English_marks = English_marks

    def display(self):
        print(self.name)
        print(self.roll_no)
        print(self.Maths_marks)
        print(self.Science_marks)
        print(self.English_marks)

student1 = Student("Prathmesh", "01", 99, 96, 100)
student1.display()