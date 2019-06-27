def binarySearch(arr, left, right, x):
    while left <= right:
        # get the mid
        mid = right // 2
        # found
        if arr[mid] == x:
            return mid
        # If x is greater, ignore left half
        elif arr[mid] < x:
            left = mid + 1
        # If x is smaller, ignore right half
        else:
            right = mid - 1
    # If we reach here, then the element
    # was not present
    return -1


# Test array
arr = [2, 3, 4, 10, 40]
x = 1

# Function call
result = binarySearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element is not present in array")
