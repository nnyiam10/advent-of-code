from pathlib import Path
from aoc.utils.parsing import read_lines
import math

def part1(puzzle_input):
    curr = 50
    times_at_zero = 0
    for rotation in puzzle_input:
        prev = curr
        direction, amount = rotation[0], int(rotation[1:])
        if direction == "R":
            curr = (curr + amount) % 100
            
        else:
            curr = (curr - amount) % 100
        if curr == 0:
            times_at_zero += 1
    return times_at_zero


def part2(puzzle_input):
    curr = 50
    times_at_zero = 0
    for rotation in puzzle_input:
        direction, amount = rotation[0], int(rotation[1:])
        if direction == "R":
            times_at_zero += (curr + amount)//100
            curr = (curr + amount) % 100
        else:
            if curr == 0:
                times_at_zero += amount // 100
            else:
                if amount >= curr:
                    times_at_zero += 1 + (amount - curr) // 100
            curr = (curr - amount) % 100
    return times_at_zero



def main():
    input_path = Path(__file__).parent / "input.txt"
    puzzle_input = read_lines(input_path)

    print(part1(puzzle_input))
    print(part2(puzzle_input))

if __name__ == "__main__":
    main()