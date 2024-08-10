# Get input from the user
user_input = input("Please enter a number: ")
user_input = int(user_input)

# The IF statement is used in making decisions based on conditions

if (user_input > 0):
    print("Number you entered is greater than zero.")
elif (user_input == 0):
    print("The number you entered is zero.")
else:
    print("Number you entered is less than zero.")