# Given a string, what is the minimum number of adjacent swaps
# required to convert a string into a palindrome.
# If not possible, return -1.

# 1. check if palindrome is possible
# 2. compute palindrome
# 3. check num swaps between original and palindrome

from collections import defaultdict


def is_palindrome(s):
    """
    - a palindrome is the same forward as it is backwards
    - if a palindrome is possible then it has even number of character counts
    except at most 1 for odd length s
    - O(n) where n is length of string s
    """
    count = defaultdict(int)
    for char in s:
        count[char] = count[char] + 1
    even = len(s) % 2 == 0
    exclude = 0
    for k, v in count.items():
        if v % 2 != 0:
            exclude = exclude + 1
        # does not allow addition character that does not have even count
        if even and exclude == 1:
            return False
        # allow additional character that does not have event count
        if not even and exclude > 1:
            return False
    return True


def compute_palindrome(s):
    """
    Create a palindrome from provided string
    - O(n) where n is length of string s
    """
    char_count = defaultdict(int)

    # duplicate of is_palindrome, could extract to get charCount or use Counter
    for c in s:
        char_count[c] = char_count[c] + 1

    # beginning and end string
    res = ""
    # middle char
    middle = ""
    for char in s:
        if char_count[char] != 0:
            # middle char
            if char_count[char] == 1:
                middle = char
                char_count[char] -= 1
            else:
                res += char
                char_count[char] -= 2

    return res + middle + res[-1::-1]


def min_swaps(s, p):
    """
    compare 2 strings with identical char counts
    check how many swaps to make strings match
    - O(n^2) looping each character and max swaps n times for each
    """
    s = list(s)
    p = list(p)
    i, j, swaps = 0, 0, 0
    for i in range(0, len(s)):
        j = i
        # find first char that equals s[i]
        while s[i] != p[j]:
            j = j + 1

        # adjacent swaps
        while i < j:
            temp = p[j]
            p[j] = p[j - 1]
            p[j - 1] = temp
            j = j - 1
            swaps = swaps + 1
    return swaps


def swap(s):
    if not is_palindrome(s):
        return -1

    p = compute_palindrome(s)
    print(s, p)
    swaps = min_swaps(s, p)
    return swaps


print(swap("mamad"))  # 3
print(swap("asflkj"))  # -1
print(swap("aabb"))  # 2
print(swap("ntiin"))  # 1
