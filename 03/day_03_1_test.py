from day_03_1 import count_houses_visited

def test_1():
    assert count_houses_visited('>') == 2

def test_2():
    assert count_houses_visited('^>v<') == 4

def test_3():
    assert count_houses_visited('^v^v^v^v^v') == 2
