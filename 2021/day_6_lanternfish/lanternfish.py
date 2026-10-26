with open('puzzle_input.txt') as file:
    fish = [int(x) for x in file.read().strip().split(',')]

part_1_days = 80
part_2_days = 256

fish_counts = [0] * 9

for f in fish:
    fish_counts[f] += 1

def simulate_days(fish_counts, days):
    counts = fish_counts[:]

    for _ in range(days):
        new_fish = counts[0]

        for i in range(1, 9):
            counts[i - 1] = counts[i]

        counts[6] += new_fish
        counts[8] = new_fish

    return sum(counts)

print("Part 1:", simulate_days(fish_counts, part_1_days))
print("Part 2:", simulate_days(fish_counts, part_2_days))
