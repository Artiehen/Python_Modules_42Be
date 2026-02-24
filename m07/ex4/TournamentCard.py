from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int,
                 rarity: str, wins: int, loses: int, rating: int, id: str):
        super().__init__(name, cost, rarity)
        self.wins = wins
        self.loses = loses
        self.rating = rating
        self.id = id
        self.combat_stats = {"attacks": 0, "defends": 0}

    def play(self, game_state: dict) -> dict:
        if self.is_playable(game_state["available_mana"]):
            play_results = {
                "card_played": self.name,
                "mana_used": self.cost
            }
            game_state["available_mana"] -= self.cost
            return play_results
        else:
            return {}

    def attack(self, target) -> dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.attack_power,
            "action": "attack",
            "attacker_health": self.health,
        }

    def defend(self, incoming_damage: int) -> dict:
        incoming_damage -= 3 if incoming_damage - 3 > 0 else incoming_damage
        if self.health - incoming_damage > 0:
            self.health -= incoming_damage
        else:
            self.health = 0
            defense_results = {
                "defender": self.name,
                "damage_taken": incoming_damage,
                "damage_blocked": 3,
                "still_alive": self.health > 0
            }
            self.combat_stats["defends"] += 1
        return (defense_results)

    def calculate_rating(self) -> int:
        return self.rating + sum(self.matches)

    def get_tournament_stats(self) -> dict:
        wins = self.wins
        losses = self.losses
        rating = self.calculate_rating()
        return {
            "Username": f"{self.name} (ID: {self.id})",
            "Interfaces": ["Card", "Combatable", "Rankable"],
            "Rating": rating,
            "Record": f"{wins}-{losses}"
        }

    def get_combat_stats(self) -> dict:
        return self.combat_stats

    def update_wins(self, wins: int) -> None:
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        self.update_losses += losses

    def get_rank_info(self) -> dict:
        return {
            "wins": self.wins,
            "losses": self.update_losses
        }
