# """
# Alexa is given n piles of equal or unequal heights.
# In one step, Alexa can remove any number of boxes from the pile
# which has the maximum height and try to make it equal to the one
# which is just lower than the maximum height of the stack.
# Determine the minimum number of steps required to make all of the piles equal in height.
# """
# from collections import defaultdict
# def minSteps(piles):
#     """
#     Time Complexity - O(N(log(n))) sort
#     Space Complexity - O(1) *sort is in place
#     """
#     piles.sort(reverse=True)
#     res = 0
#     for i in range(1,len(piles)):
#         if piles[i] < piles[i-1]:
#             res = res + i
#     return res

# print(minSteps([5, 2, 1]))
# print(minSteps([4, 5, 5, 4, 2]))

p = "1234"
print(p[-1:])
