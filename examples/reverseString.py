import timeit


def reverse_string(string):
    # create a list of the chars
    chars = list(s)
    for i in range(len(s) // 2):
        chars[i], chars[len(s) - i - 1] = chars[len(s) - i - 1], chars[i]
    return "".join(chars)


s = "abcdefghijklmnopqrstuvwxyz" * 10
# print(timeit.repeat(lambda: s[::-1]))
print(reverse_string(s))
# print(reverse_string2(s))
