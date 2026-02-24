from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name, cost, rarity, damage, health, combat_type):
        super().__init__(name, cost, rarity)
        self.damage = damage
        self.health = health
        self.combat_type = combat_type

    def play(self, game_state: dict) -> str:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Elite summoned"}

    def attack(self, target) -> dict:
        return {
            'attacker': self.name,
            'target': target,
            'damage': self.damage,
            'combat_type': self.combat_type
        }

    def defend(self, incoming_damage: int) -> dict:
        return {
            'defender': self.name,
            'damage_taken': incoming_damage,
            'damage_blocked': 3,
            'still_alive': True
        }

    def get_combat_stats(self) -> dict:
        return {
            "attack_points": self.damage,
            "health": self.health
            }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        return {
            'caster': self.name,
            'spell': spell_name,
            'targets': targets,
            'mana_used': 4
        }

    def channel_mana(self, amount: int) -> dict:
        return {
            'channeled': amount,
            'total_mana': self.cost + amount,
        }

    def get_magical_stats(self) -> dict:
        return {
            "magic_power": self.combat_type,
            "mana_pool": self.cost
        }
