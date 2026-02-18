#!/usr/bin/python3
from alchemy.transmutation.basic import lead_to_gold, stone_to_gem
from alchemy.transmutation.advanced import philosophers_stone, elixir_of_life


def absolute_import():
    try:
        print("\nTesting Absolute Imports (from basic.py):")
        print(f"lead_to_gold(): {lead_to_gold()}")
        print(f"stone_to_gem(): {stone_to_gem()}")
    except Exception as e:
        print(e)


def relative_import():
    try:
        print("\nTesting Relative Imports (from advanced.py):")
        print(f"philosophers_stone(): {philosophers_stone()}")
        print(f"elixir_of_life: {elixir_of_life()}")
    except Exception as e:
        print(e)


def package_access():
    try:
        import alchemy
        print("\nTesting Package Access:")
        x = "alchemy.transmutation.lead_to_gold()"
        y = "alchemy.transmutation.philosophers_stone()"
        print(f"{x}:{alchemy.transmutation.lead_to_gold():}")
        print(f"{y}:{alchemy.transmutation.philosophers_stone():}")
    except Exception as e:
        print(e)


def pathway_debate():
    print("\n=== Pathway Debate Mastery ===")
    absolute_import()
    relative_import()
    package_access()
    print("\nBoth pathways work! Absolute: clear, Relative: concise")


pathway_debate()
