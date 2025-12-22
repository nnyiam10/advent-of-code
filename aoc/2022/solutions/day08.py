from utils import read_grid_from_file

def part1(puzzle_input):
    rows, cols = len(puzzle_input), len(puzzle_input[0])
    visible = set()

    def sweep_line(get_i, get_j, i_range, j_range):
        for i in i_range:
            max_height = -1
            for j in j_range:
                r, c = get_i(i, j), get_j(i, j)
                if puzzle_input[r][c] > max_height:
                    visible.add((r,c))
                    max_height = puzzle_input[r][c]

    sweep_line(lambda i,j: i, lambda i, j: j, range(rows), range(cols))
    sweep_line(lambda i,j: i, lambda i, j: cols - 1 - j, range(rows), range(cols))
    sweep_line(lambda i, j: j, lambda i, j: i, range(cols), range(rows))
    sweep_line(lambda i, j: rows - 1 - j, lambda i, j: i, range(cols), range(rows))

    return len(visible)

def part2(puzzle_input):
    rows, cols = len(puzzle_input), len(puzzle_input[0])
    max_scenic_score = -1

    def viewing_distance(height, trees):
        dist = 0
        for tree in trees:
            dist += 1
            if tree >= height:
                break
        return dist
    
    for i in range(rows):
        for j in range(cols):
            height = puzzle_input[i][j]

            up = (puzzle_input[k][j] for k in range(i - 1, -1, -1))
            down = (puzzle_input[k][j] for k in range(i + 1, rows))
            left = (puzzle_input[i][k] for k in range(j - 1, -1, -1))
            right = (puzzle_input[i][k] for k in range(j + 1, cols))

            scenic_score = (
                viewing_distance(height, up) * 
                viewing_distance(height, down) * 
                viewing_distance(height, left) * 
                viewing_distance(height, right)
            )
            
            max_scenic_score = max(max_scenic_score, scenic_score)
    return max_scenic_score
        
def main():
    filename = "solutions/input.txt"
    puzzle_input = read_grid_from_file(filename)
    
    print(part1(puzzle_input))
    print(part2(puzzle_input))


if __name__ == "__main__":
    main()
