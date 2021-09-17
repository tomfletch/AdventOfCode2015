from day_07_1 import (
    Wire,
    Constant,
    NotGate,
    AndGate,
    OrGate,
    LShiftGate,
    RShiftGate,
    Instruction,
    Circuit
)

def test_constant_wire():
    a = Wire('a')
    a.set_input(Constant(5))
    assert a.get_output() == 5

def test_not():
    a = Wire('a')
    a.set_input(Constant(1))
    b = Wire('b')
    b.set_input(NotGate(a))
    assert b.get_output() == 65534

def test_and():
    a = Wire('a')
    a.set_input(Constant(13))
    b = Wire('b')
    b.set_input(Constant(10))
    c = Wire('c')
    c.set_input(AndGate(a, b))
    assert c.get_output() == 8

def test_or():
    a = Wire('a')
    a.set_input(Constant(13))
    b = Wire('b')
    b.set_input(Constant(10))
    c = Wire('c')
    c.set_input(OrGate(a, b))
    assert c.get_output() == 15

def test_lshift():
    x = Wire('x')
    x.set_input(Constant(123))
    f = Wire('f')
    f.set_input(LShiftGate(x, Constant(2)))
    assert f.get_output() == 492

def test_rshift():
    y = Wire('y')
    y.set_input(Constant(456))
    g = Wire('g')
    g.set_input(RShiftGate(y, Constant(2)))
    assert g.get_output() == 114

def test_all():
    x = Wire('x')
    x.set_input(Constant(123))
    y = Wire('y')
    y.set_input(Constant(456))
    d = Wire('d')
    d.set_input(AndGate(x, y))
    e = Wire('e')
    e.set_input(OrGate(x, y))
    f = Wire('f')
    f.set_input(LShiftGate(x, Constant(2)))
    g = Wire('g')
    g.set_input(RShiftGate(y, Constant(2)))
    h = Wire('h')
    h.set_input(NotGate(x))
    i = Wire('i')
    i.set_input(NotGate(y))

    assert d.get_output() == 72
    assert e.get_output() == 507
    assert f.get_output() == 492
    assert g.get_output() == 114
    assert h.get_output() == 65412
    assert i.get_output() == 65079
    assert x.get_output() == 123
    assert y.get_output() == 456


def test_parse_constant_instruction():
    instruction = Instruction.parse('123 -> x')
    assert instruction == Instruction(None, [123], 'x')

def test_parse_not_instruction():
    instruction = Instruction.parse('NOT a -> b')
    assert instruction == Instruction(NotGate, ['a'], 'b')

def test_parse_and_instruction():
    instruction = Instruction.parse('a AND b -> c')
    assert instruction == Instruction(AndGate, ['a', 'b'], 'c')

def test_circuit_1():
    circuit = Circuit()

    circuit.add_instruction(Instruction.parse('5 -> a'))
    circuit.add_instruction(Instruction.parse('12 -> b'))
    circuit.add_instruction(Instruction.parse('a OR b -> c'))

    assert circuit.get_wire('a').get_output() == 5
    assert circuit.get_wire('b').get_output() == 12
    assert circuit.get_wire('c').get_output() == 13

def test_circuit_2():
    circuit = Circuit()

    circuit.add_instruction(Instruction.parse('5 -> a'))
    circuit.add_instruction(Instruction.parse('12 -> b'))
    circuit.add_instruction(Instruction.parse('a AND b -> c'))

    assert circuit.get_wire('a').get_output() == 5
    assert circuit.get_wire('b').get_output() == 12
    assert circuit.get_wire('c').get_output() == 4

def test_circuit_3():
    circuit = Circuit()

    circuit.add_instruction(Instruction.parse('5 -> a'))
    circuit.add_instruction(Instruction.parse('a -> b'))
    circuit.add_instruction(Instruction.parse('b -> c'))

    assert circuit.get_wire('c').get_output() == 5

def test_circuit_4():
    circuit = Circuit()

    circuit.add_instruction(Instruction.parse('123 -> x'))
    circuit.add_instruction(Instruction.parse('456 -> y'))
    circuit.add_instruction(Instruction.parse('x AND y -> d'))
    circuit.add_instruction(Instruction.parse('x OR y -> e'))
    circuit.add_instruction(Instruction.parse('x LSHIFT 2 -> f'))
    circuit.add_instruction(Instruction.parse('y RSHIFT 2 -> g'))
    circuit.add_instruction(Instruction.parse('NOT x -> h'))
    circuit.add_instruction(Instruction.parse('NOT y -> i'))

    assert circuit.get_wire('d').get_output() == 72
    assert circuit.get_wire('e').get_output() == 507
    assert circuit.get_wire('f').get_output() == 492
    assert circuit.get_wire('g').get_output() == 114
    assert circuit.get_wire('h').get_output() == 65412
    assert circuit.get_wire('i').get_output() == 65079
    assert circuit.get_wire('x').get_output() == 123
    assert circuit.get_wire('y').get_output() == 456
