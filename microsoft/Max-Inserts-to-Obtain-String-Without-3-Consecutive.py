"""
Given a string S consisting of N characters,
return the maximum number of letters 'a' that can be inserted into S
so the resulting string does not contain 3 consecutive 'a'
If the string already contains 3 consecutive 'a's, return -1
"""


def maxInserts(s):
    """
    Time Complexity - O(n)
    Space Complexity - O(1)
    """
    limit = 3
    char = "a"
    count = 0
    cur = 0
    # checking character count to the left across string
    for v in s:
        if v == char:
            cur = cur + 1
        else:
            # update total with 2 'a' minus current number of 'a' in place
            count = count + (limit - 1) - cur
            cur = 0
        if cur == limit:
            return -1

    # end needs to check to the right of last char
    if s[:-1] == char:
        count = count + (limit - 1) - cur
    else:
        count = count + (limit - 1)
    return count


print(maxInserts("aabab"))  # 3
print(maxInserts("dog"))  # 8
print(maxInserts("aa"))  # 0
print(maxInserts("baaaa"))  # -1
