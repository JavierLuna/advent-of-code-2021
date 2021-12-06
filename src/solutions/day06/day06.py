from collections import Counter, defaultdict

BASE_PATH = "../../inputs/day06"

from collections import defaultdict, Counter

for file_name in ["test.txt", "sol.txt"]:
    with open(f"{BASE_PATH}/{file_name}") as f:
        lanternfish = defaultdict(int, Counter(int(l) for l in f.readline().strip().split(",")))

    print(f"Solutions for {file_name}:")
    n_lanternfish = sum(lanternfish.values())
    for turn in range(256):
        if turn in lanternfish:
            lanternfish[turn + 7] += lanternfish[turn]
            lanternfish[turn + 9] += lanternfish[turn]
            n_lanternfish += lanternfish[turn]
        if turn == 79:
            print(f"Part 1: {n_lanternfish}")
    print(f"Part 2: {n_lanternfish}")
