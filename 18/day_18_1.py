#!/usr/bin/env python3

class Light:
    CHAR_ON = '#'
    CHAR_OFF = '.'

    def __init__(self, is_on):
        self.is_on = is_on

    def __str__(self):
        return [Light.CHAR_OFF, Light.CHAR_ON][self.is_on]

    @staticmethod
    def create_from_char(char):
        return Light(char == Light.CHAR_ON)

class LightGrid:

    def __init__(self, grid):
        self.grid = grid
        self.height = len(grid)
        self.width = len(grid[0])

    def step(self):
        new_grid = []

        for y in range(self.height):
            new_row = []

            for x in range(self.width):
                new_row.append(self.next_light_at(x, y))

            new_grid.append(new_row)

        self.grid = new_grid

    def next_light_at(self, x, y):
        currently_on = self.grid[y][x].is_on
        on_neighbours = self.count_on_neighbours(x, y)

        if currently_on:
            is_on = (on_neighbours in [2, 3])
        else:
            is_on = (on_neighbours == 3)

        return Light(is_on)

    def count_on_neighbours(self, x, y):
        on_lights = 0

        for yc in range(y-1, y+2):
            if yc < 0 or yc >= self.height:
                continue

            for xc in range(x-1, x+2):
                if xc < 0 or xc >= self.width:
                    continue

                if xc == x and yc == y:
                    continue

                if self.grid[yc][xc].is_on:
                    on_lights += 1

        return on_lights

    def count_on_lights(self):
        count = 0

        for row in self.grid:
            for light in row:
                if light.is_on:
                    count += 1

        return count

    def __str__(self):
        row_strings = []

        for row in self.grid:
            row_strings.append(''.join([str(light) for light in row]))

        return '\n'.join(row_strings)


def main():
    light_grid = read_light_grid()

    for _ in range(100):
        light_grid.step()

    on_lights_count = light_grid.count_on_lights()
    print(f'On lights: {on_lights_count}')


def read_light_grid():
    with open('input.txt') as file:
        grid = []
        for line in file:
            grid.append([Light.create_from_char(c) for c in line.strip()])
        return LightGrid(grid)


if __name__ == '__main__':
    main()
