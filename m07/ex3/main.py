
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine


def main():
    try:
        print("\n=== DataDeck Game Engine ===\n")

        engine = GameEngine()
        factory = FantasyCardFactory()
        factory.create_themed_deck(8)
        strategy = AggressiveStrategy()
        print("Configuring Fantasy Card Game...")
        engine.configure_engine(factory, strategy)
        print(f"Available types: {factory.get_supported_types()}")

        print("\nSimulating aggressive turn...")
        h = "hand:"
        print(h, [f"{card.name} ({card.cost})" for card in factory.cards])

        print("\nTurn execution:")
        print(f"Actions: {engine.simulate_turn()}")
        print("\nGame Report:")
        print(engine.get_engine_status())
        x = "Abstract Factory+Strategy Pattern: Maximum flexibility achieved!"
        print(f"\n{x}")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
