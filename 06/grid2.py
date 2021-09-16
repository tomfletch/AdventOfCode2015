from collections import namedtuple

Cell = namedtuple('Cell', ['x', 'y'])

class Grid:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self._init_lights()

    def _init_lights(self):
        self.lights = [[0]*self.width for _ in range(self.height)]

    def turn_on(self, from_cell: Cell, to_cell: Cell):
        self.for_lights_in_range(from_cell, to_cell, lambda l: l+1)

    def turn_off(self, from_cell: Cell, to_cell: Cell):
        self.for_lights_in_range(from_cell, to_cell, lambda l: l-1)

    def toggle(self, from_cell: Cell, to_cell: Cell):
        self.for_lights_in_range(from_cell, to_cell, lambda l: l+2)

    def for_lights_in_range(self, from_cell: Cell, to_cell: Cell, func):
        for y in range(from_cell.y, to_cell.y+1):
            for x in range(from_cell.x, to_cell.x+1):
                new_value = func(self.lights[y][x])

                if new_value < 0:
                    new_value = 0

                self.lights[y][x] = new_value

    def total_brightness(self):
        return sum(map(sum, self.lights))