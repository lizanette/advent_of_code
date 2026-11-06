UNIQUE_LENGTHS = {2, 3, 4, 7}

def identify_digit(pattern, one, four):
    match len(pattern):
        case 2: return "1"
        case 3: return "7"
        case 4: return "4"
        case 7: return "8"
        case 5:
            if one <= pattern: return "3"
            return "2" if len(pattern & four) == 2 else "5"
        case 6:
            if four <= pattern: return "9"
            return "0" if one <= pattern else "6"

def decode_line(patterns, output_values):
    sets = [frozenset(p) for p in patterns]
    one = next(s for s in sets if len(s) == 2)
    four = next(s for s in sets if len(s) == 4)

    digits = [identify_digit(frozenset(v), one, four) for v in output_values]

    return int(''.join(digits))

with open('puzzle_input.txt') as file:
    entries = []
    for line in file:
        left, right = line.strip().split(' | ')
        entries.append((left.split(), right.split()))

part1 = sum(len(value) in UNIQUE_LENGTHS for _, output_values in entries for value in output_values)
part2 = sum(decode_line(patterns, output_values) for patterns, output_values in entries)

print(f"PART 1 -- How many times unique digits appear: {part1}")
print(f"PART 2 -- Total sum: {part2}")
