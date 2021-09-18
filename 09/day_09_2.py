#!/usr/bin/env python3
from typing import List
from itertools import permutations
import re

class Map:
    def __init__(self):
        self.locations = set()
        self.distances = {}

    def add_distance(self, location_1: str, location_2: str, distance: int):
        self.locations.add(location_1)
        self.locations.add(location_2)

        path = tuple(sorted([location_1, location_2]))
        self.distances[path] = distance

    def get_distance(self, location_1: str, location_2: str) -> int:
        path = tuple(sorted([location_1, location_2]))
        return self.distances[path]

    def get_path_distance(self, path: List[str]) -> int:
        path_distance = 0
        for i in range(len(path)-1):
            path_distance += self.get_distance(path[i], path[i+1])
        return path_distance

    def get_all_paths(self) -> List[List[str]]:
        return list(permutations(self.locations))

    def get_longest_distance(self) -> int:
        paths = self.get_all_paths()
        path_distances = [self.get_path_distance(path) for path in paths]
        return max(path_distances)


def main():
    m = Map()

    with open('input.txt') as file:
        for line in file:
            match = re.match(r'(?P<loc1>\w+) to (?P<loc2>\w+) = (?P<dist>\d+)', line)

            if match:
                loc1 = match.group('loc1')
                loc2 = match.group('loc2')
                dist = int(match.group('dist'))
                m.add_distance(loc1, loc2, dist)

    longest_distance = m.get_longest_distance()
    print(f'Longest distance: {longest_distance}')

if __name__ == '__main__':
    main()