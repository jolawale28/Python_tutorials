# This program converts Temperature in Celsius to Fahrenheit
# and vice-cersa

user_input = float(input("Enter temperature value: "))
temp_unit = (input("Enter unit (c for Celsius, f for Fahrenheit: )"))

def temp_converter(value, unit = 'c'):
    celsius_value = (value - 32) * 5 / 9
    fahrenheit_value = (value * 9 / 5) + 32
    
    if (unit == 'c'):
        return fahrenheit_value
    else:
        return celsius_value
    
converted = temp_converter(user_input, temp_unit)

print(f"{user_input}{temp_unit.upper()} is {converted}")