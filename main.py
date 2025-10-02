# Proto-Game #3
# Version: IDK

import random
from player import player
from events import random_event
from save_load import save_game, load_game
from player_upgrade_actions import player_upgrade_actions

border = 9
a = round(border * 0.5)

if player['Location_x'] == 0 and player['Location_y'] == 0:
    player['X'] = a
    player['Y'] = a

def clear():
    print("\033c", end="")

def basic_view():
    board = []
    for _ in range(border):
        row = ["*" for _ in range(border)]
        board.append(row)
    return board

def visual(board):
    for row in board:
        print("".join(row))


events = []

def event_spawn():
    global events
    events = []

    spawn_probability = 0.06

    for y in range(border):
        for x in range(border):
            if x == player['X'] and y == player['Y']:
                continue

            seed_value = (player['Location_x'] * 1000 + x) * 1000 + (player['Location_y'] * 1000 + y)
            random.seed(seed_value)

            if random.random() < spawn_probability:
                events.append((x, y))


def move(move_input):
    if move_input == "w":
        player['Y'] -= 1
    elif move_input == "s":
        player['Y'] += 1
    if move_input == "a":
        player['X'] -= 1
    elif move_input == "d":
        player['X'] += 1


    if player['X'] >= border:
        player['X'] = 0
        player['Location_x'] += 1
    if player['X'] < 0:
        player['X'] = border - 1
        player['Location_x'] -= 1
    if player['Y'] >= border:
        player['Y'] = 0
        player['Location_y'] += 1
    if player['Y'] < 0:
        player['Y'] = border - 1
        player['Location_y'] -= 1

    global events
    new_events_list = []

    for ex, ey in events:
        if player['X'] == ex and player['Y'] == ey:
            random_event()
        else:
            new_events_list.append((ex, ey))
    events = new_events_list


def location():
    if player['Old_Location_x'] != player['Location_x'] or player['Old_Location_y'] != player['Location_y']:
        print("New location")
        player['Old_Location_x'] = player['Location_x']
        player['Old_Location_y'] = player['Location_y']

        event_spawn()

def main_game_loop():
    move_input = 1
    while player['HP'] > 0:
        while player['Need_EXP'] <= player['EXP']:
            if player['Need_EXP'] <= player['EXP']:
                player['EXP'] -= player['Need_EXP']
                player['Level'] += 1
                player['Need_EXP'] += 50
                player['Max_HP'] += 10
                player['Max_Energy'] += 1
                player['ATK'] += 1
                player['Heal'] += 1
                player['SPoint'] += player['SPoint_Add'] + player['SPoint_Add'] * player['Level']
                player['Energy'] = player['Max_Energy']
                player['HP'] = player['Max_HP']
                print('---Level increased!---')

        if player['HP'] > player['Max_HP']:
            player['HP'] = player['Max_HP']

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
        clear()
        board = basic_view()
        move(move_input)
        location()

        for ex, ey in events:
            board[ey][ex] = "!"

        board[player['Y']][player['X']] = "@"
        print(f"X: {player['Location_x']}, Y: {player['Location_y']}")
        visual(board)
        move_input = input("").lower()

        if move_input == "save":
            clear()
            save_game()
        elif move_input == "load":
            clear()
            load_game()
            event_spawn()

clear()
load_choice = input("Load previous game? (yes/no): ").lower()
game_loaded = False

if load_choice == 'yes':
    game_loaded = load_game()
    if not game_loaded:
        pass
    else:
        event_spawn()
else:
    print("\nStarting a new game.")

if not game_loaded:
    clear()
    player_name_set = False

    while not player_name_set:
        name = input("What's your name? ").strip()
        clear()

        if name:
            player['Name'] = name
            player_name_set = True
        else:
            print("Please enter a valid name.")
    clear()
    print("Chose your class")
    print("Tank -        ++HP, +ATK, +Heal             | -Energy")
    print("Attacker -    +++ATK, +Energy               | -HP")
    print("Mage -        ++Magic, +Energy, +SPoints    | -ATK")
    print("Necromancer - +Magic, ++Necromance, +MHeal  | -HP")
    print("Adventurer -  +++SPoints")

    valid_actions = ["tank", "attacker", "mage", "necro", "necromancer", "adventurer", "adven"]
    caction = 0

    while caction not in valid_actions:
        print()
        caction = input("Chose your class: ").lower()
        if caction not in valid_actions:
            print("Invalid action. Please choose from the list.")


    if caction == "tank":
        player['SPoint'] -= 90
        player['HP'] += 60
        player['ATK'] += 3
        player['Heal'] += 3
        player['Max_Energy'] -= 3
    elif caction == "attacker":
        player['SPoint'] -= 90
        player['ATK'] += 9
        player['Max_Energy'] += 3
        player['Max_HP'] -= 30
    elif caction == "mage":
        player['SPoint'] -= 60
        player['IMagic'] += 3
        player['Energy'] += 3
        player['ATK'] -= 3
    elif caction == "necromancer" or caction == "necro":
        player['SPoint'] -= 90
        player['IMagic'] += 1.5
        player['INecro'] += 6
        player['IMHeal'] += 3
        player['Max_HP'] -= 30
    clear()

    if player['SPoint'] > 0:
        print(f"You have {player['SPoint']} SPoints.")
        print("Do you want to youse your SPoints? (yes/no)")
        yes_input = input("").lower()
        if yes_input == "yes":
            player_upgrade_actions(0,0,0,0)

    player['Energy'] = player['Max_Energy']
    player['HP'] = player['Max_HP']
clear()
main_game_loop()
