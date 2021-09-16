from grid import Grid, Cell

def test_init():
    g = Grid(3, 2)
    assert g.lights == [
        [False, False, False],
        [False, False, False]
    ]

def test_turn_on_all():
    g = Grid(3, 3)
    g.turn_on(Cell(0,0), Cell(2,2))
    assert g.lights == [
        [True, True, True],
        [True, True, True],
        [True, True, True]
    ]

def test_turn_on_off_all():
    g = Grid(3, 3)
    g.turn_on(Cell(0,0), Cell(2,2))
    g.turn_off(Cell(0,0), Cell(2,2))
    assert g.lights == [
        [False, False, False],
        [False, False, False],
        [False, False, False]
    ]

def test_turn_one_light_on():
    g = Grid(3, 3)
    g.turn_on(Cell(1,1), Cell(1,1))
    assert g.lights == [
        [False, False, False],
        [False, True, False],
        [False, False, False]
    ]

def test_turn_one_col_on():
    g = Grid(3, 3)
    g.turn_on(Cell(1,0), Cell(1,2))
    assert g.lights == [
        [False, True, False],
        [False, True, False],
        [False, True, False]
    ]

def test_toggle():
    g = Grid(3, 3)
    g.turn_on(Cell(1,0), Cell(1,2))
    g.toggle(Cell(0,0), Cell(1,1))
    assert g.lights == [
        [True, False, False],
        [True, False, False],
        [False, True, False]
    ]

def test_count_on_lights():
    g = Grid(3, 3)
    g.turn_on(Cell(1,0), Cell(1,2))
    assert g.count_on() == 3
