class Node:
    """
    represent node that supports n children
    """

    def __init__(self, key):
        self.key = key
        self.child = []


def bfs(t):
    """In BFS the Node Values at each level of the Tree are traversed before going to next level"""
    to_visit = [t]
    while to_visit:
        current = to_visit.pop(0)
        yield current
        for value in current.child:
            to_visit.append(value)


def left_then_right(t):
    if t is not None:
        for value in t.child:
            yield value


def dfs(t, chooser=left_then_right):
    if t:
        yield t.key
        for immediate_child in chooser(t):
            yield from dfs(immediate_child, chooser)


# inorder traversal given the root node
def inorder(t):
    if t:
        yield from inorder(t.left)
        yield t.key
        yield from inorder(t.right)


# pre-order traversal given the root node
from collections import deque


def preorder(root):
    if root is None:
        return []

    preorder_list = [root.key]
    stack = deque([root])
    hash_visited = {root: 1}

    while len(stack) > 0:
        top = stack.pop()
        if top.child:
            for c in top.child:
                if c not in hash_visited:
                    hash_visited[c] = 1
                    preorder_list.append(c.key)
                    stack.append(top)
                    stack.append(c)
                    break
    return preorder_list


# post-order traversal given the root node
def postorder(t):
    if t:
        yield from postorder(t.left)
        yield from postorder(t.right)
        yield t.key


def mirror_tree(root):
    if root is None:
        return
    n = len(root.child)
    if n < 2:
        return
    for i in range(n):
        mirror_tree(root.child[i])
    root.child.reverse()


# # Driver Program

#     """   Let us create below tree
#     *              10
#     *        /   /    \   \
#     *        2  34    56   100
#     *                 |   /  | \
#     *                 1   7  8  9
#     """

root = Node(10)
root.child.append(Node(2))
root.child.append(Node(34))
root.child.append(Node(56))
root.child.append(Node(100))
root.child[2].child.append(Node(1))
root.child[3].child.append(Node(7))
root.child[3].child.append(Node(8))
root.child[3].child.append(Node(9))

print("Level order traversal Before Mirroring")
print("Breadth first search")
a = [n.key for n in bfs(root)]
print(a)
mirror_tree(root)
print("Level order traversal After Mirroring")
a = [n.key for n in bfs(root)]
print(a)
print("DFS left to right")
a = [n for n in dfs(root)]
print(a)

print("pre order")
a = [n for n in preorder(root)]
print(a)
