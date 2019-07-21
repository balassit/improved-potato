def sortColors(nums) -> None:
    """
        Do not return anything, modify nums in-place instead.
        """
    low = cur = 0
    high = len(nums) - 1

    while cur <= high:
        if nums[cur] == 0:
            nums[low], nums[cur] = nums[cur], nums[low]
            low += 1
            cur += 1
        elif nums[cur] == 2:
            nums[high], nums[cur] = nums[cur], nums[high]
            high -= 1
        elif nums[cur] == 1:
            cur += 1
        else:
            raise ValueError(f"Invalid input found: {nums[cur]}")


arr = [2, 0, 2, 1, 3, 1, 0]
sortColors(arr)
print(arr)
