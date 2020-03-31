def stringWithout3Identical(S):
    """
    Time Complexity O(n) - n is length of S
    Space Complexity (n) - excluding final result string
    1. iterate characters of S
    2. if current ch equals previous ch, count increases
    3. otherwise, reset count to 1 to include just passed ch
    4. if count < 3 after pass, add to res
    return string without 3 consecutive letters
    """
    if len(S) < 3:
        return S
    ch = ""
    count = 0
    res = []
    for v in S:
        if v != ch:
            ch = v
            count = 1
        else:
            count = count + 1
        if count < 3:
            res.append(v)
    return "".join(res)


S = "eedaaad"
print(stringWithout3Identical(S))

S = "xxxtxxx"
print(stringWithout3Identical(S))

S = "uuuuxaaaaxuuu"
print(stringWithout3Identical(S))
