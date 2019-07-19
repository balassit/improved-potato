import sys


def maxOverlap(start, end):
    max_end = max(end)
    x = (max_end + 2) * [0]  # size of max val + 2
    cur = idx = 0

    # CREATING AN AUXILIARY ARRAY
    for i in range(0, len(start)):
        x[start[i]] += 1  # Lazy addition
        x[end[i] + 1] -= 1
        print(start[i], end[i])

    maxy = -1
    # Lazily Calculating value at index i
    for i in range(0, len(x)):
        cur += x[i]
        if maxy < cur:
            maxy = cur
            idx = i
    print(f"Maximum value is: {maxy} at position: {idx}")


if __name__ == "__main__":

    start = [13, 28, 29, 14, 40, 17, 3]
    end = [107, 95, 111, 105, 70, 127, 74]

    maxOverlap(start, end)
