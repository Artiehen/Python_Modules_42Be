# -------------------------------
# Sample Gaming Data
# -------------------------------



# -------------------------------
# List Comprehensions
# -------------------------------
def list_comprehension(players):

    print("=== Game Analytics Dashboard ===\n")
    print("=== List comprehension examples ===")
    # 1. Filter players with high scores
    high_scores = [p["name"] for p in players if p["score"] >= 2000]
    print("High scorers (>2000):", high_scores)

    # 2. Transform scores by adding bonus points
    bonus_scores = [p["score"] * 2 for p in players]
    print("Scores doubled:", bonus_scores)

    # 3. Create new list for active players

    active_players = [p["name"] for p in players if p["active"] == "yes"]
    print("Active players:", active_players)

    # # 3. Create formatted player summaries
    # summaries = [p["name"] + " scored " + str(p["score"]) for p in players]
    # print("Player summaries:", summaries)

# # -------------------------------
# # Dict Comprehensions
# # -------------------------------
def dict_comprehension(players):
    print("\n=== Dictionary comprehension examples ===")

    # 4. Map player names to scores
    player_dict = {p["name"]: p["score"] for p in players}
    print("Name to score mapping:", player_dict)

    # 5. Count players by level
    score_category_counts = {
        "high": len([p for p in players if p["score category"] >= 3]),
        "medium": len([p for p in players if p["score category"] == 2]),
        "low": len([p for p in players if p["score category"] == 1])
    }

    print("Player's score category:", score_category_counts)

    # 6. Map high-scoring players to their achievements
    count_achievements = {
        p["name"]: len(p["achievement"])
        for p in players if p["active"] == "yes"
    }
    print("Elite player achievements:", count_achievements)


def set_comprehension(players):
    print("\n=== Set Comprehension Examples ===")

    # 7. Find unique player levels
    player_name = {p["name"] for p in players}
    print("Unique players:", player_name)

    # # 8. Find unique achievements
    unique_achievements = {achievement for p in players
                        for achievement in p["achievement"]
                        if p["active"] == "yes"}

    print(f"Unique achievements {unique_achievements}")

    active_regions = {p["region"] for p in players}
    print(f"Active regions: {active_regions}")

def main():
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
        "score category": 1, "region": "west"}
        ]
    print("=== Game Analytics Dashboard ===\n")
    print("=== List comprehension examples ===")
    list_comprehension(players)
    print("\n=== Dictionary comprehension examples ===")
    dict_comprehension(players)
    print("\n=== Set Comprehension Examples ===")
    set_comprehension(players)
    print("\n=== Combined Analisis ===")


if __name__ == "__main__":
    main()
