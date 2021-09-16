#!/usr/bin/env python3
from enum import Enum
import re

from grid import Grid, Cell

LINE_RE = r'(?P<operation>.+) (?P<from_x>\d+),(?P<from_y>\d+) through (?P<to_x>\d+),(?P<to_y>\d+)'

class Operation(Enum):
    ON = 'ON'
    OFF = 'OFF'
    TOGGLE = 'TOGGLE'

TEXT_TO_OPERATION = {
    'turn on': Operation.ON,
    'turn off': Operation.OFF,
    'toggle': Operation.TOGGLE
}

class Instruction:
    def __init__(self, operation: Operation, from_cell: Cell, to_cell: Cell):
        self.operation = operation
        self.from_cell = from_cell
        self.to_cell = to_cell

    def __eq__(self, other):
        return (
            (self.operation == other.operation) and
            (self.from_cell == other.from_cell) and
            (self.to_cell == other.to_cell)
        )

def main():
    instructions = read_instructions()

    grid = Grid(1000, 1000)

    for instruction in instructions:
        if instruction.operation == Operation.ON:
            grid.turn_on(instruction.from_cell, instruction.to_cell)
        elif instruction.operation == Operation.OFF:
            grid.turn_off(instruction.from_cell, instruction.to_cell)
        elif instruction.operation == Operation.TOGGLE:
            grid.toggle(instruction.from_cell, instruction.to_cell)

    print(f'Lights lit: {grid.count_on()}')


def read_instructions():
    with open('input.txt') as file:
        return [parse_instruction(line) for line in file]

def parse_instruction(line):
    match = re.search(LINE_RE, line)

    operation = TEXT_TO_OPERATION[match.group('operation')]
    from_cell = Cell(int(match.group('from_x')), int(match.group('from_y')))
    to_cell = Cell(int(match.group('to_x')), int(match.group('to_y')))

    return Instruction(operation, from_cell, to_cell)


if __name__ == '__main__':
    main()
