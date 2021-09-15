from day_03_2 import count_houses_visited

def test_1():
    assert count_houses_visited('^v') == 3

def test_2():
    assert count_houses_visited('^>v<') == 3

def test_3():
    assert count_houses_visited('^v^v^v^v^v') == 11
