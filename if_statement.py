# IF statements help us to make branching decisions.

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

# Check for admission criteria

# if (comparison_expression):
#   statement

if (age < 18):
    print("Sorry, you cannot be allowed in!")

if (age > 18):
    print("You can come in. Welcome!")
 
if (name == "Ifeoma"):
    print(f"{name}, you are a VIP!")
else:
    print(f"{name}, you are a regular!")