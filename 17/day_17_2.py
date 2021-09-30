#!/usr/bin/env python3

class Containers(list):
    def remove_up_to_index(self, index):
        return Containers(self[index+1:])

def main():
    containers = read_containers()
    total = 150

    container_combinations = get_container_combinations(containers, total)

    min_length = len(container_combinations[0])
    min_count = 0

    for combination in container_combinations:
        if len(combination) < min_length:
            min_length = len(combination)
            min_count = 1
        elif len(combination) == min_length:
            min_count += 1

    print(f'Min containers combinations: {min_count}')


def get_container_combinations(containers: Containers, total: int):
    if total == 0:
        return [Containers()]

    combinations = []

    for index, container in enumerate(containers):
        if container <= total:
            new_containers = containers.remove_up_to_index(index)
            new_total = total - container

            new_combinations = get_container_combinations(new_containers, new_total)

            for new_combination in new_combinations:
                new_combination.insert(0, container)

            combinations.extend(new_combinations)

    return combinations


def read_containers():
    with open('input.txt') as file:
        return Containers([int(line) for line in file])


if __name__ == '__main__':
    main()
