def sort_diagonal(a):
    n = len(a)

    def get_diagonal_length(row, col):
        # min of row or col length
        return min(n - row, n - col)

    def get_diagonal_values(row, start_col, diag_len):
        diag_values = list()
        for col in range(start_col, diag_len + start_col):
            diag_values.append(a[row][col])
            row += 1
        return diag_values

    def update_diagonal_values(row, start_col, diag_len, diag_values):
        index = 0
        for col in range(start_col, diag_len + start_col):
            a[row][col] = diag_values[index]
            row += 1
            index += 1

    row = 0
    # iterate horizontally starting at 0,0
    for col in range(0, n):
        # get length of diagonal
        diag_len = get_diagonal_length(row, col)
        # get values of diagonal
        diag_values = get_diagonal_values(row, col, diag_len)
        # sort values of diagonal
        diag_values.sort()
        update_diagonal_values(row, col, diag_len, diag_values)

    col = 0
    # iterate vertically starting at 1,0
    for row in range(1, n):
        # get length of diagonal
        diag_len = get_diagonal_length(row, col)
        # get values of diagonal
        diag_values = get_diagonal_values(row, col, diag_len)
        # sort values of diagonal
        diag_values.sort()
        update_diagonal_values(row, col, diag_len, diag_values)


a = [
    [16, 12, 8, 4],  # [ 1, 2, 3, 4]
    [15, 11, 7, 3],  # [ 5, 6, 7, 8]
    [14, 10, 6, 2],  # [9, 10,11,12]
    [13, 9, 5, 1],  # [13,14,15, 16]
]
print(a)
sort_diagonal(a)
print(a)
