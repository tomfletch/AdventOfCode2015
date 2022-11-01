#!/usr/bin/env python3

from collections import defaultdict
from functools import lru_cache
import math
from typing import List, Set, Tuple

Rule = Tuple[str, str]
Rules = List[Rule]

rules = []

def main():
    global rules
    input_rules, molecule = read_input()
    rules = input_rules

    fewest_steps = fewest_steps_to_e(molecule)

    print('Fewest steps:', fewest_steps)

def fewest_steps_to_e(molecule: str):
    molecules = [(molecule, 0)]

    while molecules:
        molecules.sort(key=lambda m: len(m[0]))
        this_molecule, this_molecule_steps = molecules.pop(0)
        print(f'Steps: {this_molecule_steps} - Molecule: {this_molecule}')

        if this_molecule == 'e':
            return this_molecule_steps

        next_molecules = generate_possible_molecules(this_molecule)

        for next_molecule in next_molecules:
            molecules.append((next_molecule, this_molecule_steps + 1))


@lru_cache(maxsize=None)
def generate_possible_molecules(molecule: str):
    possible_molecules: Set[str] = set()

    for rule in rules:
        possible_molecules |= apply_rule_options(rule[0], rule[1], molecule)

    return possible_molecules

def apply_rule_options(from_molecule: str, to_molecule: str, molecule: str):
    new_molecules: Set[str] = set()

    start = molecule.find(from_molecule)

    while start != -1:
        before = molecule[0:start]
        after = molecule[start+len(from_molecule):]
        new_molecule = before + to_molecule + after
        new_molecules.add(new_molecule)
        start = molecule.find(from_molecule, start+1)

    return new_molecules


def read_input():
    with open('input.txt') as file:
        input = file.read()

    all_rules, molecule = input.split('\n\n', 1)
    molecule = molecule.strip()

    rule_lines = [rule.strip() for rule in all_rules.split('\n')]

    rules: Rules = []

    for line in rule_lines:
        from_molecule, to_molecule = line.split(' => ', 1)
        rules.append((to_molecule, from_molecule))

    rules.sort(key=lambda r: -len(r[0]))

    return rules, molecule

if __name__ == '__main__':
    main()
