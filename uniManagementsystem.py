class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def set_details(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}")

class Student(Person):
    def __init__(self,name, age, gender, studentID, course, grades):
        super().__init__(name, age, gender)
        self.studentID = studentID
        self.course = course
        self.grades = grades
    
    def set_student_details(self, studenID, course):
        self.studentID = studenID
        self.course = course

    def add_grade(self, grades):
        self.grades = grades.append(self.grades)
    
    def calculate_average_grade(self):
        grades = self.grades
        if len(grades) == 0:
            return 'there are no grades'
        else:
            print(sum(grades)/len(grades))

    def get_student_summary(self):
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Student ID: {self.studentID}, Course: {self.course}, Grades: {self.grades}")


class Professor(Person):
    def __init__(self,name, age, gender, staffID, department, salary):
        super().__init__(name, age, gender)
        self.staffID = staffID
        self.department = department
        self.salary = salary
    
    def set_professor_details(self, staffID, department, salary):
        self.staffID = staffID
        self.department = department
        self.salary = salary

    def give_feedback(self, student, feedback):
        print(f"Feedback for {student.name}: {feedback}")

    def increase_salary(self, percentage):
        self.salary = self.salary * (percentage + 1)

    def get_professor_summary(self):
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Staff ID: {self.staffID}, Department: {self.department}, Salary: {self.salary} ")


professor = Professor("a", 0, "b", "c", "d", 0)
professor.set_details("Dr. Smith", 45, "Male")
professor.set_professor_details("P1234", "Mathematics", 55000)

student = Student("a", 0, "b", "c", "d", 0)
student.set_details("Alice Johnson", 20, "Female")
student.set_student_details("S5678", "Physics")

professor.give_feedback(student, "Great work on your assignment!")
        

class Administrator(Person):
    def __init__(self, name, age, gender, adminID, office, years_of_service):
        super().__init__(name, age, gender)
        self.adminID = adminID
        self.office = office
        self.years_of_service = years_of_service

    def set_admin_details(self, adminID, office, years_of_service):
        self.adminID = adminID
        self.office = office
        self.years_of_service = years_of_service

    def increment_service_years(self):
        self.years_of_service += 1

    def get_admin_summary(self):
        print(f"")


    
