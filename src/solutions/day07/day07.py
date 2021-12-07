from typing import List
import statistics, math

BASE_PATH = "../../inputs/day07"


def solution_1(crabs: List[int]) -> int:
    m = statistics.median(crabs)
    return int(sum(abs(c - m) for c in crabs))


def solution_2(crabs: List[int]) -> int:
    m = statistics.mean(crabs)
    return min(sum(sum(list(range(1, abs(c - m) + 1))) for c in crabs) for m in [math.ceil(m), math.floor(m)])


for file_name in ["test.txt", "sol.txt"]:
    with open(f"{BASE_PATH}/{file_name}") as f:
        crabs = [int(l) for l in f.read().strip().split(",")]

    print(f"Solutions for {file_name}:")
    sol1 = solution_1(crabs)
    print(f"Part 1: {sol1}")
    sol2 = solution_2(crabs)
    print(f"Part 2: {sol2}")
