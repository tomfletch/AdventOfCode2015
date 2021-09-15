from day_02_2 import Box

def test_min_perimeter():
    box = Box(2, 3, 4)
    assert box.get_min_perimeter() == 10

def test_volume():
    box = Box(2, 3, 4)
    assert box.get_volume() == 24

def test_ribbon_length():
    box = Box(2, 3, 4)
    assert box.get_ribbon_length() == 34

def test_ribbon_length_2():
    box = Box(1, 1, 10)
    assert box.get_ribbon_length() == 14
