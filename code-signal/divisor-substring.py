def divisor_substring(n, k):
    n_str = str(n)
    count = set()
    for i in range(len(n_str)):
        sub = n_str[i : i + k]
        int_sub = int(sub)
        # end of substring would not have enough
        if len(sub) == k and int_sub != 0 and n % int_sub == 0:
            count.add(sub)
    return len(count)


print(divisor_substring(120, 2))  # 12, 20
