class Person:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age

    def getName(self):
        return self.name

    def getLastName(self):
        return self.last_name

    def getAge(self):
        return self.age

class Student(Person):
    def __init__(self, name, last_name, age, indexNr):
        super().__init__(name, last_name, age)
        self.indexNr = indexNr

    def getIndexNr(self):
        return self.indexNr

"""
Zadanie 5
"""

class Employee(Person):
    def __init__(self, name, last_name, age, salary, position):
        super().__init__(name, last_name, age)
        self.salary = salary
        self.position = position

    def __str__(self):
        return f"{self.getName()} {self.getLastName()}, wiek: {self.getAge()}, stanowisko: {self.position}, pensja: {self.salary} zł"

employee1 = Employee("Jan", "Kowalski", 30, 5000, "Nauczyciel")
print(employee1)

class WorkingStudent(Student, Employee):
    def __init__(self, name, last_name, age, salary, position):
        super().__init__(name, last_name, age)
        self.salary = salary
        self.position = position

student1 = Student("Anna", "Nowak", 21, "S1234")
student2 = Student("Tomasz", "Wiśniewski", 22, "S5678")

class Group:
    def __init__(self, students):
        self.students = students

group = Group([student1, student2])

for student in group.students:
    print(student.getName(), student.getLastName(), student.getIndexNr())

