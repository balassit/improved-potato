def is_safe(mat, visited, row, col):
    """
    verify that the position is either a 0 or * and that it has not been visited yetl
    """
    return (mat[row][col] == 0 or mat[row][col] == "*") and ((row, col)) not in visited


def is_valid(row, col):
    """
    verify that the position is inbounds the grid
    """
    return row < rows and col < cols and row >= 0 and col >= 0


def find_shortest_path(matrix, start):
    """
    return the location of the found vertex, number of vertexes visited, shortest path to the location
    """
    count = 0
    q = [(start, [start])]
    # construct a set to keep track of visited cells
    visited = set()
    while q:
        vertex, path = q.pop(0)
        i, j = vertex[0], vertex[1]
        visited.add((i, j))
        count += 1

        if matrix[i][j] == "*":
            return (i, j), count, path

        if is_valid(i + 1, j) and is_safe(matrix, visited, i + 1, j):
            next_node = (i + 1, j)
            q.append((next_node, path + [next_node]))
            visited.add(next_node)

        if is_valid(i - 1, j) and is_safe(matrix, visited, i - 1, j):
            next_node = (i - 1, j)
            q.append((next_node, path + [next_node]))
            visited.add(next_node)

        if is_valid(i, j + 1) and is_safe(matrix, visited, i, j + 1):
            next_node = (i, j + 1)
            q.append((next_node, path + [next_node]))
            visited.add(next_node)

        if is_valid(i, j - 1) and is_safe(matrix, visited, i, j - 1):
            next_node = (i, j - 1)
            q.append((next_node, path + [next_node]))
            visited.add(next_node)


rows = cols = 4
mat = [[0, 0, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 0, "*", 1]]
start = (0, 0)

print(find_shortest_path(mat, start))
