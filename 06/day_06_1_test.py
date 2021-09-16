from day_06_1 import parse_instruction, Instruction, Operation
from grid import Cell

def test_parse_on_instruction():
    instruction = parse_instruction('turn on 0,0 through 999,999')
    assert instruction == Instruction(Operation.ON, Cell(0,0), Cell(999,999))

def test_parse_toggle_instruction():
    instruction = parse_instruction('toggle 0,0 through 999,0')
    assert instruction == Instruction(Operation.TOGGLE, Cell(0,0), Cell(999,0))

def test_parse_off_instruction():
    instruction = parse_instruction('turn off 499,499 through 500,500')
    assert instruction == Instruction(Operation.OFF, Cell(499,499), Cell(500,500))
