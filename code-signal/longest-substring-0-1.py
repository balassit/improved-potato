"""
Find largest subarray with equal number of 0's and 1's. 
Returns largest subarray with equal number of 0s and 1s 
"""


def maxLen(arr, n):
    hash_map = {}
    curr_sum = max_len = 0
    ending_index = -1
    # convert 0 to -1
    arr = list(map(lambda x: -1 if x == 0 else x, arr))

    for i in range(0, n):
        # Add current element to sum
        curr_sum += arr[i]

        # To handle sum=0 at last index
        if curr_sum == 0:
            max_len = i + 1
            ending_index = i

        # If this sum is seen before, then update max_len if required
        if (curr_sum + n) in hash_map:
            max_len = max(max_len, i - hash_map[curr_sum + n])
        else:
            hash_map[curr_sum] = i

    print(f"{ending_index - max_len + 1} to {ending_index}")
    return max_len


arr = [1, 0, 0, 1, 0, 1, 1]
n = len(arr)

maxLen(arr, n)
