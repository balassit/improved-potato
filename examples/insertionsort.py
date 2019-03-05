def insertion_sort(items):
    for i in range(1, len(items)):
        current = items[i]
        while i > 0 and items[i - 1] > current:
            items[i] = items[i - 1]
            i -= 1
        items[i] = current
    return items


print(insertion_sort([1, 2, 3, 4]))
for i in range(5, 0, -1):
    print(i)
