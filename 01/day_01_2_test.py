from day_01_2 import determine_basement_position

def test_1():
    assert determine_basement_position(')') == 1

def test_2():
    assert determine_basement_position('()())') == 5

