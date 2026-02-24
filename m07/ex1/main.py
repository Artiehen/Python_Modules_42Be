from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck
from ex0.CreatureCard import CreatureCard


def main():
    try:
        spell = SpellCard('Lightning Bolt', 5,
                          'rare', 'Deal 3 damage to target')
        artifacts = ArtifactCard('Mana crystal', 2, 'rare',
                                 4, 'Permanent: +1 mana per turn')
        creatures = CreatureCard('Fire Dragon', 5, 'Legendary', 3, 5)

        deck = Deck()
        for card in [spell, artifacts, creatures]:
            deck.add_card(card)

        print("\n=== DataDeck Deck Builder ===")
        print("Building deck with different card types...")
        print(f"{deck.get_deck_stats()}")
        deck.shuffle()
        card1 = deck.draw_card()

        print("\nDrawing and playing cards:\n")
        print(f"Drew: {card1.name}")
        print(f"Play result: {card1.play({})}")

        deck.shuffle()
        card2 = deck.draw_card()

        print("\nDrawing and playing cards:\n")
        print(f"Drew: {card2.name}")
        print(f"Play result: {card2.play({})}")

        deck.shuffle()
        card3 = deck.draw_card()

        print("\nDrawing and playing cards:\n")
        print(f"Drew: {card3.name}")
        print(f"Play result: {card3.play({})}")

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
