# Description: Define a class Student with attributes name, age, and grade. Implement a
# constructor to initialize these attributes and a destructor to print a message when an object
# is destroyed.
# Task: Create instances of the Student class and observe the constructor and destructor
# behavior by printing messages during object creation and deletion.

class Student:

    # Object creation (Constructor)
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        print("New Student created!")
    
    # Object deletion/destroyed (Destructor)
    def __del__(self):
        print("Student removed totally!")

std1 = Student("Joseph", 28, 3.24)
std2 = Student("Ronaldo", 22, 4.01)