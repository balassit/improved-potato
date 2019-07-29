def removeInvalidParentheses(s):
    def dfs(left_rem, right_rem, depth=0, left=0, right=0, cur=""):
        if depth == len(s):
            if left == right and left_rem == right_rem == 0:
                ans.add(cur)
                return

        else:  # s[depth] can only be either a left paren, right paren or a letter
            if s[depth] == "(":
                if left_rem:  # if we can remove a left paren
                    dfs(left_rem - 1, right_rem, depth + 1, left, right, cur)
                dfs(left_rem, right_rem, depth + 1, left + 1, right, cur + "(")  # add left paren
            elif s[depth] == ")":
                if right_rem:  # if we can remove a right paren
                    dfs(left_rem, right_rem - 1, depth + 1, left, right, cur)
                if left > right:
                    dfs(
                        left_rem, right_rem, depth + 1, left, right + 1, cur + ")"
                    )  # add right paren
            else:
                dfs(left_rem, right_rem, depth + 1, left, right, cur + s[depth])  # keep the letter

    left_rem = right_rem = 0
    # determine if there are more lefts or rights
    for c in s:
        if c == "(":
            left_rem += 1
        elif c == ")":
            if left_rem == 0:
                # If not matching left, then this is a misplaced right, record it.
                right_rem += 1
            # balance a pair
            else:
                left_rem -= 1

    ans = set()
    dfs(left_rem, right_rem)
    return list(ans)


print(removeInvalidParentheses("(a)())()"))
