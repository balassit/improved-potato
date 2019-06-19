"""
@param items - list of ints
@return sorted list of items
"""


def selection_sort(items: list):
    for index in range(len(items)):
        min_idx = index
        for j in range(index + 1, len(items)):
            if items[min_idx] > items[j]:
                min_idx = j

        # Swap the found minimum element with
        # the first element
        items[index], items[min_idx] = items[min_idx], items[index]

    return items


"""
Sort a given list and print before and after. Assume list is integers
"""
if __name__ == "__main__":
    items: list = [54, 26, 93, 17]
    print(f"before sorting: {items}")
    items = selection_sort(items)
    print(f"after sorting: {items}")
