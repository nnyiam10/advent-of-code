from utils import read_lines_raw

def arrange_creates(puzzle_input):
    row_length = len(puzzle_input[0])
    num_stacks = row_length // 4
    crates = {i: [] for i in range(1, num_stacks + 1)}

    split_index = next(i for i, row in enumerate(puzzle_input) if row.strip().startswith("1"))

    for row in puzzle_input[:split_index]:
        for i in range(0, row_length, 4):
            if row[i] == "[":
                stack_num = i // 4 + 1
                crates[stack_num].append(row[i + 1])

    return puzzle_input[split_index + 2:], crates

def instructions(puzzle_input, crates, part):
    for row in puzzle_input:
        _, num, _, start, _, end = row.strip().split()
        num, start, end = int(num), int(start), int(end)
        to_move = crates[start][:num]
        if part == 1:
            to_move.reverse()
        crates[start] = crates[start][num:]
        crates[end] = to_move + crates[end]

    return "".join(crates[i][0] for i in sorted(crates) if crates[i])

def part1(puzzle_input):
    updated_input, crates = arrange_creates(puzzle_input)
    return instructions(updated_input, crates, 1)

def part2(puzzle_input):
    updated_input, crates = arrange_creates(puzzle_input)
    return instructions(updated_input, crates, 2)
    
def main():
    filename = "solutions/input.txt"
    puzzle_input = read_lines_raw(filename)
    
    print(part1(puzzle_input))
    print(part2(puzzle_input))

if __name__ == "__main__":
    main()