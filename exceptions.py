number = int(input("Please enter a number"))
big_number = 50

try:
    print(big_number / 4)
except ZeroDivisionError:
    print("Division by zero is not possible!")
    print("Will this be printed?")
except (NameError, TypeError):
    print("A variable has not been properly declared before use!")
else:
    print("This will run if there is no error in the try block!")
finally:
    print("This will surely print!")