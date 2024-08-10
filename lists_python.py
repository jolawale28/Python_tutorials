
# Joseph Olawale Bamidele
# c2024

from typing import List

def turn_to_consecutive(arr: List[int]) -> int:

    arr.sort()
    permutationList = [x + 1 for x in range(0, len(array))]
    
    global numOfOperation
    numOfOperation = 0
    
    # Check if first and last values of array are not same with permutationList
    # If not then, set both to default value of 1 and 4
    
    if (arr[0] != permutationList[0]):
        arr[0] = permutationList[0]
        numOfOperation += 1
        print("First: ", numOfOperation)
        
    if (arr[-1] != permutationList[-1]):
        arr[-1] = permutationList[-1]
        numOfOperation += 1

    
    for i, number in enumerate(arr):
        if (i == 0 or i == len(arr) - 1):
            continue
        
        if (number > permutationList[i] or number < permutationList[i]):
            
            arr[i] = permutationList[i]
            numOfOperation += 1
    
    return numOfOperation

array = [4, 3, 2, 4]
# array = [4, 4, 1, 2, 5, 5, 10]

print(f"Number of operations: {turn_to_consecutive(array)}")

