#!/usr/bin/python3

from ex0.Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        if (self.validate_attack(attack)):
            self._attack = attack
        else:
            raise ValueError("Attack value too small (must be > 0)")
        if (self.validate_health(health)):
            self._health = health
        else:
            raise ValueError("Health value too small (must be > 0)")
        return None

    @staticmethod
    def validate_health(health: int) -> bool:
        if (health > 0):
            return True
        return False

    @staticmethod
    def validate_attack(attack: int) -> bool:
        if (attack > 0):
            return True
        return False

    def get_card_info(self):
        infos = super().get_card_info()
        infos['type'] = self._type
        infos['attack'] = self._attack
        infos['health'] = self._health
        return infos

    def play(self, game_state: dict) -> dict:
        return {
            'card_played': self._name,
            'mana_used': self._cost,
            'effect': 'Creature summoned to battlefield'
            }

    def attack_target(self, target: "CreatureCard") -> dict:
        return {
            'attacker': self._name,
            'target': target._name,
            'damade_dealt': self._attack,
            'combat_resolved': True
            }
