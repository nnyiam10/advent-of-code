"""
Advent of Code 2025
--- Day 6: Trash Compactor ---
"""

from pathlib import Path
from aoc.utils.parsing import read_text_grid_from_file, read_text_grid_from_file_with_split

OPERATIONS = {
    '+': lambda x, y: x + y,
    '*': lambda x, y: x * y,
}


def part1(puzzle_input):
    nums = [int(num) for num in puzzle_input[0]]
    m, n = len(puzzle_input)-1, len(puzzle_input[0])
    for i in range(1, m):
        for j in range(n):
            op = puzzle_input[-1][j]
            nums[j] = OPERATIONS[op](nums[j], int(puzzle_input[i][j]))
    return sum(nums)


def part2(puzzle_input):
    m, n = len(puzzle_input), len(puzzle_input[0])
    nums = []
    curr_op = None
    num = None

    for j in range(n):
        num_str = ''
        for i in range(m):
            if i == m-1 and (puzzle_input[i][j] == "+" or puzzle_input[i][j] == "*"):
                curr_op = puzzle_input[i][j]
                if num:
                    nums.append(num)
                num = int(num_str)
            
            elif i == m-1:
                if num_str:
                    num = OPERATIONS[curr_op](num, int(num_str))
                
            elif puzzle_input[i][j].strip():
                num_str += puzzle_input[i][j]
    nums.append(num)
    return sum(nums)


def main():
    input_path = Path(__file__).parent / "input.txt"
    puzzle_input = read_text_grid_from_file_with_split(input_path)
    puzzle_input_2 = read_text_grid_from_file(input_path)

    print(part1(puzzle_input))
    print(part2(puzzle_input_2))

if __name__ == "__main__":
    main()