#!/usr/bin/env python3

def main():
    print(get_code_at(2981, 3075))

def get_code_at(row: int, col: int):
    index = code_index(row, col)

    code = 20151125

    for i in range(index - 1):
        code = (code * 252533) % 33554393

    return code

def code_index(row: int, col: int):
    return triangle(row + col - 1) - (row - 1)

def triangle(n: int):
    return n * (n + 1) // 2

if __name__ == '__main__':
    main()
