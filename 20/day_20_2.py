#!/usr/bin/env python3

import math

def main():
    h = 0
    presents = 0
    while presents < 29000000:
        h += 1
        presents = get_presents(h)

    print(f'House: {h}')

def get_presents(n):
    divisors = get_divisors(n)
    return sum([d*11 for d in divisors])

def get_divisors(n):
    divisors = set()
    for a in range(1, math.ceil(math.sqrt(n)+1)):
        if n % a == 0:
            if a * 50 >= n:
                divisors.add(a)
            if (n // a) * 50 >= n:
                divisors.add(n // a)
    return divisors

if __name__ == '__main__':
    main()
