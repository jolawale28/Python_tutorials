list = ['Canada', 'USA', "Norway", 'Finland', 'Sweden']

search_input = input("Enter country to search for: ")

match_found = False

for i in range(len(list)):
    if (search_input == list[i]):
        match_found = True
        print(f"{search_input} found at index: {i}")

if (match_found == False):
    print("Sorry, could not find a match!")