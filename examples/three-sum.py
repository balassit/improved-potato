def threeSum(nums):
    res = []
    length = len(nums)
    nums.sort()
    for i in range(0,len(nums)-1):
        if nums[i] > 0:
            break
        if i > 0 and nums[i]==nums[i - 1]:
            continue
        # initialize left and right
        l, r = i + 1, length - 1
        while l < r:
            total = nums[i] + nums[l] + nums[r]
            # If sum of three elements is less than zero then increment in left
            if total < 0:
                l += 1
            # If sum of three elements is greater than zero then decrement in right
            elif total > 0:
                r -= 1
            else:
                res.append([nums[i], nums[l], nums[r]])
                # for uniqueness
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                while l < r and nums[r]==nums[r-1]:
                    r -= 1
                l += 1
                r -= 1
    return res
nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))