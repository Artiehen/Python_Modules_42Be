#!/usr/bin/python3

from .basic import lead_to_gold
from ..potions import healing_potion


def philosophers_stone():
    x = "Philosopher's stone created using"
    return f"{x} {lead_to_gold()} and {healing_potion()}"


def elixir_of_life():
    return "Elixir of life: eternal youth achieved!"
