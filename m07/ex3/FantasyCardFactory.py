from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex3.CardFactory import CardFactory
import random


class FantasyCardFactory(CardFactory):
    def __init__(self) -> None:
        self.cards = []
        self.creature_count = 0
        self.artifact_count = 0
        self.spell_count = 0

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str):
            creature = CreatureCard(name_or_power, 3, "Common", 4, 10)
        elif isinstance(name_or_power, int):
            creature = CreatureCard(f"Creature {self.creature_count}",
                                    name_or_power, "Common", 4, 10)
            self.creature_count += 1
        else:
            creature = CreatureCard(f"Creature {self.creature_count}",
                                    2, "Common", 4, 10)
            self.creature_count += 1
        self.cards.append(creature)
        return creature

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str):
            spell = SpellCard(name_or_power, 7, "Rare", "damage 3")
        elif isinstance(name_or_power, int):
            spell = SpellCard(f"Spell {self.spell_count}", 3,
                              "Rare", f"damage {name_or_power}")
            self.spell_count += 1
        else:
            spell = SpellCard(f"Spell {self.spell_count}", 3,
                              "Rare", "damage 2")
            self.spell_count += 1
        self.cards.append(spell)
        return spell

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str):
            arti = ArtifactCard(name_or_power, 2, "Legendary", 3,
                                "Permanent: +1 mana per turn")
        elif isinstance(name_or_power, int):
            arti = ArtifactCard(f"Artifact {self.artifact_count}", 2,
                                "Legendary", 3,
                                f"Permanent: +{name_or_power} mana per turn")
            self.artifact_count += 1
        else:
            arti = ArtifactCard(f"Artifact {self.artifact_count}", 2,
                                "Legendary", 3, "Permanent: +2 mana per turn")
            self.artifact_count += 1
        self.cards.append(arti)
        return arti

    def create_themed_deck(self, size: int) -> dict:
        catalog = self.get_supported_types()

        counts = {
            "creatures": 0,
            "spells": 0,
            "artifacts": 0
        }

        deck_cards = []
        types = ["creature", "spell", "artifact"]

        for _ in range(size):
            election = random.choice(types)

            if election == "creature":
                name_selected = random.choice(catalog["creatures"])
                card = self.create_creature(name_selected)
                counts["creatures"] += 1

            elif election == "spell":
                name_selected = random.choice(catalog["spells"])
                card = self.create_spell(name_selected)
                counts["spells"] += 1

            elif election == "artifact":
                name_selected = random.choice(catalog["artifacts"])
                card = self.create_artifact(name_selected)
                counts["artifacts"] += 1

            deck_cards.append(card)

        return {
            "deck_name": "Fantasy Deck",
            "cards": [card.name for card in deck_cards],
            "counts": counts
        }

    def get_supported_types(self) -> dict:
        return {'creatures': ['dragon', 'goblin'],
                'spells': ['fireball'],
                'artifacts': ['mana_ring']
                }
