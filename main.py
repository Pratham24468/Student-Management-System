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

    def average(self):
        total = self.Maths_marks + self.Science_marks + self.English_marks
        aver = total / 3
        return aver
    
    def grade(self):
        if self.average() >= 90:
            return "A+"
        elif self.average() >= 80:
            return "A"
        elif self.average() >= 70:
            return "B"
        elif self.average() >= 60:
            return "C"
        else:
            return "Fail"


    def display(self):
        print(self.name)
        print(self.roll_no)
        print(self.Maths_marks)
        print(self.Science_marks)
        print(self.English_marks)
        print(self.average())
        print(self.grade())


student1 = Student("Prathmesh", "01", 99, 96, 100)

student2 = Student("Rahul", "02", 91, 90, 92)

student3 = Student("Aman", "03", 95, 94, 98)

students = [student1, student2, student3]

for student in students:
    student.display()