from collections import Counter, defaultdict
from typing import List, Dict, Tuple

BASE_PATH = "../../inputs/day14"

Polymer = List[str]
PolymerRules = Dict[str, str]


def parse_lines(lines: List[str]) -> Tuple[Polymer, PolymerRules]:
    polymer = list(lines.pop(0).strip())
    polymer_rules: PolymerRules = {}
    lines.pop(0)
    for line in lines:
        pattern, output = [p.strip() for p in line.split("->")]
        polymer_rules[pattern] = output

    return polymer, polymer_rules


def develop_polymer(polymer: Polymer, rules: PolymerRules, steps: int) -> int:
    pairs: Dict[str, int] = defaultdict(int)
    count_dict = defaultdict(int, {p: 1 for p in polymer})

    for i in range(len(polymer) - 1):
        a, b = polymer[i], polymer[i + 1]
        pairs[a + b] += 1

    for _ in range(steps):
        new_pairs = defaultdict(int)
        for old_pair, count in pairs.items():
            a, b = old_pair
            if new_polymer := rules.get(old_pair):
                new_pairs[a + new_polymer] += count
                new_pairs[new_polymer + b] += count
            else:
                new_pairs[a + b] += count
        pairs = new_pairs

    for pair, count in pairs.items():
        count_dict[pair[1]] += count

    counted_items = sorted(count_dict.items(), key=lambda i: i[1])
    return counted_items[-1][1] - counted_items[0][1] - 1


def solution_1(polymer: Polymer, rules: PolymerRules) -> int:
    return develop_polymer(polymer, rules, 10)


def solution_2(polymer: Polymer, rules: PolymerRules) -> int:
    return develop_polymer(polymer, rules, 40)


for file_name in ["test.txt", "sol.txt"]:
    with open(f"{BASE_PATH}/{file_name}") as f:
        polymer, rules = parse_lines(f.readlines())

    print(f"Solutions for {file_name}:")
    sol1 = solution_1(polymer, rules)
    print(f"Part 1: {sol1}")
    sol2 = solution_2(polymer, rules)
    print(f"Part 2: {sol2}")
