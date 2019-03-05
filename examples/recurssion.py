def imperative_linear_search(some_list, some_element):
    for e in some_list:
        if e == some_element:
            return True
    return False


def recursive_linear_search(some_list, some_element):
    print(len(some_list))
    if some_list == []:
        return False
    elif some_list[0] == some_element:  # first element always exists at this point
        return True
    else:
        return recursive_linear_search(some_list[1:], some_element)


my_list = [x for x in range(100)]
print(f"length of list: {len(my_list)}")
print(f"list: {my_list}")

print(recursive_linear_search(my_list, len(my_list) - 1))
