from typing import Tuple, List
from functools import reduce
from collections import Counter

BASE_PATH = "../../inputs/day05"

Coord = Tuple[int, int]
Line = Tuple[Coord, Coord]
flat_map = lambda l, f: reduce(list.__add__, [f(e) for e in l])


def is_diagonal(line: Line) -> bool:
    c1, c2 = line
    return not (c1[0] == c2[0] or c1[1] == c2[1])


def parse_input(content: str) -> List[Line]:
    lines: List[Line] = []
    for line in content.splitlines(keepends=False):
        c1, c2 = [[int(p) for p in c.strip().split(",")] for c in line.split("->")]
        lines.append((tuple(c1), tuple(c2)))
    return lines


def get_p_delta(p1: int, p2: int) -> int:
    if p2 > p1:
        return 1
    elif p2 < p1:
        return -1
    else:
        return 0


def expand_line(line: Line) -> List[Coord]:
    c1, c2 = line
    x_delta = get_p_delta(c1[0], c2[0])
    y_delta = get_p_delta(c1[1], c2[1])
    magnitude = abs(c2[1] - c1[1]) or abs(c2[0] - c1[0])
    return [(c1[0] + i * x_delta, c1[1] + i * y_delta) for i in range(magnitude + 1)]


def solution_2(lines: List[Lines]) -> int:
    c = Counter(flat_map(lines, expand_line))
    return len([v for v in c.values() if v > 1])


def solution_1(lines: List[Line]) -> int:
    return solution_2([line for line in lines if not is_diagonal(line)])


for file_name in ["test.txt", "sol.txt"]:
    with open(f"{BASE_PATH}/{file_name}") as f:
        lines = parse_input(f.read())

    print(f"Solutions for {file_name}:")
    sol1 = solution_1(lines)
    print(f"Part 1: {sol1}")
    sol2 = solution_2(lines)
    print(f"Part 2: {sol2}")
