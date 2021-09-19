#!/usr/bin/env python3
import re
from itertools import permutations

RULE_REGEX = re.compile(
    r'(?P<person_1>\w+) would (?P<gain_or_lose>\w+) (?P<units>\d+) '
    r'happiness units by sitting next to (?P<person_2>\w+)\.'
)


def main():
    rules = read_rules()
    people = set([rule[0] for rule in rules])

    for person in people:
        rules.update({('Me', person): 0})
        rules.update({(person, 'Me'): 0})

    people.add('Me')

    arrangements = permutations(people)

    max_happiness = 0

    for arrangement in arrangements:
        happiness = calculate_happiness(rules, arrangement)

        if happiness > max_happiness:
            max_happiness = happiness

    print(f'Optimum Happiness: {max_happiness}')


def read_rules():
    rules = {}

    with open('input.txt') as file:
        for line in file:
            rule = parse_rule(line.strip())
            rules.update(rule)

    return rules


def parse_rule(line):
    match = re.match(RULE_REGEX, line)
    person_1 = match.group('person_1')
    person_2 = match.group('person_2')
    gain_or_lose = match.group('gain_or_lose')
    units = int(match.group('units'))

    if gain_or_lose == 'lose':
        units = -units

    return {(person_1, person_2): units}


def calculate_happiness(rules, arrangement):
    happiness = 0

    for i in range(len(arrangement)):
        person_1 = arrangement[i]
        person_2 = arrangement[(i+1)%len(arrangement)]

        happiness += get_happiness(rules, person_1, person_2)
        happiness += get_happiness(rules, person_2, person_1)

    return happiness

def get_happiness(rules, person_1, person_2):
    return rules[(person_1, person_2)]


if __name__ == '__main__':
    main()
