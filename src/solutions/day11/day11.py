from typing import Tuple, List, Set
from copy import deepcopy

BASE_PATH = "../../inputs/day11"

Coord = Tuple[int, int]
Grid = List[List[int]]
NEIGHBOURS_DELTA: List[Coord] = [(dx, dy) for dx in range(-1, 2) for dy in range(-1, 2) if not dx == dy == 0]


def get_neighbours(grid: Grid, coord: Coord) -> Set[Coord]:
    neighbours: Set[Coord] = set()
    for dx, dy in NEIGHBOURS_DELTA:
        x, y = coord[0] + dx, coord[1] + dy
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
            neighbours.add((x, y))
    return neighbours


def simulate(grid: Grid) -> Tuple[Grid, int]:
    energized_octopuses: Set[Coord] = set()
    already_flashed_octopuses: Set[Coord] = set()
    n_flashes = 0

    # +1 of energy to all octopuses
    for y, row in enumerate(grid):
        for x, energy_level in enumerate(row):
            grid[y][x] += 1
            if 9 < grid[y][x]:
                energized_octopuses.add((x, y))

    while energized_octopuses:
        energized_octopus = energized_octopuses.pop()
        if energized_octopus in already_flashed_octopuses:
            continue
        # Flash
        grid[energized_octopus[1]][energized_octopus[0]] = 0
        already_flashed_octopuses.add(energized_octopus)
        n_flashes += 1

        # Energize adjacent
        adjacents = get_neighbours(grid, energized_octopus) - already_flashed_octopuses
        for adjacent in adjacents:
            grid[adjacent[1]][adjacent[0]] += 1
            if 9 < grid[adjacent[1]][adjacent[0]]:
                energized_octopuses.add(adjacent)
    return grid, n_flashes


def solution_1(grid: Grid) -> int:
    grid = deepcopy(grid)
    n_flashes = 0
    for _ in range(100):
        grid, new_flashes = simulate(grid)
        n_flashes += new_flashes
    return n_flashes


def solution_2(grid: Grid) -> int:
    step = 0
    n_octopuses = len(grid) * len(grid[0])
    while 1:
        step += 1
        grid, n_flashes = simulate(grid)
        if n_flashes == n_octopuses:
            break
    return step


for file_name in ["test.txt", "sol.txt"]:
    with open(f"{BASE_PATH}/{file_name}") as f:
        grid = [[int(c) for c in line.strip()] for line in f]

    print(f"Solutions for {file_name}:")
    sol1 = solution_1(grid)
    print(f"Part 1: {sol1}")
    sol2 = solution_2(grid)
    print(f"Part 2: {sol2}")
