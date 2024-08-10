# Create a list of numbers
numbers = [11, 12, 13, 24, 35, 26, 47, 58, 29, 20,40,44,55,60,
           11, 12, 13, 24, 35, 26, 47, 58, 29, 20,40,44,55,60 ]

# Initialize counters for even and odd numbers
even_count = 0
odd_count = 0

# Loop through the list and increment the appropriate counter
for number in numbers:
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

# Print out the counts for even and odd numbers
print(numbers)
print(f"Even numbers count: {even_count}")
print(f"Odd numbers count: {odd_count}")