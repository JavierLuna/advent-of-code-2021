from typing import List
BASE_PATH = "../../inputs/day01"

def get_numbers(file_path: str) -> List[int]:
    with open(file_path) as input_file:
        return [int(l.strip()) for l in input_file if l.strip()]

def generic_solution(numbers: List[int], window_size=1) -> int:
    return sum([int(numbers[i] < numbers[i+window_size]) for i in range(len(numbers)-window_size)])

def solution_1(numbers: List[int]) -> int:
    return generic_solution(numbers, window_size=1)

def solution_2(numbers: List[int]) -> int:
    return generic_solution(numbers, window_size=3)



for file_name in ["test.txt", "sol.txt"]:
    print(f"Solutions for {file_name}:")
    numbers = get_numbers(f"../../inputs/day01/{file_name}")
    print(f"\tPart 1: {solution_1(numbers)}")
    print(f"\tPart 2: {solution_2(numbers)}")
