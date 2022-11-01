#!/usr/bin/env python3

from abc import ABC
from dataclasses import dataclass
import math
from typing import List, Type
import copy

@dataclass
class Character:
    hit_points: int
    armor: int = 0
    mana: int = 0
    damage: int = 0

class Spell(ABC):
    name: str
    mana_cost: int
    attacker: Character
    target: Character
    timer: int = 0

    def __init__(self, name: str, mana_cost: int, duration: int = 0):
        self.name = name
        self.mana_cost = mana_cost
        self.timer = duration

    def __repr__(self):
        return self.name

    def cast(self, attacker: Character, target: Character):
        self.attacker = attacker
        self.target = target
        self.attacker.mana -= self.mana_cost
        self.immediate_effect()

    def has_ended(self):
        return self.timer == 0

    def immediate_effect(self):
        pass

    def do_effect(self):
        if self.timer == 0:
            return

        self.effect()
        self.timer -= 1

        if (self.timer == 0):
            self.end_effect()

    def effect(self):
        pass

    def end_effect(self):
        pass


class MagicMissile(Spell):
    def __init__(self):
        super().__init__('Magic Missile', 53)

    def immediate_effect(self):
        self.target.hit_points -= 4


class Drain(Spell):
    def __init__(self):
        super().__init__('Drain', 73)

    def immediate_effect(self):
        self.target.hit_points -= 2
        self.attacker.hit_points += 2


class Shield(Spell):
    def __init__(self):
        super().__init__('Shield', 113, duration=6)

    def immediate_effect(self):
        self.attacker.armor += 7

    def end_effect(self):
        self.attacker.armor -= 7

class Poison(Spell):
    def __init__(self):
        super().__init__('Poison', 173, duration=6)

    def effect(self):
        self.target.hit_points -= 3

class Recharge(Spell):
    def __init__(self):
        super().__init__('Recharge', 229, duration=5)

    def effect(self):
        self.attacker.mana += 101

SPELL_OPTIONS: List[Type[Spell]] = [MagicMissile, Drain, Shield, Poison, Recharge]


@dataclass
class GameState:
    player: Character
    boss: Character
    cast_spells: List[str]
    active_spells: List[Spell]
    player_turn: bool
    mana_cost: int

def copy_game_state(game_state: GameState):
    new_game_state = copy.deepcopy(game_state)

    for spell in new_game_state.active_spells:
        spell.attacker = new_game_state.player
        spell.target = new_game_state.boss

    return new_game_state

def generate_new_game_states(game_state: GameState):
    next_game_state = copy_game_state(game_state)

    next_game_state.player_turn = not next_game_state.player_turn

    player = next_game_state.player
    boss = next_game_state.boss

    for spell in next_game_state.active_spells:
        spell.do_effect()

    next_game_state.active_spells = [s for s in next_game_state.active_spells if not s.has_ended()]

    if boss.hit_points <= 0:
        return [next_game_state]

    if game_state.player_turn:
        next_game_states: List[GameState] = []

        for next_spell_class in SPELL_OPTIONS:
            if any(isinstance(s, next_spell_class) for s in next_game_state.active_spells):
                continue
            new_game_state = copy.deepcopy(next_game_state)

            next_spell = next_spell_class()

            if next_spell.mana_cost > next_game_state.player.mana:
                continue

            next_spell.cast(new_game_state.player, new_game_state.boss)
            new_game_state.active_spells.append(next_spell)
            new_game_state.mana_cost += next_spell.mana_cost
            new_game_state.cast_spells.append(next_spell.name)
            next_game_states.append(new_game_state)

        return next_game_states
    else:
        boss_attack_damage = max(boss.damage - player.armor, 1)
        next_game_state.player.hit_points -= boss_attack_damage

        if next_game_state.player.hit_points <= 0:
            return []

        return [next_game_state]


def main():
    player = Character(50, mana=500)
    boss = Character(51, damage=9)

    game_state = GameState(player, boss, cast_spells=[], active_spells=[], player_turn=True, mana_cost=0)

    game_states = [game_state]

    current_minimum = math.inf

    while game_states:
        current_game_state = game_states.pop(0)
        # print('Looking at game state with mana cost:', current_game_state.mana_cost)

        if current_game_state.boss.hit_points <= 0:
            if current_game_state.mana_cost < current_minimum:
                current_minimum = current_game_state.mana_cost
                print('New minimum:', current_minimum)

        new_game_states = generate_new_game_states(current_game_state)

        for new_game_state in new_game_states:
            if new_game_state.mana_cost < current_minimum:
                game_states.append(new_game_state)

    print('Min cost:', current_minimum)

if __name__ == '__main__':
    main()
