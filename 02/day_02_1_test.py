from day_02_1 import Box, create_box

def test_smallest_side():
    box = Box(2, 3, 4)
    assert box.get_smallest_area() == 6

def test_total_area():
    box = Box(2, 3, 4)
    assert box.get_total_area() == 52

def test_total_wrapping_paper():
    box = Box(2, 3, 4)
    assert box.get_total_wrapping_paper() == 58

def test_total_wrapping_paper_2():
    box = Box(1, 1, 10)
    assert box.get_total_wrapping_paper() == 43

def test_create_box():
    box = create_box('4x3x2')
    assert box.get_total_wrapping_paper() == 58
