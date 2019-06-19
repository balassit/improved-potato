"""
@param items - list of ints
@return sorted list of items
"""


def insertion_sort(items: list):
    for index in range(1, len(items)):
        current = items[index]
        position = index

        while position > 0 and items[position - 1] > current:
            items[position] = items[position - 1]
            position -= 1

        items[position] = current

    return items


"""
Sort a given list and print before and after. Assume list is integers
"""
if __name__ == "__main__":
    items: list = [54, 26, 93, 17]
    print(f"before sorting: {items}")
    items = insertion_sort(items)
    print(f"after sorting: {items}")
