#!/usr/bin/env python3

CHAR_UP = '('
CHAR_DOWN = ')'

def main():
    instructions = read_instructions()
    floor = determine_floor(instructions)

    print(f'Floor {floor}')


def read_instructions():
    with open('input.txt') as file:
        return file.readline()

def determine_floor(instructions):
    floor = 0

    for char in instructions:
        if char == CHAR_UP:
            floor += 1
        elif char == CHAR_DOWN:
            floor -= 1

    return floor


if __name__ == '__main__':
    main()
