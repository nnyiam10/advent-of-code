from utils import read_lines

def crt(puzzle_input, part=1):
    x = 1
    idx = 0
    cycle = 1
    signal_strength = 0
    check_cycles = {20, 60, 100, 140, 180, 220}

    wait_cycles = 0
    add_value = 0

    screen = []
    curr_row = ""

    while cycle <= 240:
        if part == 1 and cycle in check_cycles:
            signal_strength += cycle * x

        if part == 2:
            pixel_pos = (cycle - 1) % 40
            if pixel_pos in [x-1, x, x+1]:
                curr_row += "#"
            else:
                curr_row += "."

            if len(curr_row) == 40:
                screen.append(curr_row)
                curr_row = ""

        if wait_cycles == 0 and idx < len(puzzle_input):
            instr = puzzle_input[idx].split()
            idx += 1
            if instr[0] == "noop":
                wait_cycles = 1
                add_value = 0
            elif instr[0] == "addx":
                wait_cycles = 2
                add_value = int(instr[1])
        
        wait_cycles -= 1
        if wait_cycles == 0:
            x += add_value
        
        cycle += 1
    
    return signal_strength if part == 1 else screen

           
def main():
    filename = "solutions/input.txt"
    puzzle_input = read_lines(filename)

    # Part 1
    print(crt(puzzle_input, 1))

    # Part 2
    screen = crt(puzzle_input, 2)
    for row in screen:
        print(row)


if __name__ == "__main__":
    main()