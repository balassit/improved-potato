def quicksort(items):
    sort(items, 0, len(items) - 1)


def sort(items, low, high):
    if low >= high:
        return
    p = partition(items, low, high)
    sort(items, low, p - 1)
    sort(items, p + 1, high)


def partition(items, low, high):
    pivot = items[high]
    for i in range(low, high):
        if items[i] <= pivot:
            items[i], items[low] = items[low], items[i]
            low += 1
    items[low], items[high] = items[high], items[low]
    return low


items = [2, 1, 3, 0, 4, 6, 5, 8, 7, 9]
quicksort(items)
print(items)
