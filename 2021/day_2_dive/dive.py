with open('puzzle_input.txt') as file:
    instructions = [line.strip() for line in file]

# PART 1
horizontal_position, depth = 0, 0

for instruction in instructions:
    direction, value = instruction.split()
    value = int(value)

    if direction == "forward":
        horizontal_position += value
    elif direction == "down":
        depth += value
    elif direction == "up":
        depth -= value

print(f"Position: {horizontal_position}, Depth: {depth}. Product: {horizontal_position * depth}")

# PART 2

horizontal_position, depth, aim = 0, 0, 0

for instruction in instructions:
    direction, value = instruction.split()
    value = int(value)

    if direction == "down":
        aim += value
    elif direction == "up":
        aim -= value
    elif direction == "forward":
        horizontal_position += value
        depth += aim * value

print(f"Position: {horizontal_position}, Depth: {depth}. Product: {horizontal_position * depth}")
