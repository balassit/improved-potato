# Document classes and functions with docstrings instead of comments
class Node:
    def __init__(self, key, data, left=None, right=None, parent=None):
        self.left = left
        self.right = right
        self.key = key
        self.data = data
        self.parent = parent

    def hasLeftChild(self):
        return self.left

    def hasRightChild(self):
        return self.right

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.right or self.left)

    def hasAnyChildren(self):
        return self.right or self.left

    def hasBothChildren(self):
        return self.right and self.left

    def __repr__(self):
        return "%s" % self.data


class Tree:
    def __init__(self):
        self.root = None
        self.size = 0

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.data
            else:
                return None
        else:
            return None

    def _get(self, key, current_node):
        if not current_node:
            return None
        elif current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self._get(key, current_node.left)
        else:
            return self._get(key, current_node.right)

    def __getitem__(self, key):
        return self.get(key)

    def _put(self, key, data, current_node):
        if key < current_node.key:
            if current_node.hasLeftChild():
                self._put(key, data, current_node.left)
            else:
                current_node.left = Node(key, data, parent=current_node)
        else:
            if current_node.hasRightChild():
                self._put(key, data, current_node.right)
            else:
                current_node.right = Node(key, data, parent=current_node)

    def put(self, key, data):
        # init case no root
        if self.root:
            self._put(key, data, self.root)
        else:
            self.root = Node(key, data)
        self.size += 1

    def __setitem__(self, k, v):
        self.put(k, v)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False


###################################
#  Depth first search             #
# Order can be given as searching #
# from left to right              #
# or right to left                #
###################################


def left_then_right(t):
    if t is not None:
        yield t.left
        yield t.right


def right_then_left(t):
    if t is not None:
        yield t.right
        yield t.left


def dfs(t, chooser=left_then_right):
    if t:
        yield t.key
        for immediate_child in chooser(t):
            yield from dfs(immediate_child, chooser)


def bfs(t):
    """In BFS the Node Values at each level of the Tree are traversed before going to next level"""
    to_visit = [t]
    while to_visit:
        current = to_visit.pop(0)
        yield current
        if current.left:
            to_visit.append(current.left)
        if current.right:
            to_visit.append(current.right)


def binary_search_chooser(value):
    def binary_search_chooser_inner(t):
        if t is not None and t.key is not None:
            if str(value) <= str(t.key):
                yield t.left
            else:
                yield t.right

    return binary_search_chooser_inner


# inorder traversal given the root node
def inorder(t):
    if t:
        yield from inorder(t.left)
        yield t.key
        yield from inorder(t.right)


# pre-order traversal given the root node
def preorder(t):
    if t:
        yield t.key
        yield from preorder(t.left)
        yield from preorder(t.right)


# post-order traversal given the root node
def postorder(t):
    if t:
        yield from postorder(t.left)
        yield from postorder(t.right)
        yield t.key


tree = Tree()
tree["j"] = "j"
tree["f"] = "f"
tree["a"] = "a"
tree["d"] = "d"
tree["h"] = "h"
tree["k"] = "k"
tree["z"] = "z"


print("in order")
a = [n for n in inorder(tree.root)]
print(a)

print("pre order")
a = [n for n in preorder(tree.root)]
print(a)

print("post order")
a = [n for n in postorder(tree.root)]
print(a)

print("Breadth first search")
a = [n for n in bfs(tree.root)]
print(a)

print("DFS left to right")
a = [n for n in dfs(tree.root, chooser=left_then_right)]
print(a)

print("DFS right to left")
a = [n for n in dfs(tree.root, chooser=right_then_left)]
print(a)

print("Binary search DFS")
a = [n for n in dfs(tree.root, binary_search_chooser(6))]
print(a)
