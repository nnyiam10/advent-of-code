"""
Advent of Code 2025
--- Day 8: Playground ---
"""

from pathlib import Path
from aoc.utils.parsing import read_lines
import math

def distance(point1, point2):
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    dx, dy,dz = x2 - x1, y2 - y1, z2 - z1
    return dx*dx + dy*dy + dz*dz

def part1(puzzle_input):
    junction_boxes = []
    for line in puzzle_input:
        x, y, z = [int(x) for x in line.split(',')]
        junction_boxes.append((x, y, z))
    
    n = len(junction_boxes)
    D = []
    for i in range(n):
        for j in range(i+1, n):
            dist = distance(junction_boxes[i], junction_boxes[j])
            D.append((dist, i, j))

    D.sort()

    circuits = []
    circuit_mapping = {}
    for d, i, j in D[:1000]:
        i_in = i in circuit_mapping
        j_in = j in circuit_mapping

        if not i_in and not j_in:
            idx = len(circuits)
            circuits.append({i, j})
            circuit_mapping[i] = idx
            circuit_mapping[j] = idx
        
        elif i_in and not j_in:
            idx = circuit_mapping[i]
            circuits[idx].add(j)
            circuit_mapping[j] = idx
        
        elif not i_in and j_in:
            idx = circuit_mapping[j]
            circuits[idx].add(i)
            circuit_mapping[i] = idx
        
        else:
            idx_i = circuit_mapping[i]
            idx_j = circuit_mapping[j]

            if idx_i != idx_j:
                if len(circuits[idx_i]) < len(circuits[idx_j]):
                    idx_i, idx_j = idx_j, idx_i

                for p in circuits[idx_j]:
                    circuits[idx_i].add(p)
                    circuit_mapping[p] = idx_i
                circuits[idx_j] = set()

    circuits = [c for c in circuits if c]
    circuits.sort(key=len, reverse=True)
    return len(circuits[0]) * len(circuits[1]) * len(circuits[2])  
        

def part2(puzzle_input):
    junction_boxes = []
    for line in puzzle_input:
        x, y, z = [int(x) for x in line.split(',')]
        junction_boxes.append((x, y, z))
    
    n = len(junction_boxes)
    D = []
    for i in range(n):
        for j in range(i+1, n):
            dist = distance(junction_boxes[i], junction_boxes[j])
            D.append((dist, i, j))

    D.sort()

    circuits = []
    circuit_mapping = {}
    for d, i, j in D:
        i_in = i in circuit_mapping
        j_in = j in circuit_mapping

        if not i_in and not j_in:
            idx = len(circuits)
            circuits.append({i, j})
            circuit_mapping[i] = idx
            circuit_mapping[j] = idx
        
        elif i_in and not j_in:
            idx = circuit_mapping[i]
            circuits[idx].add(j)
            circuit_mapping[j] = idx
        
        elif not i_in and j_in:
            idx = circuit_mapping[j]
            circuits[idx].add(i)
            circuit_mapping[i] = idx
        
        else:
            idx_i = circuit_mapping[i]
            idx_j = circuit_mapping[j]

            if idx_i != idx_j:
                if len(circuits[idx_i]) < len(circuits[idx_j]):
                    idx_i, idx_j = idx_j, idx_i

                for p in circuits[idx_j]:
                    circuits[idx_i].add(p)
                    circuit_mapping[p] = idx_i
                circuits[idx_j] = set()
        
        if len(circuits[idx]) == n:
                return junction_boxes[i][0] * junction_boxes[j][0]


def main():
    input_path = Path(__file__).parent / "input.txt"
    puzzle_input = read_lines(input_path)

    print(part1(puzzle_input))
    print(part2(puzzle_input))

if __name__ == "__main__":
    main()