radius =float(input("Type The radius of the first circle: "))
Area = 3.142 * radius * radius
Circumference = 2 * 3.142 * radius

print(f"The Area of the first circle is: {round(Area)} ")
print(f"The circumference of the first circle is: {round(Circumference)}")

Radius =float(input("Type the radius of the second circle:"))
area = 3.142 * Radius * Radius
circumference = 2 * 3.142 * Radius

print(f"The Area of the second circle is: {round(area)} ")
print(f"The circumference of the second circle is: {round(circumference)}")

first_circle = radius
second_circle = Radius

if(first_circle > second_circle):
    print("The first circle has a larger Area and Circumference.")
else:
    print("The second circle has a larger Area and Circumference.")
