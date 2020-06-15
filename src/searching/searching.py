def linear_search(arr, target):
    # Your code here
    for index in range(len(arr)):
        if arr[index] == target:
            return index 


    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    if arr[len(arr)/2] > target:
        return "greater"


    return -1  # not found
