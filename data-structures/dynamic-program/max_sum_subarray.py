from typing import List


def max_sum(A: List[int]) -> int:
    max_seen = max_end = 0
    for a in A:
        max_end = max(a, a + max_end)
        max_seen = max(max_end, max_seen)
    return max_seen


if __name__ == "__main__":
    print(max_sum([904,40,523,12,-355,-385,-124,481,-31]))
