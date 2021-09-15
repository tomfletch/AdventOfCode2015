#!/usr/bin/env python3

class Box:
    def __init__(self, l, w, h):
        self.lengths = [l, w, h]
        self.areas = [l*w, w*h, l*h]

    def get_total_area(self):
        return sum(self.areas)*2

    def get_smallest_area(self):
        return min(self.areas)

    def get_total_wrapping_paper(self):
        return self.get_total_area() + self.get_smallest_area()

    def __str__(self):
        return 'x'.join(map(str, self.lengths))


def create_box(line):
    line_parts = line.split('x')
    line_parts = list(map(int, line_parts))
    return Box(*line_parts)


def read_boxes():
    with open('input.txt') as file:
        return [create_box(line) for line in file]


def main():
    boxes = read_boxes()

    areas = [box.get_total_wrapping_paper() for box in boxes]
    total_area = sum(areas)

    print(f'Total area: {total_area}')


if __name__ == '__main__':
    main()
