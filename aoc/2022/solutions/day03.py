from utils import read_lines

def priority(letter):
    return ord(letter) - 38 if letter.isupper() else ord(letter) - 96

def part1(puzzle_input):
    total_priority = 0
    for line in puzzle_input:
        half = len(line)//2
        first, second = line[:half], line[half:]
        seen = set(first)
        total_priority += next(priority(c) for c in second if c in seen)
    return total_priority

def part2(puzzle_input):
    total_priority = 0
    for i in range(0, len(puzzle_input), 3):
        group = puzzle_input[i:i+3]
        s1, s2, s3 = set(group[0]), set(group[1]), set(group[2])
        common = s1.intersection(s2, s3)
        total_priority += priority(common.pop())
    return total_priority

def main():
    filename = "solutions/input.txt"
    puzzle_input = read_lines(filename)

    print(part1(puzzle_input))
    print(part2(puzzle_input))

if __name__ == "__main__":
    main()
