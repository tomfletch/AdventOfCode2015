#!/usr/bin/env python3
import re

def encode_string(string):
    encoded = ''

    for char in string:
        if char == '"':
            encoded += '\\"'
        elif char == '\\':
            encoded += '\\\\'
        else:
            encoded += char

    return f'"{encoded}"'


def main():
    strings = read_code_lines()

    string_length = sum([len(s) for s in strings])
    print(f'Original length: {string_length}')

    encoded_length = sum([len(encode_string(s)) for s in strings])
    print(f'Encoded length: {encoded_length}')

    result = encoded_length - string_length
    print(f'Result: {result}')


def read_code_lines():
    with open('input.txt') as file:
        return [line.rstrip() for line in file]

if __name__ == '__main__':
    main()