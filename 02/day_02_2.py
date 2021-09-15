#!/usr/bin/env python3

class Box:
    def __init__(self, l, w, h):
        self.lengths = [l, w, h]

    def get_min_perimeter(self):
        [l, w, h] = self.lengths
        return min(l+w, w+h, l+h)*2

    def get_volume(self):
        return self.lengths[0] * self.lengths[1] * self.lengths[2]

    def get_ribbon_length(self):
        return self.get_min_perimeter() + self.get_volume()

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

    ribbon_lengths = [box.get_ribbon_length() for box in boxes]
    total_ribbon_length = sum(ribbon_lengths)

    print(f'Total ribbon length: {total_ribbon_length}')


if __name__ == '__main__':
    main()
