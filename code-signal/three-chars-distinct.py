def three_chars_distinct(s):
    count = 0
    for i in range(0, len(s) - 2):
        if (s[i] is not s[i + 1]) and (s[i] is not s[i + 2]) and (s[i + 1] is not s[i + 2]):
            count += 1
    return count


print(three_chars_distinct("abccb"))
