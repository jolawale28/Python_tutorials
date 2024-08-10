"""
Count Elements less than a given value
Write a Python program that counts the number of elements in the list less than the number
entered by the user.
Instructions
- Populate a list with random integers between 1 and 1000.
- Prompt the user for a number (float or int). Number must be between 1 and 1000. If user
enters number outside of the given range, program should print out “Sorry, number not
within range”.
- Based on the user’s input, perform the appropriate iteration and display the results.
"""

import random

list  = []
for i in range(5):
    list.append(random.randint(0, 1000))

user_input = float(input("Enter a number between 1 and 1000: "))

if (user_input < 1 or user_input > 1000):
    print("Sorry, number not within range!")
    exit
    
count = 0

for number in list:
    if (number < user_input):
        count += 1

print(list)

print(f"Items less than {user_input} in the list are {count} number.")