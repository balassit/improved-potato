class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def dfs(root, v):
    global visible
    if not root:
        return

    if root.val >= v:
        visible = visible + 1
        v = max(root.val, v)

    dfs(root.left, v)
    dfs(root.right, v)


visible = 0

root = Node(5)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(20)
root.left.right = Node(21)
root.right.left = Node(1)

# root = Node(-10)
# root.right = Node(-15)
# root.right.right = Node(-1)

dfs(root, -float("inf"))

print(visible)
