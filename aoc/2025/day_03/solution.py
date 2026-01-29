"""
Advent of Code 2025
--- Day 3: Lobby ---
"""

from pathlib import Path
from aoc.utils.parsing import read_lines

def part1(puzzle_input):
    total = 0
    for bank in puzzle_input:
        curr_max = -1
        for i in range(len(bank) -1):
            for j in range(i+1, len(bank)):
                num_pair = int(bank[i] + bank[j])
                curr_max = max(curr_max, num_pair)
        total += curr_max
    return total


def largest_bank_for_n(bank, n):
    res = ''
    min_idx = 0
    while n > 0:
        curr_max, curr_idx = -1, -1
        for i in range(min_idx, len(bank)-n+1):
            if int(bank[i]) > curr_max:
                curr_max = int(bank[i])
                idx = i
        res += bank[idx]
        min_idx = idx+1
        n -= 1
    return res


def part2(puzzle_input):
    total = 0
    for bank in puzzle_input:
        total += int(largest_bank_for_n(bank, 12))
    return total



def main():
    input_path = Path(__file__).parent / "input.txt"
    puzzle_input = read_lines(input_path)

    print(part1(puzzle_input))
    print(part2(puzzle_input))

if __name__ == "__main__":
    main()