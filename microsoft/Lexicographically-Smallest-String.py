def removeLargest(s):
    """
    Remove the lexicographically largest char from string
    O(n) - iterate list twice, once to find, once to remove using list.pop(index)
    """
    s = list(s)
    largest = (0, s[0])
    for i, v in enumerate(s):
        if largest[1] < v:
            largest = (i, v)
    # res = [x for i, x in enumerate(s) if i != largest[0]]
    # return "".join(res)
    s.pop(largest[0])
    return "".join(s)


print(removeLargest("abyzde"))
