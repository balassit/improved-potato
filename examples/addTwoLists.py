class Node:
    def __init__(self, data=None):
        self.next = None
        self.data = data


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


def addLists(l1, l2):
    curr1 = l1.root
    curr2 = l2.root
    carry = 0
    value = 0
    sum = LinkedList()
    while curr1 or curr2:
        if curr1 and curr2:
            value = curr1.data + curr2.data + carry

            curr1 = curr1.next
            curr2 = curr2.next

        elif curr1 is None and curr2 is not None:
            value = curr2.data + carry
            curr2 = curr2.next

        elif curr2 is None and curr1 is not None:
            value = curr1.data + carry
            curr1 = curr1.next

        carry = value // 10
        value = value % 10
        sum.insert(value)

    return sum


if __name__ == "__main__":
    l1 = LinkedList()
    l1.insert(10)
    l1.insert(0)
    l1.insert(4)
    l2 = LinkedList()
    l2.insert(3)
    l2.insert(2)

    sum = addLists(l1, l2)
    print([node.data for node in sum])
