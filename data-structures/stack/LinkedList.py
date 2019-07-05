class Node:
    def __init__(self):
        self.next = None
        self.item = None

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"{self.item!r}"

    def __eq__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        return self.item == other.item


class LinkedList:
    def __init__(self):
        self.length = 0
        self._head = Node()

    def push(self, item):
        # Code from push / append
        oldHead = self._head
        self._head = Node()
        self._head.item = item
        self._head.next = oldHead
        self.length += 1

    def pop(self):
        # Code that removes top
        self._head = self._head.next
        self.length -= 1

    def top(self):
        # Code that just returns the head
        return self._head

    def size(self):
        return self.length

    def empty(self):
        return self.length == 0

    def __iter__(self):
        current = self._head
        while current is not None:
            yield current
            current = current.next

    def __str__(self):
        return " ".join(str(o) for o in self)


class List(LinkedList):
    def insert(self, item, position):
        current = None
        if position == 0:
            print(f"pos: {position}")
            self.push(item)
            print(self.size())
        else:
            print("here")
            current = self._head
            count = 0
        while current != None:
            if count == position - 2:
                break
            else:
                count += 1
                current = current.next
                print(current)
            newNode = Node()
            newNode.next = item
            newNode.next = current.next
            current.next = newNode


# class Stack(LinkedList):
#     # Whatever functionality is unique to the stack.
#     # If there isn't any, you can consider not having a stack
#     # class and just using a LinkedList.
