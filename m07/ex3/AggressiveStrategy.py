from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def __init__(self):
        self.name = "Aggressive Strategy"
        self.prioritize_targets = []

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        played_cards = []
        damage_dealt = 0

        return {
            "cards_played": played_cards,
            "mana_used": 0,
            "targets_attacked": ["Enemy Player"],
            "damage_dealt": damage_dealt,
        }

    def get_strategy_name(self) -> str:
        return self.name

    def prioritize_targets(self, available_targets: list) -> list:
        return available_targets.sort()
