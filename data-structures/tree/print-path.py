class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


"""
Function to check if there is a path from root to the given node.
It also populates 'arr' with the given path  
"""


def get_path(root, rarr, x):
    if not root:
        return False

    # push the node's value in 'arr'
    rarr.append(root.data)

    # if it is the required node return true
    if root.data == x:
        return True

    # check whether the required node lies in the
    # left subtree or right subtree of the current node
    if get_path(root.left, rarr, x) or get_path(root.right, rarr, x):
        return True

    # required node does not lie either in the
    # left or right subtree of the current node
    # Thus, remove current node's value from
    # 'arr'and then return false
    rarr.pop()
    return False


def get_path_between_nodes(root, node1, node2):
    # vector to store the path of first and second nodes from root
    path1, path2 = [], []
    get_path(root, path1, node1)
    get_path(root, path2, node2)

    # Get intersection point
    i, j = 0, 0
    intersection = 0
    while i < len(path1) or j < len(path2):
        # Keep moving forward until no intersection is found
        if path1[i] == path2[j]:
            i, j = i + 1, j + 1
        else:
            intersection = j - 1
            break

    for i in range(len(path1) - 1, intersection - 1, -1):
        yield path1[i]
    for j in range(intersection + 1, len(path2)):
        yield path2[j]


# Driver program
if __name__ == "__main__":

    # binary tree formation
    root = Node(0)
    root.left = Node(1)
    root.left.left = Node(3)
    root.left.left.left = Node(7)
    root.left.right = Node(4)
    root.left.right.left = Node(8)
    root.left.right.right = Node(9)
    root.right = Node(2)
    root.right.left = Node(5)
    root.right.right = Node(6)
    node1 = 7
    node2 = 4
    print(list(get_path_between_nodes(root, node1, node2)))
