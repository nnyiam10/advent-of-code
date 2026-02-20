from heapq import nlargest
from utils import read_lines

def top_three(input):
    calorie_totals = []
    curr_cals = 0

    for line in input:
        if line == "":
            calorie_totals.append(curr_cals)
            curr_cals = 0
        else:
            curr_cals += int(line)

    if curr_cals > 0:
        calorie_totals.append(curr_cals)
    return nlargest(3, calorie_totals)

def main():
    filename = "solutions/input.txt"
    puzzle_input = read_lines(filename)

    #Part 1
    print(max(top_three(puzzle_input)))

    # Part 2
    print(sum(top_three(puzzle_input)))

if __name__ == "__main__":
    main()