def numIslands(grid):
    land = set()
    for i, row in enumerate(grid):
        for j, _ in enumerate(row):
            if grid[i][j] == "1":
                land.add((i, j))

    num_islands = 0
    while land:
        # visited
        v = set()
        current = land.pop()
        if current not in v:
            v.add(current)
        while v:
            spot = v.pop()
            try:
                land.remove(spot)
            except KeyError:
                pass  # The first item is already popped
            for neighbor in get_neighbors(spot, land):
                v.add(neighbor)
                land.remove(neighbor)
        num_islands += 1

    return num_islands


def get_neighbors(spot, land):
    neighbors_set = set()
    if (spot[0] - 1, spot[1]) in land:
        neighbors_set.add((spot[0] - 1, spot[1]))
    if ((spot[0] + 1, spot[1])) in land:
        neighbors_set.add((spot[0] + 1, spot[1]))
    if ((spot[0], spot[1] + 1)) in land:
        neighbors_set.add((spot[0], spot[1] + 1))
    if ((spot[0], spot[1] - 1)) in land:
        neighbors_set.add((spot[0], spot[1] - 1))
    return neighbors_set


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]
print(numIslands(grid))
