from collections import Counter

point_counts = Counter()
point_counts_diagonal = Counter()

with open('puzzle_input.txt') as file:
    for line in file:
        line = line.strip()
        if not line:
            continue

        x1, y1, x2, y2 = map(int, line.replace(" -> ", ",").split(","))

        dx = (x2 > x1) - (x2 < x1)
        dy = (y2 > y1) - (y2 < y1)

        steps = max(abs(x2 - x1), abs(y2 - y1))
        x, y = x1, y1

        for _ in range(steps + 1):
            # Part 2: Consider diagonal lines as well
            point_counts_diagonal[(x, y)] += 1

            # Part 1: Only consider horizontal and vertical lines
            if dx == 0 or dy == 0:
                point_counts[(x, y)] += 1

            x += dx
            y += dy

overlaps = sum(1 for count in point_counts.values() if count > 1)
print(f"Part 1 - Overlaps: {overlaps}")

overlaps_diagonal = sum(1 for count in point_counts_diagonal.values() if count > 1)
print(f"Part 2 - Overlaps: {overlaps_diagonal}")
