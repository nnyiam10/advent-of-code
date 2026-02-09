from pathlib import Path
from aoc.utils.parsing import read_lines
from collections import deque

def bfs(start, expected, toggles):
    seen = set()
    q = deque([(start, 0)])
    while q:
        state, presses = q.popleft()
        for toggle in toggles:
            curr = state.copy()
            for idx in toggle:
                curr[idx] = 1 - curr[idx]
            if curr == expected:
                return presses + 1
            if tuple(curr) not in seen:
                seen.add(tuple(curr))
                q.append((curr, presses + 1))


def part1(puzzle_input):
    n = len(puzzle_input)
    total = 0
    for i in range(n):
        indicator_lights = []
        possible_toggles = []
        lights, toggles = puzzle_input[i][1:].split(']')
        for char in lights:
            indicator_lights.append(char)

        toggles = toggles.split(' ')[1:]
        for toggle in toggles:
            if toggle[0] == "(":
                possible_toggles.append([int(x) for x in toggle[1:-1].split(",")])

        start = [0]*len(lights)
        expected = [1 if l == '#' else 0 for l in indicator_lights]
        total += bfs(start, expected, possible_toggles)
    return total


def part2(puzzle_input):
    pass


def main():
    input_path = Path(__file__).parent / "input.txt"
    puzzle_input = read_lines(input_path)

    print(part1(puzzle_input))
    print(part2(puzzle_input))

if __name__ == "__main__":
    main()