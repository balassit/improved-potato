# Python 3 program to demonstrate implementation
# of k stacks in a single array in time and space
# efficient way


class KStacks:
    def __init__(self, k, n):
        self.k = k  # Number of stacks.
        self.n = n  # Total size of array holding
        # all the 'k' stacks.

        # Array which holds 'k' stacks.
        self.arr = [0] * self.n

        # All stacks are empty to begin with
        # (-1 denotes stack is empty).
        self.top = [-1] * self.k

        # Top of the free stack.
        self.free = 0

        # Points to the next element in either
        # 1. One of the 'k' stacks or,
        # 2. The 'free' stack.
        self.next = [i + 1 for i in range(self.n)]
        self.next[self.n - 1] = -1

    # Check whether given stack is empty.
    def is_empty(self, sn):
        return self.top[sn] == -1

    # Check whether there is space left for
    # pushing new elements or not.
    def is_full(self):
        return self.free == -1

    # Push 'item' onto given stack number 'sn'.
    def push(self, item, sn):
        if self.is_full():
            print("Stack Overflow")
            return

        # Get the first free position
        # to insert at.
        insert_at = self.free

        # Adjust the free position.
        self.free = self.next[self.free]

        # Insert the item at the free
        # position we obtained above.
        self.arr[insert_at] = item

        # Adjust next to point to the old
        # top of stack element.
        self.next[insert_at] = self.top[sn]
        # Set the new top of the stack.
        self.top[sn] = insert_at

    # Pop item from given stack number 'sn'.
    def pop(self, sn):
        if self.is_empty(sn):
            return None

        # Get the item at the top of the stack.
        top_of_stack = self.top[sn]

        # Set new top of stack.
        self.top[sn] = self.next[self.top[sn]]

        # Push the old top_of_stack to
        # the 'free' stack.
        self.next[top_of_stack] = self.free
        self.free = top_of_stack

        return self.arr[top_of_stack]


# Driver Code
if __name__ == "__main__":

    # Create 3 stacks using an
    # array of size 10.
    kstacks = KStacks(3, 10)
    print(kstacks.next)

    # Push some items onto stack number 2.
    kstacks.push(15, 2)
    kstacks.push(45, 2)

    # Push some items onto stack number 1.
    kstacks.push(17, 1)
    kstacks.push(49, 1)
    kstacks.push(39, 1)

    # Push some items onto stack number 0.
    kstacks.push(11, 0)
    kstacks.push(9, 0)
    kstacks.push(7, 0)

    print("Popped element from stack 2 is " + str(kstacks.pop(2)))
    print("Popped element from stack 1 is " + str(kstacks.pop(1)))
    print("Popped element from stack 0 is " + str(kstacks.pop(0)))


class Stack:
    def __init__(self):
        self.items = deque()

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


print("STACK")
stack = Stack()

stack.push("eat")
stack.push("sleep")
stack.push("code")
print(stack.items)
print(stack.pop())
print(stack.items)

from collections import deque


class Queue:
    def __init__(self):
        self._queue = deque()

    def enqueue(self, item):
        self._queue.appendleft(item)

    def dequeue(self):
        return self._queue.pop()


print("QUEUE")
queue = Queue()
queue.enqueue("eat")
queue.enqueue("sleep")
queue.enqueue("code")
print(queue._queue)
print(queue.dequeue())
print(queue._queue)
