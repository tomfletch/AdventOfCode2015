#!/usr/bin/env python3

def look_and_say(input: str) -> str:
    output = ''

    last = ''
    last_count = 0

    for char in input:
        if char != last:
            if last_count != 0:
                output += f'{last_count}{last}'
            last = char
            last_count = 0
        last_count += 1

    if last_count != 0:
        output += f'{last_count}{last}'

    return output


def main():
    input = '3113322113'
    for _ in range(40):
        input = look_and_say(input)
    print(f'Result Length: {len(input)}')

if __name__ == '__main__':
    main()
