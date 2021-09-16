#!/usr/bin/env python3

def is_nice(value):
    return (
        contains_three_vowels(value) and
        contains_duplicate_letter(value) and
        not contains_bad_strings(value)
    )

def contains_three_vowels(value):
    vowels = 'aeiou'

    total = 0

    for vowel in vowels:
        total += value.count(vowel)

    return total >= 3

def contains_duplicate_letter(value):
    previous_letter = value[0]

    for letter in value[1:]:
        if letter == previous_letter:
            return True
        previous_letter = letter

    return False

def contains_bad_strings(value):
    bad_strings = ['ab', 'cd', 'pq', 'xy']

    for bad_string in bad_strings:
        if bad_string in value:
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