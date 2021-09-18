#!/usr/bin/env python3
import re

def count_string_length(code):
    escaped = code[1:-1]
    escaped = escaped.replace(R'\\', '_')
    escaped = escaped.replace(R'\"', '_')
    escaped = re.sub(r'\\x[0-9A-Fa-f]{2}', '_', escaped)
    return len(escaped)

def main():
    strings = read_code_lines()

    total_length = sum([len(s) for s in strings])
    print(f'Total length: {total_length}')

    string_length = sum([count_string_length(s) for s in strings])
    print(f'String length: {string_length}')

    result = total_length - string_length
    print(f'Result: {result}')


def read_code_lines():
    with open('input.txt') as file:
        return [line.rstrip() for line in file]

if __name__ == '__main__':
    main()