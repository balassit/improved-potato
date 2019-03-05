# def f1(lIn):
#     l1 = sorted(lIn)
#     l2 = [i for i in l1 if i<0.5]
#     return [i*i for i in l2]

# def f2(lIn):
#     l1 = [i for i in lIn if i<0.5]
#     l2 = sorted(l1)
#     return [i*i for i in l2]

# def f3(lIn):
#     l1 = [i*i for i in lIn]
#     l2 = sorted(l1)
#     return [i for i in l1 if i<(0.5*0.5)]

# import cProfile
# import random
# lIn = [random.random() for i in range(100000)]
# cProfile.run('f1(lIn)')
# cProfile.run('f2(lIn)')

# for item in range(len(nums)):
#     for nxt in range(len(nums)):
#         if (nums[item]+nums[nxt]) == target:
#             return [item,nxt]


class Solution:
    def __init__(self):
        self.answer = []

    def generate(self, nums, target):
        current, nxt = 0, 1
        while nxt < len(nums):
            if target == nums[current] + nums[nxt]:
                self.answer = [current, nxt]
                return
            current, nxt = current, nxt + 1
            yield current
        current += 1

    def twosum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for list_index in range(len(nums) - 1):
            a = self.generate(nums[list_index:], target)
            for i in range(len(nums[list_index:]) - 1):
                try:
                    next(a)
                except StopIteration:
                    self.answer = [self.answer[0] + list_index, self.answer[1] + list_index]
                    return self.answer

    def twoSum(self, nums, target):
        numbers = {}
        for index, first in enumerate(nums):
            try:
                return [numbers[first], index]
            except KeyError:
                numbers.setdefault(target - first, index)

    def twoSum(self, nums, target):
        for index, number in enumerate(nums):
            second_number = target - number
            if second_number in nums and index is not nums.index(second_number):
                return [index, nums.index(second_number)]


nums = [3, 2, 4]
target = 6
sol = Solution()
print(f"answer: {sol.twoSum(nums, target)}")
# print(f"answer: {sol.answer}")


def star(func):
    def inner(*args, **kwargs):
        print("args")
        print(*args)
        print(**kwargs)
        print("lwargs")
        func(*args, **kwargs)
        print("*" * 30)

    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)

    return inner


@star
@percent
def printer(msg):
    print(msg)
