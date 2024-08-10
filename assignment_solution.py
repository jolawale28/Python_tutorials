# Create a program (named "formatted_string.py")
# that prints a sentence using f-strings.
# For example, the program should print a message like
# "My name is John, I am 20 years old, and it is True that I am a student."
# You are expected to declare exactly 3 variables separately to use
# inside the f-string.

name = "John Oluwaseun"
age = 20
isStudent = True

print(f"1. My name is {name}, I am {age} years old, and it is {isStudent} that I am a student.")

# Write a program that uses the format() method to create a sentence
# similar to the one in task 2 above.
# Name of program should be "formatted_string_2.py"

print("2. My name is {}, I am {} years old, and it is {} that I am a student.".format(name, age, isStudent))

name = "Akindele Osaze"
age = 21
has_license = True

print(f"{name} is {age} years old")
print("Has driver's licence: {}".format(has_license))

city = "Lagos"
population = 14000000
known_for = "beaches"

print("{} has a population of {} and is known for its {}.".format(city, population, known_for))

food = "Rice"
print("My best food is {}.".format(food))
