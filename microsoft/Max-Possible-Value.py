"""
Given integer N return max possible value obtained 
by inserting one '5' digit inside the decimal representation of integer N
"""


def maxValue(n):
    """
    Time Complexity - O(n)
    Space Complexity - O(n) to create number list as string
    """
    sign = -1 if n < 0 else 1
    number = [x for x in str(abs(n))]
    index = 0
    ch = "5"
    while index < len(number):
        if sign == 1 and number[index] < ch:
            break
        elif sign == -1 and number[index] > ch:
            break
        index = index + 1
    # before, '5', after
    number = number[:index] + [ch] + number[index:]
    return int("".join(number)) * sign


print(maxValue(268))
print(maxValue(670))
print(maxValue(0))
print(maxValue(-999))
