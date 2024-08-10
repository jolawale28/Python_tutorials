# Object Oriented Programming

# Parent
class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    
    def printname(self):
        print(self.firstname, self.lastname)

person = Person("Joseph", "Olawale")

person.printname()

# Child
class Student(Person):
    def __init__(self, firstname, lastname, matric_no):
        super().__init__(firstname, lastname)
        self.matric_no = matric_no
    
    def print_matric(self):
        print(self.matric_no)

student = Student("Alawode", "Michael", "092091")
student.printname()
student.print_matric()