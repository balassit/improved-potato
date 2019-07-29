def is_unique(s):
    s = sorted(list(s))
    for i in range(0, len(s) - 1):

        if s[i] == s[i + 1]:
            return False
    return True


def is_permuatation(s1, s2):
    """
    permuatation means has the same characters
    """
    return sorted(list(s1)) == sorted(list(s2))


def urlify(s, size):
    s = list(s)
    n = len(s) - 1
    print(s)
    for i in range(size - 1, 0, -1):
        print(f"_{s[i]}_")
        if s[i] == " ":
            s[n] = s[i]
            # s[n] = "0"
            # s[n-1] = "2"
            # s[n-2] = "%"
            # n -= 3
        else:
            s[n] = s[i]
            n -= 1
    print(s)


# is_unique
print("is_unique:", is_unique("her"))
print("is_unique:", is_unique("apple"))
# is_permuatation
print("is_permuatation:", is_permuatation("abc", "cba"))

print("urlify:", urlify("Mr John Smith    ", 13))
