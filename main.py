# Proto-Game #3
# Version: prototype-1.5

from events import random_event
from player import player
from save_load import save_game, load_game

print("\n=== Welcome to the Roguelike Prototype ===\n")

load_choice = input("Load previous game? (yes/no): ").lower()
game_loaded = False
if load_choice == 'yes':
    game_loaded = load_game()
    if not game_loaded:
        pass
else:
    print("Starting a new game.")

if not game_loaded:
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
    else:
        print()
    if player['HP'] > player['Max_HP']:
        player['HP'] = player['Max_HP']

    print("\nPress Enter to face your next challenge, or type 'save' / 'load'.")
    user_action = input().lower()

    if user_action == "save":
        save_game()
    elif user_action == "load":
        load_game()
    else:
        random_event()

    if player["HP"] <= 0:
        print("\nYou have died. Game Over.")
        print("If you want load save - type 'load'")
        user_action = input().lower()
        if user_action == "load":
            load_game()
            print("Game loaded!")
        else:
            break