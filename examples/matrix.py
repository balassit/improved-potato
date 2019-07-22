def updateMatrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # left-top
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j]:
                top = matrix[i - 1][j] + 1 if i > 0 else float("inf")
                left = matrix[i][j - 1] + 1 if j > 0 else float("inf")
                matrix[i][j] = min(top, left)

    # bottom-right
    for i in range(rows - 1, -1, -1):
        for j in range(cols - 1, -1, -1):
            if matrix[i][j]:
                bottom = matrix[i + 1][j] + 1 if i < rows - 1 else float("inf")
                right = matrix[i][j + 1] + 1 if j < cols - 1 else float("inf")
                matrix[i][j] = min(matrix[i][j], bottom, right)

    return matrix


m = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
print(updateMatrix(m))
