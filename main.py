# Proto-Game #3
# Version: prototype-1.4

from events import random_event
from player import player

print("\n=== Welcome to the Roguelike Prototype ===\n")

player_name_set = False
while not player_name_set:
    name = input("What's your name? ").strip()
    if name:
        player['Name'] = name
        player_name_set = True
    else:
        print("Please enter a valid name.")

while player["HP"] > 0:
    if player['Need_EXP'] <= player['EXP']:
        player['EXP'] -= player['Need_EXP']
        player['Level'] += 1
        player['Need_EXP'] += 50
        player['Max_HP'] += 10
        player['Max_Energy'] += 1
        player['ATK'] += 1
        player['Heal'] += 1
        player['HP'] = player['Max_HP']
        print('Level increased!')
    input("\nPress Enter to face your next challenge...")
    if player['HP'] > player['Max_HP']:
        player['HP'] = player['Max_HP']
    random_event()

    if player["HP"] <= 0:
        print("\nYou have died. Game Over.")
        input('')
        break