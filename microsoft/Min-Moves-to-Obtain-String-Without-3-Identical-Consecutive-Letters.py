def minMove(S):
    """
    min moves to not have 3 consecutive identical letters
    """
    a = 0
    b = 0
    res = 0
    for v in S:
        if v == "a":
            a = a + 1
            b = 0
        elif v == "b":
            b = b + 1
            a = 0
        if a == 3 or b == 3:
            res = res + 1
            a = 0
            b = 0
    return res


S = "baaaaa"
print(minMove(S))  # 1

S = "baaabbaabbba"
print(minMove(S))  # 2

S = "baabab"
print(minMove(S))  # 0
