from typing import List, Tuple, Dict, Set
from collections import defaultdict

BASE_PATH = "../../inputs/day04"

Coord = Tuple[int, int]


class Board:

    def __init__(self, board_id: int, board_values: List[List[str]]):
        self._board = board_values
        self.board_id = board_id
        self.coords: Dict[str, Coord] = {}
        self._cols = [5] * 5
        self._rows = [5] * 5
        self._unmarked_values = {(x, y) for x in range(5) for y in range(5)}

        for y, y_val in enumerate(board_values):
            for x, x_val in enumerate(y_val):
                self.coords[board_values[y][x]] = (x, y)
        self.reset()

    def reset(self):
        self._cols = [5] * 5
        self._rows = [5] * 5
        self._unmarked_values = {(x, y) for x in range(5) for y in range(5)}

    def mark(self, number: str) -> bool:
        if number in self.coords:
            x, y = self.coords[number]
            self._cols[y] -= 1
            self._rows[x] -= 1
            self._unmarked_values.remove((x, y))
            return self.board_has_won()
        return False

    def is_num_marked(self, number: str) -> bool:
        return self.coords[number] not in self._unmarked_values

    def _check(self, board: List[int]) -> bool:
        return any(v == 0 for v in board)

    def check_rows(self) -> bool:
        return self._check(self._rows)

    def check_columns(self) -> bool:
        return self._check(self._cols)

    def board_has_won(self) -> bool:
        return self.check_rows() or self.check_columns()

    def sum_unchecked(self) -> int:
        return sum(int(self._board[y][x]) for x, y in self._unmarked_values)

    def __repr__(self):
        return f"<Board {self.board_id}>"


def parse_input(content: str) -> Tuple[List[str], List[Board]]:
    lines = [l for l in content.splitlines(keepends=False) if l]
    lucky_numbers = lines.pop(0).split(",")
    boards = []
    board_id = 1
    while lines:
        boards.append(Board(board_id, [[num for num in lines.pop(0).split(" ") if num] for _ in range(5)]))
        board_id += 1
    return lucky_numbers, boards


def solution_1(lucky_numbers: List[str], boards: List[Board]) -> int:
    for lucky_number in lucky_numbers:
        for board in boards:
            if board.mark(lucky_number):
                return board.sum_unchecked() * int(lucky_number)


def solution_2(lucky_numbers: List[str], boards: List[Board]) -> int:
    winning_boards = set()
    for lucky_number in lucky_numbers:
        for board_id, board in enumerate(boards):
            if board_id not in winning_boards and board.mark(lucky_number):
                winning_boards.add(board_id)
                if len(winning_boards) == len(boards):
                    return board.sum_unchecked() * int(lucky_number)


for file_name in ["test.txt", "sol.txt"]:
    with open(f"{BASE_PATH}/{file_name}") as f:
        lucky_numbers, boards = parse_input(f.read())

    print(f"Solutions for {file_name}:")
    sol1 = solution_1(lucky_numbers, boards)
    print(f"Part 1: {sol1}")
    [b.reset() for b in boards]
    sol2 = solution_2(lucky_numbers, boards)
    print(f"Part 2: {sol2}")
