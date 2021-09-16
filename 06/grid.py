from collections import namedtuple

Cell = namedtuple('Cell', ['x', 'y'])

class Grid:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self._init_lights()

    def _init_lights(self):
        self.lights = [[False]*self.width for _ in range(self.height)]

    def turn_on(self, from_cell: Cell, to_cell: Cell):
        self.for_lights_in_range(from_cell, to_cell, lambda l: True)

    def turn_off(self, from_cell: Cell, to_cell: Cell):
        self.for_lights_in_range(from_cell, to_cell, lambda l: False)

    def toggle(self, from_cell: Cell, to_cell: Cell):
        self.for_lights_in_range(from_cell, to_cell, lambda l: not l)

    def for_lights_in_range(self, from_cell: Cell, to_cell: Cell, func):
        for y in range(from_cell.y, to_cell.y+1):
            for x in range(from_cell.x, to_cell.x+1):
                self.lights[y][x] = func(self.lights[y][x])

    def count_on(self):
        return sum(map(sum, self.lights))