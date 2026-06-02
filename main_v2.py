
print("|-------------------------|")
print("|Student Management System|")
print("|-------------------------|")

print("1. Add Student")
print("2. View Students")
print("3. Find Topper")
print("4. Exit")

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

students = []

while True:
    choice = input("Enter choice: ")
    
    if choice == "1":
        stud_name = input("Student's Name:")
        stud_rollno = input("Student's Roll no:")
        stud_maths_marks = int(input("Student's Marks in Math:"))
        stud_science_marks = int(input("Student's Marks in Science:"))
        stud_english_marks = int(input("Student's Marks in English:"))
        student = Student(stud_name, stud_rollno, stud_maths_marks, stud_science_marks, stud_english_marks)
        students.append(student)
    
    elif choice == "2":
        for student in students:
            student.display()

    elif choice == "3":
        if students:
            topper = students[0]
        else:
            for current_student in students:
                if current_student.average() >= topper.average():
                    topper = current_student
                    Topper = topper.display()

    elif choice == "4":
        break
