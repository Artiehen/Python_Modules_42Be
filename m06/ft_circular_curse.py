#!/usr/bin/python3

from alchemy.grimoire.validator import validate_ingredients
from alchemy.grimoire.spellbook import record_spell


def circular_curse():
    try:
        print("=== Circular Curse Breaking ===")
        print("\nTesting ingredient validation:")
        a = "validate_ingredients('fire air'):"
        b = "validate_ingredients('dragon scales'):"
        c = 'record_spell("Fireball", "fire air"):'
        d = 'record_spell("Dark Magic", "shadow"):'
        e = 'record_spell("Lightning", "air"):'
        print(f"{a} {validate_ingredients("fire air")}")
        print(f"{b} {validate_ingredients("dragon scales")}")

        print("\nTesting spell recording with validation:")
        print(f'{c} {record_spell("Fireball", "fire air"):}')
        print(f'{d} {record_spell("Dark Magic", "shadow"):}')

        print("\nTesting late import technique:")
        print(f'{e} {record_spell("Lightning", "air"):}')

        print("\nCircular dependency curse avoided using late imports!")
        print("All spells processed safely!")
    except Exception as e:
        print(e)


circular_curse()
