with open('puzzle_input.txt') as file:
    sections = file.read().strip().split('\n\n')

drawn_numbers = [int(num) for num in sections[0].split(",")]

def get_boards():
    boards = []
    for block in sections[1:]:
        grid = [[int(num) for num in line.split()] for line in block.split('\n')]
        boards.append({
            'rows': [set(row) for row in grid],
            'cols': [set(col) for col in zip(*grid)],
            'unmarked': set(num for row in grid for num in row)
        })

    return boards

def solve_part_1():
    boards = get_boards()

    for number in drawn_numbers:
        for board in boards:
            if number in board["unmarked"]:
                board["unmarked"].remove(number)

            for row in board["rows"]:
                row.discard(number)

            for col in board["cols"]:
                col.discard(number)

            if any(not row for row in board["rows"]) or any(not col for col in board["cols"]):
                return sum(board["unmarked"]) * number

print(f"Part 1 - Final score: {solve_part_1()}")

def solve_part_2():
    boards = get_boards()
    active_boards = boards[:]

    for number in drawn_numbers:
        for board in active_boards[:]:
            if number in board["unmarked"]:
                board["unmarked"].remove(number)

            for row in board["rows"]:
                row.discard(number)

            for col in board["cols"]:
                col.discard(number)

            if any(not row for row in board["rows"]) or any(not col for col in board["cols"]):
                if len(active_boards) == 1:
                    return sum(board["unmarked"]) * number

                active_boards.remove(board)

print(f"Part 2 - Final score: {solve_part_2()}")
