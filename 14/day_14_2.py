#!/usr/bin/env python3
import re

STATS_REGEX = re.compile(
    r'(?P<name>\w+) can fly (?P<fly_speed>\d+) km/s for (?P<fly_time>\d+) seconds, '
    r'but then must rest for (?P<rest_time>\d+) seconds.'
)

TIME_LIMIT = 2503

class Reindeer:
    def __init__(self, name, fly_speed, fly_time, rest_time):
        self.name = name
        self.fly_speed = fly_speed
        self.fly_time = fly_time
        self.rest_time = rest_time

        self.distance = 0
        self.is_flying = True
        self.time_remaining = self.fly_time
        self.score = 0

    def update(self):
        self.time_remaining -= 1

        if self.is_flying:
            self.distance += self.fly_speed

        if self.time_remaining == 0:
            self.is_flying = not self.is_flying

            if self.is_flying:
                self.time_remaining = self.fly_time
            else:
                self.time_remaining = self.rest_time

    def inc_score(self):
        self.score += 1


def main():
    reindeer_stats = read_reindeer_stats()

    for _ in range(TIME_LIMIT):
        for reindeer in reindeer_stats:
            reindeer.update()

        max_distance = max([r.distance for r in reindeer_stats])
        top_reindeer = [r for r in reindeer_stats if r.distance == max_distance]

        for reindeer in top_reindeer:
            reindeer.inc_score()

    max_score = max(r.score for r in reindeer_stats)
    print(f'Max Points: {max_score}')


def read_reindeer_stats():
    with open('input.txt') as file:
        return [parse_reindeer_stats(line.strip()) for line in file]


def parse_reindeer_stats(line):
    match = re.match(STATS_REGEX, line)

    return Reindeer(
        match.group('name'),
        int(match.group('fly_speed')),
        int(match.group('fly_time')),
        int(match.group('rest_time'))
    )


if __name__ == '__main__':
    main()
