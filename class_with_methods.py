# Description: Define a class Circle with an attribute radius and methods area() and
# circumference() to calculate and return the area and circumference of the circle.
# Task: Create an instance of the Circle class, set the radius, and display the area and
# circumference using the class methods.

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def circumference(self):
        return 2 * math.pi * self.radius
    
circleObj = Circle(10)

print(f"Area of circle of {circleObj.radius}cm is {circleObj.area()}.")
print(f"Circumference of circle of {circleObj.radius}cm is {circleObj.circumference()}.")