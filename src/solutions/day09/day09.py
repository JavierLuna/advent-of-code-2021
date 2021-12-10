from typing import List, Tuple, Dict
from collections import defaultdict
from functools import reduce
from operator import mul

BASE_PATH = "../../inputs/day09"

Coord = Tuple[int, int]

NEIGHBOUR_DELTA: List[Coord] = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def get_lowest_points(lines: List[Tuple[List[str], List[str]]]) -> int:
    return sum(sum(len(digit) in (2, 3, 4, 7) for digit in line[1]) for line in lines)


def get_basin(lowest_point: Coord, grid):
    basin = set()
    queue = [lowest_point]
    while queue:
        coord = queue.pop(0)
        x, y = coord
        val = grid[y][x]
        if val == 9 or (x, y) in basin:
            continue
        basin.add((x, y))
        for dx, dy in NEIGHBOUR_DELTA:
            queue.append((x + dx, y + dy))
    return basin


def solution_1(grid: Dict, max_x: int, max_y: int) -> Tuple[int, List[Coord]]:
    lowest_numbers = []

    for y in range(max_y):
        for x in range(max_x):
            if all(grid[y][x] < grid[y + dy][x + dx] for dy, dx in NEIGHBOUR_DELTA):
                lowest_numbers.append((x, y))
    return sum(grid[y][x] for x, y in lowest_numbers) + len(lowest_numbers), lowest_numbers


def solution_2(grid, lowest_points: List[Coord]) -> int:
    biggest_three_basins = sorted(len(get_basin(lowest_point, grid)) for lowest_point in lowest_points)[-3:]
    return reduce(mul, biggest_three_basins)


for file_name in ["test.txt", "sol.txt"]:
    with open(f"{BASE_PATH}/{file_name}") as f:
        grid = defaultdict(lambda: defaultdict(lambda: 9))
        for y, line in enumerate(f):
            line = [int(n) for n in line.strip()]
            for x, n in enumerate(line):
                grid[y][x] = n
    max_y, max_x = y + 1, x + 1
    print(f"Solutions for {file_name}:")
    sol1, lowest_points = solution_1(grid, max_x, max_y)
    print(f"Part 1: {sol1}")
    sol2 = solution_2(grid, lowest_points)
    print(f"Part 2: {sol2}")
