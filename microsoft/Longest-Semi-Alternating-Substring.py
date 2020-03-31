"""
Given string s of length N
Only characters are 'a' and 'b'
substring is semi-alternating if it does not 
contain 3 identical consecutive characters
Return longest length of the semi-alternating substring
"""


def maxSemiAlternatingString(s):
    """
    Time Complexity - O(n) iterate length of s
    Space Complexity - O(1)
    """
    # define consecutive length param
    k = 3
    # less than k
    if len(s) < k:
        return len(s)
    left = 0
    count = 1
    res = 0
    for i in range(1, len(s)):
        # clear count when not equal
        if s[i] != s[i - 1]:
            count = 1
        else:
            count = count + 1
        # move left pointer back
        if count == k:
            left = i - 1
        # current position minus starting position + 1 for length
        else:
            res = max(res, i - left + 1)
    return res


print(maxSemiAlternatingString("baaabbabbb"))  # 7
print(maxSemiAlternatingString("babba"))  # 5
print(maxSemiAlternatingString("abaaaa"))  # 4
print(maxSemiAlternatingString("a"))  # 1
