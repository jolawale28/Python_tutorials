# Sum of Squares
# Sum of Cubes

list = [2, 3, 1, 7, 4, 8]
squared_list = [4, 9, 1, 49, 16, 64]
cubed_list = [8, 27, 1, 343, 64, 512]
sum_of_squares = 143
sum_of_cubes = 955

def sum_of_powers(list, power = 1):
    total = 0
    for number in list:
        square = number ** power
        total += square
    return total

print(sum_of_powers(list))
print(sum_of_powers(list, 2))
print(sum_of_powers(list, 3))
print(sum_of_powers(list, 100))
        