# Proto-Game #3
# Version: prototype-IDK

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
    print("\nStarting a new game.")

if not game_loaded:
    player_name_set = False
    while not player_name_set:
        name = input("What's your name? ").strip()
        if name:
            player['Name'] = name
            player_name_set = True
        else:
            print("\nPlease enter a valid name.")
    print("\nChose your class")
    print("Tank -        ++HP, +ATK")
    print("Attacker -    +++ATK")
    print("Mage -        ++Magic, +Energy")
    print("Necromancer - +Magic, ++Necromance")
    print("Adventurer -  +++SPoints")
    
    valid_actions = ["tank", "attacker", "mage", "necro", "necromancer", "adventurer", "adven"]
    caction = 0
    while caction not in valid_actions:
        print("")
        caction = input("Chose your class: ").lower()
        if caction not in valid_actions:
            print("Invalid action. Please choose from the list.")
    print("")

    if caction == "tank":
        player['HP'] += 70
        player['SPoint'] -= 100
        player['ATK'] += 3
    elif caction == "attacker":
        player['SPoint'] -= 100
        player['ATK'] += 10
    elif caction == "mage":
        player['SPoint'] -= 100
        player['IMagic'] += 3.5
        player['Energy'] += 3
    elif caction == "necromancer" or caction == "necro":
        player['SPoint'] -= 100
        player['IMagic'] += 1.5
        player['INecro'] += 7  
    print("You succesfull choise a class!")

while player["HP"] > 0:
    while player['Need_EXP'] <= player['EXP']:
        if player['Need_EXP'] <= player['EXP']:
            player['EXP'] -= player['Need_EXP']
            player['Level'] += 1
            player['Need_EXP'] += 50
            player['Max_HP'] += 10
            player['Max_Energy'] += 1
            player['ATK'] += 1
            player['Heal'] += 1
            player['UPoint'] += 5
            player['Energy'] = player['Max_Energy']
            player['HP'] = player['Max_HP']
            print('---Level increased!---')
        else:
            break
    print()
        
    if player['HP'] > player['Max_HP']:
        player['HP'] = player['Max_HP']

    print("Press Enter to face your next challenge, or type 'save' / 'load'")
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
            continue
        else:
            break