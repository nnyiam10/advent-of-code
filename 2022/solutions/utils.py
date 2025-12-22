def read_lines(filename):
    with open(filename) as f:
        return [line.strip() for line in f]
    
def read_lines_raw(filename):
    with open(filename) as f:
        return [line for line in f]

def read_raw(filename):
    with open(filename) as f:
        return f.read().strip()
    
def read_grid_from_file(filename):
    with open(filename) as f:
        return [[int(char) for char in line.strip()] for line in f]