#!/usr/bin/env python3

CHAR_UP = '('
CHAR_DOWN = ')'

def main():
    instructions = read_instructions()
    floor = determine_basement_position(instructions)

    print(f'Basement Position: {floor}')


def read_instructions():
    with open('input.txt') as file:
        return file.readline()

def determine_basement_position(instructions):
    floor = 0
    position = 1

    for char in instructions:
        if char == CHAR_UP:
            floor += 1
        elif char == CHAR_DOWN:
            floor -= 1

        if floor < 0:
            return position

        position += 1

    return None


if __name__ == '__main__':
    main()
