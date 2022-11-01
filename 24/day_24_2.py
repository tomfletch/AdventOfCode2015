#!/usr/bin/env python3
from typing import List, Set

def main():
    weights = read_package_weights()
    total_weight = sum(weights)
    weight_per_group = total_weight // 4

    group_options = weights_that_sum_options(weights, weight_per_group)
    print('Found groups')
    group_options.sort(key=lambda option: (len(option), multiply_set(option)))
    print('Sorted groups')
    grouping_option = next(find_grouping_options(group_options))

    print('QE of first group:', multiply_set(grouping_option[0]))

def multiply_set(s: Set[int]):
    total = 1

    for item in s:
        total *= item

    return total

def find_grouping_options(group_options: List[Set[int]]):
    for group_1 in group_options:

        for group_2 in group_options:
            if group_2.intersection(group_1):
                continue

            for group_3 in group_options:
                if group_3.intersection(group_1) or group_3.intersection(group_2):
                    continue

                for group_4 in group_options:
                    if group_4.intersection(group_1) or group_4.intersection(group_2) or group_4.intersection(group_3):
                        continue

                    yield [group_1, group_2, group_3, group_4]


def weights_that_sum_options(weights: Set[int], total: int):
    options: List[Set[int]] = []

    for weight in weights:
        if weight < total:
            remaining_weights = {w for w in weights if w > weight}

            if remaining_weights:
                remaining_total = total - weight
                remaining_weights_options = weights_that_sum_options(remaining_weights, remaining_total)

                for remaining_weights in remaining_weights_options:
                    options.append({weight} | remaining_weights)
        elif weight == total:
            options.append({weight})

    return options


def read_package_weights():
    with open('input.txt') as file:
        return {int(line) for line in file}

if __name__ == '__main__':
    main()
