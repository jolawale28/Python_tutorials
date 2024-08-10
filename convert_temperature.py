def convert_temperature(temp, convert_to = 'f'):
    if (convert_to == 'f'):
        converted = (temp * 9 / 5) + 32
        return converted
    elif convert_to == 'k':
        converted = temp + 273.15
        return converted
    else:
        return "Invalid conversion type!"
    
print(f"25 degrees Celsius in Fahrenheit is {convert_temperature(25)}")
print(f"25 degrees Celsius in Kelvin is {convert_temperature(25, 'k')}")
print(f"25 degrees Celsius to type 'X' is {convert_temperature(25, 'x')}")