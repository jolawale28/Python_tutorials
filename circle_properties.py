# This programs calculates the Area of a circle when the user
# inputs the radius.
#
# Copyright 2024, Joseph O.B.

radius  = float(input("Please type the radius of the circle: "))

area = 3.142 * radius * radius # Teach the computer
circumference =  2 * 3.142 * radius

decimal_places = int(input("Please specify the number of decimal places: "))

# Round the area to 1 decimal place
print(f"The area is: {round(area, decimal_places)}")
print(f"The circumference is {round(circumference, decimal_places)}")