class Node:
    def __init__(self, key, data, left=None, right=None):
        self.left = left
        self.right = right
        self.key = key
        self.data = data

    def __repr__(self):
        return "%s" % self.data


def print_level_order(root):
    currentLevel = list()
    nextLevel = list()
    currentLevel.append(root)
    level = 0
    while len(currentLevel) > 0:
        for node in currentLevel:
            print(f"{node.data}", end=" ")
        nextLevel.clear()
        for i in reversed(range(len(currentLevel))):
            left = currentLevel[i].left
            right = currentLevel[i].right
            # right to left
            if level % 2 == 0:
                if left is not None:
                    nextLevel.append(left)
                if right is not None:
                    nextLevel.append(right)
            # left to right
            else:
                if right is not None:
                    nextLevel.append(right)
                if left is not None:
                    nextLevel.append(left)
        currentLevel.clear()
        currentLevel.extend(nextLevel)
        level += 1


if __name__ == "__main__":
    root = Node(0, 0)
    root.left = Node(1, 1)
    root.right = Node(2, 2)
    root.left.left = Node(3, 3)
    root.left.right = Node(4, 4)
    root.right.left = Node(5, 5)
    root.right.right = Node(6, 6)

    print_level_order(root)
