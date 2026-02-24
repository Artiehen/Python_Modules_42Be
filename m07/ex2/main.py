from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from ex2.EliteCard import EliteCard
from typing import Any, List


def get_methods(cls: Any) -> List[str]:
    return [m for m in dir(cls) if not m.startswith('_')]


def main():
    try:
        enemy = ["Enemy1", "Enemy2"]
        arcane_warrior = EliteCard("Arcane Warrior", 2, "Legendary",
                                   5, 50, "Paladin")

        print("\n=== DataDeck Ability System ===\n")
        print("EliteCard capabilities:")
        print(f"- Card: {get_methods(Card)}")
        print(f"- Combatable: {get_methods(Combatable)}")
        print(f"- Magical: {get_methods(Magical)}")

        print(f"Playing {arcane_warrior.name} (Elite Card):\n")
        print("Combat Phase:")
        print(arcane_warrior.attack("Enemy"))
        print("Defense Result:")
        print(arcane_warrior.defend(2))

        print("\nMagic Phase:")
        print(f"Spell cast: {arcane_warrior.cast_spell('Fireball', enemy)}")
        print(f"Mana Channel: {arcane_warrior.channel_mana(3)}")

        print("\nMultiple interface implementation successful!")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
