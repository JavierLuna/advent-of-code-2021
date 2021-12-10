from typing import List, Tuple

BASE_PATH = "../../inputs/day10"

closing_pairs = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<"
}

opening_pairs = {v: k for k, v in closing_pairs.items()}


def solution_1(lines: List[str]) -> Tuple[int, List[str]]:
    score_map = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137
    }
    illegal_score = 0
    corrupted_lines = []
    for line in lines:
        stack = []
        for c in line:
            if c in opening_pairs:
                stack.append(c)
            else:
                opening = stack.pop()
                if opening not in opening_pairs or not opening == closing_pairs[c]:
                    illegal_score += score_map[c]
                    corrupted_lines.append(line)
                    break

    return illegal_score, corrupted_lines


def solution_2(lines: List[str]) -> int:
    autocomplete_score = []
    score_map = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4
    }
    for line in lines:
        stack = []
        line_score = 0
        for c in line:
            if c in opening_pairs:
                stack.append(c)
            else:
                stack.pop()
        while stack:
            line_score *= 5
            line_score += score_map[opening_pairs[stack.pop()]]
        autocomplete_score.append(line_score)
    return sorted(autocomplete_score)[int(len(autocomplete_score) / 2)]


for file_name in ["test.txt", "sol.txt"]:
    with open(f"{BASE_PATH}/{file_name}") as f:
        lines = [line.strip() for line in f]

    print(f"Solutions for {file_name}:")
    sol1, corrupted_lines = solution_1(lines)
    print(f"Part 1: {sol1}")
    sol2 = solution_2((line for line in lines if line not in corrupted_lines))
    print(f"Part 2: {sol2}")
