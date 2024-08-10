# Create a program that would find the least number in a list

import random

list = []

for i in range(10):
    list.append(random.randint(1, 10))

# make an assumption
min_number = list[0]
max_number = list[0]

for number in list:
    if (number < min_number):
        min_number = number
        
for number in list:
    if (number > max_number):
        max_number = number

print(list)
print(f"The minimum number is {min_number}")
print(f"The maximum number is {max_number}")