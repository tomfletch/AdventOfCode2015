#!/usr/bin/env python3

from dataclasses import dataclass
from enum import Enum
from typing import List


class InstructionType(Enum):
    HALF = 1
    TRIPLE = 2
    INCREMENT = 3
    JUMP = 4
    JUMP_IF_EVEN = 5
    JUMP_IF_ONE = 6

CMD_TO_INSTRUCTION_TYPE = {
    'hlf': InstructionType.HALF,
    'tpl': InstructionType.TRIPLE,
    'inc': InstructionType.INCREMENT,
    'jmp': InstructionType.JUMP,
    'jie': InstructionType.JUMP_IF_EVEN,
    'jio': InstructionType.JUMP_IF_ONE,
}

@dataclass
class Instruction:
    type: InstructionType
    register: str = None
    offset: int = None

def main():
    program: List[Instruction] = read_program()

    instruction_pointer = 0
    registers = {'a': 0, 'b': 0}

    while instruction_pointer < len(program):
        instruction = program[instruction_pointer]

        if instruction.type == InstructionType.HALF:
            registers[instruction.register] /= 2
        elif instruction.type == InstructionType.TRIPLE:
            registers[instruction.register] *= 3
        elif instruction.type == InstructionType.INCREMENT:
            registers[instruction.register] += 1
        elif instruction.type == InstructionType.JUMP:
            instruction_pointer += instruction.offset - 1
        elif instruction.type == InstructionType.JUMP_IF_EVEN:
            if registers[instruction.register] % 2 == 0:
                instruction_pointer += instruction.offset - 1
        elif instruction.type == InstructionType.JUMP_IF_ONE:
            if registers[instruction.register] == 1:
                instruction_pointer += instruction.offset - 1

        instruction_pointer += 1

    print('Register b:', registers['b'])


def read_program():
    with open('input.txt') as file:
        return [create_instruction(line.strip()) for line in file]

def create_instruction(line: str):
    instruction_str, arguments_str = line.split(' ', 1)
    arguments = arguments_str.split(', ')

    instruction_type = CMD_TO_INSTRUCTION_TYPE[instruction_str]

    if instruction_type in [InstructionType.JUMP_IF_EVEN, InstructionType.JUMP_IF_ONE]:
        return Instruction(instruction_type, arguments[0], int(arguments[1]))
    if instruction_type == InstructionType.JUMP:
        return Instruction(instruction_type, offset=int(arguments[0]))
    else:
        return Instruction(instruction_type, arguments[0])

if __name__ == '__main__':
    main()
