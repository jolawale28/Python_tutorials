# Description: Define a class Employee with attributes name, position, salary. Include a
# method give_raise(percent) that increases the salary by a given percentage.
# Task: Create an instance of the Employee class, give the employee a raise, and display the
# updated salary.

class Employee:

    def __init__(self, name, position, salary) -> None:
        self.name = name
        self.position = position
        self.salary = salary

    def give_raise(self, percent) -> float:
        new_salary = self.salary + percent / 100 * self.salary
        return new_salary

manager = Employee("Jasmine", "manager", 700000)

print(f"New salary for {manager.name} is {manager.give_raise(30)}.")