#!/usr/bin/env python3
from dataclasses import dataclass
import math

@dataclass
class Character:
    hit_points: int
    damage: int
    armor: int

@dataclass
class Item:
    name: str
    cost: int
    damage: int
    armor: int

WEAPONS = [
    Item('Dagger', 8, 4, 0),
    Item('Shortsword', 10, 5, 0),
    Item('Warhammer', 25, 6, 0),
    Item('Longsword', 40, 7, 0),
    Item('Greataxe', 74, 8, 0)
]

ARMOR = [
    Item('Leather', 13, 0, 1),
    Item('Chainmail', 31, 0, 2),
    Item('Splintmail', 53, 0, 3),
    Item('Bandedmail', 75, 0, 4),
    Item('Platemail', 102, 0, 5)
]

RINGS = [
    Item('Damage +1', 25, 1, 0),
    Item('Damage +2', 50, 2, 0),
    Item('Damage +3', 100, 3, 0),
    Item('Defense +1', 20, 0, 1),
    Item('Defense +2', 40, 0, 2),
    Item('Defense +3', 80, 0, 3)
]

def main():

    max_cost = 0

    for items in iterate_item_options():
        player = Character(100, 0, 0)
        boss = Character(103, 9, 2)

        total_cost = 0

        for item in items:
            player.damage += item.damage
            player.armor += item.armor
            total_cost += item.cost

        if total_cost < max_cost:
            continue

        if not does_player_win(player, boss):
            max_cost = total_cost

    print('Maximum cost:', max_cost)


def iterate_item_options():
    for weapon in WEAPONS:
        for i in range(-1, len(ARMOR)):

            for j in range(-1, len(RINGS)):
                for k in range(j, len(RINGS)):
                    if j != -1 and j == k:
                        continue

                    items = [weapon]

                    if i != -1:
                        items.append(ARMOR[i])

                    if j != -1:
                        items.append(RINGS[j])

                    if k != -1:
                        items.append(RINGS[k])

                    yield items



def does_player_win(player: Character, boss: Character):
    player_turns_to_win = turns_to_win(player, boss)
    boss_turns_to_win = turns_to_win(boss, player)
    return player_turns_to_win <= boss_turns_to_win

def turns_to_win(attacker: Character, defender: Character):
    hit_points_per_attack = max(attacker.damage - defender.armor, 1)
    return math.ceil(defender.hit_points / hit_points_per_attack)

if __name__ == '__main__':
    main()
