#!/usr/bin/env python3

import operator

CHAR_INSTRUCTIONS = {
    '^': ( 0, -1),
    '>': ( 1,  0),
    'v': ( 0,  1),
    '<': (-1,  0)
}

def main():
    instructions = read_instructions()
    houses_visited = count_houses_visited(instructions)
    print(f'Houses visited: {houses_visited}')


def read_instructions():
    with open('input.txt') as file:
        return file.readline().rstrip()


def count_houses_visited(instructions):
    current = (0, 0)
    visited = set([current])

    for char in instructions:
        delta = CHAR_INSTRUCTIONS[char]
        current = tuple(map(operator.add, current, delta))
        visited.add(current)

    return len(visited)


if __name__ == '__main__':
    main()
