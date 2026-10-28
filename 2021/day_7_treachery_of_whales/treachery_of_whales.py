import math

with open('puzzle_input.txt') as file:
    crabs = [int(x) for x in file.read().strip().split(',')]

def compute_fuel(target_position):
    total = 0
    for crab in crabs:
        total += abs(crab - target_position)

    return total

# Computing the median will always give us the optimal fuel
# Because the fuel cost increases linearly (1 step = 1 fuel),
# the median will always be the exact point that minimizes the sum of absolute differences.
crabs.sort()
mid = (len(crabs) - 1) // 2

print(f"Part 1: Minimum fuel: {compute_fuel(crabs[mid])} at position {crabs[mid]}")


# ----- PART 2 ------
# The mean is the mathematical point that perfectly minimizes the sum of squared differences
mean = sum(crabs) / len(crabs)

mean_rounded_down = math.floor(mean)
mean_rounded_up = math.ceil(mean)

def compute_fuel_part_2(target_position):
    total = 0
    for crab in crabs:
        distance = abs(crab - target_position)
        fuel = distance * (distance + 1) // 2
        total += fuel
    return total

fuel_rounded_down = compute_fuel_part_2(mean_rounded_down)
fuel_rounded_up = compute_fuel_part_2(mean_rounded_up)

min_fuel_part_2 = min(fuel_rounded_down, fuel_rounded_up)

print(f"Part 2 - Minimum fuel: {min_fuel_part_2}")
