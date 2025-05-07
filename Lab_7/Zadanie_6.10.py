class ReadFileError(Exception):
    def __init__(self, filename):
        super().__init__(f"Błąd odczytu pliku: {filename}. Sprawdź, czy plik istnieje i masz do niego dostęp.")

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

    def __str__(self):
        return f"{self.name} {self.last_name}, wiek: {self.age}"

class Student(Person):
    def __init__(self, name, last_name, age, indexNr):
        super().__init__(name, last_name, age)
        self.indexNr = indexNr

    def getIndexNr(self):
        return self.indexNr

    def __str__(self):
        return f"{super().__str__()}, indeks: {self.indexNr}"

class Group:
    def __init__(self, students):
        self.students = students

    def show(self):
        for student in self.students:
            print(student)

    @staticmethod
    def read_students_from_file(filename):
        students = []
        try:
            with open(filename, "r") as file:
                for line in file:
                    parts = line.strip().split(",")
                    if len(parts) == 4:
                        name, last_name, age, indexNr = parts
                        students.append(Student(name, last_name, int(age), indexNr))
            return Group(students)
        except (FileNotFoundError, PermissionError):
            raise ReadFileError(filename)

try:
    group = Group.read_students_from_file("students.txt")
    print("Wczytani studenci:")
    group.show()
except ReadFileError as e:
    print(e)
