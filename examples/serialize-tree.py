"""
O(n) time and O(n) space, BFS traversal
e.g., 1
     / \
    2   5
   / \
  3   4 
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Encodes a tree to a single string.
def serialize(root):
    sb = []
    build_string(root, sb)
    return "".join(map(str, sb))


def build_string(node, sb):
    if node is None:
        sb.append("X")
        sb.append(",")
    else:
        sb.append(node.val)
        sb.append(",")
        build_string(node.left, sb)
        build_string(node.right, sb)


# Decodes your encoded data to tree.
def deserialize(data):
    nodes = []
    nodes.extend(data.split(","))
    print(nodes)
    return build_tree(nodes)


def build_tree(nodes):
    val = nodes.pop(0)
    if val == "X":
        return None
    else:
        node = TreeNode(val)
        node.left = build_tree(nodes)
        node.right = build_tree(nodes)
        return node


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
print((serialize(root)))
