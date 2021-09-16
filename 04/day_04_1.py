#!/usr/bin/env python3

import hashlib


def lowest_suffix(key):
    suffix = 1

    while True:
        md5 = calculate_md5(key, suffix)

        if starts_with_five_zeros(md5):
            break

        suffix += 1

    return suffix


def calculate_md5(key, suffix):
    value = key + str(suffix)
    md5 = hashlib.md5(str(value).encode('utf-8'))
    return md5.hexdigest()


def starts_with_five_zeros(value):
    return value.startswith('00000')


def main():
    key = 'iwrupvqb'
    suffix = lowest_suffix(key)
    print(f'Suffix: {suffix}')

if __name__ == '__main__':
    main()