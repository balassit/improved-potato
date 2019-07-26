"""
Divide and Conquer
O(log(n))
Choice to start is in the middle
"""


def find_peak(nums):
    low = 0
    high = len(nums) - 1
    if low == high:
        return 0
    while low <= high:
        # Find index of middle element
        mid = low + (high - low) // 2
        # Compare middle element with its neighbours (if neighbours exist)
        if (mid == 0 or nums[mid - 1] <= nums[mid]) and (
            mid == len(nums) - 1 or nums[mid + 1] <= nums[mid]
        ):
            return mid
        # not a peak and right is >, then left must have peak
        elif mid > 0 and nums[mid - 1] > nums[mid]:
            high = mid
        # not a peak and left is >, then left must have peak
        else:
            low = mid + 1


arr = [3, 2, 1]
print(f"peak in array: {arr[find_peak(arr)]}")

"""
Greedy ascent algorithm
Have to make a choice on where to start and direction to traverse
O(n^2)
Similar to the O(n) on 1-D list iterating all items checking surroundings
"""

"""
1. Pick middle column j = m / 2
2. Find max on column j at (i, j)
3. Compare (i, j - 1), (i,j), (i, j + 1) - look left and right
4. Pick left columns if (i, j - 1) > (i, j)
   Pick right columns if (i, j + 1) > (i, j)
   Else, (i, j) is 2-D peak
"""
