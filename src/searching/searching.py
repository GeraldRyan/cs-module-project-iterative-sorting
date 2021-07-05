def linear_search(arr, target):
    # Your code here
    for index in range(len(arr)):
        if arr[index] == target:
            return index 


    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    low = 0
    mid = round(len(arr)/2)
    high = len(arr)-1

    while low <= high:
        mid = round((low + high) / 2)

        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            high = mid-1
        else: 
            low = mid+1
# arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]


    return -1  # not found
