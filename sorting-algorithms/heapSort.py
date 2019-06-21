# To heapify subtree rooted at index i.
# n is size of heap
def heapify(items, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and items[i] < items[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and items[largest] < items[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        items[i], items[largest] = items[largest], items[i]  # swap

        # Heapify the root.
        heapify(items, n, largest)


# The main function to sort an items of given size
def heap_sort(items):
    n = len(items)

    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(items, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        items[i], items[0] = items[0], items[i]  # swap
        heapify(items, i, 0)


"""
Sort a given list and print before and after. Assume list is integers
"""
if __name__ == "__main__":
    items: list = [54, 26, 93, 17]
    print(f"before sorting: {items}")
    heap_sort(items)
    print(f"after sorting: {items}")
