from collections import defaultdict
from utils import read_lines

def make_tree():
    return defaultdict(make_tree)

def parse_input(puzzle_input):
    fs = make_tree()
    path = []
    curr = fs
    idx = 0

    while idx < len(puzzle_input):
        parts = puzzle_input[idx].split()
        if parts[0] == "$":
            if parts[1] == "cd":
                if parts[2] == "/":
                    path = []
                    curr = fs
                elif parts[2] == "..":
                    path.pop()
                    curr = fs
                    for p in path:
                        curr = curr[p]
                else:
                    path.append(parts[2])
                    curr = curr[parts[2]]
                idx += 1
            elif parts[1] == "ls":
                idx += 1
                while idx < len(puzzle_input) and not puzzle_input[idx].startswith("$"):
                    parts = puzzle_input[idx].split()
                    if parts[0] == "dir":
                        curr[parts[1]]
                    else:
                        size, name = int(parts[0]), parts[1]
                        curr[name] = size
                    idx += 1
    return fs

def get_dir_sizes(node, sizes):
    total = 0
    for name, val in node.items():
        if isinstance(val, dict):
            sub_total = get_dir_sizes(val, sizes)
            sizes.append(sub_total)
            total += sub_total
        else:
            total += val
    return total

def part1(puzzle_input):
    fs = parse_input(puzzle_input)
    sizes = []    
    get_dir_sizes(fs, sizes)
    return sum(s for s in sizes if s <= 100000) 

def part2(puzzle_input):
    fs = parse_input(puzzle_input)
    sizes = []    
    total_space_used = get_dir_sizes(fs, sizes)
    min_diff = total_space_used - 40000000
    return min(s for s in sizes if s >= min_diff)
   
def main():
    filename = "solutions/input.txt"
    puzzle_input = read_lines(filename)

    print(part1(puzzle_input))
    print(part2(puzzle_input))


if __name__ == "__main__":
    main()
