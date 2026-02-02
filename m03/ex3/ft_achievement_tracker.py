def validate_player(name: str, achievements: set) -> None:
    """This function check for errors in the set"""
    if not isinstance(achievements, set):
        raise TypeError(f"{name} achievements must be a set")

    if not all(isinstance(a, str) for a in achievements):
        raise ValueError(f"{name} achievements must contain only strings")


def main() -> None:
    """This function takes processes the achievements of each player"""
    print("=== Achievement Tracker System ===\n")

    alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie = {'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon',
               'perfectionist'}

    try:
        validate_player("Alice", alice)
        validate_player("Bob", bob)
        validate_player("Charlie", charlie)
    except (TypeError, ValueError) as e:
        print(f"Invalid input detected: {e}")
        return

    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}\n")
    print("=== Achievement Analytics ===")
    all_achievements = alice.union(bob, charlie)

    common = alice.intersection(bob, charlie)
    alicebob = alice.intersection(bob)
    difalice = alice.difference(bob)
    difbob = bob.difference(alice)

    all_players = alice | bob | charlie

    shared_by_multiple = (
        (alice & bob) |
        (alice & charlie) |
        (bob & charlie)
        )
    rare = all_players - shared_by_multiple

    print(f"All unique achievements: {all_achievements}")
    print(f"Total unique achievements: {len(all_achievements)}\n")
    print(f"Rare achievements: {rare}\n")

    print(f"Common to all players: {common}\n")
    print(f"Alice vs bob: {alicebob}")
    print(f"Alice unique: {difalice}")
    print(f"Bob unique: {difbob}")


if __name__ == "__main__":
    main()
