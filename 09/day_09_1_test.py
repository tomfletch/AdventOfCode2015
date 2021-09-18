from day_09_1 import Map

def test_add_two_locations():
    m = Map()
    m.add_distance('A', 'B', 2)
    assert m.get_distance('A', 'B') == 2

def test_reverse_distance():
    m = Map()
    m.add_distance('A', 'B', 2)
    assert m.get_distance('B', 'A') == 2

def test_path_distance():
    m = Map()
    m.add_distance('A', 'B', 2)
    m.add_distance('B', 'C', 4)
    m.add_distance('C', 'D', 5)
    assert m.get_path_distance(['A', 'B', 'C', 'D']) == 11

def test_enumerate_locations():
    m = Map()
    m.add_distance('A', 'B', 2)
    m.add_distance('B', 'C', 4)
    m.add_distance('A', 'C', 1)
    paths = m.get_all_paths()
    assert len(paths) == 6

def test_shortest_distance():
    m = Map()
    m.add_distance('London', 'Dublin', 464)
    m.add_distance('London', 'Belfast', 518)
    m.add_distance('Dublin', 'Belfast', 141)
    assert m.get_shortest_distance() == 605

