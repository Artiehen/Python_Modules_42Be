from ex0.CreatureCard import CreatureCard


def main():
    try:

        fire_dragon = CreatureCard(
            name='Fire Dragon',
            cost=5,
            rarity='Legendary',
            attack=7,
            health=5
            )

        goblin_warrior = CreatureCard(
            name='Goblin Warrior',
            cost=5,
            rarity='Legendary',
            attack=7,
            health=5)

        print("\n=== DataDeck Card Foundation ===")
        print("\nTesting Abstract Base Class Design:\n")

        print("CreatureCard Info:")
        x = "mana available"

        print(fire_dragon.get_card_info())
        print(f'Playing {fire_dragon.name} with {fire_dragon.cost} {x}')
        print(f"Playable: {fire_dragon.is_playable(fire_dragon.cost)}")
        print(f"Play result: {fire_dragon.play({})}")

        print('Fire Dragon attacks Goblin Warrior:')
        print(f'Attack result: {fire_dragon.attack_target(goblin_warrior)}')

        print(f'Testing insufficient mana ({3} available)')
        print(f"Playable: {fire_dragon.is_playable(fire_dragon.cost)}")

        print('Abstract pattern successfully demonstrated!')
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
