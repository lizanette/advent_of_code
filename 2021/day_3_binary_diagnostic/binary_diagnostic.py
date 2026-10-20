with open('puzzle_input.txt') as file:
    report = [line.strip() for line in file]

# --- PART 1 ---
gamma_rate = ""
epsilon_rate = ""

for column in zip(*report):
    if column.count("1") > len(column) / 2:
        gamma_rate += "1"
        epsilon_rate += "0"
    else:
        gamma_rate += "0"
        epsilon_rate += "1"

gamma_val = int(gamma_rate, 2)
epsilon_val = int(epsilon_rate, 2)

print(f"Gamma rate: {gamma_rate}")
print(f"Epsilon rate: {epsilon_rate}")
print(f"Power consumption: {gamma_val} * {epsilon_val} = {gamma_val * epsilon_val}\n")


# --- PART 2 ---

def filter_numbers(numbers, keep_most_common):
    filtered = numbers.copy()

    for position in range(len(filtered[0])):
        if len(filtered) == 1:
            break

        one_count = sum(1 for number in filtered if number[position] == "1")
        zero_count = len(filtered) - one_count

        if keep_most_common:
            target_bit = "1" if one_count >= zero_count else "0"
        else:
            target_bit = "0" if one_count >= zero_count else "1"

        filtered = [number for number in filtered if number[position] == target_bit]

    return filtered[0]

oxygen_rating = filter_numbers(report, keep_most_common=True)
co2_rating = filter_numbers(report, keep_most_common=False)

oxygen_val = int(oxygen_rating, 2)
co2_val = int(co2_rating, 2)

print(f"Oxygen generator rating: {oxygen_rating}")
print(f"CO2 scrubber rating: {co2_rating}")
print(f"Life support rating: {oxygen_val} * {co2_val} = {oxygen_val * co2_val}")
