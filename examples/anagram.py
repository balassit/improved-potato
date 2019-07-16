from collections import Counter


class Solution:
    def isAnagram(self, s, t):
        return Counter(s) == Counter(t)


if __name__ == "__main__":
    sol = Solution()
    print(sol.isAnagram("a", "ab"))
