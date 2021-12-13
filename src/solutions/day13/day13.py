from typing import Set, Tuple, List

BASE_PATH = "../../inputs/day13"

Coord = Tuple[int, int]
Fold = Tuple[str, int]


def parse_content(lines: List[str]) -> Tuple[Set[Coord], List[Fold]]:
    dots: Set[Coord] = set()
    folds: List[Tuple[str, int]] = []

    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line.startswith("fold along"):
            line = line[len("fold along "):]
            axis, n_line = line.split("=")
            folds.append((axis, int(n_line)))
        else:
            x, y = line.split(",")
            dots.add((int(x), int(y)))
    return dots, folds


def do_fold(dots: Set[Coord], fold: Fold) -> Set[Coord]:
    axis, n_line = fold
    n_axis = int(axis == "y")
    in_fold = {coord for coord in dots if coord[n_axis] >= n_line}
    for in_fold_coord in in_fold:
        new_pos = n_line - (in_fold_coord[n_axis] - n_line)
        dots.add((in_fold_coord[0], new_pos) if n_axis else (new_pos, in_fold_coord[1]))
    return dots - in_fold


def print_dots(dots: Set[Coord]):
    max_x, max_y = 0, 0
    for x, y in dots:
        if max_x < x:
            max_x = x
        if max_y < y:
            max_y = y

    for y in range(max_y + 1):
        row = ""
        for x in range(max_x + 1):
            if (x, y) in dots:
                row += "#"
            else:
                row += " "
        print(row)


def solution_1(dots: Set[Coord], folds: List[Fold]) -> int:
    dots = do_fold(dots, folds[0])
    return len(dots)


def solution_2(dots: Set[Coord], folds: List[Fold]) -> Set[Coord]:
    for fold in folds:
        dots = do_fold(dots, fold)
    return dots


for file_name in ["test.txt", "sol.txt"]:
    dots: List[Coord] = []

    with open(f"{BASE_PATH}/{file_name}") as f:
        dots, folds = parse_content(f.readlines())
    print(f"Solutions for {file_name}:")
    sol1 = solution_1(dots, folds)
    print(f"Part 1: {sol1}")
    print(f"Part 2: \n")
    dots = solution_2(dots, folds)
    print_dots(dots)
