def get_score(player: dict) -> dict:
    """This function returns the player's score"""
    return player["score"]


def combine_analysis(players: dict) -> None:
    """This function calculates combined information"""
    all_players = [p["name"] for p in players]
    print("Total players:", len(all_players))

    total_unique_achievements = {achievement for p in players
                                 for achievement in p["achievement"]
                                 if p["active"] == "yes"}
    print("Total unique achievements:", len(total_unique_achievements))

    scores = [p["score"] for p in players]
    print("Average Score:", (sum(scores) / 4))

    top_performer = max(players, key=get_score)
    print("Top performer:", top_performer["name"], end=" (")
    print(top_performer["score"], end=" points, ")
    print(len(top_performer["achievement"]), "achievements)")


def list_comprehension(players: dict) -> None:
    """This function calculates list information"""
    high_scores = [p["name"] for p in players if p["score"] >= 2000]
    print("High scorers (>2000):", high_scores)

    bonus_scores = [p["score"] * 2 for p in players]
    print("Scores doubled:", bonus_scores)

    active_players = [p["name"] for p in players if p["active"] == "yes"]
    print("Active players:", active_players)


def dict_comprehension(players: dict) -> None:
    """This function calculates dictionary information"""
    player_dict = {p["name"]: p["score"] for p in players}
    print("Name to score mapping:", player_dict)

    score_category_counts = {
        "high": len([p for p in players if p["score category"] >= 3]),
        "medium": len([p for p in players if p["score category"] == 2]),
        "low": len([p for p in players if p["score category"] == 1])
    }

    print("Player's score category:", score_category_counts)

    count_achievements = {
        p["name"]: len(p["achievement"])
        for p in players if p["active"] == "yes"
    }
    print("Elite player achievements:", count_achievements)


def set_comprehension(players: dict) -> None:
    """This function generates set and performs analysis"""
    player_name = {p["name"] for p in players}
    print("Unique players:", player_name)

    unique_achievements = {achievement for p in players
                           for achievement in p["achievement"]
                           if p["active"] == "yes"}

    print(f"Unique achievements {unique_achievements}")

    active_regions = {p["region"] for p in players}
    print(f"Active regions: {active_regions}")


def main() -> None:
    players = [
        {"name": "alice", "score": 2300, "active": "yes",
         "achievement": ['first_kill', 'level_10', 'treasure_hunter',
                         'speed_demon'],
            "score category": 3, "region": "north"},
        {"name": "bob", "score": 1800, "active": "yes",
         "achievement": ['first_kill', 'level_10', 'boss_slayer', 'collector'],
         "score category": 2, "region": "south"},
        {"name": "charlie", "score": 2150, "active": "yes",
         "achievement": ['level_10', 'treasure_hunter', 'boss_slayer',
                         'speed_demon', 'perfectionist'], "score category": 5,
            "region": "east"},
        {"name": "diana", "score": 2050, "active": "no",
         "achievement": ['level_10', 'treasure_hunter', 'collector',
                         'speed_demon'],
            "score category": 1, "region": "east"}
        ]
    print("=== Game Analytics Dashboard ===\n")
    print("=== List comprehension examples ===")
    list_comprehension(players)
    print("\n=== Dictionary comprehension examples ===")
    dict_comprehension(players)
    print("\n=== Set Comprehension Examples ===")
    set_comprehension(players)
    print("\n=== Combined Analisis ===")
    combine_analysis(players)


if __name__ == "__main__":
    main()
