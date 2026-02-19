from ex0.CreatureCard import CreatureCard

print('')

print('=== DataDeck Card Foundation ===')

print('')

print('Testing Abstract Base Class Design:')

print('')

print('CreatureCard Info:')
fire_dragon = CreatureCard(
    name='Fire Dragon',
    cost=5,
    rarity='Legendary',
    attack=7,
    health=5)
print(fire_dragon.get_card_info())

print('')

mana = 6
print(f'Playing {fire_dragon._name} with {mana} mana available:')
print(f"Playable: {fire_dragon.is_playable(mana)}")
print(f"Play result: {fire_dragon.play({})}")

print('')

print('Fire Dragon attacks Goblin Warrior:')
goblin_warrior = CreatureCard(
    name='Goblin Warrior',
    cost=5,
    rarity='Legendary',
    attack=7,
    health=5)
print(f'Attack result: {fire_dragon.attack_target(goblin_warrior)}')

print('')

mana = 3
print(f'Testing insufficient mana ({mana} available)')
print(f"Playable: {fire_dragon.is_playable(mana)}")

print('')

print('Abstract pattern successfully demonstrated!')
