import math
import os
import random
import re
import sys
import collections


#
# Complete the 'rollTheString' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY roll
#


def rollTheString(s, roll):
    # Write your code here
    # total num of rolls for each char
    res = list(s)
    num_rolls = [0] * len(s)
    for r in roll:
        num_rolls[r - 1] += 1
    cur_sum = 0
    for i in range(len(num_rolls) - 1, -1, -1):
        print(i + 1, num_rolls[i])
        cur_sum += num_rolls[i]
        res[i] = roll_char(res[i], cur_sum)

    return "".join(res)


def roll_char(char, r):
    """
    update takes place for range of 26 letter
    if roll > 26 it cycles so take mod to get remainder instead
    """
    a = ord("a")
    c = ord(char) - a
    return chr((a + (c + r) % 26))


if __name__ == "__main__":

    for _ in range(1):
        out = rollTheString("abc", [3])
    print(out)
