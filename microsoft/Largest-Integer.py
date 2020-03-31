def largestInt(arr):
    """
    Time Complexity - O(n) 
    Space Complexity - O(n)
    """
    found = set()
    res = 0
    for num in arr:
        # if found opposite
        if -1 * num in found:
            res = max(abs(num), res)
        else:
            found.add(num)
    return res


print(largestInt([3, 2, -2, 5, -3]))
