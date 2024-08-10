# Define two variables with Boolean values

isRaining = False
isCloudy = False

# Print out the value of the variables
print(f"Is it raining? {isRaining}")
print(f"Is it cloudy? {isCloudy}")

# Use Booleans to make decision or create conditionals
if (isRaining):
    print("I am NOT going out because it is raining!") # If true
else:
    print("I will go out because it is NOT raining.") # If false
    
# Comparison Operators
# Greater than >
# Less than <
# Equal to ==
# Greater than or equals to >=
# Less than or equals to <=
# Not equal to !=

offer = 600_000
expectation = 600_000

if (offer >= expectation):
    print("Yes! I will accept the job.")
else:
    print("No! I no fit do am.")
    
passphrase = "daddy loves mummy"
stranger = "daddy loves mummy"

if (passphrase != stranger):
    print("I am not following you!")
else:
    print("Hello Daddy!")
