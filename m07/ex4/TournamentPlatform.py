from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self):
        self.cards = []
        self.matches = 0

    def register_card(self, card: TournamentCard) -> str:
        self.cards.append(card)
        return f"{card.name} (ID: {card.id}):\n\
- Interfaces: [Card, Combatable, Rankable]\n\
- Rating: {card.rating}\n\
- Record: {card.wins}-{card.loses}"

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        self.matches += 1
        win_r = -1
        los_r = -1
        for card in self.cards:
            if card.id == card1_id:
                card.rating += 16
                win_r = card.rating
                card.wins += 1
            if card.id == card2_id:
                card.rating -= 16
                card.loses += 1
                los_r = card.rating
        return {
            'winner': card1_id,
            'looser': card2_id,
            'winner_rating': int(win_r),
            'loser_rating': int(los_r)
        }

    def get_leaderboard(self) -> list:
        self.cards.sort(key=lambda x: x.rating, reverse=True)
        return self.cards

    def generate_tournament_report(self) -> dict:
        sum = 0
        for card in self.cards:
            sum += card.rating
        return {
            'total_cards': len(self.cards),
            'matches_played': self.matches,
            'avg_rating': sum / len(self.cards),
            'platform_status': 'active',
        }


# class TournamentPlatform:
#     def register_card(self, card: TournamentCard) -> str:

#     def create_match(self, card1_id: str, card2_id: str) -> dict:

#     def get_leaderboard(self) -> list:

#     def generate_tournament_report(self) -> dict:
