from utils import read_lines

DIR_TO_TUPLE = {
    "U" : (0, 1),
    "D" : (0, -1),
    "L" : (-1, 0), 
    "R" : (1, 0)
}

def is_adjacent(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return max(abs(x1 - x2), abs(y1 - y2)) <= 1

def move_closer(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    dx = (x1 > x2) - (x1 < x2) #inc if heads pos else dec
    dy = (y1 > y2) - (y1 < y2)
    return (x2 + dx, y2 + dy)

def unique_positions(puzzle_input, n):
    rope = [(0,0) for _ in range(n)]
    visited = {rope[-1]}
    for line in puzzle_input:
        dir, steps = line.split()
        steps = int(steps)
        dx, dy = DIR_TO_TUPLE[dir]

        for _ in range(steps):
            rope[0] = (rope[0][0] + dx, rope[0][1] + dy)
            for i in range(1, n):
                if not is_adjacent(rope[i-1], rope[i]):
                    rope[i] = move_closer(rope[i-1], rope[i])
            visited.add(rope[-1])
    return len(visited)

def main():
    filename = "solutions/input.txt"
    puzzle_input = read_lines(filename)

    # Part 1
    print(unique_positions(puzzle_input, 2))

    # Part 2
    print(unique_positions(puzzle_input, 10))


if __name__ == "__main__":
    main()
