from queue import PriorityQueue

list1 = [3, 6]
list2 = [1, 5]
list3 = [2, 4]


def merge_k_lists(lists):
    q = PriorityQueue()
    res = []

    for idx in range(len(lists)):
        for i in range(len(lists[idx])):
            q.put(lists[idx][i])

    while not q.empty():
        res.append(q.get())

    return res


"""
def merge_lists(list1, list2):
    idx1, idx2 = 0, 0
    res = []
    while idx1 < len(list1) and idx2 < len(list2):
        if list1[idx1] < list2[idx2]:
            res.append(list1[idx1])
            idx1 += 1 
            
        else:
            res.append(list2[idx2])
            idx2 += 1
            
    if idx2 < len(list2):
        res.extend(list2[idx2:])
    
    elif idx1 < len(list1):
        res.extend(list1[idx1:])
            
    return res

print(merge_lists(list1, list2))
"""

print(merge_k_lists([list1, list2, list3]))
