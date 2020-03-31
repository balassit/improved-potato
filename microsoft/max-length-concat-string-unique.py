"""
Given an array of strings arr. 
String s is a concatenation of a sub-sequence of arr which have unique characters.
Return the maximum possible length of s.
"""
res = 0


def maxLength(arr):
    """
    O(2^n)
    """
    dfs(arr, 0, "")
    return res


def dfs(l, i, s):
    global res
    # check chars are unique
    if unique(s):
        res = max(res, len(s))
        for j in range(i, len(l)):
            if unique(l[i]):
                dfs(l, j + 1, s + l[j])


def unique(s):
    """
    validate that all characters are unique
    """
    return len(s) == len(set(s))


print(maxLength(["un", "iq", "ue"]))  # 4
print(maxLength(["cha", "r", "act", "ers"]))  # 6
print(maxLength(["abcdefghijklmnopqrstuvwxyz"]))  # 26
