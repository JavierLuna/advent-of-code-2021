from typing import Tuple, List, Set, Dict
from copy import deepcopy
from collections import defaultdict

BASE_PATH = "../../inputs/day12"

NODE_START = "start"
NODE_END = "end"

Graph = Dict[str, Set[str]]


def parse_graph(lines: List[str]) -> Dict[str, Set[str]]:
    graph: Dict[str, Set[str]] = defaultdict(set)
    for line in lines:
        a, b = line.split("-")
        if not b == NODE_START:
            graph[a].add(b)
        if not a == NODE_START:
            graph[b].add(a)

    return graph


def expand_paths(graph: Graph, visit_small_cave_twice: bool):
    paths_to_expand = [([NODE_START], not visit_small_cave_twice)]
    ending_paths = []

    while paths_to_expand:
        path, has_visited_small_cave = paths_to_expand.pop()

        if path[-1] == NODE_END:  # Paths that have ended do not have to be expanded again
            ending_paths.append(path)
            continue

        connections = [connection for connection in graph[path[-1]] if
                       connection.isupper() or connection not in path or not has_visited_small_cave]

        for connection in connections:
            paths_to_expand.append(
                (path + [connection], has_visited_small_cave or (connection.islower() and connection in path)))

    return ending_paths


def solution_1(graph: Graph) -> int:
    return len(expand_paths(graph, False))


def solution_2(graph: Graph) -> int:
    return len(expand_paths(graph, True))


for file_name in ["test1.txt", "test2.txt", "test3.txt", "sol.txt"]:
    with open(f"{BASE_PATH}/{file_name}") as f:
        graph = parse_graph((l.strip() for l in f))

    print(f"Solutions for {file_name}:")
    sol1 = solution_1(graph)
    print(f"Part 1: {sol1}")
    sol2 = solution_2(graph)
    print(f"Part 2: {sol2}")
