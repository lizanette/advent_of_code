with open('puzzle_input.txt') as file:
    depths = [int(line.strip()) for line in file]

# PART 1
slow, fast = 0, 1
depth_increases = 0

while fast < len(depths):
    if depths[fast] > depths[slow]:
        depth_increases += 1
    slow += 1
    fast += 1

print(f"Number of depth increases: {depth_increases}")

# PART 2
left = 1
right = 4
depth_increases = 0

prev_sum = sum(depths[0:3])

while right <= len(depths):
    current_sum = sum(depths[left:right])

    if current_sum > prev_sum:
        depth_increases += 1

    prev_sum = current_sum
    left += 1
    right += 1

print(f"Number of sliding window increases: {depth_increases}")
