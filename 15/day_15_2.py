#!/usr/bin/env python3

class Ingredient:
    def __init__(self, name, properties):
        self.name = name
        self.properties = properties

    def __str__(self):
        properties = []
        for property_name, property_value in self.properties.items():
           properties.append(f'{property_name} {property_value}')

        properties = ', '.join(properties)
        return f'{self.name}: {properties}'


def main():
    ingredients = read_ingredients()

    recipies = create_recipies(len(ingredients), 100)

    max_score = 0

    for recipie in recipies:
        score = calculate_recipie_score(ingredients, recipie)

        if score > max_score:
            max_score = score

    print(f'Max score: {max_score}')


def calculate_recipie_score(ingredients, recipie):
    property_scores = {}

    for index, ingredient in enumerate(ingredients):
        quantity = recipie[index]

        for property_name, property_value in ingredient.properties.items():
            if property_name not in property_scores:
                property_scores[property_name] = 0

            property_scores[property_name] += quantity * property_value

    if property_scores['calories'] != 500:
        return 0

    total = 1

    for property_name, property_score in property_scores.items():
        if property_score < 0:
            return 0

        if property_name != 'calories':
            total *= property_score

    return total


def create_recipies(length, quantity):
    if length == 1:
        recipies = [[quantity]]
        return recipies

    recipies = []

    for q in range(quantity+1):
        recipie = [[q] + r for r in create_recipies(length-1, quantity-q)]
        recipies.extend(recipie)

    return recipies




def read_ingredients():
    with open('input.txt') as file:
        return [parse_ingredient(l.strip()) for l in file]


def parse_ingredient(line):
    name, property_str = line.split(': ')

    property_parts = property_str.split(', ')

    properties = {}

    for property_part in property_parts:
        property_name, property_value = property_part.split(' ')
        properties[property_name] = int(property_value)

    return Ingredient(name, properties)


if __name__ == '__main__':
    main()
