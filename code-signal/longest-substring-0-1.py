"""
Find largest subarray with equal number of 0's and 1's. 
Returns largest subarray with equal number of 0s and 1s 
"""


def maxLen(arr, n):
    m = {}
    m[0] = -1
    max_len = count = 0
    for i in range(n):
        count += 1 if arr[i] == 1 else -1
        if count in m:
            max_len = max(max_len, i - m[count])
        else:
            m[count] = i
    return max_len


arr = [0, 0, 1, 0, 1]
n = len(arr)

print(maxLen(arr, n))
