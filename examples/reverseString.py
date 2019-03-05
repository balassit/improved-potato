import timeit


def reverse_string(string):
    # create a list of the chars
    chars = list(s)
    for i, val in enumerate(s):
        if i == len(s) // 2:
            break
        tmp = val
        chars[i] = chars[len(s) - i - 1]
        chars[len(s) - i - 1] = tmp
    return "".join(chars)


def reverse_string2(string):
    # create a list of the chars
    chars = list(s)
    for i in range(len(s) // 2):
        tmp = chars[i]
        chars[i] = chars[len(s) - i - 1]
        chars[len(s) - i - 1] = tmp
    return "".join(chars)


s = "abcdefghijklmnopqrstuvwxyz" * 10
# print(timeit.repeat(lambda: s[::-1]))
print(reverse_string(s))
# print(reverse_string2(s))
