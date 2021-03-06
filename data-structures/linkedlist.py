import typing


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.root = None
        self.length = 0

    def __iter__(self):
        node = self.root
        while node:
            yield node
            node = node.next

    def insert(self, data: Node):
        if not isinstance(data, Node):
            next_node = Node(data)
        if self.root is None:
            self.root = next_node
            return
        current = self.root
        while current.next:
            current = current.next
        current.next = next_node
        self.length += 1

    def get(self, value):
        current = self.root
        while current:
            if current.data == value:
                return True
            current = current.next
        return False

    def delete(self, value):
        prev = None
        curr = self.root
        while curr:
            if curr.data == value:
                if prev:
                    prev.next = curr.next
                else:
                    self.root = curr.next
                return True
            prev = curr
            curr = curr.next
        return False


def delete_dups(node):
    items = set()
    while node is not None:
        if node.data not in items:
            items.add(node.data)
        node = node.next
    print(items)


def kth_to_last(node, k):
    curr = node
    if node is None:
        return None
    curr = node
    for _ in range(k):
        if curr is None:
            return None
        curr = curr.next
    while curr is not None:
        curr = curr.next
        node = node.next
    return node.data


l = LinkedList()
l.insert(1)
l.insert(2)
l.insert(8)
l.insert(3)
l.insert(7)
l.insert(0)
l.insert(4)
print([node.data for node in l])

# delete_dups(l.root)
print(kth_to_last(l.root, 3))
