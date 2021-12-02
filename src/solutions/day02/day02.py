from typing import List, Tuple
BASE_PATH = "../../inputs/day02"

def generic_solution(numbers: List[int], window_size=1) -> int:
    return sum([int(numbers[i] < numbers[i+window_size]) for i in range(len(numbers)-window_size)])

def solution_1(instructions) -> Tuple[int, int]:
    depth = horizontal = 0
    for instruction, value in instructions:
        if instruction == "forward":
            horizontal += value
        if instruction == "up":
            depth -= value
        if instruction == "down":
            depth += value
    return (horizontal, depth)

def solution_2(instructions) -> Tuple[int, int]:
    depth = horizontal = aim = 0
    for instruction, value in instructions:
        if instruction == "forward":
            horizontal += value
            depth += aim * value
        if instruction == "up":
            aim -= value
        if instruction == "down":
            aim += value
    return (horizontal, depth)



for file_name in ["test.txt", "sol.txt"]:
    with open(f"{BASE_PATH}/{file_name}") as f:
        lines = [[i, int(c)] for i, c in [l.strip().split() for l in f if l.strip()]]


    print(f"Solutions for {file_name}:")
    sol1 = solution_1(lines)
    print(f"Part 1: {sol1[0] * sol1[1]}")
    sol2= solution_2(lines)
    print(f"Part 2: {sol2[0] * sol2[1]}")
