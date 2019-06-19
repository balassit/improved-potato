def quick_sort(items):
    sort(items, 0, len(items) - 1)
    return items


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


"""
Sort a given list and print before and after. Assume list is integers
"""
if __name__ == "__main__":
    items: list = [54, 26, 93, 17]
    print(f"before sorting: {items}")
    items = quick_sort(items)
    print(f"after sorting: {items}")
