# Function determines if a number is even or odd
# if even, returns True
# if odd, returns False

user_input = int(input("Please enter a number: "))

def even_odd(number):
    if (number % 2 == 0):
        return "Even"
    else: 
        return "Odd"

print(f"{user_input} is an {even_odd(user_input)} number.")