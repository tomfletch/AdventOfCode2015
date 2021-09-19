#!/usr/bin/env python3
import json

def sum_numbers(data):
    if isinstance(data, list):
        return sum(map(sum_numbers, data))
    if isinstance(data, dict):
        if 'red' in data.values():
            return 0
        return sum(map(sum_numbers, data.values()))
    if isinstance(data, int):
        return data
    return 0


def main():
    with open('input.txt') as file:
        data = json.load(file)
    total = sum_numbers(data)
    print(f'Total: {total}')


if __name__ == '__main__':
    main()
