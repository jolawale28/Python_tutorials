# Get an input from the user
x = int(input("Please enter a positive number: "))

# DO a testing to check if x is less than zero
if x < 0:
    # Now that we know x is less than zero, raise Exception!
    raise Exception("Sorry, no number below zero!")