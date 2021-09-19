#!/usr/bin/env python3
import re

STATS_REGEX = re.compile(
    r'(?P<name>\w+) can fly (?P<fly_speed>\d+) km/s for (?P<fly_time>\d+) seconds, '
    r'but then must rest for (?P<rest_time>\d+) seconds.'
)

TIME_LIMIT = 2503

def main():
    reindeer_stats = read_reindeer_stats()

    max_distance = 0

    for reindeer in reindeer_stats:
        dist = calculate_distance(reindeer, TIME_LIMIT)

        if dist > max_distance:
            max_distance = dist

    print(f'Max Distance: {max_distance} km')


def read_reindeer_stats():
    with open('input.txt') as file:
        return [parse_reindeer_stats(line.strip()) for line in file]


def parse_reindeer_stats(line):
    match = re.match(STATS_REGEX, line)

    return {
        'name': match.group('name'),
        'fly_speed': int(match.group('fly_speed')),
        'fly_time': int(match.group('fly_time')),
        'rest_time': int(match.group('rest_time'))
    }


def calculate_distance(reindeer, time):
    is_resting = False

    current_time = 0
    distance = 0

    while current_time != time:
        time_remaining = time - current_time

        if is_resting:
            part_duration = reindeer['rest_time']
        else:
            part_duration = reindeer['fly_time']

        next_part_duartion = min(part_duration, time_remaining)
        current_time += next_part_duartion

        if not is_resting:
            distance += part_duration * reindeer['fly_speed']

        is_resting = not is_resting

    return distance


if __name__ == '__main__':
    main()
