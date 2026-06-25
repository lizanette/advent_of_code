from collections import deque

octopus = [
  [3, 1, 1, 3, 2, 8, 4, 8, 8, 6],
  [2, 8, 5, 1, 8, 7, 6, 1, 4, 4],
  [2, 7, 7, 4, 6, 6, 4, 4, 8, 4],
  [6, 7, 1, 5, 1, 1, 2, 5, 7, 8],
  [7, 1, 4, 6, 2, 7, 2, 1, 5, 3],
  [6, 2, 5, 6, 6, 5, 6, 3, 6, 7],
  [3, 1, 4, 8, 6, 6, 6, 2, 4, 5],
  [3, 8, 5, 7, 4, 4, 6, 5, 2, 8],
  [7, 3, 2, 2, 4, 2, 2, 8, 3, 3],
  [8, 1, 5, 2, 1, 7, 5, 1, 6, 8],
]

# octopus = [
#   [5, 4,8, 3, 1, 4, 3, 2, 2, 3],
#   [2, 7,4, 5, 8, 5, 4, 7, 1, 1],
#   [5, 2,6, 4, 5, 5, 6, 1, 7, 3],
#   [6, 1,4, 1, 3, 3, 6, 1, 4, 6],
#   [6, 3,5, 7, 3, 8, 5, 4, 7, 8],
#   [4, 1,6, 7, 5, 2, 4, 6, 4, 5],
#   [2, 1,7, 6, 8, 4, 1, 7, 2, 1],
#   [6, 8,8, 2, 8, 8, 1, 1, 3, 4],
#   [4, 8,4, 6, 8, 4, 8, 5, 5, 4],
#   [5, 2,8, 3, 7, 5, 1, 5, 2, 6],
# ]

# octopus = [
#   [6, 9, 8, 8, 8, 8, 8, 8, 8, 8],
#   [9, 9, 8, 8, 8, 8, 8, 8, 8, 8],
#   [8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
#   [8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
#   [8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
#   [8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
#   [8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
#   [8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
#   [8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
#   [8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
# ]

num_steps = 100
step = 1
flashes = 0

num_rows = len(octopus)
num_cols = len(octopus[0])

coords = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

for row in range(num_rows):
    print(octopus[row])

def get_neighbors(row, col):
  neighbors = []

  for dx, dy in coords:
    neighbor_row = row + dx
    neighbor_col = col + dy

    if 0 <= neighbor_row < num_rows and 0 <= neighbor_col < num_cols and octopus[neighbor_row][neighbor_col] <= 9:
      neighbors.append([neighbor_row, neighbor_col])

  return neighbors

while step <= num_steps:
  queue = deque([])

  for row in range(num_rows):
    for col in range(num_cols):
      octopus[row][col] += 1

      if octopus[row][col] > 9:
        flashes += 1
        queue.append((row, col))

  while len(queue) > 0:
    level_len = len(queue)

    for _ in range(level_len):
      r, c = queue.popleft()

      for neighbor_row, neighbor_col in get_neighbors(r, c):
        octopus[neighbor_row][neighbor_col] += 1

        if octopus[neighbor_row][neighbor_col] > 9:
          flashes += 1
          queue.append((neighbor_row, neighbor_col))

  for row in range(num_rows):
    for col in range(num_cols):
      if octopus[row][col] > 9:
        octopus[row][col] = 0

  step += 1

print(f"\nAfter {num_steps} steps:")
for row in range(num_rows):
    print(octopus[row])

print("TOTAL FLASHES: ", flashes)
