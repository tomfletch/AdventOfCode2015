#!/usr/bin/env python3

from typing import List, Set, Tuple

Rule = Tuple[str, str]

def main():
    rules, molecule = read_input()

    possible_molecules = generate_possible_molecules(rules, molecule)
    print('Distinct molecules:', len(possible_molecules))

def generate_possible_molecules(rules: List[Rule], molecule: str):
    possible_molecules: Set[str] = set()

    for from_molecule, to_molecule in rules:
        possible_molecules |= apply_rule_options(from_molecule, to_molecule, molecule)

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

    rules: List[Rule] = []

    for line in rule_lines:
        from_molecule, to_molecule = line.split(' => ', 1)
        rules.append((from_molecule, to_molecule))

    return rules, molecule

if __name__ == '__main__':
    main()
