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

    def get_height(self, node):
        if node is None:
            return 0
        else:
            return max(self.get_height(node.left), self.get_height(node.right)) + 1

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


# without stack or recurssion
# https://www.geeksforgeeks.org/inorder-non-threaded-binary-tree-traversal-without-recursion-or-stack/


def validate_bst(t):
    if not t:
        return True
    s = list()
    prev = None
    while t or s:
        while t:
            s.append(t)
            t = t.left
        t = s.pop()

        if prev and prev.key >= t.key:
            return False
        prev = t
        t = t.right
    return True


def kth_smallest(t, k):
    if not t:
        return True
    s = list()
    while t or s:
        while t:
            s.append(t)
            t = t.left
        t = s.pop()

        k -= 1
        if k == 0:
            return t.data
        t = t.right
    return -1


# inorder traversal given the root node
def inorder(t):
    if t:
        yield from inorder(t.left)
        yield t.key
        yield from inorder(t.right)


def inorder_iterative(t):
    if not t:
        return None
    s = list()
    res = list()
    while t or s:
        while t:
            s.append(t)
            t = t.left
        t = s.pop()
        res.append(t)
        t = t.right
    return res


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


def sorted_arr_to_bst(arr):
    if not arr:
        return None

    # find middle
    mid = (len(arr)) // 2

    # make the middle element the root
    root = Node(arr[mid], arr[mid])

    # left subtree of root has all
    # values <arr[mid]
    root.left = sorted_arr_to_bst(arr[:mid])

    # right subtree of root has all
    # values >arr[mid]
    root.right = sorted_arr_to_bst(arr[mid + 1 :])
    return root


def create_tree_in_order_pre_order(inorder_arr, preorder_arr):
    if len(inorder_arr) == 1:
        root = Node(inorder_arr[0], inorder_arr[0])

    for i, v in enumerate(preorder_arr):
        root = Node(v, v)
        index = inorder_arr.index(v)
        left = inorder_arr[:index]
        right = inorder_arr[index + 1 :]
        create_tree_in_order_pre_order(left, preorder_arr[i:])
        create_tree_in_order_pre_order(right, preorder_arr[i:])

        print(v, left, right)


def constructFromPrePost(self, pre, post):
    stack = [Node(pre[0])]
    j = 0
    for v in pre[1:]:
        node = Node(v)
        print("node", v)
        while stack[-1].val == post[j]:
            print("here", stack[-1].val)
            stack.pop()
            j += 1
        if not stack[-1].left:
            print("left", stack[-1].val, node.val)
            stack[-1].left = node
        else:
            print("right", stack[-1].val, node.val)
            stack[-1].right = node
        stack.append(node)
        for a in stack:
            print(a.val, end=" ")
        print()
    return stack[0]


# tree = Tree()
# tree.root = Node(9,9)
# tree.root.left = Node(10,10)
# tree.root.right = Node(2,2)
# tree.root.left.left = Node(1,1)
# tree.root.left.right = Node(3,3)

arr = [1, 4, 5, 7, 8, 9]
tree = Tree()
tree.root = sorted_arr_to_bst(arr)

print("3rd smallest: ", kth_smallest(tree.root, 3))

print("in order")
print(inorder_iterative(tree.root))
print("valid BST: ", validate_bst(tree.root))
# a = [n for n in inorder(tree.root)]
# print(a)

# print("pre order")
# a = [n for n in preorder(tree.root)]
# print(a)

# print("post order")
# a = [n for n in postorder(tree.root)]
# print(a)

# print("Breadth first search")
# a = [n for n in bfs(tree.root)]
# print(a)

# print("DFS left to right")
# a = [n for n in dfs(tree.root, chooser=left_then_right)]
# print(a)

# print("DFS right to left")
# a = [n for n in dfs(tree.root, chooser=right_then_left)]
# print(a)

# print("Binary search DFS")
# a = [n for n in dfs(tree.root, binary_search_chooser(6))]
# print(a)

# print("height", tree.get_height(tree.root))

# inorder_arr = [23,18,17,4,3,13,26]
# preorder_arr = [3,17,18,23,4,13,26]
# root = create_tree_in_order_pre_order(inorder_arr, preorder_arr)
