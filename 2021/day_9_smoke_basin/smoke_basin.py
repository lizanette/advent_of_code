import heapq
import math

with open("puzzle_input.txt") as file:
    heightmap = [[int(char) for char in line.strip()] for line in file]

rows, cols = len(heightmap), len(heightmap[0])
coords = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def get_neighbors(row, col):
    for dr, dc in coords:
        new_row, new_col = row + dr, col + dc

        if 0 <= new_row < rows and 0 <= new_col < cols:
            yield new_row, new_col

# PART 1:
low_points = []
for row in range(rows):
    for col in range(cols):
        if all(
            heightmap[row][col] < heightmap[n_row][n_col]
            for n_row, n_col in get_neighbors(row, col)
        ):
            low_points.append((row, col))

risk_level_sum = sum(heightmap[row][col] + 1 for row, col in low_points)
print(f"Part 1 --- Risk level sum: {risk_level_sum}")

# Part 2
def find_basin_size(row, col):
    heightmap[row][col] = 9
    stack = [(row, col)]
    basin_size = 0

    while stack:
        r, c = stack.pop()
        basin_size += 1

        for neighbor_row, neighbor_col in get_neighbors(r, c):
            if heightmap[neighbor_row][neighbor_col] != 9:
                heightmap[neighbor_row][neighbor_col] = 9
                stack.append((neighbor_row, neighbor_col))

    return basin_size

basin_sizes = [find_basin_size(row, col) for row, col in low_points]
product = math.prod(heapq.nlargest(3, basin_sizes))

print(f"Part 2 --- Product of the sizes of the three largest basins: {product}")
