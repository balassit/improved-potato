import itertools
import collections


def mergeStrings(s1, s2):
    s1 = list(s1)
    s2 = list(s2)
    res = []
    c1 = collections.Counter(s1)
    c2 = collections.Counter(s2)
    p1 = p2 = 0
    while p1 < len(s1) or p2 < len(s2):
        x = y = None
        if p1 < len(s1):
            x = s1[p1]
        if p2 < len(s2):
            y = s2[p2]

        if x is not None and y is not None:
            if c1[x] == c2[y]:
                # do normal compare and insert
                if x < y:
                    res.append(f"{x}")
                    p1 += 1
                else:
                    res.append(f"{y}")
                    p2 += 1
            elif c1[x] < c2[y]:
                res.append(f"{x}")
                p1 += 1
            elif c2[y] < c1[x]:
                res.append(f"{y}")
                p2 += 1
        elif y is not None:
            res.append(y)
            p2 += 1
        elif x is not None:
            res.append(x)
            p1 += 1

    return "".join(res)


s1 = "super"
s2 = "tower"
mergeStrings(s1, s2)
