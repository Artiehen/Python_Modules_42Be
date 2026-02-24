from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy
        self.turns = 0
        self.damage = 8
        print(f"Factory: {type(self.factory).__name__}")
        print(f"Strategy: {type(self.strategy).__name__}")

    def simulate_turn(self) -> dict:
        print(f"Strategy: {type(self.strategy).__name__}")
        dict = {
            'cards_played': [],
            'mana_used': 0,
            'targets_attacked': 'Enemy Player',
            'damage_dealt': 0
        }
        for card in self.factory.cards:
            play = card.play({})
            dict['cards_played'].append(play['card_played'])
            dict['mana_used'] += play['mana_used']
            dict['damage_dealt'] = self.damage
        self.turns += 1
        return dict

    def get_engine_status(self) -> dict:
        return {
            'turns_simulated': self.turns,
            'strategy_used': type(self.strategy).__name__,
            'total_damage': self.damage,
            'cards_created': len(self.factory.cards)
        }
