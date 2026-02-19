from abc import ABC, abstractmethod


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self._name = name
        self._cost = cost
        self._rarity = rarity
        self._type = 'Creature'
        return None

    @abstractmethod
    def play(self, game_state: dict) -> str:
        pass

    def get_card_info(self) -> dict:
        return {
            'name': self._name,
            'cost': self._cost,
            'rarity': self._rarity,
        }

    def is_playable(self, available_mana: int) -> bool:
        if (available_mana >= self._cost):
            return True
        return False
