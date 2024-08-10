# Function will accept a string from the user
# and count how many vowels are in the string

string = input("Enter your text: ")

vowels = 'aeiouAEIOU'

def count_vowels(text):
    count = 0
    # Loop through the String
    for s in text:
        if (s in vowels):
            count += 1
    return count

print(f"Number of vowels in {string} is {count_vowels(string)}.")