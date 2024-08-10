import random

# Create a list of 20 random integers between 1000 and 2000
list = []

for i in range(20):
    list.append(random.randint(1, 100))

print(list)
# Find all even numbers in the list
for number in list:
    if number % 2 == 0:
        print(number)