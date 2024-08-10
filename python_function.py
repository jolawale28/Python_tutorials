def area_of_circle(radius):
    area = 3.14 * radius ** 2
    return area

user_input = float(input("Enter the radius: "))

print(area_of_circle(user_input))