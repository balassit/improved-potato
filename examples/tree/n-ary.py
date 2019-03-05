class Node:
    def __init__(self, val):
        self.val = val
        self.children = []


from collections import deque


def preorder(root):
    if not root:
        return []
    preorder_list = [root.val]
    stack = deque([root])
    hash_visited = {root: 1}

    while stack:
        top = stack.pop()
        if top.children:
            for child in top.children:
                if child not in hash_visited:
                    hash_visited[child] = 1
                    preorder_list.append(child.val)
                    stack.append(top)
                    stack.append(child)
                    break

    return preorder_list


def postorder(root):
    if not root:
        return []
    nodes = []
    result = []
    nodes.append(root)
    while nodes:
        r = nodes.pop()
        result.append(r.val)
        if r.children:
            nodes.extend(r.children)
    result.reverse()
    return result


# # Driver Program

#     """   Let us create below tree
#     *              10
#     *        /   /    \   \
#     *        2  34    56   100
#     *                 |   /  | \
#     *                 1   7  8  9
#     """

root = Node(10)
root.children.append(Node(2))
root.children.append(Node(34))
root.children.append(Node(56))
root.children.append(Node(100))
root.children[2].children.append(Node(1))
root.children[3].children.append(Node(7))
root.children[3].children.append(Node(8))
root.children[3].children.append(Node(9))

print("pre order")
print(preorder(root))

print("post order")
print(postorder(root))
