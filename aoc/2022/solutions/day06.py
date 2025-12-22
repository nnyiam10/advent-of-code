from utils import read_raw

def parts(puzzle_input, part=1):
    seen = set()
    l = 0
    offset = 4 if part == 1 else 14
    for r in range(len(puzzle_input)):
        if r - l == offset:
            return r
        
        char = puzzle_input[r]
        if char in seen:
            while l < r and puzzle_input[l] != char:
                seen.remove(puzzle_input[l])
                l += 1
            l += 1
        else:
            seen.add(puzzle_input[r])

def main():
    filename = "solutions/input.txt"
    puzzle_input = read_raw(filename)

    print(parts(puzzle_input, 1))
    print(parts(puzzle_input, 2))

if __name__ == "__main__":
    main()