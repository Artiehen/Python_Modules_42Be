# -------------------------------
# Sample Gaming Data
# -------------------------------

players = [
    {"name": "Alex", "score": 1200, "level": "pro", "achievement": "Sharpshooter"},
    {"name": "Blake", "score": 800, "level": "casual", "achievement": "First Blood"},
    {"name": "Casey", "score": 1500, "level": "pro", "achievement": "Unstoppable"},
    {"name": "Dana", "score": 400, "level": "casual", "achievement": "First Blood"},
    {"name": "Evan", "score": 950, "level": "casual", "achievement": "Survivor"},
]

# -------------------------------
# List Comprehensions
# -------------------------------

# 1. Filter players with high scores
high_scores = [p["name"] for p in players if p["score"] >= 1000]
print("High scoring players:", high_scores)

# 2. Transform scores by adding bonus points
bonus_scores = [p["score"] + 100 for p in players]
print("Bonus scores:", bonus_scores)

# 3. Create formatted player summaries
summaries = [p["name"] + " scored " + str(p["score"]) for p in players]
print("Player summaries:", summaries)

# -------------------------------
# Dict Comprehensions
# -------------------------------

# 4. Map player names to scores
name_to_score = {p["name"]: p["score"] for p in players}
print("Name to score mapping:", name_to_score)

# 5. Count players by level
level_counts = {
    level: len([p for p in players if p["level"] == level])
    for level in {p["level"] for p in players}
}
print("Player count by level:", level_counts)

# 6. Map high-scoring players to their achievements
elite_achievements = {
    p["name"]: p["achievement"]
    for p in players
    if p["score"] >= 1000
}
print("Elite player achievements:", elite_achievements)

# -------------------------------
# Set Comprehensions
# -------------------------------

# 7. Find unique player levels
unique_levels = {p["level"] for p in players}
print("Unique levels:", unique_levels)

# 8. Find unique achievements
unique_achievements = {p["achievement"] for p in players}
print("Unique achievements:", unique_achievements)

# 9. Find unique players with scores above 900
top_players = {p["name"] for p in players if p["score"] > 900}
print("Top players:", top_players)
