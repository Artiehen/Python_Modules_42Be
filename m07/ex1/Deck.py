from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
import random


class Deck:
    def __init__(self) -> None:
        self.cards = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)
        return None

    def draw_card(self) -> Card:
        if not self.cards:
            return None
        return self.cards.pop()

    def get_deck_stats(self) -> dict:
        total_cards = len(self.cards)
        creatures = 0
        spells = 0
        artifacts = 0
        total_cost = 0

        for card in self.cards:
            total_cost += card.cost
            if isinstance(card, CreatureCard):
                creatures += 1
            elif isinstance(card, ArtifactCard):
                artifacts += 1
            elif isinstance(card, SpellCard):
                spells += 1

            if total_cards > 0:
                cost_avg = total_cost / total_cards
            else:
                cost_avg = 0.0
        return {"total_cards": total_cards,
                "creatures": creatures,
                "spells": spells,
                "artifacts": artifacts,
                "average_cost": cost_avg
                }
