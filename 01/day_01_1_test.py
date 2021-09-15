from day_01_1 import determine_floor

def test_floor_0():
    assert determine_floor('(())') == 0
    assert determine_floor('()()') == 0

def test_floor_3():
    assert determine_floor('(((') == 3
    assert determine_floor('(()(()(') == 3
    assert determine_floor('))(((((') == 3

def test_floor_negative_1():
    assert determine_floor('())') == -1
    assert determine_floor('))(') == -1

def test_floor_negative_3():
    assert determine_floor(')))') == -3
    assert determine_floor(')())())') == -3
