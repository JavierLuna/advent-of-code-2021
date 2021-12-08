from typing import List, Tuple, Dict
import itertools
from collections import defaultdict

BASE_PATH = "../../inputs/day08"

display = "abcdefg"

TRANSLATION_MAP = {
    "abcefg": "0",
    "cf": "1",
    "acdeg": "2",
    "acdfg": "3",
    "bcdf": "4",
    "abdfg": "5",
    "abdefg": "6",
    "acf": "7",
    "abcdefg": "8",
    "abcdfg": "9"
}

COMBOS_BY_LENGTH = defaultdict(list)
for translation in TRANSLATION_MAP:
    COMBOS_BY_LENGTH[len(translation)].append(set(translation))

all_mappings = [{k: v for k, v in zip(permutation, display)} for permutation in itertools.permutations(display)]


def parse_line(line: str) -> Tuple[List[str], List[str]]:
    a, b = [l.strip() for l in line.split("|")]
    return ["".join(sorted(d)) for d in a.split(" ")], ["".join(sorted(d)) for d in b.split(" ")]


def get_mapping(digits: List[str]) -> Dict[str, str]:
    mappings_left = all_mappings.copy()
    for digit in digits:
        mappings_left = [mapping for mapping in mappings_left if set(mapping[d] for d in digit) in COMBOS_BY_LENGTH[len(digit)]]

    return mappings_left[0]


def translate_digit(digit: str, mapping: Dict[str, str]) -> str:
    return TRANSLATION_MAP["".join(sorted("".join(mapping[c] for c in digit)))]


def solution_1(lines: List[Tuple[List[str], List[str]]]) -> int:
    return sum(sum(len(digit) in (2, 3, 4, 7) for digit in line[1]) for line in lines)


def solution_2(lines: List[Tuple[List[str], List[str]]]) -> int:
    final = 0
    for line in lines:
        mapping = get_mapping(line[0] + line[1])
        last_chars = "".join(translate_digit(digit, mapping) for digit in line[1])
        final += int(last_chars)

    return final


for file_name in ["test.txt", "sol.txt"]:
    with open(f"{BASE_PATH}/{file_name}") as f:
        lines = [parse_line(line.strip()) for line in f]

    print(f"Solutions for {file_name}:")
    sol1 = solution_1(lines)
    print(f"Part 1: {sol1}")
    sol2 = solution_2(lines)
    print(f"Part 2: {sol2}")
