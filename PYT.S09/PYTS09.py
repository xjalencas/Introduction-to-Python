class Subject:

    def __init__(self, name, hours, teacher):

        self.name = name
        self.hours = hours
        self.teacher = teacher

        self.students = set()

    def add_student(self, student):
        self.students.add(student)


class Person:

    def __init__(self, name, surname, NIE, birth_date=None):

        self.name = name
        self.surname = surname
        self.NIE = NIE
        self.birth_date = birth_date



class Teacher(Person):

    def __init__(self, name, surname, NIE, birth_date, salary):

        self.salary = salary
        super().__init__(name=name,
                         surname=surname,
                         NIE=NIE,
                         birth_date=birth_date)


class Student(Person):
    pass


student_instance1 = Student(name="Pere",
                            surname="Anton",
                            birth_date="1/1/1990",
                            NIE="u5241")

student_instance2 = Student(name="Pere",
                            surname="Anton",
                            birth_date="1/1/1990",
                            NIE="u5241")

student_instance3 = Student("Nuria", "Gonzalez", "u22312", "20/10/1992")
student_instance4 = Student("Toni", "Bonet", "u22312", "20/1071992")

my_student_list = [student_instance1,
                   student_instance2,
                   student_instance3,
                   student_instance4]

teacher_instance = Teacher(name="Xavi", surname="Jalencas", NIE="u1234",
                          birth_date="1/1/1980", salary=100)

PYT = Subject(name="PYT", hours=125, teacher=teacher_instance)

PYT.add_student(student_instance1)
PYT.add_student(student_instance2)
PYT.add_student(student_instance3)
PYT.add_student(student_instance4)
PYT.add_student(student_instance1)


