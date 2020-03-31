"""
Given a string s consisting of n lowercase letters, 
you have to delete the minimum number of characters 
from s so that every letter in s appears a unique number of times. 
We only care about the occurrences of letters that appear at least once in result.
"""
from collections import defaultdict


def min_deletions(s):
    """
    1. O(s) - iterate over string, s
    2. O(k) - where k is num chars (26)
    3. O(k) - find max of number of occurance of each char
    4. O(m) - max(k), iterate from max occurance to 0. As num occurances increases, more to iterate
    Time Complexity - O(k+m+s)
    Space Complexity O(k + m) - iteration over m numbers creates additional values in occ dict
    """
    # 1. key pair: char, occurances
    letters = defaultdict(str)
    for ch in s:
        letters[ch] = letters.get(ch, 0) + 1

    # 2. key pair: num occurances, number of letters that occur
    occ = defaultdict()
    for k, v in letters.items():
        occ[v] = occ.get(v, 0) + 1

    # 3. find largest key
    maxKey = max(occ.keys())
    deletions = 0
    # iterate over keys in order
    for i in range(maxKey, 0, -1):
        if occ.get(i, 0) != 0:
            carry = occ.get(i) - 1
            occ[i - 1] = occ.get(i - 1, 0) + carry
            occ[i] = occ.get(i) - carry
            deletions = deletions + carry

    print(occ, letters)
    return deletions


print(min_deletions("aaaabbbbccccddeef"))  # 7
print(min_deletions("example"))  # 4
print(min_deletions("llll"))  # 0
print(min_deletions("aabbffddeaee"))  # 6
print(min_deletions("eeeeffff"))  # 1
