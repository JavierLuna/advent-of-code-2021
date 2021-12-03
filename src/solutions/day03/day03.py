from typing import List, Tuple
from collections import defaultdict

BASE_PATH = "../../inputs/day03"


def solution_1(binary_lines: List[str]) -> int:
    count_list = [defaultdict(int) for _ in range(len(binary_lines[0]))]
    gamma = epsilon = ""
    aux_values = ["0", "1"]
    for binary_line in binary_lines:
        for i, c in enumerate(binary_line):
            count_list[i][c] += 1

    for count in count_list:
        temp = int(count['0'] < count['1'])
        gamma += aux_values[temp]
        epsilon += aux_values[(temp + 1) % 2]

    return int(gamma, 2) * int(epsilon, 2)


def filter_lines(lines: List[str], oxigen_criteria: bool) -> int:
    index = 0
    aux = ["0", "1"]
    while 1 < len(lines) and index < len(lines[0]):
        count = {"0": [], "1": []}

        for line in lines:
            count[line[index]].append(line)

        bit_criteria = aux[(int(len(count["1"]) >= len(count["0"])) + int(not oxigen_criteria)) % 2]
        lines = count[bit_criteria]

        index += 1
    return int(lines[0], 2)


def solution_2(binary_lines) -> int:
    ox = filter_lines(binary_lines, True)
    co2 = filter_lines(binary_lines, False)
    return ox * co2


for file_name in ["test.txt", "sol.txt"]:
    with open(f"{BASE_PATH}/{file_name}") as f:
        lines = [l.strip() for l in f]

    print(f"Solutions for {file_name}:")
    sol1 = solution_1(lines)
    print(f"Part 1: {sol1}")
    sol2 = solution_2(lines)
    print(f"Part 2: {sol2}")
