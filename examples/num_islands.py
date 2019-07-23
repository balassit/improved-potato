def numIslands(grid):
    visited = set()
    # find all locations with a '1' - O(row * cols)
    for i, row in enumerate(grid):
        for j, _ in enumerate(row):
            if grid[i][j] == "1": visited.add((i, j))

    print(visited)

    num_islands = 0
    while len(visited) > 0:
        adjacent_spots = set()
        vertex = visited.pop()
        adjacent_spots.add(vertex)
        while len(adjacent_spots) > 0:
            vertex = adjacent_spots.pop()
            try: visited.remove(vertex)
            except KeyError: pass  # The first item is already popped
            for neighbor in get_neighbors(vertex, visited):
                adjacent_spots.add(neighbor)
                visited.remove(neighbor)
        num_islands += 1

    return num_islands

def get_neighbors(vertex, visited):
    neighbors_set = set()
    #left
    if (vertex[0] - 1, vertex[1]) in visited:
        neighbors_set.add((vertex[0] - 1, vertex[1]))
    #right
    if ((vertex[0] + 1, vertex[1])) in visited:
        neighbors_set.add((vertex[0] + 1, vertex[1]))
    #top
    if ((vertex[0], vertex[1] + 1)) in visited:
        neighbors_set.add((vertex[0], vertex[1] + 1))
    #bottom
    if ((vertex[0], vertex[1] - 1)) in visited:
        neighbors_set.add((vertex[0], vertex[1] - 1))
    return neighbors_set


grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
print(numIslands(grid))