class Person:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = int(age)

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

class Note:
    def __init__(self, notes):
        self.notes = notes

    def getNotes(self):
        return self.notes

    def getAverage(self):
        return sum(self.notes.values()) / len(self.notes) if self.notes else 0

class StudentWithNotes(Student, Note):
    def __init__(self, name, last_name, age, indexNr, notes):
        Student.__init__(self, name, last_name, age, indexNr)
        Note.__init__(self, notes)

    def __str__(self):
        return f"{self.getName()} {self.getLastName()} ({self.getIndexNr()}), średnia ocen: {self.getAverage():.2f}"

class Group:
    def __init__(self, students=None):
        self.students = students if students else []

    def printStudents(self):
        print("Lista studentów:")
        for student in self.students:
            print(student)

    def printAverage(self):
        if not self.students:
            print("Brak studentów w grupie.")
            return
        total = sum(student.getAverage() for student in self.students)
        print(f"Średnia grupy: {total / len(self.students):.2f}")

    def loadFromFile(self, filename):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                for line in file:
                    parts = line.strip().split(",")
                    if len(parts) != 5:
                        print(f"Pominięto nieprawidłowy wiersz: {line}")
                        continue
                    name, last_name, age, indexNr, notes_str = parts
                    notes = {}
                    for note_entry in notes_str.split(";"):
                        subject, grade = note_entry.split(":")
                        notes[subject] = int(grade)
                    student = StudentWithNotes(name, last_name, age, indexNr, notes)
                    self.students.append(student)
        except FileNotFoundError:
            print(f"Plik '{filename}' nie został znaleziony.")
        except PermissionError:
            print(f"Brak uprawnień do odczytu pliku '{filename}'.")
        except Exception as e:
            print(f"Wystąpił inny błąd: {e}")

group = Group()
group.loadFromFile("students.txt")
group.printStudents()
group.printAverage()
