from ex0.Card import Card


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type
        self.type = "Spell"

    def play(self, game_state: dict) -> dict:
        return {"card_played": self.name,
                "mana_used": self.cost,
                "effect": f"Spell cast {self.effect_type}"
                }

    def resolve_effect(self, targets: list) -> dict:
        output = {}

        if self.effect_type == "damage":
            output = {"targets": targets, "effect_type": "damage",
                      "result": "damage applied"}
        elif self.effect_type == "heal":
            output = {"targets": targets, "effect_type": "heal",
                      "result": "heal applied"}
        elif self.effect_type == "buff":
            output = {"targets": targets, "effect_type": "damage",
                      "result": "buff applied"}
        else:
            output = {"targets": targets, "effect_type": "damage",
                      "result": "debuff applied"}

        return output
