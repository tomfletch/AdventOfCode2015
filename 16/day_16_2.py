#!/usr/bin/env python3


class Sue:
    def __init__(self, id, properties):
        self.id = id
        self.properties = properties

    def __str__(self):
        property_pairs = []

        for name, value in self.properties.items():
            property_pairs.append(f'{name}: {value}')

        property_str = ', '.join(property_pairs)

        return f'Sue {self.id}: {property_str}'

    def is_match(self, properties):
        for key, value in properties.items():
            if key in self.properties:
                if key in ['cats', 'trees']:
                    if self.properties[key] <= value:
                        return False
                elif key in ['pomeranians', 'goldfish']:
                    if self.properties[key] >= value:
                        return False
                elif self.properties[key] != value:
                    return False
        return True


def main():
    sues = read_sues()

    properties = {
        'children': 3,
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes': 1
    }

    valid_sues = [sue for sue in sues if sue.is_match(properties)]

    for valid_sue in valid_sues:
        print(valid_sue)




def read_sues():
    with open('input.txt') as file:
        return [parse_sue(l) for l in file]


def parse_sue(line):
    head, body = line.split(': ', 1)
    id = head.split()[1]

    pairs_str = body.split(', ')

    properties = {}

    for pair_str in pairs_str:
        key, value = pair_str.split(': ')
        properties[key] = int(value)

    return Sue(id, properties)



if __name__ == '__main__':
    main()
