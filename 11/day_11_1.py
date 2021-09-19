#!/usr/bin/env python3


def increment_letter(letter):
    if letter == 'z':
        return 'a'

    return chr(ord(letter) + 1)


def increment_password(password):
    password = password

    do_increment = True
    reversed_new_password = []

    for character in reversed(password):
        if do_increment:
            new_character = increment_letter(character)
        else:
            new_character = character

        reversed_new_password.append(new_character)

        if new_character != 'a':
            do_increment = False

    return ''.join(reversed(reversed_new_password))


def contains_increasing_letters(password):
    increasing_count = 1
    last_char = password[0]

    for char in password[1:]:
        if char == chr(ord(last_char) + 1):
            increasing_count += 1
        else:
            increasing_count = 1

        last_char = char

        if increasing_count == 3:
            return True

    return False


def contains_iol(password):
    for char in password:
        if char in 'iol':
            return True

    return False


def contains_two_pairs(password):
    last_char = password[0]
    pairs = 0

    for char in password[1:]:
        if char == last_char:
            pairs += 1
            last_char = ''

            if pairs == 2:
                return True
        else:
            last_char = char

    return False


def is_valid_password(password):
    return (
        contains_increasing_letters(password) and
        (not contains_iol(password)) and
        contains_two_pairs(password)
    )


def get_next_valid_password(password):
    while True:
        password = increment_password(password)

        if is_valid_password(password):
            return password


def main():
    next_password = get_next_valid_password('vzbxkghb')

    print(f'Next Password: {next_password}')


if __name__ == '__main__':
    main()