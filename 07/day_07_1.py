#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import List, Union
import re

class Component(ABC):
    @abstractmethod
    def get_output(self) -> int:
        pass

class Wire(Component):
    def __init__(self, id: str):
        self.id = id
        self.input = None
        self.output = None

    def set_input(self, input: Component):
        self.input = input

    def get_output(self) -> int:
        if self.output is None:
            self.output = self.input.get_output()

        return self.output

class Constant(Component):
    def __init__(self, value):
        self.value = value

    def get_output(self) -> int:
        return self.value

class NotGate(Component):
    def __init__(self, input):
        self.input = input

    def get_output(self) -> int:
        return self.input.get_output() ^ 65535

class AndGate(Component):
    def __init__(self, input1, input2):
        self.input1 = input1
        self.input2 = input2

    def get_output(self) -> int:
        return self.input1.get_output() & self.input2.get_output()

class OrGate(Component):
    def __init__(self, input1, input2):
        self.input1 = input1
        self.input2 = input2

    def get_output(self) -> int:
        return self.input1.get_output() | self.input2.get_output()

class LShiftGate(Component):
    def __init__(self, input1, input2):
        self.input1 = input1
        self.input2 = input2

    def get_output(self) -> int:
        return self.input1.get_output() << self.input2.get_output()

class RShiftGate(Component):
    def __init__(self, input1, input2):
        self.input1 = input1
        self.input2 = input2

    def get_output(self) -> int:
        return self.input1.get_output() >> self.input2.get_output()


class Instruction:
    def __init__(self, component: Component, inputs: List[Union[str, int]], output: str):
        self.component = component
        self.inputs = inputs
        self.output = output

    def __eq__(self, other):
        return (
            (self.component == other.component) and
            (self.inputs == other.inputs) and
            (self.output == other.output)
        )

    def __str__(self):
        return f'{self.component} ({self.inputs}) => {self.output}'

    @staticmethod
    def parse(line: str) -> 'Instruction':
        [input, output] = line.split(' -> ')

        parts = input.split(' ')

        inputs = []
        component = None

        for part in parts:
            if re.match(r'[A-Z]+', part):
                if part == 'NOT':
                    component = NotGate
                elif part == 'AND':
                    component = AndGate
                elif part == 'OR':
                    component = OrGate
                elif part == 'LSHIFT':
                    component = LShiftGate
                elif part == 'RSHIFT':
                    component = RShiftGate
            elif re.match(r'[a-z]+', part):
                inputs.append(part)
            elif re.match(r'\d+', part):
                inputs.append(int(part))

        return Instruction(component, inputs, output)


class Circuit:
    def __init__(self):
        self.wires = {}

    def get_wire(self, wire_id) -> Wire:
        if wire_id not in self.wires:
            self.wires[wire_id] = Wire(wire_id)

        return self.wires[wire_id]

    def add_instruction(self, instruction: Instruction):
        inputs = []

        for input in instruction.inputs:
            if type(input) == int:
                inputs.append(Constant(input))
            else:
                inputs.append(self.get_wire(input))

        if instruction.component:
            component = instruction.component(*inputs)
        else:
            component = inputs[0]

        output = self.get_wire(instruction.output)
        output.set_input(component)

def read_instructions():
    with open('input.txt') as file:
        return [Instruction.parse(line.rstrip()) for line in file]

def main():
    instructions = read_instructions()
    circuit = Circuit()

    for instruction in instructions:
        circuit.add_instruction(instruction)

    a_value = circuit.get_wire('a').get_output()

    print(f'Value of wire a: {a_value}')


if __name__ == '__main__':
    main()