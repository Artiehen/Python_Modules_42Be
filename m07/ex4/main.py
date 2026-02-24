from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main():
    try:
        print("\n=== DataDeck Tournament Platform ===\n")

        print("Registering Tournament Cards...\n")
        platform = TournamentPlatform()
        dragon = TournamentCard(
            name="Fire Dragon",
            cost=5,
            rarity=8,
            wins=0,
            loses=0,
            rating=1200,
            id="dragon_001"
        )
        wizard = TournamentCard(
            name="Ice Wizard",
            cost=5,
            rarity=8,
            wins=0,
            loses=0,
            rating=1150,
            id="wizard_001"
        )
        print(platform.register_card(dragon))
        print(platform.register_card(wizard))

        print("\nCreating tournament match...\n")

        x = "Match result: "
        print(f'{x}{platform.create_match('dragon_001', 'wizard_001')}')

        print("\nTournament Leaderboard:")
        i = 1
        cards = platform.get_leaderboard()
        for card in cards:
            print(f"{i}: {card.name} - Rating: {card.rating} ({
                card.wins}-{card.loses})")
            i += 1

        print('')

        print('Platform Report:')
        print(platform.generate_tournament_report())

        print('')

        print('=== Tournament Platform Successfully Deployed! ===')
        print('All abstract patterns working together harmoniously!')
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
