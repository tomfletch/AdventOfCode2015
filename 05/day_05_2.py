#!/usr/bin/env python3

def is_nice(value):
    return (
        contains_duplicate_pair(value) and
        contains_duplicate_letter(value)
    )

def contains_duplicate_pair(value):
    for index in range(0, len(value) - 3):
        pair = value[index:index+2]

        for compare_index in range(index + 2, len(value) - 1):
            compare_pair = value[compare_index:compare_index+2]

            if pair == compare_pair:
                return True

            compare_index

    return False


def contains_duplicate_letter(value):
    for index in range(0, len(value) - 2):
        if value[index] == value[index+2]:
            return True

    return False


def main():
    strings = read_strings()
    nice_strings = list(filter(is_nice, strings))

    print(f'Nice strings: {len(nice_strings)}')


def read_strings():
    with open('input.txt') as file:
        return [line.rstrip() for line in file]

if __name__ == '__main__':
    main()